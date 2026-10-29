# The link-definition test

*29 September 2026. Who may receive this file: nobody (—).*

**The question.** Can a link between a fragment and a claim be defined so that two
independent coders apply it the same way, and more reliably than under brief v2?
The test answers this on Pratt's hard cases and on a random sample, before any
brief v3, re-extraction or new linking stage. Nothing downstream changes until the
result is read.

---

## Decided on 29 Sep

1. Test the link definition first. This is step 2 of the revised proposal.
2. Write the new rules in full, direction included, before any pair is chosen.
3. Record how the paper itself uses a passage for a claim as its own judgment,
   from the page: the author link.
4. Have the rules and the test files reviewed independently before any chat is
   run.
5. Set the pass bar after reading the rules, and before any chat is run.
   *Set on 30 Sep as recommended below, unchanged, before any chat, and recorded
   in `link_test_bar.json`.*
6. Bechky and the two other papers wait until the test is read.

## What happened, in order

| day | step |
|---|---|
| 29 Sep | version 1 of the rules frozen, and a sample drawn (seed 20260929) |
| 29 Sep | a review, asked for before any chat: five blocking findings and six minor ones. The version-1 freeze, key and sample were set aside unused (`link_test_freeze_v1.json`, `link_test_key_v1.json`). No coder saw them |
| 29 Sep | version 1.1 written |
| 29 Sep | second review, before any freeze: three blocking findings and five minor ones, all fixed |
| 29 Sep | version 1.1 frozen, with the seed (29092026) recorded in the freeze |
| 29 Sep | the version-1.1 sample drawn |
| 30 Sep | the pass bar set (the recommendation, unchanged) and the PI's sheet filled, before any chat |
| 30 Sep | the bar recorded (`link_test_bar.json`). No answer had been read; the folder for answers did not yet exist |
| 30 Sep | the PI's sheet filed as `link_test_human_sheet_filled.xlsx` (sha256 41a39b8a…). It reads clean: 18 claims and 20 rows, every cell filled with an allowed value, the given columns unchanged. It is not compared with anything until the four replies are in |
| 30 Sep | ChatGPT's two chats received, saved as RTF; both chats kept open until they were checked |
| 30 Sep | both turned into text (`reply_rtf_to_txt.py`: LibreOffice, line separators made newlines; pandoc gives the same text) and read clean. v2: 60 rows. New rules: 33 claims, 60 stub rows, 60 page rows, the 15 re-check rows. Each file has one row its coder marked unclear, which the format allows. Nothing scored |
| 30 Sep | Opus's two chats received as text. Opus 5.5 ran at medium effort; maximum had been recommended. The v2 file had lost its 18 dashes when saved (each became "�"). Every one sat in the direction cell of a row marked "no", where only a dash is allowed, so they were restored in `reply_opus_v2.txt`, and the file as saved is kept as `reply_opus_v2_as_saved.txt`. Nothing else changed |
| 30 Sep | both read clean. v2: 60 rows. New rules: 33 claims, 60 stub rows, 60 page rows, the 15 re-check rows. Both chats kept open until they were checked |
| 30 Sep | scored, with the PI's sheet: **not passed**. Four of the nine conditions hold. See `LINK_TEST_RESULT.md` |
| 30 Sep | a rerun of Opus at a higher setting ("high or extra") decided, its replies at medium having come back much faster. Declared below, before the rerun |
| 30 Sep | the rerun received (run B): both Opus chats at extra effort, saved as RTF |
| 30 Sep | both read clean, in a copy of the folder (`link_test_answers_B/`). The first run's answers and report untouched |
| 30 Sep | the rerun scored against ChatGPT with the same script and bar: **not passed**; four of nine hold, not the same four |
| 30 Sep | the two Opus runs compared (`link_test_compare_runs.py`): the derived code changed on 4 of 60 rows. The setting is not what made the models disagree. See the last section of `LINK_TEST_RESULT.md` |

## The Opus rerun: declared 30 Sep, before it is run

- **What it is for.** To show how much of the disagreement came from Opus's
  setting. It is a diagnostic. The verdict above is the test's result and stays
  as recorded.
- **How it runs.** Both Opus chats again, v2 and new rules, in fresh incognito
  chats. Both use the same higher setting, so the comparison with v2 stays like
  for like. The files, messages and re-check list are the same as in chats 2
  and 4 of `LINK_TEST_SEND.md`. ChatGPT's answers are kept as they are.
- **How it is scored.** The same script, unchanged, and the same bar, run in a
  copy of the folder that holds ChatGPT's answers and the rerun's. The first run's
  report is not touched. The rerun's report is kept beside it under its own name.
  Opus at medium is also compared with Opus at the higher setting, field by field,
  to show how stable its judgments are.
- **How it is read.**
  - If the rerun clears the bar, that is a reason to test the rules again on a
    fresh draw, with both settings fixed in advance. It does not make version 1.1
    passed: the setting was changed after seeing the result, on the same rows.
  - If it does not clear the bar, version 2 of judgment 1 goes ahead as
    `LINK_TEST_RESULT.md` describes.
  - Either way, coder 2 should use the rerun's setting on the real papers, so
    that the test speaks for the setup actually used.

## The rules in brief (`LINK_RULES_v1_1.md`)

For each claim, the coder records two things:
- its **condition**, pinned to the printed asserted direction ("when X fails" →
  "X failing");
- its **form**: produces, requires, maps, none or describes.

For each pair, the coder makes three judgments:
1. **what the stub shows**, from the stub alone and before the coder has the
   paper: whether the condition is present, absent or not shown; whether the
   outcome goes as asserted, the other way or isn't shown; any other cause;
   whether the claim is bounded. One fact counts in one role only, and a
   practice's success is never read off its result.
2. **what kind of passage** it is, a report or the author's reading, from the
   paper.
3. **how the paper uses it** for the claim, for every passage whatever its kind:
   evidence, qualification, restatement or none. A broad claim gets a passage
   only if the paper ties it there in words.

The code is derived from judgment 1 by a fixed table for the claim's form. Coders
never see the table. `produces` is read as a tendency and `requires` as
necessity.

Every result is computed under four readings: v1.1; strict, where an outcome
alone is not `with`; covariation, where a negative case is `with`; and v2 read
literally. Each is scored as a five-value code and as a three-value code (`with`,
`against`, neither).

## The sample: 60 pairs over 33 claims

| stratum | rows | how chosen |
|---|---|---|
| hard | 18 | fixed before any draw: the cases the reviews and the audit argued |
| random linked | 21 | seeded draw from the extractor's other 406 links |
| random near-unlinked | 15 | seeded draw from 496 unlinked pairs where one of the fragment's own printed labels names one of the claim's constructs or its outcome |
| random far-unlinked | 6 | seeded draw from the other 5,372 unlinked pairs |

Rows are shuffled and numbered R01 to R60. Fragments carry shuffled labels K01 to
Knn, so the tables show neither the real ids nor clusters.

| hard case | why it is here |
|---|---|
| F93→C20, F93→C23 | coded `against`: the outcome goes the other way and the stub never shows the condition |
| F97→C21 | a negative case, coded `with` |
| F98→C21 | coded `against`, though the stub does not report the outcome |
| F99→C20, F99→C23 | the author's reading of a negative case, coded `with` |
| F20→C08 | C08's only link is its own source sentence; C08 is a claim of no relation |
| F88→C27, F109→C29 | figures that present the model, coded `with` |
| F24→C09, F25→C09, F29→C13 | stubs that dropped the paper's printed numbers |
| F10→C20 and F12→C20 | similar stubs; the first is linked, the second is not |
| F83→C20 | carries the paper's label for C20's outcome, but is not linked |
| F72→C20 and F73→C20 | the same construct, coded `illustrates` in one and `with` in the other |
| F96→C28 | a pattern reported across cases: the case the voice test cannot place |

**The page re-check, 15 rows, new rules only.** The coder makes judgment 1 again
from the passage itself instead of the stub. The list is sent only after reply 5:
- the six fixed rows: F24→C09, F25→C09, F29→C13, F93→C20, F97→C21, F98→C21;
- nine random rows on reported fragments: five linked and four unlinked.

**The PI's sheet, 20 rows over 18 claims:** 4 hard and 16 random; 16 of the 20 rows
are reports.

## The PI's part

1. **Read the rules** and set the pass bar, recorded with `link_test.py bar`,
   which refuses once any answer has been read.
2. **Fill the sheet** (`link_test_human_sheet.xlsx`) before opening any chat:
   the claims, then the stub columns, then the page columns.
3. **Run the four chats** as `LINK_TEST_SEND.md` describes:
   - The two v2 chats get the instructions and the table only.
   - The two new-rules chats get the same, then the PDF after reply 3, then the
     re-check list after reply 5.
   - Save each chat's replies, in order, in one text file.
4. **Bring back the four files and the sheet.** They are read in, which checks
   every row and code, and then scored. The result is in `LINK_TEST_RESULT.md`.

The PI's time: about two to three hours with the chats, mostly typing
`continue`, and one to two hours for the sheet.

## The pass bar: as recommended, set on 30 Sep unchanged

Recorded in `link_test_bar.json`, which holds the bar's wording as
the report will print it. `bar` writes the file once and refuses after any answer
is read.

Read on the 42 random rows, between the two new-rules models. Pass only if all of
these hold:
- **Author link and evidence link:** κ of at least 0.60.
- **Three-value code:** κ of at least 0.60, under both v1.1 and strict. This way
  the result does not hang on the open question of whether an outcome alone is
  `with`.
- **Claim form:** κ of at least 0.60. A form disagreement changes every derived
  code on that claim, so this is a prerequisite.
- **Against v2:** the new rules no worse than v2 by more than 0.10 in κ, for the
  link and the three-value code. This is judged by the lower end of a paired
  bootstrap 95% interval. Both arms now judge the stubs without the paper, so the
  comparison is fair.
- **Hard rows:** the two models agree on the five-value code for more of the 18
  hard rows than two coders answering at random would 95% of the time. The
  report prints that baseline.
- **Twins:** neither model gives `with` to one hard row and `against` to its twin.

Any κ that cannot be computed counts as not passed. The PI's sheet is a sense
check, not gated.

On 42 rows a κ is uncertain by about ±0.25, so the bar screens the rules; it does
not measure them. The random rows hold no extractor `against`: the extractor
coded only three `against` in the whole paper, and all three are hard cases. So
the three-value κ on random rows mostly measures `with` against neither, and the
`against` question rests on the hard rows.

## What the report shows

- agreement for every field, as κ, AC1 and raw agreement, split into random and
  hard rows and into linked and unlinked rows;
- direction where both coders see a link;
- the claim forms side by side, and the code on claims whose form both coders
  agree on;
- the new rules against v2, by paired bootstrap;
- each model's v2 codes against its own stub observations read by v2's box;
- agreement with the extractor's own codes, for information;
- the page re-check row by row, and how often the paper changes the code;
- the PI's sheet against each model;
- the hard cases row by row, against a random-answer baseline;
- the pass bar, once recorded.

## What it cannot show

- Which kind of link, the author's or the evidence, should feed the scored
  measure. The test shows only whether each can be coded reliably.
- Anything about a paper other than Pratt.
- A cold result. The rules were written after reading the reviews of Pratt's run.
- A fair test on the hard cases. The reviews argued them; they are there to show
  what each rule does with them.
- Whether constructs such as "encapsulated sensemaking" can be matched to stubs
  without printed definitions. Coders meet them only through the claim
  statements. A glossary was not added, because writing one would put an
  interpretation of the paper into the test. Markers, deferred, are the proper
  fix.

## Confounds to report with the result

- The v2 arm keeps v2's base-rate lines and the stubs' voice markers; the new arm
  has neither.
- The claims were written by ChatGPT 5.6, which is also one of the two coders.
- Each model codes each arm once. A retest of the 18 hard rows, once per model,
  would measure stability; it is an option, not part of the plan.
- The new-rules chats see the paper for judgments 2 and 3. The v2 chats never see
  it; the v2 extraction itself did.
- *Added 30 Sep:* Opus 5.5 ran at medium effort in both its chats; maximum had
  been recommended. ChatGPT 5.6's setting was not recorded.

## After the test

- **If the bar holds,** choose the route: a separate linking stage on the frozen
  records, or brief v3 and re-extraction. The page re-check informs the choice:
  it shows how often the paper changes a code the stub gave.
- **If it fails,** the report shows which judgment failed. That rule is revised as
  version 2 and tested on a fresh draw. It is never patched and scored again on
  the same rows.
- **Either way,** the result goes into the proposal as a finding about the
  instrument.

## Files

| file | what | who receives it |
|---|---|---|
| `LINK_RULES_v1_1.md` | the rules in full; Part B derives the codes | nobody |
| `LINK_TEST_NEW.md` | coder file, new rules: Part A word for word, and the reply format | chats 3 and 4 |
| `LINK_TEST_V2.md` | coder file, v2 rules quoted word for word, and the reply format | chats 1 and 2 |
| `link_test_table_new.md`, `link_test_table_v2.md` | the 33 claims and 60 pairs | the matching chats |
| `link_test_human_sheet.xlsx` | the PI's 20 rows, blank | the PI |
| `link_test_human_sheet_filled.xlsx` | the PI's sheet as filled, 30 Sep, before any chat | nobody |
| `link_test_bar.json` | the pass bar as set, recorded before any answer was read | nobody |
| `reply_chatgpt_v2.rtf`, `reply_chatgpt_new.rtf`, and the `.txt` made from each | ChatGPT's replies as saved, and the text that was read | nobody |
| `reply_rtf_to_txt.py` | turns a reply saved as RTF into the text `read` takes | nobody |
| `reply_opus_v2_as_saved.txt`, `reply_opus_v2.txt`, `reply_opus_new.txt` | Opus's replies: the v2 file as saved, the same with its dashes restored, and the new-rules file | nobody |
| `link_test_report.md`, `link_test_results.json` | the scored output, and the numbers behind it | nobody |
| `LINK_TEST_RESULT.md` | the verdict, which judgment failed and why, what the protocol says next, and the Opus rerun | nobody |
| `reply_opus_v2_B.rtf`, `reply_opus_new_B.rtf`, and the `.txt` made from each | the Opus rerun at extra effort, as saved, and the text that was read | nobody |
| `link_test_report_B.md`, `link_test_results_B.json` | the rerun scored against ChatGPT, and the numbers behind it | nobody |
| `link_test_compare_runs.py` | compares two runs of one coder, field by field | nobody |
| `LINK_TEST_SEND.md` | what to attach and paste, chat by chat, with the re-check list | the PI |
| `LINK_TEST_REVIEW_LOG.md` | both reviews of the rules, and the 30 Sep check of the result note, word for word, with what was done about each finding | nobody |
| `link_test.py` | compose, freeze, build, bar, read and score, with `--selftest` | nobody |
| `link_test_freeze.json`, `link_test_key.json` | the freeze with its seed, and the key | nobody |
| `LINK_RULES_v1.md`, `link_test_freeze_v1.json`, `link_test_key_v1.json` | version 1 and its unused sample, kept as history | nobody |
