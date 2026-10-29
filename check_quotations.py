"""The quotation check of the claims network page (CLAIM_NETWORK_bechky.html): which
strings the page shows repeat the paper's own words. Written on 21 Oct 2026; its rule fixed here before any run on
the paper.

THE RULE
- What is compared: every string the page shows, block by block (a paragraph, a list item, a table cell, a heading,
  a definition, a summary line, a tooltip of the drawing), and every aria-label, against the paper's text.
- The paper's text: the paper's PDF, turned to text in three renderings, each searched apart: (A) pdftotext's
  reading order, page by page, the running heads at the top of each page taken off and the pages joined, with a word
  broken over a line end by a hyphen joined again; (B) the same, the hyphen kept as a break between two words; (C)
  pdftotext's layout rendering, page by page, with broken words joined again, which keeps a table's cells on their
  lines. More text can only make the check stricter.
- Words: as wording_check.py takes them: after Unicode compatibility normalization and with curly quotes made
  straight, lower-case runs of letters and digits, an apostrophe inside a word kept.
- What counts: a run of SIX or more consecutive words of a page string that are, in the same order, consecutive words
  of a rendering of the paper. Overlapping windows of six are joined into one run. Nothing is exempt; each run is
  reported with where it stands in the page (the panel, claim or reading, and the part) and the pages of the paper
  that hold its first six words.
- Classes, for reading the result, not for exempting anything: the paper's citation; the index's claim statements
  (checked at extraction by wording_check.py, which flags seven words or more); the readings' titles; the readings
  as the coders read them; the rest of the readings.

Read-only: it writes only its report (OUT_MD) and its data (OUT_JSON), and never the paper's text.
usage: python3 -I check_quotations.py PAPER_PDF PAGE_HTML OUT_MD OUT_JSON
"""
import collections
import hashlib
import html.parser
import json
import re
import subprocess
import sys
import unicodedata

N = 6
HEADS = re.compile(r"^\s*(Bechky|\d{3}|Administrative Science Quarterly 65 \(2020\))\s*$")
BLOCK = {"p", "li", "dd", "dt", "td", "th", "h1", "h2", "h3", "h4", "summary", "title", "text", "caption"}


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    return s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')


def toks(s):
    return re.findall(r"[a-z0-9]+(?:'[a-z]+)?", norm(s).lower())


def pages_text(pdf, layout):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, check=True, text=True).stdout
    n = int(re.search(r"Pages:\s+(\d+)", out).group(1))
    pages = []
    for k in range(1, n + 1):
        args = ["pdftotext", "-f", str(k), "-l", str(k)] + (["-layout"] if layout else []) + [pdf, "-"]
        t = subprocess.run(args, capture_output=True, check=True).stdout.decode("utf-8", "replace").replace("\f", "")
        lines = t.split("\n")
        if not layout:
            while lines and (not lines[0].strip() or HEADS.match(lines[0])):
                lines.pop(0)
        pages.append("\n".join(lines))
    return pages


def renderings(pdf):
    plain, lay = pages_text(pdf, False), pages_text(pdf, True)
    joined = re.compile(r"(\w)-\s*\n\s*(\w)")
    a = [joined.sub(r"\1\2", p) for p in plain]
    b = [re.sub(r"-\s*\n\s*", " ", p) for p in plain]
    c = [joined.sub(r"\1\2", p) for p in lay]
    out = {}
    for name, pages in (("A", a), ("B", b), ("C", c)):
        stream, page_of = [], []
        if name in ("A", "B"):
            # pages joined, so that a sentence over a page break stays whole; each token knows its page
            for k, p in enumerate(pages, 1):
                tt = toks(p)
                stream += tt
                page_of += [k] * len(tt)
        else:
            for k, p in enumerate(pages, 1):
                tt = toks(p) + ["\x00"]
                stream += tt
                page_of += [k] * len(tt)
        out[name] = (stream, page_of)
    return out, len(plain)


class Blocks(html.parser.HTMLParser):
    """The page's text, block by block, each with the innermost section or anchor id around it."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.blocks, self.buf, self.skip = [], [], [], 0

    def where(self):
        ids = [i for _, i in self.stack if i]
        sect = next((i for i in reversed(ids) if i.startswith(("claim-", "reading-", "node-"))), None)
        return sect or (ids[-1] if ids else "page")

    def flush(self):
        text = re.sub(r"\s+", " ", "".join(self.buf)).strip()
        if text:
            self.blocks.append((self.where(), self.part(), text))
        self.buf = []

    def part(self):
        for tag, _ in reversed(self.stack):
            if tag in BLOCK:
                return tag
        return "inline"

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("style", "script"):
            self.skip += 1
        if tag in BLOCK:
            self.flush()
        if a.get("aria-label"):
            self.blocks.append((a.get("id") or self.where(), "aria-label", a["aria-label"]))
        self.stack.append((tag, a.get("id")))

    def handle_endtag(self, tag):
        if tag in ("style", "script"):
            self.skip -= 1
        if tag in BLOCK:
            self.flush()
        while self.stack:
            t, _ = self.stack.pop()
            if t == tag:
                break

    def handle_data(self, data):
        if not self.skip:
            self.buf.append(data)


def runs_in(tt, grams):
    hits = [i for i in range(len(tt) - N + 1) if tuple(tt[i:i + N]) in grams]
    runs, cur = [], None
    for i in hits:
        if cur and i <= cur[1]:
            cur[1] = i + N
        else:
            if cur:
                runs.append(tuple(cur))
            cur = [i, i + N]
    if cur:
        runs.append(tuple(cur))
    return runs


def classify(where, part, text, citation):
    if citation and citation in text:
        return "the paper's citation"
    if where.startswith("claim-") or where.startswith("node-"):
        return "a claim statement (the index's words)"
    if where.startswith("reading-"):
        return "a reading"
    return "elsewhere on the page"


def main(pdf, page, out_md, out_json):
    pdf_sha = hashlib.sha256(open(pdf, "rb").read()).hexdigest()
    page_bytes = open(page, "rb").read()
    page_sha = hashlib.sha256(page_bytes).hexdigest()
    rend, n_pages = renderings(pdf)
    grams = {}
    for name, (stream, page_of) in rend.items():
        for i in range(len(stream) - N + 1):
            g = tuple(stream[i:i + N])
            if "\x00" in g:
                continue
            grams.setdefault(g, set()).add(page_of[i])
    parser = Blocks()
    parser.feed(page_bytes.decode("utf-8"))
    parser.flush()
    cit = re.search(r'<p class="cite">(.*?)</p>', page_bytes.decode("utf-8"))
    citation = html.unescape(cit.group(1)) if cit else ""
    found, seen = [], set()
    for where, part, text in parser.blocks:
        tt = toks(text)
        for s, e in runs_in(tt, grams):
            words = " ".join(tt[s:e])
            key = (where, words)
            if key in seen:
                continue
            seen.add(key)
            pages = sorted(grams[tuple(tt[s:s + N])])
            found.append({"where": where, "part": part, "words": words, "length": e - s,
                          "paper_pages": [p + 605 for p in pages], "class": classify(where, part, text, citation)})
    by_class = collections.Counter(f["class"] for f in found)
    data = {"rule": {"run": N, "renderings": "A plain, heads off, hyphens joined; B the same, hyphens as breaks; "
                                            "C layout, hyphens joined"},
            "pdf_sha256": pdf_sha, "pdf_pages": n_pages, "page": page, "page_sha256": page_sha,
            "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
            "blocks_checked": len(parser.blocks), "runs": found, "by_class": dict(by_class)}
    json.dump(data, open(out_json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    L = ["# The quotation check of the claims network page", "",
         f"Page `{page.rsplit('/', 1)[-1]}`, sha256 {page_sha}; the paper's PDF, sha256 {pdf_sha} ({n_pages} pages, "
         "kept outside the folder); by `check_quotations.py`, whose rule its header fixes: a run of six or more "
         "consecutive words of a string the page shows that are consecutive words of the paper.", "",
         f"Strings checked: {len(parser.blocks)}. Runs found: {len(found)}.", ""]
    for c, n in sorted(by_class.items()):
        L.append(f"- {c}: {n}")
    L += ["", "| where in the page | part | words | length | paper page |", "|---|---|---|---|---|"]
    for f in sorted(found, key=lambda f: (f["class"], f["where"], -f["length"])):
        L.append(f"| {f['where']} | {f['part']} | {f['words']} | {f['length']} | "
                 f"{', '.join(str(p) for p in f['paper_pages'])} |")
    open(out_md, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("blocks", len(parser.blocks), "runs", len(found), dict(by_class))


if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise SystemExit(__doc__)
    main(*sys.argv[1:])
