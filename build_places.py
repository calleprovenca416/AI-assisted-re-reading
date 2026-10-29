"""
Write PLACES.md, the places that the readings chat of the system's arm starts
from (T32), and its key. Written 13 Oct 2026.

Each place is a link of the record: a claim, with what it says is affected and
which way, and a passage, by its page and its stub as a pointer; and two
readings of what the passage shows, in the fixed wording of `JUDGING.md`'s
tables (`build_judge_table.py`), named A and B. The links are given on the
command line. One random.Random(seed): the places' order, then, place by place,
which reading is A. The key (for nobody) says which code each reading states.

usage (from the folder; -B leaves no cache):
  python3 -B build_places.py --seed=N --paper=PAPER_ID --out=DIR FRAG:CLAIM=CODE/CODE ...
"""
import hashlib
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import build_judge_table as bjt   # noqa: E402


def main(argv):
    opts, links = {}, []
    for a in argv:
        if a.startswith("--"):
            k, _, v = a[2:].partition("=")
            opts[k] = v
        else:
            link, _, codes = a.partition("=")
            fid, _, cid = link.partition(":")
            links.append((fid, cid, codes.split("/")))
    if not {"seed", "paper", "out"} <= set(opts) or not links:
        raise SystemExit(__doc__)
    pid = opts["paper"]
    corpus = json.load(open(os.path.join(HERE, f"{pid}_v1.json"), encoding="utf-8"))
    claims = {c["claim_id"]: c for c in corpus["claims"]}
    frags = {f["fragment_id"]: f for f in corpus["fragments"]}
    have = {(l["fragment_id"], l["claim_id"]) for l in corpus["claim_links"]}
    rng = random.Random(int(opts["seed"]))
    order = list(links)
    rng.shuffle(order)
    lines = ["# Places", "",
             f"{len(order)} places in the paper. Each gives a claim the paper makes, as a reader "
             "summed it up, with what it says is affected and which way; a passage of the paper, "
             "by its page and a reader's summary that points to it; and two readings of what the "
             "passage shows. Both readings have fair ground in the paper. Where a summary and the "
             "paper differ, go by the paper.", ""]
    key = {"what": "the key to PLACES.md: for no chat", "seed": int(opts["seed"]),
           "paper": pid, "corpus_sha256": hashlib.sha256(
               open(os.path.join(HERE, f"{pid}_v1.json"), "rb").read()).hexdigest(), "places": []}
    for n, (fid, cid, codes) in enumerate(order, 1):
        if (fid, cid) not in have:
            raise SystemExit(f"{fid} to {cid} is not a link of the record")
        if len(codes) != 2 or codes[0] == codes[1]:
            raise SystemExit(f"{fid}:{cid}: give two different codes")
        c, fr = claims[cid], frags[fid]
        ab = list(codes)
        if rng.random() < 0.5:
            ab.reverse()
        lines.append(f"## Place {n}")
        lines.append("")
        lines.append(bjt.claim_head(c))
        if bjt.has_outcome(c):
            lines.append("")
            lines.append(f"**What it says is affected:** {bjt.clean(c['outcome'])}. "
                         f"**Which way:** {bjt.clean(c.get('asserted_direction'))}.")
        lines.append("")
        lines.append(f"**The passage:** {bjt.clean(fr.get('location'))}, the one this summary points to: "
                     f"\"{bjt.clean(fr.get('stub'))}\"")
        lines.append("")
        for lab, code in zip("AB", ab):
            lines.append(f"**Reading {lab}:** {bjt.direction_statement(code, c)}")
            lines.append("")
        key["places"].append({"place": f"Place {n}", "link": [fid, cid], "A": ab[0], "B": ab[1]})
    text = "\n".join(lines).rstrip("\n") + "\n"
    os.makedirs(opts["out"], exist_ok=True)
    open(os.path.join(opts["out"], "PLACES.md"), "w", encoding="utf-8").write(text)
    key["places_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    open(os.path.join(opts["out"], "places_key.json"), "w", encoding="utf-8").write(
        json.dumps(key, indent=1, ensure_ascii=False) + "\n")
    print("PLACES.md", key["places_sha256"][:16], "places", len(order))


if __name__ == "__main__":
    main(sys.argv[1:])
