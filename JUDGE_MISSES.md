# Judging passages that an index of a paper may have left out

You have five files: a published qualitative research paper, as a PDF; this
file; a reading sheet of an index of that paper, `CHECK_SHEET_bechky.md` or
`CHECK_SHEET_pratt.md`; `EXTRACTION_BRIEF.md`, the brief under which the index
was made; and `TWO_PASSAGE_LISTS_bechky.md` or `TWO_PASSAGE_LISTS_pratt.md`,
which holds two lists, A and B, of passages of the paper that a reader thought
the index may have left out. The two lists were made separately. Each line names
a passage by its page and its place on the page, and nothing else.

Your task has two parts. First, pair the lines of the two lists that name the
same passage. Then say of every line of both lists whether, under the brief, its
passage is a miss of the index.

Work from the paper and these files alone. Do not search the web, and set aside
anything you know about this paper or its author from elsewhere.

## The index and its sheet

- The index records the evidence the paper prints, as **fragments**, and what
  the paper asserts, as **claims**, under the brief: fragments in its pass 1,
  claims in its pass 2.
- The sheet gives the index's claims first, in full. Then, page by page, the
  claims the index locates on that page and the fragments it took from it, each
  with its location and a stub, the index's paraphrase of the passage.
- The index records a page for each fragment and claim, and never a paragraph.
  The fragments under a page should follow the page from top to bottom.

## Part 1: pairs

A line of list A and a line of list B are a **pair** when they name the same
passage of the paper, or passages that overlap: one holding the other, or each
holding part of the other.

- Find each line's passage in the paper first. One place may be named in
  different ways: a paragraph by its count on the page, as the one that runs
  over a page break, or by what stands next to it.
- Two lines on the same page that name different paragraphs are not a pair.
  Neither are two passages that make the same kind of point.
- A line may pair with more than one line of the other list, or with none.

## Part 2: verdicts

For every line of both lists, find its passage, read it, and read what the
sheet records on its page and on the pages next to it. Then give one verdict:

- `evidence`: the passage prints evidence that the brief records as a fragment,
  and no fragment on the sheet records it;
- `assertion`: the passage asserts, in the paper's own voice, how something
  works, which the brief records as a claim (pass 2, with its attribution
  test), and no claim on the sheet states it;
- `both`: both of these hold;
- `covered`: what the passage holds that the brief would record is on the
  sheet already, as fragments or claims, which you name;
- `not_in_brief`: the passage holds nothing that the brief records as a
  fragment or a claim;
- `not_found`: the line names no passage that you can find in the paper.

For each line, one sentence of reason, in your own words. Judge each line on its
passage alone. That a line is on a list is no sign either way: the lists hold
what a reader suspected, not what was found.

## Your reply

A single JSON object and nothing else, as a file if you can, otherwise as one
code block:

```json
{
  "pairs": [["A02", "B02"]],
  "verdicts": {
    "A01": {"verdict": "covered", "ids": ["F07", "C03"], "reason": "..."},
    "A02": {"verdict": "evidence", "ids": ["F12"], "reason": "..."},
    "B01": {"verdict": "not_in_brief", "ids": [], "reason": "..."},
    "B02": {"verdict": "evidence", "ids": ["F12"], "reason": "..."}
  }
}
```

- `pairs`: every pair once, its line of list A first. An empty list if there
  are none.
- `verdicts`: one entry for every line of both lists, each once, with
  `verdict` one of the six above.
- `ids`: the ids of the sheet's fragments and claims (such as F07 or C03) that
  the verdict rests on. Required for `covered`; for the others, the nearby
  records you set the passage against, or empty.
- The example shows the form only. It is not about the paper.
- Do not quote more than eight words of the paper in a row. Paraphrase, and
  cite the page.
- Give the whole object in one reply.
