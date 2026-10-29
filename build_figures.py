"""
build_figures.py: T27, the figures for the proposal, made by script from the
results files.

WHAT
----
One table per paper, Bechky 2020 and Pratt 2000, of the figures the proposal
may cite, and one table across the two papers. Every number is read from a
results file, or worked out from the files that a results file was worked out
from. Where a results file states a figure, the script works it out again and
refuses to write anything if the two differ. No number is typed. Each row
names its source.

Per paper:
  1. The record: the first return; the PI's coverage check and what the
     coverage chat added; the frozen record.
  2. Agreement between the two codings, model against model, per field. The
     figures are `agreement.py`'s own record of the paper (`paper_results`),
     and the paper's agreement log is written again from that record in
     memory and must equal the file byte for byte. Kappa is withheld under 10
     comparable judgements, by count only. For Pratt, the second count,
     without the coverage chat's additions and F109, from
     `second_count.py`, whose log must equal its file the same way.
  3. `against` and the audit, as coded and with the links the `against` check
     flags counted as `illustrates`: both versions, from the same record.
  4. The wager test (T29): the attack, the markers' agreement (Pratt's below
     the bar of 0.60, reported by a decision made after the result), the rates
     by arm, and the PI's worth by arm (declared not blind).
  5. Tests added after the plan: T31, the judges; T32, readings at places
     (Bechky); T33, the matching test (Bechky); T34, the authors' worth (no
     reply in); T35, the second extraction (Bechky).
Across the two papers: the counts that the pinned predictions are read on,
by their numbers only (their words are in no file); the judges' figures
over both papers; the attack beside worth; and the models, settings and times
of every chat, from `chats_models_hours.json`.

NEW FIGURES, marked "new" in the tables and in no results file before:
  - 95% intervals for kappas reported without one: the wager test's markers on
    each paper (seven codes), T32's markers, and T33's four kappas (A, B, Bj
    and the claim tags) with P_A, P_B and P_Bj. 2,000 resamples with
    replacement, of the sentences for the markers and of the 28 readings for
    T33 (as `score_matching.py` resamples them); the seed 20261019, one
    generator for each paper's markers, one for T32's and one for T33; the
    ends are the 2.5th and 97.5th percentiles as `agreement.py` takes them for
    the markers, and as `score_matching.py` takes them for T33. A resample
    with no kappa is left out and counted.
  - In each of Bechky's two returns, its `with` links and how many rest on a
    passage that the same return codes `author_insight`.

USAGE
-----
    python3 -B build_figures.py build --out=<folder>
    python3 -B build_figures.py selftest

`build` writes FIGURES_bechky_2020.md, FIGURES_pratt_2000.md, FIGURES_across.md
and figures.json into <folder>, which must exist. It writes over a file of
those names only if the file is one this script wrote. Nothing is written if
any check fails. figures.json holds every figure with its full precision, its
source and the sha256 of every file read.
"""
import collections
import contextlib
import hashlib
import io
import itertools
import json
import os
import random
import re
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

SEED = 20261019
RESAMPLES = 2000
PAPERS = ("bechky_2020", "pratt_2000")
NAME = {"bechky_2020": "Bechky 2020", "pratt_2000": "Pratt 2000"}
UPPER = {"bechky_2020": "BECHKY", "pratt_2000": "PRATT"}
SHORT = {"bechky_2020": "bechky", "pratt_2000": "pratt"}
TITLE = "# T27: the figures for the proposal"
OUTPUTS = ["FIGURES_bechky_2020.md", "FIGURES_pratt_2000.md", "FIGURES_across.md", "figures.json"]


class Refused(Exception):
    pass


# ------------------------------------------------------------------ files

READ = {}


def rel(name):
    return os.path.join(HERE, name)


def sha_of(name):
    return hashlib.sha256(open(rel(name), "rb").read()).hexdigest()


def note_read(name):
    if name not in READ:
        READ[name] = sha_of(name)
    return name


def read_json(name):
    note_read(name)
    return json.load(open(rel(name), encoding="utf-8"))


def read_text(name):
    note_read(name)
    return open(rel(name), encoding="utf-8").read()


def once(pattern, text, what):
    """The one match of a pattern in a results file's text, or refuse."""
    found = re.findall(pattern, text, flags=re.M)
    if len(found) != 1:
        raise Refused(f"{what}: expected one match of its line in the results file, found {len(found)}")
    return found[0]


def same(a, b, what, places=None):
    """Refuse unless a figure worked out here equals the results file's."""
    if places is not None:
        ok = a is not None and b is not None and round(float(a), places) == round(float(b), places)
    else:
        ok = a == b
    if not ok:
        raise Refused(f"{what}: worked out here {a!r}, in the results file {b!r}")


def dec(x, places):
    s = f"{x:.{places}f}"
    return s[1:] if s.startswith("-") and not s.strip("-0.") else s


def k_iv(k, lo, hi, n_ok=None, reps=RESAMPLES):
    if lo is None or hi is None:
        return f"kappa {dec(k, 3)} (no interval: no resample gave a kappa)"
    s = f"kappa {dec(k, 3)} (95% interval {dec(lo, 2)} to {dec(hi, 2)}"
    if n_ok is not None and n_ok < reps:
        s += f"; {n_ok:,} of {reps:,} resamples gave a kappa"
    return s + ")"


# ------------------------------------------------------------------ the table

class Out:
    def __init__(self):
        self.rows = []          # (paper, section, label, value, source, new)
        self.records = []

    def add(self, paper, section, fid, label, value, source, raw=None, new=False):
        self.rows.append((paper, section, label, value, source, new))
        self.records.append({"id": fid, "paper": paper, "section": section, "label": label,
                             "value": value, "source": source, "raw": raw, "new": new})


# ------------------------------------------------------------------ 1. the record

def links_by_direction(c):
    return collections.Counter(l["direction"] for l in c["claim_links"])


def record_key(kind, r):
    if kind == "fragments":
        return r["fragment_id"]
    if kind == "claims":
        return r["claim_id"]
    return (r["fragment_id"], r["claim_id"])


def natural(k):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", str(k))]


def diff_records(a, b):
    """What b adds to a, which records of a it changes (with the fields that
    differ), and which fields of the head differ, by kind."""
    out = {}
    for kind in ("fragments", "claims", "claim_links"):
        ra = {record_key(kind, r): r for r in a[kind]}
        rb = {record_key(kind, r): r for r in b[kind]}
        out[kind] = {"added": sorted(set(rb) - set(ra), key=natural), "gone": sorted(set(ra) - set(rb), key=natural),
                     "changed": {k: sorted(f for f in set(ra[k]) | set(rb[k]) if ra[k].get(f) != rb[k].get(f))
                                 for k in sorted(set(ra) & set(rb), key=natural) if ra[k] != rb[k]}}
    ma, mb = a.get("meta") or {}, b.get("meta") or {}
    out["meta"] = sorted(f for f in set(ma) | set(mb) if ma.get(f) != mb.get(f))
    return out


def changed_text(dd):
    """The records a later file changes, in words: a record whose only change is
    its list of citing claims is counted, any other is named with its fields."""
    named, citing = [], 0
    for kind in ("fragments", "claims", "claim_links"):
        for k, fields in dd[kind]["changed"].items():
            if fields == ["citing_claims"]:
                citing += 1
            else:
                named.append(f"{k if isinstance(k, str) else '→'.join(k)} ({', '.join(fields)})")
    parts = named + ([f"{citing} fragment(s) in their list of citing claims only"] if citing else [])
    s = "; ".join(parts) or "none"
    if dd["meta"]:
        s += f"; in the head: {', '.join(dd['meta'])}"
    gone = sum(len(dd[k]["gone"]) for k in ("fragments", "claims", "claim_links"))
    return s + (f"; records gone: {gone}" if gone else "")


def section_record(o, p):
    S = "1. The record"
    first_name, voice_name = f"{p}_corpus.json", f"{p}_voice_gloss.json"
    first, fvoice = read_json(first_name), read_json(voice_name)
    reported = sum(1 for v in fvoice["voice"] if v["code"] == "reported")
    d = links_by_direction(first)
    o.add(p, S, f"{p}.first.fragments", "First return: fragments (of them coded `reported` by its own voice file)",
          f"{len(first['fragments'])} ({reported} `reported`)", f"`{first_name}`, `{voice_name}`",
          {"fragments": len(first["fragments"]), "reported": reported})
    o.add(p, S, f"{p}.first.claims_links", "First return: claims; links by direction",
          f"{len(first['claims'])} claims; {len(first['claim_links'])} links: "
          + ", ".join(f"{d[k]} `{k}`" for k in ("with", "against", "illustrates", "qualifies")),
          f"`{first_name}`", {"claims": len(first["claims"]), "links": len(first["claim_links"]), **d})

    lst_name = f"{p}_coverage_list.txt"
    lines = [l.strip() for l in read_text(lst_name).splitlines() if l.strip()]
    distinct = len(dict.fromkeys(lines))
    dup = len(lines) - distinct
    o.add(p, S, f"{p}.coverage.list", "The PI's coverage check: passages listed",
          f"{distinct}" + (f" ({len(lines)} lines, of which {dup} repeat(s) an earlier line)" if dup else ""),
          f"`{lst_name}`", {"lines": len(lines), "distinct": distinct})

    cov_name = f"{p}_coverage_corpus.json"
    cov = read_json(cov_name)
    dd = diff_records(first, cov)
    o.add(p, S, f"{p}.coverage.chat", "The coverage chat: what it added to the first return, and what of the first "
          "return it changed",
          f"{len(dd['fragments']['added'])} fragments, {len(dd['claims']['added'])} claims, "
          f"{len(dd['claim_links']['added'])} links added; changed: " + changed_text(dd),
          f"`{first_name}` and `{cov_name}`, record by record",
          {k: {kk: len(vv) for kk, vv in dd[k].items()} for k in ("fragments", "claims", "claim_links")}
          | {"meta": dd["meta"]})

    v1_name, v1v_name = f"{p}_v1.json", f"{p}_v1_voice_gloss.json"
    v1, v1v = read_json(v1_name), read_json(v1v_name)
    import agreement as A
    directional = A.directional_claims(v1)
    core = sum(1 for c in v1["claims"] if c.get("core") is True)
    stated = collections.Counter(c.get("stated_as") for c in v1["claims"])
    voice = collections.Counter(v["code"] for v in v1v["voice"])
    fz = diff_records(cov, v1)
    added = sum(len(fz[k]["added"]) for k in ("fragments", "claims", "claim_links"))
    o.add(p, S, f"{p}.frozen", "The frozen record: fragments, claims, links; what the freeze changed in the "
          "coverage chat's return",
          f"{len(v1['fragments'])} fragments, {len(v1['claims'])} claims, {len(v1['claim_links'])} links; "
          f"records added: {added}; changed: " + changed_text(fz),
          f"`{v1_name}`, `{cov_name}`",
          {"fragments": len(v1["fragments"]), "claims": len(v1["claims"]), "links": len(v1["claim_links"]),
           "meta": fz["meta"]})
    o.add(p, S, f"{p}.frozen.claims", "The frozen record: claims that name an outcome (directional), core, stated as",
          f"{len(directional)} directional of {len(v1['claims'])}; {core} core; "
          + ", ".join(f"{stated[k]} {k}" for k in sorted(stated, key=str)),
          f"`{v1_name}` (`agreement.directional_claims`)",
          {"directional": len(directional), "core": core, "stated_as": dict(stated)})
    o.add(p, S, f"{p}.frozen.voice", "The frozen record: voice, coder 1's (the extraction's sidecar)",
          ", ".join(f"{voice[k]} `{k}`" for k in sorted(voice)), f"`{v1v_name}`", dict(voice))


# ------------------------------------------------------------------ 2 and 3. agreement, `against`, audit

def label_of(p):
    line = once(r"^- \*\*Who they are:\*\* (Model against model\..*)$",
                read_text(f"{UPPER[p]}_AGREEMENT_LOG.md"), f"{p}: the agreement log's line on who the coders are")
    return " ".join(line.split())


def agreement_args(p):
    stages = {st: f"returned_{p}_STAGE_{st}_coder2.xlsx" for st in ("A", "A2", "V", "B")}
    return {"corpus": f"{p}_v1.json", "sidecar": f"{p}_v1_voice_gloss.json",
            "key": f"packs/{p}/key/{p}_pack_key.json", "stages": stages,
            "readings": f"{p}_readings.json", "against": "against_check_results.json"}


def agreement_res(p):
    import agreement as A
    a = agreement_args(p)
    for name in [a["corpus"], a["sidecar"], a["key"], *a["stages"].values(), a["readings"], a["against"]]:
        note_read(name)
    res = A.paper_results(rel(a["corpus"]), rel(a["sidecar"]), rel(a["key"]),
                          {st: rel(f) for st, f in a["stages"].items()}, rel(a["readings"]), rel(a["against"]))
    log_name = f"{UPPER[p]}_AGREEMENT_LOG.md"
    if A.paper_log(res, label_of(p)) != read_text(log_name):
        raise Refused(f"{p}: the agreement log written again from agreement.py's record differs from "
                      f"{log_name}; no figure is taken from it")
    return res


def second_count_res():
    import agreement as A
    import second_count as SC
    p = "pratt_2000"
    a = agreement_args(p)
    note_read("pratt_2000_second_count.json")
    got = {}
    real = A.paper_log

    def capture(res, label=None):
        got["res"] = res
        return real(res, label)

    A.paper_log = capture
    try:
        with tempfile.TemporaryDirectory() as td:
            log_path = os.path.join(td, "PRATT_SECOND_COUNT_LOG.md")
            argv = [f"--leave-out={rel('pratt_2000_second_count.json')}", rel(a["corpus"]),
                    f"--sidecar={rel(a['sidecar'])}", f"--key={rel(a['key'])}", f"--log={log_path}",
                    f"--label={label_of(p)}"]
            argv += [f"--{st.lower()}={rel(f)}" for st, f in a["stages"].items()]
            argv += [f"--readings={rel(a['readings'])}", f"--against={rel(a['against'])}"]
            with contextlib.redirect_stdout(io.StringIO()):
                rc = SC.main(argv)
            if rc != 0:
                raise Refused("second_count.py refused to run")
            text = open(log_path, encoding="utf-8").read()
    finally:
        A.paper_log = real
    if text != read_text("PRATT_SECOND_COUNT_LOG.md"):
        raise Refused("the second count's log written again differs from PRATT_SECOND_COUNT_LOG.md")
    return got["res"]


def fig_raw(rec):
    return {k: rec[k] for k in ("n", "agree", "raw", "kappa", "kappa_note", "interval", "resamples")}


def section_agreement(o, p, res, tag, src):
    import agreement as A
    S = "2. Agreement, model against model" + (" — the second count" if tag else "")
    t = tag or ""
    o.add(p, S, f"{p}{t}.counts", "Records compared",
          f"{res['counts']['fragments']} fragments, {res['counts']['claims']} claims "
          f"({res['counts']['directional']} directional), {res['counts']['links']} links", src, res["counts"])
    a = res["A"]
    o.add(p, S, f"{p}{t}.A", "Stage A: whether a claim names an outcome", A.fig_text(a["fig"]), src, fig_raw(a["fig"]))
    if a.get("fig_as_read"):
        o.add(p, S, f"{p}{t}.A_as_read", "Stage A, with the reader's calls that coder 2's wording means none",
              A.fig_text(a["fig_as_read"]), src, fig_raw(a["fig_as_read"]))
    calls = a["calls"]
    o.add(p, S, f"{p}{t}.A_wordings", "Stage A: claims where both name an outcome, the two wordings by reading",
          f"{len(a['both'])} claims: " + ", ".join(f"{calls[k]} {k}" for k in sorted(calls)), src, dict(calls))
    a2 = res["A2"]
    c2 = a2["calls"]
    o.add(p, S, f"{p}{t}.A2", "Stage A2: the asserted direction's sign, by reading",
          f"{a2['sent']} claims sent; coder 2 gives a direction on {len(a2['rows'])}, none on {len(a2['none'])}; "
          "the sign by reading: " + ", ".join(f"{c2[k]} {k}" for k in sorted(c2)), src,
          {"sent": a2["sent"], "rows": len(a2["rows"]), "none": len(a2["none"]), "calls": dict(c2)})
    o.add(p, S, f"{p}{t}.V", "Stage V: voice", A.fig_text(res["V"]["fig"]), src, fig_raw(res["V"]["fig"]))
    d = res["B"]["direction"]
    o.add(p, S, f"{p}{t}.B.direction", "Stage B: link direction, all links", A.fig_text(d["fig"]), src, fig_raw(d["fig"]))
    o.add(p, S, f"{p}{t}.B.direction_directional", "Stage B: link direction, links to directional claims",
          A.fig_text(d["fig_directional"]), src, fig_raw(d["fig_directional"]))
    for field, rec in res["B"]["fields"].items():
        title = re.sub(r"^\d+\.\s*", "", rec["title"])
        o.add(p, S, f"{p}{t}.B.{field}", f"Stage B: {title.lower()}", A.fig_text(rec["fig"]), src, fig_raw(rec["fig"]))


def against_text(s):
    if not s["links"]:
        return "none"
    return (f"{len(s['links'])} on {len(s['per_claim'])} claim(s); at most {s['most']} on one claim "
            f"({', '.join(s['most_on'])}); claims with two or more: {', '.join(s['two_or_more']) or 'none'}")


def audit_text(x):
    return (f"coverage {dec(x['coverage'], 3)} ({x['assessed']} of {x['directional']} directional claims assessed); "
            f"seams: {len(x['seams'])}")


def section_against(o, p, res, tag, src):
    S = "3. `against` and the audit, in both versions" + (" — the second count" if tag else "")
    t = tag or ""
    ag, chk = res["against"], res["against"]["check"]
    for who, name in (("coder1", "coder 1 (the extraction)"), ("coder2", "coder 2 (Opus 5.5)")):
        o.add(p, S, f"{p}{t}.against.{who}.coded", f"`against` links, {name}, as coded",
              against_text(ag[who]), src, {"links": len(ag[who]["links"]), "most": ag[who]["most"],
                                           "two_or_more": ag[who]["two_or_more"]})
        o.add(p, S, f"{p}{t}.against.{who}.check",
              f"`against` links, {name}, with the flagged links as `illustrates`",
              against_text(chk[who]["summary"]) + f" (flagged: {len(chk[who]['flagged'])}; answered 4a: "
              f"{chk[who]['answered_4a']})", src,
              {"links": len(chk[who]["summary"]["links"]), "most": chk[who]["summary"]["most"],
               "flagged": len(chk[who]["flagged"])})
    au = res["audit"]
    for who, name in (("coder1", "coder 1"), ("coder2", "coder 2")):
        o.add(p, S, f"{p}{t}.audit.{who}.coded", f"The audit under {name}, as coded", audit_text(au[who]), src,
              {k: au[who][k] for k in ("coverage", "assessed", "directional")} | {"seams": len(au[who]["seams"])})
        o.add(p, S, f"{p}{t}.audit.{who}.check", f"The audit under {name}, with the flagged links as `illustrates`",
              audit_text(au["check"][who]), src,
              {k: au["check"][who][k] for k in ("coverage", "assessed", "directional")}
              | {"seams": len(au["check"][who]["seams"])})
    x = au["coder1"]
    o.add(p, S, f"{p}{t}.audit.rule", "The audit's floor and rule",
          f"no rate is reported under coverage {dec(x['min_coverage'], 2)}; a claim is assessed with at least "
          f"{x['min_links']} `with` or `against` links from fragments not in the author's voice", src,
          {"min_coverage": x["min_coverage"], "min_links": x["min_links"]})


# ------------------------------------------------------------------ 4. the wager test (T29)

def boot_kappa(pairs, cats, seed=SEED, reps=RESAMPLES):
    """agreement.py's way: resamples of the rows with replacement, a resample
    with no kappa left out, the 2.5th and 97.5th percentiles as it takes them."""
    import score_markers as sm
    rng = random.Random(seed)
    n = len(pairs)
    ks = []
    for _ in range(reps):
        s = [pairs[rng.randrange(n)] for _ in range(n)]
        ca = collections.Counter(a for a, _ in s)
        cb = collections.Counter(b for _, b in s)
        pe = sum(ca[c] * cb[c] for c in cats) / (n * n)
        if pe >= 1:
            continue
        ks.append(sm.kappa(s, cats)[1])
    if not ks:
        return None, None, 0
    ks.sort()
    return ks[int(0.025 * len(ks))], ks[int(0.975 * len(ks)) - 1], len(ks)


def marker_pairs(paper):
    import score_markers as sm
    key = read_json(sm.KEY)
    units = [u["unit"] for e in key["papers"][paper] for u in e["units"]]
    codes = {}
    for m, (fname, _) in sm.MARKERS[paper].items():
        note_read(os.path.join(sm.REPLIES, fname))
        obj, _ = sm.load(rel(os.path.join(sm.REPLIES, fname)))
        codes[m] = {c["unit"]: c["code"] for c in obj["codes"]}
    return [(codes["opus"][u], codes["astra"][u]) for u in units]


def results_section(text, head):
    """The part of a markdown results file under '## head', up to the next '## '."""
    m = re.search(rf"^## {re.escape(head)}\n(.*?)(?=^## |\Z)", text, flags=re.M | re.S)
    if not m:
        raise Refused(f"no section '## {head}' in the results file")
    return m.group(1)


def table_row(part, label, what):
    return [c.strip() for c in once(rf"^\| {re.escape(label)} \|(.*)\|$", part, what).split("|")]


def section_wager(o, p):
    import score_markers as sm
    S = "4. The wager test (T29)"
    short = SHORT[p]
    word = {"bechky_2020": "Bechky", "pratt_2000": "Pratt"}[p]
    # the attack
    at_name = "stage2/attack_results.md"
    at = read_text(at_name)
    rows = re.findall(r"^\| (\d+) \| (Pratt|Bechky) \| ([^|]+) \| (\w+) \| ([^|]+) \| ([^|]+) \|$", at, flags=re.M)
    cards = [r for r in rows if r[1] == word and "calibration" not in r[2]]
    calib = [r for r in rows if r[1] == word and "calibration" in r[2]]
    killed = [r for r in cards if r[3] == "killed"]
    under_b = [r for r in killed if r[4].strip().startswith("**killed**")]
    survived = sum(1 for r in cards if r[3] == "survived_attack")
    same(len(killed) + survived, len(cards), f"{p}: every card killed or survived")
    o.add(p, S, f"{p}.wager.attack", "The system's readings (cards) and the attack (GPT 6 Astra)",
          f"{len(cards)} cards: {len(killed)} killed ({len(under_b)} of them under B, import), {survived} survived",
          f"`{at_name}`", {"cards": len(cards), "killed": len(killed), "killed_under_B": len(under_b),
                           "survived": survived})
    if calib:
        o.add(p, S, f"{p}.wager.calibration", "The attack's calibration: two copies of one card, each broken on purpose",
              f"{len(calib)} copies: " + "; ".join(f"chat {r[0]} {r[3]}" for r in calib), f"`{at_name}`",
              {"copies": len(calib), "killed": sum(1 for r in calib if r[3] == "killed")})
    # the markers
    rs_name = "stage2/marker_results/RESULTS.md"
    part = results_section(read_text(rs_name), word)
    n, agree, obs, k7, obs4, k4 = once(
        r"^(\d+) sentences\. Seven codes: the markers agree on (\d+) \(([\d.]+)\); Cohen's kappa \*\*([\d.]+)\*\*\. "
        r"Four groups \(N; R, RI, RA; P; U, C\), a diagnostic only: agreement ([\d.]+), kappa ([\d.]+)\.$",
        part, f"{p}: the markers' agreement")
    pairs = marker_pairs(short)
    po, kk = sm.kappa(pairs, sm.CODES)
    same(len(pairs), int(n), f"{p}: marked sentences")
    same(sum(a == b for a, b in pairs), int(agree), f"{p}: sentences the markers agree on")
    same(kk, float(k7), f"{p}: the markers' kappa", 3)
    lo, hi, n_ok = boot_kappa(pairs, sm.CODES)
    below = kk < sm.GATE
    o.add(p, S, f"{p}.wager.markers", "The markers (Opus 5.5 and GPT 6 Astra), seven codes"
          + (": below the bar of 0.60, reported by a decision of 11 Oct, made after the result" if below else ""),
          f"{agree} of {n} sentences agree ({obs}); " + k_iv(kk, lo, hi, n_ok)
          + "; the interval is new", f"`{rs_name}`; the interval from the two replies and the key (new)",
          {"n": int(n), "agree": int(agree), "kappa": kk, "interval": [lo, hi], "resamples": n_ok, "below_bar": below},
          new=True)
    o.add(p, S, f"{p}.wager.markers4", "The markers, four groups (a diagnostic only)"
          + (": below the bar" if below else ""),
          f"agreement {obs4}, kappa {k4}", f"`{rs_name}`", {"observed": float(obs4), "kappa": float(k4)})
    for label, fid in (("resolution rate (R, RI, RA)", "resolution"), ("strict rate (R)", "strict"),
                       ("sentences that report (not N)", "reporting")):
        cells = table_row(part, label, f"{p}: the rates' row {label}")
        o.add(p, S, f"{p}.wager.rates.{fid}",
              f"By arm, Opus 5.5 / GPT 6 Astra: {label}"
              + (" (below the bar; reported by a decision made after the result)" if below else ""),
              "system " + cells[0] + "; middle " + cells[1] + "; plain " + cells[2],
              f"`{rs_name}`", {"system": cells[0], "middle": cells[1], "plain": cells[2]})
    # worth
    wj_name, wr_name = "stage2/worth/worth_joined.json", "stage2/worth/WORTH_RESULTS.md"
    readings = [r for r in read_json(wj_name)["readings"] if r["paper"] == short]
    wpart = results_section(read_text(wr_name), "1. Worth by arm")
    wsub = re.search(rf"^### {word}\n(.*?)(?=^### |\Z)", wpart, flags=re.M | re.S).group(1)
    for arm_i, arm in enumerate(("system", "middle", "plain")):
        rr = [r for r in readings if r["arm"] == arm and r["worth"] is not None]
        mean = sum(r["worth"] for r in rr) / len(rr)
        early = [r["worth"] for r in rr if not r["late"]]
        mean_early = sum(early) / len(early)
        two = sum(1 for r in rr if r["worth"] >= 2)
        same(f"{mean:.2f}", table_row(wsub, "mean worth", "mean worth")[arm_i], f"{p}: worth, {arm}")
        same(f"{mean_early:.2f}", table_row(wsub, "mean worth without the readings rated late", "mean early")[arm_i],
             f"{p}: worth without the late, {arm}")
        same(f"{two} of {len(rr)}", table_row(wsub, "rated 2 or more", "rated 2+")[arm_i], f"{p}: rated 2+, {arm}")
        late = len(rr) - len(early)
        o.add(p, S, f"{p}.wager.worth.{arm}", f"The PI's worth, {arm} arm (0 to 3; declared not blind)",
              f"mean {mean:.2f} over {len(rr)} readings; rated 2 or more: {two} of {len(rr)}"
              + (f"; without the {late} rated late, mean {mean_early:.2f}" if late else ""),
              f"`{wj_name}`, checked against `{wr_name}`",
              {"n": len(rr), "mean": mean, "mean_without_late": mean_early, "two_or_more": two, "late": late})
    gpart = re.search(r"^### The gap in mean worth between arms\n(.*?)(?=^### |\Z)",
                      read_text(wr_name), flags=re.M | re.S).group(1)
    col = {"pratt_2000": 0, "bechky_2020": 1}[p]
    for fid, label in (("system_middle", "system against middle (the reading chats)"),
                       ("system_plain", "system against plain (the plain chats)"),
                       ("middle_plain", "middle (the reading chats) against plain (the plain chats)")):
        cells = table_row(gpart, label, f"gap {label}")
        late_in = "plain" in fid and any(r["late"] for r in readings if r["arm"] == "plain")
        o.add(p, S, f"{p}.wager.gap.{fid}",
              f"Gap in the PI's mean worth (declared not blind), {label} (p by relabelling)"
              + ("; the plain arm's mean includes the readings the PI rated late" if late_in else ""),
              cells[col], f"`{wr_name}`", cells[col])


# ------------------------------------------------------------------ 5. tests added after the plan

def judge_counts(rows):
    by = collections.defaultdict(dict)
    for r in rows:
        if r["who"] in ("coder 1", "coder 2") and r["differ"]:
            by[(r["field"], tuple(r["key"]))][r["who"]] = r["answer"] == "yes"
    sorted_as = collections.Counter()
    for k, v in by.items():
        if set(v) != {"coder 1", "coder 2"}:
            raise Refused(f"the judges: a differing row without both codings' statements: {k}")
        sorted_as[{(True, True): "both held", (True, False): "only coder 1's held",
                   (False, True): "only coder 2's held", (False, False): "neither held"}[(v["coder 1"], v["coder 2"])]] += 1
    planted = {w: (sum(1 for r in rows if r["who"] == w and r["answer"] == "yes"),
                   sum(1 for r in rows if r["who"] == w)) for w in ("both", "neither")}
    return len(by), sorted_as, planted


def section_t31(o, p):
    S = "5.1 Added after the plan: T31, the judges (Gemini 3.1 Pro)"
    jr = read_json("judge_results.json")["results"][p]
    rows = jr["1"] + jr["2"]
    n, srt, planted = judge_counts(rows)
    md = read_text("JUDGE_RESULTS.md")
    want = collections.Counter()
    total = 0
    for part in ("1", "2"):
        sec = re.search(rf"^## {p}, part {part}\n(.*?)(?=^## |\Z)", md, flags=re.M | re.S).group(1)
        line = once(r"^\*\*Rows where the codings differ: (\d+)\.\*\* (.*)$", sec, f"{p} part {part}: rows that differ")
        total += int(line[0])
        for k, v in re.findall(r"(both held|only coder 1's held|only coder 2's held|neither held): (\d+)", line[1]):
            want[k] += int(v)
    same(n, total, f"{p}: the judges' differing rows")
    same(dict(srt), dict(want), f"{p}: the judges' sorting")
    o.add(p, S, f"{p}.t31.differ", "Rows where the two codings differ, as the judge sorted them",
          f"{n} rows: " + "; ".join(f"{k} {srt[k]}" for k in ("both held", "only coder 1's held",
                                                             "only coder 2's held", "neither held")),
          "`judge_results.json`, checked against `JUDGE_RESULTS.md`", dict(srt) | {"rows": n})
    o.add(p, S, f"{p}.t31.planted", "How far the judge can be trusted: statements both codings made, and none made, held",
          f"both made: {planted['both'][0]} of {planted['both'][1]} held; neither made: "
          f"{planted['neither'][0]} of {planted['neither'][1]} held", "`judge_results.json`",
          {w: list(v) for w, v in planted.items()})
    return planted


def section_t32(o, p):
    import score_markers as sm
    S = "5.2 Added after the plan: T32, readings at places"
    key = read_json("places_packs_key.json")
    units = [u["unit"] for e in key["readings"] for u in e["units"]]
    codes = {}
    for m, fname in (("opus", "reply_47_mark_places_opus.json"), ("astra", "reply_48_mark_places_astra.json")):
        obj = json.loads(read_text(fname).strip())
        codes[m] = {c["unit"]: c["code"] for c in obj["codes"]}
    pairs = [(codes["opus"][u], codes["astra"][u]) for u in units]
    po, kk = sm.kappa(pairs, sm.CODES)
    ag = read_json("places_marker_results.json")["agreement"]
    same(len(pairs), ag["sentences"], "T32: sentences")
    same(sum(a == b for a, b in pairs), ag["same"], "T32: the markers agree on")
    same(kk, ag["kappa7"], "T32: the markers' kappa", 9)
    lo, hi, n_ok = boot_kappa(pairs, sm.CODES)
    o.add(p, S, f"{p}.t32.markers", "Its markers (Opus 5.5 and GPT 6 Astra), seven codes",
          f"{ag['same']} of {ag['sentences']} sentences agree; " + k_iv(kk, lo, hi, n_ok) + "; the interval is new",
          "`places_marker_results.json`; the interval from the two replies and the key (new)",
          {"n": ag["sentences"], "agree": ag["same"], "kappa": kk, "interval": [lo, hi], "resamples": n_ok}, new=True)
    pr = read_text("PLACES_RESULTS.md")
    sec = results_section(pr, "By chat")
    for label in ("readings", "worth, mean", "worth 3, 2, 1, 0", "resolution"):
        cells = table_row(sec, label, f"T32 by chat: {label}")
        o.add(p, S, f"{p}.t32.{label.split(',')[0].replace(' ', '_')}",
              f"By chat: {label}" + (" (Opus 5.5 / GPT 6 Astra)" if label == "resolution" else ""),
              f"places given (chat 45): {cells[0]}; places found (chat 46): {cells[1]}", "`PLACES_RESULTS.md`",
              cells[:2])


def section_t33(o, p):
    import score_matching as smx
    S = "5.3 Added after the plan: T33, the matching test"
    mr = read_json("matching_results.json")
    f, b = mr["figures"], mr["bootstrap"]
    G = mr["groupings"]
    ids = sorted(next(iter(G.values())).keys())
    full = smx.figures(G, list(itertools.combinations(ids, 2)))
    for k in ("A", "B", "Bj", "P_A", "P_B", "P_Bj"):
        same(full[k], f[k], f"T33: {k}", 9)
    c1 = [mr["claims"]["b1"][i] for i in ids]
    c2 = [mr["claims"]["b2"][i] for i in ids]
    same(smx.nominal_kappa(c1, c2), mr["claim_kappa"], "T33: the claim tags' kappa", 9)
    # new: intervals for the figures themselves, by resampling the readings as the scorer does
    rng = random.Random(SEED)
    vals = {k: [] for k in ("A", "B", "Bj", "P_A", "P_B", "P_Bj", "claims")}
    left = collections.Counter()
    n = len(ids)
    for _ in range(RESAMPLES):
        draw = [ids[rng.randrange(n)] for _ in range(n)]
        pairs = [(x, y) for x, y in itertools.combinations(draw, 2) if x != y]
        ff = smx.figures(G, pairs)
        for k in ("A", "B", "Bj", "P_A", "P_B", "P_Bj"):
            if ff[k] is None:
                left[k] += 1
            else:
                vals[k].append(ff[k])
        kc = smx.nominal_kappa([mr["claims"]["b1"][i] for i in draw], [mr["claims"]["b2"][i] for i in draw])
        if kc is None:
            left["claims"] += 1
        else:
            vals["claims"].append(kc)
    iv = {k: (smx.percentile(sorted(v), 0.025), smx.percentile(sorted(v), 0.975)) for k, v in vals.items()}
    names = {"A": "Arm A (the PDF only): the two coders' groupings, pair kappa",
             "B": "Arm B (the PDF and the reference): grouping by claim number, pair kappa",
             "Bj": "Arm B: grouping by judgment, pair kappa",
             "P_A": "Agreement with the PI's grouping, arm A (mean of the two coders)",
             "P_B": "Agreement with the PI's grouping, arm B by claim number",
             "P_Bj": "Agreement with the PI's grouping, arm B by judgment"}
    for k, label in names.items():
        o.add(p, S, f"{p}.t33.{k}", label,
              k_iv(f[k], iv[k][0], iv[k][1], RESAMPLES - left[k]) + "; the interval is new",
              "`matching_results.json`; the interval by resampling the readings (new)",
              {"kappa": f[k], "interval": list(iv[k]), "left_out": left[k]}, new=True)
    for d in ("B - A", "Bj - A", "P_B - P_A", "P_Bj - P_A"):
        x, y = d.split(" - ")
        o.add(p, S, f"{p}.t33.diff.{d.replace(' ', '')}", f"Difference {d}",
              f"{dec(f[x] - f[y], 3)} (95% interval {dec(b[d]['low'], 2)} to {dec(b[d]['high'], 2)})",
              "`matching_results.json`", {"diff": f[x] - f[y], "low": b[d]["low"], "high": b[d]["high"]})
    o.add(p, S, f"{p}.t33.claims", "Arm B's two coders' claim tags on the 28 readings",
          k_iv(mr["claim_kappa"], iv["claims"][0], iv["claims"][1], RESAMPLES - left["claims"])
          + "; the interval is new", "`matching_results.json`; the interval by resampling the readings (new)",
          {"kappa": mr["claim_kappa"], "interval": list(iv["claims"]), "left_out": left["claims"]}, new=True)
    s1, s2 = set(c1) - {"none"}, set(c2) - {"none"}
    o.add(p, S, f"{p}.t33.contested", "Claims the readings contest, by arm B's tags (of the paper's 23)",
          f"{len(s1 & s2)} under both coders' tags; {len(s1 | s2)} under either", "`matching_results.json`",
          {"both": len(s1 & s2), "either": len(s1 | s2)})
    q2 = mr["q2"]
    o.add(p, S, f"{p}.t33.recur", "Recurrence across vendors (Q2)",
          f"of the {q2['found_twice']} points two or more Fable chats reached, both GPT 6 Astra runs reached "
          f"{q2['found_twice_reached']}; {q2['new_with_earlier']} of the {q2['new_readings']} new readings joined "
          f"a group with an earlier one", "`matching_results.json`",
          {k: q2[k] for k in ("found_twice", "found_twice_reached", "new_with_earlier", "new_readings")})
    # the passages cited: totals from the results, distinct passages from the two replies
    vo = mr["voices"]
    rep = sum(v["reported"] for v in vo.values())
    tot = rep + sum(v["author_insight"] for v in vo.values())
    side = read_json("bechky_2020_v1_voice_gloss.json")
    vcode = {v["fragment_id"]: v["code"] for v in side["voice"]}
    cited = []
    for name in ("reply_53_match_b_opus.json", "reply_54_match_b_astra.json"):
        note_read(name)
        rep_obj, faults = smx.load_reply(rel(name))
        if faults:
            raise Refused(f"T33: {name}: {faults}")
        faults, got = smx.check_reply(rep_obj, ids, "B")
        if faults:
            raise Refused(f"T33: {name}: {faults}")
        cited += [q for i in ids for q in got["passages"][i]]
    same(len(cited), tot, "T33: passages cited")
    same(sum(1 for q in cited if vcode[q] == "reported"), rep, "T33: passages cited that are reported material")
    distinct = set(cited)
    o.add(p, S, f"{p}.t33.cited", "Arm B's citations of passages for the 28 readings, by the frozen record's voice "
          "(described, not tested)",
          f"{rep} of {tot} name reported material; {len(distinct)} distinct passages, "
          f"{sum(1 for q in distinct if vcode[q] == 'reported')} of them reported",
          "`matching_results.json`; distinct passages from `reply_53_match_b_opus.json` and "
          "`reply_54_match_b_astra.json`", {"reported": rep, "citations": tot, "distinct": len(distinct)})
    mw = read_text("MATCHING_WORTH.md")
    new_mean = once(r"^Mean ([\d.]+); rated 3: (\d+), 2: (\d+), 1: (\d+), 0: (\d+)\.$", mw, "T33 worth, new")
    old_mean = once(r"^The 18 earlier readings: mean ([\d.]+); rated 3: (\d+), 2: (\d+), 1: (\d+), 0: (\d+)\.$",
                    mw, "T33 worth, earlier")
    o.add(p, S, f"{p}.t33.worth", "The PI's worth (described, not tested: the PI knew their source, and rated after the "
          "results): the 10 new readings, and the 18 earlier ones",
          f"new: mean {new_mean[0]} (3: {new_mean[1]}, 2: {new_mean[2]}, 1: {new_mean[3]}, 0: {new_mean[4]}); "
          f"earlier: mean {old_mean[0]} (3: {old_mean[1]}, 2: {old_mean[2]}, 1: {old_mean[3]}, 0: {old_mean[4]})",
          "`MATCHING_WORTH.md`", {"new": list(new_mean), "earlier": list(old_mean)})


def section_t34(o, p):
    S = "5.4 Added after the plan: T34, the author's own worth"
    key = {"bechky_2020": "author_ratings_key.json", "pratt_2000": "author_ratings_key_pratt.json"}[p]
    note_read(key)
    answers = [f for f in sorted(os.listdir(HERE)) if f.startswith("author_answers_") and SHORT[p] in f]
    o.add(p, S, f"{p}.t34", "The author's ratings of the wager test's readings of the paper",
          "no reply in" if not answers else f"answers on file: {', '.join(answers)}; not scored by this script",
          f"`{key}`; the folder", {"answers": answers})


def section_t35(o, p):
    S = "5.5 Added after the plan: T35, the second extraction"
    r = read_json("second_extraction_results.json")
    src = "`second_extraction_results.json`"
    fc, cnt = r["found"]["claims"], r["counts"]
    for side, label in (("first", "the first return's"), ("new", "the new return's")):
        x = fc[side]
        o.add(p, S, f"{p}.t35.claims.{side}", f"Q1: {label} {x['n']} claims found in the other return",
              f"{x['found']['a']} by chat 56 (Opus 5.5), {x['found']['b']} by chat 57 (GPT 6 Astra), "
              f"{x['found']['both']} by both", src, x["found"] | {"n": x["n"]})
    for side, label in (("first_core", "the first return's"), ("new_core", "the new return's")):
        x = fc[side]
        o.add(p, S, f"{p}.t35.claims.{side}", f"Q1: {label} {x['n']} core claims found in the other return",
              f"{x['found']['a']} by chat 56, {x['found']['b']} by chat 57, {x['found']['both']} by both",
              src, x["found"] | {"n": x["n"]})
    iv = r["intervals"]["claims_pairs"]
    o.add(p, S, f"{p}.t35.claims.kappa", "Q1: the two matchers' agreement on claim pairs (the bar: 0.60)",
          k_iv(r["kappas"]["claims_pairs"], iv["low"], iv["high"], iv["resamples"] - iv["left_out"])
          + f"; {r['pairs']['a']['claims']} pairs by chat 56, {r['pairs']['b']['claims']} by chat 57", src,
          {"kappa": r["kappas"]["claims_pairs"], "interval": [iv["low"], iv["high"]]})
    for key_, label in (("passages_out", "outside the tables"), ("passages_all", "with the table cells")):
        for side in ("first", "new"):
            x = r["found"][key_][side]
            o.add(p, S, f"{p}.t35.{key_}.{side}", f"Q2: passages {label}, the {side} return's found in the other",
                  f"{x['found']['both']} of {x['n']} ({dec(x['both'], 2)}) by both matchers"
                  + ("" if x["found"]["a"] == x["found"]["b"] else
                     f"; {x['found']['a']} by chat 56, {x['found']['b']} by chat 57"), src, x["found"] | {"n": x["n"]})
    o.add(p, S, f"{p}.t35.passages.kappa", "Q2: the matchers' agreement on passage pairs",
          f"kappa {dec(r['kappas']['passages_out_pairs'], 3)}: the two passage maps are identical, so this says "
          "nothing of the matchers' judgement", src, r["kappas"]["passages_out_pairs"])
    v = r["voice"]
    vi = r["intervals"]["voice"]
    o.add(p, S, f"{p}.t35.voice", "Q3: voice on the matched passages, first return against new (the bar: 0.80)",
          f"{v['agree']} of {v['pairs_both_name']} alike; "
          + k_iv(v["kappa"], vi["low"], vi["high"], vi["resamples"] - vi["left_out"])
          + f"; beside {dec(v['two_codings_of_the_first_extraction']['kappa'], 3)} for two codings of one extraction",
          src, {"agree": v["agree"], "n": v["pairs_both_name"], "kappa": v["kappa"], "interval": [vi["low"], vi["high"]]})
    t = v["table"]
    o.add(p, S, f"{p}.t35.voice.table", "Q3: voice on the matched passages, first / new",
          "; ".join(f"{k}: {t[k]}" for k in sorted(t)), src, t)
    for side in ("first author_insight", "first reported"):
        x = r["found"]["passages_by_voice"][side]
        o.add(p, S, f"{p}.t35.byvoice.{side.split()[1]}", f"The first return's passages coded `{side.split()[1]}`, "
              "found again", f"{x['found']['both']} of {x['n']}", src, x["found"] | {"n": x["n"]})
    o.add(p, S, f"{p}.t35.counts", "The two returns: claims, core claims, passages, voice",
          f"first: {cnt['first']['claims']} claims ({cnt['first']['core']} core), {cnt['first']['passages']} passages, "
          + ", ".join(f"{cnt['first']['voice'][k]} {k}" for k in sorted(cnt["first"]["voice"]))
          + f"; new: {cnt['new']['claims']} claims ({cnt['new']['core']} core), {cnt['new']['passages']} passages, "
          + ", ".join(f"{cnt['new']['voice'][k]} {k}" for k in sorted(cnt["new"]["voice"])), src,
          {"first": {k: cnt["first"][k] for k in ("claims", "core", "passages")},
           "new": {k: cnt["new"][k] for k in ("claims", "core", "passages")}})
    ans = r["answers"]
    o.add(p, S, f"{p}.t35.answers", "The plan's answers, as the scorer gives them",
          f"Q1, the claims: {ans['Q1']['answer']}; Q2, the passages: {ans['Q2']['answer']} (with the table cells: "
          f"{ans['Q2_with_tables']['answer']}); Q3, voice: {ans['Q3']['answer']} ({ans['Q3']['why']})", src,
          {k: ans[k]["answer"] for k in ("Q1", "Q2", "Q2_with_tables", "Q3")})
    # new: in each return, its `with` links that rest on a passage it codes `author_insight`, by its own voice codes
    for side, cname, vname in (("first", "bechky_2020_corpus.json", "bechky_2020_voice_gloss.json"),
                               ("new", "bechky_2020_x2_corpus.json", "bechky_2020_x2_voice_gloss.json")):
        c, vv = read_json(cname), read_json(vname)
        vc = {e["fragment_id"]: e["code"] for e in vv["voice"]}
        w = [l for l in c["claim_links"] if l["direction"] == "with"]
        ai = sum(1 for l in w if vc[l["fragment_id"]] == "author_insight")
        o.add(p, S, f"{p}.t35.with_on_author.{side}", f"The {side} return: its `with` links, and how many rest on a "
              "passage it codes `author_insight` (new)", f"{ai} of {len(w)}", f"`{cname}`, `{vname}` (new)",
              {"author_insight": ai, "with": len(w)}, new=True)


# ------------------------------------------------------------------ across the two papers

def section_across(o, res, planted):
    S = "The counts the pinned predictions are read on (their words are in no file)"
    for p in PAPERS:
        first = read_json(f"{p}_corpus.json")
        fv = read_json(f"{p}_voice_gloss.json")
        reported = sum(1 for v in fv["voice"] if v["code"] == "reported")
        ventured = [c["claim_id"] for c in first["claims"] if c.get("stated_as") == "ventured"]
        linked = {l["claim_id"] for l in first["claim_links"]}
        vl = [c for c in ventured if c in linked]
        a = res[p]["A"]["fig"]
        ag = res[p]["against"]
        log = f"`{UPPER[p]}_AGREEMENT_LOG.md` (agreement.py's record)"
        first_src = f"`{p}_corpus.json`"
        o.add("across", S, f"pred.{p}.P1", f"P1, {NAME[p]}: Stage A, whether a claim names an outcome",
              f"{a['agree']} of {a['n']}; " + (k_iv(a["kappa"], *a["interval"], a["resamples"])
                                              if a["kappa"] is not None and a["interval"] else
                                              f"kappa {a['kappa_note']}"), log, fig_raw(a))
        o.add("across", S, f"pred.{p}.P2", f"P2, {NAME[p]}: the most `against` links on any one claim, coder 1 / "
              "coder 2, as coded and with the flagged links as `illustrates`",
              f"as coded {ag['coder1']['most']} / {ag['coder2']['most']}; with the flags "
              f"{ag['check']['coder1']['summary']['most']} / {ag['check']['coder2']['summary']['most']}", log,
              {"coded": [ag["coder1"]["most"], ag["coder2"]["most"]],
               "check": [ag["check"]["coder1"]["summary"]["most"], ag["check"]["coder2"]["summary"]["most"]]})
        o.add("across", S, f"pred.{p}.P3", f"P3 and P5, {NAME[p]}: first return's fragments coded `reported` "
              "(all fragments)", f"{reported} ({len(first['fragments'])})", f"{first_src}, `{p}_voice_gloss.json`",
              {"reported": reported, "fragments": len(first["fragments"])})
        o.add("across", S, f"pred.{p}.P4", f"P4, {NAME[p]}: first return's ventured claims with a linked fragment",
              f"{len(vl)} of {len(ventured)} ({dec(len(vl) / len(ventured), 2)})", first_src,
              {"ventured": len(ventured), "linked": len(vl)})
        o.add("across", S, f"pred.{p}.P5", f"P5, {NAME[p]}: first return's claims", f"{len(first['claims'])}",
              first_src, len(first["claims"]))
    S = "T31 over both papers"
    both = [sum(planted[p]["both"][i] for p in PAPERS) for i in (0, 1)]
    neither = [sum(planted[p]["neither"][i] for p in PAPERS) for i in (0, 1)]
    o.add("across", S, "t31.planted", "Statements both codings made, held; statements neither made, held",
          f"both made: {both[0]} of {both[1]}; neither made: {neither[0]} of {neither[1]}", "`judge_results.json`",
          {"both": both, "neither": neither})
    S = "T29 over both papers"
    wj = read_json("stage2/worth/worth_joined.json")["readings"]
    wr = read_text("stage2/worth/WORTH_RESULTS.md")
    wsub = re.search(r"^### Both papers\n(.*?)(?=^### |^## |\Z)", results_section(wr, "1. Worth by arm"),
                     flags=re.M | re.S).group(1)
    for arm_i, arm in enumerate(("system", "middle", "plain")):
        rr = [r for r in wj if r["arm"] == arm and r["worth"] is not None]
        mean = sum(r["worth"] for r in rr) / len(rr)
        early = [r["worth"] for r in rr if not r["late"]]
        two = sum(1 for r in rr if r["worth"] >= 2)
        same(f"{mean:.2f}", table_row(wsub, "mean worth", "both: mean")[arm_i], f"both papers: worth, {arm}")
        same(f"{sum(early) / len(early):.2f}",
             table_row(wsub, "mean worth without the readings rated late", "both: early")[arm_i],
             f"both papers: worth without the late, {arm}")
        same(f"{two} of {len(rr)}", table_row(wsub, "rated 2 or more", "both: 2+")[arm_i], f"both papers: 2+, {arm}")
        late = len(rr) - len(early)
        o.add("across", S, f"t29.worth.{arm}", f"The PI's worth over both papers, {arm} arm (declared not blind)",
              f"mean {mean:.2f} over {len(rr)} readings; rated 2 or more: {two} of {len(rr)}"
              + (f"; without the {late} rated late, mean {sum(early) / len(early):.2f}" if late else ""),
              "`stage2/worth/worth_joined.json`, checked against `stage2/worth/WORTH_RESULTS.md`",
              {"n": len(rr), "mean": mean, "two_or_more": two, "late": late})
    gpart = re.search(r"^### The gap in mean worth between arms\n(.*?)(?=^### |\Z)", wr, flags=re.M | re.S).group(1)
    for fid, label in (("system_middle", "system against middle (the reading chats)"),
                       ("system_plain", "system against plain (the plain chats)"),
                       ("middle_plain", "middle (the reading chats) against plain (the plain chats)")):
        cells = table_row(gpart, label, f"gap {label}")
        o.add("across", S, f"t29.gap.{fid}", f"Gap in the PI's mean worth (declared not blind) over both papers, "
              f"{label} (p by relabelling within each paper)"
              + ("; the plain arm's mean includes the readings the PI rated late" if "plain" in fid else ""),
              cells[2], "`stage2/worth/WORTH_RESULTS.md`", cells[2])
    for status in ("killed", "survived"):
        rr = [r for r in wj if r["attack"] == status]
        mean = sum(r["worth"] for r in rr) / len(rr)
        line = once(rf"^- {status}: (\d+) readings, mean worth ([\d.]+);", wr, f"attack and worth, {status}")
        same((len(rr), f"{mean:.2f}"), (int(line[0]), line[1]), f"attack and worth, {status}")
        o.add("across", S, f"t29.attack_worth.{status}", f"The system's readings the attack {status}: the PI's worth "
              "(declared not blind)",
              f"{len(rr)} readings, mean worth {mean:.2f}", "`stage2/worth/worth_joined.json`, checked against "
              "`stage2/worth/WORTH_RESULTS.md`", {"n": len(rr), "mean": mean})


def section_hours(o):
    h = read_json("chats_models_hours.json")
    chats = h["chats"]
    S = "Models and times by step, from the list below"
    order = []
    for c in chats:
        if c["test"] not in order:
            order.append(c["test"])
    for test in order:
        cc = [c for c in chats if c["test"] == test]
        models = collections.Counter(c["model"] for c in cc)
        dates = sorted({c["date"] for c in cc if c["date"]})
        timed = [c for c in cc if c["duration_min"] is not None]
        told = [c for c in cc if c["duration_min"] is None and c["duration_as_recorded"]]
        papers = sorted({NAME[c["paper"]] for c in cc if c["paper"] in NAME})
        when = (f"start and end on record for {len(timed)}: " + ", ".join(f"{c['duration_min']}" for c in timed)
                + f" min ({sum(c['duration_min'] for c in timed)} min in all)") if timed else "no start and end on record"
        if told:
            when += f"; a length as recorded for {len(told)}" + (" more" if timed else "")
        o.add("across", S, f"hours.step.{test}", test + (f" ({', '.join(papers)})" if papers else ""),
              f"{len(cc)} chat(s); " + "; ".join(f"{m} ({k})" for m, k in models.items()) + "; "
              + (", ".join(dates) or "date not on record") + "; " + when, "`chats_models_hours.json`",
              {"chats": len(cc), "models": dict(models), "timed_min": [c["duration_min"] for c in timed],
               "told": len(told)})
    S = "Models, settings and times of every chat, as recorded"
    at = read_text("stage2/attack_results.md")
    attack = {int(m[0]): (m[1], m[2].strip()) for m in
              re.findall(r"^\| (\d+) \| (Pratt|Bechky) \| ([^|]+) \|", at, flags=re.M)}
    word_to_paper = {"Pratt": "pratt_2000", "Bechky": "bechky_2020"}
    for c in chats:
        extra = ""
        if c["test"] == "T29 attack" and c["chat_number"] in attack:
            word, move = attack[c["chat_number"]]
            if c["paper"] is None:
                extra += f", {NAME[word_to_paper[word]]} (by `stage2/attack_results.md`)"
            elif c["paper"] != word_to_paper[word]:
                raise Refused(f"chat {c['chat_number']}: the hours file and the attack's results name different papers")
            if "calibration" in move:
                extra += f"; {move}"
        when = c["date"] or "date not on record"
        if c["start"] or c["end"]:
            when += f", {c['start'] or '?'} to {c['end'] or '?'}"
        if c["duration_min"] is not None:
            when += f" ({c['duration_min']} min)"
        if c["duration_as_recorded"]:
            when += f"; {c['duration_as_recorded']}"
        label = (f"chat {c['chat_number']}: " if c["chat_number"] else "") + c["test"] + (
            f", {NAME[c['paper']]}" if c["paper"] in NAME else "") + extra
        o.add("across", S, f"hours.{c['id']}", label, f"{c['model']}, {c['setting']}; {when}",
              "`chats_models_hours.json`", {k: c[k] for k in ("date", "start", "end", "duration_min")})
    S = "The PI's own time, as recorded"
    for c in h["people"]:
        when = c["date"] + (f", from {c['start']}" if c["start"] else "") + (f" to {c['end']}" if c["end"] else "")
        o.add("across", S, f"hours.{c['id']}", c["test"] + (f", {NAME[c['paper']]}" if c["paper"] in NAME else ""),
              (c["duration_as_recorded"] or "length not on record") + f" ({when})",
              "`chats_models_hours.json`", {k: c[k] for k in ("date", "start", "end", "duration_min")})


# ------------------------------------------------------------------ writing

HEAD = {
    "bechky_2020": "Bechky 2020",
    "pratt_2000": "Pratt 2000",
    "across": "across the two papers",
}


def md(o, which):
    extra = ([] if which != "across" else
             ["The link tests (on Pratt, 29 Sep to 6 Oct) are not in these tables: their figures stand in "
              "`LINK_TEST_RESULT.md` and `LINK_TEST2_RESULT.md`, run B and run C included, each checked "
              "independently when it was written.", ""])
    L = [f"{TITLE}: {HEAD[which]}", "",
         "Written by `build_figures.py` from the results files that each row names. Nothing in it is typed, "
         "and nothing here changes a figure of any results file. Every kappa of the cold papers' codings is "
         "model against model: coder 1 is the extraction (ChatGPT), coder 2 is Opus 5.5. Rows marked *new* "
         "hold figures that no results file held before (see the script's docstring).", ""] + extra
    sec = None
    for paper, section, label, value, source, new in o.rows:
        if paper != which:
            continue
        if section != sec:
            if sec is not None:
                L.append("")
            L += [f"## {section}", "", "| figure | value | source |", "|---|---|---|"]
            sec = section
        cell = lambda s: " ".join(str(s).split()).replace("|", "\\|")
        L.append(f"| {cell(label)}{' *new*' if new else ''} | {cell(value)} | {cell(source)} |")
    return "\n".join(L) + "\n"


def build(out_dir):
    if not os.path.isdir(out_dir):
        raise Refused(f"no such folder: {out_dir}")
    for f in OUTPUTS:
        q = os.path.join(out_dir, f)
        if os.path.exists(q):
            head = open(q, encoding="utf-8", errors="replace").read(200)
            if not (head.startswith(TITLE) or (f.endswith(".json") and '"written_by": "build_figures.py"' in head)):
                raise Refused(f"{q} exists and is not a file this script wrote")
    o = Out()
    res, planted = {}, {}
    for p in PAPERS:
        section_record(o, p)
        res[p] = agreement_res(p)
        section_agreement(o, p, res[p], None, f"`{UPPER[p]}_AGREEMENT_LOG.md` (agreement.py's record)")
        if p == "pratt_2000":
            sc = second_count_res()
            section_agreement(o, p, sc, ".second", "`PRATT_SECOND_COUNT_LOG.md` (second_count.py's record)")
        section_against(o, p, res[p], None, f"`{UPPER[p]}_AGREEMENT_LOG.md` (agreement.py's record)")
        if p == "pratt_2000":
            section_against(o, p, sc, ".second", "`PRATT_SECOND_COUNT_LOG.md` (second_count.py's record)")
        section_wager(o, p)
        planted[p] = section_t31(o, p)
        if p == "bechky_2020":
            section_t32(o, p)
            section_t33(o, p)
        section_t34(o, p)
        if p == "bechky_2020":
            section_t35(o, p)
    section_across(o, res, planted)
    section_hours(o)
    texts = {f"FIGURES_{p}.md": md(o, p) for p in PAPERS}
    texts["FIGURES_across.md"] = md(o, "across")
    texts["figures.json"] = json.dumps({"written_by": "build_figures.py", "seed": SEED, "resamples": RESAMPLES,
                                        "script_sha256": sha_of(os.path.basename(__file__)),
                                        "read": dict(sorted(READ.items())), "figures": o.records},
                                       indent=1, ensure_ascii=False, default=list) + "\n"
    for f, t in texts.items():
        with open(os.path.join(out_dir, f), "w", encoding="utf-8") as fh:
            fh.write(t)
    return o


# ------------------------------------------------------------------ self-test

def selftest():
    fails = []

    def check(cond, what):
        if not cond:
            fails.append(what)

    # once(): exactly one match
    check(once(r"^a (\d)$", "a 1\nb 2", "t") == "1", "once finds its one match")
    try:
        once(r"^a (\d)$", "a 1\na 2", "t")
        fails.append("once refuses two matches")
    except Refused:
        pass
    # same(): rounding
    same(0.12345, 0.1234, "t", 3)
    try:
        same(0.1236, 0.1234, "t", 3)
        fails.append("same refuses a difference at the third place")
    except Refused:
        pass
    # boot_kappa on made-up pairs: perfect agreement gives 1 at both ends; a constant column has no kappa
    pairs = [("N", "N"), ("R", "R"), ("P", "P"), ("C", "C")] * 10
    lo, hi, ok = boot_kappa(pairs, ["N", "R", "RI", "RA", "P", "U", "C"])
    check(abs(lo - 1) < 1e-12 and abs(hi - 1) < 1e-12 and ok == RESAMPLES, "perfect agreement")
    lo, hi, ok = boot_kappa([("N", "N")] * 30, ["N", "R"])
    check(lo is None and hi is None and ok == 0, "constant pairs give no interval")
    check(k_iv(0.5, None, None).endswith("(no interval: no resample gave a kappa)"), "k_iv without interval")
    check(k_iv(0.5, 0.25, 0.75, 1990) == "kappa 0.500 (95% interval 0.25 to 0.75; 1,990 of 2,000 resamples "
          "gave a kappa)", "k_iv with some resamples left out")
    # diff_records on made-up corpora
    a = {"meta": {"x": 1}, "fragments": [{"fragment_id": "F1", "stub": "a"}], "claims": [{"claim_id": "C1"}],
         "claim_links": [{"fragment_id": "F1", "claim_id": "C1", "direction": "with"}]}
    b = json.loads(json.dumps(a))
    b["fragments"].append({"fragment_id": "F2", "stub": "b"})
    b["fragments"][0]["stub"] = "c"
    b["claim_links"].append({"fragment_id": "F2", "claim_id": "C1", "direction": "illustrates"})
    d = diff_records(a, b)
    check(d["fragments"]["added"] == ["F2"] and d["fragments"]["changed"] == {"F1": ["stub"]}
          and len(d["claim_links"]["added"]) == 1 and d["meta"] == [], "diff_records")
    b["fragments"][0]["citing_claims"] = ["C1"]
    b["meta"]["x"] = 2
    a["fragments"].append({"fragment_id": "F10", "citing_claims": []})
    b["fragments"].append({"fragment_id": "F10", "citing_claims": ["C1"]})
    d = diff_records(a, b)
    check(changed_text(d) == "F1 (citing_claims, stub); 1 fragment(s) in their list of citing claims only; "
          "in the head: x", "changed_text")
    check(sorted(["F10", "F9", "F100"], key=natural) == ["F9", "F10", "F100"], "natural order")
    # judge_counts on made-up rows
    rows = [{"who": "coder 1", "differ": True, "field": "core", "key": ["C1"], "answer": "yes"},
            {"who": "coder 2", "differ": True, "field": "core", "key": ["C1"], "answer": "no"},
            {"who": "coder 1", "differ": True, "field": "core", "key": ["C2"], "answer": "no"},
            {"who": "coder 2", "differ": True, "field": "core", "key": ["C2"], "answer": "no"},
            {"who": "both", "differ": False, "field": "core", "key": ["C3"], "answer": "yes"},
            {"who": "neither", "differ": False, "field": "core", "key": ["C4"], "answer": "no"}]
    n, srt, planted = judge_counts(rows)
    check(n == 2 and srt == {"only coder 1's held": 1, "neither held": 1}
          and planted == {"both": (1, 1), "neither": (0, 1)}, "judge_counts")
    # md(): one table per section, bars escaped
    o = Out()
    o.add("x", "S1", "a", "l|1", "v", "s")
    o.add("x", "S2", "b", "l2", "v2", "s2", new=True)
    HEAD["x"] = "test"
    t = md(o, "x")
    check(t.count("## S") == 2 and "l\\|1" in t and "*new*" in t, "md")
    del HEAD["x"]
    print("selftest:", "all passed" if not fails else "FAILED: " + "; ".join(fails))
    return 0 if not fails else 1


def main(argv):
    if argv[:1] == ["selftest"]:
        return selftest()
    if argv[:1] == ["build"] and len(argv) == 2 and argv[1].startswith("--out="):
        try:
            o = build(argv[1].split("=", 1)[1])
        except Refused as e:
            print(f"REFUSED: {e}")
            return 1
        print(f"wrote {len(OUTPUTS)} files: {sum(1 for r in o.rows if r[0] == 'bechky_2020')} rows for Bechky, "
              f"{sum(1 for r in o.rows if r[0] == 'pratt_2000')} for Pratt, "
              f"{sum(1 for r in o.rows if r[0] == 'across')} across; {len(READ)} files read")
        return 0
    print(__doc__.split("USAGE")[1])
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
