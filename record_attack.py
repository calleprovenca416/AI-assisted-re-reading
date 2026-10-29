"""Record an attack verdict on a card. A killed reading is KEPT, marked killed."""
import json, sys

card_path, verdict_path = sys.argv[1], sys.argv[2]
card = json.load(open(card_path))
v = json.load(open(verdict_path))
killed = [x["mode"] for x in v["verdicts"] if x["killed"]]
card["status"] = "killed" if killed else "survived_attack"
card["attack"] = {"killed_by": killed, "verdicts": v["verdicts"],
                  "kept": "A killed reading is retained, marked. Deleting it "
                          "removes the evidence that the pass functions."}
json.dump(card, open(card_path, "w"), indent=2)
print(f"{card_path}: status {card['status']}   killed by {killed or 'nothing'}")
