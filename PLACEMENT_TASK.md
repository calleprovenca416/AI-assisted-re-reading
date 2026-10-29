# Placing readings on a map of the paper's argument

You have four files besides this one: a published qualitative paper, as a
PDF; a map of its argument; a file of readings of the paper, numbered R01
onward; and two coders' codes of how each reading relates to the paper's
claims. Every record in the map is a summary, not the paper's words: check
the page.

Each reading proposes another way of reading the paper's own account. Your
task is to say, for each reading, where it lands on the map, what its
evidence rests on, what it targets that the map lacks, and what it opens.
You do not judge whether a reading is right, well supported or worth
pursuing: only where it bears on the paper's argument as the map lays it
out.

## How to read the map

- **Claims** (C01 onward): each with its pages, whether it is core (it
  carries the paper's contribution), whether the paper states it as
  established or ventures it, its outcome, its constructs, the passages
  linked to it, and the edges into and out of it.
- **Edges** (E01 onward): "Cj rests on Ci" means that with the paper's
  support for Ci set aside, the paper as printed no longer gives a reason to
  hold Cj as stated. Each edge has a type: `evidential` (Cj's support is Ci
  or its instances), `mechanistic` (Cj's mechanism presupposes Ci's
  outcome), `comparative` (Cj ranks explanations, and Ci is a term in the
  ranking) or `significance` (Cj stays true without Ci but loses its point);
  and a strength: `necessary` (nothing else in the paper gives Cj what Ci
  gives it) or `contributing`.
- **Constructs** (K01 onward): each construct the claims name, with the names
  the claims use for it.
- **Factors** (X1 onward): the paper's own explanatory factors, each with the
  claim that states it; where the map has them, the **units** (U1 onward)
  of the paper's comparative table, with their outcomes and each factor's
  value; and, for each contrast pair, whether each factor is held, varies or
  is unclear.
- **Passages** (F01 onward), **contrast pairs** (CP01 onward), **declared
  gaps** (DG01 onward) and **absences** (A01 onward), as the paper's index
  records them. Passages are the evidence, not elements of the argument:
  give them under `evidence`.

## The codes

For each reading, two coders, A and B, each gave the claim the reading bears
on most directly, what it does to that claim, up to two more claims with what
it does to each, a page and a reason, in six types: `inverts`,
`other_mechanism`, `rereads_evidence`, `challenges_premise`, `complements`,
`restates` (the codes file defines them). Take the codes as a first placement
on the claims, and correct them or add to them where the reading's own words
take it elsewhere: your placement is of the reading, not of the codes.

## What to give for each reading

1. **bears_on:** each element of the map the reading bears on, by its id (a
   claim, an edge, a construct, a factor, a unit, a contrast pair, a declared
   gap or an absence), each with one line on how. Give the elements the
   reading itself engages, not every element near them.
2. **evidence:** the ids of the passages the reading's own evidence rests on,
   as far as the reading's pages and descriptions let you find them; an
   empty list if none can be found.
3. **off_map:** in one sentence, what the reading targets that the map lacks
   (a claim, a tie, a construct, a factor or evidence that the map does not
   hold), or exactly `none` if it targets nothing the map lacks.
4. **opening:** two sentences. The first: what the reading opens in the
   paper's argument. The second: the next investigation that would settle
   it. Tie each sentence to the element of the map it concerns, by its id, or
   mark it `off-map`. Write the sentences themselves in plain words, without
   the map's ids: another reader will see them without the map, and the id
   goes in `tie`.

Every reading lands somewhere: give at least one element under `bears_on`,
or say under `off_map` what it targets that the map lacks.

## An example

From a made-up paper on hospital wards, not the one attached; its ids are
short, so as not to be taken for the map's. Its map holds, among others: C1
(core: endorsement by the hospital leads wards to adopt checklists), C2 (ward
A adopted after the endorsement), E1 (C1 rests on C2, evidential,
contributing), K2 (endorsement), X5 (endorsement, stated in C1), CP1 (ward A
against ward B, differing in endorsement) and F3 (p. 12, a nurse of ward A on
how the checklist came in). A reading: "Ward A adopted because its night
nurses pushed for the checklist, not because of the endorsement (p. 12)."
Both coders: C1, `other_mechanism`. A placement:

- **bears_on:** C1 (it puts the nurses' push in place of the endorsement as
  the cause); E1 (if ward A's case is the nurses', it no longer supports C1);
  X5 (it denies the factor its work in ward A); CP1 (the pair's difference
  may be the nurses, not the endorsement).
- **evidence:** F3.
- **off_map:** the night nurses' push, which no claim or factor of the map
  holds.
- **opening:** "If ward A adopted on its nurses' push, the paper's contrast
  no longer isolates the endorsement." (tie: CP1) "Comparing the nurses'
  accounts in both wards would show whether the push, not the endorsement,
  sets adoption." (tie: off-map)

## Rules

- Place every reading in the file, once, in its order.
- Read the paper. A page in a reading is a pointer, not a proof.
- Place each reading on its own words, whoever may have written it, and
  whatever the coders say of it.
- Do not quote more than eight words of the paper or of a reading in a row.
  Paraphrase, and cite the page.
- Work only from the paper and these files. Do not search the web.

## What to return

A single JSON object and nothing else, as a file if you can, otherwise as one
code block:

```json
{
  "paper": "author and year, as the paper prints them",
  "placements": [
    {
      "reading": "R01",
      "bears_on": [
        {"element": "C..", "how": "..."},
        {"element": "E..", "how": "..."}
      ],
      "evidence": ["F..", "F.."],
      "off_map": "none",
      "opening": [
        {"sentence": "...", "tie": "C.."},
        {"sentence": "...", "tie": "off-map"}
      ]
    }
  ]
}
```
