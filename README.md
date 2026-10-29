# Re-reading published qualitative papers with language models: the pilot's repository

This repository holds the pilot of a protocol that indexes a published qualitative paper (the evidence it prints,
the claims it makes and how the two connect), audits the index, and has language models propose alternative readings
of the paper's evidence, which are then attacked, marked and judged. The pilot ran on two papers:

- Pratt, M. G. 2000. The good, the bad, and the ambivalent: Managing identification among Amway distributors.
  *Administrative Science Quarterly*, 45(3): 456–493.
- Bechky, B. A. 2020. Evaluative spillovers from technological change: The effects of "DNA envy" on occupational
  practices in forensic science. *Administrative Science Quarterly*, 65(3): 606–643.

The protocol was first tried on another paper (Carlile 2002), whose files are not here. Pratt and Bechky are the
first two of four "cold" papers, run under the protocol as it stood after that trial; the other two have not been
run and are not named here.

Here are what each model chat was given and how it was run, the models' replies, the two papers' indexes, the PI's
judgments, the keys, the code and the results, from which the scripts make the reported numbers again; the replay
(below) says what it covers and what it does not. The proposal and its appendix describe the protocol; the PI is the
principal investigator. Each chat has a number; `chats_models_hours.json` gives the model, settings and times of the
chats to 20 Oct (chat 82). `FILES.md` lists every file, under the test it belongs to, and `NUMBERS.md` every number
of the proposal and its appendix, with the file and the script it comes from.

## What a scholar is handed

The protocol's output for a paper is its entry (step 10 in the appendix). For Bechky (2020) the pilot built an
example:

- `REPOSITORY_ENTRY_EXAMPLE_bechky.md` gives the head of the entry: the five distinct points of highest reach, each
  shown by its reading of highest reach, and the claims the readings engage most often; then the titles of all 28
  readings.
- `CLAIM_NETWORK_bechky.html` shows every reading. GitHub shows an HTML file as code, not as a page, and the entry's
  links lead to that code: download the file and open it in a browser. It is one page, with no script, and loads
  nothing from outside. Click a claim to see the readings that engage it, and a reading's title to read it: first the
  part the coders read and coded, then, folded, the rest as its model wrote it, never coded.

In both, as in every file here, each run of six or more of the paper's words is replaced by a note. One reading as the
network shows it: R17, the reading the appendix works through (E.11).

<details>
<summary><b>R17</b> · Impending court dates predict all outcomes and are confounded with occupational values</summary>

Reach 0.38 · Fable 5.1, chat 27, the plain prompt, with the paper

**Who wrote it, who coded it.** A language model, Fable 5.1, wrote this reading in chat 27, asked for alternative
readings of the paper. The two coders are models too, Gemini 4 Argon and GPT 6 Astra, each working in a chat of its
own and not told who wrote the reading: they read the part of it shown first below and recorded which of the paper's
claims it engages, and how. The claims it engages and its reach come from their codes.

**Engages:** C05 (both coders); C16 (both coders).

**Through ties:** C03 (support partly in question, both coders); C04 (support partly in question, both coders); C13
(support partly in question, both coders); C20 (support partly in question, both coders); C21 (support partly in
question, both coders).

**The reading, as the coders read it.** One condition accounts for all three outcomes: whether an analyst in this lab
expected to be personally challenged in the local court. Toxicology had such a date and changed. Firearms and
narcotics did not and stayed as they were. Occupational values then add nothing to the explanation. They describe how
each unit talked about a decision that local exposure had already made. Because the study has one lab, each occupation
appears under only one exposure condition, so the paper cannot tell values from exposure. A named local case with an
out-of-state expert was about to challenge toxicology results (p. 625). This is the only unit with a local court date.
Firearms [6 words of Bechky (2020), p. 624] the county's jurisdiction, and the examiners did not change in response to
pressure from elsewhere (p. 624). The paper notes that [6 words of Bechky (2020), p. 635] been through admissibility
hearings seemed motivated to change practice (p. 635). These are members of the same occupation, with different
exposure and a different stance. An examiner from outside who had faced such questioning urges colleagues to treat the
critics as a spur to do better (pp. 623–624). This again links exposure to willingness. A narcotics analyst attended a
workshop on an admissibility hearing that challenged crystal testing (p. 632). Narcotics, like firearms, had a court
challenge somewhere else and none at home. The paper's own summary says narcotics had
[6 words of Bechky (2020), p. 632] change and therefore kept its practices (p. 632). Fieldwork was three to six months
per unit within eighteen months that began the month the report came out, so units were also seen at different
distances from the report's release (p. 614).

<details>
<summary>The rest of the reading, as its model wrote it (not coded)</summary>

*What it would take to cohere.* The same occupation observed under the other exposure condition: firearms or narcotics
analysts in this lab facing a scheduled local admissibility challenge, or the local practices of the outside examiners
who had already faced one. The paper says in a footnote that it has no data on what those outside examiners did in
their own labs. It also does not print the order in which the units were observed.

*In the paper:* no; pages it gives: p. 635

*Strains against it.*

- p. 623: Some examiners at the statewide meeting who had been in admissibility fights responded by attacking the
  critics. Exposure did not uniformly produce willingness to change.
- p. 627: Toxicology's change was both locally forced and consistent with its values and existing plans, so this case
  cannot show that exposure alone was sufficient.
- p. 637: The paper uses narcotics to argue that a group with a compatible technique still refused on grounds of
  values. That argument gives values independent weight.
- pp. 633, 635: The table and discussion record narcotics as having no court pathway at all, which conflicts with the
  workshop report on p. 632. The reading depends on the p. 632 version.

*Who could complete it.* Firearms or drug analysts in a jurisdiction where an admissibility hearing was actually held,
observed at the bench before and after, or a comparative fieldworker with access to two labs that differ in local
court challenges.

</details>
</details>

This is the pilot's prototype, not the protocol's final form. The pilot's readings answer simpler prompts than the
protocol proposes: the four-part puzzle of step 6 is not yet tried. And the pilot hands a scholar readings, the coded
part first; the plan (the appendix, F.3) tests another presentation: the puzzle first, with the readings folded behind
it.

## Replaying the results

```
python3 -m pip install -r requirements.txt
python3 -B replay.py
```

`replay.py` copies this folder into a temporary folder and runs 71 steps there: each runs one of the scripts with
the arguments and seed it was run with and sets every file it makes beside the file here, byte for byte, or runs a
script's own check. Nothing here is written. It takes under a minute and ends with
`71 of 71 steps pass; 169 files made again and the same`. Two kinds of "the same" are not byte for byte, and the
replay names them: nine workbooks (the eight `returned_*_coder2.xlsx` and `stage2/worth/worth_sheet.xlsx`) differ
only in the time they were saved; and five results files (`MATCHING_RESULTS.md`, `SECOND_EXTRACTION_RESULTS.md`,
`CITATION_ONLY_RESULTS.md`, `RELATION_RESULTS.md`, `COMPLETENESS_RESULTS.md`) are checked as far as the scorer
wrote them, since notes were added below a rule (`---`) afterwards, as each says. `python3 -B replay.py --list`
names the steps and what is not replayed, with the reason; `--only=NAME` runs one step, `--keep=DIR` keeps the work.
To run a script by hand, run it on a copy, as the replay does: `record_attack.py`, for one, writes over the card it
is given.

Three things to know:

1. **What it needs.** Python 3.12 or later and one package, openpyxl, which writes its workbooks through lxml
   (`requirements.txt` pins the versions it was run with). 29 of the 48 scripts need openpyxl: 19 read or write
   workbooks, and 10 import a script that does. Without lxml, openpyxl writes the same cells with other spacing in
   the XML, so the workbooks it makes are not the bytes here; and Python before 3.12 sums floats less exactly, so a
   figure kept to full precision can differ in its last digits. The replay says at the start what it runs with.
   It has been run with Python 3.13.
2. **An exact replay from saved records, not a fresh extraction.** No model is called and nothing is fetched. The
   replay starts from the records: the models' replies as they were saved, the PI's filled sheets, the indexes and
   the keys. It shows that the scripts make the results here from those records; it does not show that a new
   extraction or a new chat would give the same records.
3. **Paraphrased records, not metadata only.** The indexes, and the replies the scripts read, are here in the
   models' own words (what is not here is listed at the end), but no paper's text is: every run of six or more of a
   paper's words is replaced by a note (below).

What the replay does not make again: the notes added below the scorers' output in those five files; and a few
files that a script not kept here made: `stage2/attack_results.md` (its figures are worked out again by
`build_figures.py`), the two calibration copies of card 31, `map_settle_revisions.json`, `MAP_TASK_v2_1.md`,
`MAP_FEEDBACK_CHECK.md`'s counts, and `REPOSITORY_ENTRY_EXAMPLE_bechky.md` with `reach_bars/`. Where a file says its
figures were also checked independently, with separate code, when it was written, that code is not here: the replay
is the check here.

## What is here

- **What each chat was given, and how it was run.** The briefs, prompts and tasks: `EXTRACTION_BRIEF.md`,
  `CODING_INSTRUCTIONS.md`, `STAGE2_PROMPT.md`, `attack.md`, `MARKING.md`, `JUDGING.md`, `READING_PROMPT.md`,
  `ALTERNATIVE_READINGS.md` and the other task files; the steps each chat was run by, in the files ending in
  `_SEND.md` and in `packs/`; `SECOND_CODER.md`, how the second coding was run. The steps files speak to the PI, who
  ran the chats, and name the working folders `chats/` and `replies/`: here, what a chat was given stands at the top
  level, in `stage2/` or in `packs/`, and each reply at the top level or in `stage2/`.
- **The plans,** fixed before the replies they judge (`*_PLAN.md`). Where a plan was changed after it was fixed,
  the change is set out at its foot, with its reason.
- **The indexes.** For each paper, `<paper>_corpus.json` (the extraction's first return), `_coverage_corpus.json`
  (after the coverage check) and `_v1.json` (frozen), with their voice glosses, extraction logs, readings and
  periods, and Bechky's pairs; Bechky's second extraction is `bechky_2020_x2_*`. `schema.py` defines the record.
- **The models' replies:** `reply_*` here and in `stage2/`, and `returned_*_coder2.xlsx`, the second coder's codes
  read into the workbooks that were sent.
- **The PI's sheets and judgments:** the sheets made for the PI and the PI's filled copies (`*_filled.xlsx`), and the
  PI's lists from the coverage check (`*_coverage_list.txt`).
- **The keys,** which say which reading or row is which: `*key*.json`.
- **The results:** the agreement logs, the `*_RESULTS.md` files and the results data. `FIGURES_*.md` and
  `figures.json` (T27) give every figure for the proposal with its source, each worked out again from its record by
  `build_figures.py`.
- **The code:** 48 scripts, `replay.py` among them.
- **Examples of what the protocol produces:** `REPOSITORY_ENTRY_EXAMPLE_bechky.md`, with the claims network
  `CLAIM_NETWORK_bechky.html` and the bars in `reach_bars/`; `MAP_ACCOUNT_SHORT_EXAMPLE_v2.md`.
- **Revised after the pilot, not yet tried:** `MAP_TASK_v2_1.md`, with its changes and its check.
- **The feedback on the map task's instructions** (`Feedback_map_task_instructions.txt`): the prompt and two models'
  answers, each in a chat of its own, given `MAP_TASK.md`, Bechky's map sheet and the paper, and asked where the
  instructions might make two coders diverge, without seeing any map; `MAP_FEEDBACK_CHECK.md` sets it beside the map
  test.
- **The negative record:** the two link tests, which did not pass, by their rules, plans, reports and results
  (`LINK_RULES_*`, `LINK_TEST*_PLAN.md`, `LINK_TEST*_RESULT.md`, `link_test*_report.md`, `link_test*_results.json`).

The record of each paper: the extraction (`EXTRACTION_BRIEF.md`), the PI's coverage check and the coverage chat, the
freeze, a second coding by another model (`SECOND_CODER.md`, `packs/`), the agreement between the two codings
(`PRATT_AGREEMENT_LOG.md`, `BECHKY_AGREEMENT_LOG.md`, and Pratt's second count), the check of the links coded
`against` (`AGAINST_CHECK.md`) and the audit (`audit.py`, `*_audit*.json`). The tests:

| test | what it asks or does | plan or steps | results |
|---|---|---|---|
| T29, the wager test | readings written from the paper's record, beside readings written with the paper in hand: attacked, marked sentence by sentence against the paper, and rated for worth | `GENERATION_SEND.md`, `BASELINE_SEND.md`, `ATTACK_SEND.md`, `MARKER_SEND.md` | `stage2/attack_results.md`, `stage2/marker_results/RESULTS.md`, `stage2/worth/WORTH_RESULTS.md` |
| T31, the judges | could a careful reader of the paper hold each coder's statements about it? | `JUDGING.md`, `JUDGE_SEND.md` | `JUDGE_RESULTS.md` |
| T32, readings at places | readings that start from given places, and from places a model finds open, in the paper (Bechky); the four given places were chosen from the index, not drawn (`PLACES.md`) | `PLACES_SEND.md`, `MARKERS_PLACES_SEND.md` | `PLACES_RESULTS.md`, `PLACES_MARKER_RESULTS.md` |
| T33, matching | does a fixed reference make the grouping of readings repeatable? (Bechky) | `MATCHING_TEST_PLAN.md` | `MATCHING_RESULTS.md`, `MATCHING_WORTH.md` |
| T34, the authors' worth | how each paper's author rates the readings of that paper (no reply came in) | `AUTHOR_RATINGS_PLAN.md` | — |
| T35, the second extraction | does an extraction repeat? (Bechky) | `SECOND_EXTRACTION_PLAN.md` | `SECOND_EXTRACTION_RESULTS.md` |
| T36, citation only | which alternatives do models offer without the paper? | `CITATION_ONLY_PLAN.md` | `CITATION_ONLY_RESULTS.md` |
| T37, the relation test | how far does each reading depart from the paper's logic, as models code it? | `RELATION_TEST_PLAN.md` | `RELATION_RESULTS.md` |
| T38, completeness | can a model take the reader's place in the coverage check? | `COMPLETENESS_TEST_PLAN.md` | `COMPLETENESS_RESULTS.md` |
| T39, the map test | does placing a reading on a map of the paper's argument tell more than T37's codes? | `MAP_TEST_PLAN.md` | `MAP_RESULTS.md`, `RANKING_CHECK.md` |

## How the files were prepared for publication

- **Anonymity.** The PI's name, place, links and paths are out of every file, the workbooks' properties included;
  the PI is "the PI"; times are given as UTC+3, but for the time stamps scripts wrote with their offset (`+00:00`,
  as in the link tests' reports and the pack keys) and the times the workbooks keep of their saving, in UTC. The
  PI's filled workbooks otherwise keep the properties Excel writes. The names of the two cold papers that were not
  run are taken out. Two people who took part are not named: a colleague who reviewed version 2 of the linking rules,
  and the person who coded Carlile as its second coder.
- **The papers' text.** In every file, a run of six or more consecutive words of a paper is replaced by a note such
  as `[12 words of Pratt (2000), p. 470]`, which gives the number of words and the pages. Words are counted as
  `check_quotations.py` counts them (letters and digits; a hyphen or a slash makes two words). A note never takes in
  the end of a sentence or a paragraph, a table cell's border or the end of a string or a cell; where a run goes on
  across a quotation mark, each part of it gets its own note, so that the mark stays where it stands. One phrase of
  five words, which a table sets beside the paper's own two-word name for an outcome, is noted wherever it stands.
  No run of six or more words of a paper is left but within a paper's own title. 1,115 runs in 115 files are
  replaced.
- **Process notes.** Who wrote a file and at whose word, why a script was revised, and the working records a file
  came from are cut. Kept: the design; the dates that show what came before what (a steps file, for one, says it was
  written after its plan was fixed); each change made after a plan was fixed, with the reviews and checks a plan
  sets as its own steps; who may receive a file ("for nobody", "it goes into no chat"), which is the blinding; the
  limits; and the figures. The steps files and the sheets stand as they were used, the sheets' line asking for the
  answers "in our conversation" included, and two replies open with the PI's covering lines, as sent
  (`against_check_reply.txt`, `pratt_2000_coverage_reply.txt`).
- **Recorded hashes.** Many files record the sha256 of the files they were made from or read, and the scripts check
  them. Where the preparation changed a file, every record of its sha256 here gives the file as it stands here, so
  the scripts run on these files as they ran on the originals. `FILE_HASHES.csv` gives each file's sha256 here and,
  where it differs, its sha256 at the time, with how the file differs. A plan whose process notes were cut has here
  a sha256 other than the one it was fixed by; that one is in `FILE_HASHES.csv`. Two records stay as they were,
  since what they hash is not here: `RELATION_TEST_PLAN.md` gives the sha256 of its own first 12,100 bytes as it
  was fixed, and `quotation_check_bechky.json` that of the third version of the claims network page, which it
  checked and whose findings `build_claim_network.py` shows on the page here. The intake record of each of the
  second coder's workbooks holds a digest of its coding tabs; where a note replaced a paper's words in a cell, the
  digest is that of the cells as they stand.
- **Made again.** Seven files that a script makes are the script's output from the prepared records, in place of
  the prepared originals: they differ from those only in the wrapping of lines, in the height a sheet gives a row
  from the length of its text, and in the sha256s they record. No number in them differs. `FILE_HASHES.csv` names
  them.
- **Edited.** The self-tests of `agreement.py`, `build_cold_pack.py`, `intake_coder2.py` and
  `build_against_check.py` ran on the files of the paper the protocol was first tried on (Carlile 2002), which are
  not here; each is replaced by a stub that says so. `check_must_agree.py` keeps no hash of the word it guards and
  no check against `CLAIM_EXTRACTION.md`, which is not here, so those two tests are left out. When
  `read_judge_answers.py` measures the longest span a reason quotes, it counts a note as the words it stands for, so
  `JUDGE_RESULTS.md` comes out as it did. `quotation_check_bechky.json` gives one run of the paper's words with the
  end of the sentence it crosses in the page it checks, so that it is cleaned as the page is.

## What is not here

- **The two papers.** `check_quotations.py` and `wording_check.py` need their text, so they are not replayed here;
  with the papers' PDFs, and pdftotext and pdfinfo (poppler), they run as their usage says.
- **`CLAIM_EXTRACTION.md`,** which maps the fields a coder codes to the moves of the audit that they trigger. It must
  never reach a coder, and a public file can. The code that applies it (`audit.py`) is here.
- **The first paper the protocol was tried on** (Carlile 2002), and its files, its logs among them. The names of two
  of its informants stand in two scripts' lists of words that no chat may be given (`check_must_agree.py`,
  `build_cold_pack.py`).
- **The files sent to the papers' authors for T34,** and `build_author_readings.py`, which wrote them. No reply came
  in.
- **The two link tests' working files** and the scripts that ran them: the tests are reported from their rules,
  plans, reports and results. The colleague's review of version 2 of the rules is not here either.
- **Replies in parts, and first versions.** The replies of chats 77 and 78 came in parts, and chats 81 and 82
  completed them; the replies as joined, which the scripts read, are here (`reply_77_*`, `reply_78_*`), not the parts
  or the script that joined them. The relation test's two planted readings (chats 62 and 63) are here as shortened
  for the test, not in their first, longer versions.
- **Superseded versions:** `MAP_TASK_v2.md` and its check, from which `MAP_TASK_v2_1.md` was made (its changes are
  listed in `MAP_TASK_v2_1_CHANGES.md`); and files that some scripts still name but that are not what ran:
  `SCHEMA_v5.md`, a specification never put to use, and `SCORING_SHEET.md` and `PROPOSAL_sep_2.md`, superseded.
- **Working material on which no reported result rests:** the extraction chats' snapshots, pass by pass
  (`*_passes.zip`); a first attempt at Pratt's extraction, which gave no return; the extractors' answers after their
  runs; notes written for the PI (`FRAGMENT_LESSONS.md` among them); and a picture of a chat's screen. The hours log
  that the steps files mention is not here; `chats_models_hours.json` gives each chat's model, settings and times as
  the working records have them.
