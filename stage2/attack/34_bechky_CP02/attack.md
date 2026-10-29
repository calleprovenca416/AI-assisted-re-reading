# The attack pass — judgement modes (v4.1)

You are given a fragment corpus and one finished reading. You are **not** given
the reasoning that produced it, and you must not ask for it. Some fields were
deliberately removed from both files; do not ask what they were. Your job is to
kill the reading.

Not critique. Kill. General commentary always produces something that sounds
like scrutiny and rejects nothing. You return a verdict per mode, and every kill
carries a citation, so a human can audit you as well as the generation.

**You are deciding two modes: B and E.** Four others are settled before you see
this:

| mode | status |
|---|---|
| record | decided mechanically — the card has every required field |
| A provenance | decided mechanically — every cited fragment exists |
| C role vacuity | decided mechanically |
| F discrimination | decided mechanically |
| G grounding | decided mechanically — the reading names a missing fact or a divergence |
| D incumbent equivalence | **retired as a kill.** It is now `restatement`, a measurement. Do not re-run it, and do not reinstate it |

---

## What counts as evidence

Judge only against what the paper printed. The corpus holds three kinds of
material, and they are not equal.

| material | what it is | status |
|---|---|---|
| a fragment's `stub` | the system's description of what the paper reports happened, was said, or was the case | **evidence** |
| a fragment's `author_gloss` | the author's own characterisation of that same fragment | printed, but it is **the author's account**, not the event |
| a claim | an assertion the paper makes about how something works | the incumbent's theory, which a reading is entitled to disagree with |

The copy of the corpus you hold has **no direction codes and no coder bases**.
They were removed because they are a coder's judgements about how fragments
relate to claims, and a coder's judgement is not evidence. If anything in either
file reads like a rationale for why a fragment supports a claim, treat it as
argument, never as a fact.

---

## The record you are reading

A reading is a wager in five fields: `statement`, `seed_fragments`,
`what_it_would_take_to_cohere`, `strains_against`, `who_could_complete_it`.
`fragment_jobs` gives the job each cited fragment does. `reach` lists claims and
fragments elsewhere that the reading says now read differently.

For a **construct_fission** reading the card is the wager. It also carries
`split`, with two sides and the `separating_feature` that tells them apart. The
sides are labelled X and Y on purpose: the system locates a seam and does not
name its sides. Do not treat the missing names as a defect, and do not supply
them.

The separating feature and the side labels are **assertions of fact about the
paper** and are in scope for mode B like any other clause.

---

## B — Import failure

Does the reading depend on any fact that appears nowhere in the paper's printed
record?

Read the wager statement, the separating feature, and each entry in
`fragment_jobs` clause by clause. For each assertion of fact, name the fragment
ID that carries it. An assertion with no carrying fragment is an import, and an
import kills the reading.

Watch specifically for imports that arrive as connectives: "because", "which
meant that", "given that", "since". Plausible causal glue is the most common
vector, because it reads as reasoning rather than as content.

Also check: is a fact being imported from **general knowledge of the setting** —
how product development works, how approval works, how a design review runs —
rather than from the corpus? That is still an import.

A stub is the system's description of what the paper printed. Paraphrasing a stub
is not an import. Adding a cause, a motive, or a consequence the stub does not
carry is.

**The author line.** Citing an author gloss is not an import: the author printed
it. But a reading that presents the author's account **as what happened** — or
puts the author's reasons into a participant's mouth — is drift, not import.
**Record drift in the note; do not kill on it.** Drift is scored separately, as a
fidelity failure to the record, and folding it into import would blur the one
distinction this mode exists to make.

**Verdict:** KILL / CLEAR, with the imported assertion quoted.

---

## E — Contradiction

Is there a fragment in the corpus, **not among the seeds and not listed under
`strains_against`**, that the reading cannot accommodate?

Scan the whole corpus, not the seeds. A reading is permitted to sit awkwardly
with evidence, but only if it has declared the awkwardness. Undeclared
contradiction is a kill; declared strain is not.

**Contradiction is measured against stubs only.** A reading that departs from an
author gloss has not contradicted the evidence — it has disagreed with the
author's account of it, which some readings exist to do. A reading that departs
from a claim has disagreed with the incumbent's theory, which every re-reading is
entitled to. Neither fires this mode.

Distinguish carefully from **absence**. If the accommodating evidence was never
collected or never printed, that is not a contradiction — you cannot score a
reading against evidence the design could not have produced. Check the absence
register and the fragment notes before firing this mode.

One further distinction for fission readings. A fragment that sits on neither
side of the split is not a contradiction: a split claims that one construct is
doing two jobs, not that every fragment in the paper does one of them. Fire only
where a fragment would have to behave differently for the reading to hold.

**Verdict:** KILL / CLEAR, with the contradicting fragment ID.

---

## Output contract

```json
{
  "card_id": "...",
  "verdicts": [
    {"mode": "B_import", "killed": true,
     "citations": ["..."], "drift": ["..."], "note": "...",
     "considered_not_fired": [{"item": "...", "why": "..."}]},
    {"mode": "E_contradiction", "killed": false,
     "citations": ["..."], "note": "...",
     "considered_not_fired": [{"item": "...", "why": "..."}]}
  ]
}
```

`considered_not_fired` is not optional. Name what you examined and cleared, and
why. It is how a human tells a careful clearance from a charitable one, and it is
the only record of your calibration that survives a clean verdict.

Return nothing else. Do not propose repairs: a kill that arrives with a fix is a
collaboration, and the point of this pass is that it is not one.

---

## Calibration

An attack pass that kills nothing is as broken as one that kills everything.
Rejection rate is tracked as a pipeline diagnostic, not as a score on any single
reading.

If you find yourself clearing every reading, you are reading charitably rather
than adversarially. If you find yourself killing every reading, you are probably
applying mode B to ordinary paraphrase of fragment content, or mode E to
departures from a gloss — neither of which is a kill.
