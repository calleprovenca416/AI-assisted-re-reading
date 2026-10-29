"""
Read the judge chats' answers back (T31) and count them. Written 13 Oct 2026.

Each reply is one part of one paper's table: a JSON object
{"part": 1 or 2, "answers": [{"row", "reason", "page", "answer"}, ...]}, saved
as the chat gave it, or in pieces that are joined in the order given. The
script takes the first "{" to the last "}" of the joined text, refuses a
reply whose rows are not exactly the table's ids in the table's order, or
whose answer is not yes, no or unclear, and checks that the table as it
stands in the folder is the one the key records.

What it writes (for nobody), from the key and the answers:
- per paper and part, the answers counted by whose statement it was (coder 1,
  coder 2, both codings, neither): the statements both codings made and those
  neither made show how the judge leans;
- per row where the codings differ, the two answers side by side, sorted into:
  both statements held; only coder 1's; only coder 2's; neither; and any
  unclear;
- the longest span a reason quotes, in words.

usage (from the folder; -B leaves no cache):
  python3 -B read_judge_answers.py --key=judge_key.json --out=JUDGE_RESULTS.md \
      --json=judge_results.json PAPER:PART=reply[+piece...] ...
  e.g. pratt_2000:1=replies/reply_43_judge_pratt_part1.json
"""
import collections
import hashlib
import json
import os
import re
import sys

ANSWERS = ("yes", "no", "unclear")


def read_reply(paths):
    text = "".join(open(p, encoding="utf-8").read() for p in paths)
    a, b = text.find("{"), text.rfind("}")
    if a < 0 or b < a:
        raise SystemExit(f"{paths}: no JSON object found")
    try:
        return json.loads(text[a:b + 1])
    except json.JSONDecodeError as e:
        raise SystemExit(f"{paths}: not valid JSON once joined ({e})")


def longest_quote(s):
    """The longest span a reason quotes, in words. A note that stands for a paper's words, such as "[12 words of
    Pratt (2000), p. 470]", counts as the words it stands for."""
    spans = re.findall(r"[\"“]([^\"”]+)[\"”]", s or "")
    note = re.compile(r"\[(\d+) words? of [^\]]+\]")
    return max((len(x.split()) + sum(int(m.group(1)) - len(m.group(0).split()) for m in note.finditer(x))
                for x in spans), default=0)


def main(argv):
    opts, replies = {}, []
    for a in argv:
        if a.startswith("--"):
            k, _, v = a[2:].partition("=")
            opts[k] = v
        else:
            spec, _, files = a.partition("=")
            pid, _, part = spec.partition(":")
            replies.append((pid, part, files.split("+")))
    if not {"key", "out", "json"} <= set(opts) or not replies:
        raise SystemExit(__doc__)
    key = json.load(open(opts["key"], encoding="utf-8"))
    here = os.path.dirname(os.path.abspath(opts["key"]))
    results, lines = {}, ["# The judges' answers", ""]
    lines.append("Written by `read_judge_answers.py` from `judge_key.json` and the replies "
                 "named below. Nothing here changes a code or a figure of either coding.")
    lines.append("")
    for pid, part, files in replies:
        p = key["papers"][pid]["parts"][part]
        table = os.path.join(here, p["file"])
        if hashlib.sha256(open(table, "rb").read()).hexdigest() != p["sha256"]:
            raise SystemExit(f"{p['file']} is not the table the key records")
        rep = read_reply(files)
        if str(rep.get("part")) != str(part):
            raise SystemExit(f"{files}: says part {rep.get('part')}, given as part {part}")
        ans = rep.get("answers") or []
        ids = [s["id"] for s in p["statements"]]
        got = [str(x.get("row", "")).strip() for x in ans]
        if got != ids:
            missing = [i for i in ids if i not in got]
            extra = [i for i in got if i not in ids]
            raise SystemExit(f"{pid} part {part}: rows differ from the table's "
                             f"(missing {missing[:10]}, extra {extra[:10]}, "
                             f"{'same set, other order' if not missing and not extra else ''})")
        bad = [x["row"] for x in ans if str(x.get("answer", "")).strip().lower() not in ANSWERS]
        if bad:
            raise SystemExit(f"{pid} part {part}: answers not yes, no or unclear: {bad[:10]}")
        no_reason = [x["row"] for x in ans if not str(x.get("reason") or "").strip()]
        by_id = {x["row"]: x for x in ans}
        recs = []
        for s in p["statements"]:
            x = by_id[s["id"]]
            recs.append(dict(s, answer=str(x["answer"]).strip().lower(),
                             reason=str(x.get("reason") or "").strip(),
                             page=x.get("page")))
        results.setdefault(pid, {})[part] = recs
        q = max((longest_quote(r["reason"]) for r in recs), default=0)

        lines.append(f"## {pid}, part {part}")
        lines.append("")
        lines.append(f"- Reply: {', '.join(os.path.basename(f) for f in files)}; "
                     f"{len(ans)} answers for the table's {len(ids)} rows, in its order. "
                     f"Without a reason: {len(no_reason)}. Longest quoted span in a reason: {q} words.")
        lines.append("")
        lines.append("| whose statement | yes | no | unclear | n |")
        lines.append("|---|---|---|---|---|")
        for who in ("coder 1", "coder 2", "both", "neither"):
            c = collections.Counter(r["answer"] for r in recs if r["who"] == who)
            n = sum(c.values())
            if n:
                lines.append(f"| {who} | {c['yes']} | {c['no']} | {c['unclear']} | {n} |")
        lines.append("")
        rows = collections.defaultdict(dict)
        for r in recs:
            if r["differ"]:
                rows[(r["field"],) + tuple(r["key"])][r["who"]] = r
        kinds = collections.Counter()
        listing = []
        for k, d in sorted(rows.items()):
            a1, a2 = d["coder 1"]["answer"], d["coder 2"]["answer"]
            if "unclear" in (a1, a2):
                kind = "unclear"
            elif a1 == "yes" and a2 == "yes":
                kind = "both held"
            elif a1 == "yes":
                kind = "only coder 1's held"
            elif a2 == "yes":
                kind = "only coder 2's held"
            else:
                kind = "neither held"
            kinds[kind] += 1
            listing.append((kind, k, d))
        lines.append(f"**Rows where the codings differ: {len(rows)}.** " +
                     "; ".join(f"{k}: {kinds[k]}" for k in ("both held", "only coder 1's held",
                                                           "only coder 2's held", "neither held",
                                                           "unclear") if kinds[k]) + ".")
        lines.append("")
        lines.append("| row | field | coder 1 | judge | coder 2 | judge | sorted as |")
        lines.append("|---|---|---|---|---|---|---|")
        for kind, k, d in listing:
            lines.append(f"| {' → '.join(k[1:])} | {k[0]} | {d['coder 1']['code']} | "
                         f"{d['coder 1']['answer']} | {d['coder 2']['code']} | {d['coder 2']['answer']} | {kind} |")
        lines.append("")
    open(opts["out"], "w", encoding="utf-8").write("\n".join(lines).rstrip("\n") + "\n")
    open(opts["json"], "w", encoding="utf-8").write(
        json.dumps({"key_seed": key["seed"], "results": results}, indent=1, ensure_ascii=False) + "\n")
    print("wrote", opts["out"], "and", opts["json"])


if __name__ == "__main__":
    main(sys.argv[1:])
