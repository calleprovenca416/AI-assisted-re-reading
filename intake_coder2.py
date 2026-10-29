"""
Take coder 2's codes back for one stage of a cold paper, check them, and write
the returned workbook that agreement.py and make_voice_sidecar.py read.
Written 28 Sep 2026 with build_cold_pack.py; revised the same day.

Coder 2 is Opus 5.5 in an incognito claude.ai chat, which may not be able to
attach a file. So a stage comes back in one of two forms:

  - the workbook itself, with the shaded columns filled; or
  - plain text, one row per line: row id | ids | reason | code, possibly over
    several replies. The ids are the fragment and claim ids printed in that row
    ("-" for section 6); the reason comes before the code, as section 1 asks.

Either way this script starts from the workbook AS SENT, which it first checks
against the pack key's hash, and then checks:

  - every row is answered; no unknown row id; a row answered more than once
    keeps its LAST answer, and every such row is listed (a coder's correction,
    or a line cut off and sent again after "continue");
  - every line that holds a "|" was read: a line that looks like an answer but
    cannot be read stops the intake and is shown;
  - the ids on each line are the ids printed in that row (a line answering the
    wrong row is caught);
  - every code is on the tab's list, after "goes beyond" -> goes_beyond and
    similar; Stages A and A2 take free text, and an answer starting "none" is
    `none`, the rest going to the reason;
  - every reason is filled in ("never leave a cell blank");
  - in a returned workbook: no coding tab is missing, no row added, dropped or
    reordered, and no printed cell changed (other tabs are ignored and listed);
  - on the direction tab, `with` or `against` on a claim with no outcome, which
    section 1 says is not available, is listed (kept as given: agreement.py
    lists it as invalid by schema).

USAGE
    python3 intake_coder2.py <attach/workbook.xlsx> --key=<pack_key.json> --text=<codes.txt> --out=<returned.xlsx>
    python3 intake_coder2.py <attach/workbook.xlsx> --key=<pack_key.json> --workbook=<returned.xlsx> --out=<returned.xlsx>
    add --partial to see what is still missing without writing anything
    python3 intake_coder2.py --selftest

Put every reply's text for the stage into one file, in the order received. Name
the output returned_<paper_id>_STAGE_<X>_coder2.xlsx.

Revision, 7 Oct 2026 (version 1.1):
- THE INTAKE RECORD. The output carries a tab "intake record" that says which
  paper and stage it is, the hash of the workbook as sent (the one the pack's
  key records), the hash of the corpus the pack was built from, the file the
  answers came in, and a digest of every cell of the coding tabs as written.
  agreement.py reads no returned workbook without it, and refuses one whose
  record names another paper, stage or pack, or whose cells have changed
  since the intake. stamp_problem() is that check. Before this, a returned
  workbook was known by its row ids only, which are the same in every pack
  with as many rows.
  What the record cannot tell: which pack a TEXT reply answered. A line of
  text carries ids only. So a pack is built once and never again after a
  stage has gone out, and each reply file is named for its paper and stage
  when it arrives.
- A reason or a code that opens with "=" is written as text. It was written as
  a formula, and a reader that asks for values then got an empty cell.
After that review's second reading, the same day:
- A workbook given with --workbook= that carries an intake record is refused.
  It is this script's own output and not what a coder returned; taking it
  would give a file changed after the intake a fresh record.
- In Stages A and A2 an answer that begins with `none` is read as `none`, and
  the rest of the cell goes to the reason. Each row where the cell held more
  words is now listed under CHECK BY HAND, by its row id, so that a reading of
  `none` that the coder did not mean is seen when the stage is read in.
- The digest takes the coding tabs in the order of their titles, so that tabs
  put in another order do not read as a changed cell.
"""

import hashlib
import json
import os
import re
import sys

from openpyxl import load_workbook

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_cold_pack import CODE_H, FREE_TEXT, ID_COLUMNS, REASON_H  # one definition, no drift

INTAKE_VERSION = "1.1, 7 Oct 2026"
STAMP_TAB = "intake record"
STAMP_FIELDS = ("paper_id", "stage", "test_pack", "sent_file", "sent_sha256", "corpus_sha256",
                "came_as", "came_file", "came_sha256", "intake", "content_sha256")
FREE = set(FREE_TEXT)
ROW_AT = re.compile(r"(?<![\w.])((?:0b|0|v|[1-7])\.\d+)[`*\s]{0,4}\|", re.I)
HEADER_LINE = re.compile(r"^[|\s`*]*(row\b|row id\b|id\b|#\s*[|`*]|[-:|\s`]+$)", re.I)
MD = re.compile(r"^[\s*_`\"'“”]+|[\s*_`\"'“”.,;:!]+$")


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def squash(v):
    return re.sub(r"\s+", " ", ("" if v is None else str(v))).strip()


def canon(rid):
    rid = rid.strip()
    return "V" + rid[1:] if rid[:1] in "vV" else rid.lower()


def put_text(ws, row, column, value):
    """Write one of the coder's cells as text. A reply that opens with "=" is a
    reply, not a formula."""
    c = ws.cell(row=row, column=column)
    c.value = value
    if isinstance(value, str) and value.startswith("="):
        c.data_type = "s"
    return c


# ------------------------------------------------------------ the intake record
def tabs_digest(wb):
    """One digest of every cell of the coding tabs, as text with its spaces
    squashed, the tabs taken in the order of their titles. Other tabs do not
    count."""
    h = hashlib.sha256()
    for ws in sorted(wb.worksheets, key=lambda w: w.title):
        if ws.title not in ID_COLUMNS:
            continue
        rows = [[squash(c.value) for c in r] for r in ws.iter_rows()]
        for r in rows:
            while r and not r[-1]:
                r.pop()
        while rows and not rows[-1]:
            rows.pop()
        h.update(json.dumps([ws.title, rows], ensure_ascii=False).encode("utf-8"))
    return h.hexdigest()


def stamp(path, record):
    """Add the intake record to a workbook this script has just written. The
    digest is taken from the file as it reads back, so that a reader who opens
    the file gets the same one."""
    wb = load_workbook(path)
    record = dict(record, content_sha256=tabs_digest(wb))
    if STAMP_TAB in wb.sheetnames:
        del wb[STAMP_TAB]
    ws = wb.create_sheet(STAMP_TAB)
    ws.append(["written by intake_coder2.py", "do not edit: agreement.py checks this record"])
    for k in STAMP_FIELDS:
        ws.append([k, str(record[k])])
    ws.column_dimensions["A"].width = 28
    ws.column_dimensions["B"].width = 80
    wb.save(path)
    return record


def read_stamp(wb):
    """The intake record of an open workbook, or None if it has none."""
    if STAMP_TAB not in wb.sheetnames:
        return None
    rows = [tuple(c.value for c in r) for r in wb[STAMP_TAB].iter_rows()]
    return {squash(r[0]): squash(r[1]) for r in rows[1:] if r and r[0] is not None}


def stamp_problem(path, paper_id=None, stage=None, key=None, wb=None):
    """Why a returned workbook is not the intake's own output for this paper,
    stage and pack, as one sentence, or None if it is. With a key, the record
    must name the workbook that key records as sent for the stage."""
    wb = load_workbook(path) if wb is None else wb
    name = os.path.basename(path)
    rec = read_stamp(wb)
    if rec is None:
        return (f"{name} carries no intake record: it has not been read in with "
                "intake_coder2.py, or it was saved without that tab")
    if any(k not in rec for k in STAMP_FIELDS):
        return f"{name}: its intake record is incomplete"
    if paper_id is not None and rec["paper_id"] != paper_id:
        return (f"{name} was read in as a workbook of {rec['paper_id']!r}, and this paper is "
                f"{paper_id!r}")
    if stage is not None and rec["stage"] != stage:
        return f"{name} was read in as Stage {rec['stage']}, and Stage {stage} is asked for"
    if key is not None:
        sent = ((key.get("workbooks") or {}).get(rec["stage"]) or {})
        if (rec["sent_sha256"] != sent.get("sha256") or rec["paper_id"] != key.get("paper_id")
                or rec["corpus_sha256"] != str(key.get("corpus_sha256"))):
            return (f"{name} answers a workbook that this pack's key does not record as sent: "
                    "it belongs to another pack, or the pack was built again after it went out")
    if rec["content_sha256"] != tabs_digest(wb):
        return (f"{name}: a cell of a coding tab has changed since the intake wrote it. Read "
                "the stage in again from what the coder returned")
    return None


def read_tabs(path, strict=True):
    """{tab: {"head", "rows", "ids", "reason_col", "code_col", "allowed"}}; ignores the
    about tab and, when not strict, any tab that is not a coding tab."""
    wb = load_workbook(path)
    tabs, other = {}, []
    for ws in wb.worksheets:
        if ws.title not in ID_COLUMNS:
            if ws.title not in ("about this workbook", STAMP_TAB):
                other.append(ws.title)
            continue
        rows = [tuple(c.value for c in r) for r in ws.iter_rows()]
        while rows and all(v is None or str(v).strip() == "" for v in rows[-1]):
            rows.pop()
        if not rows:
            raise ValueError(f"tab {ws.title!r} is empty")
        head = [squash(h) for h in rows[0]]
        if REASON_H not in head or CODE_H not in head:
            raise ValueError(f"tab {ws.title!r} has lost its {REASON_H!r} or {CODE_H!r} column")
        allowed = None
        for dv in ws.data_validations.dataValidation:
            if dv.formula1 and dv.formula1.startswith('"'):
                allowed = dv.formula1.strip('"').split(",")
        tabs[ws.title] = {"head": head, "rows": rows[1:], "ids": [squash(r[0]) for r in rows[1:]],
                          "reason_col": head.index(REASON_H), "code_col": head.index(CODE_H),
                          "allowed": allowed}
    return wb, tabs, other


def parse_text(text):
    """([(row_id, ids, reason, code, line_no)], [unreadable lines], [dropped cut-off lines]).
    A line cut off before its code (fewer than four fields) is dropped if the same
    row is answered in full elsewhere, as after "continue"; otherwise it is unreadable."""
    out, bad, pending, cut = [], [], None, []

    def close(p):
        if p is None:
            return
        parts = [x.strip() for x in p["text"].strip().strip("|").split("|")]
        if len(parts) < 4:
            cut.append(p)
            return
        out.append((p["rid"], parts[1], " | ".join(parts[2:-1]).strip(), parts[-1], p["line"]))

    for n, raw in enumerate(text.splitlines(), 1):
        line = re.sub(r"^[\s|]+", "", raw)              # a markdown table's leading pipe
        m = ROW_AT.search(line)
        if m and "|" not in line[:m.start()]:
            close(pending)
            pending = {"rid": canon(m.group(1)), "text": line[m.start():], "line": n, "raw": raw}
            continue
        if pending is not None and line.strip() and pending["text"].count("|") < 3:
            pending["text"] += " " + line.strip()          # a reason carried onto the next line
            continue
        if "|" in line and not HEADER_LINE.match(line):
            close(pending)
            pending = None
            bad.append((n, raw))
    close(pending)
    full = {r[0] for r in out}
    dropped = [(p["line"], p["raw"]) for p in cut if p["rid"] in full]
    bad += [(p["line"], p["raw"]) for p in cut if p["rid"] not in full]
    return out, sorted(bad), dropped


def norm_closed(code, allowed):
    c = MD.sub("", code).lower().replace("-", "_").replace(" ", "_")
    table = {a.lower(): a for a in allowed}
    return table.get(c)


def norm_free(code, reason):
    c = MD.sub("", code)
    m = re.match(r"^(?:none|no outcome|no direction|n/?a|null|-+)(?![\w/])\W*(.*)$", c, re.I)
    if m:
        rest = m.group(1).strip(" ()")
        return "none", (reason + (f" [code cell also said: {rest}]" if rest else "")).strip()
    return c, reason


def fill(built_wb, tabs, answers, returned=None):
    """answers: {row_id: (ids, reason, code)}. Returns (errors, notes)."""
    errors, notes = [], []
    where = {rid: t for t, info in tabs.items() for rid in info["ids"]}
    unknown = sorted(set(answers) - set(where))
    if unknown:
        errors.append(f"row ids not in this workbook: {unknown[:12]}{' ...' if len(unknown) > 12 else ''}")
    for t, info in tabs.items():
        ws = built_wb[t]
        idcols = [info["head"].index(c) for c in ID_COLUMNS[t]]
        missing, badcode, noreason, wrongrow, notavail, long_, more = [], [], [], [], [], [], []
        for k, rid in enumerate(info["ids"]):
            if rid not in answers or not answers[rid][2].strip():
                missing.append(rid)
                continue
            ids, reason, code = answers[rid]
            if returned is None and idcols:
                want = {squash(info["rows"][k][i]).upper() for i in idcols}
                got = {x.upper() for x in re.findall(r"[A-Za-z]+\d+", ids)}
                if got != want:
                    wrongrow.append(f"{rid} says {ids!r}, the row is {' '.join(sorted(want))}")
                    continue
            if t in FREE:
                before = reason
                code, reason = norm_free(code, reason)
                if code == "none" and reason != before:
                    more.append(rid)
                if code != "none" and (len(code.split()) > 12
                                       or len(code.split()) > len(reason.split())):
                    long_.append(rid)
            else:
                c = norm_closed(code, info["allowed"] or [])
                if c is None:
                    badcode.append(f"{rid} `{code}`")
                    continue
                code = c
            if not reason.strip():
                noreason.append(rid)
            if t == "1 direction" and code in ("with", "against"):
                if not squash(info["rows"][k][info["head"].index("the claim's outcome")]):
                    notavail.append(f"{rid} `{code}`")
            put_text(ws, k + 2, info["reason_col"] + 1, reason.strip() or None)
            put_text(ws, k + 2, info["code_col"] + 1, code)
        for label, items in (("unanswered", missing), ("code not on the list", badcode),
                             ("no reason", noreason), ("ids do not match the row", wrongrow)):
            if items:
                errors.append(f"{t}: {label}, {len(items)} row(s): {items[:8]}"
                              f"{' ...' if len(items) > 8 else ''}")
        if notavail:
            notes.append(f"{t}: with/against on a claim with no outcome, which section 1 says is "
                         f"not available: {notavail}")
        if more:
            notes.append(f"CHECK BY HAND, {t}: read as `none`, where the cell held more words, on "
                         f"{more[:12]}{' ...' if len(more) > 12 else ''}. The words are kept in the "
                         "reason. Did the coder mean `none` on each?")
        if long_:
            notes.append(f"CHECK BY HAND, {t}: the code is longer than 12 words or than its "
                         f"reason on {long_[:12]}{' ...' if len(long_) > 12 else ''}: were the "
                         "reason and the code swapped?")
    return errors, notes


def compare_returned(sent, back, other):
    errors, notes = [], []
    if other:
        notes.append(f"tabs added by the coder, ignored: {other}")
    for t in sent:
        if t not in back:
            errors.append(f"coding tab {t!r} missing from the returned workbook")
            continue
        a, b = sent[t], back[t]
        if a["head"] != b["head"]:
            errors.append(f"{t}: headers changed")
        elif a["ids"] != b["ids"]:
            errors.append(f"{t}: rows added, dropped or reordered")
        else:
            printed = [i for i in range(len(a["head"])) if i not in (a["reason_col"], a["code_col"])]
            changed = [a["ids"][k] for k, (x, y) in enumerate(zip(a["rows"], b["rows"]))
                       if any(squash(x[i]) != squash(y[i] if i < len(y) else None) for i in printed)]
            if changed:
                errors.append(f"{t}: printed cells changed on {changed[:10]}")
    return errors, notes


def main(argv):
    built = next((a for a in argv if not a.startswith("--")), None)
    opt = {a.split("=", 1)[0]: a.split("=", 1)[1] for a in argv if a.startswith("--") and "=" in a}
    partial = "--partial" in argv
    if (not built or "--key" not in opt or not (("--text" in opt) ^ ("--workbook" in opt))
            or ("--out" not in opt and not partial)):
        raise SystemExit(__doc__)
    key = json.load(open(opt["--key"], encoding="utf-8"))
    rec = [w for w in key["workbooks"].values() if w["file"] == os.path.basename(built)]
    if not rec or rec[0]["sha256"] != sha(built):
        print(f"REFUSED: {built} is not the workbook this key records as sent")
        return 1
    if key.get("test_pack"):
        print("NOTE: this is a TEST PACK")
    wb, tabs, _ = read_tabs(built)
    notes, returned, superseded = [], None, []
    guarded = {os.path.abspath(built)} | ({os.path.abspath(opt["--workbook"])} if "--workbook" in opt else set())
    if "--out" in opt and os.path.abspath(opt["--out"]) in guarded:
        print("REFUSED: --out would overwrite the workbook as sent or the returned file")
        return 1
    if "--text" in opt:
        rows, bad, dropped = parse_text(open(opt["--text"], encoding="utf-8").read())
        print(f"read {len(rows)} answer line(s) from {opt['--text']}")
        if dropped:
            notes.append("cut-off line(s) dropped, the row being answered in full elsewhere: "
                         + ", ".join(f"line {n}" for n, _ in dropped))
        if bad:
            for n, line in bad[:12]:
                print(f"   line {n} not read: {line.strip()[:100]}")
            print(f"REFUSED: {len(bad)} line(s) hold a '|' but could not be read as "
                  "row id | ids | reason | code")
            return 1
        answers, lines, superseded = {}, {}, []
        for rid, ids, reason, code, n in rows:
            if rid in answers and answers[rid] != (ids, reason, code):
                superseded.append((rid, lines[rid][-1], *answers[rid]))
            answers[rid] = (ids, reason, code)
            lines.setdefault(rid, []).append(n)
        if superseded:
            changed = sorted({r[0] for r in superseded
                              if MD.sub("", r[4]).lower() != MD.sub("", answers[r[0]][2]).lower()})
            notes.append(f"CHECK BY HAND: {len({r[0] for r in superseded})} row(s) answered more "
                         f"than once; the last answer is kept and the earlier ones are in the "
                         f"output's 'superseded answers' tab. The code changed on "
                         f"{len(changed)}: {changed[:12]}{' ...' if len(changed) > 12 else ''}")
    else:
        if read_stamp(load_workbook(opt["--workbook"])) is not None:
            print(f"REFUSED: {opt['--workbook']} carries an intake record. It is this script's own "
                  "output, not what a coder returned. Read the stage in from the coder's reply, "
                  "or from the workbook as the coder returned it")
            return 1
        try:
            _, back, other = read_tabs(opt["--workbook"], strict=False)
        except ValueError as e:
            print(f"REFUSED: {e}")
            return 1
        errs, more = compare_returned(tabs, back, other)
        notes += more
        if errs:
            for e in errs:
                print("  ", e)
            print("REFUSED: the returned workbook does not match the one sent")
            return 1
        answers = {rid: ("", squash(r[info["reason_col"]]), squash(r[info["code_col"]]))
                   for info in back.values() for rid, r in zip(info["ids"], info["rows"])}
        returned = back
    errors, more = fill(wb, tabs, answers, returned)
    if "--text" in opt and superseded:
        ws = wb.create_sheet("superseded answers")
        ws.append(["row", "line", "ids", "reason", "code", "replaced by the answer on line"])
        for rid, n, ids, reason, code in superseded:
            later = [x for x in lines[rid] if x > n]
            ws.append([rid, n, ids, reason, code, later[0] if later else None])
            for c in ws[ws.max_row]:
                if isinstance(c.value, str) and c.value.startswith("="):
                    c.data_type = "s"          # a superseded answer is text too
    for n in notes + more:
        print("  NOTE", n)
    if errors:
        for e in errors:
            print("  ", e)
        if partial:
            print("partial: nothing written")
            return 0
        print("REFUSED: nothing written. Ask for the missing or corrected rows, then run again "
              "with every reply's text in one file.")
        return 1
    if partial:
        print("complete: every row answered; run again without --partial to write it")
        return 0
    wb.save(opt["--out"])
    came = opt.get("--text") or opt["--workbook"]
    stamp(opt["--out"], {
        "paper_id": key["paper_id"],
        "stage": next(s for s, w in key["workbooks"].items() if w is rec[0]),
        "test_pack": bool(key.get("test_pack")), "sent_file": rec[0]["file"],
        "sent_sha256": rec[0]["sha256"], "corpus_sha256": key.get("corpus_sha256"),
        "came_as": "text" if "--text" in opt else "workbook",
        "came_file": os.path.basename(came), "came_sha256": sha(came),
        "intake": INTAKE_VERSION})
    print(f"wrote {opt['--out']}: every row answered, every code on its list")
    return 0


def selftest():
    """Left out of the repository's copy: the self-test ran on the Carlile pilot's files, which are not in the
    repository (see the README)."""
    print("selftest: left out of the repository's copy; it runs on the Carlile pilot's files, which are not "
          "here (see the README)")
    return 2


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        raise SystemExit(selftest())
    raise SystemExit(main(sys.argv[1:]))
