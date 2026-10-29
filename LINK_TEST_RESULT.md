# The link-definition test: the result

*30 September 2026. Who may receive this file: nobody (—). The full output is
`link_test_report.md`; the numbers behind it are in `link_test_results.json`.
Every figure below was checked independently against the answer files and the
key; the corrections are made.*

**Verdict: not passed.** This is under the bar set before any answer was read.
Four of its nine conditions hold. The five failures trace mainly to one judgment:
what the stub shows. A rerun of Opus at extra effort, declared before it ran,
changed little and did not pass either (last section).

---

## What held

- **Claim form.** The two models gave all 33 claims the same form (κ 1.00).
- **The author link**, meaning how the paper uses a passage for a claim. κ 0.69 on
  the 42 random rows, against a bar of 0.60. Its 95% interval is wide, about 0.33
  to 0.93. On the 18 hard rows it is weaker (κ 0.37). Kind (κ 0.69) and use
  (κ 0.76) are also above 0.60 on the random rows, though neither was a bar item
  on its own.
- **The hard cases.** The models agree on the five-value code for 17 of the 18.
  Two coders answering at random agree on 12 or fewer 95% of the time. Neither
  model splits a pair of twins into `with` and `against`. Under v2, the same two
  models agree on 10 of the 18.

## What failed

| on the 42 random rows | result | bar |
|---|---|---|
| evidence link | κ 0.38 (81% agreement) | 0.60 |
| three-value code, v1.1 | κ 0.23 (88%) | 0.60 |
| three-value code, strict | κ 0.00 (98%) | 0.60 |
| link, new rules against v2 | κ difference −0.66 to +0.07 | lower end no worse than −0.10 |
| three-value code, new rules against v2 | κ difference −1.03 to −0.26 | lower end no worse than −0.10 |

Under v2, the same two models agree on the three-value code for 95% of the
random rows (κ 0.88).

The high agreement next to a low κ is not a flaw in the measure. Under the new
rules, `with` is rare on random rows: ChatGPT gave it to 2 rows and Opus to 5, and
they share 1. Almost every row is "neither" for both, so raw agreement is high,
while κ asks whether they agree on which few rows show the claim. They mostly do
not.

## Why: one judgment

The per-claim judgments held, and so did the page judgments on the random rows.
The failure is judgment 1, what the stub shows, and within it mostly the outcome.

- **Outcome agreement is low.** κ 0.43 on the random rows. On the 21 random pairs
  the extractor linked, it is κ 0.14 (13 of 21). Each model coded the outcome
  "as asserted" on 9 random rows, but not the same 9.
- **The evidence link splits on 8 random rows.** 7 are splits on the condition or
  the outcome. In each of those 7, one model's reason says the stub shows it
  "partly", or does not show it "explicitly". The eighth is a split on kind.
- **Where the models part.** Whenever either model called a showing partial, it
  counted it as shown. The splits come where one model saw a partial showing and
  the other saw none, or where ChatGPT declined to count what the stub did not
  show "explicitly". On R49, ChatGPT counted a partial outcome; Opus saw none.
- **What the rule says.** It reads: "If the stub shows the condition or the
  outcome only in part, code what it shows and say 'partly' in your reason." It
  does not say outright that a partial showing counts as shown. The code table
  implies it does, since it keeps `not shown` for a stub that "says nothing
  about" the outcome. Neither says what counts as part of an outcome, and that is
  where the models part.
- **The outcome splits across all 60 rows.** There are 10. Six turn on partial
  showings. Two turn on the `maps` rule, where the printed direction does not say
  which kind goes with which condition. Two turn on a figure that does not pair
  categories with outcomes. Opus marked 8 of the 10 unclear; ChatGPT marked none.

**Kind** split on 6 random rows. Four rows (three passages; F18 appears twice)
are passages where the author states a pattern across cases, the kind of passage
the voice test could not place. The other two are descriptions of a practice that
carry the author's interpretation. Only one of the six (R54) changed the evidence
link. In the other five, the model that said `report` gave no link anyway: the
stub showed neither the condition nor the outcome (four rows), or the passage
restates the claim (R23).

## How rare evidence links are under these rules

Of the 21 random pairs the extractor linked, ChatGPT kept 4 as evidence links and
Opus 7. Both kept the same 2 (R26, R60). Most of the extractor's links became
"no link" for one of three reasons: the stub shows neither the condition nor the
outcome, the passage is a reading, or it restates the claim.

The seam detector counts only `with` and `against` links from reported passages,
and needs at least 4 per claim. Among the same 21, the extractor coded 11 `with`,
5 of them on reported passages. Opus's derived codes keep 3 of those 5; ChatGPT's
keep none. (ChatGPT's one `with` among the 21, R49, was an extractor
`illustrates`.) How many detector links the new rules would leave is exactly what
the two models disagree on.

## The page re-check

Reading the passage instead of the stub changed the derived code on 4 of the 15
re-check rows for each model. In 6 of those 8 changes, the page showed a
condition or an outcome the stub did not, and each moved toward more evidence.
The other two turned on the other-cause judgment, one each way.

## The PI's sheet

This is a sense check, not gated. On the PI's 20 rows:

| | matches ChatGPT | matches Opus |
|---|---|---|
| three-value code | 20 | 17 |
| evidence link | 19 | 16 |
| author link | 16 | 17 |

## Confounds

- **Opus's setting.** Opus ran at medium effort; maximum had been
  recommended. The evidence-link splits turn on partial showings, which
  points to a gap in the rules. But every unclear mark came from Opus, the model
  whose setting is in question, so the setting could not be ruled out. *Settled
  by the rerun:* at extra effort Opus changed only 4 of its 60 derived codes (last
  section).
- **ChatGPT's setting** was not recorded.
- **Who wrote the claims.** ChatGPT 5.6, which is also one of the two coders.
- **Sample size.** On 42 random rows, a κ's 95% interval spans about ±0.2 to ±0.4.
  The author link's 0.69 runs from about 0.33 to 0.93, so its pass is not secure
  either. The evidence link's 0.38 runs from 0.00 to about 0.7.
- **The v2 arm's text.** It keeps v2's base-rate lines and the stubs' voice
  markers.

## What the protocol says next

The failed rule is revised as version 2 and tested on a fresh draw. It is not
patched and scored again on these rows.

- **To revise:** judgment 1's threshold for "shows", meaning what counts as part of
  a condition or an outcome, and whether a partial showing counts. Possibly also
  kind, for patterns the author states across cases.
- **To keep:** claim form, use, and the author link.
- **To decide first:** whether judgment 1 should be made from the stub at all. The
  page re-check and the rarity of stub-based evidence links both point toward
  judging it from the passage.

---

## The Opus rerun at extra effort

*A diagnostic, declared in `LINK_TEST_PLAN.md` before it ran. The verdict above
stands. The rerun's full output is `link_test_report_B.md`.*

**Opus's answers barely changed.** Both Opus chats were rerun at extra effort
(run B). Against its answers at medium (run A), from `link_test_compare_runs.py`:

| | same in A and B |
|---|---|
| claim form | 33 of 33 claims |
| kind, use | 59 of 60 rows each |
| outcome | 57 of 60 |
| condition | 54 of 60 |
| evidence link | 58 of 60 |
| derived code (v1.1) | 56 of 60; changed on R25, R31, R49 and R57 |
| v2 arm: link | 58 of 60 |
| v2 arm: direction code | 50 of 60 |

So the setting is not what made the two models disagree.

**Scored against ChatGPT** with the same script and bar, the rerun does not pass
either. Four of the nine conditions hold again, but not the same four:

| on the 42 random rows | run A (medium) | run B (extra) |
|---|---|---|
| author link | κ 0.69, passes | κ 0.598, just under the bar |
| evidence link | κ 0.38 | κ 0.44 |
| three-value code, v1.1 | κ 0.23 | κ 0.64, passes |
| three-value code, strict | κ 0.00 | κ 0.00 |
| link against v2, lower end | −0.66 | −0.61 |
| three-value code against v2, lower end | −1.03 | −0.74 |
| hard rows agreed (beyond chance: 13 or more) | 17 of 18 | 17 of 18 |

On the PI's 20 rows, Opus B's three-value codes match the PI's on all 20, where
Opus A's matched on 17. Reading the page changed Opus B's code on 2 of the 15
re-check rows, against 4 for Opus A.

**How fragile κ is on 42 rows.** The three-value code changed on three random rows
(R31, R49 and R57). On all three, Opus B now agrees with ChatGPT, and that alone
lifted the κ from 0.23 to 0.64. One changed row (R40) moved the author link from 0.69
to just under 0.60. With `with` so rare, a κ on 42 rows swings on a handful of rows.
The next test needs more rows, or a bar that allows for this.

**What it means for the next step.** The diagnosis stands. The failure is in the
rules, at judgment 1's threshold for "shows", not in the Opus setting. Version 2
of that judgment goes ahead as described above.
