"""
Build the PI's sheet for rating the worth of the wager test's readings (T29), in one command.

    python3 build_worth_sheet.py <out.xlsx>

Written 11 Oct 2026. The PI's rating is declared not blind: the PI has seen every reply.

Reads stage2/markers/KEY.json and writes a workbook with three sheets:

    Instructions   what to rate, the scale (0 to 3), the rules, which cells to fill in,
                   and one invented example row
    Pratt          the 15 readings of Pratt, P01 to P15
    Bechky         the 14 readings of Bechky, B01 to B14

Each reading is given exactly as the markers had it (stage2/markers/READINGS_*.md):
the same text, in the same shuffled order, under the same number, its sentences joined
into one paragraph. No arm, chat, move, attack verdict or marker code appears. The
cells to fill in are Worth (a dropdown, 0 to 3) and Note, shaded yellow. The sheet
holds no formula. Its document properties carry a fixed date, so that two builds from
the same key give the same cells and the same properties.
"""
import datetime
import json
import math
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

KEY = "stage2/markers/KEY.json"
FONT = "Arial"
YELLOW = PatternFill("solid", start_color="FFFF00", end_color="FFFF00")
GREY = PatternFill("solid", start_color="D9D9D9", end_color="D9D9D9")
THIN = Side(style="thin", color="999999")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP_TOP = Alignment(wrap_text=True, vertical="top")

SCALE = [
    (0, "Not worth pursuing: it restates the paper, is trivial, or offers nothing a scholar would take up."),
    (1, "Some interest: a fair point, but it would not change how the paper's argument is read."),
    (2, "Worth a scholar's time: a real opening, worth checking against the case or the literature."),
    (3, "A strong opening: if it held, it would change how the paper's argument is read."),
]

RULES = [
    "Rate worth only: whether the reading, as an idea about the paper's theory, opens something worth a scholar's time.",
    "Whether its facts hold was checked separately by the markers. If you know a premise to be false, rate the reading as written and say so in the note.",
    "Rate each reading on its own, not against the others, and rate every one.",
    "The readings are shuffled, and nothing shows where each came from. Please do not open stage2/markers/KEY.json, or the replies and cards in stage2, until you have rated them all.",
    "You may consult the paper. A page in a reading is a pointer, not a proof.",
    "Save the workbook as worth_sheet_filled.xlsx, with no other change, and send it in our conversation or put it in replies/.",
]


def cell(ws, ref, value, bold=False, size=10, fill=None, wrap=True):
    c = ws[ref]
    c.value = value
    c.font = Font(name=FONT, bold=bold, size=size)
    c.alignment = WRAP_TOP if wrap else Alignment(vertical="top")
    if fill:
        c.fill = fill
    return c


def printable(ws):
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True


def height(text, width_chars, line_pt=13.0, minimum=15.0):
    lines = sum(max(1, math.ceil(len(part) / width_chars)) for part in str(text).split("\n"))
    return max(minimum, lines * line_pt + 4)


def readings_sheet(wb, title, entries):
    ws = wb.create_sheet(title)
    headers = ["Reading", "The reading", "Worth (0 to 3)", "Note"]
    widths = {"A": 10, "B": 100, "C": 14, "D": 45}
    for col, w in widths.items():
        ws.column_dimensions[col].width = w
    for i, h in enumerate(headers):
        c = cell(ws, f"{'ABCD'[i]}1", h, bold=True, fill=GREY)
        c.border = BOX
    dv = DataValidation(type="whole", operator="between", formula1="0", formula2="3", allow_blank=True,
                        showErrorMessage=True, errorTitle="Worth", error="Enter a whole number from 0 to 3.",
                        showInputMessage=True, promptTitle="Worth", prompt="0, 1, 2 or 3: see Instructions.")
    ws.add_data_validation(dv)
    for r, e in enumerate(entries, start=2):
        text = " ".join(u["text"] for u in e["units"])
        cell(ws, f"A{r}", e["reading"], bold=True).border = BOX
        cell(ws, f"B{r}", text).border = BOX
        c = cell(ws, f"C{r}", None, fill=YELLOW)
        c.border = BOX
        c.alignment = Alignment(horizontal="center", vertical="top")
        cell(ws, f"D{r}", None, fill=YELLOW).border = BOX
        dv.add(f"C{r}")
        ws.row_dimensions[r].height = height(text, 112)
    ws.freeze_panes = "B2"
    printable(ws)
    return ws, len(entries)


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: python3 build_worth_sheet.py <out.xlsx>")
    key = json.load(open(KEY))
    wb = Workbook()
    ins = wb.active
    ins.title = "Instructions"
    ins.column_dimensions["A"].width = 16
    ins.column_dimensions["B"].width = 110
    rows = [("Rating the worth of the readings", None, True, 13)]
    rows.append(("What", "Each reading proposes another way of reading the paper's own account. Give each a worth from 0 to 3, and a note where it helps. "
                 "Pratt has 15 readings, Bechky 14, each on its own sheet.", False, 10))
    rows.append(("Fill in", "Only the yellow cells: Worth (a dropdown, 0 to 3) and Note. Leave every other cell as it is.", False, 10))
    rows.append(("Scale", None, True, 10))
    for v, d in SCALE:
        rows.append((str(v), d, False, 10))
    rows.append(("Rules", None, True, 10))
    for i, rule in enumerate(RULES, 1):
        rows.append((str(i), rule, False, 10))
    rows.append(("Example", "An invented reading, not one of the 29, to show the format only:", True, 10))
    r = 1
    for label, text, bold, size in rows:
        cell(ins, f"A{r}", label, bold=bold or label in ("What", "Fill in"), size=size, wrap=r != 1)
        if text is not None:
            cell(ins, f"B{r}", text, bold=False, size=size)
            ins.row_dimensions[r].height = height(text, 120)
        r += 1
    ex_row = r
    for i, h in enumerate(["Reading", "The reading", "Worth (0 to 3)", "Note"]):
        cell(ins, f"{'ABCD'[i]}{ex_row}", h, bold=True, fill=GREY).border = BOX
    ex = ex_row + 1
    cell(ins, f"A{ex}", "X01", bold=True).border = BOX
    ex_text = ("Read the merger as a change of owner, not of practice: the plant's routines, as printed, are the same before and "
               "after, and the managers' new vocabulary arrives first in the training slides (p. 12).")
    cell(ins, f"B{ex}", ex_text).border = BOX
    c = cell(ins, f"C{ex}", 2)
    c.border = BOX
    c.alignment = Alignment(horizontal="center", vertical="top")
    cell(ins, f"D{ex}", "Worth checking against the case; the premise about the slides needs the paper.").border = BOX
    ins.row_dimensions[ex].height = height(ex_text, 120)
    ins.column_dimensions["C"].width = 14
    ins.column_dimensions["D"].width = 45
    printable(ins)
    sheets = []
    for title, paper in (("Pratt", "pratt"), ("Bechky", "bechky")):
        ws, n = readings_sheet(wb, title, key["papers"][paper])
        sheets.append((title, n))
    fixed = datetime.datetime(2026, 10, 11, 0, 0, 0)
    wb.properties.created = fixed
    wb.properties.modified = fixed
    wb.properties.creator = "build_worth_sheet.py"
    wb.save(sys.argv[1])
    print(f"wrote {sys.argv[1]}: Instructions, " + ", ".join(f"{t} ({n} readings)" for t, n in sheets))


if __name__ == "__main__":
    main()
