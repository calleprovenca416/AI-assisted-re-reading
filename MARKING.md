# Marking readings against a paper

You are given a published qualitative paper, as a PDF, and a file of readings
of it. Each reading proposes a way of reading the paper's own account. Your job
is not to judge whether a reading is good. It is to check, sentence by
sentence, whether what each sentence reports about the paper, and about the
case the paper studies, is in the paper.

Each reading is split into numbered sentences, such as P03-07. Give every
sentence exactly one code.

---

## Proposing and reporting

A sentence either puts forward the reading's own proposal or reports something
from the paper.

It proposes when it gives the reading's thesis or wager, however it is phrased
("Read X as Y", "The wager is that…", or a flat statement of what the reading
holds), its interpretation, a question, or what would follow if the reading
held. Code it N.

Every other sentence reports: it states what the paper prints or claims, or
what happened in the case, as something found in the paper. A short comment on
a piece of evidence that says what happened (that one thing came before
another, say, or that most of a group did something) reports, and so does a
fact stated inside a proposal: code what it reports. When you cannot tell, ask
whether the paper could show the sentence true or false; if it could, it
reports.

A reading may point to something in the paper without naming it first (the
pair, the episode, the concept). Find it in the paper from the rest of the
reading, and code as usual.

## The codes

| code | use it when |
|---|---|
| **N** | the sentence reports nothing: it only proposes |
| **R** | every fact it reports is printed in the paper, at a place you can name. A paraphrase, or a rounding, that changes no fact counts as printed |
| **RI** | every fact it reports is printed, or follows by plain arithmetic or deduction from what is printed |
| **RA** | it reports that the paper is silent on something, within whatever scope the sentence states, and you have checked the whole paper and found it silent there |
| **P** | it assigns something the paper does not print (a value, an identity, an order, a count) by a judgment from material the paper does print, where counting or plain deduction would not give it |
| **U** | at least one fact it reports is found nowhere in the paper, has no basis in what the paper prints, and is not contradicted by the paper |
| **C** | at least one fact it reports is contradicted by the paper: the paper prints otherwise |

If a sentence reports several facts, give it the code of the weakest, in this
order, weakest first: C, U, P, RI, RA, R.

A sentence that reports what the paper claims, rather than what happened in
the case, reports a fact about the paper: check that the paper claims it. A
sentence that says the paper is silent on something the paper does print is C.
An "every", "only" or "none" that the paper prints only for a narrower set is
U, or C if the paper prints an exception.

When the paper prints a fact in one place and prints otherwise in another, as
when the author's summary and the quoted material differ, code the sentence as
printed, give the page that prints it, and mark drift if it follows the summary
against the material.

A page a sentence cites is a pointer, not a proof. Check each fact in the paper
wherever it is, and give the page where you found it. If a sentence cites the
wrong page but the paper prints the fact elsewhere, code it as printed and give
the right page.

The readings were written in different ways and at different lengths. Code
what each sentence reports, not how it is put.

## For P: is the reasoning stated?

For every P, say whether any sentence of the same reading states how the
assigned thing was arrived at (`reasoning_stated`: true or false).

## For U and C: the position

Judge the position against the reading's main proposal, what it puts forward as
the way to read the paper. If two rows fit, take the first.

| position | use it when |
|---|---|
| **warrant** | the main proposal depends on it: without it, the proposal falls |
| **mechanism** | it is a detail of how the reading says things worked |
| **illustration** | it is an example or an aside, and the reading stands without it |

## Drift

Mark `drift` true for a sentence that presents the author's characterisation as
what happened in the case, or follows the author's summary of a passage where
the passage itself says otherwise. Drift is recorded beside the code, not
instead of it: a drifting sentence still gets the code for what it reports.
Drift is false for N.

---

## Rules

- Work only from the paper. Do not search the web, and set aside anything you
  know about the paper, its author or its subject from elsewhere.
- Code every sentence, in order. Do not skip, merge or split sentences.
- Do not rate the readings, rank them, or say which you prefer.
- Do not quote more than eight words of the paper in a row. Give pages instead.
- Give a short reason in `note` for every RA, P, U and C.

## Output

Return a single JSON object and nothing else:

```json
{
  "paper": "the author's surname and the year",
  "codes": [
    {"unit": "P01-01", "code": "R", "page": "p. ..", "position": null,
     "drift": false, "reasoning_stated": null, "note": ""}
  ]
}
```

`page` is the page or pages where you found what the sentence reports,
separated by semicolons; for C, the page that prints otherwise; null for N, RA
and U. `position` is null except for U and C. `reasoning_stated` is null except
for P.
