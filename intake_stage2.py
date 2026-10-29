"""
Take a generator's output, write one file per card, run the mechanical checks,
and summarise. Declined entries are kept: a decline is a finding.

    python3 intake_stage2.py <generator_output.json> <corpus.json> <cards_dir>
"""
import json
import os
import sys

from schema import load
from card import run

out_path, corpus_path, cards_dir = sys.argv[1:4]
out = json.load(open(out_path))
c = load(corpus_path)
os.makedirs(cards_dir, exist_ok=True)

rows = []
for card in out.get("cards", []):
    path = os.path.join(cards_dir, f"{card['card_id']}.json")
    json.dump(card, open(path, "w"), indent=2)
    r = run(card, c)
    json.dump(r, open(path.replace(".json", ".checks.json"), "w"), indent=2)
    rows.append((card["card_id"], card.get("move"), r["killed_by"],
                 r["restatement"]["share_new"], r["restatement"]["failed"]))

print(f"{len(rows)} card(s), {len(out.get('declined', []))} declined\n")
print(f"  {'card':<46} {'move':<22} {'mechanical kills':<24} restatement")
for cid, move, killed, share, failed in rows:
    k = ", ".join(killed) if killed else "none"
    rs = "FAILED" if failed else f"{share} new"
    print(f"  {cid[:46]:<46} {str(move):<22} {k:<24} {rs}")
for d in out.get("declined", []):
    print(f"  DECLINED  {d.get('move')} / {d.get('trigger')}: {d.get('why')}")
survivors = [r[0] for r in rows if not r[2]]
print(f"\n  to the attacker: {len(survivors)} card(s). For each, run\n"
      f"  python3 prepare_attack.py {cards_dir}/<card_id>.json {corpus_path} <folder>")
json.dump({"declined": out.get("declined", []), "summary": [
    {"card_id": r[0], "move": r[1], "mechanical_kills": r[2],
     "restatement_share_new": r[3]} for r in rows]},
    open(os.path.join(cards_dir, "_intake_summary.json"), "w"), indent=2)
