"""
Score the wager test's marker replies (T29, step 5), in one command.

    python3 score_markers.py <out_dir>

Reads stage2/markers/KEY.json and the four marker replies in stage2/marker_replies,
each filed unchanged under its chat's number:

    reply_39_mark_pratt_opus.json            Pratt, Opus 5.5 (chat 39)
    reply_40_mark_pratt_astra.json           Pratt, GPT 6 Astra (chat 40)
    reply_41_mark_bechky_opus_as_sent.txt    Bechky, Opus 5.5 (chat 41)
    reply_42_mark_bechky_astra.json          Bechky, GPT 6 Astra (chat 42)

A reply wrapped in a ```json fence has the fence dropped. Chat 41's reply came in two
blocks: the first broke off inside an entry, the chat wrote one line saying so and how
to join them, and the second block restarts at that entry and closes the object. It is
joined by that rule: the first block without its broken last entry line, then the
second block. The broken line must be the start of the second block's first line, or
the join is refused. The joined object is written to <out_dir> as
reply_41_mark_bechky_opus_joined.json.

Each reply is checked against the key: one code per numbered sentence, in the key's
order, from N, R, RI, RA, P, U, C; and against MARKING.md's field rules (page null for
N, RA and U; position given for U and C only; reasoning_stated given for P only; drift
false for N; a note for every RA, P, U and C). A deviation is counted and listed, and
the code is used as given. Quoted spans in the notes are counted: none may run past
eight words.

Then, for each paper, the two markers' agreement: observed agreement and Cohen's kappa
on the seven codes, with the confusion matrix; kappa on four groups (N; R, RI, RA;
P; U, C), as a diagnostic only; and, by arm, the sentences on which they agree.

A paper's rates are reported only if its kappa on the seven codes is at least 0.60
(SCORING_SHEET.md: no rate below kappa 0.60 between markers); each paper is judged
on its own. Below the bar, a paper's rates are reported only where it has been
decided so (REPORTED_BELOW_BAR), and are then marked as below the bar: Pratt, by
a decision of 11 Oct 2026, made after the result. Where rates are reported, for each arm and each
marker: the sentences, those that report (every code but N), the resolution rate
(R, RI and RA over those that report), the strict rate (R over those that report), P
with the share whose reasoning is stated, U and C each by position, drift, and the
readings with a U or C in the warrant position.

Writes <out_dir>/RESULTS.md and the joined reply. Names the arms as the key does:
system (the generation chats), middle (the reading chats), plain (the plain chats).
"""
import collections
import json
import os
import re
import sys

REPLIES = "stage2/marker_replies"
KEY = "stage2/markers/KEY.json"
MARKERS = {
    "pratt": {"opus": ("reply_39_mark_pratt_opus.json", 39), "astra": ("reply_40_mark_pratt_astra.json", 40)},
    "bechky": {"opus": ("reply_41_mark_bechky_opus_as_sent.txt", 41), "astra": ("reply_42_mark_bechky_astra.json", 42)},
}
NAMES = {"opus": "Opus 5.5", "astra": "GPT 6 Astra"}
CODES = ["N", "R", "RI", "RA", "P", "U", "C"]
GROUP = {"N": "N", "R": "R, RI, RA", "RI": "R, RI, RA", "RA": "R, RI, RA", "P": "P", "U": "U, C", "C": "U, C"}
GROUPS = ["N", "R, RI, RA", "P", "U, C"]
ARMS = [("system", "system (generation chats)"), ("middle", "middle (reading chats)"),
        ("plain", "plain (plain chats)")]
POSITIONS = ["warrant", "mechanism", "illustration"]
GATE = 0.60
REPORTED_BELOW_BAR = {
    "pratt": "by a decision of 11 Oct 2026, made after the result",
}


def unfence(text):
    t = text.strip()
    if t.startswith("```"):
        t = t.split("\n", 1)[1].rsplit("```", 1)[0]
    return t


def load(path):
    text = open(path, encoding="utf-8").read()
    fences = [i for i, l in enumerate(text.split("\n")) if l.strip().startswith("```")]
    if len(fences) <= 2:
        return json.loads(unfence(text)), None
    lines = text.split("\n")
    if len(fences) != 3:
        raise SystemExit(f"{path}: {len(fences)} fence lines; expected 2, or 3 for a reply in two blocks")
    f1, f2, f3 = fences
    entries = [i for i in range(f1 + 1, f2) if lines[i].lstrip().startswith('{"unit"')]
    last = entries[-1]
    broken = lines[last].rstrip()
    if broken.endswith(("},", "}")):
        raise SystemExit(f"{path}: the first block's last entry is complete; no join rule applies")
    first, second = lines[f1 + 1:last], lines[f2 + 1:f3]
    if not second or not second[0].startswith(broken):
        raise SystemExit(f"{path}: the broken line is not the start of the second block's first line")
    between = [l for l in lines[last + 1:f2] if l.strip()]
    obj = json.loads("\n".join(first + second))
    return obj, {"broken_unit": json.loads(second[0].rstrip().rstrip(","))["unit"],
                 "lines_between": len(between)}


def quoted_spans(text):
    spans = []
    for a, b in (("‘", "’"), ("“", "”"), ('"', '"')):
        spans += re.findall(re.escape(a) + r"([^" + re.escape(b) + r"]{1,400}?)" + re.escape(b), text)
    spans += re.findall(r"(?:(?<=^)|(?<=[\s(\[]))'([^']{1,400}?)'(?=[\s.,;:!?)\]]|$)", text)
    return spans


def check(reply, units):
    got = [c.get("unit") for c in reply.get("codes", [])]
    problems = []
    if got != units:
        missing = [u for u in units if u not in got]
        extra = [u for u in got if u not in units]
        problems.append(f"units differ from the key: missing {missing}, extra {extra}, "
                        f"order {'differs' if not missing and not extra else 'n/a'}")
    rules = collections.defaultdict(list)
    longest = 0
    for c in reply.get("codes", []):
        u, code = c.get("unit"), c.get("code")
        if code not in CODES:
            rules["code not one of the seven"].append(u)
            continue
        if code in ("N", "RA", "U") and c.get("page") is not None:
            rules["page given for N, RA or U"].append(u)
        if code not in ("N", "RA", "U") and not c.get("page"):
            rules["no page for R, RI, P or C"].append(u)
        if code in ("U", "C") and c.get("position") not in POSITIONS:
            rules["no valid position for U or C"].append(u)
        if code not in ("U", "C") and c.get("position") is not None:
            rules["position given for a code other than U or C"].append(u)
        if code == "P" and not isinstance(c.get("reasoning_stated"), bool):
            rules["no reasoning_stated for P"].append(u)
        if code != "P" and c.get("reasoning_stated") is not None:
            rules["reasoning_stated given for a code other than P"].append(u)
        if code == "N" and c.get("drift"):
            rules["drift true for N"].append(u)
        if code in ("RA", "P", "U", "C") and not (c.get("note") or "").strip():
            rules["no note for RA, P, U or C"].append(u)
        for s in quoted_spans(c.get("note") or ""):
            longest = max(longest, len(s.split()))
    return problems, rules, longest


def kappa(pairs, cats):
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    ca = collections.Counter(a for a, _ in pairs)
    cb = collections.Counter(b for _, b in pairs)
    pe = sum(ca[c] * cb[c] for c in cats) / (n * n)
    return po, (po - pe) / (1 - pe)


def pct(a, b):
    return f"{100 * a / b:.0f}%" if b else "—"


def arm_rates(codes, units_of_arm, readings_of_arm):
    cs = [codes[u] for u in units_of_arm]
    k = collections.Counter(c["code"] for c in cs)
    rep = sum(v for c, v in k.items() if c != "N")
    p_stated = sum(1 for c in cs if c["code"] == "P" and c.get("reasoning_stated") is True)
    pos = {code: collections.Counter(c.get("position") for c in cs if c["code"] == code) for code in ("U", "C")}
    drift = sum(1 for c in cs if c.get("drift"))
    fatal = sorted({r for r, us in readings_of_arm.items()
                    if any(codes[u]["code"] in ("U", "C") and codes[u].get("position") == "warrant" for u in us)})
    return {"sentences": len(cs), "reporting": rep, "R": k["R"], "RI": k["RI"], "RA": k["RA"],
            "P": k["P"], "P_stated": p_stated, "U": k["U"], "C": k["C"], "pos": pos,
            "drift": drift, "fatal": fatal, "readings": len(readings_of_arm)}


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: python3 score_markers.py <out_dir>")
    out_dir = sys.argv[1]
    os.makedirs(out_dir, exist_ok=True)
    key = json.load(open(KEY))
    out = ["# The wager test's markers: agreement and rates", "",
           "Written by `score_markers.py` from the four marker replies in stage2/marker_replies and",
           "stage2/markers/KEY.json. Arms: system (the readings from the generation chats, written",
           "from each paper's record), middle (the reading chats: the same prompt with the PDF),",
           "plain (the plain chats: the PDF and a plain prompt). A paper's rates are reported only",
           f"if its kappa on the seven codes is at least {GATE:.2f}, or, below it, where it has been",
           "decided so, and then they are marked as below the bar.", ""]
    for paper, who in MARKERS.items():
        entries = key["papers"][paper]
        units = [u["unit"] for e in entries for u in e["units"]]
        replies, codes = {}, {}
        out += [f"## {paper.capitalize()}", "", "### The replies", ""]
        for m, (fname, chat) in who.items():
            obj, join = load(os.path.join(REPLIES, fname))
            replies[m] = obj
            codes[m] = {c["unit"]: c for c in obj["codes"]}
            problems, rules, longest = check(obj, units)
            if join:
                with open(os.path.join(out_dir, "reply_41_mark_bechky_opus_joined.json"), "w", encoding="utf-8") as fh:
                    json.dump(obj, fh, indent=1, ensure_ascii=False)
                    fh.write("\n")
            k = collections.Counter(c["code"] for c in obj["codes"])
            line = (f"- **Chat {chat}, {NAMES[m]}** (`{fname}`): paper given as \"{obj.get('paper')}\"; "
                    f"{len(obj['codes'])} codes for the key's {len(units)} sentences; "
                    + ", ".join(f"{c} {k[c]}" for c in CODES) + ".")
            if join:
                line += (f" Came in two blocks, joined at {join['broken_unit']} by the chat's own rule; "
                         f"{join['lines_between']} line of the chat's between them is not part of the object.")
            out.append(line)
            out.append("  " + ("Units: as the key, in order." if not problems else "Units: " + "; ".join(problems)))
            if rules:
                out.append("  Field rules not followed: " + "; ".join(
                    f"{r} ({len(us)}: {', '.join(us[:6])}{' …' if len(us) > 6 else ''})" for r, us in sorted(rules.items())) + ".")
            else:
                out.append("  Field rules: all followed.")
            out.append(f"  Longest quoted span in its notes: {longest} words.")
        pairs = [(codes["opus"][u]["code"], codes["astra"][u]["code"]) for u in units]
        po, k7 = kappa(pairs, CODES)
        po4, k4 = kappa([(GROUP[a], GROUP[b]) for a, b in pairs], GROUPS)
        cm = collections.Counter(pairs)
        out += ["", "### Agreement", "",
                f"{len(units)} sentences. Seven codes: the markers agree on {sum(a == b for a, b in pairs)} "
                f"({po:.3f}); Cohen's kappa **{k7:.3f}**. Four groups (N; R, RI, RA; P; U, C), a diagnostic "
                f"only: agreement {po4:.3f}, kappa {k4:.3f}.", "",
                "Rows: Opus 5.5; columns: GPT 6 Astra.", "",
                "| | " + " | ".join(CODES) + " |", "|---|" + "---|" * len(CODES)]
        for a in CODES:
            out.append(f"| **{a}** | " + " | ".join(str(cm[(a, b)]) if cm[(a, b)] else "·" for b in CODES) + " |")
        out += ["", "By arm, the sentences on which the two markers give the same code (agreement only,",
                "not a rate):", ""]
        for arm, label in ARMS:
            us = [u["unit"] for e in entries if e["arm"] == arm for u in e["units"]]
            same = sum(codes["opus"][u]["code"] == codes["astra"][u]["code"] for u in us)
            out.append(f"- {label}: {same} of {len(us)} ({pct(same, len(us))})")
        out.append("")
        if k7 < GATE:
            if paper in REPORTED_BELOW_BAR:
                out += [f"**Below the bar:** kappa {k7:.3f} is below {GATE:.2f}. The rates below are reported",
                        f"{REPORTED_BELOW_BAR[paper]}, as they stand: they rest on codes the two markers",
                        "agree on less than the bar requires, and weigh less than a paper's above it.",
                        "The cells off the diagonal with the most sentences:", ""]
            else:
                out += [f"**Rates withheld:** kappa {k7:.3f} is below {GATE:.2f}. The cells off the diagonal with",
                        "the most sentences:", ""]
            for (a, b), v in sorted(((p, v) for p, v in cm.items() if p[0] != p[1]), key=lambda x: -x[1])[:5]:
                out.append(f"- Opus {a}, Astra {b}: {v}")
            out.append("")
            if paper not in REPORTED_BELOW_BAR:
                continue
        out += ["### Rates by arm" + (" (below the bar)" if k7 < GATE else ""), "",
                "Each cell gives Opus 5.5 / GPT 6 Astra.", "",
                "| | " + " | ".join(label for _, label in ARMS) + " |", "|---|---|---|---|"]
        rows = collections.OrderedDict()
        for arm, _ in ARMS:
            us = [u["unit"] for e in entries if e["arm"] == arm for u in e["units"]]
            rd = {e["reading"]: [u["unit"] for u in e["units"]] for e in entries if e["arm"] == arm}
            for m in ("opus", "astra"):
                rows.setdefault(m, {})[arm] = arm_rates(codes[m], us, rd)
        def cell(f):
            return " | ".join(f"{f(rows['opus'][a])} / {f(rows['astra'][a])}" for a, _ in ARMS)
        out.append("| readings | " + " | ".join(str(rows["opus"][a]["readings"]) for a, _ in ARMS) + " |")
        out.append("| sentences | " + " | ".join(str(rows["opus"][a]["sentences"]) for a, _ in ARMS) + " |")
        out.append("| sentences that report (not N) | " + cell(lambda r: r["reporting"]) + " |")
        out.append("| resolution rate (R, RI, RA) | " + cell(lambda r: pct(r["R"] + r["RI"] + r["RA"], r["reporting"])) + " |")
        out.append("| strict rate (R) | " + cell(lambda r: pct(r["R"], r["reporting"])) + " |")
        out.append("| P (reasoning stated) | " + cell(lambda r: f"{r['P']} ({r['P_stated']})") + " |")
        for code in ("U", "C"):
            out.append(f"| {code}: warrant, mechanism, illustration | " + cell(
                lambda r, code=code: f"{r[code]}: " + ", ".join(str(r['pos'][code][p]) for p in POSITIONS)) + " |")
        out.append("| drift | " + cell(lambda r: r["drift"]) + " |")
        out.append("| readings with a U or C as warrant | " + cell(lambda r: len(r["fatal"])) + " |")
        out.append("")
    with open(os.path.join(out_dir, "RESULTS.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    print("\n".join(out))


if __name__ == "__main__":
    main()
