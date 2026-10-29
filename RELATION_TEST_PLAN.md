# The relation test (T37): how far does each reading depart from the paper's logic, as models code it?

Fixed on 16 Oct 2026, before any chat of the test (chats 62 to 67). It pilots a
step the protocol does not yet have: frontier models, not the writer of a
reading, code how the reading relates to the claims of the paper's index. Its
text was not changed after; the two changes made since are set out at its foot,
with their reasons.

## What it asks

1. **Q1.** Do two coders from different vendors, Gemini 3.1 Pro and GPT 6
   Astra, agree on how each reading relates to the paper's claims, in six
   defined types and in four levels?
2. **Q2.** Does each agree with a person's coding, the PI's, on a sample of
   the readings?
3. **Q3.** Does each code planted readings, written to be of a known type, as
   that type?
4. **Described:** the types beside the PI's worth for the same readings; the
   types by the chat or arm that wrote the readings.

Described, not tested: no figure decides anything, and there is no bar.

## The readings

- **Bechky:** the 28 readings of T33, M01 to M28, each one paragraph, as
  `READINGS_matching.md` gives them.
- **Pratt:** the wager test's 15 readings, P01 to P15, as
  stage2/markers/READINGS_pratt.md gives them, their sentences joined into one
  paragraph, as on the PI's worth sheet of 11 Oct.
- **Planted:** two per paper, written by chats 62 and 63 to a specification
  (below).
- **Who wrote them:** of the 43 real readings, Fable 5.1 wrote 33 (chats 22 to
  27 and 46) and GPT 6 Astra 10 (chats 49 and 50); Gemini wrote none. The PI
  has rated all 43 for worth (the sheets of 11 Oct, of T32 and of T33).
- **The files the coders get:** for each paper, its real and planted readings
  shuffled together and numbered afresh, R01 onward, with nothing to say which
  chat, arm or test wrote a reading, or that any is planted. The shuffle, the
  draw of the PI's sample and all else drawn after the planted readings come
  back use one generator, random.Random(20261022), in this order: Bechky's
  shuffle, Pratt's shuffle, then the PI's six readings from each paper's real ones.

## The claims

Each coder gets its paper's claims as the frozen index records them
(`bechky_2020_v1.json`, 23 claims; `pratt_2000_v1.json`, 60), each with its
number, its statement and its pages, as arm B of T33 had Bechky's: no outcome,
direction, `core`, links, passages or other codes. The coders have the paper
itself for everything else.

## The types

For one reading and one claim, one type, defined against that claim:

- `inverts`: the reading holds that the claim's outcome goes the other way
  under the condition the claim names, or that a process the claim states runs
  in the reverse order.
- `other_mechanism`: the reading keeps the claim's outcome but puts a
  different mechanism or cause in place of the paper's.
- `rereads_evidence`: the reading takes passages the paper itself offers for
  the claim and reads them so that they no longer support it as stated.
- `challenges_premise`: the reading questions something the paper's account of
  the claim takes for granted (a premise, a category, a boundary), rather than
  its outcome or its mechanism.
- `complements`: the reading adds a mechanism, a condition or a level to the
  claim, or changes its scope, without denying it.
- `restates`: the reading says what the claim already says.

If more than one fits, the first that fits in this order is coded. The four
**levels**: inverts; dismantles (`other_mechanism`, `rereads_evidence`,
`challenges_premise`); complements; restates. These follow the PI's terms
(invert, dismantle or significantly complement), with a zero point.

For each reading a coder gives: its **main claim**, the one it bears on most
directly, or `none` if it bears on no claim in the list; the **main type**, on
that claim (`none` with `none`); up to two **other claims** it bears on, each
with its type; a one-sentence **reason** for the main type; and the **page**
of the paper the main type rests on. The brief, `RELATION_CODING.md`, says this
with a made-up example, and asks for one JSON object.

## The coders

| chat | paper | coder |
|---|---|---|
| 64 | Bechky | Gemini 3.1 Pro, in a fresh temporary chat, its deepest thinking setting, as the judges of T31 (chats 43 and 44) |
| 65 | Bechky | GPT 6 Astra at max, in a fresh ChatGPT Temporary Chat; memory, custom instructions and web search off; no project |
| 66 | Pratt | Gemini 3.1 Pro, as chat 64 |
| 67 | Pratt | GPT 6 Astra at max, as chat 65 |

Each gets the paper's PDF, `RELATION_CODING.md`, its paper's claims file and its
paper's readings file, and one fixed message; nothing else. One run each.

## The planted readings

- **Chats 62 (Bechky) and 63 (Pratt):** Fable 5.1 at max, in a fresh incognito
  claude.ai chat with the plain chats' settings, each given the paper's PDF
  and its specification, `PLANTED_SPEC_bechky.md` or `PLANTED_SPEC_pratt.md`,
  and nothing else. Fable writes them because it wrote most of the real
  readings, so the planted ones read like them; neither coder is Fable's
  vendor.
- **What each specification asks:** two readings, each of one type against one
  claim, in the plain prompt's form (a wager of 80 to 150 words, and the
  passages it rests on, each with its page and what it does), written as a
  reading, without naming its type, and quoting no more than eight words of
  the paper in a row. Bechky: one that **inverts** a claim and one that
  **complements** another. Pratt: one that puts **another mechanism** in place
  of a claim's and one that **restates** another. One planted reading for each
  level.
- **The claims** are drawn by the builder, with random.Random(20261021), from
  each paper's claims that the frozen index marks `core` and gives an outcome
  and a direction: two for each paper, the first drawn for the first type.
  Bechky has four such claims, Pratt eight.
- **The PI's check:** before the coders run, the PI says of each planted reading,
  on a short sheet, whether it is of its type against its claim. A planted
  reading the PI does not confirm stays in the coders' files, and is left out of
  Q3 and reported.

## The PI's sample

- **Six real readings of each paper,** drawn as above, on a sheet,
  `relation_sheet.xlsx`, with the six types, the rule of order, the example and
  each paper's claims beside them. For each, the same as a coder: the main
  claim and the main type (the cells offer them), and a note if the PI likes. About
  40 minutes.
- **Blind:** the PI fills it before opening any of chats 64 to 67. The PI has
  rated these readings for worth before, so the coding is not blind to the PI's
  earlier view of them.

## Checks on the replies

- **Writers (62, 63):** one JSON object with two readings, each with its
  claim, a non-empty wager and a list of evidence, each item a page and a job.
- **Coders (64 to 67):** one JSON object whose codes name every reading of its
  file exactly once; each main claim one of the paper's claims or `none`; each
  main type one of the six, or `none` exactly when the main claim is `none`; at
  most two other claims, each one of the paper's claims, not the main one, with
  one of the six types; a reason and a page.
- **For all:** each reply is copied into a new, empty folder and read by script
  with `python3 -I`. Every quoted span of more than eight words is flagged
  before the reply is filed, and the span is not filed. A reply in parts is
  joined. A reply that fails its check is reported as it is; a chat is run
  again only if it is decided so.

## The measures

For each paper and for both together, on the 43 real readings unless said:

- **M1. Agreement between the coders on the main type:** raw agreement and
  Cohen's kappa with its confusion table, in the six types (with `none`) and
  in the four levels (with `none`); for both papers together, a 95% interval
  from 2,000 resamples of the readings with random.Random(20261023), its ends
  read as `agreement.py` reads them. A kappa is not given when a table has one
  code throughout.
- **M2. Agreement on the main claim:** how many readings both coders give the
  same main claim, and among those how many the same main type.
- **M3. The planted readings:** for each planted reading the PI confirmed, and
  each coder: **caught** when its main claim is the planted claim and its main
  type the planted type; **caught aside** when the planted claim is among its
  other claims with the planted type; otherwise **missed**, with what it
  coded.
- **M4. Each coder against the PI,** on the PI's twelve: how many readings it gives
  the PI's main claim, the PI's main type, and the PI's level; and the two coders against
  each other on the same twelve.
- **M5. Described:** each coder's count of each type and level; on the
  readings where the two agree on the level, the PI's worth (0 to 3) by level,
  as counts and means; and the levels by the chat that wrote the reading
  (Bechky: chats 23, 26, 27, 46, 49 and 50, by `matching_key.json`) and by arm
  (Pratt: system, middle and plain, by stage2/markers/KEY.json).

## What the figures will be read as, fixed now

- Agreement between the coders shows that the coding can be repeated across
  two vendors, not that it is right: two models can share a misreading.
  Whether it is right speaks through the PI's sample and the planted readings,
  and both are small.
- A type says what a reading does to a claim of the index, not whether the
  reading holds or is worth pursuing. Worth beside the types is described, not
  tested, and the PI's worth was rated on three occasions knowing different
  things.
- The readings are coded as written. The protocol would code standard
  statements, drafted in step 9, which do not exist yet; how far a reading's
  wording sways its type is not measured here.
- In the protocol this coding would be done by models alone, checked by
  agreement across vendors, planted readings and the scholars' judgments in
  step 9; the PI's sample is the pilot's one anchor in a person's reading.

## The order

1. This plan fixed by its hash; then `RELATION_CODING.md`, the two claims
   files, the two specifications and the PI's steps, `RELATION_SEND.md`, fixed by
   theirs, before any chat.
2. The builder of the readings files, the PI's sheets and the key, and the scorer,
   tested on made-up replies and made-up sheets, fixed by their hashes before
   any reply is opened.
3. Chats 62 and 63; their replies checked and filed; the PI's check of the four
   planted readings.
4. The readings files, the key and the PI's coding sheet built; the PI's coding.
5. Chats 64 to 67, side by side; their replies checked and filed.
6. Scored; every figure checked independently, with separate code.

## Limits, known now

- Two coders, one run each; 28 and 15 real readings; twelve in the PI's
  sample; four planted readings, one for each level, so
  `rereads_evidence` and `challenges_premise` are not planted.
- GPT 6 Astra codes ten readings its own model wrote; Gemini codes none of its
  own.
- The planted readings are written by a model to a specification; they may
  differ from the real ones in ways a coder could notice.
- The PI is not blind to the readings; the PI has rated them before.
- The claims are the index's statements; a reading whose point lies outside
  them is coded `none`.

## The PI's time

Chats 62 and 63, about 10 minutes side by side; the PI's check of the planted
readings, about 10 minutes; the PI's coding, about 40 minutes; chats 64 to 67, about
20 minutes side by side. About 1.5 hours.

## Changes, added after the plan was fixed

**17 Oct 2026. The planted readings are shortened by their writers.** The
reason: chats 62 and 63 wrote readings that run 700 to 805 words as the coders
would get them, with 10 to 12 pieces of evidence each, where the real readings
run 164 to 579 words (Bechky) and 202 to 383 (Pratt), and the plain readings of
chats 49 and 50 have 3 to 5 pieces of evidence: the planted readings would have
been the longest in each file.

So the PI pastes one fixed message, below, in each of chats 62 and 63, which
are still open, and their shortened replies are the ones the readings files
take, the PI checks and the coders code. The first replies stay filed,
unchanged, and serve nothing else. The shortened replies are checked as the
first ones were, and a reply that fails is handled as the plan says. Nothing
else in the plan changes; above this section, not a byte of it has changed
(its first 12,100 bytes keep the sha256 a7388fce…).

The message, the same in both chats:

```
Please shorten both readings. Keep each reading's argument, and the claim it is about, as they are; but bring each wager to 80 to 110 words, and keep only the three to five passages the reading rests on most, each with its page and what it does, in one or two sentences. Everything else in the specification still applies. Return the whole JSON object again, in the same form, as a file if you can, otherwise as one code block.
```

**17 Oct 2026. The Google coder was Gemini 4 Argon, not Gemini 3.1 Pro.** Chats
64 and 66 ran on Google's newer model, which Google names Gemini 4 Argon
(announced on 30 Sep 2026 and open more widely from 13 Oct, by the press
reports), at its High thinking level, with every other setting as the steps say.
The coders are still of two vendors, and Google's model still wrote none of the
readings. Nothing else changes. The scorer, fixed before any reply came in,
names the Google coder "Gemini 3.1 Pro" in its tables; the results carry this
correction below their line, and every account of the test names the model as it
ran.
