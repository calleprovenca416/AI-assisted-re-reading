# The second link-definition test: the plan

*3 October 2026. The five points at the end were decided on 3 October, before
any chat. This text is the plan's third draft, with the decisions marked in it. Who may
receive this file: nobody (—).*

**The question.** Version 2.1 of the linking rules (`LINK_RULES_v2_1.md`) judges
what a passage shows against markers written for each claim. Do two independent
coders apply it the same way? The first test, on version 1.1, did not pass
(`LINK_TEST_RESULT.md`). This one runs on a fresh draw of Pratt pairs. Nothing
downstream changes until its result is read.

**What it asks of the PI.** Five decisions, taken on 3 Oct ("Decided on 3
October", at the end). Then seven chats, a reading of the markers and the
passages, and a sheet of 20 rows: about 11 to 13 hours ("The PI's time").

---

## Decided

- **30 Sep (after the two reviews of version 2).**
  - Judgment 1 is made from the passage, against markers. A separate session
    writes the markers, and another fixes each passage's first and last words.
  - A third kind of passage, `pattern`. Names are flagged. Thoughts count as
    reported. The markers and the passages are checked before they are frozen.
  - About 120 random rows, from linked and near pairs. κ of at least 0.60, gated
    on the main reading. The strict reading is reported, not gated.
  - No comparison with brief v2 on random rows. The 18 hard rows return as a
    fixed check.
  - The same two coders, with their settings recorded. Opus runs at extra effort.
- **1–3 Oct (after the colleague's review).**
  - Markers of a practice working carry a tag, `working` or `carried out`.
  - A second marker session, compared with the first without recoding.
  - The coders' table prints each passage's text. Reasons follow a short
    template.
  - Version 2.1 was frozen on 3 Oct, with the seed recorded on 30 Sep (30092026).
- **3 Oct (the five choices).**
  1. ChatGPT 5.6 writes the markers and fixes the passages, in two fresh
     Temporary Chats. Opus 5.5 writes the second marker set.
  2. The pass bar is read on one way of counting, fixed in advance: the main
     reading, names counted, patterns counted as reports, carried-out markers not
     counted, and without the pairs whose passage is the source of one of the
     claim's markers. Every other way is reported beside it.
  3. The sample: 60 linked and 60 near pairs, drawn fresh, and the 18 hard rows.
  4. The PI codes 20 of the rows by hand, as a sense check that is not gated.
  5. A new script, `link_test2.py`, is built for version 2.1.
- **3 Oct (the five points of this plan).** A-a, B the cap, C-a, D all of
  it, E as proposed. They are set out at the end.

---

## The steps, in order

Each step fixes something before the next step can see it. The script refuses a
step taken out of order.

| step | what happens | fixed when it ends |
|---|---|---|
| 0 | Version 2.1 frozen, 3 Oct | the rules and the seed |
| 1 | The PI decides the five points of this plan, the bar among them (done, 3 Oct). The script writes the three briefs from Parts S, P and A, word for word, with the reply forms and the fixed messages; they are reviewed independently. The PI checks that each model can read the paper's figures | the briefs, the bar, the cap, the draw rule, the fixed messages |
| 2 | Chat M1 (markers) and chat P (passages), run by the PI | — |
| 3 | The script reads and checks the replies; breaches are flagged independently; both returns are read in full and each flag decided | the markers, the passages, and which pairs are marker-source pairs |
| 4 | Chat M2 (second markers), run by the PI any time after step 3 | — (it is compared, never coded with) |
| 5 | The script draws the sample, builds the coders' tables and the PI's sheet. The tables are checked independently for leaks, and so is the code that derives the links, against Part B | the sample |
| 6 | The PI's sheet of 20 rows, before any coder chat | the sheet |
| 7 | Four coder chats, run by the PI | — |
| 8 | Read, score, report; the result note checked independently against the files | the result |

So the rules were fixed before any marker was written; the bar and the draw rule
before any marker was seen; the markers and passages before any pair was drawn;
and the sample before any answer was read.

---

## The seven chats

| chat | model and setting | attached | it returns | PI's time |
|---|---|---|---|---|
| **M1** markers | ChatGPT 5.6, Temporary Chat; memory, custom instructions and web search off | the marker brief, the list of claims, the PDF | condition, form and markers for the paper's 52 claims | about 1 h |
| **P** passages | ChatGPT 5.6, as M1, in its own Temporary Chat | the passage brief, the list of fragments, the PDF, three page images | the first and last words of 121 passages | about 1 h |
| **M2** second markers | Opus 5.5 at extra effort, incognito claude.ai chat, outside any project; web search, research and connectors off | the same three as M1 | the same, written independently | about 1 h |
| **C1a, C1b** coder | ChatGPT 5.6, as M1; two chats | the coder brief, one table (one half of the pairs, and their claims with the markers), the PDF, three page images | three judgments on about 75 rows each | about 45 min each |
| **C2a, C2b** coder | Opus 5.5, as M2; two chats | the same | the same | 1 to 1¼ h each |

Each coder's rows are split over two chats. One chat holding 150 rows, their
passages and the paper may be more than a chat can hold, and last time's chats
had 60 rows. The split is by row number, which is random. Within each chat,
judgment 1 is still made for every pair before judgments 2 and 3.

For every chat:

- attach exactly what the send sheet lists, and nothing else;
- note the model's name as the chat shows it, and its effort or thinking setting.
  ChatGPT's setting was not recorded last time;
- paste the first message from the send sheet. After that, type `continue` and
  nothing else, whatever the chat asks;
- copy each reply into the chat's text file as it arrives, before typing
  `continue`;
- never regenerate a reply, and never edit a message;
- keep the chat open until its file has been read in and checked;
- if a chat cannot open an attachment, stop and say so. Paste nothing else in.

Two other messages exist. Both are written in advance, in the send sheet, and
nothing else is ever typed.

- **The format request**, at most once per chat. It lists the lines the script
  could not read: a missing line, a missing field, or a code that is not one of
  the allowed words. It asks for those lines again in the form the brief gives,
  and says nothing about any answer.
- **The restart message**, for a chat that has stopped.

**If a chat stops.** A usage limit that resets is not a stop: wait, then type
`continue` in the same chat. A chat has stopped when it says the conversation is
too long, when it fails, or when it will not go on after `continue`. Then:

- **M1, M2 or P.** Keep what it returned. A fresh chat of the same model and
  setting gets the same files and the restart message, which names the first
  item still to do.
- **A coder chat that stops before judgment 1 is complete.** Its rows are coded
  again from the start in a fresh chat. The stopped chat's replies are filed and
  listed, and are not scored.
- **A coder chat that stops later.** Its judgment 1 stands. A fresh chat gets
  the same files and the restart message, which asks for judgments 2 and 3 only,
  from the first row still to do.

These are the only grounds for a second chat. The report says which items came
from which chat. A row still missing after the format request counts as a
disagreement on every field, as `not found` does.

M1 and P can run in either order; neither sees the other's output. The markers
cover all 52 claims and the passages all 121 fragments, so neither session can
tell which pairs will be drawn. Opus at extra effort is slow and takes a good
part of a session's allowance, so M2, C2a and C2b are best run on different days.

**File names.** The files a chat receives carry plain names that say nothing of a
test, a coder or a version: a file of instructions, and a list or a table.

---

## The sample: up to 150 rows

| stratum | rows | drawn from | counts toward the bar |
|---|---|---|---|
| hard | 18 | the same 18 as last time, fixed | condition 4 only |
| random linked | 60 | the extractor's 385 other links, less the marker-source pairs | yes |
| random near | 60 | 481 unlinked pairs where one of the fragment's own printed labels names one of the claim's constructs or its outcome, less the marker-source pairs | yes |
| marker-source | up to 12 | the marker-source pairs in those two pools, up to 6 from each | no: reported apart |

- **Marker-source pairs.** A pair is one when its passage holds the opening words
  of the sentence that one of the claim's markers came from. Such a passage can
  show that marker by construction. The script works this out for every pair in
  both pools when the markers and passages are frozen, before the draw. The 120
  rows of the bar are drawn from the other pairs, so the bar always rests on 120
  rows. A hard row that is a marker-source pair stays, and is flagged.
- The pools leave out the 18 hard pairs and the 42 random pairs used on 29–30
  Sep. Version 2 was written with those rows in view.
- A pair whose passage the passage session could not find leaves the pool, and
  is listed.
- **The draw rule.** Each pool is shuffled, and its pairs are taken in order
  until 60 are drawn. A pair is skipped if its claim already has six rows in that
  stratum (the cap, below).
- **The seed.** The draw's seed is made from the recorded seed (30092026) and
  the hash of the frozen markers and passages. So nobody can work out the sample
  before the markers and passages are fixed. The script draws once. The only
  other draw it allows is the top-up, under the rule in "After the test".
- Rows are shuffled and numbered from R001. The first half goes to each coder's
  first chat and the second half to the second. Fragments carry shuffled labels.
  Stubs are printed without the opening words that give away the extractor's
  voice code, as last time.
- The PI's sheet has 20 rows: 4 hard, 8 linked and 8 near, picked by the same
  seed.

**A cap of six rows per claim in each stratum (decided on 3 Oct).**
The linked pool is lopsided. One claim, C01, holds 96 of its 385 pairs, and a
third of the pool sits on the four claims with no outcome. Such claims only
describe, so their pairs can never be `with` or `against`. A simple draw would
put about 15 of the 60 linked rows on C01, and about 20 on claims with no
outcome. With the cap, C01 has six, and about 12 rows fall on claims with no
outcome. The three-value code then rests on more rows. The cap bites on C01 and
on one or two other claims; the rest of the draw is what a simple draw would
give. The cost: the sample holds fewer C01 rows than the extractor's links
would, and the report says so. (These figures come from 2,000 trial draws with
other seeds. The recorded seed has not been used.)

---

## The check before the markers and passages are frozen

**By the script.** It refuses to go on until each of these holds or is listed:

- every claim has a condition, a form, and markers or `none printed` with the
  pages searched;
- a claim with no printed outcome is `describes`, and no other claim is;
- every marker gives a page and opening words that are found in the paper's
  text;
- no sign is listed, in the same words, under both the condition and the
  outcome;
- where tags appear, they are on every condition marker of that claim, and on no
  category of a `maps` claim;
- every passage's first and last words are found on its page, once;
- no passage takes in another fragment's passage, unless it is listed.

**How words are found.** The paper is a scan with a text layer. The script looks
for each set of words in that text after setting aside case, punctuation,
spacing and hyphens at line ends, and it allows a misread letter or two. What it
cannot find is listed. It is then found by eye in the PDF, and the place is
logged.

**The printed passages.** Each passage's text is cut from the text layer between
its first and last words. Running heads and margin notes that fall inside it are
taken out. Each is read against the page before the freeze, and every correction
to the print is logged. The coders are told that the paper governs.

**Figures and table cells.** Seven fragments are a figure or a table cell (F30
to F34, F88 and F109), and two hard rows are among them. Their passage is the
figure or the cell itself. The table prints its reference and, for a cell, its
text, and the coder reads it in the paper. The scan's text layer garbles the
figures, so chat P and the four coder chats also get images of those three pages
(pp. 465, 477 and 482), the same for both models. At step 1 the PI checks that
each model can read them: one throwaway chat per model, with only the PDF, the
three images and a fixed question about Figure 1 and Table 1. If a model still
cannot, the rows on those fragments are reported apart.

**By reading.**

- An independent reader checks every marker against the sentence it cites and
  Part S, and every passage against its stub and Part P, and flags what it takes
  to be a clear breach. It is given the rules, the returns and the paper, and is
  told nothing of the hard rows or the first test, by instruction.
- Both returns are then read in full, as Part B says, and each flag decided;
  flags may be added. The readers know the hard rows, so every fix that touches
  a claim or a fragment of a hard row is marked as such.

**The fixes allowed,** and no others. They are the breaches Part B names:

1. remove a marker that is a name or another abstract term, one of the author's
   categories, a single instance, or a sign of only one part of a joint
   condition;
2. remove a sign listed on both sides from the side it does not belong to;
3. correct a wrong tag;
4. move a passage's first or last words, to leave out another occurrence or a
   comment, or to take in a sentence that reports the same occurrence;
5. correct a page or opening words that were miscopied.

No marker is added or reworded. No condition or form is changed. A breach that
none of these can put right stays as written, and is listed in the report. Each
fix is logged with its reason before the freeze. Nothing changes after it.

**When a return is poor (decided on 3 Oct: one fresh run).**

- If more than a quarter of the markers have a clear breach, the marker return is
  set aside whole and chat M1 is run once more, fresh. The same holds for the
  passages (more than 30 of 121) and chat P. If the second return is as poor,
  the test stops there, and Part S or Part P is revised as a new version.
- If the return gives no marker for the outcome of more than half of the 48
  claims that have one, or none for the condition of more than half, the test
  pauses and the PI decides whether it is worth running. Coders could then show
  those sides only by a name.

A second run departs from the wording of the frozen rules, whose opening and
Part C say the markers and the passages are written once. It keeps to the
purpose of that wording: no pair exists when the second run is made. The other
choice was no second run: a poor return stops the test, and the Part is revised.

**Note, 3 Oct 2026.** The second run is allowed (point C-a). So where the
frozen rules say that the markers and the passages are written once, this test
reads: once, or twice if the first return is set aside whole under the rule
above. The rules file is not changed. The report says whether a second run was
made.

---

## The second marker set

Chat M2 is run after the first set is frozen. So nobody who reads the first set
before its freeze has seen the second.

The two sets are compared, and nothing is coded with the second. For each claim:

- the condition: the same state, or not;
- the form;
- where `none printed` falls;
- the tags;
- marker by marker, whether each sign has a counterpart in the other set. Two
  markers are counterparts when they give the same sign in different words: any
  passage that showed one would show the other.

The markers are matched independently, without knowing which set is which. The
report gives agreement on form, on `none printed` and on tags, the share of
markers with a counterpart, and the claims where the two sets would count
different things. None of it is gated. As Part C of the rules says, it cannot
show how far the second set would change the links.

---

## The pass bar

**The bar was set on 3 Oct,** with this plan, before any marker
existed. The script records it at step 1 with the briefs, and refuses any later
change.

It is read on the 120 random rows, between the two coders, counted as choice 2
says. Pass only if all five hold:

1. **Author link:** κ of at least 0.60.
2. **Evidence link:** κ of at least 0.60.
3. **Three-value code** (`with`, `against`, neither): κ of at least 0.60, unless
   it is too few to tell (below).
4. **Hard rows:** the coders agree on the five-value code for more of the 18 than
   two coders answering at random would 95% of the time. Neither gives `with` to
   one hard row and `against` to its twin.
5. **`not found`:** neither coder marks more than 6 of all its rows `not found`.

A κ that cannot be computed counts as not passed, except as the next paragraph
says. The PI's sheet is a sense check, not gated.

**Condition 3 when the code is rare.** Last time `with` was rare: 2 and 5 of the
42 random rows, and no `against`. At those rates the stricter coder would give
6 or 7 such codes on 120 rows. A κ on so few swings on two or three answers:
three changed rows moved it from 0.23 to 0.64 in the rerun. So condition 3 has a
third result, fixed now:

- **too few to tell,** if the two coders between them give `with` or `against`
  to fewer than 5 of the 120 rows; or if each coder gives fewer than 10 such
  codes and κ's 95% interval includes 0.60;
- otherwise **passed** at 0.60 or above, and **not passed** below it.

One coder at 9 and the other at 25 is a disagreement, and is read as one. So is
one coder at none and the other at five or more. The interval comes from 2,000
resamples of the 120 rows, with a seed recorded at step 1.

Too few to tell is not a pass. If the other four conditions hold, a top-up of 60
rows is then run, and condition 3 is read once more on all 180 ("After the
test"). That is automatic, not a choice made after seeing κ. At last time's
rates it would be needed about one time in three.

**What 120 rows can show.** A κ on 120 rows moves by chance: by about ±0.18 for
each link, and by ±0.27 or more for the direction code. The bar needs all three
at once, which makes it strict. A simulation gives these rough figures:

| if the rules' true κ on all three is | the bar passes about |
|---|---|
| 0.50 or less | 1 time in 100 |
| 0.60 | 1 time in 6 |
| 0.70 | 2 times in 3 |
| 0.75 | 9 times in 10 |
| 0.80 | nearly always |

So a pass is strong evidence that the rules work. A fail is weaker evidence that
they do not: rules at 0.70 fail one time in three by chance. Without the third
result and its top-up, rules at 0.75 pass about 8 times in 10 and rules at 0.70
about 6 in 10. More rows would narrow this a little, at about an hour of the
PI's time for every 40 rows. This is the bar as decided on 30 Sep; the figures
are here so that it is set knowingly. Every κ is printed with its interval.

**The pooled figure is the kinder one.** The bar pools linked and near rows, as
decided. Near rows are mostly an easy "no", which lifts κ. In last time's rerun
the direction code stood at 0.64 on all random rows, and at 0.46 on the linked
rows alone. So each of the three κ is also printed for the 60 linked rows alone,
with its interval, next to the gated figure. It is not gated: on 60 rows a κ
moves by chance about 1.4 times as much. Not counting carried-out markers is
kinder in the same way, because it hides any split over whether such a marker
is shown. The figures with them counted are printed beside the bar too.

**The chance baseline for condition 4.** Two coders who draw every code evenly
from the values the brief allows, 20,000 times, with each claim's form as the
marker session gave it. The baseline is the number of hard rows they agree on
95% of the time. The script computes it at the draw; a sketch puts it near 11 of
18. It is a floor, and a low one: under version 1.1 the coders agreed on 17 of
the 18 and the test still failed. The twin pairs are the five in the table
below.

**More than six `not found`** is a fault in the materials, not in the rules: the
first and last words, or the scan. Each such row counts as a disagreement on
every field, so seven of them cut a link's κ by about 0.05 to 0.1, and condition
5 will seldom fail alone. "After the test" says what follows.

**Reported beside the bar, not gated:**

- every κ with its 95% interval, AC1 and raw agreement, on all 120 rows and on
  the 60 linked rows alone;
- the strict reading, and each of the other ways of counting;
- kind, use, condition, outcome, other cause, `bounded` and `named`;
- for claims with tagged markers, whether the coders list the same markers as
  shown;
- the rows the rules say are reported apart: `not found`, marker sources, sides
  no marker can show, the practice claims, named absences;
- the rows on the 29 fragments whose stub opens "the author's account is that",
  apart from the rest ("Added at step 1", below);
- every `with` count split into condition with outcome, and outcome only;
- the hard rows against the last two results. Under brief v2 the two models
  agreed on 10 of the 18, and under version 1.1 on 17;
- the PI's sheet against each coder.

---

## What each chat returns

One line per item, or one block per claim, in a fixed form that the brief gives.
Replies come in batches, with `continue` between: 13 claims, or 25 fragments or
pairs.

- **Markers, for each claim:** a reason; the condition; the form; then one line
  per marker, with its label, the sign, its tag if it has one, and the page and
  opening words of the sentence it comes from. Or `none printed`, with the pages
  searched.
- **Passages, for each fragment:**
  `K007 | pages | reason | first: its first words | last: its last words`, or
  `not found`. For a figure or a table cell, its number, row and column stand in
  place of the words. A passage of ten words or fewer is given whole.
- **Coder, judgment 1, for each row:**
  `R001 | reason | shown: c2, o1 | condition | outcome | other cause | bounded`.
  The reason follows one template: each marker found, by its label, with the few
  words of the passage that show it; or "no marker". It adds "both sides" or
  "different cases" where the rules call for them. The script reads the list
  after `shown:`, apart from the reason, as Part B asks.
- **Coder, judgments 2 and 3, for each row:** `R001 | reason | kind | use`. The
  reason says, in a clause each, what the passage reports and how the paper
  introduces or places it.

The forms are written into the briefs at step 1. The independent review checks
that each brief holds its Part word for word, that the form asks for nothing the
Part does not, and that nothing in it names a test.

**The derivation.** The script derives the links from the judgments by Part B's
table, under all 32 ways of counting. Before any coder's answer is read, that
derivation is written a second time, independently, from Part B alone. The
two are run on every possible set of answers, and any difference is settled
against Part B's text.

---

## The hard rows: what each now checks

They are the cases the reviews and the audit argued, so they are a check and not
a fair test.

| rows | why they were chosen | what they check under version 2.1 |
|---|---|---|
| F93→C20, F93→C23 | coded `against`: the outcome goes the other way and the stub never shows the condition | an outcome the other way, with no condition shown, stays out of `against` |
| F97→C21, F98→C21 | a negative case, coded `with` in one and `against` in the other | the same kind of case gets the same code |
| F99→C20, F99→C23 | the author's account of a negative case, coded `with` | a pattern the author explains; a named failure; thoughts the author attributes |
| F20→C08 | C08's only link is its own source sentence | a restatement is never evidence |
| F88→C27, F109→C29 | figures of the author's model, coded `with` | a figure of a model is a `reading` |
| F24→C09, F25→C09, F29→C13 | stubs that dropped the paper's printed numbers | the passage now prints the numbers |
| F10→C20, F12→C20 | similar stubs, one linked and one not | the same kind of case gets the same code |
| F83→C20 | carries the paper's label for C20's outcome, but was not linked | a name is marked `named`, and counted both ways |
| F72→C20, F73→C20 | the same construct, coded `illustrates` in one and `with` in the other | the same kind of case gets the same code |
| F96→C28 | a pattern reported across cases, which the voice test could not place | `pattern` |

**The five twin pairs** of condition 4, as in the first test: F93 and F99 on
C20; F93 and F99 on C23; F97 and F98 on C21; F10 and F12 on C20; F72 and F73 on
C20. With each coder's rows in two chats, two twins can fall in different chats.
The check then asks more of the rules than last time, when both sat in one chat.

C20 has 7 of the 18 rows. Its printed direction speaks of *successful* positive
programming, so its condition should come back as a practice working, with
tagged markers. If so, the hard rows will show the tags at work.

---

## What the test cannot show

- Anything about a paper other than Pratt.
- A cold result. The rules were written after the reviews of Pratt's run and
  after the first test, and the hard rows return.
- How the rules do on claims not seen before. 89% of the linked pool's pairs,
  and 78% of the near pool's, sit on a claim that had a row in the first test.
  30% and 40% sit on a fragment that had one.
- Much about `against`. The extractor's three `against` links are all hard rows.
  On the random rows the direction code will mostly be `with` or neither.
- Which link, the author's or the evidence link, should feed the scored measure.
- How far a second set of markers, or a second passage session, would change the
  links.
- How stable each coder is. Each model codes once.

## Confounds to report with the result

- ChatGPT 5.6 wrote the claims, writes the markers, fixes the passages, and is
  one of the two coders. Opus 5.5 writes the second marker set and is the other
  coder. Every chat is separate and keeps no memory.
- The examples in Part A echo the splits of the first test.
- The colleague who reviewed version 2 had the paper and the whole rules file.
- If the cap is adopted, the sample holds fewer rows on C01 than a simple draw.
- The paper's PDF is a scan with a text layer. Where the printed passage and the
  paper differ, the coders are told to go by the paper.
- The people who check the markers and passages know the hard rows.
- The passage chat sees each stub as the extractor wrote it. On 29 fragments
  the stub opens "the author's account is that", so there the passage, and with
  it the kind, partly follows the extractor's voice code.

---

## The PI's time

| what | time |
|---|---|
| the figure check: two throwaway chats | 15 min |
| chats M1 and P | about 2 h |
| reading all the markers and passages, and deciding the flags | 2 to 2½ h |
| chat M2 | about 1 h |
| the sheet of 20 rows | about 2 h |
| the four coder chats | 3½ to 4½ h |
| **in all** | **about 11 to 13 h** |
| the top-up, only if condition 3 is too few to tell | 2 to 3 h more |

The first test took about four to five hours. This one has three more chats, a
check, and more than twice the rows.

Two parts could have been dropped to save time. Neither was recommended, and
both were kept (point D):

- **the second marker chat** (about 1 h). Without it, nothing shows how far the
  markers depend on who writes them;
- **the sheet** (about 2 h). It is the only human reading in the test.

---

## After the test

- **If the bar holds,** choose the route: a separate linking stage on the frozen
  records, with markers and passages as two of its steps, or brief v3 and
  re-extraction.
- **If condition 3 is too few to tell, and the other four hold,** the top-up is
  run. It is fixed now:
  - 60 fresh pairs from the linked pool, on claims with an outcome and fragments
    the extractor marked as reported. Every `with` on a linked row fell there
    last time;
  - no marker-source pair and no row already drawn; the cap of six per claim,
    counted afresh; a seed made from the recorded seed, the hash of the frozen
    markers and passages, and the word "top-up";
  - the same frozen markers and passages, and the same two coders, in one fresh
    chat each;
  - condition 3 is then read once more, by the same rule, on all 180 rows.
    Conditions 1, 2, 4 and 5 stand as first read;
  - there is no second top-up. If condition 3 is still too few to tell, the
    direction code is left open, and the proposal says it was too rare under
    these rules to test;
  - about two to three hours of the PI's time, and about three more days.
- **If it fails,** the report shows which judgment failed. That judgment is
  revised and tested on a fresh draw, never scored again on these rows. The pools
  would still hold about 320 linked and 415 near pairs.
- **If condition 5 fails,** every κ is also computed without the `not found`
  rows, and condition 4 is read again with the hard rows that either coder
  marked `not found` counted as agreed. If a κ condition or condition 4 fails
  even so, the rules failed, as above. If none does, the materials failed and
  not the rules: the first and last words are checked against the paper and
  corrected, and the test is run again on a fresh draw, with the same rules.
  Neither case is a pass.
- **Either way,** the result goes into the proposal as a finding about the
  instrument.

---

## Added at step 1, before the freeze (3 October)

An independent review of the script and the files for the chats, before
anything was frozen, found four points that the plan above had left open. Each
was settled before any chat and before any marker existed. Points 1 and 2 touch
how the bar is read, and were settled as 1a and 2a, each against its other
option, as they stand below. Points 3 and 4 change nothing in the bar.

1. **A hard row whose passage cannot be found.** If the passage chat cannot find
   the passage of a fragment in a hard row, that row is left out and listed.
   Without a passage it cannot be judged. Condition 4 is then read on the hard
   rows that remain. (The other option was to keep the row: the coders would
   mark it `not found`, which counts against the rules.)
2. **Condition 5 failing together with condition 4.** The plan said what follows
   when condition 5 fails and a κ condition does. Condition 4 is now read the
   same way: with the hard rows that either coder marked `not found` counted as
   agreed. If it fails even so, the rules failed ("After the test"). (The other
   option was to read that case as the materials failing.)
3. **The answer to a format request.** The PI saves it in a file of its own.
   What it gives for the items the request named replaces or completes the
   earlier lines for those items. Anything else it gives again is left as first
   given, and listed. Anything a chat writes after `END` is read the same way.
   Before `END`, an item given twice keeps its first form and is listed.
4. **The stubs in the list of fragments.** The passage chat gets each stub as the
   extractor wrote it. On 29 of them it opens "the author's account is that".
   Part P tells the author's own statement from a report by exactly that, so the
   words stay. The cost is that, for those fragments, the passage partly follows
   the extractor's voice code. Their rows are reported apart. The coders' tables
   print every stub without those words, as in the first test.

The hashes of the paper's PDF and of the three page images are recorded with the
freeze, though the files stay out of the folder.

---

## Decided on 3 October

**A-a, B the cap, C-a, D all of it, E as proposed.**

**A. The pass bar:** the five conditions above. For condition 3, the options
were:

- **a. "too few to tell", with the automatic top-up. Chosen.** A fail by chance
  would cost about ten days, and the top-up costs two to three hours about one
  time in three;
- b. "too few to tell", with no top-up: the direction code is then left open;
- c. pass and fail only, whatever the count.

**B. The cap** of six rows per claim in each stratum. **Chosen,** over a simple
draw.

**C. The rule for a poor return** of markers or passages. The options were:

- **a. more than a quarter breached means one fresh run, and more than half with
  no marker means a pause. Chosen.** The second run departs from the frozen
  rules' wording, "once", and is recorded in the note above;
- b. no second run: a poor return stops the test, and the Part is revised.

**D. The time:** about 11 to 13 hours. **All of it:** the second marker chat and
the PI's sheet both stay.

**E. Smaller choices made in this plan. Confirmed as proposed:**

- each coder's rows in two chats;
- up to 12 marker-source pairs as extra rows, outside the bar;
- the draw's seed made from the recorded seed and the hash of the frozen markers
  and passages;
- images of three pages attached to chat P and the coder chats;
- the five kinds of fix allowed before the freeze.

---

## Files

Written by `link_test2.py`, except where noted.

| file | what | who receives it |
|---|---|---|
| `LINK_RULES_v2_1.md`, `link_rules_v2_1_freeze.json` | the rules and their freeze (exist) | nobody |
| `link_test2.py` | compose, freeze, read, check, draw, build, score, with a self-test | nobody |
| `link_test2_fixed.py` | the draw and the reading of the pass bar, as code; its hash is recorded at step 1 | nobody |
| `instructions_claims.md`, `claims.md` | the marker brief: Part S word for word, with the reply form; and the 52 claims: statement, pages, outcome, asserted direction | chats M1 and M2 |
| `instructions_passages.md`, `fragments.md` | the passage brief: Part P word for word, with the reply form; and the 121 fragments: label, page, stub | chat P |
| `instructions_pairs.md`; after the draw, `table_1.md` and `table_2.md` | the coder brief: Part A word for word, with the reply form; and two tables, each with one half of the pairs, their passages, and their claims with the markers | the coder chats |
| `LINK_TEST2_SEND.md` | for the PI: what to attach and paste, chat by chat, with the fixed messages | the PI |
| `link_test2_freeze.json` | recorded before any chat: the hashes of the briefs, of this plan and of the fixed code; the bar, the cap, the draw rule, the rule for a poor return, the fixed messages | nobody |
| `link_test2_prep.json` | the markers and passages as checked, every fix, the marker-source pairs, and their hash | nobody |
| `link_test2_key.json` | the sample: strata, labels, the extractor's codes, the chance baseline | nobody |
| `link_test2_human_sheet.xlsx` | the PI's 20 rows | the PI |
| the replies, the report and `LINK_TEST2_RESULT.md` | as last time | nobody |

The paper's PDF stays out of the folder, and so do the three page images made
from it. The script reads the paper's text from a copy kept outside the folder.
