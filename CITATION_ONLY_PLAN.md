# The citation-only run (T36): which alternatives do models offer without the paper?

Fixed on 16 Oct 2026, before any chat of the run (chats 58 to 61). Step 6 of the
protocol asks each model for alternative readings given only the paper's
citation, so that alternatives produced this way can be flagged as available
without the paper's text. Nothing in it was changed after.

## What it asks

1. **Q1.** Given only a paper's citation, do the models offer alternative
   readings that make the same points as the readings made with the paper?
2. **Q2.** On Bechky, which of the PI's groups of 14 Oct are reached without
   the paper, and how many of the five points that two or more Fable chats
   reached with the paper?
3. **Q3.** On Pratt, which of the wager test's 15 readings made with the paper
   have a counterpart made without it, and from which arm?
4. **Described:** what each model says it knows of each paper.

This is a control, described and not tested: no figure decides anything, and
there is no bar. It cannot tell a model's memory of the paper from inference
from the citation and the field.

## The four chats

| chat | paper | model and setting |
|---|---|---|
| 58 | Bechky 2020 | Fable 5.1 at max: a fresh incognito claude.ai chat, outside any project; web search, research and every connector off; file creation on, with its network access off; no profile preferences or style |
| 59 | Bechky 2020 | GPT 6 Astra at max: a fresh ChatGPT Temporary Chat; memory, custom instructions and web search off; no project |
| 60 | Pratt 2000 | Fable 5.1 at max, as chat 58 |
| 61 | Pratt 2000 | GPT 6 Astra at max, as chat 59 |

These are the two models that wrote the pilot's plain readings made with the
paper, with the same settings: Fable 5.1 in the wager test's plain chats (25
and 27), and GPT 6 Astra in T33's (49 and 50).

- **What each chat gets:** one file, `CITATION_ONLY_READINGS.md`, and one
  fixed message that gives the paper's citation as the corpus records it. No
  PDF, no other file, and nothing about the paper, the project or what is
  hoped for.
- **The prompt** is the plain prompt, `ALTERNATIVE_READINGS.md`, with the PDF
  taken out by fixed replacements: the paper is named by its citation; the
  evidence is cited by page where the model recalls it; and one field is added
  first, `what_you_know`, in which the model says what it knows of the paper
  and how sure it is. Every other line is the plain prompt's: up to five
  readings, the same five fields, no quote of more than eight words.
- **One run per model and paper.** The protocol proposes a fixed number of
  runs; one each is what this pilot can afford.
- **The PI's steps** are in `CITATION_ONLY_SEND.md`, written after this plan
  is fixed and fixed by its hash before any chat opens.

## Checks on the replies

Each reply is copied into a new, empty folder and read by script with `python3
-I`. It counts if it is one JSON object with a `what_you_know` field and from
one to five readings, each with a non-empty `wager`. Every quoted span in the
reply is counted: a reply with a quoted span of more than eight words in a row
is flagged before it is filed, and the span is not filed. A reply that does not
count is reported as it is; the chat is not run again unless it is decided so.

## The PI's matching

After all four replies count, a sheet is built for the PI by script with the
seed 20261020, by a builder fixed by its hash before any reply is opened:

- **Bechky:** each reading made without the paper (chats 58 and 59), shown by
  its `wager` field alone, shuffled with the seed, labelled X01 onward, and
  not saying which chat wrote it. Beside each, the PI's groups of 14 Oct
  (`grouping_sheet_filled.xlsx`; the ten named in `matching_results.json`),
  each with its readings, M01 to M28, as `READINGS_matching.md` gives them.
  The PI names the one group that makes the same point, or `none`, with a note
  if the PI likes.
- **Pratt:** the readings made without the paper (chats 60 and 61) in the same
  form, and the wager test's 15 readings P01 to P15 as its markers had them
  (`stage2/markers/READINGS_pratt.md`). The PI names every reading made with the
  paper that makes the same point, or `none`.
- **Not blind:** the PI runs the chats and will have seen the replies. The sheet
  does not say which chat wrote which reading.

## The measures

For each paper, from the PI's sheet and the key:

- **M1.** For each model and for both together: the readings made without the
  paper; how many the PI places with readings made with it (Bechky: in one of the PI's
  groups; Pratt: the same point as at least one of P01 to P15); how many the PI
  marks as a new point.
- **M2, Bechky.** The groups reached without the paper, by each model and by
  either; and of the five points that two or more Fable chats reached with the
  paper (`accreditation`, `capacity`, `different demands`, `firearms already
  changed` and `staff sorting`, as `matching_results.json` gives the groups
  and the chats), how many are reached without it.
- **M3, Pratt.** The readings made with the paper that have a counterpart
  without it, by arm (system, middle, plain, as `stage2/markers/KEY.json`
  gives them), by each model and by either.
- **M4.** Each model's `what_you_know`, as it wrote it, for each paper.

## What the figures will be read as, fixed now

- A point reached without the paper is **available without the paper's
  text**: to the models, it could have come from memory of the paper or of
  writing about it, or from inference from the title, the journal and the
  field. The run cannot say which.
- It does not make the readings made with the paper worthless, nor show that
  they were remembered: a model given the paper may reach the same point from
  the paper.
- Nothing here judges a reading made without the paper as faithful or worth
  pursuing: no marker checks it and no worth is rated.
- A model that says it does not know a paper and still reaches its points
  makes inference the likelier source; one that says it knows the paper well
  makes memory possible. Neither is shown.

## The order

1. This plan fixed by its hash, then `CITATION_ONLY_READINGS.md` and
   `CITATION_ONLY_SEND.md` fixed by theirs, all before any chat opens.
2. The builder of the PI's sheet and the scorer, tested on made-up replies and a
   made-up filled sheet, fixed by their hashes before any reply is opened.
3. The four chats, side by side.
4. The replies checked and filed; the PI's sheet built.
5. The PI's filled sheet checked (no cell but the ones the PI fills changed),
   filed and scored; every figure checked independently, with separate code.

## Limits, known now

- One run per model and paper, two models, two papers.
- The PI is not blind to the source of what the PI matches.
- Pratt's comparison is to single readings, Bechky's to the PI's groups, so the two
  papers' figures are not alike in kind.
- The models may know the papers unequally: Pratt 2000 is older and much
  cited.
- Web search is off by the settings and by the message; that the chats kept to
  it rests on the settings and on what the windows show.

## The PI's time

The four chats, about 15 minutes side by side; the PI's matching, about 45
minutes.
