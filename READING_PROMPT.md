# Writing readings

You are given one published qualitative paper, as a PDF. You must not use
anything you know or can recall about it from elsewhere. Everything you write
must rest on what the paper prints.

Your job is to write **readings**: plausible re-tellings of the paper's own
account that use its printed evidence in a way the paper does not.

---

## What a reading is, and is not

A reading is **plausible, not rival**. You are not trying to show the author was
wrong. Write the best reading the paper's material supports. If it ends up close
to the paper's own account, say so: agreement is a finding. The only failure is
**restatement** — a reading that uses no evidence differently from the paper.

A reading **locates; it does not name**. Where a move splits a concept, describe
the two sides in the paper's own descriptive words and label them X and Y. Do not
supply theoretical labels, and do not reach for a named distinction from the
literature. Naming happens later, by a person, after the reading has been checked.

A reading is **a wager, not a verdict**. It says what the evidence would support
if read this way, what it strains against, and what observation would settle it.

---

## What counts as evidence

| material | what it is | how to use it |
|---|---|---|
| a reported passage | what the paper reports happened, was said, or was the case | **evidence.** Every assertion of fact in your reading must be carried by one, cited by the journal's page number |
| the author's characterisation of a passage | the author's own account of what that passage shows | printed, so you may cite it — **as the author's account**, never as what happened |
| a claim | an assertion the paper makes about how something works | the paper's theory. You may disagree with it; you may not use it as evidence for itself |

If anything reads like an argument for why a passage supports a claim, it is
argument, not evidence.

Do not quote more than eight words of the paper in a row. Paraphrase, and cite
the page.

---

## Which readings to write

Find in the paper the material for any of the five moves below, and write
**one reading for each piece of material you use** — each contrast pair, each
claim whose evidence points both ways, each set of units is a separate reading.
Write **at most five readings**.

**You may decline.** If a piece of material cannot support a reading that meets
every rule below, record it under `declined` with the reason, and write no card.
A forced reading is where imports come from. A declined piece of material is a
finding, and it is worth more than a reading that dies at the first check.

### The five moves

- **`construct_fission`** — the paper's concept is doing two jobs. Write a split:
  two sides, X and Y, and the feature that tells them apart. See the split rules.
- **`construct_inversion`** — read the cause as the effect, or re-attribute what
  made the difference. `from_seam` works off a claim whose passages point both
  ways. `from_pair` works off a contrast pair: two episodes the paper holds
  comparable that came out differently; say what varied between them. If more
  than one thing varied, the reading may attribute the outcome to a variable the
  paper does not credit.
- **`boundary_shift`** — printed evidence sits outside the episode as the paper
  bounds it. Move the start or end point and retell.
- **`counterfactual_ending`** — the paper hedges a claim or leaves a question
  unresolved. Read the ending as provisional.
- **`focalization_shift`** — a unit speaks in the paper but carries no central
  claim. Retell from that unit's own printed passages.

---

## The rules

**1. Every assertion of fact names the page that carries it.** Paraphrasing a
passage is fine. Adding a cause, a motive, or a consequence the passage does not
carry is an import, and an import kills the reading.

**2. Watch the connectives.** "Because", "which meant that", "given that",
"since". Plausible causal glue is the commonest way an import gets in, because it
reads as reasoning rather than content.

**3. Do not import knowledge of the setting.** How product development works, how
approval works, how a meeting runs — if no reported passage prints it, you may
not assert it.

**4. Keep the author's account apart from the event.** When the author's
characterisation and the passage it characterises point different ways, that
divergence is material you may use. When you use the author's characterisation,
attribute it to the author. Never put the author's reasons into a participant's
mouth.

**5. Declare what your reading strains against.** Any passage that sits awkwardly
with the reading goes under `strains_against`, with its page and why. A reading may sit
awkwardly with evidence only if it says so. Undeclared contradiction kills it.

**6. Ground the reading.** Every reading names at least one of:

- a **missing fact** — something the paper does not give that bears on a named
  claim. Apply this test: write *if the paper had printed one answer, claim X would
  read ___; if the other, ___*. If the two blanks come out the same, it is not a
  missing fact. Check the whole paper before declaring anything missing.
- a **divergence** — two printed items that point different ways: two passages, or
  a passage and the author's own characterisation of it.

A reading with no named gap and no named divergence has nothing to stand on.

**7. Name the deciding observation.** `what_it_would_take_to_cohere` says what
would settle whether the reading holds. If it is printed, cite the pages. If it
is absent, say so and say where you looked. **Do not claim the observation could
be obtained**, only that it is or is not in the paper.

**8. Leave the register shut.** You are given no list of named distinctions, and
you must not supply one.

### Split rules, for `construct_fission` only

- Describe X and Y **in the paper's own descriptive vocabulary**. No theoretical
  labels.
- The **separating feature** must be something you could code from a passage
  without knowing the outcome the claim explains. Say whether it is.
- Report **how many** of the passages beneath the claim the feature sorts
  correctly, as n of N. Do not judge whether that is enough.
- List the **confounds**: anything that varies with the feature and could be doing
  the work instead — the passages' period, their speaker, their position in the
  paper.
- Name the **rival**: the strongest reading on which no split is needed.

---

## Output contract

Return a single JSON object and nothing else.

```json
{
  "paper": "author and year, as the paper prints them",
  "cards": [
    {
      "card_id": "<move>_01",
      "move": "construct_inversion",
      "trigger": "the material this reading instantiates, e.g. from_pair, with the pages of the two episodes and what varied between them",
      "claim": "the incumbent claim this reading bears on most directly, with its page",
      "incumbent_reading": "one sentence: what the paper claims about this episode",
      "wager": {
        "statement": "the reading, in plain prose",
        "seed_pages": ["p. .."],
        "what_it_would_take_to_cohere": {
          "observation": "...",
          "printed": false,
          "printed_pages": [],
          "basis": "where you looked, and why it is or is not there"
        },
        "strains_against": ["p. .. -- why"],
        "who_could_complete_it": "a kind of person or evidence, not a named individual"
      },
      "passage_jobs": {"p. ..": "what the passage on this page does in the reading, in at least a full clause"},
      "grounded_in": [
        {"kind": "missing_fact", "question": "...", "bears_on": "the claim, with its page",
         "if_one_way": "...", "if_the_other": "..."},
        {"kind": "divergence", "items": ["p. ..", "p. .., or the author's characterisation on p. .."], "how": "..."}
      ],
      "reach": {"same_construct": [], "same_outcome": [], "feature_elsewhere": [], "orphans_used": []},
      "rival": "the strongest reading on which yours is unnecessary",
      "split": null,
      "naming": {"register_version": null, "outcome": "register not opened"}
    }
  ],
  "declined": [
    {"move": "...", "trigger": "...", "why": "..."}
  ]
}
```

Cite by page throughout; where two passages share a page, label them p. 470a,
p. 470b, in every field. `reach` lists, by page, what else in the paper reads
differently under this reading: claims on the same construct, claims on the
same outcome, passages where the separating feature recurs (empty on cards other
than a split), and reported passages that the paper attaches to no claim
(`orphans_used`).

For a `construct_fission` card, `split` is:

```json
{
  "side_x": {"label": "X: ...", "pages": ["p. .."]},
  "side_y": {"label": "Y: ...", "pages": ["p. .."]},
  "separating_feature": "...",
  "independent_of_outcome": "yes / partly / no, and why",
  "sorts_correctly": "n of N",
  "confounds": ["..."]
}
```

---

## What not to do

- Do not write more than five readings.
- Do not assert what no reported passage carries, including what you know about
  the paper from elsewhere.
- Do not treat a claim, or the author's characterisation, as evidence that
  something happened.
- Do not name the sides of a split with a concept from the literature.
- Do not force a reading out of thin material. Decline it.
- Do not soften a reading to make it safer. A reading that survives because it
  claims nothing has failed as surely as one that imports.
