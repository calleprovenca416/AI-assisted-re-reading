# Checking an index of a paper for what it left out

You have four files: a published qualitative research paper, as a PDF; this
file; a reading sheet of an index of that paper, `CHECK_SHEET_bechky.md` or
`CHECK_SHEET_pratt.md`; and `EXTRACTION_BRIEF.md`, the brief under which the
index was made.

The index records the evidence the paper prints, as fragments, and what the
paper asserts, as claims. Your task is to read the paper against the index and
list the passages that it left out. You do not add to the index or correct it:
you list the passages.

Work from the paper and these files alone. Do not search the web, and set aside
anything you know about this paper or its author from elsewhere.

## The sheet

- It gives the index's claims first, in full. Then, page by page, the claims
  the index locates on that page, in words, and the fragments it took from that
  page, each with its location and a stub.
- A stub is the index's paraphrase of a passage, not the paper's words. A gloss
  is the paper's own later reading of that passage, where the index kept one.
- The index records a page for each fragment and claim, and never a paragraph.
  The fragments under a page are numbered in the order the index met them, so
  they should follow the page from top to bottom.
- The sheet's head names the pages with no fragment at all. They are a place to
  start, not a finding: a page of references has none either.
- The sheet shows what was recorded and where. It cannot show whether a record
  gives its passage rightly, and that is not your task.

## What to do

1. **Read the claims once,** at the head of the sheet. Under each page the
   sheet gives that page's claims again, in words.
2. **Then read the paper section by section, paragraph by paragraph, with the
   sheet beside it,** from the first page to the last. Tick off each fragment
   as you meet its passage.
3. **List each passage of which one of these holds:**
   - it prints evidence (an event, a quote, an observation, an archival item,
     a table cell), and no fragment covers it;
   - it asserts, in the paper's own voice, how something works, and none of
     the claims covers it.

   Most paragraphs answer both with "no" in a few seconds. A page with no
   fragment is not by itself a miss. The brief says where misses hide: in
   footnotes, table notes and figure captions. What the index counts as a
   fragment and as a claim is in the brief, passes 1 and 2. In doubt, it is
   your call.
4. **Name each passage by its page and its place on the page, and nothing
   else,** so that someone with only the PDF finds it:
   - Count full paragraphs: `p. 12, first full paragraph`.
   - A paragraph that runs over a page break: `pp. 12–13, the paragraph that
     runs over the page`.
   - On the paper's first page: `p. 1, first paragraph after the abstract`.
   - What is not a paragraph, by its name: `p. 1, abstract`; `p. 30,
     footnote 5`; `p. 8, Table 1`; and for one cell of a table, its row and
     column as the table labels them.

   These lines show the form only, with made-up pages. None of them is a
   suggestion.
5. **For each passage, say which test it meets,** `evidence`, `assertion` or
   `both`, and give one sentence of reason, in your own words.

## What to return

A single JSON object and nothing else, as a file if you can, otherwise as one
code block:

```json
{
  "paper": "author and year, as the paper prints them",
  "read_to": "the last page you read",
  "passages": [
    {
      "n": 1,
      "where": "p. 12, second full paragraph",
      "test": "evidence",
      "reason": "..."
    }
  ]
}
```

- The passages in the order of the paper, each once, numbered from 1.
- `where` in the forms of step 4; `test` one of `evidence`, `assertion` or
  `both`.
- If you find no such passage, `passages` is empty.
- Do not quote more than eight words of the paper in a row. Paraphrase, and
  cite the page.
