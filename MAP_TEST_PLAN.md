# The map test (T39): plan

Fixed on 18 Oct 2026, before any chat of the test (chats 73 to 80). Its text was
not changed after; the changes made since are set out at its foot, dated, with
their reasons.

## What it asks

1. **The PI's question.** Does placing a reading on an argument map of its paper
   give a more objective and more informative account of how the reading
   relates to the paper's argumentative architecture than T37's relation codes
   do? The PI judges it on twelve readings, side by side (part E).
2. Do two models from different vendors, blind to the readings, build the
   same map from a paper's frozen index?
3. Where do the 47 readings of T37 land on the map, and what typed effects
   follow from T37's codes through it?
4. At what cost, in chats and in the PI's minutes?

Described, not tested: no bar. **The PI's criterion:** the map stays in the
protocol if its account of how readings relate to the paper's argumentative
architecture is, in the PI's judgment, more objective and more informative than
T37's; the measures of part F are read beside it. The PI judges it once the
results are in.

## Materials, fixed now

- The frozen indexes: `bechky_2020_v1.json` (sha256
  6f83d744cd1dd68326cce29568a4aff461580d852d1222c4f1d096cb6922ced0) and
  `pratt_2000_v1.json` (sha256
  a4810cc03d9a439220b2c8781acf494c62d5ac63f7f53f359157238739147c99), with their
  voice files. No chat gets them: the coders get a sheet made from each.
- T37: `RELATION_READINGS_bechky.md` (20cadee8…), `RELATION_READINGS_pratt.md`
  (c6de0290…), `relation_results.json` (5dff925e…) and `relation_key.json`
  (b8598261…): the 47 readings (43 real, 4 planted), both coders' codes, the
  PI's sample of twelve and the PI's worth of the 43.
- The PI's PDFs of the two papers.

## A. The map sheets and the pairs, by script, before any chat

`build_map_test.py pairs --seed=20261025` writes, from each frozen index, a
map sheet for the coders, and one key.

- **The sheet** (`MAP_SHEET_bechky.md`, `MAP_SHEET_pratt.md`): the claims in
  full (id, pages, core or not, stated as, statement, outcome, constructs, and
  the passages linked to it, by direction); the passages (id, pages, unit,
  data type, speaker where named, stub, gloss where kept); the contrast pairs,
  declared gaps and absences; which parts of the task apply, by the rule
  below; and the numbered pairs to code. No voice code, no basis of a link,
  and no text of the paper, which the index does not hold.
- **The pairs** are ordered, from a claim Ci to a claim Cj, and Cj is always a
  core claim. Candidates, by four rules applied to the index:
  1. *Level:* Ci is a unit claim (at least five linked passages, at least 80%
     of them from one unit), Cj is not, and the two share a construct, word
     for word.
  2. *Shared passages:* Ci and Cj share at least three linked passages,
     leaving out passages linked to more than six claims.
  3. *Chaining:* Ci's outcome and Cj's constructs share at least two content
     words.
  4. *Stated ties:* a passage whose stub or gloss says "combined with", "led
     to", "leads to", "builds on", "rests on", "depends on" or "drawing on"
     is linked to both.
  To the candidates is added a random sample of the other ordered pairs with
  a core target: 25 on Bechky and 30 on Pratt, drawn with
  `random.Random(20261025)`, Bechky first; then each paper's pairs are
  shuffled with the same generator and numbered P001 onward. The sheet does
  not say which pairs are candidates; the key does, with the rules behind
  each.
- **What applies:** the comparative table, when at least two unit claims of
  different units have an outcome; the contrast controls, when the index has
  contrast pairs. By this rule, on the frozen indexes: Bechky, both (unit
  claims C14, C16, C17 and C18; two contrast pairs); Pratt, the contrast
  controls only (no unit claim; three contrast pairs).
- **The key** (`map_key.json`): the seed; the sha256 of every input and of
  the builder; every pair, with its rules or "sample"; the order; what applies.

## B. Round 1: the maps (chats 73 to 76)

- **The coders:** Opus 5.5 at High, in a fresh incognito
  claude.ai chat (web search, research and every connector off; file creation
  on, with its network access off); and GPT 6 in a fresh ChatGPT Temporary
  Chat, under Chat, thinking High (web search off). Chat 73, Bechky, Opus;
  74, Bechky, GPT 6; 75, Pratt, Opus; 76, Pratt, GPT 6.
- **Each gets** `MAP_TASK.md`, its paper's map sheet and the PI's PDF of the paper,
  with a fixed message, and nothing else: none of the alternative readings,
  and no other chat's work.
- **Each returns** one JSON object: for every listed pair, whether Cj rests on
  Ci, and if so its type (evidential, mechanistic, comparative, significance),
  its strength (necessary, contributing), its basis and a page, with a
  reason of one sentence; up to ten further pairs with a core target that
  rest on another; a registry of the constructs (groups of the sheet's
  construct names that name one construct, each with a canonical name); where
  it applies, the comparative table (the paper's own explanatory factors, each
  with the claim that states it; for each unit, its outcome and each factor's
  value, + / − / ?, with ids); and, for each contrast pair, each factor held,
  varied or unclear, with ids.
- **The definitions** are Fable's ("rests on": a
  counterfactual test; the four types; the two strengths), with a boundary
  test between the types and a made-up example (`MAP_TASK.md`).
- **The checks on a reply** (`build_map_test.py check-map`), as in T37 and T38:
  one JSON object; every listed pair answered once, and no other pair among
  them; ids the index's; values from the lists; a page for each edge; no
  quoted span of more than eight words of the paper. A fault stops the reply;
  a remark is reported. A quoted span found is flagged and left out of the
  filed copy.

## C. The PI's settling, and the settled map

- **The PI's sheet,** one per paper: every item on which the two maps differ (a
  pair that one calls an edge and the other not; two types or two strengths;
  registry groups that differ; table and contrast cells that differ), each
  with both coders' answers and reasons, a yellow cell for the PI's choice (A, B,
  or the PI's own) and one for a note; timed by the PI's start and end.
- **The maps' agreement and their other measures** (F1) are taken on the maps
  as built, before the PI's settling, since the PI has read the readings.
- **The settled map:** what both coders agree on, with the PI's choices. From it,
  by script: the closure (part D); the mechanical modules: each core claim's
  evidence (its passages by voice code and data type, and by unit), timing
  (the periods and the resolution), scope (the units its passages come from,
  and the declared scope limits), constructs (each canonical construct and the
  claims that use it, by the settled registry), and the paper's own openings
  (ventured claims, declared gaps, absences, qualifying links); where the table
  applies, the factors whose values follow the outcome in every unit; and the
  network of the claims' constructs, drawn by a registered script from the
  frozen index, its merges from the settled registry, and labelled as shared
  constructs, not dependence.

## D. The closure: the typed effects, fixed now

- A reading **hits** a claim when a T37 code gives the claim one of the types
  inverts, other_mechanism, rereads_evidence or challenges_premise, as its main
  claim or another. Each coder's codes are taken on their own; every effect is
  reported with the coder or coders whose codes give it.
- A hit core claim is **contested.** Through each settled edge from a
  contested or unsupported claim Ci to a claim Cj:
  - *evidential:* Cj is **unsupported** if the edge is necessary, or if every
    evidential edge into Cj comes from a contested or unsupported claim;
    otherwise **weakened**;
  - *mechanistic:* **unsupported** if necessary, **weakened** if contributing;
  - *comparative:* **restated**;
  - *significance:* **idle**.
- Only contested and unsupported claims carry an effect onward. A claim given
  more than one label keeps the strongest, in this order: contested,
  unsupported, weakened, restated, idle.

## E. Round 2: placement, the openings' check and the PI's comparison

- **Placement (chats 77 and 78):** Gemini 4 Argon at Thinking Level High in a
  temporary chat, with the settings of chats 64 and 66, one per paper; Google's
  models wrote none of the readings. It gets the placement task, its paper's
  settled map, T37's readings file, both T37 coders' codes for each reading
  (as coder A and coder B) and the PDF. For each reading: the map elements it
  bears on, by id, each with a line on how; the passages its evidence rests
  on, by id; what it targets that the map lacks (off-map), or none; and its
  **opening:** two sentences, what the reading opens in the paper's argument
  and the next investigation that would settle it, each tied to a map element
  or marked off-map.
- **The openings' check (chats 79 and 80):** GPT 6 in ChatGPT's Chat mode at
  High, one per paper: for each reading, given with its opening, yes or no:
  does the opening say what the reading says, and nothing it does not? With a
  reason.
- **The PI's comparison:** on the twelve readings of the PI's T37 sample (Bechky R05,
  R07, R16, R22, R27, R29; Pratt R01, R02, R03, R08, R09, R14), a sheet that
  gives each reading and two accounts of it: T37's (both coders' codes and
  reasons) and the map's (the elements it bears on, with what each is; the
  typed effects; where its evidence sits; anything off-map; the opening).
  Their order is drawn for each row with `random.Random(20261026)`. Two
  questions on each reading: which account tells you more about what the
  reading does to the paper's argument, and which account could another reader
  check more readily against the paper; each answered account 1, account 2,
  the same, or neither, with a note. Timed.
- Round 2's task files, its builder and the PI's comparison sheet's builder are
  fixed by their hashes before any chat of round 2; the scorer before any reply
  of round 2 is opened.

## F. Measures, described, not tested

1. **The maps' agreement,** per paper, on the maps as built: on the listed
   pairs, whether an edge (raw agreement, kappa, positive agreement); on the
   pairs both call edges, the type and the strength (kappa, with the confusion
   table); the registries (agreement on the pairs of construct names placed
   together); the table and contrast cells (raw agreement). The further pairs
   each proposes, and those both propose. Each coder's share of edges among
   the sampled pairs beside its share among the candidates: what the four rules
   miss.
2. **Settling:** the items the PI settled, and the PI's minutes.
3. **Placement:** per reading, the elements it bears on, by kind; the readings
   with something off-map; the planted readings' placements beside the claim and
   type each was written to.
4. **Typed effects:** per reading, the labels on core claims, by coder, beside
   T37's main types and the PI's worth.
5. **Openings:** the check's yes and no.
6. **The PI's comparison:** for each question, how often the PI picked T37's account,
   the map's, the same or neither, with the PI's notes.
7. **Cost:** each chat's minutes, by the PI's report; the PI's minutes for settling and
   for the comparison.

## G. Order

1. This plan, fixed by its sha256, before any chat.
2. `build_map_test.py` and round 1's files (`MAP_TASK.md`, the two map sheets,
   `map_key.json`, `MAP_SEND.md`), fixed by their sha256s, with an
   independent check of the key and the sheets; then round 1.
3. Before any reply of round 1 is opened: the reader of the replies is the one
   fixed in 2 (`check-map`); the settling sheet's builder, the closure and the
   modules' script are fixed by their sha256s.
4. Round 2's files and builder, fixed before any chat of round 2; the scorer,
   before any reply of round 2 is opened.
5. Every figure of the results checked independently, with separate code.

## H. Limits

- Two papers; one chat per coder and paper; the PI settles knowing the readings.
- The placement uses T37's codes, at most three claims a reading.
- The map is built from the index, whose instability T35 showed; this test
  does not measure how far a map moves with it (the second extraction was
  dropped from the design).
- The PI's comparison is not blind to which account is the map's.

## I. Seeds

20261025, for the sampled pairs and the order of the pairs; 20261026, for the
order of the two accounts on the PI's comparison sheet. Neither was in use when
this plan was written.

## Changes, added after the plan was fixed

None yet.

Then, on 18 Oct 2026, before any chat of the test, before any reply was opened,
and before the closure's script was fixed:

- **Part D, its second point, is read as:** a hit claim, core or not, is
  contested and carries its effect onward; the labels are reported on core
  claims, as F4 has them. As fixed, "A hit core claim is contested" would let
  no edge whose base is not core carry an effect, though a pair's base may be
  any claim, and the adopted definitions work their first example through
  such edges (C05 on C16, C17 and C18). In T37's codes, 104 of the 205 hits
  are on claims that are not core.
- **Part A:** each sheet also lists every construct name in the claims, with
  the claims that use it, for the registry; and it gives the table's unit
  names between back-quotes, which the task asks the coders to copy.
- **Part B:** "held, varied or unclear" are the task's and the check's
  `held`, `varies` and `unclear`. The check reads some forms leniently, each
  reading a remark (`build_map_test.py`'s docstring lists them), and no factor
  where parts 5 or 6 apply is a remark, not a fault, since a paper may use
  none.

Then, on 18 Oct 2026, before any chat of round 2:

- **Part E, the PI's comparison:** the twelve readings. The tabs are Bechky's
  six and then Pratt's, each in the sample's order, and the draw is made tab by
  tab in that order. T37's account gives, with each code, the claim's statement
  and the page the coder gave, as the map's account gives what each element is;
  neither account is labelled, though their form shows which is which (part H).
  The sheet's two time cells may be left empty: the PI's report of how long it
  took serves, as it did for the settling, whose time cells were left empty.
- **Part E, the openings' check:** the question stays as fixed. The checkers
  are told that an opening's second sentence names an investigation, which
  the reading need not propose, and fails only if what it would settle is not
  what the reading says. As fixed, the question would fail every opening
  whose second sentence the reading does not itself propose, which is what
  the placement task asks the second sentence to be.
- **Part E, the placement:** the chats get T37's codes as coder A (T37's
  Google coder, chats 64 and 66) and coder B (its OpenAI coder, chats 65 and
  67), unnamed, and are told to take them as a first placement on the claims
  and to place each reading on its own words; the task gives an example from
  a made-up paper, as round 1's did; passages are evidence, not elements; the
  check reads some forms leniently, each reading a remark
  (`build_map_round2.py`'s docstring lists them).
- **Part F:** each measure as `score_map_test.py`'s docstring defines it. To
  F4 it adds, by coder, the readings whose codes leave a core claim a label
  besides contested.

Then, on 18 Oct 2026, after chats 77 and 78 had run four times and each reply
had vanished at its very end, before any part of their new runs:

- **Part E, the placement:** the same model, settings
  and files, but the reply is asked for in parts, so that no single answer is
  long: Bechky's readings R01 to R10, R11 to R20 and R21 to R30, Pratt's R01
  to R09 and R10 to R17, each part one JSON object of the task's form, one
  part per `continue`, in the same chat (`MAP_SEND_2b.md`). A part that
  vanishes is asked for again. Each part is filed as it came;
  `join_placements.py`, fixed before any part is opened, joins a chat's parts
  in order into the one reply that the checks, the openings, the PI's comparison
  and the scorer read as before.

Then, on 18 Oct 2026, after chats 77 and 78 had given their parts and been
closed, before any reply of the new chats:

- **Part E, the placement:** chat 77 gave Bechky's R01
  to R20 in two parts, and its third part, R21 to R30, vanished at its end;
  chat 78 gave Pratt's two parts, but the second leaves R13 without an
  opening, and the comma left where it would have been makes that part no
  JSON object. Both chats were then closed, and a temporary chat cannot be
  reopened. Since the openings, the PI's comparison and the scorer take a reply
  only when every reading of its paper counts, the missing readings are asked
  of two fresh chats of the same model, settings and files, each asked only
  for them (`MAP_SEND_2c.md`): chat 81, Bechky's R21 to R30 in two parts (R21
  to R25, R26 to R30); chat 82, Pratt's R10 to R17 in one. A reply that
  vanishes is asked for again, and one that vanishes twice, one reading per
  reply. `join_placements.py`, unchanged, joins chat 77's two parts and
  chat 81's into `reply_77_bechky_place_argon.json`, and chat 78's first part
  and chat 82's reply into `reply_78_pratt_place_argon.json`, the names the
  scorer reads; chat 78's second part is filed as it came and not used.
  Before the new chats, the four parts were checked as far as they can be
  alone: no fault but the readings still to come and, in Pratt's second part,
  read with that comma dropped for this look only, R13's missing opening; no
  quoted span of more than eight words in any.
- **Part H, a limit added:** each paper's placements come from two chats of
  the same model, and Bechky's R21 to R30 and Pratt's R10 to R17 from chats
  that saw none of the other placements. Each reading is placed on its own,
  so the checks and measures read the joined replies as before; F7 counts the
  minutes of every run the PI reports, the runs that vanished among them.

Then, on 19 Oct 2026, after T39's results were in, and before any figure of what
follows was computed on the test's files:

- **Part F, a measure added (8): a rough ranking of the readings by the map,
  and its check against the PI's worth.** Exploratory: it is not a criterion of
  T39 and changes none of F1 to F7. The score is the one a Fable chat proposed
  on 19 Oct, with a table of twelve figures, unchanged, and nothing below is
  changed once a figure has been seen.
  - **A coding's score:** for each reading and each of T37's two codings as
    F4 gives them (the first coding the Google coder's, `gemini`; the second
    the OpenAI coder's, `astra`), the labels the closure gives the paper's
    core claims (`map_round2_key.json`: Bechky 7, Pratt 10), weighted
    contested 3, unsupported 2, weakened 1, idle ½ and restated 0 (the
    proposal names no weight for it), summed, and divided by 3 times the
    number of core claims. **A reading's score** is the lower of its two
    codings' scores.
  - **Stars,** from a score rounded to two decimals, half up, as Fable's
    table gives it: 0.60 or more, five; 0.40 to 0.59, four; 0.25 to 0.39,
    three; 0.10 to 0.24, two; below 0.10, one. A reading's stars are its
    score's. **The flag:** its two codings' scores give different stars.
    **The cost:** the number of passages in its evidence list in the joined
    placement reply (`reply_77_bechky_place_argon.json`,
    `reply_78_pratt_place_argon.json`).
  - **The check,** each paper on its own, on its real readings (Bechky 28,
    Pratt 15): Spearman's rank correlation between the reading's score and
    the PI's worth (0 to 3, `relation_results.json`), tied values given their mean
    rank; and its two-sided permutation p-value: the PI's worths shuffled among
    the same readings 10,000 times, each shuffle made afresh from their order
    by reading, with one stream of Python's `random.Random(20261027)` used in
    the order Bechky, Pratt, both papers together; a shuffle counts when its
    correlation is at least as far from zero as the observed one (within
    1e-12), and p is (count + 1) / 10,001. Beside it, described only: the
    same correlation for each coding's own score; the mean score at each
    worth; and, as a secondary figure, the correlation over both papers' 43
    real readings together, with its p. The four planted readings, which have
    no worth, are listed apart, with their score, stars, flag and cost. The
    seed was in use nowhere.
  - **How it is read, fixed now:** in a paper, the score tracks the PI's worth if
    its correlation is positive with p below 0.05, and runs against it if
    negative with p below 0.05; otherwise the check shows no clear relation
    at this size. The secondary figure is read the same way, as secondary.
  - **By script, then checked:** `rank_map_readings.py`, fixed by its sha256
    before it is run on the test's files, reads `map_results.json`
    (F4's labels and the planted readings), `relation_results.json` (the PI's
    worth), `map_round2_key.json` (the core claims) and the two joined
    placement replies, and writes `RANKING_CHECK.md` and
    `ranking_check.json`; it also recomputes the twelve figures of Fable's
    table, to show that the score is the one proposed. Every figure is
    recomputed independently, with separate code.
- **Part H, limits added for measure 8:** the score inherits the map's edge
  strengths, which decide between unsupported and weakened, and on which the
  two map coders agreed with kappa 0.884 (Bechky) and 0.321 (Pratt) before the
  PI's settling; it inherits T37's codes, whose coders agreed on the main claim
  of 31 of the 43 real readings; and the labels crowd the core (F4: a median of
  6 of Bechky's 7 core claims, 7 of Pratt's 10). It measures how much of the
  argument a reading would bring down if it were right, not whether it is
  right. The PI's worth was rated before the map was built, but the PI settled
  the map, so the two are not wholly apart; and Pratt's fifteen readings give a
  check of little power.
