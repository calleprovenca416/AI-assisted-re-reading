"""
Build the complete bundle for a blind attack pass, in one command.

    python3 prepare_attack.py <card.json> <corpus.json> <out_dir>

Writes three files and nothing else:
    card_for_attack.json    the reading, with the author's reasoning stripped
    corpus_for_attack.json  the corpus, with every direction code and coder basis blanked
    attack.md               the instructions

Why the corpus is stripped too: the generator now sees stubs, claims and
directions but never bases (dossier.py --for-generation). The attacker should see
less still. Direction codes and bases are a coder's judgements about how fragments
relate to claims, and the attacker judges a reading against what the paper
printed. The last attack diagnosed an import correctly BECAUSE it could see a
basis -- but the verdict did not depend on it, and consistency between what the
generator and the attacker are allowed to treat as evidence matters more.

Kept: stubs, author glosses, fragment notes (which record facts about the printed
text, such as the eight-week figure being unresolvable), claims, contrast pairs,
declared gaps, absences, and the fact of attachment.
"""
import json
import os
import shutil
import sys

from card import for_attack


def _strip_history(note):
    """Fragment notes may record facts about the printed text, which the generator
    and attacker need. Correction history is not a fact about the text: it tells a
    reader what was wrong before, and here it names a divergence the generator
    should find for itself."""
    if not note:
        return note
    note = note.split("Corrected in v4.1:")[0].strip()
    return note or None


def strip_corpus(raw: dict):
    out = json.loads(json.dumps(raw))
    n = 0
    for l in out.get("claim_links", []):
        if l.get("direction") != "unassigned" or l.get("basis"):
            n += 1
        l["direction"], l["basis"], l["confidence"] = "unassigned", "", "low"
    for c in out.get("claims", []):
        c["notes"] = None
    for f in out.get("fragments", []):
        f["notes"] = _strip_history(f.get("notes"))
    out["meta"]["claim_layer_basis"] = ("Claim layer extracted by a single coder; "
                                        "direction codes removed for this pass.")
    out["meta"]["for_attack"] = True
    return out, n


if __name__ == "__main__":
    card_path, corpus_path, out_dir = sys.argv[1:4]
    os.makedirs(out_dir, exist_ok=True)
    card, removed = for_attack(json.load(open(card_path)))
    json.dump(card, open(os.path.join(out_dir, "card_for_attack.json"), "w"), indent=2)
    corpus, n = strip_corpus(json.load(open(corpus_path)))
    json.dump(corpus, open(os.path.join(out_dir, "corpus_for_attack.json"), "w"), indent=2)
    shutil.copy("attack.md", os.path.join(out_dir, "attack.md"))
    print(f"bundle in {out_dir}/")
    print(f"  card:   removed {len(removed)} fields ({', '.join(removed)})")
    print(f"  corpus: blanked direction and basis on {n} links")
    print("  Give the attacker these three files and nothing else. Modes B and E only.")
