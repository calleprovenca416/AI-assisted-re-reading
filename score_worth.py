"""
Set the PI's worth ratings beside the markers' codes and the attack (T29), in one command.

    python3 score_worth.py <out_dir>

The PI's sheet came twice: first with three readings blank, then with those three rated
and nothing else changed.

Reads:

    stage2/worth/worth_sheet_filled_2.xlsx  the PI's ratings, the second sheet, filed unchanged
    stage2/worth/worth_sheet_filled.xlsx    the PI's ratings, the first sheet, filed unchanged
    stage2/markers/KEY.json                which reading came from which arm, card or reply
    stage2/marker_replies/                 the four marker replies, loaded as score_markers.py loads them
    each system reading's card             its move and its attack status (killed or survived)

Both sheets are checked first: the same sheets, readings and texts as the key, and every
Worth a whole number from 0 to 3 or left empty; and the second must keep every Worth and
Note the first gave. Anything else stops the script. The ratings used are the second
sheet's. A reading blank on the first sheet and rated on the second is marked as rated
late: the PI rated those after the PI had been told their arm, so each arm's mean is also given
without them. An empty Worth on the second sheet is reported as not rated, left out of
every mean and every test, and never filled in; where an arm has readings not rated, the
lowest and the highest mean it could have once they are rated are given beside its mean.

Writes <out_dir>/WORTH_RESULTS.md and <out_dir>/worth_joined.json (one record per
reading: its arm, move, sentences, worth, note, each marker's counts and its attack
status). WORTH_RESULTS.md has:

 1. worth by arm, for each paper and for both together: readings, rated, mean, the count
    at each point of the scale, rated 2 or more, and the mean length of a reading in sentences;
 2. worth beside the markers, by arm: facts found (R, RI and RA over the sentences that
    report) and contradicted sentences for each marker; readings with a U or C in the
    warrant position; of the readings rated, those rated 2 or more whose warrant no marker
    codes U or C, and those rated 2 or more with no C from either marker; the attack's
    verdicts (the attack ran on the system's readings only);
 3. reading by reading, the same, with the PI's note;
 4. other cuts: worth of the system's killed and surviving readings; how far worth goes
    with facts found and with a reading's length (Spearman's rank correlation, its p-value
    by 20,000 seeded shuffles); the gap in mean worth between the system and each other
    arm, and between the middle and the plain arm, with its p-value by exact relabelling
    (within each paper, for both papers together); worth by move.

Arms are named with their sources: system (the generation chats, which wrote from each
paper's record, without the PDF), middle (the reading chats: the same prompt with the
PDF), plain (the plain chats: the PDF and a plain prompt). The markers' figures on Pratt
rest on a kappa below the bar of 0.60 and are reported, marked so, by a decision of
11 Oct 2026 made after the result, as in score_markers.py. The PI's rating is declared not blind: the PI had
seen every reply before the PI rated, and the plain arm's form can be told apart.
"""
import collections
import itertools
import json
import os
import random
import sys

from openpyxl import load_workbook

from score_markers import CODES, GATE, KEY, MARKERS, NAMES, REPLIES, REPORTED_BELOW_BAR, kappa, load

SHEET = "stage2/worth/worth_sheet_filled_2.xlsx"
FIRST = "stage2/worth/worth_sheet_filled.xlsx"
SEED = 20261011
SHUFFLES = 20000
PAPERS = [("pratt", "Pratt", "Pratt (2000)"), ("bechky", "Bechky", "Bechky (2020)")]
ARMS = [("system", "system (the generation chats)"), ("middle", "middle (the reading chats)"),
        ("plain", "plain (the plain chats)")]
SHORT = {"system": "system", "middle": "middle", "plain": "plain"}
SCALE = [0, 1, 2, 3]
MOVES = {"construct_inversion": "construct inversion", "counterfactual_ending": "counterfactual ending",
         "focalization_shift": "focalization shift", "construct_fission": "construct fission",
         "boundary_shift": "boundary shift"}


def read_sheet(key, path):
    wb = load_workbook(path)
    if wb.sheetnames != ["Instructions", "Pratt", "Bechky"]:
        raise SystemExit(f"{path}: sheets {wb.sheetnames}, not Instructions, Pratt, Bechky")
    out = {}
    for paper, title, _ in PAPERS:
        ws = wb[title]
        for r, e in enumerate(key["papers"][paper], start=2):
            rid, text = ws[f"A{r}"].value, ws[f"B{r}"].value
            if rid != e["reading"]:
                raise SystemExit(f"{path} {title} A{r}: {rid!r}, the key has {e['reading']}")
            if text != " ".join(u["text"] for u in e["units"]):
                raise SystemExit(f"{path} {title} B{r} ({rid}): the text is not the key's")
            w = ws[f"C{r}"].value
            if isinstance(w, float) and w.is_integer():
                w = int(w)
            if w is not None and (isinstance(w, bool) or not isinstance(w, int) or not 0 <= w <= 3):
                raise SystemExit(f"{path} {title} C{r} ({rid}): Worth {w!r} is not a whole number from 0 to 3")
            note = ws[f"D{r}"].value
            out[rid] = {"worth": w, "note": note.strip() if isinstance(note, str) and note.strip() else None}
        last = len(key["papers"][paper]) + 1
        if any(c.value is not None for row in ws.iter_rows(min_row=last + 1) for c in row):
            raise SystemExit(f"{path} {title}: cells filled below the last reading")
    return out


def marks(codes, units):
    cs = [codes[u] for u in units]
    k = collections.Counter(c["code"] for c in cs)
    reporting = sum(v for c, v in k.items() if c != "N")
    return {"reporting": reporting, "found": k["R"] + k["RI"] + k["RA"], "R": k["R"], "P": k["P"],
            "U": k["U"], "C": k["C"],
            "warrant": any(c["code"] in ("U", "C") and c.get("position") == "warrant" for c in cs)}


def mean(xs):
    return sum(xs) / len(xs) if xs else None


def f2(x):
    return "—" if x is None else f"{x:.2f}"


def pct(a, b):
    return f"{100 * a / b:.0f}%" if b else "—"


def ranks(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    i = 0
    while i < len(xs):
        j = i
        while j + 1 < len(xs) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        for t in range(i, j + 1):
            r[order[t]] = (i + j) / 2 + 1
        i = j + 1
    return r


def pearson(a, b):
    n = len(a)
    ma, mb = sum(a) / n, sum(b) / n
    sa, sb = sum((x - ma) ** 2 for x in a), sum((y - mb) ** 2 for y in b)
    if sa == 0 or sb == 0:
        return None
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / (sa * sb) ** 0.5


def spearman(a, b, label):
    """Spearman's rho and a two-sided p-value from SHUFFLES seeded shuffles of b."""
    rho = pearson(ranks(a), ranks(b))
    if rho is None:
        return None, None
    rng = random.Random(f"{SEED}-{label}")
    ra, bb, hits = ranks(a), list(b), 0
    for _ in range(SHUFFLES):
        rng.shuffle(bb)
        r = pearson(ra, ranks(bb))
        if r is not None and abs(r) >= abs(rho) - 1e-12:
            hits += 1
    return rho, (hits + 1) / (SHUFFLES + 1)


def relabel_test(strata):
    """strata: per paper, (worths of arm A, worths of arm B). The gap is mean(A) - mean(B) over
    all strata together; its two-sided p-value by every relabelling within each stratum."""
    a_all = [w for a, _ in strata for w in a]
    b_all = [w for _, b in strata for w in b]
    gap = mean(a_all) - mean(b_all)
    na, nb = len(a_all), len(b_all)
    options = []
    for a, b in strata:
        pool = a + b
        sums = [sum(pool[i] for i in idx) for idx in itertools.combinations(range(len(pool)), len(a))]
        options.append((sum(pool), sums))
    total = hits = 0
    for combo in itertools.product(*[s for _, s in options]):
        sa = sum(combo)
        sb = sum(t for t, _ in options) - sa
        g = sa / na - sb / nb
        total += 1
        if abs(g) >= abs(gap) - 1e-12:
            hits += 1
    return gap, hits / total, total


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: python3 score_worth.py <out_dir>")
    out_dir = sys.argv[1]
    os.makedirs(out_dir, exist_ok=True)
    key = json.load(open(KEY, encoding="utf-8"))
    first = read_sheet(key, FIRST)
    rated = read_sheet(key, SHEET)
    for rid, v in first.items():
        if v["worth"] is not None and (rated[rid]["worth"], rated[rid]["note"]) != (v["worth"], v["note"]):
            raise SystemExit(f"{rid}: {SHEET} changes the Worth or Note that {FIRST} gave")
    late = {rid for rid, v in first.items() if v["worth"] is None and rated[rid]["worth"] is not None}
    rows, below = [], {}
    for paper, title, _ in PAPERS:
        entries = key["papers"][paper]
        units = [u["unit"] for e in entries for u in e["units"]]
        codes = {}
        for m, (fname, _) in MARKERS[paper].items():
            obj, _ = load(os.path.join(REPLIES, fname))
            codes[m] = {c["unit"]: c for c in obj["codes"]}
        _, k7 = kappa([(codes["opus"][u]["code"], codes["astra"][u]["code"]) for u in units], CODES)
        below[paper] = k7 if k7 < GATE else None
        if k7 < GATE and paper not in REPORTED_BELOW_BAR:
            raise SystemExit(f"{title}: kappa {k7:.3f} is below the bar, and no decision to report it is recorded")
        for e in entries:
            us = [u["unit"] for u in e["units"]]
            if e["arm"] == "system":
                card = json.load(open(e["source"], encoding="utf-8"))
                move, attack = card["move"], {"killed": "killed", "survived_attack": "survived"}[card["status"]]
            elif e["arm"] == "middle":
                move, attack = e["source_id"].rsplit("_", 1)[0], "not attacked"
            else:
                move, attack = None, "not attacked"
            rows.append({"paper": paper, "reading": e["reading"], "arm": e["arm"], "source_id": e["source_id"],
                         "move": move, "sentences": len(us), "worth": rated[e["reading"]]["worth"],
                         "note": rated[e["reading"]]["note"], "late": e["reading"] in late, "attack": attack,
                         "opus": marks(codes["opus"], us), "astra": marks(codes["astra"], us)})

    def sel(paper=None, arm=None, only_rated=False):
        return [r for r in rows if (paper is None or r["paper"] == paper) and (arm is None or r["arm"] == arm)
                and (not only_rated or r["worth"] is not None)]

    scopes = [(p, t) for p, t, _ in PAPERS] + [(None, "Both papers")]
    out = ["# Worth beside the markers: the wager test's 29 readings", "",
           "Written by `score_worth.py` from the PI's worth ratings (stage2/worth/worth_sheet_filled_2.xlsx,",
           "filed unchanged; the PI's first sheet, worth_sheet_filled.xlsx, had",
           "three readings blank), stage2/markers/KEY.json, the four marker",
           "replies in stage2/marker_replies and the system's cards. Arms: system (the generation chats,",
           "which wrote from each paper's record, without the PDF), middle (the reading chats: the same",
           "prompt with the PDF), plain (the plain chats: the PDF and a plain prompt).", "",
           "Worth is the PI's, on the sheet's scale: 0 not worth pursuing, 1 some interest, 2 worth a",
           "scholar's time, 3 a strong opening. **The PI's rating is declared not blind:** the PI had seen every",
           "reply before the PI rated, and the plain arm's form can be told apart (the markers' packs' blinding",
           "is partial). A reading left without a worth is reported as not rated and is left out of every",
           "mean and test.", ""]
    for paper, t, _ in PAPERS:
        if below[paper] is not None:
            out += [f"**{t}'s marker figures are below the bar:** kappa {below[paper]:.3f}, under {GATE:.2f}; they are",
                    f"reported {REPORTED_BELOW_BAR[paper]}, and weigh less than Bechky's.", ""]
    not_rated = [r["reading"] for r in rows if r["worth"] is None]
    out += [f"**Not rated:** {', '.join(not_rated) if not_rated else 'none'}"
            + (" (" + ", ".join(sorted({SHORT[r['arm']] for r in rows if r['worth'] is None})) + " arm)" if not_rated else "")
            + ".", ""]
    late_ids = [r["reading"] for r in rows if r["late"]]
    if late_ids:
        out += [f"**Rated late:** {', '.join(late_ids)} ("
                + ", ".join(sorted({SHORT[r['arm']] for r in rows if r['late']})) + " arm): blank on the PI's first sheet and",
                "rated on the second, after the PI had been told their arm. Each arm's mean is also given",
                "without them.", ""]

    out += ["## 1. Worth by arm", ""]
    for paper, t in scopes:
        out += [f"### {t}", "", "| | " + " | ".join(l for _, l in ARMS) + " |", "|---|---|---|---|"]
        cols = {a: sel(paper, a) for a, _ in ARMS}
        rw = {a: [r["worth"] for r in cols[a] if r["worth"] is not None] for a, _ in ARMS}
        out.append("| readings | " + " | ".join(str(len(cols[a])) for a, _ in ARMS) + " |")
        out.append("| rated | " + " | ".join(str(len(rw[a])) for a, _ in ARMS) + " |")
        out.append("| mean worth | " + " | ".join(f2(mean(rw[a])) for a, _ in ARMS) + " |")
        if any(r["late"] for a, _ in ARMS for r in cols[a]):
            out.append("| mean worth without the readings rated late | " + " | ".join(
                f2(mean([r["worth"] for r in cols[a] if r["worth"] is not None and not r["late"]])) for a, _ in ARMS) + " |")
        if any(len(rw[a]) < len(cols[a]) for a, _ in ARMS):
            def bounds(a):
                k = len(cols[a]) - len(rw[a])
                if not k:
                    return "—"
                return f"{sum(rw[a]) / len(cols[a]):.2f} to {(sum(rw[a]) + 3 * k) / len(cols[a]):.2f}"
            out.append("| mean once all are rated: lowest to highest | " + " | ".join(bounds(a) for a, _ in ARMS) + " |")
        out.append("| rated 0 / 1 / 2 / 3 | " + " | ".join(
            " / ".join(str(rw[a].count(v)) for v in SCALE) for a, _ in ARMS) + " |")
        out.append("| rated 2 or more | " + " | ".join(
            f"{sum(w >= 2 for w in rw[a])} of {len(rw[a])}" for a, _ in ARMS) + " |")
        out.append("| sentences per reading, mean | " + " | ".join(
            f"{mean([r['sentences'] for r in cols[a]]):.1f}" for a, _ in ARMS) + " |")
        out.append("")

    out += ["## 2. Worth beside the markers, by arm", "",
            "Each marker's cell gives Opus 5.5 / GPT 6 Astra. Facts found: the sentences coded R, RI or RA",
            "over those that report (every code but N). Warrant: a U (not printed) or C (contradicted) in the",
            "position of the reading's warrant.", ""]
    for paper, t in scopes:
        out += [f"### {t}" + (" (markers below the bar)" if paper and below[paper] is not None else
                               " (Pratt's markers below the bar)" if paper is None else ""), "",
                "| | " + " | ".join(l for _, l in ARMS) + " |", "|---|---|---|---|"]
        cols = {a: sel(paper, a) for a, _ in ARMS}

        def both(f):
            return " | ".join(f"{f(cols[a], 'opus')} / {f(cols[a], 'astra')}" for a, _ in ARMS)

        out.append("| mean worth (rated) | " + " | ".join(
            f2(mean([r['worth'] for r in cols[a] if r['worth'] is not None])) for a, _ in ARMS) + " |")
        out.append("| facts found | " + both(lambda rs, m: pct(sum(r[m]['found'] for r in rs), sum(r[m]['reporting'] for r in rs))) + " |")
        out.append("| contradicted sentences (C) | " + both(lambda rs, m: sum(r[m]['C'] for r in rs)) + " |")
        out.append("| not printed (U) | " + both(lambda rs, m: sum(r[m]['U'] for r in rs)) + " |")
        out.append("| readings with a U or C as warrant | " + both(lambda rs, m: sum(r[m]['warrant'] for r in rs)) + " |")
        out.append("| rated 2 or more, warrant clear for both markers | " + " | ".join(
            f"{sum(1 for r in cols[a] if r['worth'] is not None and r['worth'] >= 2 and not r['opus']['warrant'] and not r['astra']['warrant'])}"
            f" of {sum(r['worth'] is not None for r in cols[a])} rated" for a, _ in ARMS) + " |")
        out.append("| rated 2 or more, no C for either marker | " + " | ".join(
            f"{sum(1 for r in cols[a] if r['worth'] is not None and r['worth'] >= 2 and not r['opus']['C'] and not r['astra']['C'])}"
            f" of {sum(r['worth'] is not None for r in cols[a])} rated" for a, _ in ARMS) + " |")
        out.append("| the attack: killed / survived | " + " | ".join(
            (f"{sum(r['attack'] == 'killed' for r in cols[a])} / {sum(r['attack'] == 'survived' for r in cols[a])}"
             if a == "system" else "not attacked") for a, _ in ARMS) + " |")
        out.append("")

    out += ["## 3. Reading by reading", "",
            "Sorted by paper, arm and reading. Found: facts found, R, RI and RA over the sentences that",
            "report. Each marker's cell gives Opus 5.5 / GPT 6 Astra. Warrant: yes if that marker codes a U",
            "or C in the warrant position. A worth marked (late) was given on the PI's second sheet, after the PI",
            "had been told the reading's arm.", ""]
    order = {a: i for i, (a, _) in enumerate(ARMS)}
    for paper, t, _ in PAPERS:
        out += [f"### {t}" + (" (markers below the bar)" if below[paper] is not None else ""), "",
                "| reading | arm | move | sentences | worth | the PI's note | found | U | C | warrant | attack |",
                "|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in sorted(sel(paper), key=lambda r: (order[r["arm"]], r["reading"])):
            o, a = r["opus"], r["astra"]
            out.append(f"| {r['reading']} | {SHORT[r['arm']]} | {MOVES.get(r['move'], '—') if r['move'] else '—'} | "
                       f"{r['sentences']} | {'not rated' if r['worth'] is None else str(r['worth']) + (' (late)' if r['late'] else '')} | "
                       f"{(r['note'] or '').replace('|', '/')} | {o['found']}/{o['reporting']} / {a['found']}/{a['reporting']} | "
                       f"{o['U']} / {a['U']} | {o['C']} / {a['C']} | "
                       f"{'yes' if o['warrant'] else 'no'} / {'yes' if a['warrant'] else 'no'} | {r['attack']} |")
        out.append("")

    out += ["## 4. Other cuts", "", "### The attack and worth (the system's readings)", ""]
    for status in ("killed", "survived"):
        rs = [r for r in rows if r["attack"] == status]
        ws = [r["worth"] for r in rs if r["worth"] is not None]
        out.append(f"- {status}: {len(rs)} readings, mean worth {f2(mean(ws))}; "
                   + ", ".join(f"{r['reading']} {r['worth'] if r['worth'] is not None else 'not rated'}" for r in rs) + ".")
    out += ["", "### How far worth goes with facts found, and with length", "",
            f"Spearman's rank correlation over the rated readings; p two-sided, by {SHUFFLES:,} seeded shuffles.",
            "With so few readings, only a large correlation is told apart from chance.", "",
            "| | Pratt | Bechky | both papers |", "|---|---|---|---|"]

    def rho_cell(paper, f, label):
        rs = sel(paper, only_rated=True)
        rho, p = spearman([r["worth"] for r in rs], [f(r) for r in rs], f"{label}-{paper or 'both'}")
        return "—" if rho is None else f"{rho:+.2f} (p {p:.2f}, n {len(rs)})"

    for label, f in [("worth and facts found, Opus 5.5", lambda r: r["opus"]["found"] / r["opus"]["reporting"]),
                     ("worth and facts found, GPT 6 Astra", lambda r: r["astra"]["found"] / r["astra"]["reporting"]),
                     ("worth and sentences in the reading", lambda r: r["sentences"])]:
        out.append(f"| {label} | " + " | ".join(rho_cell(p, f, label) for p, _ in scopes) + " |")
    out += ["", "### The gap in mean worth between arms", "",
            "The first arm's mean worth minus the second's, over the rated readings. p two-sided, by every",
            "relabelling of the two arms' readings within each paper (for both papers together, within each",
            "paper at once).", "", "| arms | Pratt | Bechky | both papers |", "|---|---|---|---|"]
    pairs = [("system", ("middle",), "system against middle (the reading chats)"),
             ("system", ("plain",), "system against plain (the plain chats)"),
             ("system", ("middle", "plain"), "system against middle and plain together"),
             ("middle", ("plain",), "middle (the reading chats) against plain (the plain chats)")]
    for first, second, plabel in pairs:
        cells = []
        for paper, _ in scopes:
            papers = [p for p, _, _ in PAPERS] if paper is None else [paper]
            strata = []
            for p in papers:
                a = [r["worth"] for r in sel(p, first, True)]
                b = [r["worth"] for r in sel(p, only_rated=True) if r["arm"] in second]
                strata.append((a, b))
            gap, pv, n = relabel_test(strata)
            cells.append(f"{gap:+.2f} (p {pv:.3f})")
        out.append(f"| {plabel} | " + " | ".join(cells) + " |")
    out += ["", "### Worth by move (system and middle; the plain arm has no moves)", "",
            "| move | system (the generation chats) | middle (the reading chats) |", "|---|---|---|"]
    for mv in MOVES:
        cell = []
        for a in ("system", "middle"):
            rs = [r for r in rows if r["arm"] == a and r["move"] == mv]
            cell.append(", ".join(f"{r['reading']} {r['worth'] if r['worth'] is not None else 'not rated'}" for r in rs) or "—")
        out.append(f"| {MOVES[mv]} | " + " | ".join(cell) + " |")
    out.append("")
    with open(os.path.join(out_dir, "WORTH_RESULTS.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    with open(os.path.join(out_dir, "worth_joined.json"), "w", encoding="utf-8") as fh:
        json.dump({"sheet": SHEET, "first_sheet": FIRST, "below_bar": {p: (round(v, 3) if v is not None else None) for p, v in below.items()},
                   "readings": rows}, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
