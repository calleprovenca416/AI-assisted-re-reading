# The matching test (T33): does a fixed reference make the counting of openings repeatable?

Fixed on 14 Oct 2026, before any chat of the test (chats 49 to 54). Nothing in
it was changed after; the one change is set out at the foot, with its reason.

## What it asks

1. **Q1.** Does a fixed reference for the paper (its claims, numbered, and its
   passages with their pages and voice, taken from the frozen record) make the
   grouping of readings by the point they make more repeatable between two
   coders than grouping without it, without losing agreement with the PI's own
   grouping?
2. **Q2.** Do the openings of a second vendor's plain readings recur among those
   of the four earlier runs on the paper, all Fable 5.1?
3. **Q3.** How many readings fit no claim of the reference: its measured gap.

## The readings

- **The 14 readings of Bechky in the wager test (11 Oct):** B01 to B14 of
  `stage2/markers/KEY.json`, their sentences joined in order, as the markers
  read them; from chats 23 (generation from the record), 26 (the reading chat)
  and 27 (the plain chat), all Fable 5.1 at max.
- **The 4 readings of chat 46 (13 Oct, Fable 5.1 at max):** W01, W03, W05 and W06
  of `places_packs_key.json`, their sentences joined in order, as the markers
  read them, with the edits of `places_pack_edits.json`.
- **The readings of chats 49 and 50 (new):** GPT 6 Astra at max, each in a fresh
  ChatGPT Temporary Chat, given Bechky's PDF and `ALTERNATIVE_READINGS.md` with
  the message `BASELINE_SEND.md` gives the plain chats, word for word; up to five
  readings each. Each is put in the form of the plain readings of 11 Oct by the
  same code (`build_marker_packs.py`: the wager, then each piece of evidence's
  job with its page, the pages then made alike).
- **Left out:** the four readings of chat 45, written at places chosen for the
  chat, so that their points were not its own choice.
- All of them are shuffled with the seed 20261014 and numbered M01 onward.
  `READINGS_matching.md` gives each as one paragraph; `matching_key.json`, for
  nobody, says which came from where.

## The arms

Each arm has two coders, one Claude and one ChatGPT, each in a fresh chat with
the markers' settings of 13 Oct: Opus 5.5 at Extra in an incognito claude.ai
chat (web search, research and every connector off; file creation on, with its
network access off; no profile preferences or style); GPT 6 Astra at max in a
ChatGPT Temporary Chat (memory, custom instructions and web search off; no
project).

- **Arm A, without the reference:** chats 51 (Opus) and 52 (Astra), given the
  PDF, `MATCHING_A.md` and `READINGS_matching.md`. For each reading: the claim
  of the paper it contests most directly, in the coder's own words, with the
  pages where the paper makes it, and the reading's alternative in one sentence.
  Then a grouping of all the readings by the point they make.
- **Arm B, with the reference:** chats 53 (Opus) and 54 (Astra), given the same
  three files and `REFERENCE_bechky.md`: the record's 23 claims, numbered, with
  their statements and pages, and its 172 passages, numbered, each with its
  page, the unit it concerns, its voice and its one-sentence summary; no links,
  pairs, gaps, `core` or other codes. For each reading: the number of the claim
  it contests most directly, or `none`; up to three other claims it also
  contests; up to five passages its case rests on most; its alternative in one
  sentence. Then a grouping of all the readings by the point they make, as in A.
- **The rule for the same point,** the same in both arms and on the PI's sheet:
  two readings make the same point when they contest the same claim of the
  paper with the same alternative account, whatever their wording, emphasis or
  evidence. Each reading is grouped by its main point, the one its wager states
  first; a reading whose point no other reading makes is a group of its own;
  every reading is in exactly one group. The claim a reading contests **most
  directly** is the one whose statement its main point denies, replaces or
  re-explains; where a claim about one unit or episode and a general claim both
  fit, it is the specific one. One example, from a made-up paper with no
  content of Bechky's, goes with the rule wherever it is given.

## The anchor

The PI's own grouping of all the readings by the same rule, on
`grouping_sheet.xlsx`, made before any coder chat opens and without seeing any
coder's reply. The PI has read the 18 earlier readings before and rated them, so
the PI's grouping is not blind to their sources; it is blind to both arms. Once it is
in, the PI's worth sheet for the readings of chats 49 and 50, on the wager test's
scale (0 to 3), not blind to their source.

## The groupings compared

- **A1, A2:** the groupings of chats 51 and 52.
- **B1, B2, by rule:** from the claim numbers of chats 53 and 54: readings given
  the same claim form one group, and each reading given `none` is a group of its
  own. This is the archive's own procedure, a count made by rule from the
  reference.
- **B1j, B2j, judged:** the groupings chats 53 and 54 make themselves.
- **B1p, B2p, by rule, finer:** within each claim's group, two readings joined
  when they name at least one passage in common, and the groups those joins form.
- **P:** the PI's grouping.

## The measures

- **Agreement between two groupings:** over every pair of distinct readings,
  whether each grouping puts the pair together or apart, and Cohen's kappa on
  those pair labels: the **pair kappa**. The adjusted Rand index is given beside
  it.
- **Uncertainty:** 2,000 bootstrap resamples of the readings, seed 20261014:
  readings drawn with replacement, pairs formed among drawn readings that are
  copies of different readings, and every kappa computed on the same resample.
  The 2.5th and 97.5th percentiles of a difference between two kappas give its
  95% interval; a resample in which a kappa cannot be computed is left out, and
  the count of those is given.
- **Q1:**
  - **A** = pair kappa of A1 and A2; **B** = pair kappa of B1 and B2; the gain
    **B − A**, with its interval.
  - **P_A** = the mean of the pair kappas of A1 with P and of A2 with P;
    **P_B** = the mean of those of B1 and B2 with P.
  - The same for B1j and B2j (**Bj**, **P_Bj**) and for B1p and B2p (**Bp**,
    **P_Bp**), as second figures.
  - **Claim agreement in arm B:** Cohen's kappa on the two coders' claim
    numbers, `none` counted as a code, over all readings.
- **Q2,** on P: the groups that hold readings of at least two of the four earlier
  chats (23, 26, 27 and 46), the **groups found twice**; how many of them hold a
  reading of chat 49 or 50; how many of the new readings share a group with any
  earlier reading; and how many of chat 49's groups hold a reading of chat 50.
- **Q3:** the share of readings that chat 53 gives `none`, that chat 54 does,
  and that both do.
- **Described, not tested:** for each group of P, the voice of the passages
  chats 53 and 54 name for its readings.

## What counts as an answer, fixed now

**Q1,** with A, B, P_A and P_B as above:

1. **Repeatable without the reference:** A ≥ 0.80. The coders group alike
   without it, and the reference is not needed for this.
2. **The reference makes the count repeatable:** not case 1; B − A ≥ 0.15, with
   its 95% interval above 0; and P_B ≥ P_A − 0.05.
3. **Repeatable, but coarser than the PI's grouping:** not case 1; B − A ≥ 0.15,
   with its interval above 0; but P_B < P_A − 0.05.
4. **No clear gain:** any other result.

Whatever the case, **neither arm finds the PI's points** if P_A and P_B are both
below 0.40. The four cases are also given with Bj and P_Bj in place of B and
P_B, as a second reading: with the reference, judged. Where a kappa cannot be
computed (a grouping with no pair together, or with every pair together), the
case is **not decided**, with the reason.

**Q2:** the openings **recur across vendors** if at least half of the groups
found twice hold a reading of chat 49 or 50; **in part** if at least one does,
but fewer than half; **not** if none does.

**Q3** is given as figures, with no bar.

## Checks on the replies

A coder's reply counts if it is one JSON object of the form its instructions
give, names every reading exactly once in its list of readings, and puts every
reading in exactly one group; in arm B, every claim number is one of C01 to C23
or `none`, and every passage one of F01 to F172. A reply that fails is recorded
with its faults, and the chat gets the fixed answer of its steps once. If it
fails again, it is reported, and the figures that need it are given as not
decided. No reply is edited. The replies of chats 49 and 50 count if each is one
JSON object of the prompt's form with one to five readings; one that is not is
recorded, and the chat is not run again.

## The order

1. This plan, fixed by its hash.
2. Chats 49 and 50, by `ASTRA_PLAIN_SEND.md`.
3. Before their replies are opened: `MATCHING_A.md`, `MATCHING_B.md`,
   `REFERENCE_bechky.md`, `build_matching_pack.py` and `score_matching.py`
   written, the scorer tested on made-up groupings, and all of them fixed by hash.
4. The replies of chats 49 and 50 read as untrusted files, and the pack built:
   `READINGS_matching.md`, `matching_key.json`, `grouping_sheet.xlsx`.
5. The PI's grouping, made before any coder chat opens.
6. Chats 51 to 54, side by side, by `MATCHING_SEND.md`; and the PI's worth sheet
   for the new readings.
7. The scorer run, `MATCHING_RESULTS.md` written, and its figures checked
   against the files by an independent recomputation.

## Limits, known now

- One paper; about 28 readings; one person's grouping, not blind to the sources
  of the 18 the PI has read; the coders are models, two to an arm.
- The reference is one version of the record (Bechky v1, frozen on 7 Oct), with
  the limits set out in `FRAGMENT_LESSONS.md`; the counts are relative to it.
- Arm B's coders get more to read than arm A's, and a gain could come from the
  list of claims alone: the test does not separate the claims from the passages.
- The rule "same claim, same group" puts two different alternatives to one
  claim in one group; P_B against P_A is there to show whether that matters.
- GPT 6 Astra writes two of the readings and codes in both arms.
- The bars (0.80, 0.15, 0.05, 0.40) are judgments fixed in advance, not
  standards.

## The PI's time

About 25 minutes for chats 49 and 50, side by side; under an hour for the PI's
grouping; ten minutes for the worth sheet; about 30 minutes for chats 51 to 54,
side by side.

---

## Change after the plan was fixed

**14 Oct 2026: the anchor came after the coders.** The four coder chats (51 to
54) ran, as `MATCHING_SEND.md` says, about five minutes each, before the PI's
grouping was made. The PI then grouped from the sheet alone, without opening any
coder reply again; a second, blind grouping by someone who had seen none of the
material was not possible, and whether the PI had read the coders' groups when
saving their replies is not on record. So the PI's grouping is not blind to the
coders' replies, and every figure that uses it (P_A, P_B, P_Bj, P_Bp, and all of
Q2) is reported with that caveat. The figures between the coders (A, B, Bj, Bp
and their differences, and the claim agreement in arm B) do not use it and
stand as planned. Nothing else changes.
