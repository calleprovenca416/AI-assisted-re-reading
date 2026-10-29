# The completeness test (T38): can a model take the reader's place in step 3?

Fixed on 17 Oct 2026, before any chat of the test (chats 68 to 72). It pilots a
step that the protocol gives to a person: in step 3, "A researcher reads the
paper against the index, page by page, and lists what it missed". Nothing in it
was changed after.

## What it asks

1. **Q1.** Given what the PI had for the PI's coverage check (the paper, the reading
   sheet of the first return and the extraction brief), does a frontier model of
   a vendor other than the extractor's list the passages the PI listed?
2. **Q2.** What else does it list, and how much of that is a miss under the
   brief, as a second model, of a third vendor, judges?
3. **Q3, the ready test.** Does the second extraction of Bechky (T35) hold the
   passages of the PI's Bechky list?
4. **Described:** the judge's verdicts on the PI's passages beside the coverage
   chats' decisions on them, the one check on the judge; the judge's verdicts
   on the two lists side by side; the kinds of passage each list names; the
   chats' times beside the PI's.

Described, not tested: no figure decides anything, and there is no bar.

## The material

- **The PI's lists:** `bechky_2020_coverage_list.txt` (7 Oct: 16 lines, of which
  lines 15 and 16 are the same, a duplicate, so 15 passages) and
  `pratt_2000_coverage_list.txt` (9 Oct: 14 passages). Each line names a page
  and a place on it, with no reason. The PI wrote them reading the paper with the
  reading sheet beside it, end to end and alone, in about 3.5 hours a paper;
  for Bechky, the PI also read the extraction brief, on what counts as a claim.
- **The coverage chats' decisions:** for each of the PI's passages, whether the
  coverage chat added a record from it, a fragment or a claim, as the section
  "Coverage additions" of its log answers each line
  (`bechky_2020_coverage_extraction_log.md`,
  `pratt_2000_coverage_extraction_log.md`). Bechky: 4 of the PI's 15 (F169 to
  F172). Pratt: 10 of the PI's 14 (F122 to F125 and C53 to C60). Taken into the
  key by hand, with the log's line for each, and checked independently against
  the two logs and the two lists before any chat.
- **The reading sheets:** `bechky_2020_coverage_reading.md` and
  `pratt_2000_coverage_reading.md`, which `coverage_sheet.py` made from the first
  returns and the PI read beside the paper; made again on 17 Oct, byte for
  byte the same. The chats get a copy, `CHECK_SHEET_bechky.md` and
  `CHECK_SHEET_pratt.md`, in which the sheet's first italic line, on who may
  receive it, is replaced by one that says the copy is for checking the index
  against the paper; nothing else changes.
- **The brief:** `EXTRACTION_BRIEF.md`, version 2, as frozen on 27 Sep (its
  sha256 opens 72a98c29), the brief of both extractions and both coverage chats.
- **The second extraction:** list Q of `TWO_LISTS_bechky.md` (T35; its sha256
  opens 8ffba0dd), the new return of chat 55, with 39 claims (QC01 to QC39) and
  168 passages (QP001 to QP168), as T35's matchers had it.

## The chats

| chat | paper | role | model |
|---|---|---|---|
| 68 | Bechky | checker | Opus 5.5 at Extra |
| 69 | Pratt | checker | Opus 5.5 at Extra |
| 70 | Bechky | matcher, the ready test | Opus 5.5 at Extra |
| 71 | Bechky | judge | Gemini 4 Argon at Thinking Level High |
| 72 | Pratt | judge | Gemini 4 Argon at Thinking Level High |

- **Opus 5.5:** a fresh incognito claude.ai chat, outside any project; web
  search, research and every connector off; file creation on, with its network
  access off; no profile preferences or style active (the settings of T35's
  chat 56). Anthropic's model: not of the extractor's vendor (OpenAI).
- **Gemini 4 Argon:** a fresh temporary chat; outside any Gem; personal context
  and saved info off; no apps or extensions; no Deep Research and no Canvas (the
  settings of chats 64 and 66). Google's: neither the extractor's vendor nor the
  checker's.
- **Round 1:** chats 68, 69 and 70, side by side. **Round 2:** chats 71 and 72,
  once the replies of 68 and 69 are checked and the judges' lists are built from
  them.
- **What each gets, and nothing else:** the paper's PDF, the PI's own copy, as
  the earlier chats had it; and
  - chats 68 and 69: `COMPLETENESS_CHECK.md`, the paper's `CHECK_SHEET` and
    `EXTRACTION_BRIEF.md`;
  - chat 70: `MATCH_PASSAGES_TO_Q.md` and `PASSAGES_AND_Q_bechky.md`, which
    holds the PI's 15 Bechky passages (L01 to L15, the PI's lines as the PI wrote them, the
    duplicate once) and list Q copied byte for byte from `TWO_LISTS_bechky.md`;
  - chats 71 and 72: `JUDGE_MISSES.md`, the paper's `CHECK_SHEET`,
    `EXTRACTION_BRIEF.md` and `TWO_PASSAGE_LISTS_bechky.md` or
    `TWO_PASSAGE_LISTS_pratt.md`, built after round 1: list A and list B, one
    the PI's and one the checker's, each line its place as written and nothing else,
    numbered A01, A02, … and B01, B02, … in its own order. Which list is A is
    drawn for each paper, Bechky first, by random.Random(20261024): the PI's list is
    A when `randrange(2)` gives 0. The draw is made, and recorded in the key,
    before any chat.
- One fixed message per chat, in the PI's steps, `COMPLETENESS_SEND.md`. One
  run each.

## The tasks

The three task files are fixed by their hashes before any chat. In short:

- **The checker** (`COMPLETENESS_CHECK.md`) does what the PI's steps of 6 Oct
  asked of the PI (`BECHKY_COVERAGE_SEND.md`, part 1), in their words where they
  serve: read the sheet's claims once, then the paper section by section with
  the sheet beside it, and list each passage of which one of these holds: it
  prints evidence (an event, a quote, an observation, an archival item, a table
  cell) and no fragment covers it; or it asserts, in the paper's own voice, how
  something works, and none of the claims covers it. A page with no fragment
  is not by itself a miss; misses hide in footnotes, table notes and figure
  captions. Each line names the page and the place in the forms the PI's steps gave
  (full paragraphs counted; a paragraph over a page break named as such; an
  abstract, footnote, table or figure by its name). For each line the checker
  also says which test it meets (evidence, assertion or both) and gives one
  sentence of reason; the PI gave no reasons, and the judge sees none.
- **The judge** (`JUDGE_MISSES.md`), in two parts. First, **pairs:** every
  pair of a line of list A and a line of list B that name the same passage of
  the paper, or passages that overlap. Then, **verdicts:** for every line of
  both lists, what the passage holds under the brief, set against the sheet:
  `evidence` (it prints evidence that the brief records as a fragment, and no
  fragment on the sheet records it), `assertion` (it asserts, in the paper's own
  voice, how something works, a claim as the brief defines one, and no claim on
  the sheet states it), `both`, `covered` (what it holds is on the sheet, with
  the fragment and claim ids), `not_in_brief` (what it holds is neither a
  fragment nor a claim under the brief, with why), or `not_found` (the line
  names no passage it can find). One sentence of reason for each. A miss is
  `evidence`, `assertion` or `both`.
- **The matcher** (`MATCH_PASSAGES_TO_Q.md`): for each of the PI's Bechky lines,
  the passages of list Q whose description records something printed in that
  passage of the paper, and the claims of list Q whose statement states what
  that passage asserts; or none; or `not_found`. One sentence of reason for
  each.

## The key

Built by script before any chat, `completeness_key.json`: the PI's lines for each
paper as the PI wrote them (Bechky's duplicate once, and recorded as such), with
the page and the place read from each; the coverage chat's decision on each,
with the records it added and the log's line; the draw of list A for each
paper; the hashes of every source. Checked independently before any chat.

## Checks on the replies

A fault makes a reply not count; a remark is reported, and the reply counts.

- **Checkers (68, 69):** one JSON object whose passages each have a place, a
  test of the three and a reason. Remarks: a place that names no page of the
  paper (Bechky pp. 606–643, Pratt pp. 456–493), which the judge's file keeps
  as written; a place of more than 20 words, which may say more than a page and
  a place; two lines with the same place.
- **Matcher (70):** one JSON object with an entry for every line L01 to L15,
  once, each found or not, with ids of list Q only, and none when not found.
- **Judges (71, 72):** one JSON object; pairs only of an A line with a B line,
  each pair once; a verdict of the six for every line of both lists, once,
  with a reason; every `covered` names at least one id. Remark: an id that is
  not a fragment or claim of the first return.
- **For all:** each reply is copied into a new, empty folder and read by script
  with `python3 -I`. Every quoted span of more than eight words is flagged
  before the reply is filed, and the span is not filed. A reply in parts is
  joined. A reply that does not count is reported as it is; a chat is run
  again only if it is decided so.

## The measures

For each paper and for both together:

- **M1 (Q1).** Of the PI's passages, how many the checker lists, by the judge's pairs
  (a passage of the PI's with at least one pair); and of those from which the
  coverage chat added a record (4 and 10), how many.
- **M2 (Q2).** The checker's lines: how many; how many paired with one of the PI's;
  the judge's verdicts on all of them and on the unpaired ones: miss, covered,
  not in the brief, not found.
- **M3 (Q3, Bechky).** Of the PI's 15 passages, how many hold a passage or a claim of
  list Q, by the matcher; how many a passage, how many a claim; and of the 4
  from which the coverage chat added a record, how many.
- **M4, described: the judge against the coverage chats.** On the PI's passages, the
  judge's verdict (miss or not; `not_found` apart) against the coverage chat's
  decision (added a record or not): the table, raw agreement and Cohen's kappa,
  per paper and together.
- **M5, described.** The judge's verdicts on the PI's lines and on the checker's,
  side by side; the checker's tests and the kinds of place in each list
  (paragraph, footnote, table, figure, abstract, caption); the pages; each
  chat's time, beside the PI's 3.5 hours a paper.

## What the figures will be read as, fixed now

- Agreement with the PI's list is agreement with one reader, who read liberally: from
  11 of the PI's 15 Bechky passages the coverage chat added nothing. The PI's list is not
  the set of true misses, and what both the PI and the checker missed stays unknown:
  the protocol's second reader, on a random sample of pages, is not run here.
- The judge's verdict is one model's reading of the brief. M4 sets it against
  another model's decisions, the coverage chat's, of the extractor's vendor,
  not against a person's.
- The checker sees the first return's sheet, as the PI did. The frozen records also
  hold what the coverage chats added; a passage both the PI and the checker list is
  one the protocol's next step has already acted on.
- The ready test asks whether a second extraction holds what the PI's reading found,
  not whether it holds what the first return missed; the second extraction ran
  on the extractor's vendor.
- One checker, one judge and one matcher, one run each; two papers.

## The order

1. This plan fixed by its hash; then `COMPLETENESS_CHECK.md`,
   `JUDGE_MISSES.md`, `MATCH_PASSAGES_TO_Q.md` and the PI's steps,
   `COMPLETENESS_SEND.md`, fixed by theirs, before any chat.
2. The builder, `build_completeness_test.py`, which makes the two sheet copies,
   the matcher's file, the key and, after round 1, the judges' lists, and checks
   every reply; and the scorer, `score_completeness_test.py`: both tested on
   made-up replies and fixed by their hashes before any reply is opened. The
   key checked independently.
3. Chats 68 to 70; their replies checked and filed.
4. The judges' lists built from the checkers' replies; chats 71 and 72; their
   replies checked and filed.
5. Scored; every figure checked independently, with separate code.

## Limits, known now

- One checker of one vendor, one run per paper: whether two checkers of
  different vendors miss the same passages is not tested.
- The judge pairs the lines and judges them in the same chat; no second judge.
- The PI's lists name passages by page and place, not by text; a place named two
  ways may be paired or not by the judge's reading.
- The ready test is Bechky's alone, and the second extraction is of the
  extractor's vendor.
- The coverage chats' decisions are a model's, under the brief; they are the
  key's second tier, not a person's verdict.

## The PI's time

Round 1, chats 68 to 70 side by side, about 20 minutes; round 2, chats 71 and
72 side by side, about 15 minutes. About 40 minutes in all, with the downloads;
no coding or judging of the PI's.
