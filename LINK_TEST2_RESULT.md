# The second link-definition test: the result

*5 October 2026, with additions of 5 and 6 October. Who may receive this file:
nobody (—). The full output is `link_test2_report.md`; the numbers behind it are
in `link_test2_results.json`. A dagger (†) after a heading, a point or a
sentence marks figures that are not in the report: they were worked out from the
answers after the scoring, and none was fixed in advance. Where a run was
declared before it was made, the words "found by looking" mark a figure that was
not among those declared. Every figure was checked independently against the
files and worked out again; the corrections are made. The additions are the
rerun of chat C1a, run B (the declared second run of the four coder chats) and
run C (the two ChatGPT chats run once more with another model setting), each
outside the test. Through them the verdict and every figure of the test stand.*

**Verdict: not passed.** This is under the bar set on 3 October, before any
marker existed. Three of its five conditions hold. The evidence link and the
three-value code do not. No top-up is due.

**In short.**

- As in the first test, the two coders part on judgment 1: what a passage shows
  of a claim's condition and outcome.
- Kind held, with the new `pattern`. The author link held, though not securely.
- Most of the disagreement sits in the first half of the rows (table 1). That
  was found after the result, and the test cannot say whether it comes from
  the chats or from the rows.
- **The sheet is not an independent human reading.** It was made by Fable 5.1 at
  max, in an incognito chat, and validated by the PI, who changed no cell. It
  gives the 20 rows the same evidence link and the same two codes as coder 2.
  Fable is a Claude model, as coder 2 is. This test has no independent human
  reading.
- **Chat C1a was run a second time, by the PI.** That run is outside the test
  and changes nothing in the verdict. It is one chat, and it was not declared
  before it ran. By the PI's account it was set up exactly as the first run, and
  made before the four files were sent, so before any result. In it coder 1
  reads table 1 as sparingly as before: it finds the claim's condition or its
  outcome shown on 8 of the 63 rows of that half that count for the bar, as in
  the first run. 13 of that half's 16 disagreements with coder 2 on the evidence
  link are still there. Where coder 1 does find something, its two runs agree
  only in part. With the rerun in the place of the first run, the bar still does
  not hold.
- **Run B, the declared second run of all four chats, is in.** What would be
  compared was fixed before any of its chats was opened. It is outside the test
  and changes nothing in the verdict.
  - Each coder mostly repeats itself, and not on every link. Between its two
    runs the evidence link's κ is 0.73 for coder 1 and 0.83 for coder 2. Of
    the rows with a link in either run, coder 1 has the link in both on 11 of
    18, and coder 2 on 22 of 29.
  - On the three codes of the bar the two coders agree with each other less
    than each agrees with itself, whichever run of the one is set beside
    whichever run of the other (four pairings): on the evidence link κ 0.41
    to 0.64. The bar holds under none of the four.
  - Most of coder 2's first-half links came back: 14 of 19.
  - The gap between the two halves came back too, for both coders. So it
    goes with table 1's rows, and not with how one chat happened to run.
- **Run C, a second declared diagnostic, is in,** on whether the results would
  differ with other model settings. Run C is the two ChatGPT chats run once more
  with GPT 6 Astra at max. What would be compared was fixed before any chat was
  opened. It is outside the test and changes nothing in the verdict.
  - Under the bar's way of counting, with GPT 6 Astra at max in coder 1's
    place both links are above 0.60 beside either run of coder 2: the author
    link at κ 0.68 and 0.70, and the evidence link at 0.72 and 0.68. No
    pairing of the test's two coders gave that. The three-value code is again
    too few to tell.
  - What carries the evidence link over 0.60 is links that rest on a name
    alone, which GPT 6 Astra gives as coder 2 does. With names not counted,
    and all else as the bar has it, the evidence link reads 0.52 and 0.57,
    below 0.60 (found by looking).
  - It is one run. Between its own two runs coder 1 moved by 0.17 and 0.18 on
    the evidence link beside the same run of coder 2, and GPT 6 Astra stands
    above coder 1's better run by 0.14 and 0.03. So how much of the
    difference is the setting cannot be told.
  - The intervals are wide: for both links the lower ends are below 0.60.
  - It is not a pass. The rows are the ones the rules failed on, and GPT 6
    Astra was not the test's coder.
- **No third test is made for this package** (decided on 6 Oct): the results go
  into the proposal as findings about the instrument. See the end of this note.

**Words used here.** The *author link*: the paper itself uses the passage for
the claim. The *evidence link*: the passage reports something that shows the
claim's condition or its outcome, holding or not holding, whether or not the
paper draws the connection. A passage that is the author's own reading, or that
restates the claim, never carries one. The *five-value code* on an evidence link
is `with`, `against`, `illustrates`, `qualifies` or no link; the *three-value
code* is `with`, `against` or neither. A `with` *on the outcome only* shows the
claim's outcome going the asserted way, and not its condition. The *top-up* is
60 more rows, run only if condition 3 is "too few to tell" and the other four
hold. Coder 1 is ChatGPT, and coder 2 is Claude Opus 5.5. *The sheet* is the 20
rows coded in a chat of their own: by Fable 5.1, which is also a Claude model,
and validated by the PI.

---

## The bar

Read on the 120 random rows, between the two coders, counted as fixed in
advance: the main reading, names counted, patterns as reports, carried-out
markers not counted.

| condition | found | 95% interval | result |
|---|---|---|---|
| 1. author link, κ of at least 0.60 | κ 0.65; agreed on 106 of 120 | 0.45 to 0.80 | holds |
| 2. evidence link, κ of at least 0.60 | κ 0.41; agreed on 100 of 120 | 0.19 to 0.61 | does not hold |
| 3. three-value code, κ of at least 0.60 | κ 0.25; agreed on 110 of 120 | −0.05 to 0.56 | not passed |
| 4. hard rows | agreed on 13 of 18; two coders answering at random agree on 10 or fewer 95% of the time; no twin pair split between `with` and `against` | — | holds |
| 5. `not found`, at most 6 for either coder | 0 and 0 | — | holds |

- **Why no top-up.** The top-up is run only when the other four conditions
  hold, and condition 2 does not. Condition 3 also reads "not passed" and not
  "too few to tell": between them the coders gave `with` or `against` to 12 of
  the 120 rows, which is not fewer than 5; and though each gave fewer than 10
  (5 and 9), κ's interval ends at 0.56 and does not include 0.60. So `topup`
  was not run, and the recorded seed has had its one use.
- **How far from the bar.** The estimates are 0.41 and 0.25 against 0.60. Both
  intervals exclude 0.70. The three-value code's also excludes 0.60; the
  evidence link's just reaches it (0.61). The plan's figures: rules whose true
  κ is 0.70 fail about one time in three by chance, and rules at 0.50 or less
  pass about once in 100.
- **No way of counting would have passed.** Across all 32, on the 120 rows, the
  evidence link's κ runs from 0.32 to 0.44 and the three-value code's from 0.00
  to 0.48. The report gives each with its interval.

## What held

- **Kind.** κ 0.93 (0.86 to 0.99), agreed on 115 of 120. The third kind,
  `pattern`, was given to 52 and 53 of the 120 rows.
- **Use, and the author link.** Use is κ 0.70 (0.54 to 0.83), and the author
  link κ 0.65 (0.45 to 0.80). The pass is not secure. On the 60 linked rows
  alone the author link is κ 0.53 (0.29 to 0.73) and use κ 0.595 (0.39 to
  0.76), both under 0.60. The near rows lift the pooled figure: there the
  coders agree on the author link on 59 of 60.
- **The hard rows.** Agreed on 13 of 18. That is more than under brief v2 (10)
  and fewer than under version 1.1 (17). Neither coder gave `against` or
  `qualifies` to any of the 148 rows, so no twin pair could be split.
- **The materials.** No row is `not found`. No line had to be asked for again.
  No return was one that the rules' order cannot give.

## What failed

| on the 120 rows | neither coder | both | coder 2 only | coder 1 only | κ |
|---|---|---|---|---|---|
| an evidence link | 90 | 10 | 17 | 3 | 0.41 |
| `with` | 108 | 2 | 7 | 3 | 0.25 |

- Coder 1 gives an evidence link to 13 rows and coder 2 to 27. They share 10.
- Agreement looks high because most rows are "no link" for both. κ asks whether
  the coders agree on which few rows carry a link. Mostly they do not.
- With no `against`, the three-value code is a test of `with` alone. Coder 1
  gave 5, all on the outcome only. Coder 2 gave 9: 3 with the condition and 6
  on the outcome only. They share two rows (R078, R118).

## Why: judgment 1 again †

- **Of the four main judgments, the condition and the outcome agree least.**
  κ 0.43 (0.18 to 0.64) and κ 0.47 (0.22 to 0.69), against 0.93 for kind and
  0.70 for use. (These four figures are the report's.)
- **17 of the 20 disagreements on the evidence link turn on judgment 1 alone.**
  Give both coders the same judgment 1, whichever coder's it is, leave each
  one's kind and use as they are, and the two derived links agree. Two of the
  other three turn on use: one coder calls the passage a restatement (R074,
  R086). The last needs judgment 1 and kind together (R010).
- **One coder finds nothing, and the other finds something.** In 16 of the 20,
  coder 1's reason for judgment 1 is "no marker" and coder 2 has a link. Coder
  2's link rests on a marker it lists in 8 of them, on a name alone in 6, and
  on the contrary of a marker in 2.
- **Only coder 2's reasons say why.** "No marker" is what the reply form asks
  for when a coder finds none, and it is coder 1's whole reason on 100 of the
  120 rows. So what follows is read from coder 2's reasons alone.
- **Coder 2 says where it doubts.** On seven of the 120 rows its reason has a
  "though": the showing is close to a step away, rests on few words, or may be
  the author's. It counts the showing all the same. On all seven the coders
  disagree. Coder 2 marked 30 of the 120 rows unclear in judgment 1; the
  coders disagree on the evidence link on 15 of those 30, and on 5 of the
  other 90. Coder 1 marked no row unclear.
- **What the rules say.** Part A says that a showing which needs something
  added is not a showing, and its examples code "a step away" as `not shown`.
  What it lacks is a rule for doubt about whether something is added. Rule 4
  asks only for a best answer and the mark `unclear`. Coder 2 counted all
  seven of its "though" rows, and of the 30 rows it marked unclear it coded a
  condition or an outcome as shown on 18 and gave an evidence link to 17.
  Coder 1 gave no sign of seeing a doubtful case at all.
- **Names.** Six of the 20 rest on a word that coder 2 takes as a name and
  coder 1 does not. `named` itself agrees poorly: κ 0.30 (−0.04 to 0.65) on
  the condition and 0.33 (−0.04 to 0.70) on the outcome. Setting names aside
  does not help: six of the 20 disagreements go, two new ones come, and the
  coders then agree on 104 rows instead of 100; but κ falls to 0.32 (0.06 to
  0.55), because fewer rows carry a link.
- **Contraries.** Coder 1 coded no outcome `other way` on any of its 148 rows.
  Coder 2 did on 7.
- **The two that are left.** On R016, coder 1 codes a tagged condition `absent`
  from the contrary of its one `working` marker, and coder 2 finds nothing that
  rules it out. On R134, coder 2 sets the outcome aside under the rule for
  different cases.

**Parts of the rules this sample did not exercise.** `bounded` was never
`yes`, for either coder, on any of the 148 rows. Other cause was `yes` once
(coder 2, R140), so its κ of 0.00 (119 of 120) says little. Use was never
`qualification`. So nothing here tests `against`, `qualifies`, or the rules for
a boundary and for another cause.

## The two halves †

*Not part of the bar. Found by looking, after the result.*

Each coder's rows are in two chats: R001 to R074 (table 1, chats C1a and C2a)
and R075 to R148 (table 2, chats C1b and C2b). The row numbers were shuffled at
the draw, so each half is a random half. Of the bar's 120 rows, 63 are in the
first half and 57 in the second.

| on the bar's rows | first half: 63 rows | second half: 57 rows |
|---|---|---|
| author link | κ 0.58 (0.32 to 0.80); 53 of 63 | κ 0.74 (0.44 to 0.94); 53 of 57 |
| evidence link | κ 0.24 (0.01 to 0.47); 47 of 63 | κ 0.71 (0.37 to 0.94); 53 of 57 |
| three-value code | κ 0.00; 56 of 63 (coder 1 gave no `with` here) | κ 0.55 (0.00 to 1.00); 54 of 57 |
| condition | κ 0.28 (−0.04 to 0.58); 52 of 63 | κ 0.64 (0.20 to 0.92); 53 of 57 |
| outcome | κ 0.20 (−0.08 to 0.51); 52 of 63 | κ 0.77 (0.47 to 1.00); 54 of 57 |
| kind | κ 0.87 (0.74 to 0.97); 58 of 63 | κ 1.00; 57 of 57 |
| use | κ 0.63 (0.42 to 0.82); 52 of 63 | κ 0.79 (0.57 to 0.95); 53 of 57 |

The coders disagree on the evidence link on 16 rows of the first half and on 4
of the second. In the first half, 15 of the 16 are rows where only coder 2 has
a link. In the second, the 4 are two each way.

**Both coders code differently in the two halves, in opposite directions.**

| rows of the bar on which a coder gives | coder 1: first, second half | coder 2: first, second half | both coders: first, second |
|---|---|---|---|
| an evidence link | 5 and 8 | 19 and 8 | 4 and 6 |
| `with` | 0 and 5 | 7 and 2 | 0 and 2 |
| a condition or an outcome as shown | 8 and 12 | 19 and 13 | 5 and 10 |
| a marker listed as shown | 1 and 8 | 10 and 10 | 0 and 8 |
| a code marked `named`, on either side | 6 and 3 | 10 and 2 | 4 and 1 |
| judgment 1 marked unclear | 0 and 0 | 20 and 10 | — |

- **Coder 2** lists markers at the same rate in both halves, but gives 19 links
  in the first and 8 in the second. Eight of its first-half links rest on a
  name alone, against one in the second. All seven of its "though" rows are in
  the first half.
- **Coder 1's** number of links hardly moves, but what they rest on does. None
  of its 5 first-half links rests on a marker (4 on a name, 1 on a contrary).
  Six of its 8 second-half links do.
- **Kind gives a direct look at coder 1's two chats.** Kind is a judgment of
  the passage alone, and 22 fragments have rows in both tables. Coder 2 gives
  each of them one kind throughout. Coder 1 does not for three. It gives F27
  and F51 one kind in its first chat and another in its second, and it gives
  F86 two kinds inside its first chat. All five rows on which the two coders
  disagree on kind are first-chat rows on those three fragments. In its second
  chat, coder 1 gives each the kind coder 2 gives.
- **The halves are not quite alike in what they hold.** Each has 30 near rows;
  they have 33 and 27 linked rows, and 22 and 21 rows on author's-account
  fragments. But the first half has 11 rows that the extractor coded `with` on
  a passage it marked as reported, and the second has 3. Five of the first
  half's 16 disagreements are on those 11 rows. Without the 14 rows, the
  disagreements are 11 of 52 against 4 of 54.
- **How likely by chance.** For the count of disagreements, 16 against 4:
  about once in 130 (Fisher's exact test, p = 0.0075). For the gap in κ itself,
  0.24 against 0.71: about once in 40 (p = 0.025, worked out exactly over
  every way the 120 rows can fall into halves of 63 and 57). Both were looked
  for after the result, among other comparisons, so they count for less than
  that.
- **What this shows, and what it does not.** Some of the gap can be the rows.
  Kind shows that coder 1 judged the same passages differently in its two
  chats, and on F86 within one chat. But only one of the first half's 16
  disagreements turns on kind (R010), and the gap is in judgment 1. Whether
  the same holds there the test cannot say, because each row was coded once
  by each model. (Chat C1a has since been run a second time, outside the
  test: see "Outside the test: the rerun of chat C1a". And all four chats
  have been run again in run B, where the gap between the halves comes back
  for both coders: see "Outside the test: run B".) The second half's κ
  of 0.71 rests on 8 links from each
  coder, 6 of them shared, and its interval runs from 0.37 to 0.94; the
  three-value code there would read "too few to tell". The verdict is read on
  all 120 rows, and stands.
- The file names that ChatGPT's citations leave in a reply also differ between
  its two chats (the report counts them). They come and go by whole replies,
  which may be how a reply was copied. Nothing is drawn from them.

## How rare evidence links are, and where they fall †

| | coder 1 | coder 2 | both |
|---|---|---|---|
| the 60 linked rows: an author link | 23 | 20 | 15 |
| the 60 linked rows: an evidence link | 7 | 15 | 6 |
| the 60 near rows: an author link | 4 | 3 | 3 |
| the 60 near rows: an evidence link | 6 | 12 | 4 |

- **The author link tells the extractor's links from the near pairs. The
  evidence link hardly does:** each coder finds almost as many among the near
  rows as among the linked ones.
- **Why most of the extractor's links have no evidence link.** Of coder 1's 53
  linked rows without one, 6 are readings, 2 more are restatements, 44 more
  show neither the condition nor the outcome, and 1 shows only a carried-out
  marker. Of coder 2's 45: 6, 2, 35 and 2.
- **`with`.** The extractor coded 23 of the 60 `with`, 14 of them on passages
  it marked as reported. Of those 14, coder 1's derived codes keep 2 as `with`
  and coder 2's keep 4. They share one (R078). Why this matters is in the
  first test's note: the seam detector counts only `with` and `against` links
  from reported passages, and assesses a claim only when it has at least four.
- **C01,** the claim that holds 96 of the linked pool's pairs, reached the cap
  of six rows. Both coders gave all six no link and no author link.

## The hard rows

On each of the five rows not agreed, coder 1 gives no link and coder 2 a link.
Three are in the first half (of its 7 hard rows) and two in the second (of
11). †

| row | pair | coder 2's code | what it turns on † |
|---|---|---|---|
| R063 | F97 > C21 | `illustrates` · outcome other way | the contrary of the outcome's marker; coder 1: "no marker" |
| R002 | F98 > C21 | `illustrates` · outcome other way | the same |
| R130 | F99 > C23 | `illustrates` · outcome other way | coder 1 finds the contrary of one outcome marker and applies the rule that one is not enough; coder 2 finds the contrary of both |
| R077 | F24 > C09 | `illustrates` · condition only | a `none` claim; coder 2 lists c1; coder 1: "no marker" |
| R049 | F83 > C20 | `with` · outcome only | coder 2 lists o1; coder 1: "no marker" |

What the plan chose the hard rows to check: †

- **A restatement is never evidence** (F20 > C08): `restatement` for both.
- **A figure of the author's model is a `reading`** (F88 > C27, F109 > C29):
  `reading` for both.
- **A pattern across cases** (F96 > C28): `pattern` for both, and `with` on the
  outcome only for both. For both it rests on a name alone: with names not
  counted, both give no link.
- **An outcome the other way stays out of `against`** (F93): no `against`.
- **The same kind of case gets the same code.** Coder 1 gives both twins the
  same five-value code in all five pairs, and coder 2 in four. In the fifth
  (F93 and F99 on C23) coder 2 gives no link to one and `illustrates` to the
  other.
- **The passage now prints the numbers** (F24, F25 > C09; F29 > C13): two
  agreed as no link, and one not agreed (R077, above).
- **A name is marked `named`** (F83 > C20): not shown here. Neither coder used
  `named`; coder 2 listed a marker and coder 1 found none.
- **A named failure** (F99 > C20): coder 2 codes the condition `absent, named`,
  and coder 1 codes it `absent` from a contrary. Both give `illustrates`.

Three of the entries logged before the freeze touch a hard row: entry 2 (the
page of C23's outcome marker o1; C23 is the claim of R130 and R133), entry 3
(the last words of F99's passage; R097 and R130) and entry 20 (a correction to
the print of F98's passage; R002). R002 and R130 are among the five rows not
agreed. Those entries were made and confirmed with the hard rows known.

## The sheet

A sense check, not gated. 20 rows: 4 hard, 8 linked, 8 near.

- **What it is.** The plan had the PI code the 20 rows by hand, and called the
  sheet "the only human reading in the test". It was made another way: Fable 5.1
  at max, in an incognito chat, gave the answers, and the PI validated them. So
  it is a third model's reading, validated by the PI, and this test has no
  independent human reading.
- **The model.** Fable 5.1 is a Claude model, as coder 2 is.
- **How it was made,** by the PI's account. The Fable chat was most likely given
  `instructions_pairs.md`, the Excel file and the PDF; the PI does not remember
  exactly. The PI validated by sense-checking every answer, found nothing
  unreasonable and no hallucination, and changed no cell. The notes on eight
  rows are Fable's. The blank sheet holds, for its 20 rows, what a coder's table
  holds, and no stratum or code of the extractor's.
- **The script's label.** The report calls it "the PI's sheet" and speaks of
  "the PI and coder 2", and the results file holds its codes under a key
  named `pi`. Both stand as the script wrote them. Read the label as this
  section describes the sheet.
- **When.** The file was fixed by its hash on 5 Oct, before any coder chat was
  run. Its own stamp says it was last saved at 08:05 that morning, if the stamp
  is in UTC.

| field | the sheet and coder 1 | the sheet and coder 2 |
|---|---|---|
| author link | 18 of 20; κ 0.76 (0.38 to 1.00) | 18 of 20; κ 0.78 (0.43 to 1.00) |
| evidence link | 16 of 20; κ 0.41 (0.00 to 0.83) | 20 of 20 |
| three-value code | 18 of 20; κ 0.44 (−0.11 to 1.00) | 20 of 20 |
| five-value code | 15 of 20; κ 0.31 (0.00 to 0.67) | 20 of 20 |
| kind | 18 of 20; κ 0.82 (0.54 to 1.00) | 19 of 20; κ 0.91 (0.67 to 1.00) |
| use | 17 of 20; κ 0.75 (0.44 to 1.00) | 18 of 20; κ 0.84 (0.59 to 1.00) |
| condition | 15 of 20; κ −0.09 (−0.21 to 0.00) | 18 of 20; κ 0.70 (0.00 to 1.00) |
| outcome | 17 of 20; κ 0.64 (0.18 to 1.00) | 20 of 20 |

**How close the sheet is to coder 2.** †

- Of the 120 code cells (six codes on 20 rows) the sheet differs from coder 2
  on 5, and from coder 1 on 15. Fifteen rows equal coder 2's in every code and
  in the list of markers shown; eight equal coder 1's.
- The sheet's reasons run parallel to coder 2's, often in near the same words
  where the words are not the paper's (R013, R113 and R120 are examples). Some
  of that follows from the rules and the markers, which both follow. The
  sheet's model and coder 2 are both Claude models.
- In the first test the sheet stood nearer ChatGPT: on the evidence link it
  matched ChatGPT on 19 of 20 rows and Opus on 16. By the PI's account that
  sheet was not made in this way.
- **So the table is not an independent human check that sides with coder 2.**
  It shows that a second Claude model, with the PI's validation, gives these
  20 rows the same evidence link, the same two codes and the same outcome as
  coder 2. On kind, use, the condition and the author link it differs from
  coder 2 on one or two rows each. The rules were drafted by a Claude model
  too. Why the two agree, the table cannot say: they may agree because they
  are of one family, or because both read the rows as the rules mean. Nor can
  it say whether an independent human reader would side with coder 2 or with
  coder 1.

**Where the sheet differs from coder 1.** †

- The sheet's five-value code differs from coder 1's on five rows: R057, R069,
  R077, R101 and R140. On the first four the sheet has a link and coder 1 has
  none, with "no marker" as its reason. On R140 they differ on other cause.
- **The notes on eight rows** came with the sheet, before any coder chat. They
  are Fable's. All five rows are among the eight. Cell by cell:

| row, field | the sheet has | the notes name as the alternative | coder 1 | coder 2 |
|---|---|---|---|---|
| R068, use | restatement | none | none | restatement |
| R140, condition | not shown | absent | not shown | absent |
| R140, other cause | yes | — | no | yes |
| R051, kind | report | pattern | report | report |
| R077, kind | report | pattern | pattern | pattern |
| R057, outcome | as asserted | (rests on how two words are read) | not shown | as asserted |
| R069, condition | present, named | (rests on counting the paper's terms as names) | not shown | present, named |
| R093, condition | present, named | (the same) | not shown | not shown |
| R101, outcome | other way | (rests on what counts as the contrary) | not shown | other way |

On eight of these nine cells at least one coder differs from the sheet. Five
of the nine are of the kinds named under "Why": a showing that rests on a
reading (R057), a name (R069, R093) and a contrary (R101, and the condition on
R140). The other four are use, other cause and kind.

R057 is also one of the three rows on which coder 1's link changed in the
rerun of chat C1a: see "Outside the test: the rerun of chat C1a".

## Beside the bar, in short

The report has every figure here, each with its interval, except those marked
†.

- **The 60 linked rows alone.** Author link κ 0.53 (0.29 to 0.73), evidence
  link κ 0.46 (0.17 to 0.71), three-value code κ 0.35 (−0.06 to 0.73).
- **The 60 near rows alone.** Author link κ 0.85 (0.00 to 1.00), evidence link
  κ 0.36 (0.05 to 0.66), three-value code κ −0.03 (−0.06 to 0.00).
- **With carried-out markers counted.** Evidence link κ 0.44 (0.23 to 0.63);
  the three-value code is unchanged; hard rows 12 of 18.
- **Patterns as readings.** Evidence link κ 0.33 (0.00 to 0.605); three-value
  code κ 0.38 (−0.02 to 0.74), which would read "too few to tell"; hard rows
  15 of 18.
- **Names not counted.** Evidence link κ 0.32 (0.06 to 0.55); three-value code
  κ 0.33 (−0.03 to 0.67), "too few to tell".
- **The strict and covariation readings.** Three-value code κ 0.00: coder 1
  then has no `with` at all.
- **The marker-source rows,** 10 extra rows whose passage holds the sentence a
  marker of the claim came from. With them, on 130 rows: author link κ 0.62
  (0.43 to 0.77), evidence link κ 0.46 (0.26 to 0.64), three-value code κ 0.31
  (−0.04 to 0.603). The coders agree on the five-value code on 8 of the 10; on
  both of the others (R022, R109) coder 2 calls the passage a restatement. †
- **Sides no marker can show.** For 17 claims the marker chat found no
  observable sign of the condition or of the outcome; only a name can then
  show that side. 24 of the 120 rows are on such claims. There the coders
  agree on the evidence link on 23 of 24. Without those rows, on 96: evidence
  link κ 0.25 (0.03 to 0.48), three-value code κ 0.23 (−0.06 to 0.55). So rows
  where little can be shown help the pooled figure.
- **The author's-account fragments,** 43 of the 120 rows. Evidence link κ 0.44
  (0.08 to 0.74) on them and 0.39 (0.11 to 0.65) without them.
- **Figures and table cells,** 7 rows: agreed on the evidence link on all 7.
- **Claims with tagged markers,** 28 rows. The coders list the same condition
  markers on 25; the other three are R084, R104 and R142. A `present` that
  rests on carried-out markers alone: four rows for coder 1 and three for
  coder 2. On 22 of the 25, both coders list none; on the six rows where
  either lists one, they list the same on three. †
- **Named absences,** where a condition is coded `absent` by a name alone: one
  (coder 2, R097).
- **Claims with no marker at all.** Six rows (three on C52, two on C40, one on
  C50): no link for both coders on all six. †
- **The cap.** C01 has six linked rows where a draw with no cap would give
  about 16. C07 reached the cap among the near rows, where about 5 were to be
  expected in any case.

## The second marker set

Compared with the first, and never coded with
(`LINK_TEST2_MARKERS_COMPARED.md`).

- In the matching, form is the same in 52 of 52 claims, and the condition is the
  same state in 52 of 52.
- Where no marker is printed: the two sets agree on 88 of 100 sides. The first
  set alone has none on 9, and the second alone on 3.
- Tags: the same six claims are tagged in both, and the 8 matched condition
  markers in them carry the same tag.
- 109 of the first set's 130 markers (84%) have a counterpart in the second.
  114 of the second's 259 (44%) have one in the first, and 145 have none: the
  second chat wrote about twice as many signs.
- **In 47 of the 52 claims the two sets would count different things.** In 37
  of them the second set only adds signs (the log has this count).
- **C07 and C11.** The second chat wrote `no mapping given` for every category
  of both claims, and so no outcome marker. With its set, the outcome on these
  two claims could never be shown. The sample holds 11 rows on them. With the
  first set, coder 1 coded an outcome as shown on 4 of the 11 and coder 2 on
  3. †
- The markers were matched in one pass, with no second matching. Nobody read the
  second set for breaches of the rules.

## The rules' wording: what it leaves open

- **Four points in Part B,** found when the derivation was written a second
  time. Both versions chose alike, and the rules were frozen, so nothing was
  changed. For the two coders, none of them decided a code in this sample. †
  1. A report on a `none` claim is coded like any other report, though Part B
     also says such a claim needs evidence across cases. One of the coders'
     rows is of this kind (R051), and it is no link for both. On the sheet
     the point arises twice (R051, R077), and on R077 it decides the sheet's
     code.
  2. The table for `describes` claims has no line for an outcome not shown.
     That arises on no row: on the 12 such rows of each coder the condition is
     not shown either, and the first step gives no link before the table is
     reached.
  3. On a claim with tagged markers, a `present` with no marker listed and no
     name counts as changed by the treatment. It occurs on no row; the nearest
     is coder 1's R054, where a name stands in for the marker. And it matters
     only for a `bounded` pair, of which there is none.
  4. A `none` claim's `with` stays `with` under the strict and covariation
     readings. Neither coder gave `with` on a `none` claim.
- **Claims whose statement and printed direction word the condition
  differently.** Found by reading all 52 claims. †
  - In the sense of Part S, a practice carried out in the one and the practice
    working in the other: **C13.** The statement has dream building doing the
    work as a practice; the printed direction has it *successfully* linking
    aspirations to the self. The marker session went by the direction, tagged
    the markers, and said so. Four rows, all no link for both coders. **C20,
    in part:** the first half of the statement speaks of the practice itself,
    and the second half, like the direction, of it working. Eleven rows, seven
    of them hard.
  - In another way, where the statement starts from something done and the
    direction from the state it produces: **C15** (comparing the two selves,
    against the size of the discrepancy; two rows, one of them R078, where
    both coders give `with`), **C22** (revaluing relationships, against the
    barriers this creates) and **C50** (creating seekership, against more
    seekership). **C14** is arguable in the same way (seven rows).
- **Coder 2's notes on claims,** which the instructions allow and the scoring
  does not read. The report prints them.
  - C08, in both chats: marker c1 is a member sponsoring others, while the
    paper's reason is that every member had already been recruited.
  - C42: the paper ties most of the outcome's markers to strong identification
    and not to the practices, and c1 comes from an example outside Amway.
  - C25: the condition as printed covers both answers a prospect can give, so
    it cannot fail once a prospect is approached.

## Before the freeze: the seven notes, and the materials

The report prints seven notes from the frozen file. In short:

1. Chats M1 (markers) and P (passages) each ran once, on 4 Oct, in ChatGPT.
   Neither return was set aside, and no second run was made.
2. Both returns were read before the freeze, independently and by the PI. Three
   markers' opening words were corrected, and the print of one passage. The
   independent reading's doubtful points stayed as written, apart from the two
   markers the PI flagged.
3. Removed under fix 1: C40 c1 and C50 c1, each a sign of one part of a joint
   condition. Both claims are left with no marker.
4. Stays as written: C28 and C29 each have one `working` marker and no
   `carried out` marker, where the rules ask for both kinds.
5. Stays as written: C29 c1 gives half of its joint condition by the paper's
   abstract term.
6. Stays as written: C24 o1 carries the condition inside the outcome's sign.
7. The print: the five cells of Table 1 were read off the page image by
   machine; twelve other passages' print was corrected; a dash is printed as a
   hyphen.

What became of notes 4 to 6 in the result: †

- **C29** has six rows in the sample, and the coders' five-value codes differ
  on four (R016, R044, R109, R140). On two of them a coder reads the joint
  condition as ruled out: coder 1 on R016, coder 2 on R140.
- **C24** has two rows, both no link for both coders. **C28** has one, the hard
  row R080, where both give `with` by a name alone.

Also for the record:

- 7 of the 132 markers and 2 of the 121 passages were touched by a fix or a
  listed finding.
- **The print check** set the text layer beside a second machine reading of
  each page. It cannot show a place where both are wrong in the same way.
- **What holds the frozen files.** At every run the scoring refuses to go on if
  the rules, the plan, the send sheet, the briefs, the lists of claims and
  fragments, the corpus, the fixed messages or the fixed code differ from the
  freeze of step 1; if the frozen markers and passages are not the file the
  sample was drawn from; if the sample, the chance figure or a table is not what
  the recorded seed gives; if a reply file is not the one that was read in; or
  if the second derivation is not the sealed file, or gives a different code on
  any row. Three files are held by no script: the file of logged entries, whose
  28 entries and seven notes are all copied into the frozen markers and
  passages; the blank sheet; and the filled sheet, whose hash is recorded in the
  results file. All three hashes were checked by hand on 5 Oct, and again
  independently: unchanged.

## The tables, as the coders got them

- **A straight apostrophe.** Six of the 83 stubs carry a straight apostrophe
  where 15 others carry a curly one. The mark comes from how a stub is printed
  once the extractor's opening words are taken out, so it falls on stubs that
  had the extractor's voice cue: all six are author's-account fragments, whose
  rows are reported apart in any case. Its 17 rows are 9 linked, 5 near, one
  marker-source row and 2 hard rows, so it does not tell the groups apart. On 5
  Oct it was decided to leave the tables as drawn.
- **From the independent check of the tables for leaks,** three more points
  stand:
  - a fragment that recurs is more often in a near pair, which follows from
    the frozen draw rule;
  - the stubs are worded like the claims, as in the first test: the same
    writer wrote both;
  - the instructions and the tables differ on small points of form, such as
    the shape of a fragment's label and where a note on a claim goes.

## How the chats ran

- **The models.** Coder 2: "Opus 5.5" at "Extra", in incognito Claude chats.
  Coder 1: ChatGPT, in Temporary Chats. Its window shows no model's name. A
  picture of it (`chatgpt_interface_5oct.png`) shows the window before a chat is
  begun, perhaps only part of it, with a control named "Thinking effort" set to
  "High". It is not a picture of a chat of the test, and it shows no sign of a
  Temporary Chat. "GPT 5.6 Sol", the name on the first line of coder 1's files,
  is what the model answers when asked in a separate Temporary Chat; the frozen
  plan and send sheet say "ChatGPT 5.6". A model's own account of its name is
  weak evidence. So the record reads: ChatGPT as served on 4 and 5 Oct 2026,
  calling itself "5.6 Sol", with thinking effort at High in every chat, by the
  PI's account.
- **All four coder chats ran on 5 Oct,** in the 47 minutes between the sending
  of the steps and the return of the four files. The plan had put about 45
  minutes on each ChatGPT chat and an hour or more on each Claude chat, and had
  advised different days for the two Claude chats, for the allowance. By the
  PI's account Claude was the faster and took little allowance.
- **Before the scoring, the PI confirmed** that each chat ran as the protocol
  says: the settings, only the folder's five files and the PDF attached, the
  first message and then only `continue`, nothing regenerated and nothing
  edited. All of this rests on the PI's account; only the files' hashes stand
  apart from it. The settings confirmed then named coder 1's model as GPT 5.6
  Sol; that name is the model's own account, and the window does not show it.
- **No restart and no format request.** The files show none, and the PI
  confirmed that no coder chat was stopped.
- **Chat M1's file** opened with "Reply 1" and no model's name; the PI confirmed
  GPT 5.6 Sol. **Chat M2's first line** said "max"; the PI confirmed that it ran
  at Extra.
- **`unclear`.** Coder 2 marked 58 of its 148 rows unclear in one judgment or
  the other. Coder 1 marked none.

**How run A's chats ran beside one another,** by the PI's account: side by side,
all four open at once, as in run B; and the rerun of chat C1a began after chat
C1a had ended.

## Confounds

- **Who wrote what.** ChatGPT wrote the claims, the markers and the passages,
  and is coder 1. Opus wrote the second marker set, and is coder 2. Every chat
  is separate and keeps no memory.
- **Who wrote the rules.** A Claude model drafted them, and coder 2 and the
  sheet's model are Claude models too.
- **Within the test, each model coded each row once.** The two halves differ.
  Apart from kind, nothing in the test says whether a coder's second run on the
  same rows would agree with its first. Outside the test, all four chats have
  now been run a second time (run B). With the test's ChatGPT, chat C1a has
  three runs in all, counting the PI's rerun, which was the second of them in
  time. Run C adds one more run of chat C1a and of chat C1b, with another model
  setting.
- **ChatGPT's model** is on record only as the name it gives itself, and its
  thinking effort only by the PI's account.
- **The test is of two model settings.** They are ChatGPT as served on 5 Oct
  with thinking effort at High, and Opus 5.5 at Extra. Outside the test, run
  C set another ChatGPT setting in coder 1's place, with another model and
  another effort by the names on record, and the figures differ: see "Outside
  the test: run C".
- **The sheet** is a Claude model's reading, validated by the PI. It is not
  independent of coder 2 as a human reading would be, and the test has no
  independent human reading.
- **Reply files outside the folder.** On 5 Oct both of coder 1's reply files for
  table 1 went to a Fable chat, with the files that chat C1a had received, to be
  compared. When exactly is not on record. That chat is no part of the test and
  coded no row for it.
- **A fifth chat.** By the PI's account, the rerun of chat C1a was made before
  the four files were sent. So the test's chat C1a is the first of two runs that
  existed then. That the file sent as the test's is the first run's is not
  stated in so many words: it rests on the first lines typed ("Reply 1 GPT 5.6
  Sol", and "Reply 1 Rerun ChatGPT 5.6 sol") and on the PI's account that the
  rerun began after chat C1a had ended. A Temporary Chat keeps no memory, so the
  four chats stand as confirmed before the scoring; the fifth was not mentioned
  then.
  - *Two loose ends.* The times leave little room: the four files came 47
    minutes after the steps were sent, and in run B chat C1a alone took 31
    minutes. And one file in chat C1a's folder carries a time 46 minutes after
    the four files came, which is not explained. Neither contradicts the PI's
    account, and neither can be checked.
- **The examples in Part A** echo the cases on which the coders differed in
  the first test.
- **The colleague** who reviewed version 2 had the paper and the whole rules
  file.
- **The cap.** The sample holds fewer rows on C01 than a simple draw would.
- **The scan.** The PDF is a scan with a text layer. The coders were told that
  the paper governs where the print and the paper differ.
- **Who checked the markers and passages** knows the hard rows, and three
  logged entries touch one.
- **The passage chat saw each stub as the extractor wrote it.** On 29
  fragments the stub opens with the extractor's voice cue, so there the
  passage, and with it the kind, partly follows the extractor's voice code. 43
  of the 120 rows are on those fragments.
- **Sample size.** Every κ here moves by chance: by about ±0.2 on 120 rows for
  a link, and by more for the three-value code, on 60 rows, and on a half.

## What the test cannot show

From the plan:

- anything about a paper other than Pratt;
- a cold result: the rules were written after the reviews of Pratt's run and
  after the first test, and the hard rows return;
- how the rules do on claims not seen before: 89% of the linked pool's pairs
  and 78% of the near pool's sit on a claim that had a row in the first test,
  and 30% and 40% on a fragment that had one;
- much about `against`: the extractor's three `against` links are all hard
  rows, and on these 148 rows neither coder gave `against` at all;
- which link, the author's or the evidence link, should feed the scored
  measure;
- how far a second set of markers, or a second passage session, would change
  the links;
- how stable each coder is: each model codes once.

Beyond the plan, one more:

- how the coders compare with an independent human reader: the sheet was a
  model's reading, validated by the PI.

On the plan's last point, how stable each coder is, the test itself still
shows nothing. Run B, outside the test, gives a first measure from two runs of
each chat: see "Outside the test: run B".

Since run C, one more:

- how far the result holds for other models or settings than the two that
  were tested. Run C, outside the test, gives one other ChatGPT setting, run
  once: see "Outside the test: run C".

## What the plan says next

"If it fails, the report shows which judgment failed. That judgment is revised
and tested on a fresh draw, never scored again on these rows." The pools still
hold about 320 linked and 415 near pairs. "Either way, the result goes into the
proposal as a finding about the instrument."

The plan and the frozen protocol provide for no second run of a coder chat,
except for a chat that stops.

## Outside the test: the rerun of chat C1a †

*Not part of the test. Every figure here was worked out on copies of the
folder's files, after the result, and none was fixed in advance. Nothing was
read into the test's answers, and the verdict stands.*

- **What it is.** The PI ran chat C1a a second time. Its first line calls it a
  rerun. By the PI's account it had the same setting, ChatGPT in a Temporary
  Chat calling itself 5.6 Sol, and the same set-up in every point asked: the
  same six attachments, the frozen first message, only `continue`, nothing
  regenerated, and memory, custom instructions and web search off. By the same
  account it was the only second run of any chat of the test. The reply is filed
  as it came (`reply_C1a_rerun.rtf`).
- **When, and why this chat.** By the PI's account it was made after the first
  chat was complete and before the four files were sent, so before the scoring
  and the verdict; out of curiosity, with a coder's agreement with itself in
  mind. So it was not picked because its half agreed worst: nobody knew then
  which half that was. No second run had been declared.
- **What was done with it.** A script turned the file into plain text, and the
  folder's own reader read that on a copy: 74 lines for judgment 1 and 74 for
  judgments 2 and 3, nothing to ask for again, and no `unclear` mark. The
  results are kept apart from the test's, in `link_test2_answers_rerun`.
- **Nothing here was fixed in advance.** Much of it was found by looking, after
  the first comparison or after the independent check: what the 13 rows are,
  coder 2's `unclear` marks, coder 1's first-half pattern, the reply's form,
  which run is nearer coder 2, kind on R041 and R051, R012, the hard rows, and
  the 32 ways of counting.
- **The rerun's reply differs from the first in form.** In 54 of its 74 lines
  for judgments 2 and 3 the reason names the claim by its number. No such line
  of the first run, or of chat C1b, does. It also carries 151 file names left by
  citations, where the first run has 49 and chat C1b 123. That may be chance, or
  the copying. By the PI's account the set-up was the same, so the difference is
  the chat's own.

**Coder 1's two runs of table 1, set side by side.**

| on the 63 bar rows of table 1 | the two runs agree on | κ, with its 95% interval |
|---|---|---|
| author link | 57 rows | 0.76 (0.55 to 0.93) |
| evidence link | 60 | 0.70 (0.25 to 1.00) |
| condition | 60 | 0.64 (−0.01 to 1.00) |
| outcome | 58 | 0.41 (−0.04 to 0.79) |
| kind | 59 | 0.90 (0.78 to 0.97) |
| use | 57 | 0.80 (0.63 to 0.94) |
| every code the coder writes for a row | 47 | — |

The condition and the outcome are counted here without `named`. The last row
counts the six codes a coder writes for a row: the condition and the outcome
with `named`, other cause, `bounded`, kind and use. For the three-value code
the two runs give κ 0.00, with 62 of the 63 rows the same. That figure tells
nothing: the first run has no `with` on these rows, and the rerun has one
(R057).

- **The second run is as sparing as the first.** Each codes a condition or an
  outcome as shown on 8 of the 63 rows, and each gives "no marker" as its
  whole reason for judgment 1 on 55 of them. The first gives 5 evidence links
  and the second 6.
- **Where coder 1 does find something, its two runs agree only in part.**
  Both runs code a side as shown on 5 rows. On 6 more, only one of them does;
  on three of those six both runs call the passage a reading, so the
  difference cannot change the link there. Of the 7 rows with an evidence
  link in either run, 4 have it in both. So the agreement in the table rests
  mostly on rows where both runs find nothing, which is why the intervals are
  so wide.
- **Coder 1's first-half pattern came back.** On the bar's rows, in the first
  run of table 1, in the rerun, and in chat C1b on table 2: evidence links 5,
  6 and 8; rows with a marker listed 1, 3 and 8; `with` 0, 1 and 5; links
  that rest on a name alone 4 of 5, 4 of 6 and 1 of 8. That is a first hint
  that, for coder 1, the two halves differ because of their rows and not
  because of chat C1a. When this was written chat C1b had been run once; it
  has since been run again, in run B.
- **Kind.** The two runs differ on kind on five of the 74 rows, four of them
  among the 63. The rerun gives F51 and
  F86 the kind that chat C1b and coder 2 give. F27 it again calls a `reading`,
  where chat C1b has `pattern`. On two rows it newly has `pattern` where the
  first run and coder 2 have `report` (R041, and the hard row R051). On the
  63 rows, kind differs from coder 2's on five in the first run and on three
  in the rerun (R004, R010 and R041).
- **The seven hard rows of table 1** have the same five-value code in both
  runs.

**Each run beside coder 2, on the same 63 rows.**

| | the first run and coder 2 | the rerun and coder 2 |
|---|---|---|
| author link | κ 0.58 (0.32 to 0.80); 53 of 63 | κ 0.58 (0.32 to 0.79); 53 of 63 |
| evidence link | κ 0.24 (0.01 to 0.47); 47 | κ 0.39 (0.14 to 0.62); 50 |
| condition | κ 0.28 (−0.04 to 0.58); 52 | κ 0.45 (0.12 to 0.74); 55 |
| outcome | κ 0.20 (−0.08 to 0.51); 52 | κ 0.45 (0.10 to 0.73); 55 |

- **13 of the 16 disagreements on the evidence link are still there,** and on
  all 13 coder 2 has the link and coder 1 has none. Three are gone. On R015
  and R057 the rerun now has a link, as coder 2 has. On R016 the first run
  had a link that coder 2 has not, and the rerun has none. No new
  disagreement comes on the 63 rows. One comes outside the bar: on R012, a
  marker-source row, the rerun gives `with` where the first run and coder 2
  give no link. Each of the 6 links the rerun gives on the 63 rows is a link
  coder 2 gives too; coder 2 gives 19.
- **Where the two runs differ, the rerun is mostly the one nearer coder 2:**
  on the condition on 3 rows of 3, and on the outcome on 4 of 5. Every figure
  in the table but the author link rose.
- **Some of that gain may be chance,** as with any one second run. It is not the
  gain to be expected of a half picked for agreeing worst: by the PI's account
  the rerun was made before any result. How much of the gain is chance, one
  rerun cannot say.
- **What the 13 are** (found by looking, after the first comparison). On 12
  of them, all but R074, coder 1 finds neither side shown in both runs, with
  "no marker" as its whole reason both times. On R074 it codes a side as
  shown and calls the passage a restatement, in both runs. Coder 2's link
  rests on a marker it lists in 8 of the 13 and on a name alone in 5.
- **Coder 2 marked 12 of the 13 unclear** in judgment 1, all but R010 (found
  by looking, as above). That is not new with the rerun. Coder 2 marked 20 of
  the 63 rows unclear. Beside the first run the coders disagree on 13 of
  those 20 and on 3 of the other 43; beside the rerun, on 12 and on 1.

**The bar with the rerun in the place of the first run.** Read by the
scoring's own code on a scratch copy, as a diagnostic. It is not a second
scoring of the test.

| condition | with the rerun in place | as scored |
|---|---|---|
| 1. author link | κ 0.65 (0.45 to 0.80); 106 of 120: holds | the same |
| 2. evidence link | κ 0.51 (0.29 to 0.69); 103 of 120: does not hold | κ 0.41 (0.19 to 0.61); 100 of 120 |
| 3. three-value code | κ 0.36 (−0.03 to 0.66); 111 of 120: "too few to tell" | κ 0.25 (−0.05 to 0.56); 110 of 120: not passed |
| 4. hard rows | 13 of 18: holds | the same |
| 5. `not found` | 0 and 0: holds | the same |

The bar does not hold in this reading either. Condition 2 fails, so no top-up
would follow from condition 3. No way of counting passes with the rerun in
place: over all 32, the evidence link's κ runs from 0.47 to 0.53 and the
three-value code's from 0.00 to 0.54.

**The Fable chat about the two runs.** A Fable 5.1 chat was given the six files
that chat C1a had received and coder 1's two replies for table 1, and asked how
the replies differ. That chat did not have coder 2's answers. Its transcript is
filed (`fable_C1a_rerun_transcript.docx`).

- **Its figures were worked out again from the two files, and all match.**
  Among them: 55 of the 74 rows are the same in every code and 19 are not; and
  of the 16 rows where either run finds anything in judgment 1, the whole
  line is the same on 6.
- **Its other two replies are judgments, and were not checked.** Asked which
  code the instructions support on each disputed row, it sides with the rerun
  on 13 of 21 codes and with the first run on 8, and calls that "one more
  reader's judgment, not a gold standard". Asked how to improve the
  instructions, it makes ten suggestions and proposes keeping the 19 rows as
  a test set.
- **What its suggestions bear on.** They rest on the 19 rows where coder 1
  differs from itself. Only two of those, R019 and R074, are among the 13
  rows where the two coders still differ. So they bear on how steady coder 1
  is more than on the disagreement that failed the bar. Five of the ten are
  on judgment 1, and five on kind, use and the `unclear` mark.
- **On R057 the sheet and this Fable chat disagree.** This chat finds `not
  shown` supported for the outcome. The sheet, made with another Fable chat, has
  `as asserted`; the PI changed no cell, so that is the model's own answer.
  Coder 1 gave R057 no link in its first run and `with` in its second; coder 2
  gives `with`.

**What the rerun shows, and what it cannot.**

- **It was set up as the first run was, by the PI's account. It shows** that
  coder 1's sparing reading of table 1 came back in a second chat. Most of the
  first half's disagreement, 13 of the 16 rows, is then not chat C1a's chance.
- **It also shows** that coder 1's two runs part where either finds
  something: both find a side shown on 5 rows, and one alone on 6 more.
- **It cannot show** whether coder 2's links would come back. They come from
  one chat, C2a, which stood unchanged in every comparison here. When this
  section was written, no chat of coder 2 had been run twice under these
  rules. (Run B has since done that: see the next section.)
- **It is one chat, of one half, not declared before it ran,** and its set-up
  rests on the PI's account. Its figures are a first look, and every interval is
  wide.

## Outside the test: run B, the declared second run

*Not part of the test. Run B is the declared second run of all four coder chats.
It has no bar and reads no verdict: the test's verdict is the one read on its
own run, run A. Every figure here comes from the comparison declared before any
chat of run B was opened, unless it is marked "found by looking". Every figure
of this section was worked out again independently, with separate code, and none
differed.*

**Words used in this section.** A *pairing* sets one run of coder 1 beside one
run of coder 2. There are four: 1A with 2A, which is the test; 1A with 2B; 1B
with 2A; and 1B with 2B. "1B" is coder 1's run B. A link *rests on a marker*
when the coder lists a marker of the claim as shown; it *rests on a name
alone* when the coder lists no marker and marks a side `named`; the few that
are left rest on a contrary alone.

**In short.**

- **Each coder mostly repeats itself, and not on every link.** On the evidence
  link, between its two runs: coder 1 κ 0.73, coder 2 κ 0.83. Of the rows
  with a link in either run, coder 1 has the link in both on 11 of 18, and
  coder 2 on 22 of 29.
- **On the three codes of the bar, the two coders agree with each other less
  than each agrees with itself,** under all four pairings: on the evidence
  link κ runs from 0.41 to 0.64. It is not so for every code: under two
  pairings the coders agree on kind and on the outcome better than coder 1
  agrees with itself.
- **The bar holds under none of the four pairings.** Which condition fails
  depends on the runs. The test's own pairing gave the author link its
  highest figure of the four and the evidence link its lowest.
- **Most of coder 2's first-half links came back:** 14 of 19. Of the 13 rows on
  which coder 2 alone had a link beside both coder 1's run A and the PI's rerun
  of chat C1a, its run B has the link again on 8.
- **The gap between the two halves came back,** for both coders. So it goes
  with table 1's rows, and not with how one chat happened to run. What in
  those rows does it, run B does not show.

**How it ran.**

- What run B is, and the ten things that are compared, were fixed before any
  chat was opened. One addition was made later, also before any chat: the chats
  run in the manner of run A's.
- The script that makes the comparison was fixed by its hash before any chat was
  opened, after two rehearsals on made-up runs, and was not changed afterwards.
- The four chats ran side by side, in 39 minutes, as run A's had. Each read
  whole, with no format request. The first lines do not carry the words "run B"
  that the steps asked for; the file names do.
- The PI confirmed how the chats ran: the same settings, files and messages as
  in run A. Only then was anything compared, on copies. Nothing was read into
  the test's answers.
- The results are kept apart from the test's, in `link_test2_answers_B`.

**The six main figures: each coder with itself, run A against run B, on the
120 rows of the bar.**

| | coder 1 (ChatGPT) | coder 2 (Opus) |
|---|---|---|
| author link | κ 0.72 (0.54 to 0.86); the same on 109 of 120 | κ 0.82 (0.67 to 0.95); 114 |
| evidence link | κ 0.73 (0.49 to 0.90); 113 | κ 0.83 (0.68 to 0.94); 113 |
| three-value code | κ 0.90 (0.66 to 1.00); 119 | κ 0.65 (0.27 to 0.90); 115 |

- **Evidence links,** in run A, in run B and in both: coder 1 gives 13, 16 and
  11; coder 2 gives 27, 24 and 22.
- **`with`,** the same way: coder 1 gives 5, 6 and 5; coder 2 gives 9, 6 and 5.
  The three-value code rests on these few rows, which is why its intervals
  are so wide.
- **On all 148 rows,** which the declaration also names: the author link, κ
  0.71 (0.57 to 0.83; 133 of 148) for coder 1 and 0.79 (0.65 to 0.90; 139)
  for coder 2; the evidence link, κ 0.80 (0.65 to 0.92; 140) and 0.80 (0.67
  to 0.91; 137); the three-value code, κ 0.88 (0.66 to 1.00; 146) and 0.68
  (0.38 to 0.89; 142). So on the evidence link the two coders are about
  equally steady: each changed 7 of the 120 rows, and coder 1 changed 8 of
  the 148 and coder 2 11.

**The other codes, each coder with itself, on the 120 rows.**

| | coder 1 | coder 2 |
|---|---|---|
| condition | κ 0.69 (0.37 to 0.92); 115 | κ 0.76 (0.55 to 0.91); 113 |
| outcome | κ 0.63 (0.34 to 0.84); 112 | κ 0.87 (0.70 to 0.97); 116 |
| kind | κ 0.93 (0.86 to 0.99); 115 | κ 1.00; 120 |
| use | κ 0.77 (0.63 to 0.88); 109 | κ 0.87 (0.76 to 0.96); 114 |
| five-value code | κ 0.73 (0.50 to 0.90); 113 | κ 0.81 (0.68 to 0.92); 112 |
| every code the coder writes for a row | the same on 94 | the same on 106 |

The condition and the outcome are counted without `named`. The last row counts
the six codes a coder writes: the condition and the outcome with `named`, other
cause, `bounded`, kind and use.

**Each half apart.** Both coders are steadier on the second half.

| each coder with itself | coder 1 | coder 2 |
|---|---|---|
| evidence link, first half (63 rows) | κ 0.50 (−0.03 to 0.84); 58 | κ 0.76 (0.56 to 0.92); 57 |
| evidence link, second half (57 rows) | κ 0.87 (0.64 to 1.00); 55 | κ 0.93 (0.74 to 1.00); 56 |
| author link, first half | κ 0.65 (0.42 to 0.85); 55 | κ 0.75 (0.53 to 0.94); 58 |
| author link, second half | κ 0.81 (0.56 to 1.00); 54 | κ 0.92 (0.71 to 1.00); 56 |

**The two coders with each other, under each pairing of runs, on the 120
rows.** "1B with 2A" is coder 1's run B beside coder 2's run A.

| pairing | author link | evidence link | three-value code |
|---|---|---|---|
| 1A with 2A, the test | κ 0.65 (0.45 to 0.80); 106 | κ 0.41 (0.19 to 0.61); 100 | κ 0.25 (−0.05 to 0.56); 110 |
| 1A with 2B | κ 0.61 (0.42 to 0.79); 106 | κ 0.47 (0.23 to 0.67); 103 | κ 0.33 (−0.04 to 0.68); 113 |
| 1B with 2A | κ 0.59 (0.38 to 0.76); 105 | κ 0.58 (0.38 to 0.75); 105 | κ 0.36 (−0.03 to 0.65); 111 |
| 1B with 2B | κ 0.48 (0.25 to 0.68); 103 | κ 0.64 (0.44 to 0.81); 108 | κ 0.47 (−0.02 to 0.80); 114 |

- **Over all 16 ways** of taking run A or run B for each of the four chats, κ
  runs from 0.48 to 0.65 for the author link, from 0.40 to 0.67 for the
  evidence link, and from 0.22 to 0.52 for the three-value code.
- **The other codes,** over the four pairings: the condition κ 0.43 to 0.64,
  the outcome 0.44 to 0.76, kind 0.93 to 1.00, use 0.59 to 0.70.
- **By half,** the evidence link over the four pairings: 0.24, 0.32, 0.39 and
  0.50 in the first half; 0.71, 0.65, 0.87 and 0.81 in the second.
- **The evidence link differs under all four pairings on 9 rows,** and under at
  least one on 23.

**The bar's five conditions under each pairing.** Read by the scoring's own
code on scratch copies, as a diagnostic. None is a second scoring of the test.

| condition | 1A with 2A, the test | 1A with 2B | 1B with 2A | 1B with 2B |
|---|---|---|---|---|
| 1. author link | 0.65: holds | 0.61: holds | 0.59: does not hold | 0.48: does not hold |
| 2. evidence link | 0.41: does not hold | 0.47: does not hold | 0.58: does not hold | 0.64: holds |
| 3. three-value code | 0.25: not passed | 0.33: too few to tell | 0.36: too few to tell | 0.47: too few to tell |
| 4. hard rows agreed | 13 of 18: holds | 16: holds | 13: holds | 16: holds |
| 5. `not found` | 0 and 0: holds | holds | holds | holds |
| the bar | does not hold | does not hold | does not hold | does not hold |

- **In none of the four pairings do conditions 1 and 2 hold together.** Where
  the evidence link holds, the author link does not.
- **Found by looking:** the same is so under all 16 ways. The author link is
  at 0.60 or more in 7 of the 16, the evidence link in 2, and the three-value
  code in none.
- **Found by looking, the other ways of counting.** The scoring gives each
  pairing under 32 ways of counting, of which the bar's is one. Over the 32,
  the evidence link's κ runs from 0.32 to 0.44 under the test's pairing, from
  0.41 to 0.53 under 1A with 2B, from 0.57 to 0.60 under 1B with 2A, and from
  0.64 to 0.76 under 1B with 2B. Leaving names out makes no steady
  difference. Set way for way against the same counting with names, it gives
  the higher κ in all 16 ways under 1B with 2B (0.72 to 0.76, against 0.64 to
  0.69), in 12 of 16 under 1B with 2A, and in 8 of 16 under each of the other
  two. The author link does not depend on the way of counting. So under none
  of these four pairings does any way of counting bring both links to 0.60.

**Whether links come back.**

| evidence links on the bar's rows | in run A | in run B | in both |
|---|---|---|---|
| coder 1, first half | 5 | 6 | 3 |
| coder 1, second half | 8 | 10 | 8 |
| coder 2, first half | 19 | 15 | 14 |
| coder 2, second half | 8 | 9 | 8 |

- **The 13 rows.** These are the first-half rows on which coder 2's run A has a
  link and coder 1 has none, in its run A and in the PI's rerun alike. The
  declaration named them, to see whether chat C2a's links come back. Coder 2's
  run B has the link again on 8 of them (R008, R009, R010, R011, R028, R034,
  R053 and R069), and not on 5 (R019, R033, R044, R070 and R074). Of the 8, 5
  rest on a name alone and 3 on a marker it lists. Run B marks judgment 1
  unclear on 11 of the 13.
- **Coder 1's run B** has a link on 2 of the 13 (R008 and R011). This count is
  not in the declaration's list; the script, fixed beforehand, prints it.

**The 120 rows, sorted by what the four pairings give** (found by looking).

- **On 97 rows the coders agree under every pairing:** on 88 neither has a
  link in either of its two declared runs, and on 9 both have one in both.
- **On 9 rows they differ under every pairing** of the two declared runs. On 7
  of them coder 2 has the link in both runs and coder 1 in neither; coder 2's
  link rests on a name alone in 4 and on a marker it lists in 3. On the other 2
  (R086 and R134) coder 1 has the link in both runs and coder 2 in neither. Two
  runs of each coder cannot show that these rows would separate the coders in
  every run: on one of the 7, R057, coder 1 did give a link in the PI's rerun.
- **On 14 rows it depends on the run:** on 7 of them coder 1's two runs
  differ, and on the other 7 coder 2's.
- **Coder 2's changes sit on rows it marked unclear.** Its two runs differ on
  the evidence link on 7 of the 120 rows. Six of the 7 are among the 30 rows
  it marked unclear in judgment 1 in run A; one is among the other 90.

**The two halves.** On the bar's rows of each half:

| | coder 1, run A | coder 1, run B | coder 2, run A | coder 2, run B |
|---|---|---|---|---|
| evidence links, first and second half | 5 and 8 | 6 and 10 | 19 and 8 | 15 and 9 |
| links that rest on a name alone | 4 and 1 | 3 and 2 | 8 and 1 | 9 and 2 |
| links that rest on a marker listed | 0 and 6 | 2 and 6 | 10 and 5 | 5 and 5 |
| rows with a marker listed | 1 and 8 | 2 and 8 | 10 and 10 | 6 and 10 |
| `with` | 0 and 5 | 1 and 5 | 7 and 2 | 3 and 3 |
| judgment 1 marked unclear | 0 and 0 | 0 and 0 | 20 and 10 | 17 and 9 |

The row "links that rest on a marker listed" is not in the declaration's list;
the script, fixed beforehand, prints it.

**The first half's pattern comes back in part.**

- *Came back:* coder 2 gives more links in the first half (19 and 8, then 15
  and 9) and marks more rows unclear there; coder 1 lists a marker on far
  fewer rows there (1 and 8, then 2 and 8).
- *Did not come back:* coder 2's `with` (7 and 2, then 3 and 3). Coder 1's
  links by a name alone are 3 against 2 in run B, which is no difference.
- *New in run B:* coder 2 lists a marker on fewer rows of the first half than
  of the second (6 and 10). In run A the two halves were equal (10 and 10).
- *Agreement.* Between the coders it is lower in the first half under every
  pairing: 0.24 to 0.50 there, against 0.65 to 0.87 in the second. Each coder
  also agrees less with itself there.

So the gap between the halves goes with table 1 in both runs, and not with how
one chat happened to run. That is reached by ruling the chat out, from two
runs. What in table 1's rows makes them harder, run B does not show.

**Kind.** In run B coder 1 gives no fragment two kinds, within a chat or
across its two chats; in run A it did so for F27, F51 and F86. Coder 2 gives
none in either run. In run B coder 1's kind is coder 2's on all 120 rows.

**Use and the author link.** The author link is read from use alone: a pair
has it when the use is `evidence` or `qualification`. So a coder's steadiness
on the author link is its steadiness on use. Coder 1's two runs differ on the
author link on 11 rows, and coder 2's on 6. Both coders gave `evidence` as the
use less often in run B: coder 1 has 27 author links in run A and 22 in run B,
and coder 2 has 23 and 17.

**The hard rows.** Coder 1 gives all 18 the same five-value code in both runs.
Coder 2 does on 15: in run B it gives no link to R063, R002 and R049, where
run A had `illustrates` twice and `with`. The coders agree on 13 of the 18
under the test's pairing and under 1B with 2A, and on 16 under the two
pairings with coder 2's run B. No twin pair is split in any run.

**The three runs of chat C1a that there were after run B,** on the 63 rows. The
PI's rerun is given beside the two declared runs and is never pooled with them.
Run C's run of this chat, with another model setting, is in the next section.

| | run A and the rerun | run A and run B | the rerun and run B |
|---|---|---|---|
| author link | κ 0.76 (0.55 to 0.93); 57 | κ 0.65 (0.42 to 0.85); 55 | κ 0.74 (0.51 to 0.92); 57 |
| evidence link | κ 0.70 (0.25 to 1.00); 60 | κ 0.50 (−0.03 to 0.84); 58 | κ 0.63 (0.14 to 0.91); 59 |
| outcome | κ 0.41 (−0.04 to 0.79); 58 | κ 0.21 (−0.07 to 0.64); 57 | κ 0.41 (−0.05 to 0.79); 58 |
| kind | κ 0.90 (0.78 to 0.97); 59 | κ 0.87 (0.74 to 0.97); 58 | κ 0.92 (0.82 to 1.00); 60 |
| use | κ 0.80 (0.63 to 0.94); 57 | κ 0.71 (0.52 to 0.88); 55 | κ 0.79 (0.60 to 0.93); 57 |
| evidence links in each, and in both | 5 and 6; 4 | 5 and 6; 3 | 6 and 6; 4 |

Each of the three runs gives 5 or 6 evidence links on these rows, and any two
of them share 3 or 4. That is coder 1 on table 1: few links, and not the same
few each time.

**The form of the replies.**

- **Coder 1.** "No marker" is the whole reason for judgment 1 on 45 of the 74
  rows of chat C1a in run B, against 61 in run A; and on 51 of chat C1b's,
  against 50. In run B 17 of chat C1a's reasons for judgments 2 and 3 name the
  claim by its number, and 5 of chat C1b's; in run A none did, and in the
  rerun 54. So that difference in form comes and goes between chats that were
  set up alike, by the PI's account. The script's reader took 148 file names
  out of each of coder 1's two files.
- **Coder 2** marked judgment 1 unclear on 23 rows of chat C2a and 14 of chat
  C2b, against 25 and 14 in run A. It again opens chat C2a with notes on C08
  and C42; chat C2b has notes on C20, C25 and C31, where run A had C08 and
  C25.

**The sheet beside run B.** The sheet is Fable's reading as the PI validated it,
not a human's. It again has the evidence link and both codes of coder 2 on all
20 rows; kind is now the same on all 20, and use, the condition and the author
link on 18 each. Beside coder 1's run B it has the same evidence link on 17 rows
and the same five-value code on 16.

**What run B shows, and what it cannot.**

- **It shows how steady each coder is under these rules,** on these rows: the
  six figures above. Coder 2 is somewhat the steadier on the author link, and
  coder 1 on `with`. On the evidence link they are about equally steady.
- **It shows that part of the disagreement between the coders stays and part
  moves.** Nine rows separate them under all four pairings of the two
  declared runs; fourteen more separate them or not, as one coder's run
  falls.
- **It shows that one run of each coder does not pin a figure down.** On the
  same rows, under the same rules, the evidence link's κ between the coders
  moves from 0.41 to 0.64 with the runs, and the author link's from 0.48 to
  0.65. The bar holds under none of the four pairings.
- **It answers the third thing it was declared for:** whether a third test, if
  there is one, should have each coder code its rows more than once. On these
  figures it should: one run of each coder leaves the evidence link's κ anywhere
  between 0.41 and 0.64 on the same rows.
- **It cannot show whether better rules would reach the bar,** nor what the
  chances of a third test are. A revision can only be tested on fresh rows.
- **It is two runs of each chat,** so each coder's steadiness rests on one pair
  of runs, and the intervals are wide. How the chats ran rests on the PI's
  account. Which model ChatGPT served in the evening, as in the morning, is
  known only from the name it gives itself.

## Outside the test: run C, a declared diagnostic with another ChatGPT setting

*Not part of the test. Run C is the two ChatGPT chats run once more with another
model setting, GPT 6 Astra at max. It has no bar and reads no verdict: the
test's verdict is the one read on its own run, run A. Every figure here comes
from the comparison declared before any chat of run C was opened, unless it is
marked "found by looking" or "worked out". Every figure of this section was
counted again independently, with separate code, and none differed; how each
code is derived, the κ intervals and the bar's reading were taken from the
folder's scoring.*

**Words used in this section.**

- *The test's ChatGPT* is coder 1: ChatGPT as served on 5 Oct, which calls
  itself GPT 5.6 Sol, with thinking effort at High. Its two runs are 1A, which
  is the test, and 1B, which is run B.
- *GPT 6 Astra at max* is the setting of run C. Its one run is 1C. It is not
  the test's coder. By the names on record both the model and the effort
  differ from the test's ChatGPT, so "setting" means the two together.
- *Opus* is coder 2, Opus 5.5 at Extra. Its two runs are 2A, the test, and 2B.
- *The first new pairing* is GPT 6 Astra beside Opus's run A (1C with 2A).
  *The second new pairing* is GPT 6 Astra beside Opus's run B (1C with 2B).
- *The yardstick* is what one setting gave with itself in run B: on the
  evidence link, κ 0.73 for the test's ChatGPT and 0.83 for Opus.
- A link *rests on a marker* when the coder lists a marker of the claim as
  shown. It *rests on a name alone* when the coder lists no marker and marks a
  side `named`. The few that are left rest on a contrary alone.

**In short.**

- **Under the bar's way of counting, both links are above 0.60 with GPT 6
  Astra at max beside either run of Opus:** the author link at κ 0.68 and
  0.70, and the evidence link at 0.72 and 0.68. Under none of the four
  pairings of the test's two coders were both. Each link alone had been at
  0.60 or more before.
- **What carries the evidence link over 0.60 is links that rest on a name
  alone.** GPT 6 Astra gives 12 of them, where the test's ChatGPT gave 5 and
  5, and Opus has a link on 11 and on 10 of the 12. With names not counted,
  and all else as the bar has it, the evidence link reads 0.52 and 0.57 under
  the two new pairings, which is below 0.60 (found by looking).
- **It is one run, and the intervals are wide.** For both links the lower ends
  lie between 0.48 and 0.54. Between its own two runs the test's ChatGPT moved
  by 0.17 and 0.18 on the evidence link beside the same run of Opus, and GPT 6
  Astra stands above the better of those runs by 0.14 and by 0.03. So how much
  of the difference is the setting, and how much is how one run fell, cannot
  be told.
- **The three-value code is again too few to tell.** The scoring's reading
  under both new pairings is "top-up", not "passed".
- **Nothing here is a pass.** The rows are the ones the rules failed on, and
  GPT 6 Astra was not the test's coder.

**How it ran.**

- Run C asks whether the results would differ with two coders of more comparable
  reasoning: GPT 6 Astra at max and Fable 5.1 at max. What run C is, and the
  eight things that are compared, were fixed before any chat was opened.
- **As declared, run C had two sides:** GPT 6 Astra at max for the two ChatGPT
  chats, and Claude Fable 5.1 at max for the two Claude chats. It was then
  decided to run the ChatGPT side only. What is then left of the declared points
  was fixed before any file of run C had come: 6 of the 9 pairings, and 4 of the
  9 main figures. **Two of the three things run C was declared for cannot be
  answered:** whether Fable at max reads all 148 rows as Opus does, and what the
  pair of new settings gives together.
- The script that makes the comparison was fixed by its hash before any file of
  run C had come, after two rehearsals on made-up files, and was not changed
  afterwards.
- When the files came, chat C1a was complete, and chat C1b had stopped at a
  usage limit after five of its six replies. Nothing was set beside another run
  then: the declaration says that a usage limit that resets is not a stop. The
  files' lines were seen when they came, and how many lines of each file are
  marked `unclear`, one of the declared counts, was printed then. That cannot
  have changed a figure: the script was fixed beforehand, and it was run again
  independently with the same numbers.
- The usage limit was then lifted with bought credit; the chat still showed GPT
  6 Astra at Max, and `continue` was typed. The declaration's word for a usage
  limit was to wait; credit is what happened. The complete file begins with the
  part that came first, byte for byte. Only the sixth reply and `END` were
  added.
- The PI confirmed how the chats ran: GPT 6 Astra at Max as the window showed
  it; each chat in its own Temporary Chat, with memory, custom instructions and
  web search off; the same files and messages as in the test; nothing
  regenerated or edited; and no other chat on these rows. Only then was anything
  compared, on copies. Nothing was read into the test's answers.
- For the test's chats ChatGPT's window showed no model's name. For run C the
  model and the effort are on record by the PI's confirmation, and by the first
  lines typed. How the window shows them is not on record.
- **"Work" and "Chat".** ChatGPT's window has two modes, and the picture of 5
  Oct shows the switch between them, set to "Chat". By the PI's account GPT 6
  Astra can be chosen only under "Work", under "Chat" the model cannot be seen,
  and the settings differ between the two; only run C's chats ran under "Work",
  and every other ChatGPT chat of this study under "Chat". So run C differs from
  the test's ChatGPT in the mode as well as in the model and the effort, and
  "setting" in this section covers all three. What else differs between the two
  modes is not on record.
- **How the two chats ran in time.** Side by side, by the PI's account, though
  chat C1b ended much later, after the credit was bought. When each began and
  ended is not on record.
- The first lines of the files read "Reply 1 GPT-6 Astra Max". They do not
  carry the words "run C" that the steps asked for; the folder's file names
  do.
- The results are kept apart from the test's, in `link_test2_answers_C`.

**The four main figures: the evidence link, on the 120 rows of the bar.**

| | κ (95% interval) | rows agreed |
|---|---|---|
| GPT 6 Astra with Opus's run A (1C with 2A) | 0.72 (0.54 to 0.86) | 109 |
| GPT 6 Astra with Opus's run B (1C with 2B) | 0.68 (0.49 to 0.83) | 108 |
| GPT 6 Astra with the test's ChatGPT, run A (1A with 1C) | 0.57 (0.34 to 0.76) | 107 |
| GPT 6 Astra with the test's ChatGPT, run B (1B with 1C) | 0.63 (0.41 to 0.80) | 108 |

- **Beside them, from run B:** the test's ChatGPT with itself 0.73 (0.49 to
  0.90; 113); Opus with itself 0.83 (0.68 to 0.94; 113); and the test's
  ChatGPT with Opus 0.41, 0.47, 0.58 and 0.64 under the four pairings.
- **Against the test's ChatGPT beside the same run of Opus** (worked out from
  the unrounded figures). GPT 6 Astra's figure is higher by 0.30 and by 0.14
  beside Opus's run A, where the test's ChatGPT read 0.41 and 0.58; and by
  0.21 and by 0.03 beside Opus's run B, where it read 0.47 and 0.64. The
  test's ChatGPT itself moved by 0.17 and by 0.18 between its two runs. So
  GPT 6 Astra stands above the test's ChatGPT's better run by less than that
  coder moved between its own runs. The same is so on the author link: it
  stands above the better run by 0.03 and by 0.09, where the test's ChatGPT
  moved by 0.06 and by 0.13. The better run is run B for the evidence link
  and run A for the author link: no one run of the test's ChatGPT was the
  better on both.
- **Evidence links.** GPT 6 Astra gives 22 on the 120 rows. It shares 11 with
  the test's ChatGPT's run A, which has 13, and 13 with its run B, which has
  16. Worked out from the counts: it shares 19 with Opus's run A, which has
  27, and 17 with Opus's run B, which has 24.

**The two new pairings, code by code, on the 120 rows.** The last column is
from run B's section.

| | the first new pairing (with Opus's run A) | the second (with Opus's run B) | the test's ChatGPT with Opus, over the four pairings |
|---|---|---|---|
| author link | κ 0.68 (0.48 to 0.83); 108 | κ 0.70 (0.50 to 0.86); 110 | 0.48 to 0.65 |
| evidence link | κ 0.72 (0.54 to 0.86); 109 | κ 0.68 (0.49 to 0.83); 108 | 0.41 to 0.64 |
| three-value code | κ 0.50 (0.11 to 0.80); 113 | κ 0.47 (−0.02 to 0.79); 114 | 0.25 to 0.47 |
| five-value code | κ 0.71 (0.53 to 0.85); 108 | κ 0.69 (0.51 to 0.84); 108 | not given there |
| condition | κ 0.84 (0.68 to 0.96); 115 | κ 0.78 (0.57 to 0.93); 114 | 0.43 to 0.64 |
| outcome | κ 0.65 (0.39 to 0.86); 111 | κ 0.63 (0.36 to 0.83); 111 | 0.44 to 0.76 |
| kind | κ 0.97 (0.93 to 1.00); 118 | κ 0.97 (0.93 to 1.00); 118 | 0.93 to 1.00 |
| use | κ 0.75 (0.61 to 0.87); 108 | κ 0.78 (0.63 to 0.90); 110 | 0.59 to 0.70 |

- **By half, on the evidence link:** 0.67 (0.44 to 0.85; 55 of 63) and 0.63
  (0.37 to 0.84; 55) in the first half; 0.79 (0.51 to 1.00; 54 of 57) and
  0.74 (0.44 to 0.94; 53) in the second. With the test's ChatGPT the first
  half read 0.24 to 0.50 and the second 0.65 to 0.87. So on the evidence link
  the halves lie closer together with GPT 6 Astra, about 0.1 apart against
  0.3 to 0.5, and the first half is still the lower. On the author link they
  do not lie closer (found by looking): 0.56 and 0.56 in the first half, and
  0.85 and 0.92 in the second.
- **On all 148 rows.** The declaration names them, and the script does not print
  them for these two pairings. Worked out afterwards, twice, independently: the
  evidence link κ 0.66 (0.50 to 0.79; 130 of 148) and 0.66 (0.49 to 0.80; 131);
  the author link 0.67 (0.50 to 0.80; 132) and 0.66 (0.48 to 0.80; 133); the
  three-value code 0.51 (0.20 to 0.76; 138) and 0.53 (0.18 to 0.79; 140).
- The evidence link differs on 11 rows of the bar under the first new pairing
  and on 12 under the second.

**GPT 6 Astra beside the test's ChatGPT, on the 120 rows.** The last column is
the yardstick: the test's ChatGPT with itself.

| | with run A (1A with 1C) | with run B (1B with 1C) | the test's ChatGPT with itself (1A with 1B) |
|---|---|---|---|
| author link | κ 0.70 (0.51 to 0.85); 108 | κ 0.54 (0.31 to 0.71); 103 | κ 0.72 (0.54 to 0.86); 109 |
| evidence link | κ 0.57 (0.34 to 0.76); 107 | κ 0.63 (0.41 to 0.80); 108 | κ 0.73 (0.49 to 0.90); 113 |
| three-value code | κ 0.52 (−0.01 to 0.85); 115 | κ 0.65 (0.23 to 0.92); 116 | κ 0.90 (0.66 to 1.00); 119 |
| condition | κ 0.49 (0.22 to 0.72); 108 | κ 0.58 (0.29 to 0.80); 111 | κ 0.69 (0.37 to 0.92); 115 |
| outcome | κ 0.57 (0.27 to 0.79); 111 | κ 0.76 (0.51 to 0.94); 115 | κ 0.63 (0.34 to 0.84); 112 |
| kind | κ 0.90 (0.82 to 0.97); 113 | κ 0.97 (0.93 to 1.00); 118 | κ 0.93 (0.86 to 0.99); 115 |
| use | κ 0.74 (0.57 to 0.86); 107 | κ 0.63 (0.47 to 0.78); 103 | κ 0.77 (0.63 to 0.88); 109 |
| every code the coder writes for a row | the same on 85 | the same on 89 | the same on 94 |

The last row counts the six codes a coder writes: the condition and the
outcome with `named`, other cause, `bounded`, kind and use.

- **Read against the yardstick,** GPT 6 Astra differs from the test's ChatGPT
  on the evidence link somewhat more than the test's ChatGPT differs from
  itself: 0.57 and 0.63 against 0.73. The intervals overlap widely. On kind
  it is the same reader.
- **On all 148 rows,** the evidence link reads κ 0.60 (0.41 to 0.75; 131 of
  148) and 0.62 (0.44 to 0.77; 131), against 0.80 (0.65 to 0.92; 140) for the
  test's ChatGPT with itself.
- **By half,** the evidence link reads 0.37 (0.07 to 0.65; 53 of 63) and 0.46
  (0.12 to 0.72; 54) in the first half, against 0.50 for the test's ChatGPT
  with itself; and 0.79 (0.50 to 1.00; 54 of 57) and 0.81 (0.56 to 1.00; 54)
  in the second, against 0.87.

**The bar's five conditions under the two new pairings.** Read by the
scoring's own code on scratch copies, as a diagnostic. Neither is a scoring of
the test.

| condition | the first new pairing (with Opus's run A) | the second (with Opus's run B) |
|---|---|---|
| 1. author link | 0.68: holds | 0.70: holds |
| 2. evidence link | 0.72: holds | 0.68: holds |
| 3. three-value code | 0.50: too few to tell | 0.47: too few to tell |
| 4. hard rows agreed | 11 of 18: holds | 14 of 18: holds |
| 5. `not found` | none on either side: holds | none on either side: holds |
| the scoring's reading | top-up | top-up |

- **"Top-up" is not "passed".** It is what the plan gives when condition 3 is
  too few to tell and the other four hold: 60 more rows are coded, and
  condition 3 is read once more. No top-up is drawn here; the declaration
  rules it out. GPT 6 Astra gave `with` to 6 of the 120 rows, and Opus to 9
  in run A and to 6 in run B. None of the three runs gave `against`.
- **Condition 4 holds by one row under the first new pairing.** It needs more
  than 10 of the 18, and 11 agree. That is the fewest of the six pairings:
  the earlier four had 13, 16, 13 and 16.
- **Of the six pairings there are now two under which conditions 1 and 2 hold
  together.** Both have GPT 6 Astra in them.
- **Found by looking: the other ways of counting.** The scoring gives each
  pairing under 32 ways of counting, of which the bar's is one.
  - With names not counted, and all else as the bar has it, the evidence link
    reads κ 0.52 (0.27 to 0.74; 108 of 120) under the first new pairing and
    0.57 (0.26 to 0.81; 111) under the second. Both are below 0.60. The same
    line reads 0.32, 0.43, 0.57 and 0.72 under the four earlier pairings. So
    without names GPT 6 Astra agrees with Opus no better than the test's
    ChatGPT did in its run B, and better than it did in its run A. The
    highest figure without names is 0.64 under both new pairings, when
    patterns are also taken as readings.
  - Over all 32 ways the evidence link runs from 0.52 to 0.72 under the first
    new pairing, and is at 0.60 or more in 24 of them. Under the second it
    runs from 0.56 to 0.68, and is at 0.60 or more in 16. The author link does
    not depend on the way of counting.
  - Set way for way against the same counting with names, leaving names out
    gives the lower κ in all 16 ways under the first new pairing, and in 8 of
    16 under the second.

**Counts, on the bar's rows:** all 120, with the first and the second half in
brackets.

| | the test's ChatGPT, run A | the test's ChatGPT, run B | GPT 6 Astra | Opus, run A | Opus, run B |
|---|---|---|---|---|---|
| evidence links | 13 (5 and 8) | 16 (6 and 10) | 22 (13 and 9) | 27 (19 and 8) | 24 (15 and 9) |
| author links | 27 (17 and 10) | 22 (13 and 9) | 23 (15 and 8) | 23 (15 and 8) | 17 (10 and 7) |
| `with` | 5 (0 and 5) | 6 (1 and 5) | 6 (3 and 3) | 9 (7 and 2) | 6 (3 and 3) |
| rows with a marker listed | 9 (1 and 8) | 10 (2 and 8) | 10 (2 and 8) | 20 (10 and 10) | 16 (6 and 10) |
| links that rest on a name alone | 5 (4 and 1) | 5 (3 and 2) | 12 (10 and 2) | 9 (8 and 1) | 11 (9 and 2) |
| links that rest on a marker listed | 6 (0 and 6) | 8 (2 and 6) | 7 (2 and 5) | 15 (10 and 5) | 10 (5 and 5) |
| links that rest on a contrary alone | 2 (1 and 1) | 3 (1 and 2) | 3 (1 and 2) | 3 (1 and 2) | 3 (1 and 2) |
| judgment 1 marked unclear | 0 | 0 | 14 (9 and 5) | 30 (20 and 10) | 26 (17 and 9) |

- **Where GPT 6 Astra stands between the two.**
  - *Like Opus:* links that rest on a name alone. It has 12, where Opus has 9
    and 11 and the test's ChatGPT 5 and 5. Ten of its 12 are in the first
    half.
  - *Like the test's ChatGPT:* the markers it lists. It lists a marker on 10
    rows and has 7 links by a marker, where the test's ChatGPT has 9 and 10
    rows and 6 and 8 links, and Opus 20 and 16 rows and 15 and 10 links.
  - *Between the two:* evidence links (22; 13 and 16; 27 and 24), and rows
    marked unclear in judgment 1 (14; none; 30 and 26).
- **Found by looking: what its links by a name alone meet.** Opus has a link
  on 11 of the 12 in run A and on 10 in run B, by a name alone on 8 each
  time. So 11 of the 19 links that GPT 6 Astra shares with Opus's run A, and
  10 of the 17 it shares with run B, are its links by a name alone. The
  test's ChatGPT has a link on 5 of the 12 in run A and on 6 in run B. So of
  the 13 rows on which GPT 6 Astra and the test's ChatGPT's run A differ on
  the evidence link, 7 are links that GPT 6 Astra gives by a name alone; and
  of the 12 for run B, 6. That is about half.
- **Found by looking: where GPT 6 Astra and Opus still part.** Under the first
  new pairing Opus alone has the link on 8 rows, and 6 of those links rest on
  a marker it lists; GPT 6 Astra alone has the link on 3. Under the second,
  Opus alone has it on 7, by a marker on 3, by a name alone on 3 and by a
  contrary on 1; GPT 6 Astra alone has it on 5. So beside Opus's run A what
  still separates the two is mostly a marker that Opus lists. Beside run B
  it is as often a name.

**The rows already singled out.**

- **The 9 rows on which the test's two coders differ under all four
  pairings.** On the 7 where Opus has the link in both runs and the test's
  ChatGPT in neither, GPT 6 Astra has the link on 4: R010, R034 and R069 by a
  name alone, and R009 by a marker it lists. It has none on 3: R028, R053 and
  R057. On the 2 the other way round, it has the link on R086, as the test's
  ChatGPT does, and none on R134, as Opus has none.
- **The 13 rows named in run B's declaration.** GPT 6 Astra has a link on 7
  of them (R008, R009, R010, R033, R034, R069 and R070), and marks judgment 1
  unclear on 6 of the 13. The test's ChatGPT had a link on none of them in
  run A and on 2 in run B; Opus on all 13 in run A and on 8 in run B.

**Kind.** GPT 6 Astra gives no fragment two kinds, within a chat or across its
two chats. Its kind is Opus's on 118 of the 120 rows, beside either run.

**The hard rows.** GPT 6 Astra gives 16 of the 18 the five-value code that the
test's ChatGPT gave in both its runs. On the other two it stands alone: it has
`with` on R133, where the four earlier runs have no link, and no link on
R097, where the four have `illustrates`. With Opus it agrees on 11 of the 18
under the first new pairing and on 14 under the second. No twin pair is
split.

**The form of the replies.** Each of the two files has all 74 lines for
judgment 1 and all 74 for judgments 2 and 3, with no line to ask for again and
no row `not found`. Unlike the test's ChatGPT in either run, GPT 6 Astra never
gives "no marker" as the whole reason for judgment 1; the test's ChatGPT did
on 61 and 50 rows of its two chats in run A, and on 45 and 51 in run B. It
marks judgment 1 unclear on 11 rows of chat C1a and on 9 of chat C1b. Three of
chat C1b's reasons for judgments 2 and 3 name a claim by its number. The
script's reader took no file name out of either file.

**The sheet beside run C.** The sheet is Fable's reading as the PI validated it,
not a human's. Beside GPT 6 Astra it has the same evidence link on 17 of the 20
rows, the same author link on 19, the same three-value code on 19 and five-value
code on 17, the same kind and the same use on 19 each, the condition on 17 and
the outcome on 18.

- *On the evidence link* that is where the test's ChatGPT stood, with 16 rows
  in run A and 17 in run B.
- *On four of the other seven codes* GPT 6 Astra has more rows the same as the
  sheet than the test's ChatGPT had in either run: the author link on 19 rows
  against 18 and 17, the three-value code on 19 against 18 and 18, the
  five-value code on 17 against 15 and 16, and use on 19 against 17 and 17.
  On kind (19, against 18 and 19) and on the condition (17, against 15 and
  17) it is level with the test's ChatGPT's run B. On the outcome (18,
  against 17 and 19) it is one row below run B.
- Opus has the evidence link and both codes of the sheet on all 20 rows in
  both runs.

**What run C shows, and what it cannot.**

- **It shows that another ChatGPT setting can give other figures on the same
  rows.** Under the same rules, under the bar's way of counting and beside
  the same two runs of Opus, GPT 6 Astra at max gave both links above 0.60.
  The test's ChatGPT did not, in either of its runs.
- **It does not show how much of that is the setting.** GPT 6 Astra ran once.
  On both links it stands above the test's ChatGPT's better run by less than
  that coder moved between its own two runs. A second run of GPT 6 Astra
  could fall lower, or higher.
- **It shows that about half of what separates the two ChatGPT settings on the
  evidence link is names.** GPT 6 Astra counts a name alone as Opus does, and
  the test's ChatGPT mostly does not. With names not counted, and all else as
  the bar has it, the evidence link is below 0.60 under both new pairings
  (found by looking). So what carries the evidence link over 0.60 rests on a
  rule that a revision of judgment 1 would change.
- **It answers in part the first thing it was declared for:** whether the
  other ChatGPT setting reads these rows more like the Claude side or like
  the test's ChatGPT. On the evidence link it stands nearer to Opus (κ 0.72
  and 0.68) than to the test's ChatGPT (0.57 and 0.63). The intervals
  overlap, so "nearer" is a reading of four figures and not a tested
  difference. In what it counts it is like Opus in one thing, links by a name
  alone; like the test's ChatGPT in another, the markers it lists; and
  between the two in the rest. On the author link it stands no nearer to
  Opus: 0.68 and 0.70 beside Opus, and 0.70 and 0.54 beside the test's
  ChatGPT.
- **It cannot say which reader is right.** To agree with Opus is not to be
  right. Beside the sheet GPT 6 Astra stands where the test's ChatGPT stood
  on the evidence link, and has more rows the same as the sheet on four of
  the other seven codes; and the sheet is itself a Claude model's reading.
- **It is not a pass, and it cannot be made one.** The rows are the ones the
  rules failed on, the run was made after both results were known, and GPT 6
  Astra was not the test's coder. Under the plan a failed rule is never
  scored again on the same rows.
- **It was not declared to show a third test's chances, and it cannot.** It is
  one run, of rules that a revision would change.
- **It says nothing about better rules, and nothing about Fable at max.** That
  side of run C was not run.
- **How the chats ran rests on the PI's account.** For this run the times are
  not on record, and the sixth reply of chat C1b came after credit was bought
  and not after a wait.

## After the test

*None of this section is the plan's. It was written after the result.*

**Decided on 6 Oct: no third test for this package.** So:

- no third test is made for this package, and the verdict stands: not
  passed;
- the results of both tests, of run B and of run C go into the proposal as
  findings about the instrument;
- no revision of judgment 1 is drafted now. Version 2.1 is reported as what
  was tested, and nothing is coded under it. Brief v2 and the cold-paper
  coding instructions stay as frozen;
- a third test stays possible after the package, on a fresh draw.

**What the results bear on.**

- **What the test supports keeping:** kind, with `pattern`. Run B bears it
  out: each coder gives a row the same kind in both runs on 115 and on all
  120 of the 120 rows (κ 0.93 and 1.00), and the two coders agree on kind at
  κ 0.93 to 1.00 under the four pairings.
- **The author link is at the bar, not over it.** It held in the first test's
  scored run (κ 0.69, interval about 0.33 to 0.93) and here (0.65, 0.45 to
  0.80); in the first test's rerun it stood just under the bar (0.598).
  Between the coders it runs from 0.48 to 0.65 under the four pairings of run
  A and run B, and it is under 0.60 in two of them. With GPT 6 Astra at max
  in coder 1's place it reads 0.68 and 0.70 beside coder 2's two runs (run C,
  one run; the lower ends are 0.48 and 0.50). That is above coder 1's better
  figure beside each of those runs by 0.03 and 0.09, where coder 1 itself
  moved by 0.06 and 0.13 between its runs.
- **Where judgment 1 would be revised,** as read from coder 2's reasons: what a
  coder does when it doubts whether a showing needs something added; when a word
  is a name; when the contrary of a marker rules a side out. Run B points the
  same way (both counts found by looking). On 7 of the 9 rows where the coders
  differ under all four pairings, coder 2 gives a link that coder 1 gives in
  neither declared run: by a name alone on 4, and by a marker it lists on 3. (On
  one of the 7, R057, coder 1 did give a link in the PI's rerun.) And 6 of the 7
  rows on which coder 2's own two runs differ are rows it had marked unclear.
  Run C bears on names too, in another way. GPT 6 Astra gives links by a name
  alone as coder 2 does: 12 on the 120 rows, where coder 1 has 5 and 5 and coder
  2 has 9 and 11; and coder 2 has a link on 11 and on 10 of those 12 (found by
  looking). So the rule on names is read in one way by coder 1 and in another by
  coder 2 and by GPT 6 Astra. Beside coder 2's run A, what still separates GPT 6
  Astra from coder 2 is mostly a marker that coder 2 lists: 6 of the 8 rows on
  which coder 2 alone has the link. Beside its run B it is a marker on 3 of the
  7 and a name alone on 3 (found by looking). In the markers it lists, GPT 6
  Astra is as coder 1 is. And it marks judgment 1 unclear on 14 rows, where
  coder 1 marked none.
- **Use needs a look too.** On the 60 linked rows use and the author link are
  both under 0.60, and 13 of the 14 disagreements on the author link are on
  linked rows. In five of the nine where coder 1 has the link and coder 2 has
  none, coder 2's reason is the rule for a broad claim and a narrow one. † The
  author link is read from use alone, so a coder's unsteadiness on it is
  unsteadiness on use: in run B coder 1 changed it on 11 rows and coder 2 on
  6.
- **What this test could not show about the markers and the passages:** how
  much the links depend on who writes them. In 47 of 52 claims a second set
  would count different things; 17 claims have a side no marker can show; and
  5 of coder 1's 13 links and 9 of coder 2's 27 are lost when names are not
  counted. †
- **How far the disagreement comes from the rules and how far from the run**
  was the open question after the result. The run means how one chat happened
  to code on one occasion. Run B gives a first answer, for these rows. Each
  coder agrees with itself at κ 0.73 and 0.83 on the evidence link. The two
  agree with each other at 0.41 to 0.64, as the runs fall. So part of the
  disagreement is between the coders and is there under all four pairings of
  the two declared runs (9 rows), and part moves with the run (14 rows). The
  two are still not separate: rules that leave doubtful cases open make one
  model disagree with itself too.
- **A third test's chances: what the figures say, and what they do not.** Run
  B was not declared to show them and cannot, and neither was run C. How much
  a revision gains is shown only on fresh rows. Five things bear on them. None
  measures a revised version.
  - *The plan's figures.* They are rough, from a simulation that takes one true
    κ for all three codes and counts the top-up. The bar passes about one time
    in six at a true κ of 0.60, about two times in three at 0.70, and about nine
    times in ten at 0.75. How many of all such tests go to the top-up hangs on
    how rare `with` is: at a true κ of 0.70, about six in ten with `with` on 5%
    of the rows, and about three in ten at 8%. Here each coder gave `with` to 5
    to 9 of the 120 rows, which is 4% to 8%. The simulation also takes both
    coders to give each code at the same rate, an evidence link on 22% or 25% of
    the rows, and `with` on 20% or 25% of the top-up's rows; and it leaves
    conditions 4 and 5 out. Here coder 1 gave an evidence link to 11% to 13% of
    the rows and coder 2 to 20% to 23%. And on the 33 linked rows of the bar
    that are of the kind a top-up draws, each coder gave `with` to 2 to 5, which
    is 6% to 15% (found by looking). So the table is, if anything, on the kind
    side. An independent run of the simulation reads it so too: there it was the
    lower rate of `with` in the top-up's rows that moved the figure most.
  - *Where version 2.1 stands,* between the coders, over the four pairings:
    0.41 to 0.64 on the evidence link, 0.48 to 0.65 on the author link, and
    0.25 to 0.47 on the three-value code.
  - *How much room there is.* Each coder agrees with itself at κ 0.73 and
    0.83 on the evidence link and at 0.72 and 0.82 on the author link. Those
    figures are over the bar, and about where the plan's table makes a pass
    likely. Two coders mostly agree with each other no better than each does
    with itself, though that is no strict rule: here kind and the outcome
    break it under two pairings. So if a revision took away what separates
    the two coders, the links could reach the bar. The room is version
    2.1's, from one pair of runs for each coder, with wide intervals, and a
    revision would move it. On the three-value code coder 2's own figure is
    0.65: over the bar, and under the 0.70 at which the plan's table has the
    bar passing two times in three.
  - *What the last revision did* cannot be told. The evidence link read κ
    0.38 in the first test and 0.44 in its rerun, on 42 rows; here it reads
    0.41 to 0.64 over the four pairings, on other rows. The intervals overlap
    widely.
  - *What another ChatGPT setting gave (run C).* Run C was not declared to
    show a third test's chances either. What it gives: with GPT 6 Astra at
    max beside Opus 5.5 at Extra, version 2.1 as it stands read the author
    link at κ 0.68 and 0.70 and the evidence link at 0.72 and 0.68, on these
    rows, under the bar's way of counting. Read them with their limits.
    - They come from one run of GPT 6 Astra, set beside two runs of coder 2
      that agree with each other at 0.83. So they are not four separate
      readings.
    - They are observed figures, and by the plan a link's κ moves by about
      ±0.18 by chance on 120 rows. Their lower ends lie at 0.48 to 0.54.
    - They stand above coder 1's better run by less than coder 1 moved
      between its own two runs.
    - With names not counted, and all else as the bar has it, the evidence
      link reads 0.52 and 0.57 (found by looking), and the rule on names is
      one a revision would change.
    - The plan's table cannot be read across to them. It takes one true κ for
      all three codes, and under these two pairings the three-value code read
      0.50 and 0.47 and was too few to tell.

  So the figures still leave a third test's chances open. The judgment before
  run C was that a pass at the first try of a new revision is the less likely
  end, for two reasons: it needs both links and the three-value code to come
  right together; and in neither test's own run did the evidence link reach the
  bar. Run C leaves the first reason as it was: the three-value code read "too
  few to tell" under five of the six pairings and "not passed" under the test's
  own. It weakens the second, for one pair of settings: beside coder 2, GPT 6
  Astra at max had both links at 0.60 or more, on one run. It stood above coder
  1's better figure by less than coder 1 itself moved between its two runs, and
  the evidence link got over 0.60 by way of the rule on names. So the judgment
  stands, and nothing measures it.

  What may be expected of a third test, as a judgment and no more: with the
  test's own pair of coders, "not passed" on a link, as before. With GPT 6 Astra
  at max beside Opus 5.5 at Extra there is no expectation either way on the two
  links. If both links hold, the test would more likely than not go to the
  top-up, since the three-value code was too few to tell under both pairings
  where they did; and it could then end with the links held and the direction
  code left open.
- **A human reading.** The test has no independent one. If a third test is run,
  whether the PI codes its sheet by hand is to be decided before it starts.
  Whatever comes next, the proposal has to describe the sheet as what it was.
- **The Fable chat's suggestions** are one reader's, written with table 1's
  rows in view and without coder 2's answers. They bear more on coder 1's
  steadiness than on the disagreement between the coders. They can feed a
  revision. Under the plan a revision is tested on a fresh draw, so the 19
  rows can serve as a check while rewriting, and never as the test.
