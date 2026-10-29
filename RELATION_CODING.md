# How each reading relates to the paper's claims

You have three files besides this one: a published qualitative paper, as a
PDF; a list of the paper's claims, numbered, each with its statement and the
pages where the paper makes it; and a file of readings of the paper, numbered
R01 onward. A statement in the list is a summary, not the paper's words: check
the page.

Each reading proposes another way of reading the paper's own account. Your
task is to say, for each reading, which of the paper's claims it bears on and
what it does to each of them. You do not judge whether a reading is right,
well supported or worth pursuing: only what it does to the claims.

## What to give for each reading

1. **main_claim:** the number of the claim the reading bears on most directly,
   or `none` if it bears on no claim in the list.
2. **main_type:** what the reading does to its main claim: one of the six types
   below, or `none` exactly when main_claim is `none`.
3. **other_claims:** up to two more claims the reading also bears on, each with
   its type. Leave the list empty if there are none. A claim appears once per
   reading.
4. **reason:** one sentence: why this type on the main claim.
5. **page:** the page of the paper your main type rests on.

## The six types

For one reading and one claim, one type:

- `inverts`: the reading holds that the claim's outcome goes the other way
  under the condition the claim names, or that a process the claim states runs
  in the reverse order.
- `other_mechanism`: the reading keeps the claim's outcome but puts a
  different mechanism or cause in place of the paper's.
- `rereads_evidence`: the reading takes passages the paper itself offers for
  the claim and reads them so that they no longer support it as stated.
- `challenges_premise`: the reading questions something the paper's account of
  the claim takes for granted (a premise, a category, a boundary), rather than
  its outcome or its mechanism.
- `complements`: the reading adds a mechanism, a condition or a level to the
  claim, or changes its scope, without denying it.
- `restates`: the reading says what the claim already says.

**If more than one type fits, give the first that fits in the order above.**

## An example

From a made-up paper, not the one attached. Its claims: **C1** (p. 4), cooks
under time pressure skip the tasting step because they value speed over care;
**C2** (p. 7), head chefs who taste every dish themselves keep the step alive.

- **R1:** "Cooks under time pressure taste more, not less, since a mistake costs
  more when the pass is full." C1, `inverts`.
- **R2:** "The step is skipped because the recipe cards go missing in the rush,
  not because cooks value speed." C1, `other_mechanism`.
- **R3:** "The paper's own episodes of skipping all fall on nights the head chef
  was away; read again, they show missing supervision, not speed." C1,
  `rereads_evidence`.
- **R4:** "The paper treats tasting as one step; in these kitchens it is three
  different checks, and only one is ever skipped." C1, `challenges_premise`.
- **R5:** "Head chefs keep the step alive only in kitchens with a separate pass
  station." C2, `complements`.
- **R6:** "Where the head chef tastes every dish, the kitchen keeps tasting."
  C2, `restates`.

In R2, the same reading might also be said to add a condition to C1; the order
of the types decides: `other_mechanism` comes first.

## Rules

- Code every reading in the file, once, in its order.
- Read the paper. A page in a reading is a pointer, not a proof.
- Code each reading on its own words, whoever may have written it.
- Do not quote more than eight words of the paper in a row. Paraphrase, and
  cite the page.
- Work only from the paper and these files. Do not search the web.

## What to return

A single JSON object and nothing else, as a file if you can, otherwise as one
code block:

```json
{
  "paper": "author and year, as the paper prints them",
  "codes": [
    {
      "reading": "R01",
      "main_claim": "C03",
      "main_type": "other_mechanism",
      "other_claims": [{"claim": "C07", "type": "complements"}],
      "reason": "...",
      "page": "p. .."
    }
  ]
}
```
