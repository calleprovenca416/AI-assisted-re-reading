"""
Score the two marker replies of T32 (13 Oct 2026), in one command, on the wager
test's scorer, `score_markers.py`, whose checks, kappa and rates it uses unchanged.

    python3 -B score_places_markers.py <out_dir>

Reads `places_packs_key.json` and the two replies, each filed unchanged under its
chat's number:

    reply_47_mark_places_opus.json     Opus 5.5 (chat 47)
    reply_48_mark_places_astra.json    GPT 6 Astra (chat 48)

Each reply is checked against the key and `MARKING.md`'s field rules as the wager
test's were (score_markers.check). Then the two markers' agreement: observed
agreement and Cohen's kappa on the seven codes, with the confusion matrix, and on
four groups as a diagnostic only. Rates are reported only if kappa on the seven
codes is at least 0.60, the wager test's bar. Where they are, for each arm (places
given, chat 45; places found, chat 46) and for each reading, and for each marker:
the sentences, those that report (every code but N), the resolution rate (R, RI
and RA over those that report), the strict rate (R over those that report), P
with the share whose reasoning is stated, U and C each by position, drift, and
whether a U or C stands in the warrant position.

Writes <out_dir>/PLACES_MARKER_RESULTS.md and <out_dir>/places_marker_results.json.
Both say which chat wrote which reading, so both are for nobody until the PI's
worth sheet is back. The agreement section alone says nothing of it.
"""
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import score_markers as sm  # noqa: E402

KEY = "places_packs_key.json"
WHO = {"opus": ("reply_47_mark_places_opus.json", 47), "astra": ("reply_48_mark_places_astra.json", 48)}
ARMS = [("places given", "places given (chat 45)"), ("places found", "places found (chat 46)")]


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: python3 -B score_places_markers.py <out_dir>")
    out_dir = sys.argv[1]
    os.makedirs(out_dir, exist_ok=True)
    key = json.load(open(os.path.join(HERE, KEY), encoding="utf-8"))
    entries = key["readings"]
    units = [u["unit"] for e in entries for u in e["units"]]
    out = ["# The markers of T32: agreement and rates", "",
           "Written by `score_places_markers.py` from `reply_47_mark_places_opus.json`,",
           "`reply_48_mark_places_astra.json` and `places_packs_key.json`, with the wager test's",
           "checks, kappa and rates (`score_markers.py`). It says which chat wrote which reading:",
           "for nobody until the PI's worth sheet is back. Arms: places given (chat 45, the readings",
           "at the four places), places found (chat 46, the readings at places it found itself).",
           f"Rates are reported only if kappa on the seven codes is at least {sm.GATE:.2f}.", "",
           "## The replies", ""]
    codes, summary = {}, {"replies": {}}
    for m, (fname, chat) in WHO.items():
        path = os.path.join(HERE, fname)
        obj = json.loads(open(path, encoding="utf-8").read().strip())
        codes[m] = {c["unit"]: c for c in obj["codes"]}
        problems, rules, longest = sm.check(obj, units)
        k = collections.Counter(c["code"] for c in obj["codes"])
        out.append(f"- **Chat {chat}, {sm.NAMES[m]}** (`{fname}`): paper given as \"{obj.get('paper')}\"; "
                   f"{len(obj['codes'])} codes for the key's {len(units)} sentences; "
                   + ", ".join(f"{c} {k[c]}" for c in sm.CODES) + ".")
        out.append("  " + ("Units: as the key, in order." if not problems else "Units: " + "; ".join(problems)))
        if rules:
            out.append("  Field rules not followed: " + "; ".join(
                f"{r} ({len(us)}: {', '.join(us[:6])}{' …' if len(us) > 6 else ''})"
                for r, us in sorted(rules.items())) + ".")
        else:
            out.append("  Field rules: all followed.")
        out.append(f"  Longest quoted span in its notes: {longest} words.")
        summary["replies"][m] = {"file": fname, "codes": dict(k), "problems": problems,
                                 "rules": {r: us for r, us in rules.items()}, "longest_quote": longest}
    pairs = [(codes["opus"][u]["code"], codes["astra"][u]["code"]) for u in units]
    po, k7 = sm.kappa(pairs, sm.CODES)
    po4, k4 = sm.kappa([(sm.GROUP[a], sm.GROUP[b]) for a, b in pairs], sm.GROUPS)
    cm = collections.Counter(pairs)
    summary["agreement"] = {"sentences": len(units), "same": sum(a == b for a, b in pairs),
                            "observed": po, "kappa7": k7, "observed4": po4, "kappa4": k4}
    out += ["", "## Agreement", "",
            f"{len(units)} sentences. Seven codes: the markers agree on {sum(a == b for a, b in pairs)} "
            f"({po:.3f}); Cohen's kappa **{k7:.3f}**. Four groups (N; R, RI, RA; P; U, C), a diagnostic "
            f"only: agreement {po4:.3f}, kappa {k4:.3f}.", "",
            "Rows: Opus 5.5; columns: GPT 6 Astra.", "",
            "| | " + " | ".join(sm.CODES) + " |", "|---|" + "---|" * len(sm.CODES)]
    for a in sm.CODES:
        out.append(f"| **{a}** | " + " | ".join(str(cm[(a, b)]) if cm[(a, b)] else "·" for b in sm.CODES) + " |")
    out += ["", "The cells off the diagonal with the most sentences:", ""]
    for (a, b), v in sorted(((p, v) for p, v in cm.items() if p[0] != p[1]), key=lambda x: (-x[1], x[0]))[:6]:
        out.append(f"- Opus {a}, Astra {b}: {v}")
    out.append("")
    if k7 < sm.GATE:
        out += [f"**Rates withheld:** kappa {k7:.3f} is below {sm.GATE:.2f}.", ""]
        summary["rates"] = None
    else:
        out += ["## Rates by arm", "", "Each cell gives Opus 5.5 / GPT 6 Astra.", "",
                "| | " + " | ".join(label for _, label in ARMS) + " |", "|---|---|---|"]
        rows, per = {}, {}
        for arm, _ in ARMS:
            us = [u["unit"] for e in entries if e["arm"] == arm for u in e["units"]]
            rd = {e["reading"]: [u["unit"] for u in e["units"]] for e in entries if e["arm"] == arm}
            for m in WHO:
                rows.setdefault(m, {})[arm] = sm.arm_rates(codes[m], us, rd)

        def cell(f):
            return " | ".join(f"{f(rows['opus'][a])} / {f(rows['astra'][a])}" for a, _ in ARMS)
        out.append("| readings | " + " | ".join(str(rows["opus"][a]["readings"]) for a, _ in ARMS) + " |")
        out.append("| sentences | " + " | ".join(str(rows["opus"][a]["sentences"]) for a, _ in ARMS) + " |")
        out.append("| sentences that report (not N) | " + cell(lambda r: r["reporting"]) + " |")
        out.append("| resolution rate (R, RI, RA) | " + cell(lambda r: sm.pct(r["R"] + r["RI"] + r["RA"], r["reporting"])) + " |")
        out.append("| strict rate (R) | " + cell(lambda r: sm.pct(r["R"], r["reporting"])) + " |")
        out.append("| P (reasoning stated) | " + cell(lambda r: f"{r['P']} ({r['P_stated']})") + " |")
        for code in ("U", "C"):
            out.append(f"| {code}: warrant, mechanism, illustration | " + cell(
                lambda r, code=code: f"{r[code]}: " + ", ".join(str(r['pos'][code][p]) for p in sm.POSITIONS)) + " |")
        out.append("| drift | " + cell(lambda r: r["drift"]) + " |")
        out.append("| readings with a U or C as warrant | " + cell(lambda r: len(r["fatal"])) + " |")
        out += ["", "## By reading", "", "Each cell gives Opus 5.5 / GPT 6 Astra.", "",
                "| reading | chat, reading | sentences | report | resolution | strict | P (stated) | U | C | drift | U or C as warrant |",
                "|---|---|---|---|---|---|---|---|---|---|---|"]
        for e in entries:
            us = [u["unit"] for u in e["units"]]
            r = {m: sm.arm_rates(codes[m], us, {e["reading"]: us}) for m in WHO}

            def two(f):
                return f"{f(r['opus'])} / {f(r['astra'])}"
            out.append(f"| {e['reading']} | {e['chat']}, {e['source_id']} | {len(us)} | "
                       f"{two(lambda x: x['reporting'])} | "
                       f"{two(lambda x: sm.pct(x['R'] + x['RI'] + x['RA'], x['reporting']))} | "
                       f"{two(lambda x: sm.pct(x['R'], x['reporting']))} | "
                       f"{two(lambda x: str(x['P']) + ' (' + str(x['P_stated']) + ')')} | "
                       f"{two(lambda x: x['U'])} | {two(lambda x: x['C'])} | {two(lambda x: x['drift'])} | "
                       f"{two(lambda x: 'yes' if x['fatal'] else 'no')} |")
            per[e["reading"]] = {"chat": e["chat"], "source_id": e["source_id"],
                                 "rates": {m: {k2: v for k2, v in r[m].items() if k2 not in ("pos", "fatal")}
                                           | {"pos": {c: dict(r[m]["pos"][c]) for c in ("U", "C")},
                                              "warrant_U_or_C": bool(r[m]["fatal"])} for m in WHO}}
        out.append("")
        summary["rates"] = {"by_arm": {m: {a: {k2: v for k2, v in rows[m][a].items() if k2 not in ("pos",)}
                                              | {"pos": {c: dict(rows[m][a]["pos"][c]) for c in ("U", "C")}}
                                              for a, _ in ARMS} for m in WHO},
                            "by_reading": per}
    with open(os.path.join(out_dir, "PLACES_MARKER_RESULTS.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out).rstrip("\n") + "\n")
    with open(os.path.join(out_dir, "places_marker_results.json"), "w", encoding="utf-8") as fh:
        fh.write(json.dumps(summary, indent=1, ensure_ascii=False) + "\n")
    print(f"kappa {k7:.3f} on {len(units)} sentences; wrote PLACES_MARKER_RESULTS.md and places_marker_results.json")


if __name__ == "__main__":
    main()
