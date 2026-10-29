"""
Stage 2: the reading record and the checks that run before any model is asked
anything. Version 4.

THE RECORD
----------
A reading is a wager in five fields, as specified in PROPOSAL_sep_2.md:

    statement · seed fragments by ID · what it would take to cohere ·
    what it strains against · who could complete it

For a fission reading the split card IS the wager: the card's deciding
observation is the "what it would take to cohere" field, so there is one record
type rather than two that drift apart.

THE CHECKS
----------
Three of the six attack modes are decided mechanically, before a model is
involved, because a language model should never be asked to do what a lookup can
do:

    A  provenance    every cited fragment exists in the corpus
    C  role vacuity  no fragment is given a job that says nothing
    F  discrimination the deciding observation names something checkable

One more is a MEASUREMENT rather than a kill, renamed from D_incumbent_equiv:

    restatement      does the reading use any fragment in a way the incumbent
                     does not? Only a reading that uses nothing differently
                     fails. Divergence is measured, never required.

Modes B (import) and E (contradiction) are model-judged and are NOT run here.
They require a session that has never seen the reasoning that produced the
reading, which by construction is not the session that wrote it.

SPLIT ADMISSIBILITY
-------------------
Three conditions, reported and never scored:

  1. a separating feature, independent of the outcome, that sorts the fragments
  2. reach: something outside the seam's own fragments reads differently
  3. a deciding observation that would tell this split from its rival

How cleanly the feature sorts is REPORTED. No pass mark: a cut-off would be one
more guessed number. A failing split is kept in the record, marked as failing.
"""

import json
import sys
from schema import load, Corpus

VACUOUS = ("provides context", "illustrates the tension", "supports the argument",
           "is relevant", "shows the importance", "adds colour", "is background",
           "demonstrates the point", "reflects the theme")


def _ids(card):
    out = set(card["wager"]["seed_fragments"])
    sp = card.get("split") or {}
    for side in ("side_x", "side_y"):
        out |= set(sp.get(side, {}).get("fragments", []))
    for v in (card.get("reach") or {}).values():
        out |= {x for x in v if x.startswith("F")}
    out |= set((card.get("fragment_jobs") or {}).keys())
    for g in card.get("grounded_in") or []:
        for item in g.get("items", []):
            head = str(item).split()[0] if str(item).strip() else ""
            if head.startswith("F"):
                out.add(head)
    d = (card.get("wager") or {}).get("what_it_would_take_to_cohere") or {}
    out |= set(d.get("printed_fragments") or [])
    return sorted(out)


def check_provenance(card, c: Corpus) -> dict:
    """Mode A. No new content enters. A required fact not in the corpus is a
    research question, never a citation."""
    known = {f.fragment_id for f in c.fragments}
    cited = _ids(card)
    missing = [x for x in cited if x not in known]
    claims = {x.claim_id for x in c.claims}
    bad_claims = [x for x in [card.get("claim")] + (card.get("reach", {}).get("same_construct", []) +
                  card.get("reach", {}).get("same_outcome", []))
                  if x and x.startswith("C") and x not in claims]
    return {"mode": "A_provenance", "killed": bool(missing or bad_claims),
            "cited_fragments": len(cited), "unknown_fragments": missing,
            "unknown_claims": bad_claims}


def check_role_vacuity(card, c: Corpus) -> dict:
    """Mode C. A fragment given a job that says nothing has not been used."""
    jobs = card.get("fragment_jobs") or {}
    vacuous = [k for k, v in jobs.items()
               if any(p in v.lower() for p in VACUOUS) or len(v.split()) < 4]
    unjobbed = [x for x in _ids(card) if x not in jobs]
    return {"mode": "C_role_vacuity", "killed": bool(vacuous),
            "vacuous_jobs": vacuous, "fragments_without_a_job": unjobbed}


def check_discrimination(card, c: Corpus) -> dict:
    """Mode F. The deciding observation must name something a person could go and
    check: either fragments the paper printed, or a stated absence."""
    d = card["wager"].get("what_it_would_take_to_cohere") or {}
    named = bool((d.get("observation") or "").strip())
    printed = d.get("printed")
    cites = d.get("printed_fragments") or []
    ok = named and (printed is True and cites or printed is False and d.get("basis"))
    return {"mode": "F_discrimination", "killed": not ok, "observation_named": named,
            "printed": printed, "fragments": cites,
            "note": ("names printed evidence" if printed else
                     "names an absence with a basis" if ok else
                     "does not name anything checkable")}


REQUIRED = ["card_id", "paper_id", "move", "trigger", "claim", "incumbent_reading",
            "wager", "fragment_jobs", "grounded_in"]
WAGER_FIELDS = ["statement", "seed_fragments", "what_it_would_take_to_cohere",
                "strains_against", "who_could_complete_it"]


def check_record(card, c: Corpus) -> dict:
    """An incomplete record cannot be judged. Mechanical, before anything else."""
    missing = [k for k in REQUIRED if not card.get(k)]
    missing += [f"wager.{k}" for k in WAGER_FIELDS
                if not (card.get("wager") or {}).get(k)]
    if card.get("move") == "construct_fission" and not card.get("split"):
        missing.append("split")
    return {"mode": "record", "killed": bool(missing), "missing_fields": missing}


def check_grounding(card, c: Corpus) -> dict:
    """Mode G: the doubt condition. A reading must name at least one missing fact
    that bears on a named claim, with both readings of it written out, or one
    divergence between two printed items. Checked for structure here; whether the
    fact is really missing is mode B's business, since asserting it is an import."""
    claims = {x.claim_id for x in c.claims}
    ok, problems = [], []
    for g in card.get("grounded_in") or []:
        if g.get("kind") == "missing_fact":
            need = [k for k in ("question", "bears_on", "if_one_way", "if_the_other")
                    if not (g.get(k) or "").strip()]
            if g.get("bears_on") and g["bears_on"] not in claims:
                need.append(f"bears_on {g['bears_on']} is not a claim")
            if not need and g["if_one_way"].strip() == g["if_the_other"].strip():
                need.append("both readings identical: fails the two-sentence test")
            (problems if need else ok).append((g.get("question", "?")[:60], need))
        elif g.get("kind") == "divergence":
            items = [i for i in g.get("items", []) if str(i).startswith("F")]
            need = [] if len(items) >= 2 and (g.get("how") or "").strip() else \
                ["a divergence needs two printed items and how they diverge"]
            (problems if need else ok).append((", ".join(map(str, items)), need))
        else:
            problems.append((str(g)[:60], ["kind must be missing_fact or divergence"]))
    return {"mode": "G_grounding", "killed": not ok,
            "grounds_accepted": [x[0] for x in ok],
            "grounds_rejected": problems}


def measure_restatement(card, c: Corpus) -> dict:
    """Not a kill: a measurement. Does the reading use any fragment in a way the
    incumbent does not? Computed from the corpus, not judged.

    Three ways a use can be new: a fragment the incumbent attached to nothing; a
    fragment the reading moves to a different claim; and a fragment the incumbent
    filed under a claim it runs AGAINST, which the reading now gives a job to.
    """
    new_uses, same = [], []
    for fid in _ids(card):
        links = c.links_by_fragment(fid)
        if not links:
            new_uses.append((fid, "orphan in the corpus, given a job here"))
            continue
        incumbent_claims = {l.claim_id for l in links}
        against = [l.claim_id for l in links if l.direction == "against"]
        if card.get("claim") and card["claim"] in incumbent_claims and fid in against:
            new_uses.append((fid, f"ran against {card['claim']} for the incumbent; "
                                  "re-sorted into a second bin here"))
        elif card.get("claim") and card["claim"] not in incumbent_claims:
            new_uses.append((fid, f"the incumbent files it under "
                                  f"{','.join(sorted(incumbent_claims))}, not {card['claim']}"))
        else:
            same.append(fid)
    return {"measure": "restatement", "failed": not new_uses,
            "new_uses": new_uses, "used_as_incumbent_does": same,
            "share_new": round(len(new_uses) / max(1, len(_ids(card))), 3)}


def report_admissibility(card, c: Corpus) -> dict:
    if card.get("move") != "construct_fission":
        return {"applies": False}
    sp = card.get("split") or {}
    sorted_n = sp.get("sorts_correctly")
    total = len(sp.get("side_x", {}).get("fragments", [])) + \
        len(sp.get("side_y", {}).get("fragments", []))
    reach = card.get("reach") or {}
    reach_hits = {k: v for k, v in reach.items() if v}
    d = card["wager"].get("what_it_would_take_to_cohere") or {}
    return {"separating_feature": sp.get("separating_feature"),
            "feature_independent_of_outcome": sp.get("independent_of_outcome"),
            "sorts": f"{sorted_n} of {total}",
            "confounds": sp.get("confounds", []),
            "reach": reach_hits,
            "reach_routes_firing": f"{len(reach_hits)} of 4",
            "deciding_observation": d.get("observation"),
            "rival": card.get("rival"),
            "note": "Reported, not scored. No pass mark is set on any of the three."}


def run(card, c: Corpus) -> dict:
    checks = [check_record(card, c), check_provenance(card, c),
              check_role_vacuity(card, c), check_discrimination(card, c),
              check_grounding(card, c)]
    return {"card_id": card["card_id"], "paper_id": card["paper_id"],
            "move": card["move"], "claim": card.get("claim"),
            "mechanical_checks": checks,
            "killed_by": [k["mode"] for k in checks if k["killed"]],
            "restatement": measure_restatement(card, c),
            "admissibility": report_admissibility(card, c),
            "not_run_here": ["B_import", "E_contradiction"],
            "why_not_run": "model-judged; they require a session that has never "
                           "seen the reasoning that produced this reading",
            "register": ("not opened" if not (card.get("naming") or {}).get("register_version")
                         else card["naming"]["register_version"])}


def text(r: dict) -> str:
    L = [f"STAGE 2 CHECKS  --  {r['card_id']}  ({r['move']} on {r['claim']})", ""]
    for k in r["mechanical_checks"]:
        L.append(f"  {k['mode']:<20} {'KILLED' if k['killed'] else 'clear'}")
        for f, v in k.items():
            if f in ("mode", "killed") or not v:
                continue
            L.append(f"      {f}: {v}")
    m = r["restatement"]
    L += ["", f"  restatement          {'FAILED -- no new use of evidence' if m['failed'] else 'measured, not a kill'}",
          f"      new uses {len(m['new_uses'])} of {len(m['new_uses']) + len(m['used_as_incumbent_does'])}"
          f"   share {m['share_new']}"]
    for fid, why in m["new_uses"]:
        L.append(f"      {fid}: {why}")
    a = r["admissibility"]
    if not a.get("applies", True):
        L += ["", f"  modes not run here: {', '.join(r['not_run_here'])}",
              f"  register: {r['register']}"]
        return "\n".join(L)
    L += ["", "  SPLIT ADMISSIBILITY (reported, never scored)",
          f"      feature: {a['separating_feature']}",
          f"      independent of the outcome: {a['feature_independent_of_outcome']}",
          f"      sorts: {a['sorts']}",
          f"      reach routes firing: {a['reach_routes_firing']}"]
    for k, v in a["reach"].items():
        L.append(f"         {k}: {', '.join(v)}")
    for cfd in a["confounds"]:
        L.append(f"      CONFOUND: {cfd}")
    L += [f"      rival: {a['rival']}", "",
          f"  modes not run here: {', '.join(r['not_run_here'])}",
          f"      {r['why_not_run']}",
          f"  register: {r['register']}"]
    return "\n".join(L)


# ------------------------------------------------------------ attack copy
# attack.md: the attacker is given the corpus and one finished wager, and is NOT
# given the reasoning that produced it. These fields are that reasoning. Removing
# them by hand each time is how a stray field eventually gets through.
#
# What stays, and why: the five wager fields are the wager; `strains_against`
# stays because mode E distinguishes declared strain from undeclared
# contradiction and cannot do that if the declarations are removed;
# `fragment_jobs` stays because mode B names the carrying fragment for each
# assertion; the `reach` ID lists stay because they are claims the reading makes.
ATTACK_STRIP = [
    "rival",                        # the author's own best counter-argument
    "provenance",                   # which codings are contested, and by whom
    "reach_notes",                  # the author weighing what reach is worth
    "naming",                       # register bookkeeping and check status
    "status",
    "written_before_register_opened",
    "split.confounds",              # the author's account of the split's weaknesses
    "split.independent_of_outcome",  # the author's self-assessment of the feature
    "split.feature_source",         # how the feature was arrived at
    "split.sorts_correctly",        # the author's own result; the attacker can count
]


def for_attack(card: dict):
    """Return (stripped copy, list of fields actually removed).

    The list is for the author's audit trail and is printed, never written into
    the copy: telling an attacker that a field called `rival` was removed is
    telling them there is a rival.
    """
    out = json.loads(json.dumps(card))
    removed = []
    for path in ATTACK_STRIP:
        node, *rest = path.split(".")
        if not rest:
            if node in out:
                out.pop(node)
                removed.append(path)
        elif isinstance(out.get(node), dict) and rest[0] in out[node]:
            out[node].pop(rest[0])
            removed.append(path)
    out["for_attack"] = True
    return out, removed


if __name__ == "__main__":
    if sys.argv[1] == "--for-attack":
        card = json.load(open(sys.argv[2]))
        stripped, removed = for_attack(card)
        out_path = sys.argv[3]
        json.dump(stripped, open(out_path, "w"), indent=2)
        print(f"wrote {out_path}")
        print(f"  removed {len(removed)}: {', '.join(removed)}")
        print(f"  kept: the five wager fields, split sides and separating feature, "
              f"fragment_jobs, reach")
        print("  Give the attacker this file, the corpus, and attack.md. Nothing else.")
        print("  Modes to run: B (import) and E (contradiction) only. A, C and F are "
              "decided mechanically and D is now the restatement measurement.")
        raise SystemExit(0)

    card = json.load(open(sys.argv[1]))
    corpus = load(sys.argv[2])
    result = run(card, corpus)
    print(text(result))
    if len(sys.argv) > 3:
        json.dump(result, open(sys.argv[3], "w"), indent=2)
