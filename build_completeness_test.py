#!/usr/bin/env python3
"""
The completeness test (T38): the builder of its files and the checks of its replies.

WHY
---
`COMPLETENESS_TEST_PLAN.md` asks whether a model, given what the PI had for the PI's coverage check (the paper, the
reading sheet of the first return and the extraction brief), lists the passages the PI listed (chats 68 and 69, the
checker); how many of its lines a second model judges to be misses under the brief (chats 71 and 72, the judge,
who also pairs its lines with the PI's, blind to whose is whose); and whether the second extraction of Bechky (T35)
holds the passages of the PI's Bechky list (chat 70, the matcher). This script makes every file those chats get but the
task files, makes the key, and checks every reply. It judges nothing.

USAGE
-----
    python3 -B build_completeness_test.py files <out dir>
        the chats' copies of the two reading sheets, CHECK_SHEET_bechky.md and CHECK_SHEET_pratt.md, and the
        matcher's file, PASSAGES_AND_Q_bechky.md
    python3 -B build_completeness_test.py key <out path>
        the key, completeness_key.json: the PI's lines, the coverage chats' decisions on them, the draw
    python3 -B build_completeness_test.py check-checker <bechky|pratt> <reply>
    python3 -B build_completeness_test.py check-matcher <key> <reply>
    python3 -B build_completeness_test.py lists <key> <checker reply, Bechky> <checker reply, Pratt> <out dir>
        the judges' files, TWO_PASSAGE_LISTS_bechky.md and TWO_PASSAGE_LISTS_pratt.md, and their key,
        completeness_lists_key.json
    python3 -B build_completeness_test.py check-judge <lists key> <bechky|pratt> <reply>
    python3 -B build_completeness_test.py --selftest

Every file it writes it refuses to write over. The same sources always give the same bytes: no date, no clock.

THE SOURCES, each checked against its sha256 before use
-------------------------------------------------------
- The PI's two reading sheets, made by `coverage_sheet.py` from the first returns; the chats' copies differ from
  them in their third line alone, which says who the sheet is for.
- The PI's two lists. Bechky's has 16 lines, of which 15 and 16 are the same (a
  duplicate): the key keeps line 15 and records 16 as its duplicate. Pratt's has 14.
- The two coverage chats' logs: their section "Coverage additions" answers each of the PI's lines. DECISIONS below
  gives, for each line, the log's line that answers it and the records the chat added from it, typed in by hand
  from the logs on 17 Oct; `key` checks that each such log line names the place of the PI's line and each record
  given, and that the logs name no added record that DECISIONS leaves out.
- `TWO_LISTS_bechky.md` (T35): its list Q, from the line "## List Q" to the end, is copied byte for byte into
  the matcher's file.
- The first returns, for the ids of their fragments and claims, against which the judges' ids are checked.

THE CHECKS
----------
A reply is read as the text from its first "{" to its last "}" (a reply in parts is joined before). Faults make a
reply not count; remarks are reported and the reply counts. Every quoted span of more than eight words in any
string of a reply is named (where, how many words), never printed; the plan shows such spans to the PI before the
reply is filed, and the span is not filed.
- Checker: an object whose `passages` is a list; each item an object with `where`, a non-empty string; `test`, one
  of evidence, assertion, both; and `reason`, a non-empty string. Remarks: a `where` that names no page of the
  paper (Bechky pp. 606-643, Pratt pp. 456-493); a `where` of more than 20 words, which may say more than a page
  and a place; `n` not running 1, 2, 3 ...; two lines with the same `where`.
- Matcher: an object whose `lines` has exactly the keys L01 to L15, each an object with `found` (true or false),
  `passages` (QP ids of list Q), `claims` (QC ids of list Q) and a non-empty `reason`; when `found` is false, both
  lists are empty. Faults: a missing or extra line, an id not in list Q, a wrong kind of value.
- Judge: an object with `pairs`, a list of [A id, B id], each id one of the lists' lines and each pair once; and
  `verdicts`, an object with exactly one entry for every line of both lists, each with `verdict` one of evidence,
  assertion, both, covered, not_in_brief, not_found; `ids`, a list of strings; and a non-empty `reason`. A
  `covered` verdict names at least one id. Remarks: an id that is not a fragment or claim of the first return.
"""
import hashlib
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import build_citation_sheet as bcs  # noqa: E402

PAPERS = ("bechky", "pratt")
RANGE = {"bechky": (606, 643), "pratt": (456, 493)}
SEED = 20261024
SHEET = {"bechky": "bechky_2020_coverage_reading.md", "pratt": "pratt_2000_coverage_reading.md"}
LIST = {"bechky": "bechky_2020_coverage_list.txt", "pratt": "pratt_2000_coverage_list.txt"}
LOG = {"bechky": "bechky_2020_coverage_extraction_log.md", "pratt": "pratt_2000_coverage_extraction_log.md"}
FIRST = {"bechky": "bechky_2020_corpus.json", "pratt": "pratt_2000_corpus.json"}
TWO_LISTS = "TWO_LISTS_bechky.md"
SHA = {
    "bechky_2020_coverage_reading.md": "909001acb132fbd210ddc3d245775bd8988a6e974710f347f25e0c904f6df2ca",
    "pratt_2000_coverage_reading.md": "07b743457e1f03f15209c146ec7b0b52d777b5af4d03e0254a08ed622924a939",
    "bechky_2020_coverage_list.txt": "c022ce409510b89838117a9d47a0d9a93f948f6f23a6733a4639a13c8a47f080",
    "pratt_2000_coverage_list.txt": "9543f6f1c6ab14b4706b7a43fed8ec1d1d573a0c9645cc5acd055465fc71f4e3",
    "bechky_2020_coverage_extraction_log.md": "84c446452422b03de235c0d93c9033ad49f65ee2b4747530dc8ff0fac41ada04",
    "pratt_2000_coverage_extraction_log.md": "9565c8183363e4f6aca000767265facef9f00ab7c477ca7175b17dd79ffa2b14",
    "bechky_2020_corpus.json": "7ce0e382bb5659552a63d65b889035674ed7ddbd112bdef37295a520b20f5acc",
    "pratt_2000_corpus.json": "b22a8f26e2eb875ce0da9a29572380ba5a24dc88c196b5515d9380f47d2bd2c9",
    "TWO_LISTS_bechky.md": "8ffba0ddbaa3d4f74780483623f267ef263808f01ffd47c6bc07cc74c461e5ea",
}
TESTS = ("evidence", "assertion", "both")
VERDICTS = ("evidence", "assertion", "both", "covered", "not_in_brief", "not_found")
MISS = ("evidence", "assertion", "both")
MATCHER_LINES = tuple("L%02d" % i for i in range(1, 16))

# For each of the PI's lines, in the order of the PI's list: the log's line (1-based) that answers it, and the records
# the coverage chat added from it. Typed in by hand from the two logs' sections "Coverage additions" on 17 Oct.
DECISIONS = {
    "bechky": [
        ("pp. 606–607, the paragraph that runs over the page", 199, []),
        ("p. 607, second full paragraph", 200, []),
        ("p. 608, first full paragraph", 201, []),
        ("p. 609, third full paragraph", 202, []),
        ("p. 610, the paragraph above the subheading", 203, []),
        ("pp. 610–611, the paragraph that runs over the page", 204, []),
        ("p. 611, first full paragraph", 205, []),
        ("pp. 611–612, the paragraph that runs over the page", 206, ["F169"]),
        ("p. 612, footnote 1", 207, ["F170"]),
        ("p. 621, footnote 4", 208, []),
        ("pp. 622–623, the paragraph that runs over the page", 209, ["F171"]),
        ('p. 633, Table 2, row "Values", column "Toxicology"', 210, []),
        ("p. 636, third full paragraph", 211, ["F172"]),
        ("pp. 637–638, the paragraph that runs over the page", 212, []),
        ("p. 638, first full paragraph", 213, []),
    ],
    "pratt": [
        ("p. 459, third full paragraph", 207, ["F122"]),
        ("p. 460, footnote 6", 208, ["C53"]),
        ("p. 461, second full paragraph", 209, ["F123"]),
        ("pp. 464–465, the paragraph that runs over the page", 210, []),
        ("p. 466, second full paragraph", 211, []),
        ("p. 467, footnote 11", 212, ["C54"]),
        ("p. 471, first full paragraph", 213, []),
        ("p. 473, footnote 13", 214, ["C55"]),
        ("p. 477, first full paragraph", 215, ["F124", "C56"]),
        ("p. 478, first full paragraph", 216, ["F125", "C57"]),
        ("p. 479, first full paragraph", 217, ["C58"]),
        ("pp. 481–482, the paragraph that runs over the page", 218, ["C59"]),
        ("p. 482, Figure 2", 219, ["C60"]),
        ("pp. 486–487, the paragraph that runs over the page", 220, []),
    ],
}
# The records each coverage chat added, as its log's section "Added records" or "New fragments" and "New claims"
# lists them: every one must be in DECISIONS once.
# The first returns' counts: a fragment or claim numbered above them was added by a coverage chat.
FIRST_COUNTS = {"bechky": (168, 23), "pratt": (121, 52)}
ADDED = {"bechky": ["F169", "F170", "F171", "F172"],
         "pratt": ["F122", "F123", "F124", "F125", "C53", "C54", "C55", "C56", "C57", "C58", "C59", "C60"]}

SHEET_LINE3 = re.compile(r"^(\*Made by `coverage_sheet\.py` from `[^`]+` \(sha256 [0-9a-f]{64}\)\. )"
                         r"Who may receive this file: nobody \(—\)\. It is for the PI's coverage check, and it goes "
                         r"into no chat\.\*$")
SHEET_LINE3_NEW = "This copy is for checking the index against the paper.*"


def here(name):
    return os.path.join(HERE, name)


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def source(name):
    """The bytes of a source, after checking its sha256."""
    path = here(name)
    got = sha(path)
    if got != SHA[name]:
        raise SystemExit(f"{name}: sha256 {got}, not {SHA[name]}")
    return open(path, "rb").read()


def write_new(path, data):
    if os.path.exists(path):
        raise SystemExit(f"refusing to write over {path}")
    with open(path, "wb") as f:
        f.write(data)
    print(f"written: {path} ({len(data)} bytes, sha256 {hashlib.sha256(data).hexdigest()})")


# ---------------------------------------------------------------- places

PAGE = re.compile(r"\bpp?\.\s*(\d{1,4})(?:\s*[–—-]\s*(\d{1,4}))?|\bpages?\s+(\d{1,4})(?:\s*[–—-]\s*(\d{1,4}))?",
                  re.IGNORECASE)


def pages_of(where):
    """The pages a place names, first to last, from its first page reference; [] if it names none."""
    m = PAGE.search(where or "")
    if not m:
        return []
    a = int(m.group(1) or m.group(3))
    b = m.group(2) or m.group(4)
    if b is None:
        return [a]
    b = int(b)
    if b < a and len(str(b)) < len(str(a)):          # "612-13"
        b = int(str(a)[:len(str(a)) - len(str(b))] + str(b))
    return list(range(a, b + 1)) if a <= b <= a + 5 else [a]


def kind_of(where):
    w = (where or "").casefold()
    for k, words in (("footnote", ("footnote", "note ")), ("table", ("table",)), ("figure", ("figure", "fig.")),
                     ("abstract", ("abstract",)), ("caption", ("caption",))):
        if any(x in w for x in words):
            return k
    return "paragraph"


def in_range(paper, pages):
    lo, hi = RANGE[paper]
    return bool(pages) and all(lo <= p <= hi for p in pages)


# ---------------------------------------------------------------- the files of round 1

def sheet_copy(paper):
    text = source(SHEET[paper]).decode("utf-8")
    lines = text.split("\n")
    m = SHEET_LINE3.match(lines[2])
    if not m:
        raise SystemExit(f"{SHEET[paper]}: its third line is not the one this script replaces")
    lines[2] = m.group(1) + SHEET_LINE3_NEW
    out = "\n".join(lines)
    assert out.count("PI") == 0, "the copy still names the PI"
    return out.encode("utf-8")


def pi_lines(paper):
    """The PI's lines, as the PI wrote them: [(list line, text)], Bechky's duplicate left out; and the duplicate."""
    raw = source(LIST[paper]).decode("utf-8").split("\n")
    lines = [(i, t) for i, t in enumerate(raw, 1) if t.strip()]
    dup = None
    if paper == "bechky":
        assert len(lines) == 16 and lines[14][1] == lines[15][1], "Bechky's list is not as recorded"
        dup = {"list_line": 16, "same_as_list_line": 15}
        lines = lines[:15]
    else:
        assert len(lines) == 14, "Pratt's list is not as recorded"
    return lines, dup


def q_part():
    text = source(TWO_LISTS).decode("utf-8")
    i = text.index("\n## List Q\n") + 1
    return text[i:]


def q_ids():
    t = q_part()
    return set(re.findall(r"\*\*(QP\d{3})\*\*", t)), set(re.findall(r"\*\*(QC\d{2})\*\*", t))


def matcher_file():
    lines, _ = pi_lines("bechky")
    head = ["# Fifteen passages of a paper, and list Q", "",
            "The lines L01 to L15 each name a passage of the paper by its page and its place on the page. List Q is "
            "a record of the paper made separately. What to do with them is in `MATCH_PASSAGES_TO_Q.md`.", "",
            "## The passages", ""]
    head += [f"- **{lid}** · {t}" for lid, (_, t) in zip(MATCHER_LINES, lines)]
    return ("\n".join(head) + "\n\n" + q_part()).encode("utf-8")


def files(out):
    os.makedirs(out, exist_ok=True)
    for paper in PAPERS:
        write_new(os.path.join(out, f"CHECK_SHEET_{paper}.md"), sheet_copy(paper))
    write_new(os.path.join(out, "PASSAGES_AND_Q_bechky.md"), matcher_file())


# ---------------------------------------------------------------- the key

def check_decisions(paper):
    log = source(LOG[paper]).decode("utf-8").split("\n")
    lines, _ = pi_lines(paper)
    dec = DECISIONS[paper]
    assert [t for _, t in lines] == [t for t, _, _ in dec], f"{paper}: DECISIONS is not the PI's list, line for line"
    start = log.index("## Coverage additions")
    for text, ln, added in dec:
        row = log[ln - 1]
        assert ln - 1 > start and row.startswith("- **"), f"{paper}: log line {ln} is not an answer to a line"
        pg = pages_of(text)
        assert pages_of(row) == pg, f"{paper}: log line {ln} is not about {text!r}"
        for r in added:
            assert re.search(r"\b%s\b" % r, row), f"{paper}: log line {ln} does not name {r}"
    named = [r for _, _, a in dec for r in a]
    assert sorted(named) == sorted(ADDED[paper]) and len(set(named)) == len(named), f"{paper}: added records"
    section = "\n".join(log[start:])
    nf, nc = FIRST_COUNTS[paper]
    found = {r for r in re.findall(r"\b([FC]\d+)\b", section)
             if (r[0] == "F" and int(r[1:]) > nf) or (r[0] == "C" and int(r[1:]) > nc)}
    assert found == set(ADDED[paper]), f"{paper}: the log's added records {sorted(found)} are not ADDED"


def draw():
    rng = random.Random(SEED)
    return {paper: rng.randrange(2) == 0 for paper in PAPERS}


def key_data():
    pi_a = draw()
    out = {"what": "the key of the completeness test (T38): the PI's lines, the coverage chats' decisions on them, "
                   "and which of the judges' two lists is the PI's; for nobody",
           "plan": "COMPLETENESS_TEST_PLAN.md", "seed": SEED,
           "draw": "random.Random(20261024): for bechky, then pratt, the PI's list is list A when randrange(2) gives 0",
           "sources": {n: SHA[n] for n in sorted(SHA)}, "builder_sha256": sha(os.path.abspath(__file__)),
           "papers": {}}
    for paper in PAPERS:
        check_decisions(paper)
        lines, dup = pi_lines(paper)
        rows = []
        for i, ((ln, text), (_, logline, added)) in enumerate(zip(lines, DECISIONS[paper]), 1):
            rows.append({"id": "H%02d" % i, "list_line": ln, "line": text, "pages": pages_of(text),
                         "kind": kind_of(text), "coverage_added": added, "coverage_log_line": logline})
        out["papers"][paper] = {"range": list(RANGE[paper]), "lines": rows, "duplicate": dup,
                                "pi_is_list_A": pi_a[paper]}
    out["matcher"] = {lid: "H%02d" % i for i, lid in enumerate(MATCHER_LINES, 1)}
    return out


def key(path):
    data = key_data()
    write_new(path, (json.dumps(data, ensure_ascii=False, indent=1) + "\n").encode("utf-8"))
    for paper in PAPERS:
        p = data["papers"][paper]
        print(f"{paper}: {len(p['lines'])} lines, {sum(bool(r['coverage_added']) for r in p['lines'])} with an "
              f"addition; the PI's list is list {'A' if p['pi_is_list_A'] else 'B'}")


# ---------------------------------------------------------------- the checks

def report_spans(rep, paper):
    spans = bcs.long_spans(rep, bcs.citation(paper))
    for where, words, unclosed, inside in spans:
        print(f"  QUOTED SPAN over {bcs.MAX_QUOTE} words: {where}: {words} words"
              f"{', unclosed' if unclosed else ''}{', within the citation' if inside else ''}")
    return spans


def checker_faults(rep, paper):
    if not isinstance(rep, dict):
        return ["not a JSON object"], []
    ps = rep.get("passages")
    if not isinstance(ps, list):
        return ["`passages` is not a list"], []
    faults, remarks = [], []
    seen = {}
    for i, p in enumerate(ps, 1):
        if not isinstance(p, dict):
            faults.append(f"passage {i}: not an object")
            continue
        w = p.get("where")
        if not isinstance(w, str) or not w.strip():
            faults.append(f"passage {i}: no `where`")
            continue
        if p.get("test") not in TESTS:
            faults.append(f"passage {i}: `test` {p.get('test')!r} is not one of {', '.join(TESTS)}")
        if not isinstance(p.get("reason"), str) or not p["reason"].strip():
            faults.append(f"passage {i}: no `reason`")
        if p.get("n") != i:
            remarks.append(f"passage {i}: `n` is {p.get('n')!r}")
        if not in_range(paper, pages_of(w)):
            remarks.append(f"passage {i}: its `where` names no page of the paper")
        if len(w.split()) > 20:
            remarks.append(f"passage {i}: its `where` runs to {len(w.split())} words, more than a page and a place")
        key_w = " ".join(w.split()).casefold()
        if key_w in seen:
            remarks.append(f"passage {i}: the same `where` as passage {seen[key_w]}")
        seen.setdefault(key_w, i)
    return faults, remarks


def check_checker(paper, path):
    rep, faults = bcs.load(path)
    remarks = []
    if not faults:
        faults, remarks = checker_faults(rep, paper)
    chat = {"bechky": "68", "pratt": "69"}[paper]
    print(f"chat {chat} ({paper}, the checker): {os.path.basename(path)}, sha256 {sha(path)}")
    if faults:
        for f in faults:
            print(f"  FAULT: {f}")
        print("  DOES NOT COUNT")
        return 1
    ps = rep["passages"]
    print(f"  paper field: {rep.get('paper')!r}; read_to: {rep.get('read_to')!r}")
    print(f"  passages: {len(ps)}; tests " + ", ".join(f"{t} {sum(p['test'] == t for p in ps)}" for t in TESTS))
    for r in remarks:
        print(f"  REMARK: {r}")
    if report_spans(rep, paper):
        print("  COUNTS; to be shown to the PI before it is filed (the plan): the spans above are not filed")
        return 2
    print("  COUNTS; no quoted span of more than eight words")
    return 0


def matcher_faults(rep):
    if not isinstance(rep, dict) or not isinstance(rep.get("lines"), dict):
        return ["not a JSON object with an object `lines`"]
    ls = rep["lines"]
    faults = []
    if sorted(ls) != list(MATCHER_LINES):
        missing = [k for k in MATCHER_LINES if k not in ls]
        extra = [k for k in ls if k not in MATCHER_LINES]
        faults.append(f"lines missing {missing}, lines not asked {extra}")
    qp, qc = q_ids()
    for k in MATCHER_LINES:
        e = ls.get(k)
        if e is None:
            continue
        if not isinstance(e, dict) or not isinstance(e.get("found"), bool):
            faults.append(f"{k}: not an object with a true or false `found`")
            continue
        for field, ids, what in (("passages", qp, "QP"), ("claims", qc, "QC")):
            v = e.get(field)
            if not isinstance(v, list) or not all(isinstance(x, str) for x in v):
                faults.append(f"{k}: `{field}` is not a list of ids")
                continue
            bad = [x for x in v if x not in ids]
            if bad:
                faults.append(f"{k}: `{field}` names {bad}, not {what} ids of list Q")
            if len(set(v)) != len(v):
                faults.append(f"{k}: `{field}` names an id twice")
        if not e["found"] and (e.get("passages") or e.get("claims")):
            faults.append(f"{k}: not found, yet it names ids")
        if not isinstance(e.get("reason"), str) or not e["reason"].strip():
            faults.append(f"{k}: no `reason`")
    return faults


def check_matcher(key_path, path):
    json.load(open(key_path, encoding="utf-8"))
    rep, faults = bcs.load(path)
    faults = faults or matcher_faults(rep)
    print(f"chat 70 (bechky, the matcher): {os.path.basename(path)}, sha256 {sha(path)}")
    if faults:
        for f in faults:
            print(f"  FAULT: {f}")
        print("  DOES NOT COUNT")
        return 1
    ls = rep["lines"]
    print(f"  lines: {len(ls)}; found {sum(e['found'] for e in ls.values())}; with a passage of Q "
          f"{sum(bool(e['passages']) for e in ls.values())}; with a claim of Q {sum(bool(e['claims']) for e in ls.values())}")
    if report_spans(rep, "bechky"):
        print("  COUNTS; to be shown to the PI before it is filed (the plan): the spans above are not filed")
        return 2
    print("  COUNTS; no quoted span of more than eight words")
    return 0


# ---------------------------------------------------------------- the judges' lists (after round 1)

def checker_lines(paper, path):
    rep, faults = bcs.load(path)
    if not faults:
        faults, _ = checker_faults(rep, paper)
    if faults:
        raise SystemExit(f"{paper}: the checker's reply does not count: {faults}")
    if bcs.long_spans(rep, bcs.citation(paper)):
        raise SystemExit(f"{paper}: the checker's reply holds a quoted span of more than eight words; "
                         f"the plan shows it to the PI first")
    return [" ".join(p["where"].split()) for p in rep["passages"]]


def lists_data(key_path, paths):
    k = json.load(open(key_path, encoding="utf-8"))
    out = {"what": "which line of the judges' two lists is whose; for nobody", "key_sha256": sha(key_path),
           "replies": {}, "papers": {}}
    texts = {}
    for paper, path in zip(PAPERS, paths):
        out["replies"][paper] = {"file": os.path.basename(path), "sha256": sha(path)}
        kp = k["papers"][paper]
        pis = [(r["id"], r["line"]) for r in kp["lines"]]
        its = [(i, w) for i, w in enumerate(checker_lines(paper, path), 1)]
        a_src, b_src = (("pi", pis), ("checker", its)) if kp["pi_is_list_A"] else (("checker", its), ("pi", pis))
        lines = {}
        md = [f"# Two lists of passages of one paper: A and B", "",
              "Each line names a passage of the paper by its page and its place on the page, and nothing else. The "
              "two lists were made separately. What to do with them is in `JUDGE_MISSES.md`.", ""]
        for letter, (who, items) in (("A", a_src), ("B", b_src)):
            md += [f"## List {letter} ({len(items)} lines)", ""]
            for j, (src_id, text) in enumerate(items, 1):
                lid = "%s%02d" % (letter, j)
                lines[lid] = {"source": who, "id": src_id, "line": text}
                md.append(f"- **{lid}** · {text}")
            md.append("")
        out["papers"][paper] = {"pi_list": "A" if kp["pi_is_list_A"] else "B", "lines": lines}
        texts[paper] = "\n".join(md).rstrip("\n") + "\n"
    return out, texts


def lists(key_path, path_b, path_p, outdir):
    data, texts = lists_data(key_path, (path_b, path_p))
    os.makedirs(outdir, exist_ok=True)
    for paper in PAPERS:
        write_new(os.path.join(outdir, f"TWO_PASSAGE_LISTS_{paper}.md"), texts[paper].encode("utf-8"))
    write_new(os.path.join(outdir, "completeness_lists_key.json"),
              (json.dumps(data, ensure_ascii=False, indent=1) + "\n").encode("utf-8"))


def first_ids(paper):
    c = json.loads(source(FIRST[paper]).decode("utf-8"))
    return {f["fragment_id"] for f in c["fragments"]} | {x["claim_id"] for x in c["claims"]}


def judge_faults(rep, line_ids, paper):
    if not isinstance(rep, dict):
        return ["not a JSON object"], []
    faults, remarks = [], []
    pairs, verdicts = rep.get("pairs"), rep.get("verdicts")
    if not isinstance(pairs, list):
        faults.append("`pairs` is not a list")
        pairs = []
    if not isinstance(verdicts, dict):
        faults.append("`verdicts` is not an object")
        verdicts = {}
    a_ids = {x for x in line_ids if x.startswith("A")}
    b_ids = {x for x in line_ids if x.startswith("B")}
    seen = set()
    for i, p in enumerate(pairs, 1):
        if not (isinstance(p, list) and len(p) == 2 and p[0] in a_ids and p[1] in b_ids):
            faults.append(f"pair {i}: {p!r} is not [an A line, a B line] of the lists")
            continue
        if tuple(p) in seen:
            faults.append(f"pair {i}: {p!r} given twice")
        seen.add(tuple(p))
    if verdicts and sorted(verdicts) != sorted(line_ids):
        faults.append(f"verdicts missing {sorted(set(line_ids) - set(verdicts))}, "
                      f"not of the lists {sorted(set(verdicts) - set(line_ids))}")
    known = first_ids(paper)
    for lid in sorted(verdicts):
        v = verdicts[lid]
        if not isinstance(v, dict) or v.get("verdict") not in VERDICTS:
            faults.append(f"{lid}: no verdict of the six")
            continue
        ids = v.get("ids")
        if not isinstance(ids, list) or not all(isinstance(x, str) for x in ids):
            faults.append(f"{lid}: `ids` is not a list of strings")
            continue
        if v["verdict"] == "covered" and not ids:
            faults.append(f"{lid}: covered, and no id named")
        if not isinstance(v.get("reason"), str) or not v["reason"].strip():
            faults.append(f"{lid}: no `reason`")
        odd = [x for x in ids if x.strip() not in known]
        if odd:
            remarks.append(f"{lid}: ids not of the first return's fragments or claims: {odd}")
    return faults, remarks


def check_judge(lists_key, paper, path):
    lk = json.load(open(lists_key, encoding="utf-8"))
    line_ids = sorted(lk["papers"][paper]["lines"])
    rep, faults = bcs.load(path)
    remarks = []
    if not faults:
        faults, remarks = judge_faults(rep, line_ids, paper)
    chat = {"bechky": "71", "pratt": "72"}[paper]
    print(f"chat {chat} ({paper}, the judge): {os.path.basename(path)}, sha256 {sha(path)}")
    if faults:
        for f in faults:
            print(f"  FAULT: {f}")
        print("  DOES NOT COUNT")
        return 1
    vs = rep["verdicts"]
    print(f"  pairs: {len(rep['pairs'])}; verdicts: {len(vs)}; " +
          ", ".join(f"{v} {sum(x['verdict'] == v for x in vs.values())}" for v in VERDICTS))
    for r in remarks:
        print(f"  REMARK: {r}")
    if report_spans(rep, paper):
        print("  COUNTS; to be shown to the PI before it is filed (the plan): the spans above are not filed")
        return 2
    print("  COUNTS; no quoted span of more than eight words")
    return 0


# ---------------------------------------------------------------- the self-test

def selftest():
    import tempfile
    ok = True

    def expect(label, cond):
        nonlocal ok
        print(("ok    " if cond else "FAIL  ") + label)
        ok = ok and cond

    expect("pages: p. 612", pages_of("p. 612, footnote 1") == [612])
    expect("pages: pp. 606–607", pages_of("pp. 606–607, the paragraph that runs over the page") == [606, 607])
    expect("pages: pp. 612-13", pages_of("pp. 612-13, the paragraph") == [612, 613])
    expect("pages: page 480", pages_of("page 480, Table 3") == [480])
    expect("pages: none", pages_of("the second paragraph") == [])
    expect("kind: footnote", kind_of("p. 612, footnote 1") == "footnote")
    expect("kind: table", kind_of('p. 633, Table 2, row "Values"') == "table")
    expect("kind: figure", kind_of("p. 482, Figure 2") == "figure")
    expect("kind: paragraph", kind_of("p. 607, second full paragraph") == "paragraph")
    for paper in PAPERS:
        s = sheet_copy(paper).decode("utf-8").split("\n")
        o = source(SHEET[paper]).decode("utf-8").split("\n")
        expect(f"{paper}: the sheet's copy differs in its third line alone",
               len(s) == len(o) and [i for i, (x, y) in enumerate(zip(s, o)) if x != y] == [2])
        try:
            check_decisions(paper)
            expect(f"{paper}: DECISIONS agrees with the list and the log", True)
        except AssertionError as e:
            expect(f"{paper}: DECISIONS agrees with the list and the log ({e})", False)
    m = matcher_file().decode("utf-8")
    expect("the matcher's file ends with list Q, byte for byte", m.endswith(q_part()) and m.count("**L") == 15)
    qp, qc = q_ids()
    expect("list Q: 168 passages and 39 claims", len(qp) == 168 and len(qc) == 39)
    k = key_data()
    expect("the draw: the PI's list is A for both papers, as random.Random(20261024) gives",
           draw() == {"bechky": True, "pratt": True} and all(k["papers"][p]["pi_is_list_A"] for p in PAPERS))
    expect("the key: 15 and 14 lines, 4 and 10 with an addition",
           [len(k["papers"][p]["lines"]) for p in PAPERS] == [15, 14] and
           [sum(bool(r["coverage_added"]) for r in k["papers"][p]["lines"]) for p in PAPERS] == [4, 10])
    with tempfile.TemporaryDirectory() as td:
        def put(name, obj):
            p = os.path.join(td, name)
            with open(p, "w", encoding="utf-8") as f:
                f.write(obj if isinstance(obj, str) else json.dumps(obj))
            return p
        kp = put("key.json", k)
        good_b = {"paper": "x", "read_to": "p. 643", "passages": [
            {"n": 1, "where": "p. 607, second full paragraph", "test": "assertion", "reason": "r"},
            {"n": 2, "where": "p. 620, footnote 3", "test": "evidence", "reason": "r"}]}
        good_p = {"paper": "x", "read_to": "p. 493", "passages": [
            {"n": 1, "where": "p. 459, third full paragraph", "test": "evidence", "reason": "r"}]}
        pb, pp = put("cb.json", "Here it is:\n```json\n" + json.dumps(good_b) + "\n```"), put("cp.json", good_p)
        expect("checker: a good reply counts", check_checker("bechky", pb) == 0)
        bad = json.loads(json.dumps(good_b))
        bad["passages"][1]["test"] = "maybe"
        expect("checker: an unknown test does not count", check_checker("bechky", put("bad1.json", bad)) == 1)
        bad = json.loads(json.dumps(good_b))
        del bad["passages"][0]["reason"]
        expect("checker: a missing reason does not count", check_checker("bechky", put("bad2.json", bad)) == 1)
        long = json.loads(json.dumps(good_b))
        long["passages"][0]["reason"] = 'it says "one two three four five six seven eight nine ten" there'
        expect("checker: a long quoted span is named", check_checker("bechky", put("long.json", long)) == 2)
        wordy = json.loads(json.dumps(good_b))
        wordy["passages"][0]["where"] = "p. 607, second full paragraph, " + "where the author says a great deal " * 3
        _, rem = checker_faults(wordy, "bechky")
        expect("checker: a long `where` is a remark", any("more than a page and a place" in r for r in rem))
        off = json.loads(json.dumps(good_b))
        off["passages"][0]["where"] = "p. 12, first full paragraph"
        _, rem = checker_faults(off, "bechky")
        expect("checker: a page outside the paper is a remark", any("names no page" in r for r in rem))
        out = os.path.join(td, "lists")
        lists(kp, pb, pp, out)
        lk = json.load(open(os.path.join(out, "completeness_lists_key.json"), encoding="utf-8"))
        lb = lk["papers"]["bechky"]["lines"]
        expect("lists: Bechky has 15 + 2 lines", len(lb) == 17)
        pi_letter = lk["papers"]["bechky"]["pi_list"]
        expect("lists: the PI's lines are the drawn list", all(v["source"] == "pi" for x, v in lb.items()
                                                        if x.startswith(pi_letter)))
        md = open(os.path.join(out, "TWO_PASSAGE_LISTS_bechky.md"), encoding="utf-8").read()
        expect("lists: the file holds no reason and no test", "assertion" not in md and "evidence" not in md)
        a1 = sorted(x for x in lb if x.startswith("A"))[0]
        b1 = sorted(x for x in lb if x.startswith("B"))[0]
        verdicts = {x: {"verdict": "covered", "ids": ["F01"], "reason": "r"} for x in lb}
        jgood = {"pairs": [[a1, b1]], "verdicts": verdicts}
        lkp = os.path.join(out, "completeness_lists_key.json")
        expect("judge: a good reply counts", check_judge(lkp, "bechky", put("j.json", jgood)) == 0)
        jbad = json.loads(json.dumps(jgood))
        jbad["pairs"] = [[b1, a1]]
        expect("judge: a pair B first does not count", check_judge(lkp, "bechky", put("j2.json", jbad)) == 1)
        jbad = json.loads(json.dumps(jgood))
        del jbad["verdicts"][a1]
        expect("judge: a missing verdict does not count", check_judge(lkp, "bechky", put("j3.json", jbad)) == 1)
        jbad = json.loads(json.dumps(jgood))
        jbad["verdicts"][a1] = {"verdict": "covered", "ids": [], "reason": "r"}
        expect("judge: covered with no id does not count", check_judge(lkp, "bechky", put("j4.json", jbad)) == 1)
        jodd = json.loads(json.dumps(jgood))
        jodd["verdicts"][a1]["ids"] = ["F999"]
        f, rem = judge_faults(jodd, sorted(lb), "bechky")
        expect("judge: an unknown id is a remark", not f and rem)
        mgood = {"lines": {x: {"found": True, "passages": ["QP001"], "claims": [], "reason": "r"} for x in MATCHER_LINES}}
        expect("matcher: a good reply counts", check_matcher(kp, put("m.json", mgood)) == 0)
        mbad = json.loads(json.dumps(mgood))
        mbad["lines"]["L03"]["passages"] = ["QP999"]
        expect("matcher: an id not in list Q does not count", check_matcher(kp, put("m2.json", mbad)) == 1)
        mbad = json.loads(json.dumps(mgood))
        del mbad["lines"]["L15"]
        expect("matcher: a missing line does not count", check_matcher(kp, put("m3.json", mbad)) == 1)
        mbad = json.loads(json.dumps(mgood))
        mbad["lines"]["L02"]["found"] = False
        expect("matcher: not found with ids does not count", check_matcher(kp, put("m4.json", mbad)) == 1)
    print("SELFTEST PASSES" if ok else "SELFTEST FAILS")
    return 0 if ok else 1


def main(argv):
    if argv[1:] == ["--selftest"]:
        return selftest()
    cmd = argv[1] if len(argv) > 1 else ""
    if cmd == "files" and len(argv) == 3:
        files(argv[2])
    elif cmd == "key" and len(argv) == 3:
        key(argv[2])
    elif cmd == "check-checker" and len(argv) == 4 and argv[2] in PAPERS:
        return check_checker(argv[2], argv[3])
    elif cmd == "check-matcher" and len(argv) == 4:
        return check_matcher(argv[2], argv[3])
    elif cmd == "lists" and len(argv) == 6:
        lists(argv[2], argv[3], argv[4], argv[5])
    elif cmd == "check-judge" and len(argv) == 5 and argv[3] in PAPERS:
        return check_judge(argv[2], argv[3], argv[4])
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
