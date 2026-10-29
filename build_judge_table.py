"""
Build the judges' tables for the adjudication of the two codings of a cold
paper, and their key. Written 13 Oct 2026.

WHAT A JUDGE GETS
A judge chat gets the paper, JUDGING.md and one paper's table, in two parts:
part 1, the claims (what a claim says is affected; whether the paper's argument
rests on it; how firmly the paper puts it), and part 2, the passages (what a
passage shows of a claim). Part 2 prints each claim's outcome and direction as
the record has them, so part 1 is answered and returned before part 2 is sent,
as Stage A comes before Stage B in the coding.

Each row is one statement about the paper, in a fixed wording per code, so that
no wording of a row leans either way. A row never says who made the statement,
whether anyone else made another, or what the codes were.

WHICH STATEMENTS
For every row on which the two codings differ, in the fields of the two parts:
each coding's code, as a statement of its own. The fields: Stage A's outcome
(one coding names an outcome and the other none, or both name one and the
reading call on the two wordings is not "match"), Stage B's core and stated_as,
and link direction. Voice, gloss relation, gap kind, pairs and periods are not
judged. Mixed in, drawn from the rows on which the two codings agree, in each
part's fields in proportion to their differing rows: pairs of the agreed
statement and a statement neither coding made, and agreed statements alone,
about a fifth of the part's differing rows of each, at least two. A statement
neither coding made is: for an outcome, that the claim names none; for core and
stated_as, the other value; for direction, a code neither gave, among those
open to the claim (with and against only where the claim names an outcome).

ORDER AND IDS
One random.Random(seed): the papers in the order given, within a paper part 1
then part 2; within a part the rows drawn, then shuffled until no two
statements on the same claim or link stand within three places of each other.
Each statement gets a random id of four characters, unique across the build.

THE KEY
judge_key.json, for no judge: the seed, the sources
with their hashes, and for each id its paper, part, field, the claim or link,
the code it states, whose it is (coder 1, coder 2, both or neither), whether
the codings differ there, and the hash of each table.

usage (from the folder, so that its modules are found; -B leaves no cache):
  python3 -B build_judge_table.py --seed=N --out=DIR PAPER_ID ...
"""
import hashlib
import json
import os
import random
import string
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import agreement as ag                                  # noqa: E402
from build_cold_pack import read_sidecar, has_outcome   # noqa: E402
from schema import load                                 # noqa: E402

DIRECTION = {
    "with": "The passage shows {o} going the way the claim says.",
    "against": ("The passage shows {o} going the other way from what the claim says, "
                "or happening without the cause the claim names."),
    "qualifies": ("The passage limits the claim: it shows where or when the claim does not "
                  "hold, or holds only in part."),
    "illustrates": "The passage is about what the claim is about, but shows nothing of {o} itself.",
}
DIRECTION_NO_OUTCOME = {
    "with": "The passage bears the claim out.",
    "against": "The passage goes against the claim.",
    "qualifies": DIRECTION["qualifies"],
    "illustrates": ("The passage is about what the claim is about, but neither bears it out "
                    "nor limits it."),
}
OUTCOME_NAMED = "What this claim says is affected is: {w}."
OUTCOME_NONE = "This claim does not say that anything in particular is affected."
CORE = {"true": ("The paper's argument rests on this claim: without it, the paper would lose "
                 "its contribution."),
        "false": ("The paper's argument does not rest on this claim: it is background, a step "
                  "on the way, or support for another claim.")}
STATED = {"established": "The paper puts this claim as something it has shown.",
          "ventured": ("The paper puts this claim tentatively: hedged, offered or proposed, not "
                       "as something it has shown.")}
PART_FIELDS = {1: ["outcome", "core", "stated_as"], 2: ["direction"]}
ID_CHARS = "".join(c for c in string.ascii_uppercase + string.digits if c not in "IO01")
MIN_GAP = 3


def files(pid):
    p = lambda name: os.path.join(HERE, name)
    return {
        "corpus": p(f"{pid}_v1.json"),
        "sidecar": p(f"{pid}_v1_voice_gloss.json"),
        "key": p(os.path.join("packs", pid, "key", f"{pid}_pack_key.json")),
        "stages": {st: p(f"returned_{pid}_STAGE_{st}_coder2.xlsx") for st in ("A", "A2", "V", "B")},
        "readings": p(f"{pid}_readings.json"),
        "against": p("against_check_results.json"),
    }


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def clean(s):
    return " ".join((s or "").split())


def outcome_statement(w):
    w = clean(w).rstrip(".")
    return OUTCOME_NONE if w.lower() in ("", "none") else OUTCOME_NAMED.format(w=w)


def direction_statement(code, claim):
    if has_outcome(claim):
        return DIRECTION[code].format(o=clean(claim["outcome"]).rstrip("."))
    return DIRECTION_NO_OUTCOME[code]


def rows_of(pid):
    """Every row of the four judged fields: (field, key, coder 1's code, coder 2's
    code, differ?), in the corpus's order, with the claims and fragments."""
    f = files(pid)
    res = ag.paper_results(f["corpus"], f["sidecar"], f["key"], f["stages"],
                           readings_path=f["readings"], against_path=f["against"])
    corpus = ag.read_json(f["corpus"], "the corpus")
    key = ag.read_json(f["key"], "the pack's key")
    side, _, _ = read_sidecar(f["sidecar"], corpus, load(f["corpus"]))
    ret = {st: ag.read_returned(p, st, corpus, key) for st, p in f["stages"].items()}
    first = ag.from_corpus(corpus, side)
    second = ag.second_coding({t: recs for st in ret.values() for t, recs in st.items()})
    claims = {c["claim_id"]: c for c in corpus["claims"]}
    frags = {x["fragment_id"]: x for x in corpus["fragments"]}

    rows = []
    # outcome: each coding's wording, or none
    a = res["A"]
    named2 = {ids[0]: code for _, ids, code, _ in ret["A"]["0 outcome"]}
    wording_call = {x[0]: x[3] for x in a["both"]}
    differ = {x[0] for x in a["differ"]}
    for _, (cid,), _, _ in ret["A"]["0 outcome"]:
        c = claims[cid]
        one = clean(c["outcome"]) if has_outcome(c) else "none"
        two_raw = clean(named2[cid])
        two = "none" if ag_norm_none(two_raw) else two_raw
        split = cid in differ or (cid in wording_call and wording_call[cid] != "match")
        rows.append(("outcome", (cid,), one, two, split))
    for field in ("core", "stated_as", "direction"):
        a1, b2 = first[field], second[field]
        ok = ag.comparable(a1, b2, field)
        tab = {"core": "2 core", "stated_as": "3 stated_as", "direction": "1 direction"}[field]
        for _, ids, _, _ in ret["B"][tab]:
            k = tuple(ids)
            if k in ok:
                rows.append((field, k, a1[k], b2[k], a1[k] != b2[k]))
    # the split counts must be the log's
    want = {"outcome": len(differ | {c for c, call in wording_call.items() if call != "match"}),
            "direction": len(res["B"]["direction"]["dis"]),
            "core": len(res["B"]["fields"]["core"]["dis"]),
            "stated_as": len(res["B"]["fields"]["stated_as"]["dis"])}
    for fld, n in want.items():
        got = sum(1 for r in rows if r[0] == fld and r[4])
        assert got == n, f"{pid} {fld}: {got} differing rows here, {n} in the log's figures"
    return rows, claims, frags


def ag_norm_none(code):
    from intake_coder2 import norm_free
    return norm_free(code, "")[0] == "none"


def statement(field, code, key, claims):
    if field == "outcome":
        return outcome_statement(code)
    if field == "core":
        return CORE[code]
    if field == "stated_as":
        return STATED[code]
    return direction_statement(code, claims[key[1]])


def decoy_code(field, key, agreed, claims, rng):
    if field == "outcome":
        return None if agreed == "none" else "none"
    if field == "core":
        return "false" if agreed == "true" else "true"
    if field == "stated_as":
        return "ventured" if agreed == "established" else "established"
    open_codes = ["with", "against", "qualifies", "illustrates"] if has_outcome(claims[key[1]]) \
        else ["qualifies", "illustrates"]
    choices = [c for c in open_codes if c != agreed]
    return rng.choice(choices) if choices else None


def allocate(total, weights):
    """Largest remainder: split `total` over the fields in proportion to `weights`."""
    s = sum(weights.values())
    if not s:
        return {k: 0 for k in weights}
    raw = {k: total * w / s for k, w in weights.items()}
    out = {k: int(v) for k, v in raw.items()}
    for k in sorted(raw, key=lambda k: (raw[k] - out[k], k), reverse=True)[:total - sum(out.values())]:
        out[k] += 1
    return out


def spread(items, rng, attempts=20000):
    """Shuffle until statements on the same claim or link stand MIN_GAP apart."""
    for _ in range(attempts):
        rng.shuffle(items)
        last = {}
        ok = True
        for i, it in enumerate(items):
            g = it["group"]
            if g in last and i - last[g] < MIN_GAP:
                ok = False
                break
            last[g] = i
        if ok:
            return items
    raise SystemExit("could not spread the statements; widen the table or lower MIN_GAP")


def new_id(rng, used):
    while True:
        i = "".join(rng.choice(ID_CHARS) for _ in range(4))
        if i not in used:
            used.add(i)
            return i


def claim_head(c):
    loc = clean(c.get("location"))
    return f"**Claim** ({loc}): {clean(c['statement'])}" if loc else f"**Claim:** {clean(c['statement'])}"


def render_row(it, claims, frags):
    lines = [f"### {it['id']}", ""]
    field, key = it["field"], it["key"]
    if field == "direction":
        fid, cid = key
        c, fr = claims[cid], frags[fid]
        lines.append(claim_head(c))
        if has_outcome(c):
            lines.append("")
            lines.append(f"**What it says is affected:** {clean(c['outcome'])}. "
                         f"**Which way:** {clean(c.get('asserted_direction'))}.")
        lines.append("")
        lines.append(f"**The passage:** {clean(fr.get('location'))}, the one this summary points to: "
                     f"\"{clean(fr.get('stub'))}\"")
    else:
        lines.append(claim_head(claims[key[0]]))
    lines.append("")
    lines.append(f"**Statement:** {it['text']}")
    lines.append("")
    return "\n".join(lines)


PART_TITLE = {1: "Part 1: the claims", 2: "Part 2: the passages"}
PART_NOTE = {
    1: ("Each row gives a claim the paper makes, as a reader summed it up, with the "
        "pages where the paper makes it, and one statement about that claim."),
    2: ("Each row gives a claim the paper makes, as a reader summed it up, with what it "
        "says is affected and which way, then a passage of the paper, by its page and a "
        "reader's summary that points to it, and one statement about that passage."),
}


def main(argv):
    seed = out = None
    papers = []
    for a in argv:
        if a.startswith("--seed="):
            seed = int(a.split("=", 1)[1])
        elif a.startswith("--out="):
            out = a.split("=", 1)[1]
        else:
            papers.append(a)
    if seed is None or not out or not papers:
        raise SystemExit(__doc__)
    os.makedirs(out, exist_ok=True)
    rng = random.Random(seed)
    used = set()
    key = {"what": "the key to the judges' tables: for no judge",
           "seed": seed, "built_by": "build_judge_table.py", "papers": {}}
    for pid in papers:
        f = files(pid)
        rows, claims, frags = rows_of(pid)
        rec = {"sources": {os.path.relpath(p, HERE): sha(p)
                           for p in [f["corpus"], f["sidecar"], f["key"], f["readings"],
                                     f["against"]] + list(f["stages"].values())},
               "parts": {}}
        for part in (1, 2):
            flds = PART_FIELDS[part]
            prow = [r for r in rows if r[0] in flds]
            split = [r for r in prow if r[4]]
            agreed = [r for r in prow if not r[4]]
            items = []
            for fld, k, one, two, _ in split:
                group = (fld,) + k
                for who, code in (("coder 1", one), ("coder 2", two)):
                    items.append({"field": fld, "key": k, "code": code, "who": who,
                                  "differ": True, "group": group,
                                  "text": statement(fld, code, k, claims)})
            n = max(2, round(len(split) / 5))
            weights = {fld: sum(1 for r in split if r[0] == fld) for fld in flds}
            pool = {fld: [r for r in agreed if r[0] == fld] for fld in flds}
            take_pairs = allocate(n, weights)
            take_single = allocate(n, weights)
            for fld in flds:
                cands = list(pool[fld])
                rng.shuffle(cands)
                pairs, singles = [], []
                for r in cands:
                    if len(pairs) < take_pairs[fld]:
                        d = decoy_code(fld, r[1], r[2], claims, rng)
                        if d is not None:
                            pairs.append((r, d))
                            continue
                    if len(singles) < take_single[fld]:
                        singles.append(r)
                    if len(pairs) >= take_pairs[fld] and len(singles) >= take_single[fld]:
                        break
                for r, d in pairs:
                    group = (fld,) + r[1]
                    items.append({"field": fld, "key": r[1], "code": r[2], "who": "both",
                                  "differ": False, "group": group,
                                  "text": statement(fld, r[2], r[1], claims)})
                    items.append({"field": fld, "key": r[1], "code": d, "who": "neither",
                                  "differ": False, "group": group,
                                  "text": statement(fld, d, r[1], claims)})
                for r in singles:
                    items.append({"field": fld, "key": r[1], "code": r[2], "who": "both",
                                  "differ": False, "group": (fld,) + r[1],
                                  "text": statement(fld, r[2], r[1], claims)})
            items.sort(key=lambda it: (it["field"], ag.natural(" ".join(it["key"])), it["who"]))
            items = spread(items, rng)
            for it in items:
                it["id"] = new_id(rng, used)
            short = pid.split("_")[0]
            name = f"JUDGE_TABLE_{short}_part{part}.md"
            body = [f"# {PART_TITLE[part]}", "",
                    PART_NOTE[part], "",
                    f"{len(items)} rows. Judge each statement on its own, as JUDGING.md asks.", ""]
            body += [render_row(it, claims, frags) for it in items]
            text = "\n".join(body).rstrip("\n") + "\n"
            open(os.path.join(out, name), "w", encoding="utf-8").write(text)
            rec["parts"][str(part)] = {
                "file": name, "sha256": hashlib.sha256(text.encode()).hexdigest(),
                "rows": len(items), "differing_rows": len(split),
                "statements": [{"id": it["id"], "field": it["field"], "key": list(it["key"]),
                                "code": it["code"], "who": it["who"], "differ": it["differ"]}
                               for it in items]}
            print(pid, "part", part, "rows", len(items), "differing rows", len(split),
                  {fld: weights[fld] for fld in flds},
                  "pairs with a statement neither made", sum(1 for it in items if it["who"] == "neither"),
                  "agreed alone", sum(1 for it in items if it["who"] == "both") -
                  sum(1 for it in items if it["who"] == "neither"))
        key["papers"][pid] = rec
    ktext = json.dumps(key, indent=1, ensure_ascii=False) + "\n"
    open(os.path.join(out, "judge_key.json"), "w", encoding="utf-8").write(ktext)
    print("key sha256", hashlib.sha256(ktext.encode()).hexdigest())


if __name__ == "__main__":
    main(sys.argv[1:])
