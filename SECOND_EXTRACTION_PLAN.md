# The second extraction of Bechky (T35): does an extraction repeat?

Fixed on 15 Oct 2026, before any chat of the test (chats 55 to 57). Nothing in
it was changed after.

## What it asks

1. **Q1.** Do two extractions of one paper, under one frozen brief, find the
   same claims?
2. **Q2.** Do they find the same passages of evidence, page by page?
3. **Q3.** On the passages both find, do they code voice alike: the paper
   reporting, or the author interpreting?
4. **Described, not tested:** what one extraction finds and the other does
   not; and, on what both find, how far they agree on a claim's `stated_as` and
   `core`, and on the links between matched claims and matched passages.

These are the first figures for whether the light index the proposal leans on
(claims, passages with their pages, and voice) can be made again. Whether the
extraction repeats has not been tested until now.

## What the figure is, and is not

- **Across a change of model.** Bechky's first return (6 Oct) was made by
  ChatGPT in a Temporary Chat under "Chat", thinking High, by a model that named
  itself GPT 5.6 Sol. The same set-up has named itself GPT-6 since 8 Oct. The new
  extraction runs in the same set-up, whatever model that now is, recorded as the
  window shows it and as a model check names it. So the figures are the
  agreement of two extractions under one brief across a change of model, the
  condition any pool of records will face. They are not a test–retest of one
  model, and one new run cannot tell how much of a difference is the model and
  how much the run.
- **Against the first return, not the frozen record.** No coverage check is run
  on the new return, so it is set against Bechky's first return as it came back
  (`bechky_2020_corpus.json`: 168 fragments, 23 claims, 290 links; and
  `bechky_2020_voice_gloss.json`), not against the frozen record, which also
  holds the four fragments of the coverage chat.

## The new extraction (chat 55)

- The PI's chat, by `SECOND_EXTRACTION_SEND.md`, written after this plan is
  fixed: ChatGPT in a fresh Temporary Chat under "Chat", thinking effort High,
  not inside any project; memory, custom instructions, web search and every
  connector off. It is given `EXTRACTION_BRIEF.md` (version 2, as frozen; its
  sha256 opens 72a98c29) and the PI's PDF of Bechky, and nothing else; the opening
  message of `BECHKY_SEND.md`, word for word, with the same paper_id and
  citation; after each pass, `continue` and nothing else, with the fixed replies
  of `BECHKY_SEND.md` if the chat asks something. Just before it, a model check
  in a separate Temporary Chat, with a picture, as for Pratt's coverage chat. A
  model's own account of its name is weak evidence, so the name the window shows
  is recorded beside it.
- After every pass the PI downloads the three files and copies the pass's message,
  with its time, into one text file.
- **The return counts** if the three files of the last pass hold a corpus that
  `schema.py` validates with 0 errors, and a voice file with one voice code for
  every fragment. If a format fault stops it, the chat is asked once to fix the
  format only, as `BECHKY_SEND.md` allows. If it fails again, or the chat cannot
  finish, the test stops there and is reported; no further extraction is run in
  its place unless that is decided.
- Filed unchanged under names of their own, for nobody:
  `bechky_2020_x2_corpus.json`, `bechky_2020_x2_voice_gloss.json`,
  `bechky_2020_x2_extraction_log.md`, the files of every pass with the messages
  as `bechky_2020_x2_passes.zip`, and the model check's picture. Nothing of the
  new return goes into any chat but the matchers' (below), and nothing goes back
  into chat 55.

## The matchers (chats 56 and 57)

- Two chats of two vendors, set up as T33's coders: chat 56, Opus 5.5 at Extra
  in a fresh incognito claude.ai chat (web search, research and every connector
  off); chat 57, GPT 6 Astra at max in a fresh ChatGPT Temporary Chat (memory,
  custom instructions and web search off; no project). Each is given the PI's PDF of
  Bechky, the matchers' instructions and the matchers' file, and nothing else.
- **The matchers' file,** built by script from the two returns, holds them as
  list P and list Q; which return is P is drawn with the seed. In each list: the
  claims, with new ids, in the order of their first page, each with its
  statement and its pages; and the passages, page by page, each with a new id,
  its location and its stub, the openings that mark the author's voice cut from
  every stub by the rule of the coders' packs (`build_cold_pack.py`: "the
  author's account is that", "the paper explains that", "for the author,").
  Nothing else of either return: no outcome, direction, `core`, `stated_as`,
  voice, unit, period, speaker, label, gloss, link, pair, gap or note, and
  nothing that says which return came first or how either was made.
- **The matchers' task,** for every claim and every passage of both lists: an
  entry naming its counterparts in the other list, or none.
  - **Claims.** Two claims are counterparts when they assert the same thing
    about the paper's subject: for a claim that names an outcome and a
    direction, the same condition, the same outcome and the same direction,
    whatever their wording or breadth (the brief's own rule for what counts as
    one claim); for a claim that names none, the same assertion. Where one list
    states as one claim what the other states as two, each of the two is a
    counterpart of the one.
  - **Passages.** Two passages are counterparts when they report the same
    printed material: the same event, observation, quotation, document or table
    cell, whether one cuts it wider or narrower than the other; a passage that
    holds two of the other list's counts as the counterpart of each.
    Counterparts are looked for on the same page, and on the page before or
    after where the material runs over a page break; a table's cells (a passage
    whose location names a table) within the same table.
  - Each matcher goes to the PDF where a stub or a statement leaves it unclear,
    and judges from the paper and the two lists alone.
  - The reply is one JSON object, with an entry for every claim and every
    passage of both lists.
- The matchers' instructions and file format, the builder of the file and the
  scorer are written before the new return is opened, the builder and the
  scorer tested on made-up returns, and all of them fixed by their hashes.

## The measures

A matcher's pairs are every pair it names in either direction (an entry of list
P naming an item of list Q, or the other way round); pairs named in one
direction only are counted and reported.

- **Found again:** the share of the first return's claims with at least one
  counterpart in the new return, and the share of the new return's claims with
  one in the first; the same for passages. Each under each matcher, under both
  (an item counts only if both matchers give it a counterpart, not necessarily
  the same one) and under either. Shown apart: the first return's 7 core
  claims, its 40 table cells, and the passages by their voice in each return.
- **The matchers' agreement:** Cohen's kappa on whether each item has a
  counterpart, over every item of both lists; and the pair kappa, Cohen's kappa
  on whether each candidate pair is named, over every pair of a claim of P and a
  claim of Q, and over every pair of a passage of P and a passage of Q on the
  same page or on pages next to each other, or in the same table. Claims and
  passages apart.
- **Voice on matched passages:** over the passage pairs that both matchers
  name, the two returns' voice codes (`reported` or `author_insight`), compared
  as raw agreement and as Cohen's kappa, set beside the two codings' agreement on
  Bechky's voice (kappa 0.865, 161 of 172). A passage matched to two partners
  counts once in each pair.
- **Uncertainty:** 2,000 bootstrap resamples, seed 20261018: the items drawn
  with replacement for the kappas on items and on pairs (pairs formed among drawn
  items that are copies of different items, as in T33), and the pairs drawn with
  replacement for voice; every kappa of a resample computed on the same
  resample. The 2.5th and 97.5th percentiles give a 95% interval; a resample in
  which a kappa cannot be computed is left out, and the count of those is given.
- **Described, not tested:** the counts of claims and passages in each return,
  and how many claims each marks core; on the claim pairs both matchers name,
  whether `stated_as` and `core` agree; on each pair of matched claims and each
  pair of matched passages, whether each return links the passage to the claim,
  and with which direction; the passages per page in each return.

## What counts as an answer, fixed now

**Q1, claims.** With f the share of the first return's claims found again and s
the share of the new return's claims found in the first, read under each
matcher:

1. **The claims repeat:** f ≥ 0.80 and s ≥ 0.80.
2. **They repeat in part:** not case 1; f ≥ 0.50 and s ≥ 0.50.
3. **They do not repeat:** any other result.

The answer is the case that both matchers' figures support: where the two
matchers give different cases, the lower of the two, with each given beside. As
a second reading, the case under both and under either. **Not decided** if the
two matchers' pair kappa on claims is below 0.60, or cannot be computed: the
matching itself is then not steady enough to read, and the figures are given as
they stand. Their kappa on whether a claim has a counterpart is given beside it,
and decides nothing: where nearly every claim is found, that kappa swings on one
item.

**Q2, passages.** The same cases and rules, read on the passages outside the
tables, and again with the table cells as a second reading: the first return cut
its two tables into 40 cells, a cut the brief allows and the record's lessons
fault (`FRAGMENT_LESSONS.md`, lesson 15).

**Q3, voice.** On the passage pairs both matchers name: kappa of at least 0.80,
**as steady as two codings of one extraction** (0.865 on Bechky); from 0.60 to
under 0.80, **less steady**; under 0.60, **not steady**. **Not decided** if
there are fewer than 20 such pairs, if a kappa cannot be computed, or if Q2 is
not decided.

The bars (0.80, 0.50, 0.60, 20) are judgments fixed in advance, not standards.
T33's bar for "repeatable" was 0.80 too.

## Checks on the replies

A matcher's reply counts if it is one JSON object of the form its instructions
give, names every claim and every passage of both lists exactly once as an
entry, and names as counterparts only ids of the other list. A pair of passages
more than one page apart is recorded, counted and reported. A reply that fails
is recorded with its faults, and the chat gets the fixed answer of the PI's
steps once; if it fails again, it is reported, and the figures that need it are
given as not decided. No reply is edited.

## The order

1. This plan, fixed by its hash.
2. The steps for chat 55, `SECOND_EXTRACTION_SEND.md`; then the model check
   and chat 55. Its files are copied into a new, empty folder and not opened
   until step 3 is done.
3. The matchers' instructions, the builder of their file and the scorer,
   written, tested on made-up returns, and fixed by their hashes.
4. The new return opened, as untrusted files, and checked (`schema.py` and the
   voice file); filed; the matchers' file built with the seed.
5. Chats 56 and 57, side by side, by steps of their own.
6. The scorer run, the results written, and every figure checked independently
   against the files.

## Limits, known now

- One paper and one new run, across a change of model: the figures say how far
  two extractions agree, not why they differ.
- Against the first return, which lacks the coverage chat's four fragments;
  neither return has had a coverage check.
- The matchers are models, two of two vendors, working from statements and
  stubs with the PDF; no person checks their pairs. GPT 6 Astra comes from the
  vendor of both extractions.
- The new return may cut passages more finely or more coarsely than the first.
  The rule lets one passage pair with several, and the shares are counts of
  items, so a finer cut on one side can show as a lower share on the other.
- Statements and stubs are paraphrases: a stub that misstates its passage can
  hide a match or make a false one, and the matchers have the PDF to settle
  doubt, not to replace the stubs.
- The bars are judgments.

## The PI's time

About 5 minutes for the model check; about an hour for chat 55 (the first
extraction of Bechky ran from 20:06 to 21:03 on 6 Oct, with the files downloaded
after every pass); about half an hour for chats 56 and 57, side by side.
