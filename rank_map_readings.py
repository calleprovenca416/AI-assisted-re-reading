"""T39, measure 8 (MAP_TEST_PLAN.md, the addition of 19 Oct 2026): a rough ranking of the readings by the map,
the score a Fable chat proposed on 19 Oct, unchanged, and its check against the PI's worth.

A coding's score: for each reading and each of T37's two codings as F4 of `map_results.json` gives them (the first
coding `gemini`, the second `astra`), the labels the closure gives the paper's core claims, weighted contested 3,
unsupported 2, weakened 1, idle 1/2, restated 0, summed and divided by 3 times the number of core claims
(`map_round2_key.json`). A reading's score is the lower of its two codings' scores. Scores are exact fractions.

Stars, from a score rounded to two decimals, half up: 0.60 or more 5; 0.40 to 0.59 4; 0.25 to 0.39 3; 0.10 to 0.24 2;
below 0.10 1. A reading's stars are its score's. The flag: its two codings' scores give different stars. The cost: the
number of passages in its evidence list in the joined placement reply.

The check, each paper on its own, on its real readings: Spearman's rank correlation between the reading's score and
the PI's worth (`relation_results.json`), tied values given their mean rank; its two-sided permutation p-value: the
worths shuffled among the same readings 10,000 times, each shuffle made afresh (a copy of the worths in reading order,
shuffled by `random.Random(20261027).shuffle`), one stream used in the order bechky, pratt, both papers together; a
shuffle counts when abs(its correlation) >= abs(the observed one) - 1e-12; p = (count + 1) / 10,001. Beside it: the
same correlation for each coding's own score (no p); the mean score at each worth; the correlation over both papers'
real readings together, with its p, as a secondary figure. Read, as fixed: tracks the PI's worth if the correlation is
positive with p < 0.05; runs against it if negative with p < 0.05; otherwise no clear relation at this size.

Also recomputes the twelve figures of Fable's table and says whether each is the same.

usage: python3 -I -B rank_map_readings.py selftest
       python3 -I -B rank_map_readings.py run <folder with the inputs> <output folder>
"""
import hashlib, json, math, os, random, sys
from fractions import Fraction

WEIGHTS = {"contested": Fraction(3), "unsupported": Fraction(2), "weakened": Fraction(1), "idle": Fraction(1, 2),
           "restated": Fraction(0)}
CODINGS = ("gemini", "astra")
PAPERS = ("bechky", "pratt")
SEED = 20261027
SHUFFLES = 10000
TOL = 1e-12
PLACEMENTS = {"bechky": "reply_77_bechky_place_argon.json", "pratt": "reply_78_pratt_place_argon.json"}
INPUTS = ("map_results.json", "relation_results.json", "map_round2_key.json", PLACEMENTS["bechky"], PLACEMENTS["pratt"])
# Fable's table: (paper, reading) -> (first coding, second coding), to two decimals
FABLE = {("pratt", "R09"): ("0.70", "0.70"), ("pratt", "R14"): ("0.70", "0.73"), ("bechky", "R22"): ("0.62", "0.62"),
         ("bechky", "R05"): ("0.57", "0.57"), ("pratt", "R08"): ("0.48", "0.45"), ("bechky", "R07"): ("0.48", "0.38"),
         ("bechky", "R29"): ("0.31", "0.31"), ("pratt", "R03"): ("0.20", "0.20"), ("pratt", "R02"): ("0.17", "0.13"),
         ("bechky", "R27"): ("0.48", "0.14"), ("pratt", "R01"): ("0.03", "0.03"), ("bechky", "R16"): ("0.43", "0.00")}
FABLE_FINDINGS = {("pratt", "R09"): 9, ("pratt", "R14"): 7, ("bechky", "R22"): 8, ("bechky", "R05"): 25,
                  ("pratt", "R08"): 4, ("bechky", "R07"): 9, ("bechky", "R29"): 10, ("pratt", "R03"): 13,
                  ("pratt", "R02"): 6, ("bechky", "R27"): 5, ("pratt", "R01"): 10, ("bechky", "R16"): 13}


def coding_score(labels, ncore):
    """labels: {claim: label} on core claims; returns an exact Fraction."""
    for lab in labels.values():
        if lab not in WEIGHTS:
            raise ValueError(f"unknown label {lab!r}")
    return sum((WEIGHTS[lab] for lab in labels.values()), Fraction(0)) / (3 * ncore)


def round2(x):
    """x a Fraction; rounded to two decimals, half up, returned as a Fraction of hundredths."""
    return Fraction(math.floor(x * 100 + Fraction(1, 2)), 100)


def stars(x):
    q = round2(x)
    if q >= Fraction(60, 100):
        return 5
    if q >= Fraction(40, 100):
        return 4
    if q >= Fraction(25, 100):
        return 3
    if q >= Fraction(10, 100):
        return 2
    return 1


def fmt2(x):
    k = round2(x) * 100
    assert k.denominator == 1 and k >= 0
    k = int(k)
    return f"{k // 100}.{k % 100:02d}"


def midranks(values):
    order = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
            j += 1
        mean_rank = (i + j) / 2 + 1
        for k in range(i, j + 1):
            ranks[order[k]] = mean_rank
        i = j + 1
    return ranks


def pearson(a, b):
    n = len(a)
    ma, mb = sum(a) / n, sum(b) / n
    da, db = [x - ma for x in a], [y - mb for y in b]
    sab = sum(x * y for x, y in zip(da, db))
    saa, sbb = sum(x * x for x in da), sum(y * y for y in db)
    if saa == 0 or sbb == 0:
        return None
    return sab / math.sqrt(saa * sbb)


def spearman(x, y):
    return pearson(midranks(list(x)), midranks(list(y)))


def perm_p(x, y, rng, shuffles=SHUFFLES):
    """Two-sided permutation p of Spearman's rho, shuffling y afresh each time; returns (rho, p, count)."""
    obs = spearman(x, y)
    if obs is None:
        for _ in range(shuffles):  # keep the stream in step even when rho is undefined
            w = list(y)
            rng.shuffle(w)
        return None, None, None
    count = 0
    for _ in range(shuffles):
        w = list(y)
        rng.shuffle(w)
        r = spearman(x, w)
        if r is not None and abs(r) >= abs(obs) - TOL:
            count += 1
    return obs, (count + 1) / (shuffles + 1), count


def verdict(rho, p):
    if rho is None or p is None:
        return "no clear relation at this size"
    if p < 0.05 and rho > 0:
        return "tracks the PI's worth"
    if p < 0.05 and rho < 0:
        return "runs against the PI's worth"
    return "no clear relation at this size"


def reading_rows(f4_readings, ncore, evidence_counts):
    rows = []
    for r in f4_readings:
        s = {c: coding_score(r[c]["core_labels"], ncore) for c in CODINGS}
        low = min(s.values())
        st = {c: stars(s[c]) for c in CODINGS}
        rows.append({"reading": r["reading"], "planted": bool(r["planted"]), "worth": r["worth"],
                     "score_gemini": s["gemini"], "score_astra": s["astra"], "score": low, "stars": stars(low),
                     "stars_gemini": st["gemini"], "stars_astra": st["astra"],
                     "flag": st["gemini"] != st["astra"], "cost": evidence_counts[r["reading"]]})
    return rows


def ordered(rows):
    return sorted(rows, key=lambda x: (-x["score"], x["reading"]))


def check_block(rows, rng):
    real = sorted([x for x in rows if not x["planted"]], key=lambda x: x["reading_key"])
    sc = [x["score"] for x in real]
    w = [x["worth"] for x in real]
    rho, p, count = perm_p(sc, w, rng)
    per_coding = {c: spearman([x["score_" + c] for x in real], w) for c in CODINGS}
    by_worth = {}
    for v in sorted(set(w)):
        grp = [x["score"] for x in real if x["worth"] == v]
        by_worth[str(v)] = {"n": len(grp), "mean_score": float(sum(grp, Fraction(0)) / len(grp))}
    return {"n": len(real), "rho": rho, "p": p, "count": count, "verdict": verdict(rho, p),
            "rho_by_coding": per_coding, "mean_score_by_worth": by_worth}


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def compute(folder):
    j = {n: json.load(open(os.path.join(folder, n), encoding="utf-8")) for n in INPUTS}
    worth_src = j["relation_results.json"]["worth"]
    out = {"what": "T39, measure 8: a rough ranking of the readings by the map (Fable's score) and its check against "
                   "the PI's worth, by rank_map_readings.py, as MAP_TEST_PLAN.md's addition of 19 Oct 2026 "
                   "defines them",
           "inputs": {n: sha(os.path.join(folder, n)) for n in INPUTS},
           "script_sha256": sha(os.path.abspath(__file__)),
           "seed": SEED, "shuffles": SHUFFLES, "papers": {}}
    rng = random.Random(SEED)
    all_rows = []
    for k, p in enumerate(PAPERS):
        core = j["map_round2_key.json"]["papers"][p]["core"]
        f4 = j["map_results.json"]["papers"][p]["F4"]["readings"]
        ev = {x["reading"]: len(x["evidence"]) for x in j[PLACEMENTS[p]]["placements"]}
        assert set(ev) == {r["reading"] for r in f4}, p
        for r in f4:  # F4's worth must be the PI's worth as relation_results.json holds it
            want = None if r["planted"] else worth_src[f"{p}|{r['reading']}"]
            assert r["worth"] == want, (p, r["reading"])
        rows = reading_rows(f4, len(core), ev)
        for x in rows:
            x["reading_key"] = (k, x["reading"])
        out["papers"][p] = {"core": core, "rows": rows}
        all_rows += rows
    for p in PAPERS:
        out["papers"][p]["check"] = check_block(out["papers"][p]["rows"], rng)
    out["both"] = check_block(all_rows, rng)
    fable = []
    for (p, r), (a, b) in FABLE.items():
        row = next(x for x in out["papers"][p]["rows"] if x["reading"] == r)
        got = (fmt2(row["score_gemini"]), fmt2(row["score_astra"]))
        fable.append({"paper": p, "reading": r, "fable": [a, b], "recomputed": list(got),
                      "fable_findings": FABLE_FINDINGS[(p, r)], "cost": row["cost"],
                      "same": got == (a, b) and FABLE_FINDINGS[(p, r)] == row["cost"]})
    out["fable_table"] = fable
    return out


def as_json(out):
    def conv(o):
        if isinstance(o, Fraction):
            return {"fraction": f"{o.numerator}/{o.denominator}", "value": round(float(o), 6)}
        if isinstance(o, dict):
            return {k: conv(v) for k, v in o.items() if k != "reading_key"}
        if isinstance(o, list):
            return [conv(v) for v in o]
        if isinstance(o, float):
            return round(o, 6)
        return o
    return json.dumps(conv(out), ensure_ascii=False, indent=1, sort_keys=True) + "\n"


def f3(x):
    return "—" if x is None else f"{x:.3f}"


def as_md(out):
    L = ["# T39, measure 8: a rough ranking of the readings by the map", "",
         "Fable's score (proposed on 19 Oct), unchanged, and its check against the PI's worth, as "
         "`MAP_TEST_PLAN.md`'s addition of 19 Oct 2026 defines them. Exploratory: not a criterion of T39. "
         "Written by `rank_map_readings.py` (sha256 opens " + out["script_sha256"][:8] + ").", "",
         "A coding's score: the labels on the paper's core claims, weighted contested 3, unsupported 2, weakened 1, "
         "idle ½, restated 0, over 3 × the core claims. A reading's score is the lower of its two codings' (first: "
         "`gemini`; second: `astra`). Stars from the score rounded to two decimals: ≥ 0.60 five, 0.40–0.59 four, "
         "0.25–0.39 three, 0.10–0.24 two, below 0.10 one. Flag: the two codings give different stars. Cost: the "
         "passages in the reading's evidence list. It measures how much of the argument a reading would bring down "
         "if it were right, not whether it is right.", ""]
    names = {"bechky": "Bechky", "pratt": "Pratt"}
    for p in PAPERS:
        P = out["papers"][p]
        c = P["check"]
        L += [f"## {names[p]} ({len(P['core'])} core claims)", "",
              f"**The check:** Spearman's rho between the score and the PI's worth, {c['n']} real readings: "
              f"{f3(c['rho'])}, permutation p {f3(c['p'])} ({c['count']} of {out['shuffles']:,} shuffles at least as "
              f"far from zero). Read as fixed: **{c['verdict']}**.", "",
              f"Each coding's own score against the PI's worth: first {f3(c['rho_by_coding']['gemini'])}, second "
              f"{f3(c['rho_by_coding']['astra'])}. Mean score at each worth: " +
              "; ".join(f"{v}: {d['mean_score']:.3f} (n {d['n']})" for v, d in c["mean_score_by_worth"].items()) +
              ".", "",
              "| reading | worth | first coding | second coding | score | stars | flag | cost |",
              "|---|---|---|---|---|---|---|---|"]
        for x in ordered([r for r in P["rows"] if not r["planted"]]):
            flag = f"yes ({x['stars_gemini']}/{x['stars_astra']})" if x["flag"] else ""
            L.append(f"| {x['reading']} | {x['worth']} | {fmt2(x['score_gemini'])} | {fmt2(x['score_astra'])} | "
                     f"{fmt2(x['score'])} | {x['stars']} | {flag} | {x['cost']} |")
        L += ["", "The planted readings, which have no worth:", "",
              "| reading | first coding | second coding | score | stars | flag | cost |", "|---|---|---|---|---|---|---|"]
        for x in ordered([r for r in P["rows"] if r["planted"]]):
            flag = f"yes ({x['stars_gemini']}/{x['stars_astra']})" if x["flag"] else ""
            L.append(f"| {x['reading']} | {fmt2(x['score_gemini'])} | {fmt2(x['score_astra'])} | {fmt2(x['score'])} | "
                     f"{x['stars']} | {flag} | {x['cost']} |")
        L.append("")
    b = out["both"]
    L += ["## Both papers together (secondary)", "",
          f"Spearman's rho over {b['n']} real readings: {f3(b['rho'])}, permutation p {f3(b['p'])} ({b['count']} of "
          f"{out['shuffles']:,} shuffles). Read as fixed, as secondary: **{b['verdict']}**. Each coding's own score: "
          f"first {f3(b['rho_by_coding']['gemini'])}, second {f3(b['rho_by_coding']['astra'])}.", "",
          "## Fable's twelve figures, recomputed", "",
          "| paper | reading | Fable: first / second | recomputed | Fable's findings | cost | same |",
          "|---|---|---|---|---|---|---|"]
    for f in out["fable_table"]:
        L.append(f"| {names[f['paper']]} | {f['reading']} | {f['fable'][0]} / {f['fable'][1]} | "
                 f"{f['recomputed'][0]} / {f['recomputed'][1]} | {f['fable_findings']} | {f['cost']} | "
                 f"{'yes' if f['same'] else 'NO'} |")
    L += ["", "Seed " + str(out["seed"]) + ", one stream: Bechky's shuffles, then Pratt's, then both papers'. Inputs, "
          "by sha256:", ""]
    for n, h in out["inputs"].items():
        L.append(f"- `{n}`: {h}")
    return "\n".join(L) + "\n"


def run(folder, outdir):
    out = compute(folder)
    os.makedirs(outdir, exist_ok=True)
    open(os.path.join(outdir, "ranking_check.json"), "w", encoding="utf-8").write(as_json(out))
    open(os.path.join(outdir, "RANKING_CHECK.md"), "w", encoding="utf-8").write(as_md(out))
    same = sum(f["same"] for f in out["fable_table"])
    print("written RANKING_CHECK.md and ranking_check.json; Fable's figures the same:", same, "of", len(FABLE))
    for p in PAPERS:
        c = out["papers"][p]["check"]
        print(p, "n", c["n"], "rho", f3(c["rho"]), "p", f3(c["p"]), "->", c["verdict"])
    b = out["both"]
    print("both n", b["n"], "rho", f3(b["rho"]), "p", f3(b["p"]), "->", b["verdict"], "(secondary)")


def selftest():
    fails = []

    def expect(name, cond):
        print(("ok   " if cond else "FAIL ") + name)
        if not cond:
            fails.append(name)

    F = Fraction
    expect("score: each weight once over 7 core claims is 6.5/21",
           coding_score({"A": "contested", "B": "unsupported", "C": "weakened", "D": "idle", "E": "restated"}, 7)
           == F(13, 42))
    expect("score: divisor is 3 x the core claims (10)", coding_score({"A": "contested"}, 10) == F(1, 10))
    expect("score: no labels is 0", coding_score({}, 7) == 0)
    try:
        coding_score({"A": "toppled"}, 7)
        expect("score: an unknown label is refused", False)
    except ValueError:
        expect("score: an unknown label is refused", True)
    expect("round half up: 25/42 (0.5952) -> 0.60, five stars", round2(F(25, 42)) == F(60, 100) and stars(F(25, 42)) == 5)
    expect("round half up: 0.245 exactly -> 0.25, three stars", round2(F(49, 200)) == F(25, 100) and stars(F(49, 200)) == 3)
    expect("round: 0.5949 -> 0.59, four stars", stars(F(5949, 10000)) == 4)
    expect("round half up: 4/42 (0.0952) -> 0.10, two stars", stars(F(4, 42)) == 2)
    expect("stars: 0.0949 -> one star", stars(F(949, 10000)) == 1)
    expect("stars: 0.40 exactly -> four, 0.3949 -> three", stars(F(40, 100)) == 4 and stars(F(3949, 10000)) == 3)
    expect("stars: 0.25 exactly -> three, 0.10 exactly -> two", stars(F(1, 4)) == 3 and stars(F(1, 10)) == 2)
    expect("fmt2: 0.619 -> '0.62', 0 -> '0.00', 1/30 -> '0.03'",
           fmt2(F(13, 21)) == "0.62" and fmt2(F(0)) == "0.00" and fmt2(F(1, 30)) == "0.03")
    expect("midranks: ties take their mean rank", midranks([10, 20, 20, 5]) == [2.0, 3.5, 3.5, 1.0])
    r = spearman([1, 2, 3, 4, 5], [5, 6, 7, 8, 7])
    expect("spearman with a tie: 8/sqrt(95)", r is not None and abs(r - 8 / math.sqrt(95)) < 1e-12)
    expect("spearman: reversed order is -1", abs(spearman([1, 2, 3, 4], [4, 3, 2, 1]) + 1) < 1e-12)
    expect("spearman: a constant is undefined", spearman([1, 2, 3], [2, 2, 2]) is None)
    rho1, p1, c1 = perm_p([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], random.Random(7), 2000)
    rho2, p2, c2 = perm_p([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], random.Random(7), 2000)
    expect("perm: the same seed gives the same p", (rho1, p1, c1) == (rho2, p2, c2))
    expect("perm: a perfect order of 5 has p near 2/120", abs(rho1 - 1) < 1e-12 and 0.005 < p1 < 0.035)
    expect("perm: p is (count + 1) / (shuffles + 1)", abs(p1 - (c1 + 1) / 2001) < 1e-15)
    expect("perm: each shuffle afresh from the order given (count 39 for seed 7, as an independent scipy run gives)",
           c1 == 39)
    rho3, p3, c3 = perm_p([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], random.Random(7), 2000)
    expect("perm: two-sided (a perfect reversed order counts the same as a perfect order)",
           abs(rho3 + 1) < 1e-12 and 0.005 < p3 < 0.035)
    rho4, p4, _ = perm_p([1, 2, 3, 4, 5, 6], [3, 1, 2, 6, 4, 5], random.Random(7), 2000)
    expect("perm: a weak order is not significant", rho4 > 0 and p4 > 0.05)
    expect("verdict: positive and p < .05 tracks; negative and p < .05 runs against; else none",
           verdict(0.6, 0.01) == "tracks the PI's worth" and verdict(-0.6, 0.01) == "runs against the PI's worth"
           and verdict(0.6, 0.05) == "no clear relation at this size" and verdict(None, None).startswith("no clear"))
    f4 = [{"reading": "R01", "planted": False, "worth": 2,
           "gemini": {"core_labels": {"C1": "contested", "C2": "unsupported"}},
           "astra": {"core_labels": {"C1": "weakened"}}},
          {"reading": "R02", "planted": True, "worth": None,
           "gemini": {"core_labels": {"C1": "contested"}}, "astra": {"core_labels": {"C1": "contested"}}}]
    rows = reading_rows(f4, 3, {"R01": 4, "R02": 7})
    x = rows[0]
    expect("rows: the lower of the two codings is the score",
           x["score_gemini"] == F(5, 9) and x["score_astra"] == F(1, 9) and x["score"] == F(1, 9))
    expect("rows: stars from the lower score; flag when the codings' stars differ",
           x["stars"] == 2 and x["stars_gemini"] == 4 and x["stars_astra"] == 2 and x["flag"] is True)
    expect("rows: no flag when the stars agree; cost is the evidence count",
           rows[1]["flag"] is False and rows[1]["cost"] == 7 and x["cost"] == 4)
    expect("order: by score, highest first, then by reading",
           [r["reading"] for r in ordered([{"reading": "R2", "score": F(1, 3)}, {"reading": "R1", "score": F(1, 3)},
                                           {"reading": "R3", "score": F(1, 2)}])] == ["R3", "R1", "R2"])
    blk_rows = []
    for i, (wv, sc) in enumerate([(0, 0), (1, 1), (2, 2), (3, 3), (1, 2), (2, 1)]):
        blk_rows.append({"reading": f"R{i:02d}", "planted": False, "worth": wv, "score": F(sc, 10),
                         "score_gemini": F(sc, 10), "score_astra": F(sc, 20), "reading_key": (0, f"R{i:02d}")})
    blk_rows.append({"reading": "R99", "planted": True, "worth": None, "score": F(9, 10), "score_gemini": F(9, 10),
                     "score_astra": F(9, 10), "reading_key": (0, "R99")})
    blk = check_block(blk_rows, random.Random(3))
    expect("check: planted readings are left out of the correlation", blk["n"] == 6)
    expect("check: the mean score at each worth",
           blk["mean_score_by_worth"]["1"] == {"n": 2, "mean_score": 0.15} and blk["mean_score_by_worth"]["3"]["n"] == 1)
    expect("check: each coding's own rho is given", set(blk["rho_by_coding"]) == set(CODINGS))
    print(f"{'ALL PASSED' if not fails else str(len(fails)) + ' FAILED'}")
    return 1 if fails else 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "selftest":
        sys.exit(selftest())
    if len(sys.argv) == 4 and sys.argv[1] == "run":
        run(sys.argv[2], sys.argv[3])
        sys.exit(0)
    raise SystemExit(__doc__)
