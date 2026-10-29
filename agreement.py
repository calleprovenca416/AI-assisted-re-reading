"""
Inter-coder agreement, per field, from returned coding sheets.

This script computes every agreement figure from the returned workbooks, so
that each figure can be made again from the files alone.

USAGE
    python3 agreement.py <corpus> <stage_B.xlsx>
        first coding = the corpus, second = the returned workbook
    python3 agreement.py <corpus> <stage_B.xlsx> <other_stage_B.xlsx>
        two returned workbooks against each other (e.g. human and blind);
        the corpus is used only to say which claims are directional
    python3 agreement.py <corpus> --stage-a <stage_A.xlsx>
        `outcome`, directional or not
    python3 agreement.py --selftest
        rebuilds the codings the logs describe and checks the eleven logged
        figures for direction, core and outcome; then tries the cold-paper
        mode on a made-up second coding

  For a cold paper (added 7 Oct 2026):
    python3 agreement.py <corpus> <stage_V_or_B.xlsx> --sidecar=<voice_gloss.json>
        the first form, with coder 1's voice and gloss relation taken from the
        extraction's sidecar, where a cold paper has them. A QUICK LOOK ONLY,
        and it says so in its first line: it checks neither the intake's
        record nor the pack's key, and it withholds kappa by the rule of
        Carlile's logs. A cold paper's figures are those of its log, below.
    python3 agreement.py --paper <corpus_vN.json> --sidecar=<voice_gloss.json>
            --key=<pack_key.json> --log=<the paper's agreement log.md>
            --label=<one line on who the two coders are>
            [--a=<returned A.xlsx>] [--a2=<returned A2.xlsx>]
            [--v=<returned V.xlsx>] [--b=<returned B.xlsx>]
            [--readings=<readings.json>]
            [--against=<against_check_results.json>]
        writes that paper's agreement log from the stages that are back.
        --label= may be left out for a test pack, and for nothing else

RULES, FROM SECOND_CODER.md
- Per field, never pooled.
- Computed before any discussion; this script has no notion of reconciliation.
- Raw agreement with its denominator for small fields. Kappa is withheld for
  any field with fewer than ten comparable judgements, and reported as
  undefined when expected agreement is 1.
- On Carlile (the first three usages above) kappa is also withheld for
  `stated_as`, `resolution_period` and `gloss_relation` at any size, as
  Carlile's logs withhold it. On a cold paper (--paper) it is withheld by count
  only, by a rule fixed on 7 Oct 2026, before any sheet of a cold paper had
  come back.
- Direction: `unassigned` and blank codes are not comparable. Reported for all
  comparable links and for links on directional claims (a claim with both an
  outcome and an asserted direction). `with`/`against` on a non-directional
  claim is counted and listed as invalid by schema.

`asserted_direction` (Stage A2) is judged on sign, which needs a reader: its
wording differs between any two coders. It is not computed here.

THE PAPER'S LOG (--paper)
The returned workbooks are the ones intake_coder2.py writes. Each is checked
before anything is computed:
  - it carries the intake's record, for this paper and this stage, naming the
    workbook that the pack's key records as sent, and no cell of its coding
    tabs has changed since the intake wrote it;
  - its tabs are its stage's; its rows are the rows of this corpus, in the
    pack builder's order; its row ids are those the pack's key records; and
    every row carries a code on its tab's list.
The key must have been built from this corpus and must record this sidecar,
by their hashes. The sidecar is checked by the pack builder's own check
(read_sidecar), the one the builder ran when it recorded the hash. Anything
that fails is refused, and nothing is written.

What these checks cannot tell: which pack a reply that came back as TEXT
answered. A line of text carries ids only. So a pack is built once, and each
reply file is named for its paper and stage when it arrives.

Coder 1 is the corpus and the extraction's sidecar; coder 2 is the returned
workbooks. The log gives, per field and never pooled:
  Stage A   outcome, directional or not; and, where both coders name an
            outcome, the two wordings side by side
  Stage A2  the two wordings of the asserted direction side by side, and the
            claims on which coder 2 writes `none`
  Stage V   voice, against the sidecar
  Stage B   direction (all comparable links, and links on directional
            claims), core, stated_as, gap kind, pair drawn_by_authors,
            resolution period, and gloss relation against the sidecar
  `against` how many links on directional claims each coding has, on which
            claims, and whether a claim reaches two; an `against` on a claim
            that names no outcome is invalid by schema and is counted apart;
            and once --against= gives the `against` check's results, these
            counts and the audit again, with the links that check flags
            counted as `illustrates`
  the audit under each coding: coverage, claims assessed, seams, moves
Each disagreement is listed with both codes, and with both reasons where the
corpus or the sidecar records coder 1's.

A kappa comes with a 95% interval, made as in the link tests: BOOT_REPS
resamples of the rows with replacement, and the 2.5th and 97.5th percentiles
of the kappas they give. A resample whose kappa is undefined is left out, and
the log says how many gave a kappa whenever some did not.

Two things are judged by reading and are not computed: whether two outcome
wordings name the same thing (Stage A), and whether two asserted directions
push the printed outcome the same way (Stage A2). The reader's calls go into
a JSON file given with --readings=, and the log prints and counts them:
    {"paper_id": "...", "judged_by": "who made the calls, and when",
     "judged_on": {"A": "<the digest of the returned Stage A workbook's coding tabs>",
                   "A2": "<the same for Stage A2>"},
     "outcome_wording": {"C01": {"call": "match", "note": "..."}},
     "direction_sign":  {"C01": {"call": "agree", "note": "..."}}}
    outcome_wording: match, polarity inverted, different variable, unclear,
                     coder 2 means none
    direction_sign:  agree, disagree, unclear, coder 2 means none
A row with no call is printed as not yet judged. The file must say who made
the calls and on which returned codes: `judged_on` gives, for each stage, the
digest that the intake's record keeps of the workbook's coding tabs, whole or
its first sixteen digits, as the log's table of files prints it. That digest
changes when a cell changes and not when a file is saved again, so a call
stays good for the codes it was made on, and is refused beside any others.
`coder 2 means none` is for a wording that says there is no outcome, or no
direction, in words the intake does not read as `none`. It may be made
wherever coder 2 names an outcome or gives a direction; where coder 1 names
no outcome it is the only call there is. The log then gives Stage A's figure
both ways.

A resolution period left null with a resolution basis is coder 1's answer
that the story does not close (brief v2), and is compared as `none`. Left
null with no basis, it is not coded and not comparable.

The log is written whole each time, from the files and the one line given with
--label=: the same files and the same line give the same log. So it is never
edited by hand. Its table of files names this script too, by its hash, and it
carries no date. The line says who the two coders are. It is required for a
pack that is not a test pack: no cold paper's figure goes unlabelled. The
log states the line, so that it is typed the same each time.
"""

import hashlib
import json
import os
import random
import re
import subprocess
import sys
import tempfile
from collections import Counter

from openpyxl import load_workbook

RAW_ONLY = {"stated_as", "resolution_period", "gloss_relation"}   # Carlile's rule only
MIN_FOR_KAPPA = 10
DIRECTION_CODES = {"with", "against", "illustrates", "qualifies"}
NONE_WORDS = {"", "none", "-", "--", "n/a", "no outcome"}
BOOT_REPS = 2000             # resamples of the rows for a kappa's 95% interval
BOOT_SEED = 20261007         # for those resamples only

# tab title -> (field, key column index (0-based), how to normalise)
TABS = {
    "1 direction": ("direction", (1, 3), "word"),
    "2 core": ("core", (1,), "bool"),
    "3 stated_as": ("stated_as", (1,), "word"),
    "4 gap kind": ("gap kind", (1,), "word"),
    "5 pair drawn_by": ("pair drawn_by_authors", (1,), "bool"),
    "6 resolution_period": ("resolution_period", (0,), "word"),
    "7 gloss_relation": ("gloss_relation", (1,), "word"),
    "8 voice": ("voice", (1,), "word"),
    "V voice": ("voice", (1,), "word"),          # a cold paper's Stage V workbook
}


def norm(v, how):
    s = ("" if v is None else str(v)).strip().strip("`").lower()
    if how == "bool":
        if s in ("true", "yes", "y", "1", "core"):
            return "true"
        if s in ("false", "no", "n", "0", "not core"):
            return "false"
    return s.upper() if s[:1] == "p" and s[1:].isdigit() else s


def read_sheet(path):
    """{field: {key: code}} from a returned Stage B workbook, or from a cold
    paper's returned Stage V workbook."""
    wb = load_workbook(path, read_only=True, data_only=True)
    out = {}
    for ws in wb.worksheets:
        if ws.title not in TABS:
            continue
        field, keycols, how = TABS[ws.title]
        rows = list(ws.iter_rows(values_only=True))
        header = [str(h or "") for h in rows[0]]
        code_col = next(i for i, h in enumerate(header) if h.startswith("YOUR CODE"))
        codes = {}
        for r in rows[1:]:
            if r is None or all(v is None for v in r):
                continue
            key = tuple(str(r[i]) for i in keycols) if field != "resolution_period" else ("paper",)
            codes[key] = norm(r[code_col], how)
        out[field] = codes
    return out


def read_stage_a(path):
    wb = load_workbook(path, read_only=True, data_only=True)
    ws = wb.worksheets[0]
    rows = list(ws.iter_rows(values_only=True))
    header = [str(h or "") for h in rows[0]]
    code_col = next(i for i, h in enumerate(header) if h.startswith("YOUR CODE"))
    return {str(r[1]): ("none" if norm(r[code_col], "word") in NONE_WORDS else "directional")
            for r in rows[1:] if r and r[1] is not None}


def from_corpus(corpus, sidecar=None):
    """The first coding, in the same shape read_sheet returns.

    `sidecar` is the extraction's voice file (<paper_id>_voice_gloss.json). A
    cold paper's corpus carries neither voice nor gloss relation: coder 1's
    codes for both are in the sidecar, and are taken from it when it is given.

    A resolution period left null with a resolution basis is the answer that
    the story does not close (brief v2), which a coder gives as `none`."""
    c = corpus
    b = lambda v: "true" if v else "false"
    resolution = (c["meta"].get("resolution_period") or "").upper()
    if not resolution and (c["meta"].get("resolution_basis") or "").strip():
        resolution = "none"
    out = {
        "direction": {(l["fragment_id"], l["claim_id"]): (l.get("direction") or "").lower()
                      for l in c["claim_links"]},
        "core": {(x["claim_id"],): b(x.get("core")) for x in c["claims"]},
        "stated_as": {(x["claim_id"],): (x.get("stated_as") or "").lower() for x in c["claims"]},
        "gap kind": {(g["gap_id"],): (g.get("kind") or "").lower() for g in c["declared_gaps"]},
        "pair drawn_by_authors": {(p["pair_id"],): b(p.get("drawn_by_authors"))
                                  for p in c["contrast_pairs"]},
        "resolution_period": {("paper",): resolution},
    }
    for fld in ("gloss_relation", "voice"):
        if sidecar is not None:
            vals = {(x["fragment_id"],): (x.get("code") or "").lower()
                    for x in sidecar.get(fld) or []}
        else:
            vals = {(f["fragment_id"],): (f.get(fld) or "").lower() for f in c["fragments"]}
        if any(vals.values()):
            out[fld] = vals
    return out


def directional_claims(corpus):
    return {x["claim_id"] for x in corpus["claims"]
            if (x.get("outcome") or "").strip() and (x.get("asserted_direction") or "").strip()}


def kappa(pairs):
    n = len(pairs)
    if not n:
        return None, None
    po = sum(a == b for a, b in pairs) / n
    ma, mb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum(ma[k] * mb[k] for k in ma) / n ** 2
    return po, (None if pe == 1 else (po - pe) / (1 - pe))


def line(label, pairs, raw_only=False):
    po, k = kappa(pairs)
    n = len(pairs)
    if not n:
        return f"  {label:<34} not comparable"
    agree = sum(a == b for a, b in pairs)
    s = f"  {label:<34} n={n:<3} raw {po:.3f} ({agree}/{n})"
    if raw_only or n < MIN_FOR_KAPPA:
        return s + "   kappa withheld (small field)"
    return s + ("   kappa undefined (no variance)" if k is None else f"   kappa {k:.3f}")


def comparable(a, b, field):
    """The keys on which both codings of a field carry a code that can be
    compared: for direction one of the four codes, elsewhere any code."""
    keys = sorted(set(a) & set(b))
    if field == "direction":
        return [k for k in keys if a[k] in DIRECTION_CODES and b[k] in DIRECTION_CODES]
    return [k for k in keys if a[k] and b[k]]


def compare(first, second, directional, names=("first", "second")):
    """Returns (report lines, figures dict). figures[field] = (raw, kappa)."""
    out, fig, disagreements = [], {}, []
    for field in ("direction", "core", "stated_as", "gap kind", "pair drawn_by_authors",
                  "resolution_period", "gloss_relation", "voice"):
        a, b = first.get(field), second.get(field)
        if a is None or b is None:
            out.append(f"  {field:<34} not comparable: no {names[0] if a is None else names[1]} coding")
            continue
        keys = sorted(set(a) & set(b))
        ok = comparable(a, b, field)
        if field == "direction":
            invalid = [(k, who, code[k]) for k in keys for who, code in zip(names, (a, b))
                       if k[1] not in directional and code[k] in ("with", "against")]
            allp = [(a[k], b[k]) for k in ok]
            dirp = [(a[k], b[k]) for k in ok if k[1] in directional]
            out.append(line("direction, all comparable links", allp))
            out.append(line("direction, directional claims", dirp))
            fig["direction"], fig["direction_directional"] = kappa(allp), kappa(dirp)
            if invalid:
                out.append(f"    invalid by schema (with/against on a non-directional claim): {len(invalid)}")
                for (f_, c_), who, code in invalid:
                    out.append(f"      {f_}->{c_}: {who} `{code}`")
            dist = {who: Counter(code[k] for k in ok) for who, code in zip(names, (a, b))}
            for who in names:
                out.append(f"    {who:<8} " + ", ".join(f"{c} {dist[who][c]}" for c in
                                                     ("illustrates", "with", "against", "qualifies")))
            disagreements += [("direction", "->".join(k), a[k], b[k]) for k in ok if a[k] != b[k]]
        else:
            p = [(a[k], b[k]) for k in ok]
            out.append(line(field, p, field in RAW_ONLY))
            fig[field] = kappa(p)
            disagreements += [(field, "/".join(k), a[k], b[k]) for k in ok if a[k] != b[k]]
    if disagreements:
        out.append(f"\n  disagreements ({names[0]} | {names[1]}):")
        for field, key, x, y in disagreements:
            out.append(f"    {field:<22} {key:<10} {x:<14} | {y}")
    return out, fig


def main(argv):
    if argv[:1] == ["--selftest"]:
        return selftest()
    if argv[:1] == ["--paper"]:
        return paper(argv[1:])
    side = [a.split("=", 1)[1] for a in argv if a.startswith("--sidecar=")]
    argv = [a for a in argv if not a.startswith("--sidecar=")]
    corpus = json.load(open(argv[0]))
    sidecar = json.load(open(side[0], encoding="utf-8")) if side else None
    if sidecar is not None and sidecar.get("paper_id") != corpus["meta"]["paper_id"]:
        print(f"REFUSED: the sidecar is for {sidecar.get('paper_id')!r}; "
              f"the corpus is {corpus['meta']['paper_id']!r}")
        return 1
    if argv[1:2] == ["--stage-a"]:
        coded = read_stage_a(argv[2])
        first = {x["claim_id"]: ("directional" if (x.get("outcome") or "").strip() else "none")
                 for x in corpus["claims"]}
        p = [(first[k], coded[k]) for k in sorted(set(first) & set(coded))]
        print("Stage A -- outcome, directional or not (corpus | sheet)")
        print(line("outcome", p))
        for k in sorted(set(first) & set(coded)):
            if first[k] != coded[k]:
                print(f"    {k:<5} {first[k]:<12} | {coded[k]}")
        return 0
    second = read_sheet(argv[1])
    if len(argv) > 2:
        first, names = read_sheet(argv[2]), ("other", "sheet")
        print(f"{argv[2]}  vs  {argv[1]}")
    else:
        first, names = from_corpus(corpus, sidecar), ("corpus", "sheet")
        print(f"{argv[0]}  vs  {argv[1]}")
    if sidecar is not None:
        print("A QUICK LOOK ONLY. This form checks neither the intake's record nor the pack's key, "
              "and it withholds kappa by the rule of Carlile's logs. A cold paper's figures are "
              "those of its agreement log: agreement.py --paper.")
    print("Per field, computed before any discussion. Never pool these.\n")
    lines, _ = compare(first, second, directional_claims(corpus), names)
    print("\n".join(lines))
    return 0


# ---------------------------------------------------------- the cold papers
# Added 7 Oct 2026. A cold paper's second coding comes back
# in four workbooks, one per stage, as intake_coder2.py writes them. The
# functions below read them against the corpus and the pack's key, and write
# the paper's agreement log. Nothing above this line changed in what it prints.

COLD_STAGES = {"A": ["0 outcome"], "A2": ["0b asserted_direction"], "V": ["V voice"],
               "B": ["1 direction", "2 core", "3 stated_as", "4 gap kind", "5 pair drawn_by",
                     "6 resolution_period", "7 gloss_relation"]}
BOOL_TABS = {"2 core", "5 pair drawn_by"}
B_FIELDS = [("2 core", "core", "2. Core"),
            ("3 stated_as", "stated_as", "3. Stated as"),
            ("4 gap kind", "gap kind", "4. Gap kind"),
            ("5 pair drawn_by", "pair drawn_by_authors", "5. Pair drawn by authors"),
            ("6 resolution_period", "resolution_period", "6. Resolution period"),
            ("7 gloss_relation", "gloss_relation", "7. Gloss relation")]
MEANS_NONE = "coder 2 means none"
OUTCOME_CALLS = ("match", "polarity inverted", "different variable", "unclear", MEANS_NONE)
SIGN_CALLS = ("agree", "disagree", "unclear", MEANS_NONE)
READINGS_KEYS = {"paper_id", "judged_by", "judged_on", "outcome_wording", "direction_sign"}
VOICE_CODES = ("reported", "author_insight")
LOG_TITLE = ": agreement between the two codings"


class Refused(Exception):
    pass


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def read_json(path, what):
    """A JSON object from a file, or a refusal that says what the file was given as."""
    try:
        x = json.load(open(path, encoding="utf-8"))
    except ValueError:                      # not JSON, or not a text file at all
        raise Refused(f"{what} is not a JSON file that can be read: {os.path.basename(path)}")
    if not isinstance(x, dict):
        raise Refused(f"{what} is not a JSON object: {os.path.basename(path)}")
    return x


def natural(s):
    """Sort key that puts F2 before F10."""
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", str(s))]


def boot_interval(pairs, reps=BOOT_REPS, seed=BOOT_SEED):
    """A 95% interval for kappa, made as in the link tests: `reps` resamples of
    the rows with replacement, and the 2.5th and 97.5th percentiles of the
    kappas they give. A resample in which kappa is undefined, because both
    coders use one code throughout it, is left out. Returns (low end, high
    end, how many resamples gave a kappa), or None if none did.

    The ends move by a few hundredths with the seed, and rows are resampled
    one by one, as if no two belonged together: the log says both."""
    n = len(pairs)
    if not n:
        return None
    rng = random.Random(seed)
    ks = []
    for _ in range(reps):
        k = kappa([pairs[rng.randrange(n)] for _ in range(n)])[1]
        if k is not None:
            ks.append(k)
    if not ks:
        return None
    ks.sort()
    return ks[int(0.025 * len(ks))], ks[int(0.975 * len(ks)) - 1], len(ks)


def figure(pairs):
    """One field's agreement on a cold paper, as a record: kappa is withheld
    under ten comparable judgements, by count only, and is
    undefined when expected agreement is 1. A kappa that is given comes with
    its interval, and with the number of resamples that gave a kappa."""
    n = len(pairs)
    rec = {"n": n, "agree": sum(a == b for a, b in pairs), "raw": None, "kappa": None,
           "kappa_note": None, "interval": None, "resamples": None}
    if not n:
        rec["kappa_note"] = "not comparable"
        return rec
    rec["raw"], k = kappa(pairs)
    if n < MIN_FOR_KAPPA:
        rec["kappa_note"] = f"withheld (fewer than {MIN_FOR_KAPPA} judgements)"
    elif k is None:
        rec["kappa_note"] = "undefined (no variance)"
    else:
        rec["kappa"] = k
        got = boot_interval(pairs)
        if got:
            rec["interval"], rec["resamples"] = got[:2], got[2]
    return rec


def cold_rows(corpus):
    """For each coding tab of a cold paper's pack, the ids its rows carry, in
    the order build_cold_pack.py prints them."""
    from build_cold_pack import has_outcome, page_order
    frags, claims = corpus["fragments"], corpus["claims"]
    fidx = {f["fragment_id"]: i for i, f in enumerate(frags)}
    cidx = {c["claim_id"]: i for i, c in enumerate(claims)}
    links = sorted(corpus["claim_links"],
                   key=lambda l: (fidx[l["fragment_id"]], cidx[l["claim_id"]]))
    return {
        "0 outcome": [(c["claim_id"],) for c in claims],
        "0b asserted_direction": [(c["claim_id"],) for c in claims if has_outcome(c)],
        "V voice": [(f["fragment_id"],) for f in frags],
        "1 direction": [(l["fragment_id"], l["claim_id"]) for l in links],
        "2 core": [(c["claim_id"],) for c in claims],
        "3 stated_as": [(c["claim_id"],) for c in claims],
        "4 gap kind": [(g["gap_id"],) for g in corpus["declared_gaps"]],
        "5 pair drawn_by": [(p["pair_id"],) for p in corpus["contrast_pairs"]],
        "6 resolution_period": [()],
        "7 gloss_relation": [(frags[k]["fragment_id"],) for k in page_order(frags)
                             if (frags[k].get("author_gloss") or "").strip()],
    }


def read_returned(path, stage, corpus, key):
    """One returned stage of a cold paper, as intake_coder2.py writes it:
    {tab: [(row id, ids, code, reason)]}. The code is as given for Stages A
    and A2, which take free text, and normalised for the other tabs.

    Refuses a workbook that does not carry the intake's record for this paper,
    this stage and this pack, or whose cells have changed since the intake
    wrote it; one that is not this stage's; one whose rows are not this
    corpus's in the builder's order, or whose row ids are not those the pack's
    key records; and one in which a row has no code or a code off its tab's
    list. A refusal names rows by their ids and never prints a coder's words."""
    from build_cold_pack import CODES, ID_COLUMNS
    from intake_coder2 import stamp_problem
    want = cold_rows(corpus)
    name = os.path.basename(path)
    try:
        wb = load_workbook(path)
    except Exception:                       # openpyxl has several errors for a file that is no workbook
        raise Refused(f"{name} is not a workbook that can be opened")
    why = stamp_problem(path, corpus["meta"]["paper_id"], stage, key, wb)
    if why:
        raise Refused(why)
    sheets = {ws.title: ws for ws in wb.worksheets}
    out = {}
    for tab in COLD_STAGES[stage]:
        if tab not in sheets:
            raise Refused(f"{name} has no tab {tab!r}: it is not a returned Stage {stage} workbook")
        rows = [tuple(c.value for c in r) for r in sheets[tab].iter_rows()]
        head = [" ".join(str(h or "").split()) for h in rows[0]] if rows else []
        try:
            code_col = next(i for i, h in enumerate(head) if h.startswith("YOUR CODE"))
            reason_col = next(i for i, h in enumerate(head) if h.startswith("YOUR REASON"))
            id_cols = [head.index(c) for c in ID_COLUMNS[tab]]
        except (StopIteration, ValueError):
            raise Refused(f"{name}, tab {tab!r}: a column the pack builder prints is missing")
        if tab in CODES:
            allowed = [c.lower() for c in CODES[tab]]
        elif tab == "6 resolution_period":
            allowed = [p.lower() for p in corpus["meta"].get("periods") or []] + ["none"]
        else:
            allowed = None                                   # Stages A and A2: free text
        recs, bad = [], []
        for r in rows[1:]:
            if all(v is None or str(v).strip() == "" for v in r):
                continue
            rid = str(r[0]).strip()
            ids = tuple(str(r[i]).strip() for i in id_cols)
            given = " ".join(str("" if r[code_col] is None else r[code_col]).split())
            reason = " ".join(str("" if r[reason_col] is None else r[reason_col]).split())
            if allowed is None:
                code = given
                if not given:
                    bad.append(rid)
            else:
                code = norm(given, "bool" if tab in BOOL_TABS else "word")
                if code.lower() not in allowed:
                    bad.append(rid)
            recs.append((rid, ids, code, reason))
        if bad:
            raise Refused(f"{name}, tab {tab!r}: {len(bad)} row(s) with no code, or a code that is "
                          f"not on the tab's list: {bad[:10]}{' ...' if len(bad) > 10 else ''}. "
                          "Read the stage in with intake_coder2.py first")
        if [x[1] for x in recs] != want[tab]:
            raise Refused(f"{name}, tab {tab!r}: its rows are not this corpus's rows in the pack "
                          f"builder's order ({len(recs)} rows here, {len(want[tab])} expected)")
        sent = ((key.get("workbooks") or {}).get(stage) or {}).get("rows", {}).get(tab)
        if sent is None or [x[0] for x in recs] != [str(i) for i in sent]:
            raise Refused(f"{name}, tab {tab!r}: its row ids are not the ones the pack's key records")
        out[tab] = recs
    return out


def second_coding(tabs):
    """Returned tabs as one coding, in the shape read_sheet gives. Stages A
    and A2 are free text and are not part of it."""
    out = {}
    for tab, recs in tabs.items():
        if tab in TABS:
            out[TABS[tab][0]] = {(ids or ("paper",)): code for _, ids, code, _ in recs}
    return out


def load_readings(path, pid, claims, digests=None):
    """The reader's calls for Stage A's wordings and Stage A2's signs.

    `digests` is {stage: the digest of the returned workbook's coding tabs, from
    its intake record}. A file with calls must say who made them (`judged_by`)
    and on which codes (`judged_on`, that digest whole or its first sixteen
    digits): a call made on one set of codes is refused beside another. A part
    the script does not know is refused, so that a misspelt name does not pass
    as no calls at all."""
    out = {"file": None, "judged_by": "", "outcome_wording": {}, "direction_sign": {}}
    if not path:
        return out
    try:
        r = json.load(open(path, encoding="utf-8"))
    except ValueError:
        raise Refused("the readings file is not a JSON file")
    if not isinstance(r, dict) or r.get("paper_id") != pid:
        raise Refused("the readings file is not for this paper: its paper_id is "
                      f"{r.get('paper_id') if isinstance(r, dict) else None!r}, and the corpus is {pid!r}")
    unknown = sorted(set(r) - READINGS_KEYS)
    if unknown:
        raise Refused(f"the readings file has a part the script does not know: {unknown}. The "
                      f"parts are: {', '.join(sorted(READINGS_KEYS))}")
    out["file"], out["judged_by"] = path, " ".join(str(r.get("judged_by") or "").split())
    on = r.get("judged_on") or {}
    if not isinstance(on, dict):
        raise Refused("the readings file: judged_on must give, for each stage, the digest of its "
                      "workbook's coding tabs")
    for part, calls, stage in (("outcome_wording", OUTCOME_CALLS, "A"),
                               ("direction_sign", SIGN_CALLS, "A2")):
        given = r.get(part) or {}
        if not isinstance(given, dict):
            raise Refused(f"the readings file, {part}: the calls must be given by claim id")
        if given and not out["judged_by"]:
            raise Refused("the readings file has calls and does not say who made them (judged_by)")
        on_this = on.get(stage) if isinstance(on.get(stage), str) else ""
        if given and digests is not None and stage in digests and not (
                len(on_this) >= 16 and digests[stage].startswith(on_this)):
            raise Refused(f"the readings file, {part}: its calls were not made on this returned "
                          f"Stage {stage} workbook. judged_on must give the digest of that "
                          "workbook's coding tabs, whole or its first sixteen digits, as the "
                          "log's table of files prints it")
        for cid, v in given.items():
            v = v if isinstance(v, dict) else {"call": v}
            if cid not in claims:
                raise Refused(f"the readings file names {cid}, which is not a claim of this corpus")
            if v.get("call") not in calls:
                raise Refused(f"the readings file, {part}, {cid}: its call is not one of: "
                              f"{', '.join(calls)}")
            out[part][cid] = (v["call"], " ".join(str(v.get("note") or "").split()))
    return out


def load_against(path, pid):
    """From the results build_against_check.py writes: for each coder, this
    paper's `against` links that the check looked at, those it answered 4a to
    4x (they count as `illustrates` in the second version of every figure that
    rests on `against`), and how many it answered 4a."""
    r = read_json(path, "the file of the `against` check's results")
    out = {"file": path, "not_sent": [(x["fragment_id"], x["claim_id"])
                                      for x in r.get("not_sent_claim_has_no_outcome", [])
                                      if x.get("paper_id") == pid]}
    for who in ("coder1", "coder2"):
        mine = [x for x in r.get("results", []) if x.get("paper_id") == pid
                and who in x.get("coded_by", [])]
        out[who] = {"looked_at": {(x["fragment_id"], x["claim_id"]) for x in mine},
                    "flagged": {(x["fragment_id"], x["claim_id"]) for x in mine if x.get("flagged")},
                    "answered_4a": sum(1 for x in mine if x.get("answer") == "4a")}
    return out


def by_link(k):
    return natural(k[0]), natural(k[1])


def against_summary(direction, directional, flagged=()):
    """One coding's `against` links on directional claims: which, on which
    claims, the most on any one claim, and the claims with two or more. A
    flagged link is left out. An `against` on a claim that is not directional
    is invalid by schema: the `against` check never sees it and the audit
    never counts it, so it is not counted here either, and is given apart."""
    coded = sorted((k for k, d in direction.items() if d == "against"), key=by_link)
    links = [k for k in coded if k[1] in directional and k not in flagged]
    per = Counter(c for _, c in links)
    top = max(per.values(), default=0)
    return {"links": links, "per_claim": dict(per), "most": top,
            "most_on": sorted((c for c, n in per.items() if n == top), key=natural),
            "two_or_more": sorted((c for c, n in per.items() if n >= 2), key=natural),
            "invalid": [k for k in coded if k[1] not in directional]}


def audit_under(corpus_path, voice, coding=None, flagged=()):
    """The Stage 1 audit of the corpus under one coding, with the voice rule.

    `voice` is {fragment: code}. `coding`, for coder 2, is the returned codes:
    they take the place of the corpus's direction, core, stated_as, gap kind
    and resolution period. Whether a pair was drawn by the authors changes no
    figure that is taken from the audit here, so it is left as it is. Which
    claims are directional stays the corpus's in either case, because both
    codings of direction were made against the outcome and the direction the
    corpus records. A link in `flagged` that is coded `against` counts as
    `illustrates`."""
    from schema import load
    import audit
    c = load(corpus_path)
    if coding is not None:
        for l in c.links:
            l.direction = coding["direction"][(l.fragment_id, l.claim_id)]
        for x in c.claims:
            x.core = coding["core"][(x.claim_id,)] == "true"
            x.stated_as = coding["stated_as"][(x.claim_id,)]
        for g in c.gaps:
            g.kind = coding["gap kind"][(g.gap_id,)]
        period = coding["resolution_period"][("paper",)]
        c.meta.resolution_period = None if period == "none" else period
    for l in c.links:
        if l.direction == "against" and (l.fragment_id, l.claim_id) in flagged:
            l.direction = "illustrates"
    r = audit.run_audit(c, voice=voice)
    uni = r["measures"][0]
    rows = uni.detail.get("claims", [])
    return {"directional": uni.detail.get("directional_claims", 0),
            "with": sum(x["with"] for x in rows), "against": sum(x["against"] for x in rows),
            "out_with": r["voice_rule"]["excluded_with"],
            "out_against": r["voice_rule"]["excluded_against"],
            "assessed": uni.detail.get("assessed_claims", 0), "coverage": uni.coverage,
            "seams": list(uni.detail.get("seams", [])), "scored": uni.scored, "score": uni.score,
            "moves": list(r["readiness"]["moves_parameterised"]),
            "min_links": audit.MIN_LINKS_FOR_UNIFORMITY, "min_coverage": audit.MIN_COVERAGE}


def paper_results(corpus_path, sidecar_path, key_path, stages, readings_path=None,
                  against_path=None):
    """Everything a cold paper's agreement log reports, as one record. `stages`
    is {"A" | "A2" | "V" | "B": the returned workbook's path}."""
    from build_cold_pack import CODES, has_outcome, read_sidecar
    from build_cold_pack import Refused as PackRefused
    from intake_coder2 import norm_free, read_stamp
    from schema import load, validate

    corpus = read_json(corpus_path, "the corpus")
    key = read_json(key_path, "the pack's key")
    meta, pid = corpus["meta"], corpus["meta"]["paper_id"]
    unknown = sorted(set(stages) - set(COLD_STAGES))
    if unknown or not stages:
        raise Refused(f"stages must be among {', '.join(COLD_STAGES)}; got {sorted(stages)}")

    # ---- the checks that come before any figure
    c_obj = load(corpus_path)
    errs, _ = validate(c_obj)
    if errs:
        raise Refused(f"{os.path.basename(corpus_path)} has {len(errs)} validation error(s)")
    if key.get("paper_id") != pid or key.get("corpus_sha256") != sha(corpus_path):
        raise Refused("the pack's key was not built from this corpus: its paper_id or its "
                      "record of the corpus's hash differs")
    if not key.get("sidecar_sha256"):
        raise Refused("the pack's key records no sidecar, so coder 1's voice and gloss relation "
                      "cannot be told from any other file's. Packs are built with --sidecar= "
                      "from builder version 1.3 on")
    if key["sidecar_sha256"] != sha(sidecar_path):
        raise Refused("the sidecar is not the one the pack's key records: coder 1's voice and "
                      "gloss relation are the extraction's, frozen with the corpus")
    try:        # the builder's own check, which it ran when it recorded that hash
        side, voice1, _ = read_sidecar(sidecar_path, corpus, c_obj)
    except PackRefused as e:
        raise Refused(str(e))
    claims = {c["claim_id"]: c for c in corpus["claims"]}
    frags = {f["fragment_id"]: f for f in corpus["fragments"]}
    gloss = side.get("gloss_relation") or []
    directional = directional_claims(corpus)
    odd = sorted((cid for cid, c in claims.items() if has_outcome(c) != (cid in directional)),
                 key=natural)
    if odd:
        raise Refused(f"the pack builder and the audit would not agree on whether these claims "
                      f"name an outcome: {odd}")
    ret = {st: read_returned(p, st, corpus, key) for st, p in stages.items()}
    records = {st: read_stamp(load_workbook(p)) for st, p in stages.items()}
    first = from_corpus(corpus, side)
    second = second_coding({t: recs for st in ret.values() for t, recs in st.items()})
    readings = load_readings(readings_path, pid, claims,
                             {st: rec["content_sha256"] for st, rec in records.items()})
    flags = load_against(against_path, pid) if against_path else None
    said_none = lambda code: norm_free(code, "")[0] == "none"   # the intake's rule, and no other

    on_file = lambda what, p: (what, os.path.basename(p), sha(p))
    files = [on_file("coder 1: the corpus", corpus_path),
             on_file("coder 1: the sidecar", sidecar_path),
             on_file(f"the pack's key (builder version {key.get('builder') or 'not recorded'})",
                     key_path)]
    for st in COLD_STAGES:
        if st in stages:        # the workbook; what the intake read it from; and its codes
            rec = records[st]
            files += [on_file(f"coder 2: Stage {st}", stages[st]),
                      (f"Stage {st} as it came, read in from a {rec['came_as']}", rec["came_file"],
                       rec["came_sha256"]),
                      (f"Stage {st}: the digest of its coding tabs (for `judged_on`)", "",
                       rec["content_sha256"])]
    files += ([on_file("the readings", readings_path)] if readings_path else []) \
        + ([on_file("the `against` check's results", against_path)] if against_path else []) \
        + [on_file("written by", os.path.abspath(__file__))]
    res = {"paper_id": pid, "citation": meta.get("citation") or pid,
           "test_pack": bool(key.get("test_pack")),
           "counts": {"fragments": len(frags), "claims": len(claims),
                      "links": len(corpus["claim_links"]), "directional": len(directional)},
           "files": files, "digests": {st: rec["content_sha256"] for st, rec in records.items()},
           "missing": [st for st in COLD_STAGES if st not in stages],
           "judged_by": readings["judged_by"], "A": None, "A2": None, "V": None, "B": None,
           "against": None, "audit": None}

    def unused(part, judged):
        extra = sorted(set(readings[part]) - set(judged), key=natural)
        if extra:
            raise Refused(f"the readings file, {part}: a call is given for {extra}, where coder 2 "
                          "gives nothing to judge")

    # ---- Stage A: outcome
    if "A" in ret:
        recs = ret["A"]["0 outcome"]
        named2 = {ids[0]: not said_none(code) for _, ids, code, _ in recs}
        word = lambda v: "directional" if v else "none"
        pairs = [(word(has_outcome(claims[i[0]])), word(named2[i[0]])) for _, i, _, _ in recs]
        differ, both, both_none, alone, means_none = [], [], [], [], []
        for _, (cid,), code, reason in recs:
            one = has_outcome(claims[cid])
            call, note = readings["outcome_wording"].get(cid, ("", ""))
            if one and named2[cid]:
                both.append((cid, claims[cid]["outcome"].strip(), code, call or "not yet judged", note))
            elif named2[cid]:
                # coder 2 alone names an outcome. There are no two wordings to set side
                # by side, so the one call a reader can make is that this one means none
                if call and call != MEANS_NONE:
                    raise Refused(f"the readings file, outcome_wording, {cid}: coder 1 names no "
                                  f"outcome there, so the only call is `{MEANS_NONE}`")
                alone.append(cid)
                differ.append((cid, "none", code, reason, call, note))
            elif one:
                differ.append((cid, claims[cid]["outcome"].strip(), "none", reason, "", ""))
            else:
                both_none.append(cid)
            if call == MEANS_NONE and named2[cid]:
                means_none.append(cid)
        unused("outcome_wording", [x[0] for x in both] + alone)
        # where the reader says that coder 2's wording means none, the figure both ways
        as_read = [(word(has_outcome(claims[i[0]])),
                    word(named2[i[0]] and i[0] not in means_none)) for _, i, _, _ in recs]
        res["A"] = {"fig": figure(pairs), "pairs": pairs, "differ": differ, "both": both,
                    "both_none": both_none, "calls": Counter(x[3] for x in both),
                    "means_none": means_none,
                    "fig_as_read": figure(as_read) if means_none else None}
    elif readings["outcome_wording"]:
        raise Refused("the readings file has calls on outcome wordings, and Stage A is not given")

    # ---- Stage A2: asserted direction
    if "A2" in ret:
        rows, nones = [], []
        for _, (cid,), code, reason in ret["A2"]["0b asserted_direction"]:
            c = claims[cid]
            if said_none(code):
                nones.append((cid, c["outcome"].strip(), (c.get("asserted_direction") or "").strip(),
                              reason))
            else:
                call, note = readings["direction_sign"].get(cid, ("not yet judged", ""))
                rows.append((cid, c["outcome"].strip(), (c.get("asserted_direction") or "").strip(),
                             code, call, note))
        unused("direction_sign", [x[0] for x in rows])
        res["A2"] = {"sent": len(rows) + len(nones), "rows": rows, "none": nones,
                     "calls": Counter(x[4] for x in rows)}
    elif readings["direction_sign"]:
        raise Refused("the readings file has calls on the sign, and Stage A2 is not given")

    def closed(field, recs, reasons1=None):
        """A closed field in the sheet's row order: its pairs, its figure, the
        rows that cannot be compared, and each disagreement with its reasons."""
        a, b = first.get(field) or {}, second[field]
        ok = set(comparable(a, b, field))
        keyed = [(rid, ids or ("paper",), reason) for rid, ids, _, reason in recs]
        pairs = [(a[k], b[k]) for _, k, _ in keyed if k in ok]
        dis = [(rid, k, a[k], b[k], (reasons1 or {}).get(k, ""), reason)
               for rid, k, reason in keyed if k in ok and a[k] != b[k]]
        return {"pairs": pairs, "dis": dis, "fig": figure(pairs), "rows": len(keyed),
                "not_comparable": [rid for rid, k, _ in keyed if k not in ok],
                "has_reasons1": reasons1 is not None}

    # ---- Stage V: voice
    if "V" in ret:
        recs = ret["V"]["V voice"]
        v = closed("voice", recs, {(x["fragment_id"],): x.get("reason") or "" for x in side["voice"]})
        v["removed"] = sorted((x["fragment_id"] for x in key.get("V_opening_removed") or []),
                              key=natural)
        v["location"] = {f: (frags[f].get("location") or "") for f in frags}
        res["V"] = v

    # ---- Stage B: sections 1 to 7
    if "B" in ret:
        tabs = ret["B"]
        basis = {(l["fragment_id"], l["claim_id"]): l.get("basis") or ""
                 for l in corpus["claim_links"]}
        d = closed("direction", tabs["1 direction"], basis)
        a, b = first["direction"], second["direction"]
        ok = set(comparable(a, b, "direction"))
        on_dir = [(a[k], b[k]) for _, k, _, _ in tabs["1 direction"]
                  if k in ok and k[1] in directional]
        d["fig_directional"], d["pairs_directional"] = figure(on_dir), on_dir
        d["invalid"] = [(rid, k, who, code[k]) for rid, k, _, _ in tabs["1 direction"]
                        for who, code in (("coder 1", a), ("coder 2", b))
                        if k[1] not in directional and code[k] in ("with", "against")]
        reasons = {"pair drawn_by_authors": {(p["pair_id"],): p.get("basis") or ""
                                             for p in corpus["contrast_pairs"]},
                   "resolution_period": {("paper",): meta.get("resolution_basis") or ""},
                   "gloss_relation": {(g["fragment_id"],): g.get("reason") or "" for g in gloss}}
        periods = [p for p in meta.get("periods") or []] + ["none"]
        fields = {}
        for tab, field, title in B_FIELDS:
            fields[field] = closed(field, tabs[tab], reasons.get(field))
            fields[field]["title"] = title
            fields[field]["codes"] = [c.lower() if tab != "6 resolution_period" else c
                                      for c in CODES.get(tab, periods)]
        res["B"] = {"direction": d, "fields": fields}

        # ---- `against` in each coding
        one, two = against_summary(a, directional), against_summary(b, directional)
        res["against"] = {"coder1": one, "coder2": two,
                          "both": sorted(set(one["links"]) & set(two["links"]), key=by_link),
                          "check": None}
        if flags:
            for who, code in (("coder1", a), ("coder2", b)):
                mine = {k for k, x in code.items() if x == "against" and has_outcome(claims[k[1]])}
                if mine != flags[who]["looked_at"]:
                    raise Refused(f"the `against` check's results do not cover {who}'s `against` "
                                  f"links of this paper: {len(flags[who]['looked_at'])} looked at, "
                                  f"{len(mine)} coded on claims that name an outcome")
            res["against"]["check"] = {
                who: {"summary": against_summary(code, directional, flags[who]["flagged"]),
                      "flagged": sorted(flags[who]["flagged"], key=by_link),
                      "answered_4a": flags[who]["answered_4a"]}
                for who, code in (("coder1", a), ("coder2", b))}
            res["against"]["check"]["not_sent"] = sorted(flags["not_sent"], key=by_link)
    elif flags:
        raise Refused("the `against` check's results are given, and Stage B is not")

    # ---- the audit under each coding
    aud = {"coder1": audit_under(corpus_path, voice1), "coder2": None, "check": None}
    if flags:
        aud["check"] = {"coder1": audit_under(corpus_path, voice1, None, flags["coder1"]["flagged"]),
                        "coder2": None}
    if "V" in ret and "B" in ret:
        voice2 = {k[0]: code for k, code in second["voice"].items()}
        aud["coder2"] = audit_under(corpus_path, voice2, second)
        if flags:
            aud["check"]["coder2"] = audit_under(corpus_path, voice2, second,
                                                 flags["coder2"]["flagged"])
    res["audit"] = aud
    return res


# ------------------------------------------------------- the log, as text
def cell(v):
    """A value in a markdown table: on one line, a dash if empty, and a bar
    escaped, with any backslash before it, so that neither ends the cell."""
    s = " ".join(str("" if v is None else v).split()).replace("\\", "\\\\").replace("|", "\\|")
    return s or "—"


def table(head, rows):
    return (["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
            + ["| " + " | ".join(cell(x) for x in r) + " |" for r in rows] + [""])


def crosstab(pairs, codes):
    """Coder 1 in rows, coder 2 in columns, over the codes either coder used."""
    used = [c for c in codes if any(c in p for p in pairs)]
    used += sorted({x for p in pairs for x in p} - set(used))
    n = Counter(pairs)
    return table(["coder 1 in rows, coder 2 in columns"] + [f"`{c}`" for c in used],
                 [[f"`{a}`"] + [n[(a, b)] for b in used] for a in used])


def dec(x, places):
    """A number to so many decimals, and never a minus before a zero."""
    s = f"{x:.{places}f}"
    return s[1:] if s.startswith("-") and not s.strip("-0.") else s


def fig_text(rec):
    """One figure in words."""
    if not rec["n"]:
        return "not comparable"
    s = f"n = {rec['n']}; raw agreement {rec['raw']:.3f} ({rec['agree']} of {rec['n']})"
    if rec["kappa"] is None:
        return s + f"; kappa {rec['kappa_note']}"
    s += f"; kappa {dec(rec['kappa'], 3)}"
    if rec["interval"] is None:
        return s + " (no interval: no resample gave a kappa)"
    s += f" (95% interval {dec(rec['interval'][0], 2)} to {dec(rec['interval'][1], 2)}"
    if rec["resamples"] < BOOT_REPS:
        s += f"; {rec['resamples']:,} of {BOOT_REPS:,} resamples gave a kappa"
    return s + ")"


def link(k):
    return f"{k[0]}→{k[1]}"


def listed(items, none="none"):
    return ", ".join(items) if items else none


def count(n, word):
    return f"{n} {word}" if n == 1 else f"{n} {word}s"


def paper_log(res, label=None):
    """The text of the paper's agreement log, from paper_results()."""
    pid, L = res["paper_id"], []
    add = L.append
    add(f"# {pid}{LOG_TITLE}\n")
    if res["test_pack"]:
        add("**TEST PACK. The pack was built from an unfrozen corpus and is never sent. Nothing "
            "below is a result.**\n")
    add(f"{res['citation']}\n")
    add("Written by `agreement.py --paper` from the files in the table below, and written whole "
        "again whenever a stage returns. It is not edited by hand: the same files, and the same "
        "line on who the coders are, give the same log. It carries no date.\n")
    add("- **Coder 1** is the extraction: the corpus, and the extraction's sidecar for voice and "
        "gloss relation. **Coder 2** is the second coding: the returned workbooks.")
    add("- " + (f"**Who they are:** {' '.join(label.split())}" if label else
                "**Who they are** is not given to the script: see `SECOND_CODER.md`."))
    add("- Every figure is **per field and never pooled.** Each is computed from the files as "
        "they stand, with no notion of a discussion or a reconciliation: nothing here is merged "
        "into the corpus, and no figure changes with what is agreed later. That the coding came "
        "back before any disagreement was discussed is the protocol's to ensure "
        "(`SECOND_CODER.md`), and the script cannot know it.")
    add(f"- **Kappa** is withheld for a field with fewer than {MIN_FOR_KAPPA} comparable "
        f"judgements, by count only, and is undefined when both coders use one and the same code "
        f"throughout. Carlile's logs also withheld it for three named fields at any size; on the "
        f"cold papers that part of the rule was dropped before any sheet came back "
        f"(7 Oct 2026).")
    add(f"- **A kappa that is given comes with a 95% interval:** {BOOT_REPS:,} resamples of the "
        f"rows with replacement (seed {BOOT_SEED}), and the 2.5th and 97.5th percentiles of their "
        f"kappas. A resample in which both coders use one code throughout has no kappa and is "
        f"left out; where that happens, the figure says how many resamples gave one. Two "
        f"cautions. The ends move with the seed, and more where a field has few rows: on made-up tables, "
        f"by about a hundredth at some hundreds of rows, by a few hundredths at about fifty, "
        f"and by as much as 0.14 at ten to fifteen. And rows are resampled one "
        f"by one, though links cluster by claim and by fragment, so the interval for direction "
        f"is likely too narrow.")
    add("- **By reading** marks a call that a reader made: whether two outcome wordings name "
        "the same thing, and whether two asserted directions push the printed outcome the same "
        "way. The script counts the calls. Where a call says that coder 2's wording means "
        "`none`, it also gives Stage A's figure a second time, with that call applied."
        + (f" The calls were made by: {res['judged_by']}." if res["judged_by"] else ""))
    c = res["counts"]
    add(f"- The corpus has {c['fragments']} fragments, {c['claims']} claims and {c['links']} "
        f"links. {c['directional']} of the claims are directional: they carry both an outcome "
        f"and an asserted direction.\n")
    L += table(["what", "file", "sha256 opens"],
               [(what, f"`{name}`" if name else "", digest[:16]) for what, name, digest in res["files"]])
    if res["missing"]:
        add("**Not yet back:** Stage " + ", Stage ".join(res["missing"]) + ".\n")

    # ---- Stage A
    add("## Stage A: the outcome of every claim (section 0)\n")
    A = res["A"]
    if A is None:
        add("Not yet back.\n")
    else:
        add(f"**Directional or not:** {fig_text(A['fig'])}.\n")
        L += crosstab(A["pairs"], ["directional", "none"])
        add(f"**One coder names an outcome and the other writes `none`: "
            f"{count(len(A['differ']), 'claim')}.**\n")
        if A["differ"]:
            add(f"Where coder 2 alone names an outcome, a reader may call the wording "
                f"`{MEANS_NONE}`. No other call applies there, because there are no two "
                "wordings to compare.\n")
            L += table(["claim", "coder 1", "coder 2", "coder 2's reason", "by reading", "note"],
                       A["differ"])
        add(f"**Both name an outcome: {count(len(A['both']), 'claim')}.** Whether the two wordings name "
            "the same thing is judged by reading. The calls: "
            + ", ".join(f"{x} {A['calls'][x]}" for x in OUTCOME_CALLS + ("not yet judged",)) + ".\n")
        if A["both"]:
            L += table(["claim", "coder 1", "coder 2", "by reading", "note"], A["both"])
        if A["means_none"]:
            add(f"**By the reader's call, coder 2's wording means `none` on "
                f"{count(len(A['means_none']), 'claim')}:** {listed(A['means_none'])}. The intake "
                "reads as `none` only an answer that begins with `none`, `no outcome`, `no "
                "direction`, `n/a`, `na`, `null` or a hyphen, so the figure at the head of this "
                "section counts these as an outcome named. **With them counted as `none`, directional or "
                f"not reads:** {fig_text(A['fig_as_read'])}.\n")
        add(f"**Both write `none`: {count(len(A['both_none']), 'claim')}.** "
            f"{listed(A['both_none'])}.\n")

    # ---- Stage A2
    add("## Stage A2: the asserted direction (section 0b)\n")
    A2 = res["A2"]
    if A2 is None:
        add("Not yet back.\n")
    else:
        add(f"{A2['sent']} claims name an outcome in the corpus, and only those were sent, each "
            f"with the corpus's outcome printed. Coder 2 gives a direction on {len(A2['rows'])} "
            f"and writes `none` on {len(A2['none'])}.\n")
        add("**Sign, by reading.** The wording of a direction differs between any two coders, "
            "so what is judged is whether both push the printed outcome the same way. No kappa "
            "is computed. The calls: "
            + ", ".join(f"{x} {A2['calls'][x]}" for x in SIGN_CALLS + ("not yet judged",)) + "."
            + (f" A call of `{MEANS_NONE}` is for a wording that gives no direction in words the "
               "intake does not read as `none`: such a claim belongs with those of the last "
               "table of this section." if A2["calls"][MEANS_NONE] else "") + "\n")
        if A2["rows"]:
            L += table(["claim", "the outcome as printed", "coder 1", "coder 2", "sign, by reading",
                        "note"], A2["rows"])
        add(f"**Coder 2 writes `none`: {count(len(A2['none']), 'claim')}.**\n")
        if A2["none"]:
            L += table(["claim", "the outcome as printed", "coder 1", "coder 2's reason"],
                       A2["none"])

    def disagreements(rec, id_head, reason1_head):
        """The table of one field's disagreements."""
        add(f"**Disagreements: {len(rec['dis'])}.**\n")
        if rec["not_comparable"]:
            add(f"Rows that cannot be compared, because coder 1 has no code for them: "
                f"{listed(rec['not_comparable'])}.\n")
        if not rec["dis"]:
            return
        head = ["row"] + id_head + ["coder 1", "coder 2"]
        head += ([reason1_head] if rec["has_reasons1"] else []) + ["coder 2's reason"]
        rows = []
        for rid, k, x, y, r1, r2 in rec["dis"]:
            ids = [] if k == ("paper",) else list(k)
            rows.append([rid] + ids + [f"`{x}`", f"`{y}`"]
                        + ([r1] if rec["has_reasons1"] else []) + [r2])
        L.extend(table(head, rows))

    # ---- Stage V
    add("## Stage V: voice (section V)\n")
    V = res["V"]
    if V is None:
        add("Not yet back.\n")
    else:
        add(f"**Voice:** {fig_text(V['fig'])}.\n")
        L += crosstab(V["pairs"], list(VOICE_CODES))
        starred = set(V["removed"])
        add(f"The pack builder took an opening voice cue off the description of "
            f"{count(len(starred), 'row')}, which the key lists. Their fragments are marked * "
            "below. Where coder 2 notes that such a description and the page disagree, that is "
            "the builder's doing.\n")
        V = dict(V, dis=[(rid, (k[0] + ("*" if k[0] in starred else ""), V["location"].get(k[0], "")),
                          x, y, r1, r2) for rid, k, x, y, r1, r2 in V["dis"]])
        disagreements(V, ["fragment", "location"], "coder 1's reason")

    # ---- Stage B
    add("## Stage B: sections 1 to 7\n")
    B = res["B"]
    if B is None:
        add("Not yet back.\n")
    else:
        d = B["direction"]
        add("### 1. Direction\n")
        add(f"**All comparable links:** {fig_text(d['fig'])}.\n")
        add(f"**Links on directional claims:** {fig_text(d['fig_directional'])}.\n")
        L += crosstab(d["pairs"], ["illustrates", "with", "against", "qualifies"])
        if d["invalid"]:
            add(f"**Invalid by schema: {len(d['invalid'])}.** `with` or `against` on a claim that "
                "is not directional: "
                + "; ".join(f"{rid} {link(k)}, {who} `{code}`" for rid, k, who, code in d["invalid"])
                + ".\n")
        disagreements(d, ["fragment", "claim"], "coder 1's basis")
        heads = {"core": ["claim"], "stated_as": ["claim"], "gap kind": ["gap"],
                 "pair drawn_by_authors": ["pair"], "resolution_period": [],
                 "gloss_relation": ["fragment"]}
        for _, field, title in B_FIELDS:
            rec = B["fields"][field]
            add(f"### {title}\n")
            if not rec["rows"]:
                add(f"**`{field}`:** no rows. The corpus has none to code.\n")
                continue
            add(f"**`{field}`:** {fig_text(rec['fig'])}.\n")
            if rec["pairs"]:
                L += crosstab(rec["pairs"], rec["codes"])
            disagreements(rec, heads[field], "coder 1's reason")

    # ---- `against`
    add("## `against` in each coding\n")
    G = res["against"]
    if G is None:
        add("Stage B is not yet back.\n")
    else:
        def rows_for(one, two):
            most = lambda s: f"{s['most']}" + (f" ({listed(s['most_on'])})" if s["most"] else "")
            return [("links coded `against`, on directional claims", len(one["links"]),
                     len(two["links"])),
                    ("claims with at least one", len(one["per_claim"]), len(two["per_claim"])),
                    ("the most on one claim", most(one), most(two)),
                    ("claims with two or more", listed(one["two_or_more"]),
                     listed(two["two_or_more"])),
                    ("coded `against` on a claim that names no outcome: invalid by schema, and "
                     "not counted above", len(one["invalid"]), len(two["invalid"]))]
        add("Every link coded `against` on a directional claim, as coded, whatever the voice of "
            "its fragment. An `against` on a claim that names no outcome is invalid by schema: "
            "the `against` check is never sent it and the audit never counts it, so it is "
            "counted in the last row and nowhere else.\n")
        L += table(["", "coder 1", "coder 2"], rows_for(G["coder1"], G["coder2"]))
        add(f"- Coder 1: {listed([link(k) for k in G['coder1']['links']])}.")
        add(f"- Coder 2: {listed([link(k) for k in G['coder2']['links']])}.")
        add(f"- Coded `against` by both: {len(G['both'])}"
            + (f" ({listed([link(k) for k in G['both']])})" if G["both"] else "") + ".\n")
        if G["check"] is None:
            add("**No results of the `against` check were given to the script.** That check runs "
                "once, after all coding. With its results, the counts of this section and the "
                "audit below are given a second time, with the links that check flags counted "
                "as `illustrates`. The agreement on direction above is not: it stands as coded.\n")
        else:
            k1, k2 = G["check"]["coder1"], G["check"]["coder2"]
            add("**With the links the `against` check flags counted as `illustrates`:**\n")
            L += table(["", "coder 1", "coder 2"],
                       rows_for(k1["summary"], k2["summary"])
                       + [("links flagged (answered 4a to 4x)",
                           f"{len(k1['flagged'])}: {listed([link(k) for k in k1['flagged']])}",
                           f"{len(k2['flagged'])}: {listed([link(k) for k in k2['flagged']])}"),
                          ("of them, answered 4a", k1["answered_4a"], k2["answered_4a"])])
            if G["check"]["not_sent"]:
                add("Not sent to the check, because the claim names no outcome: "
                    + listed([link(k) for k in G["check"]["not_sent"]]) + ".\n")

    # ---- the audit
    add("## The audit under each coding\n")
    U = res["audit"]
    add("Coder 1's column is the corpus with the extraction's sidecar. Coder 2's column is the "
        "corpus with coder 2's codes in place of coder 1's (direction, core, stated as, gap kind "
        "and resolution period) and with coder 2's voice codes. Whether a pair was drawn by the "
        "authors changes no figure in this table. Which claims are directional is the corpus's "
        "in both, because both codings of direction were made against the outcome and the "
        "direction the corpus records. The voice rule is applied in both: a `with` or `against` "
        "link from a fragment coded `author_insight` is left out, and counted in the row \"left "
        "out by the voice rule\".\n")

    def audit_rows(one, two):
        def col(fn):
            return fn(one), ("needs Stages V and B" if two is None else fn(two))
        rate = lambda x: (f"{x['score']:.3f}" if x["scored"] else
                          f"not reported: coverage is under {x['min_coverage']:.2f}")
        return [("directional claims", *col(lambda x: x["directional"])),
                ("`with` and `against` links counted",
                 *col(lambda x: f"{x['with']} and {x['against']}")),
                ("left out by the voice rule",
                 *col(lambda x: f"{x['out_with']} `with`, {x['out_against']} `against`")),
                (f"claims assessed (at least {one['min_links']} counted links)",
                 *col(lambda x: x["assessed"])),
                ("coverage", *col(lambda x: f"{x['coverage']:.3f}")),
                ("seams", *col(lambda x: listed(x["seams"]))),
                ("uniformity rate", *col(rate)),
                ("moves parameterised", *col(lambda x: listed(x["moves"])))]
    L += table(["", "coder 1", "coder 2"], audit_rows(U["coder1"], U["coder2"]))
    if U["check"] is not None:
        add("**With the links the `against` check flags counted as `illustrates`:**\n")
        L += table(["", "coder 1", "coder 2"], audit_rows(U["check"]["coder1"], U["check"]["coder2"]))

    add("## What this log does not hold\n")
    add("- Whether the pinned predictions held. They are stated apart, in no file.")
    add("- The extraction's miss rate, which comes from the coverage check, and the hours.")
    add("- Any reconciliation. Disagreements are discussed only when every paper is coded.")
    return "\n".join(L) + "\n"


def paper_screen(res):
    """What --paper prints: one line per figure, and no word of any coder."""
    out = [f"{res['paper_id']}{'  (TEST PACK)' if res['test_pack'] else ''}"]
    if res["A"]:
        out.append(f"  Stage A   outcome, directional or not: {fig_text(res['A']['fig'])}")
        out.append("            both name an outcome on " + str(len(res["A"]["both"])) + "; by reading: "
                   + ", ".join(f"{k} {v}" for k, v in sorted(res["A"]["calls"].items())))
    if res["A2"]:
        out.append(f"  Stage A2  direction given on {len(res['A2']['rows'])} of {res['A2']['sent']}, "
                   f"`none` on {len(res['A2']['none'])}; sign by reading: "
                   + ", ".join(f"{k} {v}" for k, v in sorted(res["A2"]["calls"].items())))
    if res["V"]:
        out.append(f"  Stage V   voice: {fig_text(res['V']['fig'])}")
    if res["B"]:
        d = res["B"]["direction"]
        out.append(f"  Stage B   direction, all comparable links: {fig_text(d['fig'])}")
        out.append(f"            direction, directional claims: {fig_text(d['fig_directional'])}")
        for _, field, _ in B_FIELDS:
            rec = res["B"]["fields"][field]
            out.append(f"            {field}: {fig_text(rec['fig']) if rec['rows'] else 'no rows'}")
        g = res["against"]
        out.append(f"  against   coder 1: {len(g['coder1']['links'])}, most on one claim "
                   f"{g['coder1']['most']}; coder 2: {len(g['coder2']['links'])}, most on one "
                   f"claim {g['coder2']['most']}; coded by both: {len(g['both'])}")
    for who in ("coder1", "coder2"):
        a = res["audit"][who]
        if a:
            out.append(f"  audit     {who}: coverage {a['coverage']:.3f}, {a['assessed']} of "
                       f"{a['directional']} directional claims assessed, seams: {listed(a['seams'])}")
    if res["missing"]:
        out.append("  not yet back: Stage " + ", Stage ".join(res["missing"]))
    return out


def paper(argv):
    """--paper: write one cold paper's agreement log."""
    known = {"--sidecar", "--key", "--log", "--a", "--a2", "--v", "--b", "--readings",
             "--against", "--label"}
    usage = ("usage: agreement.py --paper <corpus_vN.json> --sidecar=<voice_gloss.json> "
             "--key=<pack_key.json> --log=<log.md> --label=<who the two coders are> "
             "[--a=...] [--a2=...] [--v=...] [--b=...] [--readings=...] [--against=...]")
    flags = [a for a in argv if a.startswith("--")]
    args = [a for a in argv if not a.startswith("--")]
    names = [a.split("=", 1)[0] for a in flags]
    opt = {a.split("=", 1)[0]: a.split("=", 1)[1] for a in flags if "=" in a}
    stages = {st: opt["--" + st.lower()] for st in COLD_STAGES if "--" + st.lower() in opt}
    wrong = []
    if len(args) != 1:
        wrong.append(f"one corpus file is expected, and {len(args)} were given")
    wrong += [f"{n} is given {names.count(n)} times" for n in sorted(set(names)) if names.count(n) > 1]
    wrong += [f"{a.split('=', 1)[0]} needs a value, as {a.split('=', 1)[0]}=<...>"
              for a in flags if "=" not in a]
    wrong += [f"{n} is not an option of --paper" for n in sorted(set(names) - known)]
    wrong += [f"{n}= is missing" for n in ("--sidecar", "--key", "--log") if n not in names]
    if not stages and not wrong:
        wrong.append("no stage is given: at least one of --a=, --a2=, --v=, --b=")
    if wrong:
        print("REFUSED: " + "; ".join(wrong))
        print(usage)
        return 2
    read = [args[0], opt["--sidecar"], opt["--key"], *stages.values()]
    read += [opt[k] for k in ("--readings", "--against") if k in opt]
    gone = [p for p in read if not os.path.isfile(p)]
    if gone:
        print(f"REFUSED: no such file: {', '.join(gone)}")
        return 1
    log_path = opt["--log"]
    if os.path.abspath(log_path) in {os.path.abspath(p) for p in read}:
        print("REFUSED: --log names one of the files that are read")
        return 1
    if not os.path.isdir(os.path.dirname(os.path.abspath(log_path))):
        print(f"REFUSED: the folder that --log names does not exist: {os.path.dirname(log_path)}")
        return 1
    if os.path.exists(log_path):
        first = open(log_path, encoding="utf-8", errors="replace").readline() if os.path.isfile(log_path) else ""
        if not (first.startswith("# ") and first.rstrip().endswith(LOG_TITLE)):
            print(f"REFUSED: {log_path} exists and is not a log this script wrote. It writes "
                  "over an agreement log of its own, and over nothing else")
            return 1
    label = " ".join((opt.get("--label") or "").split())
    try:
        res = paper_results(args[0], opt["--sidecar"], opt["--key"], stages,
                            opt.get("--readings"), opt.get("--against"))
        if not label and not res["test_pack"]:
            raise Refused("--label= is missing. A cold paper's log says on its first page who "
                          "the two coders are (model against model, and which models): give "
                          "the line that the paper's agreement log states")
        if os.path.exists(log_path):
            head = open(log_path, encoding="utf-8", errors="replace").read(2000)
            if not head.startswith(f"# {res['paper_id']}{LOG_TITLE}"):
                raise Refused(f"{log_path} is the agreement log of another paper")
            if res["test_pack"] and "**TEST PACK." not in head:
                raise Refused(f"{log_path} is the log of a pack that is not a test pack, and this "
                              "run is of a test pack: it is not written over")
    except Refused as e:
        print(f"REFUSED: {e}")
        return 1
    except json.JSONDecodeError:
        print("REFUSED: the corpus, the sidecar, the key or the `against` results is not a JSON "
              "file that can be read")
        return 1
    with open(log_path, "w", encoding="utf-8") as fh:
        fh.write(paper_log(res, label or None))
    print("\n".join(paper_screen(res)))
    print(f"wrote {log_path}")
    return 0


# ------------------------------------------------------------------ self-test
def selftest():
    """Left out of the repository's copy: the self-test ran on the Carlile pilot's files, which are not in the
    repository (see the README)."""
    print("selftest: left out of the repository's copy; it runs on the Carlile pilot's files, which are not "
          "here (see the README)")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
