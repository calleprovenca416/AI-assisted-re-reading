"""
Build, from the replies of chats 45 and 46 (T32), the markers' readings file and
the PI's worth sheet, in one command. Written 13 Oct 2026, on the wager test's
`build_marker_packs.py` and `build_worth_sheet.py`.

    python3 -B build_places_packs.py --seed=N --out=DIR [--edits=FILE] REPLY_45 REPLY_46

Each reading of both replies is put in the form the wager test gave its plain
arm: the wager, then each piece of evidence's job with its page in parentheses
at the end of the job's first sentence; pages made alike as there. Nothing else
of a reading goes in: not its place, its other fields, or which chat wrote it.
The readings are shuffled with the seed, numbered W01 onward and split into
sentences, W01-01 onward, with the wager test's own sentence splitter.

Added on 13 Oct, after both replies were read: --edits=FILE, a JSON list of
exact changes to a reading's words ({"chat", "reading_id", "field": "wager" or
"evidence N", "before", "after"}), made before anything else is done; each
"before" must stand exactly once in its field, or the build stops. It is for
words that would show which chat wrote a reading (places_pack_edits.json says
which and why). The key records the file and how many changes were made.

Writes:
- READINGS_places.md: for the two marker chats, with MARKING.md and the PDF.
- places_packs_key.json: which reading came from which chat and reading id;
  for nobody.
- worth_sheet_places.xlsx: the PI's sheet, the wager test's scale and layout,
  the readings in the markers' order and words, a sentence each joined into a
  paragraph; nothing on it says which chat wrote which. Its document properties
  and the times inside its zip are set to a fixed date after saving (openpyxl
  stamps the time of saving), so that two builds give the same bytes.
"""
import datetime
import hashlib
import json
import os
import random
import re
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import build_marker_packs as bmp     # noqa: E402
import build_worth_sheet as bws      # noqa: E402
from openpyxl import Workbook         # noqa: E402
from openpyxl.styles import Alignment  # noqa: E402

ARMS = (("places given", "45"), ("places found", "46"))

RULES = [
    "Rate worth only: whether the reading, as an idea about the paper's theory, opens something worth a scholar's time.",
    "Whether its facts hold is checked separately by the markers. If you know a premise to be false, rate the reading as written and say so in the note.",
    "Rate each reading on its own, not against the others, and rate every one.",
    "The readings are shuffled, and nothing shows where each came from. Please do not open places_packs_key.json, or the replies of chats 45 and 46, until you have rated them all.",
    "You may consult the paper. A page in a reading is a pointer, not a proof.",
    "Save the workbook as worth_sheet_places_filled.xlsx, with no other change, and send it in our conversation or put it in replies/.",
]


def load_reply(path):
    text = open(path, encoding="utf-8").read()
    a, b = text.find("{"), text.rfind("}")
    if a < 0 or b < a:
        raise SystemExit(f"{path}: no JSON object found")
    return json.loads(text[a:b + 1])


def steady(path):
    stamp = b"2026-10-13T00:00:00Z"
    with zipfile.ZipFile(path) as z:
        items = [(i, z.read(i.filename)) for i in z.infolist()]
    with zipfile.ZipFile(path, "w") as z:
        for i, data in items:
            if i.filename == "docProps/core.xml":
                data, n = re.subn(rb"(<dcterms:modified[^>]*>)[^<]*(</dcterms:modified>)",
                                  rb"\g<1>" + stamp + rb"\g<2>", data)
                if n != 1:
                    raise SystemExit("docProps/core.xml: no single modified date")
            j = zipfile.ZipInfo(i.filename, date_time=(2026, 10, 13, 0, 0, 0))
            j.compress_type = i.compress_type
            j.external_attr = i.external_attr
            z.writestr(j, data)


def apply_edits(rep, chat, edits):
    n = 0
    for e in edits:
        if e["chat"] != chat:
            continue
        r = [x for x in rep["readings"] if x.get("reading_id") == e["reading_id"]]
        if len(r) != 1:
            raise SystemExit(f"edit {e}: reading not found once")
        if e["field"] == "wager":
            holder, k = r[0], "wager"
        elif e["field"].startswith("evidence "):
            holder, k = r[0]["evidence"][int(e["field"].split()[1]) - 1], "job"
        else:
            raise SystemExit(f"edit {e}: field not known")
        if holder[k].count(e["before"]) != 1:
            raise SystemExit(f"edit {e}: found {holder[k].count(e['before'])} times, not once")
        holder[k] = holder[k].replace(e["before"], e["after"])
        n += 1
    return n


def reading_text(r):
    ev = " ".join(bmp.cite_first(e["job"], e["page"]) for e in r.get("evidence") or [])
    return bmp.tidy_pages((r["wager"].strip() + " " + ev).strip())


def main(argv):
    opts, files = {}, []
    for a in argv:
        if a.startswith("--"):
            k, _, v = a[2:].partition("=")
            opts[k] = v
        else:
            files.append(a)
    if not {"seed", "out"} <= set(opts) or len(files) != 2:
        raise SystemExit(__doc__)
    out = opts["out"]
    os.makedirs(out, exist_ok=True)
    rs, sources = [], {}
    edits, done = [], 0
    if opts.get("edits"):
        edits = json.load(open(opts["edits"], encoding="utf-8"))["edits"]
    for (arm, chat), path in zip(ARMS, files):
        rep = load_reply(path)
        done += apply_edits(rep, chat, edits)
        sources[chat] = {"file": os.path.basename(path),
                         "sha256": hashlib.sha256(open(path, "rb").read()).hexdigest(),
                         "paper": rep.get("paper")}
        for r in rep["readings"]:
            rs.append({"arm": arm, "chat": chat, "source_id": r.get("reading_id"),
                       "place": r.get("place"), "text": reading_text(r)})
    if done != len(edits):
        raise SystemExit(f"{len(edits) - done} edits name no reply given")
    rng = random.Random(int(opts["seed"]))
    rng.shuffle(rs)
    citation = json.load(open(os.path.join(HERE, "bechky_2020_v1.json"), encoding="utf-8"))["meta"]["citation"]
    lines = [f"# Readings of {citation}", "",
             f"{len(rs)} readings of this paper, in no particular order. Each is split",
             "into numbered sentences. A page in a sentence is a pointer, not a proof.", ""]
    entries = []
    for i, r in enumerate(rs, 1):
        rid = f"W{i:02d}"
        lines += [f"## Reading {rid}", ""]
        units = []
        for j, s in enumerate(bmp.sentences(r["text"]), 1):
            uid = f"{rid}-{j:02d}"
            lines += [f"{uid}  {s}", ""]
            units.append({"unit": uid, "text": s})
        entries.append({"reading": rid, "arm": r["arm"], "chat": r["chat"],
                        "source_id": r["source_id"], "place": r["place"], "units": units})
    text = "\n".join(lines)
    open(os.path.join(out, "READINGS_places.md"), "w", encoding="utf-8").write(text)
    key = {"what": "the key to READINGS_places.md and worth_sheet_places.xlsx: for nobody",
           "seed": int(opts["seed"]), "sources": sources,
           "edits": ({"file": os.path.basename(opts["edits"]),
                      "sha256": hashlib.sha256(open(opts["edits"], "rb").read()).hexdigest(),
                      "made": done} if opts.get("edits") else None),
           "readings_sha256": hashlib.sha256(text.encode()).hexdigest(), "readings": entries}
    open(os.path.join(out, "places_packs_key.json"), "w", encoding="utf-8").write(
        json.dumps(key, indent=1, ensure_ascii=False) + "\n")

    wb = Workbook()
    ins = wb.active
    ins.title = "Instructions"
    ins.column_dimensions["A"].width = 16
    ins.column_dimensions["B"].width = 110
    rows = [("Rating the worth of the readings", None, True, 13),
            ("What", f"Each reading proposes another way of reading the paper's own account. Give each a worth "
                     f"from 0 to 3, and a note where it helps. Bechky has {len(entries)} readings, on the sheet Bechky.",
             False, 10),
            ("Fill in", "Only the yellow cells: Worth (a whole number, 0 to 3; the cell takes nothing else) and Note. Leave every other cell as it is.",
             False, 10),
            ("Scale", None, True, 10)]
    rows += [(str(v), d, False, 10) for v, d in bws.SCALE]
    rows.append(("Rules", None, True, 10))
    rows += [(str(i), rule, False, 10) for i, rule in enumerate(RULES, 1)]
    r = 1
    for label, t, bold, size in rows:
        bws.cell(ins, f"A{r}", label, bold=bold or label in ("What", "Fill in"), size=size, wrap=r != 1)
        if t is not None:
            bws.cell(ins, f"B{r}", t, bold=False, size=size)
            ins.row_dimensions[r].height = bws.height(t, 120)
        r += 1
    bws.printable(ins)
    bws.readings_sheet(wb, "Bechky", entries)
    fixed = datetime.datetime(2026, 10, 13, 0, 0, 0)
    wb.properties.created = fixed
    wb.properties.modified = fixed
    wb.properties.creator = "build_places_packs.py"
    wb.save(os.path.join(out, "worth_sheet_places.xlsx"))
    steady(os.path.join(out, "worth_sheet_places.xlsx"))
    arms = {a: sum(1 for e in entries if e["arm"] == a) for a, _ in ARMS}
    print(f"{len(entries)} readings {arms}, {sum(len(e['units']) for e in entries)} sentences; "
          f"{done} edits; READINGS_places.md {key['readings_sha256'][:16]}")


if __name__ == "__main__":
    main(sys.argv[1:])
