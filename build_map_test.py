#!/usr/bin/env python3
"""
The map test (T39): round 1's sheets and key, and the check of the map coders' replies.

WHY
---
`MAP_TEST_PLAN.md` asks, among other things, whether two models from different vendors, blind to the alternative
readings, build the same argument map of a paper from its frozen index (chats 73 to 76, round 1). This script makes
what those chats get besides the task and the paper (a map sheet per paper, with the numbered pairs of claims to
code), makes the key, and checks every reply. It judges nothing.

USAGE
-----
    python3 -B build_map_test.py pairs --seed=20261025 <out dir>
        writes MAP_SHEET_bechky.md, MAP_SHEET_pratt.md and map_key.json into <out dir>
    python3 -B build_map_test.py check-map <bechky|pratt> <map_key.json> <reply>
        exit 0: the reply counts; 1: it does not; 2: it counts, with a quoted span to show the PI first
    python3 -B build_map_test.py --selftest

It refuses to write over a file. The same sources always give the same bytes: no date and no clock go in.

THE SOURCES, each checked against its sha256 before use
-------------------------------------------------------
The frozen indexes, `bechky_2020_v1.json` and `pratt_2000_v1.json`, beside this script. No chat gets them: the
coders get the sheets. The check of quoted spans is `build_citation_sheet.py`'s, as in T37 and T38.

THE PAIRS (the plan's part A)
-----------------------------
A pair is ordered: a base Ci and a claim Cj, two different claims of the paper, Cj core (`core` true); the question
is whether Cj rests on Ci. Pairs are sorted by the number in the base's id, then in the claim's. Candidates, by four
rules on the index:
1. level: the base is a unit claim (at least 5 linked passages, at least 80% of them from one unit), the claim is not,
   and the two share a construct, string for string;
2. shared passages: at least 3 passages linked to both, counting only passages linked to at most 6 claims;
3. chaining: the base has an outcome (not empty, not "none") and its content words and those of the claim's
   constructs (joined by spaces) share at least 2; content words are the runs of a to z in the lower-cased text,
   3 letters or more, not in STOP;
4. stated tie: a passage linked to both whose stub and gloss (joined by a space, lower-cased) hold one of PHRASES.
The others are the pairs that are not candidates. One random.Random(seed): for Bechky and then Pratt,
`rng.sample(others, SAMPLE[paper])`; then, for Bechky and then Pratt, `rng.shuffle` of the paper's candidates and
sample together, sorted as above; the pairs are numbered P001 onward in the shuffled order.
What applies: the comparative table (the task's part 5) when the unit claims with an outcome come from at least two
units, and its rows are those units, in the order of their claims; the contrast controls (part 6) when the index
has contrast pairs; the factors (part 4) when either applies.

THE SHEET
---------
The paper's citation; what applies; the claims in full (id, pages, core or not, stated as, statement, outcome,
constructs, and the passages linked to the claim, by direction); every construct name, with the claims that use it;
the passages (id, pages, unit, data type, speaker where named, stub, gloss where kept); the contrast pairs, declared
gaps and absences; and the numbered pairs. It gives no voice code, no basis of a link, no confidence and no note of
the extraction, and does not say which pairs are candidates: the key does.

THE CHECK OF A REPLY
--------------------
A reply is read as the text from its first "{" to its last "}". Faults make it not count; remarks are reported.
Some forms are read leniently first, each reading a remark: a type, strength or control in other case or with other
spacing or between back-quotes; the control "varied" or "vary" for "varies"; a page given as a whole number; a
factor's claim given as a list (its first, if it is the paper's); a unit or contrast pair named in other case or
spacing or between back-quotes, or a unit named without its words in brackets or with other ones, where that names one
unit of the sheet alone. A minus may be a hyphen, an en dash or a minus sign.
Faults: not one JSON object; a key given twice in one object; a missing key among paper, pairs, further_edges,
registry, factors, units, contrasts; `pairs` not a list of objects; a pair not in the key, or answered twice, or a
pair of the key not answered; a pair whose claim and base are not the key's; `rests_on` not true or false; no
reason; for an edge (rests_on true), a type not in TYPES, a strength not in STRENGTHS, no basis, or a page with no
page number; more than 10 further edges, or one whose ids are not two of the paper's claims, whose claim is not core,
or that lacks a type, strength, basis, page or reason; a registry group without a canonical name or with fewer than
two names; a factor without an id, a name, or a claim of the paper; two factors with one id; where part 5 applies, the units not exactly the sheet's, each once, or a unit without an outcome of
+ - ?, a value of + - ? for every factor, or a list of ids; where part 6 applies, a contrast pair of the index without
exactly one entry, an entry for anything else, or an entry without held, varies or unclear for every factor, or
without a list of ids. Remarks: `paper` not naming the author; no factor where part 5 or 6 applies (the paper may
use none); a further edge that is a listed pair; a registry name
not among the sheet's construct names, or in two groups, or a canonical name not among its group's names; units or
contrasts given where they do not apply; an empty list of ids; an id not the paper's. Every quoted span of more than
eight words in any string is named (where, how many words), never printed: the plan shows such a span to the PI
before the reply is filed, and the span is not filed.
"""
import collections
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
INDEX = {"bechky": "bechky_2020_v1.json", "pratt": "pratt_2000_v1.json"}
AUTHOR = {"bechky": "bechky", "pratt": "pratt"}
SHA = {
    "bechky_2020_v1.json": "6f83d744cd1dd68326cce29568a4aff461580d852d1222c4f1d096cb6922ced0",
    "pratt_2000_v1.json": "a4810cc03d9a439220b2c8781acf494c62d5ac63f7f53f359157238739147c99",
}
SEED = 20261025
SAMPLE = {"bechky": 25, "pratt": 30}
UNIT_MIN_LINKS = 5
UNIT_SHARE = 0.8
SHARED_MIN = 3
SHARED_CAP = 6
CHAIN_MIN = 2
PHRASES = ("combined with", "led to", "leads to", "builds on", "rests on", "depends on", "drawing on")
STOP = tuple(sorted(set("""a an the of and or in on to for by with from at as is are be been its their this that
these those which who whom what how than more less into over under between within across about against among through
after before during not no nor but also such other same each both all any some own very can may might would should
could will shall has have had was were being do does did""".split())))
DIRECTIONS = ("with", "illustrates", "qualifies", "against")
TYPES = ("evidential", "mechanistic", "comparative", "significance")
STRENGTHS = ("necessary", "contributing")
SIGNS = {"+": "+", "-": "-", "\u2212": "-", "\u2013": "-", "?": "?"}
CONTROLS = ("held", "varies", "unclear")
KEYS = ("paper", "pairs", "further_edges", "registry", "factors", "units", "contrasts")
MAX_FURTHER = 10
PAGE_NO = re.compile(r"\d")


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha(path):
    return sha_bytes(open(path, "rb").read())


def load_index(paper, folder=None):
    """The paper's frozen index, checked against its sha256 (a made-up index in another folder: the self-test)."""
    name = INDEX[paper]
    path = os.path.join(folder or HERE, name)
    got = sha(path)
    if folder is None and got != SHA[name]:
        raise SystemExit(f"{name}: sha256 {got}, not {SHA[name]}")
    return json.load(open(path, encoding="utf-8")), got


def write_new(path, data):
    if os.path.exists(path):
        raise SystemExit(f"refusing to write over {path}")
    with open(path, "wb") as f:
        f.write(data)
    print(f"written: {path} ({len(data)} bytes, sha256 {sha_bytes(data)})")


def num(cid):
    return int(re.sub(r"\D", "", cid) or 0)


def content_words(s):
    return {w for w in re.findall(r"[a-z]+", (s or "").lower()) if len(w) >= 3 and w not in STOP}


def has_outcome(c):
    o = (c.get("outcome") or "").strip()
    return bool(o) and o.lower() != "none"


# ---------------------------------------------------------------- the pairs

def structure(d):
    claims = {c["claim_id"]: c for c in d["claims"]}
    frags = {f["fragment_id"]: f for f in d["fragments"]}
    links = collections.defaultdict(set)
    nclaims = collections.defaultdict(set)
    for l in d["claim_links"]:
        links[l["claim_id"]].add(l["fragment_id"])
        nclaims[l["fragment_id"]].add(l["claim_id"])
    core = sorted((c for c in claims if claims[c].get("core") is True), key=num)
    return claims, frags, links, nclaims, core


def unit_claims(d):
    """{claim: its unit} for every unit claim, in the order of the claims."""
    claims, frags, links, _, _ = structure(d)
    out = {}
    for c in sorted(claims, key=num):
        fs = links[c]
        if len(fs) < UNIT_MIN_LINKS:
            continue
        counts = collections.Counter(frags[f]["unit"] for f in fs)
        top = max(counts.values())
        if top / len(fs) >= UNIT_SHARE:
            out[c] = [u for u, n in counts.items() if n == top][0]
    return out


def applies(d):
    claims = {c["claim_id"]: c for c in d["claims"]}
    units = []
    for c, u in unit_claims(d).items():
        if has_outcome(claims[c]) and u not in [x for x, _ in units]:
            units.append((u, c))
    table = len(units) >= 2
    contrasts = [p["pair_id"] for p in d.get("contrast_pairs", [])]
    return {"table": table, "units": [{"unit": u, "claim": c} for u, c in units] if table else [],
            "contrasts": contrasts, "factors": table or bool(contrasts)}


def all_pairs(d):
    claims, _, _, _, core = structure(d)
    return sorted(((b, c) for c in core for b in claims if b != c), key=lambda p: (num(p[0]), num(p[1])))


def candidates(d):
    """{(base, claim): [rules]} for every candidate pair."""
    claims, frags, links, nclaims, core = structure(d)
    uc = unit_claims(d)
    cons = {c: set(claims[c].get("constructs") or []) for c in claims}
    out = collections.defaultdict(set)
    for b, c in all_pairs(d):
        if b in uc and c not in uc and cons[b] & cons[c]:
            out[(b, c)].add("level")
        if len([f for f in links[b] & links[c] if len(nclaims[f]) <= SHARED_CAP]) >= SHARED_MIN:
            out[(b, c)].add("shared passages")
        if has_outcome(claims[b]) and \
                len(content_words(claims[b]["outcome"]) & content_words(" ".join(claims[c].get("constructs") or []))) \
                >= CHAIN_MIN:
            out[(b, c)].add("chaining")
    for f in sorted(frags, key=num):
        text = ((frags[f].get("stub") or "") + " " + (frags[f].get("author_gloss") or "")).lower()
        if any(p in text for p in PHRASES):
            for b in nclaims[f]:
                for c in nclaims[f]:
                    if b != c and c in core:
                        out[(b, c)].add("stated tie")
    return {k: sorted(v) for k, v in out.items()}


def draw(indexes, seed, sample=None):
    """For each paper: its candidates, its sample and the numbered order, all from one generator."""
    sample = sample or SAMPLE
    rng = random.Random(seed)
    cand, others, picked = {}, {}, {}
    for paper in PAPERS:
        cand[paper] = candidates(indexes[paper])
        others[paper] = [p for p in all_pairs(indexes[paper]) if p not in cand[paper]]
        picked[paper] = rng.sample(others[paper], sample[paper])
    out = {}
    for paper in PAPERS:
        chosen = sorted(list(cand[paper]) + picked[paper], key=lambda p: (num(p[0]), num(p[1])))
        rng.shuffle(chosen)
        order = [{"id": "P%03d" % i, "base": b, "claim": c,
                  "source": "candidate" if (b, c) in cand[paper] else "sample",
                  "rules": cand[paper].get((b, c), [])} for i, (b, c) in enumerate(chosen, 1)]
        out[paper] = {"candidates": len(cand[paper]), "sample": len(picked[paper]), "others": len(others[paper]),
                      "order": order}
    return out


# ---------------------------------------------------------------- the sheet

def construct_names(d):
    """{name: [claims]} for every construct name, as written."""
    out = collections.defaultdict(list)
    for c in sorted(d["claims"], key=lambda c: num(c["claim_id"])):
        for n in c.get("constructs") or []:
            if c["claim_id"] not in out[n]:
                out[n].append(c["claim_id"])
    return dict(out)


def sheet(d, order):
    claims, frags, _, _, core = structure(d)
    ap = applies(d)
    L = [f"# {d['meta']['citation']}", "",
         "The map sheet: the paper's claims, passages, contrast pairs, declared gaps and absences as its index "
         "records them, and the pairs of claims to code. Every record is a summary, not the paper's words: check the "
         "page.", "", "## What applies", "",
         "- **Parts 1 to 3:** always."]
    if ap["factors"]:
        L.append("- **Part 4, the paper's explanatory factors:** applies.")
    else:
        L.append("- **Part 4, the paper's explanatory factors:** does not apply; give `factors` as an empty list.")
    if ap["table"]:
        rows = "; ".join(f"`{x['unit']}` ({x['claim']})" for x in ap["units"])
        L.append(f"- **Part 5, the comparative table:** applies, to these {len(ap['units'])} units, each named as "
                 f"between the back-quotes here, with the claim that names it: {rows}.")
    else:
        L.append("- **Part 5, the comparative table:** does not apply; give `units` as an empty list.")
    if ap["contrasts"]:
        L.append(f"- **Part 6, the contrast controls:** applies, to the contrast pairs {', '.join(ap['contrasts'])}.")
    else:
        L.append("- **Part 6, the contrast controls:** does not apply; give `contrasts` as an empty list.")
    L.append(f"- **The core claims,** one of which is the claim of every pair: {', '.join(core)}.")
    L += ["", f"## The claims ({len(claims)})", ""]
    links = collections.defaultdict(lambda: collections.defaultdict(list))
    for l in d["claim_links"]:
        links[l["claim_id"]][l["direction"]].append(l["fragment_id"])
    for c in sorted(claims, key=num):
        cl = claims[c]
        tags = (["core"] if cl.get("core") is True else []) + ([cl["stated_as"]] if cl.get("stated_as") else [])
        L.append(f"- **{c}** · {cl.get('location') or 'no page'} · {', '.join(tags)}")
        L.append(f"  {cl['statement']}")
        L.append(f"  *outcome:* {cl.get('outcome') or 'none'}")
        L.append(f"  *constructs:* {'; '.join(cl.get('constructs') or []) or 'none'}")
        by = links[c]
        parts = [f"{k}: {', '.join(sorted(set(by[k]), key=num))}" for k in DIRECTIONS if by.get(k)]
        parts += [f"{k}: {', '.join(sorted(set(by[k]), key=num))}" for k in sorted(by) if k not in DIRECTIONS]
        L.append(f"  *passages:* {' · '.join(parts) if parts else 'none'}")
    names = construct_names(d)
    L += ["", f"## The construct names ({len(names)})", "",
          "Every construct name in the claims, as written, with the claims that use it.", ""]
    for n in sorted(names, key=lambda s: (s.casefold(), s)):
        L.append(f"- {n}: {', '.join(names[n])}")
    L += ["", f"## The passages ({len(frags)})", ""]
    for f in sorted(frags, key=num):
        fr = frags[f]
        head = f"- **{f}** · {fr.get('location') or 'no page'} · {fr.get('unit') or 'no unit'} · " \
               f"{fr.get('data_type') or 'no data type'}"
        if fr.get("speaker_name"):
            head += f" · speaker: {fr['speaker_name']}"
        L.append(head)
        L.append(f"  {fr.get('stub') or ''}")
        if fr.get("author_gloss"):
            L.append(f"  *gloss:* {fr['author_gloss']}")
    L += ["", "## The contrast pairs", ""]
    for p in d.get("contrast_pairs", []):
        L.append(f"- **{p['pair_id']}** · drawn by the paper: {'yes' if p.get('drawn_by_authors') else 'no'}")
        L.append(f"  *a:* {p['episode_a']} ({', '.join(p.get('fragments_a') or []) or 'no passage'})")
        L.append(f"  *b:* {p['episode_b']} ({', '.join(p.get('fragments_b') or []) or 'no passage'})")
        L.append(f"  *held comparable:* {p['held_comparable']}")
        L.append(f"  *differs in:* {p['differs_in']}")
    if not d.get("contrast_pairs"):
        L.append("None.")
    L += ["", "## The declared gaps", ""]
    for g in d.get("declared_gaps", []):
        L.append(f"- **{g['gap_id']}** · {g.get('location') or 'no page'} · {g.get('kind') or ''} · bears on "
                 f"{', '.join(g.get('bears_on') or []) or 'no claim'}")
        L.append(f"  {g['statement']}")
    if not d.get("declared_gaps"):
        L.append("None.")
    L += ["", "## The absences", ""]
    for a in d.get("absences", []):
        L.append(f"- **{a['absence_id']}** · {a.get('kind') or ''} · {a.get('evidence_class') or ''} · bears on "
                 f"{', '.join(a.get('bears_on') or []) or 'no claim'}")
        L.append(f"  {a['basis']}")
    if not d.get("absences"):
        L.append("None.")
    L += ["", f"## The pairs to code ({len(order)})", "",
          "Each asks whether a core claim rests on another claim (part 1).", ""]
    for o in order:
        L.append(f"- **{o['id']}**: does {o['claim']} rest on {o['base']}?")
    L.append("")
    return "\n".join(L).encode("utf-8")


PROCEDURE = [
    "pairs: every ordered pair (base, claim) of two different claims with the claim core (core is true); sorted by "
    "the number in the base's id, then in the claim's",
    "unit claim: at least unit_min_links linked passages, and at least unit_share of them from one unit",
    "level: the base is a unit claim, the claim is not, and their constructs share a string",
    "shared passages: at least shared_min passages linked to both, counting only passages linked to at most "
    "shared_cap claims",
    "chaining: the base's outcome is not empty and not 'none', and its content words and the content words of the "
    "claim's constructs joined by spaces share at least chain_min; content words: the runs of a-z in the lower-cased "
    "text, 3 letters or more, not in stop",
    "stated tie: a passage linked to both whose stub, a space and its gloss (if any), lower-cased, contain a phrase",
    "draw: one random.Random(seed); for bechky then pratt, rng.sample(others, sample[paper]), others being the "
    "sorted pairs that are not candidates; then, for bechky then pratt, rng.shuffle of the paper's candidates and "
    "sample together, sorted as the pairs are; numbered P001 onward in the shuffled order",
    "table applies when the unit claims with an outcome come from at least two units; its units are those units, in "
    "the order of their claims, each with its first such claim; contrasts apply when the index has contrast pairs; "
    "factors when either applies",
]


def build(outdir, seed, folder=None, sample=None):
    indexes, shas = {}, {}
    for paper in PAPERS:
        indexes[paper], shas[paper] = load_index(paper, folder)
    drawn = draw(indexes, seed, sample)
    files = {}
    key = {"what": "The key of the map test's round 1 (T39, MAP_TEST_PLAN.md, part A): every pair with its source and "
                   "rules, the order, and what applies. Not for any chat.",
           "seed": seed, "sample": sample or SAMPLE,
           "rules": {"unit_min_links": UNIT_MIN_LINKS, "unit_share": UNIT_SHARE, "shared_min": SHARED_MIN,
                     "shared_cap": SHARED_CAP, "chain_min": CHAIN_MIN, "phrases": list(PHRASES), "stop": list(STOP)},
           "procedure": PROCEDURE,
           "builder": os.path.basename(os.path.abspath(__file__)),
           "builder_sha256": sha(os.path.abspath(__file__)), "inputs": {}, "papers": {}}
    for paper in PAPERS:
        d = indexes[paper]
        data = sheet(d, drawn[paper]["order"])
        name = f"MAP_SHEET_{paper}.md"
        files[name] = data
        key["inputs"][INDEX[paper]] = shas[paper]
        key["papers"][paper] = {"index": INDEX[paper], "core": structure(d)[4], "unit_claims": unit_claims(d),
                                "applies": applies(d), "pairs_with_core_claim": len(all_pairs(d)),
                                "candidates": drawn[paper]["candidates"], "sample": drawn[paper]["sample"],
                                "others": drawn[paper]["others"], "order": drawn[paper]["order"],
                                "sheet": name, "sheet_sha256": sha_bytes(data)}
    files["map_key.json"] = (json.dumps(key, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    os.makedirs(outdir, exist_ok=True)
    for name in sorted(files):
        if os.path.exists(os.path.join(outdir, name)):
            raise SystemExit(f"refusing to write over {os.path.join(outdir, name)}")
    for name in sorted(files):
        write_new(os.path.join(outdir, name), files[name])
    return files


# ---------------------------------------------------------------- the check of a reply

def twice(path):
    """Keys given twice in one object anywhere in the reply's JSON object."""
    text = open(path, encoding="utf-8").read()
    a, b = text.find("{"), text.rfind("}")
    found = []

    def hook(pairs):
        seen = collections.Counter(k for k, _ in pairs)
        found.extend(sorted(k for k, n in seen.items() if n > 1))
        return dict(pairs)
    try:
        json.loads(text[a:b + 1], object_pairs_hook=hook)
    except json.JSONDecodeError:
        return []
    return found


def page_ok(s):
    return isinstance(s, str) and bool(PAGE_NO.search(s))


def nonempty(s):
    return isinstance(s, str) and bool(s.strip())


def st(x):
    """x if it is a string, else its repr: a value the reply got wrong never stops the check."""
    return x if isinstance(x, str) else repr(x)


def plain(s):
    return " ".join(s.replace("`", " ").split()).casefold() if isinstance(s, str) else None


def unbracketed(s):
    return plain(re.sub(r"\([^)]*\)", " ", s)) if isinstance(s, str) else None


def normalized(rep, paper, key, index):
    """(a copy of the reply with forms read leniently, remarks), by the docstring's rules; every reading is a remark."""
    import copy
    if not isinstance(rep, dict):
        return rep, []
    r = copy.deepcopy(rep)
    remarks = []
    kp = key["papers"][paper]
    claims = structure(index)[0]

    def lists(k):
        v = r.get(k)
        return v if isinstance(v, list) else []

    def word(obj, field, allowed, where, alias=None):
        v = obj.get(field)
        if isinstance(v, str) and v not in allowed:
            w = (alias or {}).get(plain(v), plain(v))
            if w in allowed:
                obj[field] = w
                remarks.append(f"{where}: {field} {v!r} read as {w!r}")

    def page(obj, where):
        v = obj.get("page")
        if isinstance(v, float) and v.is_integer():
            v = int(v)
        if isinstance(v, int) and not isinstance(v, bool):
            obj["page"] = f"p. {v}"
            remarks.append(f"{where}: a page given as a number, read as 'p. {v}'")

    for p in lists("pairs"):
        if isinstance(p, dict):
            where = st(p.get("pair"))
            word(p, "type", TYPES, where)
            word(p, "strength", STRENGTHS, where)
            page(p, where)
    for i, e in enumerate(lists("further_edges"), 1):
        if isinstance(e, dict):
            word(e, "type", TYPES, f"further edge {i}")
            word(e, "strength", STRENGTHS, f"further edge {i}")
            page(e, f"further edge {i}")
    for i, x in enumerate(lists("factors"), 1):
        c = x.get("claim") if isinstance(x, dict) else None
        if isinstance(c, list) and c and all(isinstance(y, str) for y in c) and c[0] in claims:
            remarks.append(f"factor {i}: the claims {c!r} read as {c[0]!r}")
            x["claim"] = c[0]
    want = [u["unit"] for u in kp["applies"]["units"]]
    for i, u in enumerate(lists("units"), 1):
        if isinstance(u, dict) and isinstance(u.get("unit"), str) and u["unit"] not in want:
            m = [w for w in want if plain(w) == plain(u["unit"])] or \
                [w for w in want if unbracketed(w) == unbracketed(u["unit"])]
            if len(m) == 1:
                remarks.append(f"unit {i}: {u['unit']!r} read as {m[0]!r}")
                u["unit"] = m[0]
    cps = kp["applies"]["contrasts"]
    for i, c in enumerate(lists("contrasts"), 1):
        if not isinstance(c, dict):
            continue
        if isinstance(c.get("contrast"), str) and c["contrast"] not in cps:
            m = [w for w in cps if plain(w) == plain(c["contrast"])]
            if len(m) == 1:
                remarks.append(f"contrast entry {i}: {c['contrast']!r} read as {m[0]!r}")
                c["contrast"] = m[0]
        if isinstance(c.get("controls"), dict):
            for fid in list(c["controls"]):
                word(c["controls"], fid, CONTROLS, f"contrast entry {i}", alias={"varied": "varies", "vary": "varies"})
    return r, remarks


def ids_ok(x, ids_all, where, faults, remarks):
    if not isinstance(x, list) or not all(isinstance(i, str) for i in x):
        faults.append(f"{where}: no list of ids")
        return
    if not x:
        remarks.append(f"{where}: an empty list of ids")
    if any(i not in ids_all for i in x):
        remarks.append(f"{where}: an id not the paper's")


def faults_of(rep, paper, key, index):
    """(faults, remarks) of one reply, by the docstring's rules."""
    claims, frags, _, _, core = structure(index)
    ids_all = set(claims) | set(frags) | {p["pair_id"] for p in index.get("contrast_pairs", [])} | \
        {g["gap_id"] for g in index.get("declared_gaps", [])} | {a["absence_id"] for a in index.get("absences", [])}
    kp = key["papers"][paper]
    listed = {o["id"]: (o["base"], o["claim"]) for o in kp["order"]}
    ap = kp["applies"]
    faults, remarks = [], []
    if not isinstance(rep, dict):
        return ["not a JSON object"], []
    missing = [k for k in KEYS if k not in rep]
    if missing:
        return [f"no key `{k}`" for k in missing], []
    if not (isinstance(rep["paper"], str) and AUTHOR[paper] in rep["paper"].lower()):
        remarks.append(f"`paper` does not name {AUTHOR[paper].capitalize()}")
    # part 1
    pairs = rep["pairs"]
    if not isinstance(pairs, list) or not all(isinstance(p, dict) for p in pairs):
        faults.append("`pairs` is not a list of objects")
    else:
        count = collections.Counter(st(p.get("pair")) for p in pairs)
        notlisted = sorted(str(k) for k in count if k not in listed)
        if notlisted:
            faults.append(f"pairs not in the list: {', '.join(notlisted[:8])}{' …' if len(notlisted) > 8 else ''}")
        twice_ = sorted(k for k, n in count.items() if k in listed and n > 1)
        if twice_:
            faults.append(f"pairs answered more than once: {', '.join(twice_)}")
        left = sorted(k for k in listed if k not in count)
        if left:
            faults.append(f"pairs not answered: {', '.join(left[:8])}{' …' if len(left) > 8 else ''} ({len(left)})")
        for p in pairs:
            pid = st(p.get("pair"))
            if pid not in listed:
                continue
            if (st(p.get("base")), st(p.get("claim"))) != listed[pid]:
                faults.append(f"{pid}: claim and base not the list's (does {listed[pid][1]} rest on {listed[pid][0]}?)")
            if not isinstance(p.get("rests_on"), bool):
                faults.append(f"{pid}: `rests_on` not true or false")
                continue
            if not nonempty(p.get("reason")):
                faults.append(f"{pid}: no reason")
            if p["rests_on"]:
                if p.get("type") not in TYPES:
                    faults.append(f"{pid}: type not one of {', '.join(TYPES)}")
                if p.get("strength") not in STRENGTHS:
                    faults.append(f"{pid}: strength not one of {', '.join(STRENGTHS)}")
                if not nonempty(p.get("basis")):
                    faults.append(f"{pid}: no basis")
                if not page_ok(p.get("page")):
                    faults.append(f"{pid}: no page number")
    # part 2
    fe = rep["further_edges"]
    if not isinstance(fe, list):
        faults.append("`further_edges` is not a list")
    else:
        if len(fe) > MAX_FURTHER:
            faults.append(f"more than {MAX_FURTHER} further edges ({len(fe)})")
        for i, e in enumerate(fe, 1):
            if not isinstance(e, dict):
                faults.append(f"further edge {i}: not an object")
                continue
            eb, ec = st(e.get("base")), st(e.get("claim"))
            if eb not in claims or ec not in claims or eb == ec:
                faults.append(f"further edge {i}: claim and base not two of the paper's claims")
            elif ec not in core:
                faults.append(f"further edge {i}: {ec} is not a core claim")
            elif (eb, ec) in set(listed.values()):
                remarks.append(f"further edge {i}: a listed pair")
            if e.get("type") not in TYPES or e.get("strength") not in STRENGTHS or not nonempty(e.get("basis")) \
                    or not page_ok(e.get("page")) or not nonempty(e.get("reason")):
                faults.append(f"further edge {i}: a type, strength, basis, page number or reason missing or not "
                              f"allowed")
    # part 3
    reg = rep["registry"]
    names = set(construct_names(index))
    if not isinstance(reg, list):
        faults.append("`registry` is not a list")
    else:
        seen = collections.Counter()
        for i, g in enumerate(reg, 1):
            if not isinstance(g, dict) or not nonempty(g.get("canonical")) or not isinstance(g.get("names"), list) \
                    or len(g["names"]) < 2 or not all(isinstance(n, str) for n in g["names"]):
                faults.append(f"registry group {i}: no canonical name, or fewer than two names")
                continue
            seen.update(set(g["names"]))
            if any(n not in names for n in g["names"]):
                remarks.append(f"registry group {i}: a name not among the sheet's construct names")
            if g["canonical"] not in g["names"]:
                remarks.append(f"registry group {i}: the canonical name not among its names")
        if any(n > 1 for n in seen.values()):
            remarks.append("a construct name in two registry groups")
    # part 4
    fac = rep["factors"]
    fids = []
    if not isinstance(fac, list):
        faults.append("`factors` is not a list")
    else:
        for i, x in enumerate(fac, 1):
            if not isinstance(x, dict) or not nonempty(x.get("id")) or not nonempty(x.get("name")) \
                    or st(x.get("claim")) not in claims:
                faults.append(f"factor {i}: no id, no name, or no claim of the paper")
                continue
            fids.append(x["id"])
        if len(set(fids)) != len(fids):
            faults.append("two factors with one id")
        if ap["factors"] and not fac:
            remarks.append("no factor, where part 5 or 6 applies")
    # part 5
    units = rep["units"]
    if not isinstance(units, list):
        faults.append("`units` is not a list")
    elif not ap["table"]:
        if units:
            remarks.append("units given where part 5 does not apply: left aside")
    else:
        want = [x["unit"] for x in ap["units"]]
        got = collections.Counter(st(u.get("unit")) for u in units if isinstance(u, dict))
        if sorted(got.elements()) != sorted(want) or len(units) != len(want):
            faults.append(f"the units not exactly the sheet's {len(want)}, each once")
        for i, u in enumerate(units, 1):
            if not isinstance(u, dict) or SIGNS.get(st(u.get("outcome"))) is None or not isinstance(u.get("values"), dict):
                faults.append(f"unit {i}: no outcome of + - ?, or no values")
                continue
            if any(SIGNS.get(st(u["values"].get(fid))) is None for fid in fids):
                faults.append(f"unit {i}: not a value of + - ? for every factor")
            ids_ok(u.get("ids"), ids_all, f"unit {i}", faults, remarks)
    # part 6
    con = rep["contrasts"]
    if not isinstance(con, list):
        faults.append("`contrasts` is not a list")
    elif not ap["contrasts"]:
        if con:
            remarks.append("contrasts given where part 6 does not apply: left aside")
    else:
        got = collections.Counter(st(c.get("contrast")) for c in con if isinstance(c, dict))
        for pid in ap["contrasts"]:
            if got[pid] != 1:
                faults.append(f"contrast pair {pid}: {got[pid]} entries, not one")
        for i, c in enumerate(con, 1):
            if not isinstance(c, dict) or st(c.get("contrast")) not in ap["contrasts"]:
                faults.append(f"contrast entry {i}: not for a contrast pair of the sheet")
                continue
            ctl = c.get("controls")
            if not isinstance(ctl, dict) or any(ctl.get(fid) not in CONTROLS for fid in fids):
                faults.append(f"contrast pair {c['contrast']}: not held, varies or unclear for every factor")
            ids_ok(c.get("ids"), ids_all, f"contrast pair {c['contrast']}", faults, remarks)
    return faults, remarks


def check_map(paper, key_path, path, folder=None):
    """Print the check of one reply; return its exit code (0 counts, 1 does not, 2 counts with a span to show)."""
    key = json.load(open(key_path, encoding="utf-8"))
    index, _ = load_index(paper, folder)
    rep, faults = bcs.load(path)
    remarks = []
    if not faults:
        dup = twice(path)
        faults = [f"a key given twice in one object: {', '.join(sorted(set(dup)))}"] if dup else []
        rep, remarks = normalized(rep, paper, key, index)
        f2, r2 = faults_of(rep, paper, key, index)
        faults += f2
        remarks += r2
    print(f"{paper} map reply: {os.path.basename(path)}, sha256 {sha(path)}")
    for f in faults:
        print(f"  FAULT: {f}")
    if faults:
        print("  DOES NOT COUNT")
        return 1
    for r in sorted(set(remarks)):
        print(f"  remark: {r}")
    edges = [p for p in rep["pairs"] if p["rests_on"]]
    print(f"  pairs answered {len(rep['pairs'])}; edges {len(edges)}; by type "
          f"{dict(sorted(collections.Counter(e['type'] for e in edges).items()))}; by strength "
          f"{dict(sorted(collections.Counter(e['strength'] for e in edges).items()))}")
    print(f"  further edges {len(rep['further_edges'])}; registry groups {len(rep['registry'])}; "
          f"factors {len(rep['factors'])}; units {len(rep['units'])}; contrast entries {len(rep['contrasts'])}")
    spans = bcs.long_spans(rep, index["meta"]["citation"])
    for where, words, unclosed, inside in spans:
        print(f"  QUOTED SPAN of more than {bcs.MAX_QUOTE} words: {where}: {words} words"
              f"{', unclosed' if unclosed else ''}{', within the citation' if inside else ''}")
    if spans:
        print("  COUNTS; the spans above go to the PI before the reply is filed, and are not filed")
        return 2
    print(f"  COUNTS; no quoted span of more than {bcs.MAX_QUOTE} words")
    return 0


# ---------------------------------------------------------------- self-test

def made_up_index(paper):
    """A small index in the frozen indexes' form: 6 claims (3 core), 14 passages, 2 units, one contrast pair."""
    frags = []
    for i in range(1, 15):
        unit = "ward A" if i <= 6 else ("ward B" if i <= 12 else "hospital")
        stub = "The ward changed its plating." if i != 13 else "Endorsement combined with budget led to change."
        frags.append({"paper_id": paper, "fragment_id": "F%02d" % i, "stub": stub, "text": "",
                      "text_status": "withheld", "data_type": "interview", "unit": unit,
                      "speaker_name": "Ann" if i == 1 else None, "period": "P1", "author_code": "CODE-X",
                      "author_gloss": "a gloss" if i == 2 else None, "citing_claims": [],
                      "location": "p. %d" % (10 + i), "extraction_confidence": "high", "notes": "NOTE-X"})
    claims = [
        ("C01", True, "Endorsement leads wards to adopt checklists.", "checklist adoption", ["endorsement", "adoption"]),
        ("C02", False, "Ward A adopted after endorsement.", "ward A checklist adoption", ["endorsement", "ward A"]),
        ("C03", False, "Ward B resisted without endorsement.", "ward B resistance", ["endorsement", "ward B"]),
        ("C04", True, "Endorsement mattered more than budget.", "none", ["endorsement", "budget"]),
        ("C05", True, "Identity and endorsement are intertwined.", "", ["identity", "endorsement", "adoption"]),
        ("C06", False, "Budgets shape checklist adoption speed.", "checklist adoption speed", ["budget"]),
    ]
    cl = [{"paper_id": paper, "claim_id": c, "statement": s, "constructs": k, "outcome": o, "asserted_direction": None,
           "core": core, "stated_as": "established", "location": "p. 20", "decomposed_into": [],
           "extraction_confidence": "high", "notes": "NOTE-Y"} for c, core, s, o, k in claims]
    links = []

    def link(f, c, d="illustrates"):
        links.append({"paper_id": paper, "fragment_id": f, "claim_id": c, "direction": d, "basis": "BASIS-Z",
                      "confidence": "high"})
    for i in range(1, 7):
        link("F%02d" % i, "C02", "with")
    for i in range(7, 13):
        link("F%02d" % i, "C03")
    for i in (1, 2, 3, 7, 8):
        link("F%02d" % i, "C01")
    link("F13", "C04", "with")
    link("F13", "C06")
    link("F14", "C05")
    return {"meta": {"paper_id": paper, "citation": "Doe, J. 2024. A made-up study of wards. Journal 1: 1-20.",
                     "periods": ["P1"], "resolution_period": None},
            "fragments": frags, "claims": cl, "claim_links": links,
            "contrast_pairs": [{"paper_id": paper, "pair_id": "CP01", "episode_a": "Ward A adopted.",
                                "episode_b": "Ward B resisted.", "held_comparable": "Same hospital.",
                                "differs_in": "Endorsement.", "fragments_a": ["F01"], "fragments_b": ["F07"],
                                "basis": "BASIS-Z", "drawn_by_authors": True}],
            "declared_gaps": [{"paper_id": paper, "gap_id": "DG01", "statement": "One hospital only.",
                               "kind": "scope_limit", "location": "p. 20", "bears_on": ["C01"]}],
            "absences": [{"paper_id": paper, "absence_id": "A01", "kind": "not_collected",
                          "evidence_class": "costs", "basis": "No cost data.", "bears_on": ["C06"],
                          "source": "extraction"}]}


def selftest():
    import contextlib
    import io
    import shutil
    import tempfile
    n_ok = n_bad = 0

    def expect(label, cond):
        nonlocal n_ok, n_bad
        if cond:
            n_ok += 1
            print(f"ok    {label}")
        else:
            n_bad += 1
            print(f"FAIL  {label}")

    tmp = tempfile.mkdtemp()
    try:
        src = os.path.join(tmp, "src")
        os.makedirs(src)
        for paper in PAPERS:
            with open(os.path.join(src, INDEX[paper]), "w") as f:
                json.dump(made_up_index(paper), f, indent=1)
        d = made_up_index("bechky")
        expect("unit claims: C02 (ward A) and C03 (ward B); not C01 (3 of 5 from one unit)",
               unit_claims(d) == {"C02": "ward A", "C03": "ward B"})
        ap = applies(d)
        expect("the table applies, to ward A (C02) and ward B (C03)",
               ap["table"] and ap["units"] == [{"unit": "ward A", "claim": "C02"}, {"unit": "ward B", "claim": "C03"}])
        d2 = made_up_index("bechky")
        d2["claims"][2]["outcome"] = "none"
        expect("the table does not apply when one unit claim has an outcome", applies(d2)["table"] is False)
        d3 = made_up_index("bechky")
        d3["contrast_pairs"] = []
        expect("with no table and no contrast pair, no factors", applies(d3)["table"] and applies(d3)["factors"]
               and not applies({**d2, "contrast_pairs": []})["factors"])
        d4 = made_up_index("bechky")
        d4["claim_links"] = [l for l in d4["claim_links"] if not (l["claim_id"] == "C03" and l["fragment_id"] > "F10")]
        expect("a claim with 4 linked passages is no unit claim", "C03" not in unit_claims(d4))
        cand = candidates(d)
        expect("level: C02 to C01 (unit claim, shared construct)", "level" in cand.get(("C02", "C01"), []))
        expect("level: C02 to C04 (shares 'endorsement')", "level" in cand.get(("C02", "C04"), []))
        expect("shared passages: C02 to C01 (F01 to F03)", "shared passages" in cand.get(("C02", "C01"), []))
        expect("shared passages: not C03 to C01 (two shared)", "shared passages" not in cand.get(("C03", "C01"), []))
        d5 = made_up_index("bechky")
        for c in ("C04", "C05", "C06", "C03"):
            for f in ("F01", "F02", "F03"):
                d5["claim_links"].append({"fragment_id": f, "claim_id": c, "direction": "illustrates"})
        for c in ("X1", "X2"):
            d5["claims"].append({**d5["claims"][5], "claim_id": c})
            for f in ("F01", "F02", "F03"):
                d5["claim_links"].append({"fragment_id": f, "claim_id": c, "direction": "illustrates"})
        expect("shared passages: passages linked to more than 6 claims are left out",
               "shared passages" not in candidates(d5).get(("C02", "C01"), []))
        expect("chaining: C06's outcome and C04's constructs share one word only (budget)",
               "chaining" not in cand.get(("C06", "C04"), []))
        expect("chaining: C06's outcome and C05's constructs share one word only (adoption)",
               "chaining" not in cand.get(("C06", "C05"), []))
        d6 = made_up_index("bechky")
        d6["claims"][5]["outcome"] = "identity endorsement"
        expect("chaining: an outcome sharing two content words with a core claim's constructs",
               "chaining" in candidates(d6).get(("C06", "C05"), []))
        d6["claims"][5]["outcome"] = "the identity of endorsement"
        expect("chaining: stop words do not count, content words do",
               "chaining" in candidates(d6).get(("C06", "C05"), []))
        expect("stated tie: F13 says 'combined with' and links C04 and C06: does C04 rest on C06",
               "stated tie" in cand.get(("C06", "C04"), []))
        expect("no pair has a claim that is not core", all(c in ("C01", "C04", "C05") for _, c in cand))
        d8 = made_up_index("bechky")
        d8["claims"][2]["core"] = True
        expect("level: not from one unit claim to another (C02 to C03, now core)",
               "level" not in candidates(d8).get(("C02", "C03"), []) and "level" in candidates(d8).get(("C02", "C01"), []))
        hits = []
        for ph in PHRASES:
            d9 = made_up_index("bechky")
            d9["fragments"][12]["stub"] = f"Endorsement {ph} budget."
            hits.append("stated tie" in candidates(d9).get(("C06", "C04"), []))
        d9["fragments"][12]["stub"] = "Endorsement and budget."
        d9["fragments"][12]["author_gloss"] = "The author says budget BUILDS ON endorsement."
        expect("stated tie: each phrase alone, and in a gloss, in any case",
               all(hits) and len(hits) == 7 and "stated tie" in candidates(d9).get(("C06", "C04"), []))
        two = {"bechky": d, "pratt": made_up_index("pratt")}
        s = {"bechky": 3, "pratt": 4}
        dr1, dr2 = draw(two, 7, s), draw(two, 7, s)
        expect("the draw is the same twice", dr1 == dr2)
        o = dr1["bechky"]["order"]
        expect("candidates plus the sample, numbered P001 onward",
               len(o) == len(cand) + 3 and [x["id"] for x in o] == ["P%03d" % i for i in range(1, len(o) + 1)])
        expect("no pair twice", len({(x["base"], x["claim"]) for x in o}) == len(o))
        expect("the sample holds no candidate", all(x["rules"] == [] for x in o if x["source"] == "sample"))
        rng = random.Random(7)
        oth = {p: [q for q in all_pairs(two[p]) if q not in candidates(two[p])] for p in PAPERS}
        pb, pp = rng.sample(oth["bechky"], 3), rng.sample(oth["pratt"], 4)
        cb = sorted(list(candidates(d)) + pb, key=lambda q: (num(q[0]), num(q[1])))
        rng.shuffle(cb)
        expect("the draw: both samples first, Bechky's then Pratt's, then the shuffles",
               [(x["base"], x["claim"]) for x in o] == cb)
        expect("another seed gives another order", draw(two, 8, s) != dr1)
        out1, out2 = os.path.join(tmp, "o1"), os.path.join(tmp, "o2")
        with contextlib.redirect_stdout(io.StringIO()):
            f1 = build(out1, 7, folder=src, sample=s)
            f2 = build(out2, 7, folder=src, sample=s)
        expect("two builds give the same bytes", f1 == f2)
        sh = f1["MAP_SHEET_bechky.md"].decode()
        expect("the sheet holds no voice or author code, no note, no basis, no confidence",
               not any(x in sh for x in ("CODE-X", "NOTE-X", "NOTE-Y", "BASIS-Z", "high", "confidence")))
        expect("the sheet does not say which pairs are candidates",
               "candidate" not in sh.lower() and "sample" not in sh.lower() and "rule" not in sh.lower())
        expect("the sheet gives each claim's passages by direction",
               "*passages:* with: F01, F02, F03, F04, F05, F06" in sh)
        expect("the sheet lists every pair, as a question",
               all(f"**{x['id']}**: does {x['claim']} rest on {x['base']}?" in sh for x in o))
        expect("the sheet names the table's units", "`ward A` (C02); `ward B` (C03)" in sh)
        expect("the sheet lists the construct names", "- endorsement: C01, C02, C03, C04, C05" in sh)
        expect("the sheet gives a speaker and a gloss where kept", "speaker: Ann" in sh and "*gloss:* a gloss" in sh)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                build(out1, 7, folder=src, sample=s)
            expect("refuses to write over a file", False)
        except SystemExit:
            expect("refuses to write over a file", True)
        key = json.loads(f1["map_key.json"])
        expect("the key holds the seed, the rules, the inputs and the builder's sha256",
               key["seed"] == 7 and key["rules"]["phrases"] == list(PHRASES) and len(key["inputs"]) == 2
               and len(key["builder_sha256"]) == 64)
        kpath = os.path.join(out1, "map_key.json")
        order = key["papers"]["bechky"]["order"]
        edge = [x["id"] for x in order if (x["base"], x["claim"]) == ("C02", "C01")][0]
        listed = {(x["base"], x["claim"]) for x in order}
        free = [(b, c) for b, c in all_pairs(d) if (b, c) not in listed]

        def good():
            pairs = []
            for x in order:
                p = {"pair": x["id"], "claim": x["claim"], "base": x["base"], "rests_on": x["id"] == edge,
                     "reason": "Ward A is one instance of C01." if x["id"] == edge else "No tie."}
                if x["id"] == edge:
                    p.update({"type": "evidential", "strength": "contributing", "basis": "F01 to F03",
                              "page": "p. 12"})
                pairs.append(p)
            return {"paper": "Bechky (made up)", "pairs": pairs,
                    "further_edges": [{"claim": free[0][1], "base": free[0][0], "type": "comparative",
                                       "strength": "contributing", "basis": "the ranking", "page": "p. 20",
                                       "reason": "A ranking."}],
                    "registry": [{"canonical": "endorsement", "names": ["endorsement", "adoption"]}],
                    "factors": [{"id": "X1", "name": "endorsement", "claim": "C01"}],
                    "units": [{"unit": "ward A", "outcome": "+", "values": {"X1": "+"}, "ids": ["C02", "F01"]},
                              {"unit": "ward B", "outcome": "−", "values": {"X1": "-"}, "ids": ["C03"]}],
                    "contrasts": [{"contrast": "CP01", "controls": {"X1": "varies"}, "ids": ["F01", "F07"]}]}

        def run(name, rep, raw=None):
            p = os.path.join(tmp, name)
            with open(p, "w") as f:
                f.write(raw if raw is not None else "Here it is:\n```json\n" + json.dumps(rep) + "\n```\n")
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = check_map("bechky", kpath, p, folder=src)
            return rc, buf.getvalue()

        rc, txt = run("good.json", good())
        expect("a good reply counts, with no remark", rc == 0 and "COUNTS" in txt and "remark" not in txt)
        r = good(); r["pairs"].pop(0)
        expect("a pair left out: does not count", run("a.json", r)[0] == 1)
        r = good(); r["pairs"].append(dict(r["pairs"][0]))
        expect("a pair answered twice: does not count", run("b.json", r)[0] == 1)
        r = good(); r["pairs"].append({"pair": "P999", "claim": "C01", "base": "C02", "rests_on": False, "reason": "x"})
        expect("a pair not in the list: does not count", run("c.json", r)[0] == 1)
        r = good(); x = [p for p in r["pairs"] if p["pair"] == edge][0]; x["claim"], x["base"] = x["base"], x["claim"]
        expect("a pair with claim and base swapped: does not count", run("d.json", r)[0] == 1)
        r = good(); [p for p in r["pairs"] if p["pair"] == edge][0]["type"] = "logical"
        expect("a type not in the list: does not count", run("e.json", r)[0] == 1)
        r = good(); [p for p in r["pairs"] if p["pair"] == edge][0]["strength"] = "strong"
        expect("a strength not in the list: does not count", run("f.json", r)[0] == 1)
        r = good(); [p for p in r["pairs"] if p["pair"] == edge][0]["page"] = "see the paper"
        expect("an edge with no page number: does not count", run("g.json", r)[0] == 1)
        r = good(); del [p for p in r["pairs"] if p["pair"] == edge][0]["basis"]
        expect("an edge with no basis: does not count", run("h.json", r)[0] == 1)
        r = good(); r["pairs"][0]["rests_on"] = "no"
        expect("rests_on not true or false: does not count", run("i.json", r)[0] == 1)
        r = good(); r["pairs"][0]["reason"] = " "
        expect("an empty reason: does not count", run("j.json", r)[0] == 1)
        r = good(); r["further_edges"][0]["claim"] = "C06"
        expect("a further edge whose claim is not core: does not count", run("k.json", r)[0] == 1)
        r = good(); r["further_edges"] = r["further_edges"] * 11
        expect("more than ten further edges: does not count", run("l.json", r)[0] == 1)
        r = good(); r["further_edges"][0].update({"claim": "C01", "base": "C02"})
        rc, txt = run("m.json", r)
        expect("a further edge that is a listed pair: a remark", rc == 0 and "a listed pair" in txt)
        r = good(); r["registry"][0]["names"] = ["endorsement"]
        expect("a registry group of one name: does not count", run("n.json", r)[0] == 1)
        r = good(); r["registry"][0]["names"] = ["endorsement", "endorsing"]
        rc, txt = run("o.json", r)
        expect("a registry name not among the construct names: a remark", rc == 0 and "not among" in txt)
        r = good(); r["registry"][0]["canonical"] = "approval"
        rc, txt = run("p0.json", r)
        expect("a canonical name not among its group's names: a remark", rc == 0 and "canonical name not among" in txt)
        r = good(); r["registry"].append({"canonical": "adoption", "names": ["adoption", "budget"]})
        rc, txt = run("p.json", r)
        expect("a name in two groups: a remark", rc == 0 and "two registry groups" in txt)
        r = good(); r["factors"] = []
        rc, txt = run("q.json", r)
        expect("no factor where the table applies: a remark, and it counts", rc == 0 and "no factor" in txt)
        r = good(); x = [p for p in r["pairs"] if p["pair"] == edge][0]; x["type"] = " Evidential"; x["page"] = 12
        r["contrasts"][0]["controls"]["X1"] = "Varied"; r["units"][0]["unit"] = "Ward  A"; r["factors"][0]["claim"] = ["C01", "C04"]
        r["contrasts"][0]["contrast"] = "cp01"; r["units"][1]["outcome"] = "\u2013"; r["units"][1]["unit"] = "`ward B`"
        [p for p in r["pairs"] if p["pair"] == edge][0]["page"] = 12.0
        rc, txt = run("q2.json", r)
        expect("lenient readings: type, page, control, unit, factor claim, contrast pair; each a remark, and it counts",
               rc == 0 and all(w in txt for w in ("read as 'evidential'", "read as 'p. 12'", "read as 'varies'",
                                                   "read as 'ward A'", "read as 'C01'", "read as 'CP01'",
                                                   "read as 'ward B'")))
        rr, rem = normalized({"units": [{"unit": "ward  a (east wing)"}, {"unit": "Ward B"}], "contrasts": []}, "bechky",
                             {"papers": {"bechky": {"applies": {"units": [{"unit": "ward A (east wing)"},
                                                                          {"unit": "ward B"}], "contrasts": []}}}}, d)
        rr2, rem2 = normalized({"units": [{"unit": "ward A"}]}, "bechky",
                               {"papers": {"bechky": {"applies": {"units": [{"unit": "ward A (east)"}, {"unit": "ward B"}],
                                                                  "contrasts": []}}}}, d)
        rr3, rem3 = normalized({"units": [{"unit": "ward"}]}, "bechky",
                               {"papers": {"bechky": {"applies": {"units": [{"unit": "ward (east)"}, {"unit": "ward (west)"}],
                                                                  "contrasts": []}}}}, d)
        expect("units: read in other case and spacing, or without the words in brackets, when one unit alone fits",
               [u["unit"] for u in rr["units"]] == ["ward A (east wing)", "ward B"] and rr2["units"][0]["unit"] ==
               "ward A (east)" and rr3["units"][0]["unit"] == "ward" and not rem3)
        r = good(); r["factors"].append({"id": "X1", "name": "budget", "claim": "C04"})
        expect("two factors with one id: does not count", run("r.json", r)[0] == 1)
        r = good(); r["factors"][0]["claim"] = "C99"
        expect("a factor with a claim not the paper's: does not count", run("s.json", r)[0] == 1)
        r = good(); r["units"].pop()
        expect("a unit of the sheet left out: does not count", run("t.json", r)[0] == 1)
        r = good(); r["units"][1]["unit"] = "ward C"
        expect("a unit not the sheet's: does not count", run("u.json", r)[0] == 1)
        r = good(); r["units"][0]["values"] = {}
        expect("a unit without a value for a factor: does not count", run("v.json", r)[0] == 1)
        r = good(); r["units"][0]["outcome"] = "yes"
        expect("an outcome not + - ?: does not count", run("w.json", r)[0] == 1)
        r = good(); del r["units"][0]["ids"]
        expect("a unit without a list of ids: does not count", run("x.json", r)[0] == 1)
        r = good(); r["contrasts"] = []
        expect("a contrast pair left out: does not count", run("y.json", r)[0] == 1)
        r = good(); r["contrasts"][0]["controls"]["X1"] = "same"
        expect("a control not held, varies or unclear: does not count", run("z.json", r)[0] == 1)
        r = good(); r["contrasts"].append({"contrast": "CP09", "controls": {"X1": "held"}, "ids": []})
        expect("a contrast entry for a pair not the sheet's: does not count", run("za.json", r)[0] == 1)
        r = good(); r["contrasts"][0]["ids"] = ["F99"]
        rc, txt = run("zb.json", r)
        expect("an id not the paper's: a remark", rc == 0 and "an id not the paper's" in txt)
        r = good(); r["paper"] = "Doe"
        rc, txt = run("zc.json", r)
        expect("`paper` not naming the author: a remark", rc == 0 and "does not name" in txt)
        r = good(); [p for p in r["pairs"] if p["pair"] == edge][0]["reason"] = \
            'The paper says "' + " ".join(["word"] * 10) + '" here.'
        rc, txt = run("zd.json", r)
        expect("a quoted span of ten words is named, not printed",
               rc == 2 and "10 words" in txt and "word word" not in txt)
        r = good(); r["pairs"][0]["pair"] = ["P001"]; r["units"][0]["outcome"] = ["+"]
        r["factors"][0]["claim"] = {"C": 1}; r["contrasts"][0]["contrast"] = ["CP01"]
        expect("values of the wrong kind: does not count, and the check does not stop", run("zz.json", r)[0] == 1)
        r = good(); del r["registry"]
        expect("a missing key: does not count", run("ze.json", r)[0] == 1)
        raw = json.dumps(good()).replace('"paper": "Bechky (made up)"', '"paper": "Bechky", "paper": "Bechky"', 1)
        expect("a key given twice in one object: does not count", run("zf.json", None, raw=raw)[0] == 1)
        expect("no JSON object: does not count", run("zg.json", None, raw="no object here")[0] == 1)
        d7 = made_up_index("pratt")
        d7["claims"][2]["outcome"] = "none"
        with open(os.path.join(src, INDEX["pratt"]), "w") as f:
            json.dump(d7, f)
        out3 = os.path.join(tmp, "o3")
        with contextlib.redirect_stdout(io.StringIO()):
            f3 = build(out3, 7, folder=src, sample=s)
        sh3 = f3["MAP_SHEET_pratt.md"].decode()
        expect("where the table does not apply, the sheet says so", "comparative table:** does not apply" in sh3)
        k3 = os.path.join(out3, "map_key.json")
        r = good()
        r["pairs"] = [{"pair": x["id"], "claim": x["claim"], "base": x["base"], "rests_on": False, "reason": "No."}
                      for x in json.loads(f3["map_key.json"])["papers"]["pratt"]["order"]]
        r["paper"] = "Pratt (made up)"
        r["further_edges"] = []
        p = os.path.join(tmp, "zh.json")
        with open(p, "w") as f:
            json.dump(r, f)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = check_map("pratt", k3, p, folder=src)
        expect("units given where the table does not apply: a remark, and the reply counts",
               rc == 0 and "units given where part 5 does not apply" in buf.getvalue())
    finally:
        shutil.rmtree(tmp)
    print(f"{n_ok} checks passed, {n_bad} failed")
    print("SELFTEST PASSES" if n_bad == 0 else "SELFTEST FAILS")
    return 0 if n_bad == 0 else 1


def main(argv):
    if argv[1:] == ["--selftest"]:
        return selftest()
    if len(argv) == 4 and argv[1] == "pairs" and re.fullmatch(r"--seed=\d+", argv[2]):
        build(argv[3], int(argv[2].split("=")[1]))
        return 0
    if len(argv) == 5 and argv[1] == "check-map" and argv[2] in PAPERS:
        return check_map(argv[2], argv[3], argv[4])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
