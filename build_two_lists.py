"""
Build the matchers' file of the second extraction of Bechky (T35), by
SECOND_EXTRACTION_PLAN.md. Written on 15 Oct 2026, before the new return was
opened.

    python3 -B build_two_lists.py selftest
    python3 -B build_two_lists.py build --seed=20261018 --first=CORPUS,VOICE --new=CORPUS,VOICE
        --out=DIR [--descriptions=JSON]

build writes two files into DIR:

- TWO_LISTS_bechky.md, for the two matcher chats (56 and 57), with
  MATCH_TWO_LISTS.md and the paper's PDF: the two returns as list P and list Q.
- two_lists_key.json, for nobody: which return is P, the hashes of the four
  source files and of the lists file, and for every new id the return and the
  id it stands for, with what the scorer needs (pages, table, voice, core,
  stated_as) and both returns' links.

Which return is P: random.Random(seed).choice(["first", "new"]).

In each list, and nothing else of either return:

- the claims, numbered PC01, PC02, ... (QC01, ... in list Q), in the order of
  the lowest page their location names (a tie keeps the return's own order; a
  claim whose location names no page goes last, in that order), each with its
  location as the return gives it and its statement;
- the passages, numbered PP001, PP002, ... (QP001, ...), page by page: by the
  lowest page the location names (a tie keeps the return's order; a passage
  with no page keeps the page of the one before it in the return, as the
  coders' packs do), each with its location as the return gives it and its
  stub with the opening
  that marks the author's voice removed by the rule of the coders' packs
  (build_cold_pack.v_description, as for Stage V). A stub that rule refuses
  (empty, or still opening with a voice cue, once the cue is removed) stops the
  build, unless --descriptions gives its replacement, {"first:F12": "...",
  "new:F07": "..."}, which is checked the same way. Its warnings (a reporting
  verb at the opening, a cue later in the stub) are listed in the key and
  printed.

Whitespace inside a statement, location or stub is made single spaces; nothing
else in them is changed. A statement, location or stub that names an id of
either return (C01, F12 and the like) is listed as a warning. No outcome,
direction, core, stated_as, voice, unit, period, speaker, label, gloss, link,
pair, gap or note goes into the lists file, and nothing that says which return
came first or how either was made.

A claim's location is its pages, as the brief has it ("location | page"), and is
printed as the return gives it.

The key's pages: every page a location names after "p.", "pp.", "pg.", "page" or
"pages" (not inside a word, so "Supp. 3" names no page), with ranges expanded
("pp. 615–17" is 615 to 617) and further pages after a comma kept when they have
as many digits as the first; its first page, the lowest of them; its table: the
table a location names ("Table 1", "Tab. 2"), or none. Voice codes must be
`reported` or `author_insight`, one for every fragment, or the build stops.
Warnings: a location with no page read from it, a page outside the paper's
pages (606 to 643), a location that speaks of a table but names none, an id of
either return in a printed text, and the voice-cue rule's own. build stops
unless the first return's two files are those of 6 Oct (their sha256 open
7ce0e382 and 6ded1283), or --test=1 is given. Two builds from the same files
give the same bytes.
"""
import hashlib
import json
import os
import random
import re
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import build_cold_pack as bcp     # noqa: E402

LISTS = "TWO_LISTS_bechky.md"
KEY = "two_lists_key.json"
PAPER_PAGES = (606, 643)
PAGE_RE = re.compile(r"(?<![A-Za-z])(?:pp?\.|pg\.|pages?\b)\s*(\d+)((?:\s*[–—-]\s*\d+)?)"
                     r"((?:\s*,\s*\d+(?:\s*[–—-]\s*\d+)?)*)", re.I)
RANGE_RE = re.compile(r"(\d+)(?:\s*[–—-]\s*(\d+))?")
TABLE_RE = re.compile(r"\b(?:tables?\s+|tab\.\s*)([a-z]?[0-9]+[a-z]?\b|[ivxlc]+\b|[a-z]\b)", re.I)
TABLE_WORD = re.compile(r"\b(?:tables?|tab\.)", re.I)
ID_RE = re.compile(r"\b(?:C\d{2,3}|F\d{2,4})\b")
VOICE_CODES = ("reported", "author_insight")
FIRST_SHA256 = {"corpus": "7ce0e382bb5659552a63d65b889035674ed7ddbd112bdef37295a520b20f5acc",
                "voice": "6ded1283ccfbba25e6e6a3f1c4b145d0a8cce9fec5bffb8cbd1330e499e06d67"}


class Refused(Exception):
    pass


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def one_line(s):
    return " ".join(str(s or "").split())


def _span(a, b):
    a = int(a)
    if b is None:
        return [a]
    if len(b) < len(str(a)):
        b = str(a)[:len(str(a)) - len(b)] + b
    b = int(b)
    return list(range(a, b + 1)) if a <= b <= a + 60 else [a]


def pages_of(loc):
    """Every page a location names, sorted, without repeats."""
    out = set()
    for m in PAGE_RE.finditer(loc or ""):
        first = m.group(1)
        rest = re.sub(r"^\s*[–—-]\s*", "", m.group(2)) or None
        out.update(_span(first, rest))
        for r in RANGE_RE.finditer(m.group(3) or ""):
            if len(r.group(1)) == len(first):
                out.update(_span(r.group(1), r.group(2)))
    return sorted(out)


def table_of(loc):
    m = TABLE_RE.search(loc or "")
    if not m:
        return None
    t = m.group(1)
    return f"Table {int(t)}" if t.isdigit() else f"Table {t.upper()}"


def load_return(corpus_path, voice_path, which):
    c = json.load(open(corpus_path, encoding="utf-8"))
    v = json.load(open(voice_path, encoding="utf-8"))
    for k in ("claims", "fragments", "claim_links"):
        if not isinstance(c.get(k), list):
            raise Refused(f"{which}: the corpus has no list `{k}`")
    if not isinstance(v.get("voice"), list):
        raise Refused(f"{which}: the voice file has no list `voice`")
    voice = {}
    for e in v["voice"]:
        fid = e.get("fragment_id")
        if fid in voice:
            raise Refused(f"{which}: two voice codes for {fid}")
        voice[fid] = e.get("code")
    fids = [f.get("fragment_id") for f in c["fragments"]]
    cids = [x.get("claim_id") for x in c["claims"]]
    if len(set(fids)) != len(fids) or len(set(cids)) != len(cids):
        raise Refused(f"{which}: a fragment or claim id repeats")
    missing = [f for f in fids if not voice.get(f)]
    if missing:
        raise Refused(f"{which}: fragments with no voice code: {missing[:10]}")
    odd = sorted({str(v) for f, v in voice.items() if v not in VOICE_CODES})
    if odd:
        raise Refused(f"{which}: voice codes other than {VOICE_CODES}: {odd[:10]}")
    extra = sorted(set(voice) - set(fids))
    if extra:
        raise Refused(f"{which}: voice codes for fragments not in the corpus: {extra[:10]}")
    return c, voice


def claim_order(claims):
    def key(i):
        p = pages_of(claims[i].get("location"))
        return (0, p[0], i) if p else (1, 0, i)
    return sorted(range(len(claims)), key=key)


def passage_order(frags):
    """Fragment indices page by page: by the lowest page the location names; a tie
    keeps the return's order; a fragment with no page keeps the page of the one
    before it in the return, as the coders' packs do (build_cold_pack.page_order)."""
    pages, last = [], -1
    for f in frags:
        p = pages_of(f.get("location"))
        last = p[0] if p else last
        pages.append(last)
    return sorted(range(len(frags)), key=lambda i: (pages[i], i))


def describe(which, frag, overrides, warnings, removed_log, new_id):
    fid = frag["fragment_id"]
    ov = overrides.get(f"{which}:{fid}")
    try:
        s, removed, warn = bcp.v_description(frag.get("stub"), ov)
    except bcp.Refused as e:
        raise Refused(f"{which}:{fid}: {e}")
    if removed:
        removed_log[new_id] = removed
    if warn:
        warnings.append(f"{new_id} ({which}:{fid}): {warn}")
    return one_line(s)


def build(seed, first, new, out, overrides=None):
    """first and new: (corpus path, voice path). Returns the key."""
    overrides = overrides or {}
    for k, v in overrides.items():
        if not re.fullmatch(r"(first|new):\S+", k) or not str(v).strip():
            raise Refused(f"--descriptions: bad entry {k!r}")
    src = {"first": first, "new": new}
    data = {w: load_return(*src[w], w) for w in ("first", "new")}
    p_is = random.Random(seed).choice(["first", "new"])
    order = {"P": p_is, "Q": "new" if p_is == "first" else "first"}
    warnings, removed_log, used = [], {}, set()
    key = {"plan": "SECOND_EXTRACTION_PLAN.md", "seed": seed,
           "draw": f'random.Random({seed}).choice(["first", "new"])', "P": order["P"], "Q": order["Q"],
           "sources": {w: {"corpus": os.path.basename(src[w][0]), "corpus_sha256": sha(src[w][0]),
                           "voice": os.path.basename(src[w][1]), "voice_sha256": sha(src[w][1])}
                       for w in ("first", "new")},
           "claims": {}, "passages": {}, "links": {}, "removed": removed_log, "warnings": warnings}
    lines = ["# Two lists of one paper: P and Q", "",
             "Each list records the paper's claims, in the order of their first page, and the passages of the",
             "evidence it prints, page by page. The claims are PC01, PC02, ... in list P and QC01, QC02, ... in",
             "list Q; the passages PP001, PP002, ... and QP001, QP002, .... What to do with them is in",
             "`MATCH_TWO_LISTS.md`.", ""]
    counts = []
    body = []
    for L in ("P", "Q"):
        which = order[L]
        c, voice = data[which]
        claims, frags = c["claims"], c["fragments"]
        counts.append(f"List {L}: {len(claims)} claims, {len(frags)} passages.")
        body += [f"## List {L}", "", f"### The claims of list {L} ({len(claims)})", ""]
        for n, i in enumerate(claim_order(claims), 1):
            cl = claims[i]
            nid = f"{L}C{n:02d}"
            loc, st = one_line(cl.get("location")), one_line(cl.get("statement"))
            if not st:
                raise Refused(f"{which}:{cl.get('claim_id')}: no statement")
            for t in (loc, st):
                if ID_RE.search(t):
                    warnings.append(f"{nid} ({which}:{cl['claim_id']}): names an id: {ID_RE.search(t).group(0)}")
            if not pages_of(loc):
                warnings.append(f"{nid} ({which}:{cl['claim_id']}): no page read from its location {loc!r}")
            body += [f"**{nid}** ({loc or 'no page given'}). {st}", ""]
            key["claims"][nid] = {"return": which, "id": cl["claim_id"], "location": loc,
                                  "pages": pages_of(loc), "core": cl.get("core"),
                                  "stated_as": cl.get("stated_as")}
        body += [f"### The passages of list {L} ({len(frags)})", ""]
        for n, i in enumerate(passage_order(frags), 1):
            f = frags[i]
            nid = f"{L}P{n:03d}"
            loc = one_line(f.get("location"))
            if not loc:
                raise Refused(f"{which}:{f.get('fragment_id')}: no location")
            used.add(f"{which}:{f['fragment_id']}")
            d = describe(which, f, overrides, warnings, removed_log, nid)
            for t in (loc, d):
                if ID_RE.search(t):
                    warnings.append(f"{nid} ({which}:{f['fragment_id']}): names an id: {ID_RE.search(t).group(0)}")
            body += [f"**{nid}** · {loc}. {d}", ""]
            pg = pages_of(loc)
            tag = f"{nid} ({which}:{f['fragment_id']})"
            if not pg:
                warnings.append(f"{tag}: no page read from its location {loc!r}")
            if any(not PAPER_PAGES[0] <= p <= PAPER_PAGES[1] for p in pg):
                warnings.append(f"{tag}: a page outside {PAPER_PAGES}: {pg}")
            if TABLE_WORD.search(loc) and table_of(loc) is None:
                warnings.append(f"{tag}: its location speaks of a table but names none: {loc!r}")
            key["passages"][nid] = {"return": which, "id": f["fragment_id"], "location": loc, "pages": pg,
                                    "first_page": pg[0] if pg else None, "table": table_of(loc),
                                    "voice": voice[f["fragment_id"]]}
    unused = sorted(set(overrides) - used)
    if unused:
        raise Refused(f"--descriptions names fragments not in either return: {unused}")
    for w in ("first", "new"):
        key["links"][w] = [[x.get("claim_id"), x.get("fragment_id"), x.get("direction")]
                           for x in data[w][0]["claim_links"]]
    text = "\n".join(lines + counts + [""] + body).rstrip("\n") + "\n"
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, LISTS), "w", encoding="utf-8") as fh:
        fh.write(text)
    key["lists_sha256"] = hashlib.sha256(text.encode("utf-8")).hexdigest()
    key["descriptions_replaced"] = sorted(overrides)
    with open(os.path.join(out, KEY), "w", encoding="utf-8") as fh:
        json.dump(key, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    return key


# ---------------------------------------------------------------- self-test

SENTINELS = ["SENTINEL-OUTCOME", "SENTINEL-NOTE", "SENTINEL-UNIT", "SENTINEL-SPEAKER", "SENTINEL-PERIOD",
             "SENTINEL-GLOSS", "SENTINEL-REASON", "SENTINEL-TEXT", "SENTINEL-CONSTRUCT", "SENTINEL-META",
             "SENTINEL-LABEL", "SENTINEL-PAIR", "SENTINEL-GAP", "SENTINEL-ABSENCE"]


def made_up(which):
    """A made-up return about an invented paper, with a sentinel in every field
    that must not reach the lists file."""
    def frag(fid, loc, stub, unit="SENTINEL-UNIT"):
        return {"fragment_id": fid, "location": loc, "stub": stub, "text": "SENTINEL-TEXT",
                "unit": unit, "period": "SENTINEL-PERIOD", "speaker_name": "SENTINEL-SPEAKER",
                "author_gloss": "SENTINEL-GLOSS", "author_code": "SENTINEL-LABEL", "notes": "SENTINEL-NOTE",
                "data_type": "observation", "text_status": "paraphrase", "citing_claims": [],
                "extraction_confidence": "high", "paper_id": "x"}

    def claim(cid, loc, st, core, sa):
        return {"claim_id": cid, "location": loc, "statement": st, "outcome": "SENTINEL-OUTCOME",
                "asserted_direction": "increases", "constructs": ["SENTINEL-CONSTRUCT"], "core": core,
                "stated_as": sa, "notes": "SENTINEL-NOTE", "decomposed_into": [], "paper_id": "x",
                "extraction_confidence": "high"}
    if which == "first":
        claims = [claim("C01", "p. 610; pp. 612–613", "Ovens moved baking to the day.", True, "established"),
                  claim("C02", "p. 606", "Bakers judged ovens by the crust.", False, "ventured"),
                  claim("C03", "pp. 620–21", "Training kept ovens in use.", True, "established")]
        frags = [frag("F01", "p. 612", "The author's account is that the bakers trusted the crust."),
                 frag("F02", "p. 607", "A head baker recalls the last night shift."),
                 frag("F03", "Table 1, Loaves — before, p. 613", "The count before the ovens."),
                 frag("F04", "Table 1, Loaves — after, p. 613", "The count after the ovens."),
                 frag("F05", "pp. 615–16", "For the author, training mattered more than price."),
                 frag("F06", "p. 615", "*The paper explains that* owners paid for courses.")]
        links = [{"claim_id": "C01", "fragment_id": "F02", "direction": "with", "basis": "x", "confidence": "high"},
                 {"claim_id": "C03", "fragment_id": "F05", "direction": "illustrates", "basis": "x",
                  "confidence": "high"}]
        voice = [("F01", "author_insight"), ("F02", "reported"), ("F03", "reported"), ("F04", "reported"),
                 ("F05", "author_insight"), ("F06", "author_insight")]
    else:
        claims = [claim("C01", "p. 606", "Crust was the bakers' test of an oven.", False, "established"),
                  claim("C02", "pp. 610–613", "The ovens shifted work from night to day.", True, "established")]
        frags = [frag("F01", "pp. 607–608", "The head baker on the last night shift and the first morning."),
                 frag("F02", "Table 1, p. 613", "Loaves by day, before and after."),
                 frag("F03", "p. 615", "Owners paid for training courses."),
                 frag("F04", "p. 630", "According to the author, small bakeries waited.")]
        links = [{"claim_id": "C02", "fragment_id": "F01", "direction": "with", "basis": "x", "confidence": "high"}]
        voice = [("F01", "reported"), ("F02", "reported"), ("F03", "reported"), ("F04", "author_insight")]
    corpus = {"meta": {"note": "SENTINEL-META"}, "claims": claims, "fragments": frags, "claim_links": links,
              "contrast_pairs": [{"pair_id": "CP01", "note": "SENTINEL-PAIR"}],
              "declared_gaps": [{"gap_id": "G01", "statement": "SENTINEL-GAP"}],
              "absences": [{"absence_id": "A01", "statement": "SENTINEL-ABSENCE"}]}
    vfile = {"paper_id": "x", "voice": [{"fragment_id": f, "code": c, "reason": "SENTINEL-REASON"}
                                        for f, c in voice],
             "gloss_relation": [{"fragment_id": "F01", "relation": "SENTINEL-GLOSS"}]}
    return corpus, vfile


def selftest():
    fails = []

    def check(cond, msg):
        if not cond:
            fails.append(msg)

    # pages and tables
    check(pages_of("p. 612") == [612], "pages: p. 612")
    check(pages_of("pp. 615–17") == [615, 616, 617], "pages: abbreviated range")
    check(pages_of("pp. 607-608; p. 634") == [607, 608, 634], "pages: hyphen and a list")
    check(pages_of("Table 1, Gender — firearms, p. 613") == [613], "pages: a table cell")
    check(pages_of("pp. 607, 610–611") == [607, 610, 611], "pages: a comma list")
    check(pages_of("p. 612, 2nd paragraph") == [612], "pages: a paragraph number is no page")
    check(pages_of("pages 620 and 622") == [620], "pages: 'and' is not followed")
    check(pages_of("abstract") == [], "pages: none")
    check(table_of("Table 1, Gender — firearms, p. 613") == "Table 1", "table: Table 1")
    check(table_of("table II, row 3") == "Table II", "table: roman")
    check(table_of("p. 613, the timetable") is None, "table: a word ending in table is no table")
    check(table_of("p. 613") is None, "table: none")
    check(table_of("Table A1, p. 640") == "Table A1", "table: A1")
    check(table_of("Tables 1 and 2, p. 613") == "Table 1", "table: the first of two")
    check(table_of("Tab. 2, p. 619") == "Table 2" and pages_of("Tab. 2, p. 619") == [619], "table: Tab. 2")
    check(pages_of("Supp. 3, p. 640") == [640] and pages_of("App. 2") == [], "pages: not inside a word")
    check(pages_of("page 612") == [612] and pages_of("p.612") == [612] and pages_of("pg. 612") == [612],
          "pages: page, p. without a space, pg.")
    order = passage_order([{"location": "p. 640"}, {"location": "page 612"}, {"location": "p. 612"},
                           {"location": "Abstract"}, {"location": "Supp. 3, p. 641"}])
    check(order == [1, 2, 3, 0, 4], f"passage order: {order}")   # "Abstract" keeps p. 612, before it
    with tempfile.TemporaryDirectory() as d:
        paths = {}
        for w in ("first", "new"):
            corpus, vfile = made_up(w)
            cp, vp = os.path.join(d, f"{w}_corpus.json"), os.path.join(d, f"{w}_voice.json")
            json.dump(corpus, open(cp, "w", encoding="utf-8"))
            json.dump(vfile, open(vp, "w", encoding="utf-8"))
            paths[w] = (cp, vp)
        out1, out2 = os.path.join(d, "o1"), os.path.join(d, "o2")
        k1 = build(20261018, paths["first"], paths["new"], out1)
        build(20261018, paths["first"], paths["new"], out2)
        for name in (LISTS, KEY):
            check(open(os.path.join(out1, name), "rb").read() == open(os.path.join(out2, name), "rb").read(),
                  f"two builds differ: {name}")
        text = open(os.path.join(out1, LISTS), encoding="utf-8").read()
        check(k1["P"] == random.Random(20261018).choice(["first", "new"]), "P is not the seed's draw")
        for s in SENTINELS:
            check(s not in text, f"the lists file holds {s}")
        frame = "\n".join(l for l in text.split("\n") if not re.match(r"\*\*[PQ][CP]\d+\*\*", l))
        frame = frame.replace("their first page", "")
        for word in ("first", "second", "earlier", "later", "new", "extraction", "extractor", "ChatGPT",
                     "GPT", "Claude", "model", "run", "reported", "author_insight", "core", "established",
                     "ventured", "voice", "direction", "outcome"):
            check(not re.search(r"\b" + re.escape(word) + r"\b", frame, re.I),
                  f"the lists file's own text names {word!r}")
        check(len(text.split("\n")) - len(frame.split("\n")) == 15, "every claim and passage on one line")
        for marker in ("author's account", "the paper explains", "for the author", "according to the author"):
            check(marker not in text.lower(), f"a voice cue is left: {marker}")
        P, Q = k1["P"], k1["Q"]
        nP = {"first": 3, "new": 2}
        check(sorted(i for i in k1["claims"] if i.startswith("PC")) == [f"PC{n:02d}" for n in range(1, nP[P] + 1)],
              "claim ids of P")
        check(sorted(i for i in k1["claims"] if i.startswith("QC")) == [f"QC{n:02d}" for n in range(1, nP[Q] + 1)],
              "claim ids of Q")
        fk = {v["id"]: k for k, v in k1["passages"].items() if v["return"] == "first"}
        ck = {v["id"]: k for k, v in k1["claims"].items() if v["return"] == "first"}
        pre = "P" if P == "first" else "Q"
        # claims by lowest page: C02 (606), C01 (610), C03 (620)
        check([ck["C02"], ck["C01"], ck["C03"]] == [f"{pre}C01", f"{pre}C02", f"{pre}C03"], "claim order")
        # passages by first page: F02 (607), F01 (612), F03, F04 (613), F05 (615), F06 (615)
        check([fk[x] for x in ("F02", "F01", "F03", "F04", "F05", "F06")] ==
              [f"{pre}P{n:03d}" for n in range(1, 7)], "passage order")
        check(k1["passages"][fk["F03"]]["table"] == "Table 1" and k1["passages"][fk["F02"]]["table"] is None,
              "tables in the key")
        check(k1["passages"][fk["F05"]]["pages"] == [615, 616], "pages in the key")
        check(k1["passages"][fk["F01"]]["voice"] == "author_insight", "voice in the key")
        check(k1["claims"][ck["C01"]]["core"] is True and k1["claims"][ck["C02"]]["stated_as"] == "ventured",
              "core and stated_as in the key")
        check(set(k1["removed"]) == {fk["F01"], fk["F05"], fk["F06"]} | (
              {next(k for k, v in k1["passages"].items() if v["return"] == "new" and v["id"] == "F04")}),
              f"removed: {k1['removed']}")
        check(f"**{fk['F01']}** · p. 612. The bakers trusted the crust." in text, "a stub after its cue is cut")
        check(f"**{fk['F06']}** · p. 615. Owners paid for courses." in text, "a cue in markdown is cut")
        check(f"**{fk['F02']}** · p. 607. A head baker recalls the last night shift." in text,
              "a stub without a cue is printed as written")
        check(k1["links"]["first"] == [["C01", "F02", "with"], ["C03", "F05", "illustrates"]], "links in the key")
        check(k1["lists_sha256"] == sha(os.path.join(out1, LISTS)), "the lists file's hash in the key")
        # a stub that is only a cue is refused, and a replacement passes
        corpus, vfile = made_up("new")
        corpus["fragments"][2]["stub"] = "The author's account is that"
        bp = os.path.join(d, "bad_corpus.json")
        json.dump(corpus, open(bp, "w", encoding="utf-8"))
        try:
            build(20261018, paths["first"], (bp, paths["new"][1]), os.path.join(d, "o3"))
            check(False, "a stub that is only a cue was not refused")
        except Refused as e:
            check("new:F03" in str(e), f"the refusal names the fragment: {e}")
        k3 = build(20261018, paths["first"], (bp, paths["new"][1]), os.path.join(d, "o4"),
                   {"new:F03": "Owners paid for training courses."})
        check(k3["descriptions_replaced"] == ["new:F03"], "the replacement is recorded")
        for bad in ({"new:F03": "The paper explains that owners paid."}, {"new:F99": "x"}):
            try:
                build(20261018, paths["first"], (bp, paths["new"][1]), os.path.join(d, "o5"), bad)
                check(False, f"a bad replacement passed: {bad}")
            except Refused:
                pass
        # a fragment without a voice code, or with a code outside the two, is refused
        for k, change in enumerate((lambda v: v[:-1], lambda v: v[:-1] + [{**v[-1], "code": "Reported"}])):
            vfile2 = json.load(open(paths["new"][1], encoding="utf-8"))
            vfile2["voice"] = change(vfile2["voice"])
            vp2 = os.path.join(d, f"bad_voice{k}.json")
            json.dump(vfile2, open(vp2, "w", encoding="utf-8"))
            try:
                build(20261018, paths["first"], (paths["new"][0], vp2), os.path.join(d, f"o6{k}"))
                check(False, f"a bad voice file was not refused ({k})")
            except Refused:
                pass
        # a passage with no page, and a location that speaks of a table but names none, are warned of
        corpus, vfile = made_up("new")
        corpus["fragments"][3]["location"] = "Abstract"
        corpus["fragments"][2]["location"] = "the table on p. 615"
        wp = os.path.join(d, "warn_corpus.json")
        json.dump(corpus, open(wp, "w", encoding="utf-8"))
        k7 = build(20261018, paths["first"], (wp, paths["new"][1]), os.path.join(d, "o7"))
        check(any("new:F04): no page read" in x for x in k7["warnings"]), "no warning for a passage with no page")
        check(any("new:F03): its location speaks of a table" in x for x in k7["warnings"]),
              "no warning for a table not named")
    if fails:
        print("SELF-TEST FAILED:")
        for f in fails:
            print("  ", f)
        return 1
    print("self-test passed: pages and tables, two builds alike, the seed's draw, no field but the four, "
          "voice cues cut, ids and order, the key, refusals and replacements")
    return 0


def main(argv):
    if not argv or argv[0] not in ("selftest", "build"):
        print(__doc__)
        return 2
    if argv[0] == "selftest":
        return selftest()
    opts = dict(a[2:].split("=", 1) for a in argv[1:] if a.startswith("--") and "=" in a)
    for need in ("seed", "first", "new", "out"):
        if need not in opts:
            print(f"--{need}= is needed")
            return 2
    first, new = opts["first"].split(","), opts["new"].split(",")
    if len(first) != 2 or len(new) != 2:
        print("--first and --new each take CORPUS,VOICE")
        return 2
    got = {"corpus": sha(first[0]), "voice": sha(first[1])}
    if got != FIRST_SHA256 and opts.get("test") != "1":
        print(f"REFUSED: --first is not the first return of 6 Oct: {got}")
        return 1
    overrides = json.load(open(opts["descriptions"], encoding="utf-8")) if "descriptions" in opts else {}
    try:
        key = build(int(opts["seed"]), first, new, opts["out"], overrides)
    except Refused as e:
        print(f"REFUSED: {e}")
        return 1
    print(f"P is the {key['P']} return, Q the {key['Q']}")
    for L in ("P", "Q"):
        cs = [v for k, v in key["claims"].items() if k.startswith(L)]
        ps = [v for k, v in key["passages"].items() if k.startswith(L)]
        print(f"list {L} ({key[L]} return): {len(cs)} claims, {sum(1 for v in cs if v['core'] is True)} core; "
              f"{len(ps)} passages, {sum(1 for v in ps if v['table'])} table cells, "
              f"{sum(1 for v in ps if not v['pages'])} with no page; voice "
              f"{dict(sorted((c, sum(1 for v in ps if v['voice'] == c)) for c in VOICE_CODES))}")
    print(f"voice cues removed: {len(key['removed'])}; replaced by --descriptions: "
          f"{len(key['descriptions_replaced'])}")
    for w in key["warnings"]:
        print("warning:", w)
    print(f"{LISTS}: sha256 {key['lists_sha256']}")
    print(f"{KEY}: sha256 {sha(os.path.join(opts['out'], KEY))}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
