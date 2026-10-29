#!/usr/bin/env python3
"""
The completeness test (T38): the scorer.

WHY
---
`COMPLETENESS_TEST_PLAN.md` fixes five measures before any reply comes. This script computes them from the key,
the judges' lists key and the five replies, and writes them out twice: `COMPLETENESS_RESULTS.md` to read and
`completeness_results.json` to check. It reads every reply with the checks of `build_completeness_test.py` and
refuses one that does not count. It judges nothing.

USAGE
-----
    python3 -B score_completeness_test.py score --key=completeness_key.json --lists=completeness_lists_key.json \\
        --checker-bechky=<reply 68> --checker-pratt=<reply 69> --matcher=<reply 70> \\
        --judge-bechky=<reply 71> --judge-pratt=<reply 72> --out=<dir>
    python3 -B score_completeness_test.py --selftest

THE MEASURES (the plan's words, made exact)
-------------------------------------------
For each paper and for both together. "The PI's passages" are the key's lines (Bechky 15, the duplicate once; Pratt
14); "confirmed" are those from which the coverage chat added a record (the key's `coverage_added` not empty).
A line is "paired" when it is in at least one of the judge's pairs. A "miss" is a verdict of evidence, assertion
or both.
- M1: the PI's passages: n; paired (listed by the checker); confirmed: n and paired.
- M2: the checker's lines: n; paired; the judge's verdicts on all of them, and on the unpaired ones, counted by
  verdict, with misses (evidence + assertion + both) summed.
- M3 (Bechky): the PI's 15 passages by the matcher: found; with a passage of Q; with a claim of Q; with either; and of
  the confirmed, with either.
- M4: on the PI's passages whose verdict is not `not_found`: the pairs (the judge says miss, the coverage chat added a
  record), as a 2 x 2 table; raw agreement and Cohen's kappa by `agreement.kappa`; per paper and both together.
  The number left out as `not_found` is given.
- M5: the judge's verdicts on the PI's lines and on the checker's, side by side; the checker's tests; the kinds of
  place in each list, by `build_completeness_test.kind_of`; the pages each list names.
Every line of both lists is then given in a table: its id in the judges' file, whose it is, its place, the
coverage chat's records (the PI's) or its test (the checker's), its pairs, its verdict, and for the PI's Bechky lines the
matcher's ids. No reason of any chat is printed.
"""
import hashlib
import json
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import agreement as A                    # noqa: E402
import build_citation_sheet as bcs       # noqa: E402
import build_completeness_test as bct    # noqa: E402

PAPERS = bct.PAPERS
NAMES = {"bechky": "Bechky", "pratt": "Pratt", "both": "both papers"}
CHATS = {"checker": {"bechky": "68", "pratt": "69"}, "matcher": {"bechky": "70"},
         "judge": {"bechky": "71", "pratt": "72"}}


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def load_counted(path, faults_of):
    rep, faults = bcs.load(path)
    if not faults:
        f = faults_of(rep)
        faults = f[0] if isinstance(f, tuple) else f
    if faults:
        raise SystemExit(f"{path}: does not count: {faults}")
    return rep


def measures(key, lk, checkers, matcher, judges):
    res = {"m1": {}, "m2": {}, "m3": {}, "m4": {}, "m5": {}, "lines": {}}
    m4_pairs = {}
    m4_left = {}
    for paper in PAPERS:
        kp = key["papers"][paper]
        lines = lk["papers"][paper]["lines"]
        j = judges[paper]
        paired = Counter(x for pr in j["pairs"] for x in pr)
        partners = {}
        for a, b in j["pairs"]:
            partners.setdefault(a, []).append(b)
            partners.setdefault(b, []).append(a)
        verdict = {lid: j["verdicts"][lid]["verdict"] for lid in lines}
        pis = {v["id"]: lid for lid, v in lines.items() if v["source"] == "pi"}
        its = [lid for lid, v in sorted(lines.items()) if v["source"] == "checker"]
        rows = {r["id"]: r for r in kp["lines"]}
        conf = [h for h, r in rows.items() if r["coverage_added"]]
        res["m1"][paper] = {"n": len(rows), "paired": sum(paired[pis[h]] > 0 for h in rows),
                            "confirmed": len(conf), "confirmed_paired": sum(paired[pis[h]] > 0 for h in conf)}
        unpaired = [lid for lid in its if not paired[lid]]

        def counts(ids):
            c = Counter(verdict[x] for x in ids)
            out = {v: c.get(v, 0) for v in bct.VERDICTS}
            out["miss"] = sum(c.get(v, 0) for v in bct.MISS)
            return out
        res["m2"][paper] = {"n": len(its), "paired": len(its) - len(unpaired), "verdicts_all": counts(its),
                            "unpaired": len(unpaired), "verdicts_unpaired": counts(unpaired)}
        pairs, left = [], 0
        for h, r in rows.items():
            v = verdict[pis[h]]
            if v == "not_found":
                left += 1
                continue
            pairs.append((v in bct.MISS, bool(r["coverage_added"])))
        m4_pairs[paper], m4_left[paper] = pairs, left
        tests = Counter(p["test"] for p in checkers[paper]["passages"])
        res["m5"][paper] = {
            "verdicts_pi": counts([pis[h] for h in rows]), "verdicts_checker": counts(its),
            "checker_tests": {t: tests.get(t, 0) for t in bct.TESTS},
            "kinds_pi": dict(sorted(Counter(r["kind"] for r in rows.values()).items())),
            "kinds_checker": dict(sorted(Counter(bct.kind_of(lines[x]["line"]) for x in its).items())),
            "pages_pi": sorted({p for r in rows.values() for p in r["pages"]}),
            "pages_checker": sorted({p for x in its for p in bct.pages_of(lines[x]["line"])}),
        }
        table = []
        for lid in sorted(lines):
            v = lines[lid]
            row = {"id": lid, "whose": "the PI's" if v["source"] == "pi" else "checker", "line": v["line"],
                   "pairs": sorted(partners.get(lid, [])), "verdict": verdict[lid]}
            if v["source"] == "pi":
                row["pi_id"] = v["id"]
                row["coverage_added"] = rows[v["id"]]["coverage_added"]
                if paper == "bechky":
                    lm = [k for k, h in key["matcher"].items() if h == v["id"]][0]
                    e = matcher["lines"][lm]
                    row["matcher"] = {"line": lm, "found": e["found"], "passages": e["passages"],
                                      "claims": e["claims"]}
            else:
                row["checker_n"] = v["id"]
                row["test"] = checkers[paper]["passages"][v["id"] - 1]["test"]
            table.append(row)
        res["lines"][paper] = table
    for scope, papers in (("bechky", ("bechky",)), ("pratt", ("pratt",)), ("both", PAPERS)):
        pairs = [p for x in papers for p in m4_pairs[x]]
        po, k = A.kappa(pairs)
        tab = Counter(pairs)
        res["m4"][scope] = {"n": len(pairs), "not_found_left_out": sum(m4_left[x] for x in papers),
                            "miss_added": tab[(True, True)], "miss_not_added": tab[(True, False)],
                            "not_miss_added": tab[(False, True)], "not_miss_not_added": tab[(False, False)],
                            "raw": po, "kappa": k}
    res["m1"]["both"] = {f: sum(res["m1"][p][f] for p in PAPERS) for f in res["m1"]["bechky"]}
    both2 = {"n": sum(res["m2"][p]["n"] for p in PAPERS), "paired": sum(res["m2"][p]["paired"] for p in PAPERS),
             "unpaired": sum(res["m2"][p]["unpaired"] for p in PAPERS)}
    for f in ("verdicts_all", "verdicts_unpaired"):
        both2[f] = {v: sum(res["m2"][p][f][v] for p in PAPERS) for v in res["m2"]["bechky"][f]}
    res["m2"]["both"] = both2
    ml = matcher["lines"]
    rows_b = {r["id"]: r for r in key["papers"]["bechky"]["lines"]}
    conf_l = [lm for lm, h in key["matcher"].items() if rows_b[h]["coverage_added"]]
    res["m3"] = {"n": len(ml), "found": sum(e["found"] for e in ml.values()),
                 "with_passage": sum(bool(e["passages"]) for e in ml.values()),
                 "with_claim": sum(bool(e["claims"]) for e in ml.values()),
                 "with_either": sum(bool(e["passages"] or e["claims"]) for e in ml.values()),
                 "confirmed": len(conf_l),
                 "confirmed_with_either": sum(bool(ml[x]["passages"] or ml[x]["claims"]) for x in conf_l)}
    return res


def frac(a, b):
    return f"{a} of {b}" if b else "none"


def dec(x, places=3):
    return "—" if x is None else f"{x:.{places}f}"


def write_md(res, meta):
    L = ["# The completeness test (T38): the results", "",
         f"Written by `score_completeness_test.py score`, as `COMPLETENESS_TEST_PLAN.md` fixes the measures. The key's "
         f"sha256 is {meta['key_sha256']}; the lists key's {meta['lists_sha256']}.", "", "## The replies", ""]
    for role, paper, f, s in meta["replies"]:
        L.append(f"- **chat {CHATS[role][paper]}, {NAMES[paper]}, the {role}:** {f}, sha256 {s}: counts.")
    L += ["", "## M1. The PI's passages that the checker lists", "",
          "By the judge's pairs. Confirmed: those from which the coverage chat added a record.", "",
          "| | the PI's passages | listed by the checker | confirmed | confirmed, listed |", "|---|---|---|---|---|"]
    for sc in ("bechky", "pratt", "both"):
        m = res["m1"][sc]
        L.append(f"| {NAMES[sc]} | {m['n']} | {m['paired']} | {m['confirmed']} | {m['confirmed_paired']} |")
    L += ["", "## M2. The checker's lines, and what the judge says of them", "",
          "| | lines | paired with the PI's | miss | covered | not in the brief | not found | unpaired | unpaired, miss |",
          "|---|---|---|---|---|---|---|---|---|"]
    for sc in ("bechky", "pratt", "both"):
        m = res["m2"][sc]
        va, vu = m["verdicts_all"], m["verdicts_unpaired"]
        L.append(f"| {NAMES[sc]} | {m['n']} | {m['paired']} | {va['miss']} | {va['covered']} | {va['not_in_brief']} "
                 f"| {va['not_found']} | {m['unpaired']} | {vu['miss']} |")
    L += ["", "A miss is a verdict of evidence, assertion or both. By verdict, on all the checker's lines:", ""]
    for sc in ("bechky", "pratt", "both"):
        va = res["m2"][sc]["verdicts_all"]
        L.append(f"- {NAMES[sc]}: " + ", ".join(f"{v} {va[v]}" for v in bct.VERDICTS))
    m = res["m3"]
    L += ["", "## M3. The ready test: the PI's Bechky passages in the second extraction (list Q)", "",
          f"By the matcher: found {frac(m['found'], m['n'])}; with a passage of list Q {frac(m['with_passage'], m['n'])}; "
          f"with a claim of list Q {frac(m['with_claim'], m['n'])}; with either {frac(m['with_either'], m['n'])}. "
          f"Of the {m['confirmed']} confirmed, with either: {m['confirmed_with_either']}.", "",
          "## M4. Described: the judge against the coverage chats, on the PI's passages", "",
          "| | n | miss, added | miss, not added | not a miss, added | not a miss, not added | raw | kappa | not found, left out |",
          "|---|---|---|---|---|---|---|---|---|"]
    for sc in ("bechky", "pratt", "both"):
        m = res["m4"][sc]
        L.append(f"| {NAMES[sc]} | {m['n']} | {m['miss_added']} | {m['miss_not_added']} | {m['not_miss_added']} | "
                 f"{m['not_miss_not_added']} | {dec(m['raw'])} | {dec(m['kappa'])} | {m['not_found_left_out']} |")
    L += ["", "## M5. Described", ""]
    for paper in PAPERS:
        m = res["m5"][paper]
        L += [f"**{NAMES[paper]}.**", "",
              "- The judge's verdicts on the PI's lines: " + ", ".join(f"{v} {m['verdicts_pi'][v]}" for v in bct.VERDICTS) + ".",
              "- On the checker's: " + ", ".join(f"{v} {m['verdicts_checker'][v]}" for v in bct.VERDICTS) + ".",
              "- The checker's tests: " + ", ".join(f"{t} {m['checker_tests'][t]}" for t in bct.TESTS) + ".",
              "- Kinds of place, the PI's: " + ", ".join(f"{k} {n}" for k, n in m["kinds_pi"].items()) +
              "; the checker's: " + (", ".join(f"{k} {n}" for k, n in m["kinds_checker"].items()) or "none") + ".",
              "- Pages, the PI's: " + ", ".join(map(str, m["pages_pi"])) + "; the checker's: " +
              (", ".join(map(str, m["pages_checker"])) or "none") + ".", ""]
    L += ["## Each line", "",
          "No reason of any chat is printed. A line's id is its id in the judges' file; the PI's are H01 onward in the "
          "key, the checker's are numbered as it numbered them.", ""]
    for paper in PAPERS:
        L += [f"### {NAMES[paper]}", "", "| id | whose | place | records added / test | pairs | verdict | matcher |",
              "|---|---|---|---|---|---|---|"]
        for r in res["lines"][paper]:
            if r["whose"] == "the PI's":
                rec = ", ".join(r["coverage_added"]) or "none"
                who = f"the PI's {r['pi_id']}"
                mt = ""
                if "matcher" in r:
                    e = r["matcher"]
                    mt = (f"{e['line']}: " + (", ".join(e["passages"] + e["claims"]) or "none")
                          if e["found"] else f"{e['line']}: not found")
            else:
                rec, who, mt = r["test"], f"checker {r['checker_n']}", ""
            L.append(f"| {r['id']} | {who} | {r['line'].replace('|', '/')} | {rec} | {', '.join(r['pairs']) or '—'} | "
                     f"{r['verdict']} | {mt} |")
        L.append("")
    return "\n".join(L).rstrip("\n") + "\n"


def score(args):
    a = dict(x.split("=", 1) for x in args)
    need = ("--key", "--lists", "--checker-bechky", "--checker-pratt", "--matcher", "--judge-bechky",
            "--judge-pratt", "--out")
    if sorted(a) != sorted(need):
        raise SystemExit(f"score needs exactly {need}")
    key = json.load(open(a["--key"], encoding="utf-8"))
    lk = json.load(open(a["--lists"], encoding="utf-8"))
    if lk["key_sha256"] != sha(a["--key"]):
        raise SystemExit("the lists key was not built from this key")
    checkers = {p: load_counted(a[f"--checker-{p}"], lambda r, p=p: bct.checker_faults(r, p)) for p in PAPERS}
    for p in PAPERS:
        if lk["replies"][p]["sha256"] != sha(a[f"--checker-{p}"]):
            raise SystemExit(f"{p}: the lists were not built from this checker's reply")
        if len(checkers[p]["passages"]) != sum(v["source"] == "checker" for v in lk["papers"][p]["lines"].values()):
            raise SystemExit(f"{p}: the checker's lines and the lists disagree")
    matcher = load_counted(a["--matcher"], bct.matcher_faults)
    judges = {p: load_counted(a[f"--judge-{p}"],
                              lambda r, p=p: bct.judge_faults(r, sorted(lk["papers"][p]["lines"]), p)) for p in PAPERS}
    res = measures(key, lk, checkers, matcher, judges)
    meta = {"key_sha256": sha(a["--key"]), "lists_sha256": sha(a["--lists"]),
            "replies": [("checker", "bechky", os.path.basename(a["--checker-bechky"]), sha(a["--checker-bechky"])),
                        ("checker", "pratt", os.path.basename(a["--checker-pratt"]), sha(a["--checker-pratt"])),
                        ("matcher", "bechky", os.path.basename(a["--matcher"]), sha(a["--matcher"])),
                        ("judge", "bechky", os.path.basename(a["--judge-bechky"]), sha(a["--judge-bechky"])),
                        ("judge", "pratt", os.path.basename(a["--judge-pratt"]), sha(a["--judge-pratt"]))],
            "scorer_sha256": sha(os.path.abspath(__file__))}
    out = a["--out"]
    os.makedirs(out, exist_ok=True)
    md = write_md(res, meta).encode("utf-8")
    js = (json.dumps({"meta": meta, **res}, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    for name, data in (("COMPLETENESS_RESULTS.md", md), ("completeness_results.json", js)):
        bct.write_new(os.path.join(out, name), data)
    return res


def selftest():
    import tempfile
    ok = True

    def expect(label, cond):
        nonlocal ok
        print(("ok    " if cond else "FAIL  ") + label)
        ok = ok and cond

    k = bct.key_data()
    with tempfile.TemporaryDirectory() as td:
        def put(name, obj):
            p = os.path.join(td, name)
            with open(p, "w", encoding="utf-8") as f:
                f.write(json.dumps(obj))
            return p
        kp = put("key.json", k)
        # made-up checkers: Bechky lists three passages, Pratt two
        cb = {"paper": "x", "read_to": "p. 643", "passages": [
            {"n": 1, "where": "pp. 611–612, the paragraph that runs over the page", "test": "evidence", "reason": "r"},
            {"n": 2, "where": "p. 612, footnote 1", "test": "evidence", "reason": "r"},
            {"n": 3, "where": "p. 630, second full paragraph", "test": "assertion", "reason": "r"}]}
        cp = {"paper": "x", "read_to": "p. 493", "passages": [
            {"n": 1, "where": "p. 459, third full paragraph", "test": "evidence", "reason": "r"},
            {"n": 2, "where": "p. 490, Table 3", "test": "both", "reason": "r"}]}
        pb, pp = put("cb.json", cb), put("cp.json", cp)
        out = os.path.join(td, "lists")
        bct.lists(kp, pb, pp, out)
        lkp = os.path.join(out, "completeness_lists_key.json")
        lk = json.load(open(lkp, encoding="utf-8"))

        def lid(paper, source, ident):
            return [x for x, v in lk["papers"][paper]["lines"].items() if v["source"] == source and v["id"] == ident][0]

        def a_first(x, y):
            return [x, y] if x.startswith("A") else [y, x]
        # Bechky judge: checker 1 pairs the PI's H08, checker 2 pairs the PI's H09; checker 3 unpaired, a miss
        jb_v = {}
        for x, v in lk["papers"]["bechky"]["lines"].items():
            jb_v[x] = {"verdict": "not_in_brief", "ids": [], "reason": "r"}
        for h in ("H08", "H09", "H11", "H13"):          # the four confirmed: misses
            jb_v[lid("bechky", "pi", h)] = {"verdict": "evidence", "ids": [], "reason": "r"}
        jb_v[lid("bechky", "pi", "H12")] = {"verdict": "covered", "ids": ["F149"], "reason": "r"}
        jb_v[lid("bechky", "pi", "H01")] = {"verdict": "assertion", "ids": [], "reason": "r"}   # miss, not added
        jb_v[lid("bechky", "pi", "H05")] = {"verdict": "not_found", "ids": [], "reason": "r"}
        jb_v[lid("bechky", "checker", 1)] = {"verdict": "evidence", "ids": [], "reason": "r"}
        jb_v[lid("bechky", "checker", 2)] = {"verdict": "evidence", "ids": [], "reason": "r"}
        jb_v[lid("bechky", "checker", 3)] = {"verdict": "both", "ids": [], "reason": "r"}
        jb = {"pairs": [a_first(lid("bechky", "pi", "H08"), lid("bechky", "checker", 1)),
                        a_first(lid("bechky", "pi", "H09"), lid("bechky", "checker", 2))], "verdicts": jb_v}
        # Pratt judge: checker 1 pairs the PI's H01; checker 2 unpaired, covered
        jp_v = {x: {"verdict": "covered", "ids": ["F01"], "reason": "r"} for x in lk["papers"]["pratt"]["lines"]}
        for h in ("H01", "H02", "H03"):
            jp_v[lid("pratt", "pi", h)] = {"verdict": "both", "ids": [], "reason": "r"}
        jp_v[lid("pratt", "checker", 1)] = {"verdict": "evidence", "ids": [], "reason": "r"}
        jp = {"pairs": [a_first(lid("pratt", "pi", "H01"), lid("pratt", "checker", 1))], "verdicts": jp_v}
        m = {"lines": {x: {"found": True, "passages": [], "claims": [], "reason": "r"} for x in bct.MATCHER_LINES}}
        m["lines"]["L08"]["passages"] = ["QP010"]
        m["lines"]["L14"]["passages"] = ["QP167"]
        m["lines"]["L15"]["claims"] = ["QC39"]
        m["lines"]["L05"] = {"found": False, "passages": [], "claims": [], "reason": "r"}
        res = score([f"--key={kp}", f"--lists={lkp}", f"--checker-bechky={pb}", f"--checker-pratt={pp}",
                     f"--matcher={put('m.json', m)}", f"--judge-bechky={put('jb.json', jb)}",
                     f"--judge-pratt={put('jp.json', jp)}", f"--out={os.path.join(td, 'out')}"])
        expect("M1 Bechky: 15 passages, 2 listed, 4 confirmed, 2 confirmed listed",
               res["m1"]["bechky"] == {"n": 15, "paired": 2, "confirmed": 4, "confirmed_paired": 2})
        expect("M1 Pratt: 14, 1, 10, 1", res["m1"]["pratt"] == {"n": 14, "paired": 1, "confirmed": 10,
                                                               "confirmed_paired": 1})
        expect("M1 both: 29, 3, 14, 3", res["m1"]["both"] == {"n": 29, "paired": 3, "confirmed": 14,
                                                             "confirmed_paired": 3})
        m2b = res["m2"]["bechky"]
        expect("M2 Bechky: 3 lines, 2 paired, 3 misses (one of them both), 1 unpaired miss",
               (m2b["n"], m2b["paired"], m2b["verdicts_all"]["miss"], m2b["unpaired"], m2b["verdicts_unpaired"]["miss"])
               == (3, 2, 3, 1, 1))
        m2p = res["m2"]["pratt"]
        expect("M2 Pratt: 2 lines, 1 paired, 1 miss, 1 covered, 1 unpaired, 0 unpaired miss",
               (m2p["n"], m2p["paired"], m2p["verdicts_all"]["miss"], m2p["verdicts_all"]["covered"],
                m2p["unpaired"], m2p["verdicts_unpaired"]["miss"]) == (2, 1, 1, 1, 1, 0))
        expect("M3: 14 found, 2 with a passage, 1 with a claim, 3 with either, 1 of 4 confirmed",
               (res["m3"]["found"], res["m3"]["with_passage"], res["m3"]["with_claim"], res["m3"]["with_either"],
                res["m3"]["confirmed"], res["m3"]["confirmed_with_either"]) == (14, 2, 1, 3, 4, 1))
        m4b = res["m4"]["bechky"]
        # Bechky: 15 passages, H05 not found -> 14; misses: H08, H09, H11, H13 (added), H01 (not added)
        expect("M4 Bechky: 14 judged, 4 miss-added, 1 miss-not-added, 0 not-miss-added, 9 not-miss-not-added, 1 left out",
               (m4b["n"], m4b["miss_added"], m4b["miss_not_added"], m4b["not_miss_added"], m4b["not_miss_not_added"],
                m4b["not_found_left_out"]) == (14, 4, 1, 0, 9, 1))
        po, kap = A.kappa([(True, True)] * 4 + [(True, False)] + [(False, False)] * 9)
        expect("M4 Bechky: raw and kappa as agreement.kappa gives", (m4b["raw"], m4b["kappa"]) == (po, kap))
        m4p = res["m4"]["pratt"]
        # Pratt: H01-H03 misses, all added; the other 11 covered: added are H06, H08-H13 (7) -> not-miss-added 7
        expect("M4 Pratt: 3 miss-added, 0, 7 not-miss-added, 4 not-miss-not-added",
               (m4p["miss_added"], m4p["miss_not_added"], m4p["not_miss_added"], m4p["not_miss_not_added"])
               == (3, 0, 7, 4))
        expect("M4 both: 28 judged", res["m4"]["both"]["n"] == 28)
        expect("M5 Bechky: checker tests 2 evidence, 1 assertion",
               res["m5"]["bechky"]["checker_tests"] == {"evidence": 2, "assertion": 1, "both": 0})
        expect("M5 Pratt: kinds of the checker's lines", res["m5"]["pratt"]["kinds_checker"] == {"paragraph": 1, "table": 1})
        md = open(os.path.join(td, "out", "COMPLETENESS_RESULTS.md"), encoding="utf-8").read()
        expect("the results print no reason", "| r |" not in md and " r." not in md)
        expect("the lines table has 17 + 16 rows", md.count("| the PI's H") == 29 and md.count("| checker ") == 5)
        # a judge's reply that does not count is refused
        bad = json.loads(json.dumps(jb))
        del bad["verdicts"][lid("bechky", "checker", 3)]
        try:
            score([f"--key={kp}", f"--lists={lkp}", f"--checker-bechky={pb}", f"--checker-pratt={pp}",
                   f"--matcher={put('m.json', m)}", f"--judge-bechky={put('jb2.json', bad)}",
                   f"--judge-pratt={put('jp.json', jp)}", f"--out={os.path.join(td, 'out2')}"])
            expect("a judge's reply that does not count is refused", False)
        except SystemExit:
            expect("a judge's reply that does not count is refused", True)
    print("SELFTEST PASSES" if ok else "SELFTEST FAILS")
    return 0 if ok else 1


def main(argv):
    if argv[1:] == ["--selftest"]:
        return selftest()
    if len(argv) > 2 and argv[1] == "score":
        score(argv[2:])
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
