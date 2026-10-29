# Finding passages of a paper in a record of it

You have three files: a published qualitative research paper, as a PDF; this
file; and `PASSAGES_AND_Q_bechky.md`. That file holds, first, 15 lines, L01 to
L15, each naming a passage of the paper by its page and its place on the page;
and then list Q, a record of the paper made separately, which records what the
paper claims and the evidence it prints:

- **Claims** (QC01, QC02, …): what the paper asserts, each as one statement,
  with the pages where the paper makes it, in the order of their first page.
- **Passages** (QP001, QP002, …): pieces of the evidence the paper prints, such
  as a reported event, a quotation, an observation, a document or a table
  cell, each with its location in the paper and a short description, page by
  page.

The statements and descriptions are short paraphrases, not the paper's words.

Your task: for each line, L01 to L15, find its passage in the paper, and say
which items of list Q come from that passage.

Work from the paper and the two files alone. Do not search the web, and set
aside anything you know about this paper or its author from elsewhere.

## When an item of list Q comes from a line's passage

- **A passage of list Q** comes from it when its description records material
  printed in that passage: the same event, observation, quotation, document or
  table cell, whether it cuts it wider or narrower. A passage of list Q that
  holds the line's passage and more counts, and so does one that holds a part
  of it. Look on the line's page, and on the page before or after where the
  material runs over a page break.
- **A claim of list Q** comes from it when that passage asserts, in the paper's
  own voice, what the claim states: the same relation, whatever the wording.
  A claim about the same subject that the passage does not assert does not
  count.
- Two items that make the same kind of point as the passage, or speak of the
  same people, do not count unless they come from it.
- A line may have no item of list Q, or several.

## Your reply

A single JSON object and nothing else, as a file if you can, otherwise as one
code block:

```json
{
  "lines": {
    "L01": {"found": true, "passages": ["QP012"], "claims": [], "reason": "..."},
    "L02": {"found": true, "passages": [], "claims": [], "reason": "..."},
    "L03": {"found": false, "passages": [], "claims": [], "reason": "..."}
  }
}
```

- One entry for every line, L01 to L15, each once.
- `found`: false only when the line names no passage that you can find in the
  paper; then both lists are empty.
- `passages` and `claims`: the ids of list Q that come from the line's
  passage, or empty lists.
- `reason`: one sentence, in your own words.
- The example shows the form only. It is not about the paper.
- Do not quote more than eight words of the paper in a row. Paraphrase, and
  cite the page.
- Give the whole object in one reply.
