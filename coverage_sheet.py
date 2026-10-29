#!/usr/bin/env python3
"""
A reading sheet for the PI's coverage check of a cold paper.

WHY
---
After a cold paper's first return the PI reads the paper section by section and
lists the passages that produced no fragment or no claim. The returned corpus
is a JSON file in the order of its records, not of
the paper's pages. This script lays the same records out page by page, so that
the PI can read them beside the paper. It adds nothing and judges nothing.

USAGE
-----
    python3 -B coverage_sheet.py <corpus.json> <out.md>
    python3 -B coverage_sheet.py --selftest

It refuses to write over a file that exists. The same corpus always gives the
same sheet, byte for byte: the sheet carries the corpus's hash and no date.

WHAT THE SHEET HOLDS
--------------------
First the claims in full, to be read once before the pages. Then, for every
printed page of the paper, first to last: the claims the extraction locates on
it, each with its statement, and the fragments located on it, in the
extraction's own order, each with its location, its unit, its speaker where
one is named, its stub and, where it has one, its gloss. Pages with no
fragment, and pages with neither a fragment nor a claim, are listed at the
head. Last come the declared gaps, the absences, the contrast pairs, and what
the corpus keeps outside the fragments (the scale of the fieldwork).

A corpus records a page for each record and never a paragraph, so the sheet
cannot say which paragraph a record comes from. It does say whether the
fragments' numbering follows the pages, since then the fragments under a page
can be ticked off in the order of the page.

It holds no link, no direction, no basis and no voice code: the check is of
coverage only.

Changed on 6 Oct 2026, the day it was written, after a first look at a
sheet: the claims moved to the front, each page gives its claims in words and
no longer by id alone, and the sheet says what the order of the fragments is
worth.

WHO MAY RECEIVE THE SHEET
-------------------------
Nobody but the PI. It shows the extraction's records, so it goes into no chat:
not the coverage chat, and not a coder's.

On the terminal the script prints counts and ids only, never a stub.
"""
import hashlib
import json
import os
import re
import sys

PAGE = re.compile(r"\bpp?\.\s*(\d+)(?:\s*[–—-]\s*(\d+))?")
CITED_RANGE = re.compile(r":\s*(\d+)\s*[–—-]\s*(\d+)\.?\s*$")


def pages_of(location):
    """The printed pages a location names, ranges spelled out, in order."""
    out = []
    for m in PAGE.finditer(location or ""):
        a = int(m.group(1))
        b = int(m.group(2)) if m.group(2) else a
        if b < a:
            raise SystemExit(f"a page range runs backwards: {location!r}")
        for p in range(a, b + 1):
            if p not in out:
                out.append(p)
    return out


def paper_range(corpus):
    """First and last printed page, from the citation; else from the records."""
    m = CITED_RANGE.search(corpus["meta"].get("citation") or "")
    if m:
        return int(m.group(1)), int(m.group(2)), True
    cited = [p for f in corpus["fragments"] for p in pages_of(f["location"])]
    cited += [p for c in corpus["claims"] for p in pages_of(c["location"])]
    if not cited:
        raise SystemExit("no page is cited anywhere in the corpus")
    return min(cited), max(cited), False


def runs(pages):
    """[606, 607, 608, 612] -> 'pp. 606–608, p. 612'."""
    pages = sorted(pages)
    if not pages:
        return "none"
    out, start, prev = [], pages[0], pages[0]
    for p in pages[1:] + [None]:
        if p is not None and p == prev + 1:
            prev = p
            continue
        out.append(f"p. {start}" if start == prev else f"pp. {start}–{prev}")
        start = prev = p
    return ", ".join(out)


def one_line(text):
    return re.sub(r"\s+", " ", text or "").strip()


def build(corpus, corpus_name, corpus_sha):
    meta = corpus["meta"]
    frags, claims = corpus["fragments"], corpus["claims"]
    first, last, from_citation = paper_range(corpus)
    all_pages = list(range(first, last + 1))

    home = {}          # page -> fragments whose location begins there
    runs_on = {}       # page -> fragments that run on from an earlier page
    nowhere = []       # fragments whose location names no page
    for f in frags:
        ps = pages_of(f["location"])
        if not ps:
            nowhere.append(f["fragment_id"])
            continue
        home.setdefault(ps[0], []).append(f)
        for p in ps[1:]:
            runs_on.setdefault(p, []).append(f)
    claims_on = {}
    claims_nowhere = []
    for c in claims:
        ps = pages_of(c["location"])
        if not ps:
            claims_nowhere.append(c["claim_id"])
        for p in ps:
            claims_on.setdefault(p, []).append(c["claim_id"])
    gaps_on = {}
    for g in corpus.get("declared_gaps", []):
        for p in pages_of(g.get("location")):
            gaps_on.setdefault(p, []).append(g)

    outside = sorted(p for p in set(home) | set(runs_on) | set(claims_on) | set(gaps_on)
                     if p < first or p > last)
    if outside:
        raise SystemExit(f"pages cited outside the paper's range {first}–{last}: {outside}")

    with_fragment = set(home) | set(runs_on)
    no_fragment = [p for p in all_pages if p not in with_fragment]
    nothing = [p for p in no_fragment if p not in claims_on and p not in gaps_on]

    statement_of = {c["claim_id"]: one_line(c["statement"]) for c in claims}
    # does the fragments' numbering follow the pages? Each place where the next
    # fragment begins on an earlier page than the one before it is a step back.
    firsts = [(f["fragment_id"], pages_of(f["location"])) for f in frags]
    firsts = [(i, ps[0]) for i, ps in firsts if ps]
    backward = [b[0] for a, b in zip(firsts, firsts[1:]) if b[1] < a[1]]

    L = []
    add = L.append
    add(f"# {meta['paper_id']}: reading sheet for the coverage check")
    add("")
    add(f"*Made by `coverage_sheet.py` from `{corpus_name}` (sha256 {corpus_sha}). "
        "Who may receive this file: nobody (—). It is for the PI's coverage check, "
        "and it goes into no chat.*")
    add("")
    add(one_line(meta.get("citation")))
    add("")
    add("## How to read it")
    add("")
    add("- **Read the claims first, once.** They follow below, in full. A paper states "
        "its main claims on many pages, so the same few come round again and again.")
    add("- **Then the pages.** Under each printed page stand the claims that the "
        "extraction locates there, in words, and the fragments it took from that page.")
    add("- **The corpus records a page for each record, and never a paragraph.** So the "
        "sheet cannot say which paragraph a fragment or a claim comes from.")
    if not backward:
        add("- **The fragments are numbered in the order in which the extraction met them, "
            "and in this corpus their pages never go backwards.** So the fragments under a "
            "page should follow the page from top to bottom, and can be ticked off as the "
            "page is read.")
    else:
        times = "once" if len(backward) == 1 else f"{len(backward)} times"
        add("- **The fragments are numbered in the order in which the extraction recorded "
            f"them. In this corpus that order goes back to an earlier page {times}** (at "
            f"{', '.join(backward)}). So the order under a page is not a sure guide to the "
            "order on the page.")
    add("- A stub is the extractor's paraphrase of a passage, not the paper's words. A "
        "gloss is the paper's own later reading of that passage, where the extraction "
        "kept one; the corpus does not record the gloss's own page.")
    add("- A fragment is listed under the first page of its location. Where it runs on, "
        "the next page says so.")
    add("- The sheet shows what was recorded and where. It cannot show whether a record "
        "gives its passage rightly. The check is of coverage: a passage that prints "
        "evidence which no fragment gives, or asserts something which no claim gives.")
    add("")
    add("## At a glance")
    add("")
    add(f"- The paper: pp. {first}–{last}, {len(all_pages)} pages"
        + ("" if from_citation else " (taken from the records: the citation gives no page range)") + ".")
    add(f"- Fragments: {len(frags)}, on {len(with_fragment)} pages. Claims: {len(claims)}.")
    add(f"- **Pages with no fragment ({len(no_fragment)}):** {runs(no_fragment)}.")
    add(f"- **Pages with neither a fragment, a claim nor a declared gap ({len(nothing)}):** {runs(nothing)}.")
    if nowhere:
        add(f"- Fragments whose location names no page: {', '.join(nowhere)}.")
    if claims_nowhere:
        add(f"- Claims whose location names no page: {', '.join(claims_nowhere)}.")
    add("")
    add("## The claims")
    add("")
    for c in claims:
        tags = [c.get("stated_as") or "stated_as not given"]
        if c.get("core"):
            tags.insert(0, "core")
        add(f"- **{c['claim_id']}** · {one_line(c['location'])} · {', '.join(tags)}")
        add(f"  {one_line(c['statement'])}")
        add(f"  *outcome:* {one_line(c.get('outcome')) or 'none'}")
    add("")
    add("## Page by page")
    for p in all_pages:
        add("")
        add(f"### p. {p}")
        add("")
        cl = claims_on.get(p, [])
        if cl:
            add("Claims located here:")
            add("")
            for cid in cl:
                add(f"- {cid}: {statement_of[cid]}")
        else:
            add("Claims located here: none.")
        for g in gaps_on.get(p, []):
            add("")
            add(f"Declared gap located here: {g['gap_id']} ({one_line(g.get('location'))}).")
        add("")
        here, carried = home.get(p, []), runs_on.get(p, [])
        if not here and not carried:
            add("**No fragment is located on this page.**")
            continue
        add("Fragments located here:")
        add("")
        for f in carried:
            add(f"- {f['fragment_id']} runs on from p. {pages_of(f['location'])[0]}.")
        for f in here:
            head = f"- **{f['fragment_id']}** · {one_line(f['location'])} · {one_line(f.get('unit')) or 'no unit'}"
            if f.get("speaker_name"):
                head += f" · speaker: {one_line(f['speaker_name'])}"
            add(head)
            add(f"  {one_line(f['stub'])}")
            if f.get("author_gloss"):
                add(f"  *gloss:* {one_line(f['author_gloss'])}")
    add("")
    add("## Other records")
    add("")
    gaps = corpus.get("declared_gaps", [])
    add(f"**Declared gaps ({len(gaps)}).**")
    add("")
    for g in gaps:
        add(f"- **{g['gap_id']}** · {one_line(g.get('location')) or 'no location'} · "
            f"{g.get('kind') or 'no kind'} · bears on {', '.join(g.get('bears_on') or []) or 'no claim'}")
        if g.get("statement"):
            add(f"  {one_line(g['statement'])}")
    add("")
    absences = corpus.get("absences", [])
    add(f"**Absences ({len(absences)}).**")
    add("")
    for a in absences:
        add(f"- **{a['absence_id']}** · {one_line(a.get('evidence_class')) or 'no evidence class'} · "
            f"bears on {', '.join(a.get('bears_on') or []) or 'no claim'}")
    add("")
    pairs = corpus.get("contrast_pairs", [])
    add(f"**Contrast pairs ({len(pairs)}).**")
    add("")
    for pr in pairs:
        add(f"- **{pr['pair_id']}** · one side: {', '.join(pr.get('fragments_a') or []) or 'none'} · "
            f"other side: {', '.join(pr.get('fragments_b') or []) or 'none'}")
    add("")
    add("## Kept outside the fragments")
    add("")
    add("**The scale of the fieldwork,** as the corpus records it from the methods section:")
    add("")
    add(one_line(meta.get("fieldwork_scale")) or "nothing recorded.")
    add("")
    add(f"**Periods:** {', '.join(meta.get('periods') or []) or 'none'}. "
        f"**Resolution period:** {meta.get('resolution_period') or 'none'}.")
    add("")
    text = "\n".join(L)

    # the sheet must hold every record exactly once
    for f in frags:
        n = text.count(f"- **{f['fragment_id']}** ·")
        want = 0 if f["fragment_id"] in nowhere else 1
        if n != want:
            raise SystemExit(f"{f['fragment_id']} is listed {n} times, not {want}")
    for c in claims:
        if text.count(f"- **{c['claim_id']}** ·") != 1:
            raise SystemExit(f"{c['claim_id']} is not listed exactly once")
    stats = {
        "paper": f"{first}–{last}", "pages": len(all_pages), "fragments": len(frags),
        "claims": len(claims), "pages with a fragment": len(with_fragment),
        "pages with no fragment": no_fragment, "pages with nothing": nothing,
        "fragments with no page": nowhere, "claims with no page": claims_nowhere,
        "steps back in the fragments' page order": backward,
        "gaps": len(gaps), "absences": len(absences), "pairs": len(pairs),
    }
    return text, stats


def selftest():
    corpus = {
        "meta": {"paper_id": "made_up", "citation": "Nobody, N. 2000. A made-up paper. Journal, 1(1): 10–14.",
                 "periods": ["P1"], "resolution_period": None, "fieldwork_scale": "Three weeks."},
        "fragments": [
            {"fragment_id": "F01", "location": "p. 10", "unit": "bakers", "speaker_name": None,
             "stub": "A baker opened the shop early.", "author_gloss": None},
            {"fragment_id": "F02", "location": "pp. 10–11", "unit": "bakers", "speaker_name": "Ada",
             "stub": "Ada said the ovens were cold.", "author_gloss": "A reading of it."},
            {"fragment_id": "F03", "location": "Table 1, Staff — bakers, p. 13", "unit": "bakers",
             "speaker_name": None, "stub": "Table 1 gives four bakers.", "author_gloss": None},
        ],
        "claims": [
            {"claim_id": "C01", "location": "p. 10; pp. 13–14", "statement": "Cold ovens delay opening.",
             "outcome": "time of opening", "core": True, "stated_as": "established"},
            {"claim_id": "C02", "location": "p. 14", "statement": "Bakers adapt.", "outcome": None,
             "core": False, "stated_as": "ventured"},
        ],
        "declared_gaps": [{"gap_id": "DG01", "location": "p. 14, footnote 2", "kind": "scope_limit",
                           "bears_on": ["C01"], "statement": "One shop only."}],
        "absences": [{"absence_id": "A01", "evidence_class": "sales figures", "bears_on": ["C01"]}],
        "contrast_pairs": [{"pair_id": "CP01", "fragments_a": ["F01"], "fragments_b": ["F02"]}],
    }
    text, stats = build(corpus, "made_up.json", "0" * 64)
    checks = [
        ("page range from the citation", stats["paper"] == "10–14" and stats["pages"] == 5),
        ("pages with no fragment", stats["pages with no fragment"] == [12, 14]),
        ("pages with nothing", stats["pages with nothing"] == [12]),
        ("a fragment is listed once, under its first page",
         text.count("- **F02** ·") == 1 and text.index("- **F02** ·") < text.index("### p. 11")),
        ("a fragment that runs on is named on the next page", "- F02 runs on from p. 10." in text),
        ("a table cell is placed by its page", text.index("### p. 13") < text.index("- **F03** ·")),
        ("claims are given in words on every page of a range",
         "### p. 13\n\nClaims located here:\n\n- C01: Cold ovens delay opening.\n" in text
         and "### p. 14\n\nClaims located here:\n\n- C01: Cold ovens delay opening.\n- C02: Bakers adapt.\n" in text),
        ("the claims in full stand before the pages, each once",
         text.index("## The claims") < text.index("## Page by page")
         and text.count("- **C01** ·") == 1 and text.index("- **C01** ·") < text.index("## Page by page")),
        ("a page's fragments have their own heading", "Fragments located here:\n\n- **F01** ·" in text),
        ("the sheet says that the fragments' pages never go backwards",
         "their pages never go backwards" in text and stats["steps back in the fragments' page order"] == []),
        ("an empty page says so", "### p. 12\n\nClaims located here: none.\n\n**No fragment is located on this page.**" in text),
        ("the gloss and the speaker are shown", "*gloss:* A reading of it." in text and "speaker: Ada" in text),
        ("a gap is placed by its page", "Declared gap located here: DG01 (p. 14, footnote 2)." in text),
        ("runs of pages", runs([606, 607, 608, 612]) == "pp. 606–608, p. 612" and runs([]) == "none"),
        ("no link, basis or voice code is printed",
         not re.search(r"\b(basis|direction|illustrates|qualifies|author_insight)\b", text)),
        ("the same corpus gives the same sheet", build(corpus, "made_up.json", "0" * 64)[0] == text),
    ]
    bad = dict(corpus, fragments=corpus["fragments"] + [
        {"fragment_id": "F04", "location": "p. 99", "unit": "x", "speaker_name": None, "stub": "x", "author_gloss": None}])
    try:
        build(bad, "made_up.json", "0" * 64)
        checks.append(("a page outside the paper is refused", False))
    except SystemExit:
        checks.append(("a page outside the paper is refused", True))
    late = dict(corpus, fragments=corpus["fragments"] + [
        {"fragment_id": "F04", "location": "p. 11", "unit": "bakers", "speaker_name": None,
         "stub": "A late addition.", "author_gloss": None}])
    late_text, late_stats = build(late, "made_up.json", "0" * 64)
    checks.append(("a fragment numbered after a later page is named as a step back",
                   late_stats["steps back in the fragments' page order"] == ["F04"]
                   and "goes back to an earlier page once** (at F04)" in late_text
                   and "never go backwards" not in late_text))
    for name, ok in checks:
        print(("ok    " if ok else "FAILED") + "  " + name)
    if all(ok for _, ok in checks):
        print(f"selftest: all {len(checks)} checks pass")
        return 0
    print("selftest: FAILED")
    return 1


def main(argv):
    if argv[1:] == ["--selftest"]:
        return selftest()
    if len(argv) != 3:
        print(__doc__)
        return 2
    src, out = argv[1], argv[2]
    if os.path.exists(out):
        raise SystemExit(f"{out} exists already, and is not written over")
    raw = open(src, "rb").read()
    corpus = json.loads(raw.decode("utf-8"))
    text, stats = build(corpus, os.path.basename(src), hashlib.sha256(raw).hexdigest())
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(text)
    for k, v in stats.items():
        print(f"{k}: {v}")
    print(f"written: {out} ({len(text.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
