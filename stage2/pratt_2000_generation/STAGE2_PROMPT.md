# Stage 2 — writing readings (v4.1)

You are given two files about one published qualitative paper: a **dossier**,
which reports what an audit of the paper located, and the paper's **corpus**,
which records the evidence the paper printed and the claims it makes. You are not
given the paper itself, and you must not use anything you know or can recall
about it. Everything you write must rest on the corpus.

Your job is to write **readings**: plausible re-tellings of the paper's own
account that use its printed evidence in a way the paper does not.

---

## What a reading is, and is not

A reading is **plausible, not rival**. You are not trying to show the author was
wrong. Write the best reading the audit's material supports. If it ends up close
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
| a fragment's `stub` | the system's description of what the paper reports happened, was said, or was the case | **evidence.** Every assertion of fact in your reading must be carried by one, named by ID |
| a fragment's `author_gloss` | the author's own characterisation of that fragment | printed, so you may cite it — **as the author's account**, never as what happened |
| a claim | an assertion the paper makes about how something works | the paper's theory. You may disagree with it; you may not use it as evidence for itself |
| a link's `direction` | a coder's judgement of how a fragment behaves under a claim | **not evidence.** It tells you where the audit looked. Never write "F03 runs against C1, therefore". Write what F03 prints |
| fragment `notes` | facts about the printed text, such as a figure the paper does not resolve | use them to tell what is absent from what is contradicted |

There are no coder rationales in your files. If anything reads like an argument
for why a fragment supports a claim, it is argument, not evidence.

---

## Which readings to write

Section 9 of the dossier, **MOVE PARAMETERS**, lists each move the audit found
material for, and the material. Write **one reading for each entry** — each
contrast pair, each seam, each set of units is a separate reading. Write nothing
for moves that are not listed, and nothing for `seed_fragments` or
`research_questions_only`, which are not moves.

**You may decline.** If an entry's material cannot support a reading that meets
every rule below, record it under `declined` with the reason, and write no card.
A forced reading is where imports come from. A declined entry is a finding, and
it is worth more than a reading that dies at the first check.

### The five moves

- **`construct_fission`** — the paper's concept is doing two jobs. Write a split:
  two sides, X and Y, and the feature that tells them apart. See the split rules.
- **`construct_inversion`** — read the cause as the effect, or re-attribute what
  made the difference. `from_seam` works off a claim whose fragments point both
  ways. `from_pair` works off a contrast pair: two episodes the paper holds
  comparable that came out differently, and the pair's `differs_in` note says what
  varied between them. If more than one thing varied, the reading may attribute
  the outcome to a variable the paper does not credit.
- **`boundary_shift`** — printed evidence sits outside the episode as the paper
  bounds it. Move the start or end point and retell.
- **`counterfactual_ending`** — the paper hedges a claim or leaves a question
  unresolved. Read the ending as provisional.
- **`focalization_shift`** — a unit speaks in the paper but carries no central
  claim. Retell from that unit's own printed fragments.

---

## The rules

**1. Every assertion of fact names the stub that carries it.** Paraphrasing a stub
is fine. Adding a cause, a motive, or a consequence the stub does not carry is an
import, and an import kills the reading.

**2. Watch the connectives.** "Because", "which meant that", "given that",
"since". Plausible causal glue is the commonest way an import gets in, because it
reads as reasoning rather than content.

**3. Do not import knowledge of the setting.** How product development works, how
approval works, how a meeting runs — if no stub prints it, you may not assert it.

**4. Keep the author's account apart from the event.** When a gloss and its stub
point different ways, that divergence is material you may use. When you use a
gloss, attribute it to the author. Never put the author's reasons into a
participant's mouth.

**5. Declare what your reading strains against.** Any fragment that sits awkwardly
with the reading goes under `strains_against`, with why. A reading may sit
awkwardly with evidence only if it says so. Undeclared contradiction kills it.

**6. Ground the reading.** Every reading names at least one of:

- a **missing fact** — something the corpus does not give that bears on a named
  claim. Apply this test: write *if the paper had printed one answer, claim X would
  read ___; if the other, ___*. If the two blanks come out the same, it is not a
  missing fact. Check the whole corpus before declaring anything missing.
- a **divergence** — two printed items that point different ways: two stubs, or a
  stub and its own gloss.

A reading with no named gap and no named divergence has nothing to stand on.

**7. Name the deciding observation.** `what_it_would_take_to_cohere` says what
would settle whether the reading holds. If it is printed, cite the fragments. If
it is absent, say so and say where you looked. **Do not claim the observation
could be obtained**, only that it is or is not in the record.

**8. Leave the register shut.** You are given no list of named distinctions, and
you must not supply one.

### Split rules, for `construct_fission` only

- Describe X and Y **in the paper's own descriptive vocabulary**. No theoretical
  labels.
- The **separating feature** must be something you could code from a fragment
  without knowing the outcome the claim explains. Say whether it is.
- Report **how many** of the claim's fragments the feature sorts correctly. Do not
  judge whether that is enough.
- List the **confounds**: anything that varies with the feature and could be doing
  the work instead — the fragments' period, their speaker, their position in the
  paper.
- Name the **rival**: the strongest reading on which no split is needed.

---

## Output contract

Return a single JSON object and nothing else.

```json
{
  "paper_id": "...",
  "cards": [
    {
      "card_id": "<paper>_<move>_<trigger>_01",
      "paper_id": "...",
      "move": "construct_inversion",
      "trigger": "the dossier entry this reading instantiates, e.g. from_pair CP01",
      "claim": "the incumbent claim this reading bears on most directly",
      "incumbent_reading": "one sentence: what the paper claims about this episode",
      "wager": {
        "statement": "the reading, in plain prose",
        "seed_fragments": ["F.."],
        "what_it_would_take_to_cohere": {
          "observation": "...",
          "printed": false,
          "printed_fragments": [],
          "basis": "where you looked, and why it is or is not there"
        },
        "strains_against": ["F.. -- why"],
        "who_could_complete_it": "a kind of person or evidence, not a named individual"
      },
      "fragment_jobs": {"F..": "what this fragment does in the reading, in at least a full clause"},
      "grounded_in": [
        {"kind": "missing_fact", "question": "...", "bears_on": "C..",
         "if_one_way": "...", "if_the_other": "..."},
        {"kind": "divergence", "items": ["F..", "F.. or F.. gloss"], "how": "..."}
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

For a `construct_fission` card, `split` is:

```json
{
  "side_x": {"label": "X: ...", "fragments": ["F.."]},
  "side_y": {"label": "Y: ...", "fragments": ["F.."]},
  "separating_feature": "...",
  "independent_of_outcome": "yes / partly / no, and why",
  "sorts_correctly": 0,
  "confounds": ["..."]
}
```

---

## What not to do

- Do not write a reading for a move the dossier does not list.
- Do not assert what no stub carries, including what you know about the paper.
- Do not treat a direction code, a claim, or a gloss as evidence that something
  happened.
- Do not name the sides of a split with a concept from the literature.
- Do not force a reading out of thin material. Decline it.
- Do not soften a reading to make it safer. A reading that survives because it
  claims nothing has failed as surely as one that imports.
