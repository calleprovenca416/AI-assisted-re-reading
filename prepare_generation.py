"""
Build the complete bundle for a clean Stage 2 generation session, in one command.

    python3 prepare_generation.py <corpus.json> <out_dir> [--voice=<sidecar.json>]

With --voice= the dossier applies the voice rule, as `audit.py --voice=` does,
and its section 0 says so; without it, section 0 says the rule was not applied.
Pass the paper's voice sidecar when generation runs on a cold paper. The sidecar
is read and checked against the corpus before anything is written, and it does
not go into the bundle: only the dossier's use of it does.

Writes three files and nothing else:
    STAGE2_PROMPT.md                the instructions
    dossier_for_generation.txt      the Stage 1 dossier with every coder basis removed
    corpus_for_generation.json      the corpus with bases blanked, claim notes
                                    removed and the extraction history neutralised

What the generator keeps: stubs, glosses, fragment notes, claims and their
directions -- a seam is defined by the directions, so the generator must see them
-- plus contrast pairs, gaps and absences. What it loses is every trace of the
project's history with this paper: which codes were contested, what was recoded,
and whether a seam once existed here. A generator that knows where the last
reading died writes readings shaped to survive the attacker, and the rejection
rate then measures what it learned rather than what the pipeline does.
"""
import json
import os
import shutil
import sys

from schema import load
from dossier import build
from audit import load_voice

NEUTRAL = ("Claim layer extracted by a single coder. Direction codes are that "
           "coder's judgements and have not been second-coded.")


def _strip_history(note):
    """Fragment notes may record facts about the printed text, which the generator
    and attacker need. Correction history is not a fact about the text: it tells a
    reader what was wrong before, and here it names a divergence the generator
    should find for itself."""
    if not note:
        return note
    note = note.split("Corrected in v4.1:")[0].strip()
    return note or None


def strip_for_generation(raw: dict):
    out = json.loads(json.dumps(raw))
    for l in out.get("claim_links", []):
        l["basis"] = ""
    for c in out.get("claims", []):
        c["notes"] = None
    for f in out.get("fragments", []):
        f["notes"] = _strip_history(f.get("notes"))
    out["meta"]["claim_layer_basis"] = NEUTRAL
    return out


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--voice=")]
    voice_args = [a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--voice=")]
    if len(args) != 2 or len(voice_args) > 1:
        raise SystemExit("usage: python3 prepare_generation.py <corpus.json> <out_dir> "
                         "[--voice=<sidecar.json>]")
    corpus_path, out_dir = args
    voice_path = voice_args[0] if voice_args else None
    voice = None
    if voice_path is not None:
        try:
            voice = load_voice(voice_path, load(corpus_path))
        except ValueError as e:
            raise SystemExit(f"REFUSING, nothing written: {e}")
    os.makedirs(out_dir, exist_ok=True)
    raw = json.load(open(corpus_path))
    clean = strip_for_generation(raw)
    cpath = os.path.join(out_dir, "corpus_for_generation.json")
    json.dump(clean, open(cpath, "w"), indent=2)
    dossier = build(load(cpath), for_generation=True, voice=voice,
                    voice_source=os.path.basename(voice_path) if voice_path else None)
    open(os.path.join(out_dir, "dossier_for_generation.txt"), "w").write(dossier)
    shutil.copy("STAGE2_PROMPT.md", os.path.join(out_dir, "STAGE2_PROMPT.md"))
    print(f"bundle in {out_dir}/: STAGE2_PROMPT.md, dossier_for_generation.txt, "
          f"corpus_for_generation.json")
    if voice_path is not None:
        print(f"  voice rule applied from {os.path.basename(voice_path)} "
              f"({len(voice)} fragments coded); the sidecar is not in the bundle.")
    else:
        print("  voice rule NOT applied: no --voice= given.")
    print("  Give a clean session these three files and nothing else.")
    print("  It must not have seen any attack verdict, card, or project summary.")
