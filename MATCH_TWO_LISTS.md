# Matching two lists of one paper

You have three files: a published research paper (a PDF), this file, and
`TWO_LISTS_bechky.md`, which holds two lists of that paper, list P and list Q.
Each list records what the paper claims and the evidence it prints. The two
lists were made separately, and they divide the paper differently. Your task is
to say, for every item of each list, which items of the other list are its
counterparts, if any.

Work from the paper and the two lists alone. Do not search the web, and set
aside anything you know about this paper or its author from elsewhere.

## What the lists hold

Each list has two parts.

- **Claims** (PC01, PC02, … in list P; QC01, QC02, … in list Q): what the
  paper asserts, each as one statement, with the pages where the paper makes
  it. They are in the order of their first page.
- **Passages** (PP001, PP002, … in list P; QP001, QP002, … in list Q): pieces of
  the evidence the paper prints, such as a reported event, a quotation, an
  observation, a document or a table cell, each with its location in the paper
  and a short description. They are page by page.

The statements and descriptions are short paraphrases. Where one leaves you
unsure what it points to, go to its location in the paper and decide from what
the paper prints there.

## When two claims are counterparts

A claim of P and a claim of Q are counterparts when they assert the same thing
about the paper's subject.

- If a claim says that some condition affects some outcome in some direction
  (raises it, lowers it, makes it more or less likely, changes it in a
  stated way), its counterpart names the same condition, the same outcome and
  the same direction, whatever the wording and however broadly or narrowly each
  is put.
- If a claim names no direction, or no condition and outcome at all, its
  counterpart makes the same assertion.
- Where one list states as one claim what the other states as two, each of the
  two is a counterpart of the one, and the one is a counterpart of each.
- A claim may have no counterpart.

## When two passages are counterparts

A passage of P and a passage of Q are counterparts when they report the same
printed material: the same event, observation, quotation, document or table
cell, whether one cuts it wider or narrower than the other.

- A passage that holds two or more passages of the other list is a counterpart
  of each of them, and each of them is a counterpart of it.
- Two passages that overlap, each holding part of the other's material, are
  counterparts too.
- Look for a passage's counterparts on the same page, and on the page before or
  after where the material runs over a page break. A table's cells (passages
  whose location names a table) are matched within the same table.
- Two passages that make the same kind of point, or speak of the same people,
  are not counterparts unless they report the same material.
- A passage may have no counterpart.

## Your reply

One JSON object, with the two keys below and no others, and nothing before or
after it:

```json
{
  "claims": {
    "PC01": ["QC01"],
    "PC02": [],
    "QC01": ["PC01"]
  },
  "passages": {
    "PP001": ["QP001", "QP002"],
    "QP001": ["PP001"],
    "QP002": ["PP001"]
  }
}
```

- `claims` has one entry for every claim of both lists, and `passages` one
  for every passage of both lists: each id exactly once, as a key.
- Each entry lists the ids of its counterparts in the other list, or is empty,
  `[]`. A claim's counterparts are claims, and a passage's are passages.
- Counterparts are mutual: decide each pair once, and name it from both sides.
  If PP001 lists QP002, QP002 lists PP001.
- Give the whole object in one reply.

## A made-up example

The example is invented and has nothing to do with the paper.

List P:

- **PC01** (p. 4). Bakeries that adopted the new ovens cut their night shifts.
- **PC02** (p. 5). Bakeries that adopted the new ovens baked more bread by day.
- **PC03** (pp. 8–9). Bakers judged the new ovens by the crust they produced.
- **PP001** · p. 4. A head baker recalls the last night shift before the ovens
  came.
- **PP002** · Table 1, loaves baked by day — before the ovens, p. 5. The count
  before the ovens.
- **PP003** · Table 1, loaves baked by day — after the ovens, p. 5. The count
  after the ovens.
- **PP004** · p. 8. A baker taps a crust and calls the oven "honest".

List Q:

- **QC01** (pp. 4–5). Adopting the new ovens moved baking from night to day.
- **QC02** (p. 11). Owners who trained their staff kept the ovens longer.
- **QP001** · pp. 4–5. The head baker's account of the last night shift and of
  the first morning with the ovens.
- **QP002** · Table 1, p. 5. Loaves baked by day, before and after the ovens.
- **QP003** · p. 10. An owner describes the training course.

The reply:

```json
{
  "claims": {
    "PC01": ["QC01"],
    "PC02": ["QC01"],
    "PC03": [],
    "QC01": ["PC01", "PC02"],
    "QC02": []
  },
  "passages": {
    "PP001": ["QP001"],
    "PP002": ["QP002"],
    "PP003": ["QP002"],
    "PP004": [],
    "QP001": ["PP001"],
    "QP002": ["PP002", "PP003"],
    "QP003": []
  }
}
```

QC01 states as one claim what P states as two, so it is a counterpart of both.
QP001 cuts the head baker's account wider than PP001, and QP002 holds both of
P's table cells. PC03, PP004, QC02 and QP003 have no counterpart.
