# Second coder — protocol

Who may code a paper a second time, what they receive, what they code, and what
may be reported from the result. Companion to `CLAIM_EXTRACTION.md`, which
defines most of the fields, and to `attack.md`, which no coder may ever read.
Gloss relation's four codes are not defined there: they are defined in
`EXTRACTION_BRIEF.md` and `CODING_INSTRUCTIONS.md`, in the same words.

**This page is not what a coder reads.** A coder reads `CODING_INSTRUCTIONS.md`,
which is frozen, and nothing else of this folder. This page is for whoever
runs the coding and reports from it.

Rewritten on 7 October 2026 for the cold papers. The version before it barred a
model from coding, ordered the stages A, A2, B, and gave the coder a blind
corpus. Three decisions changed that: a second frontier model as coder 2 (26
Sep, named on 28 Sep), the decisions of 28 Sep after Pratt's run, and Stage V.
What that version laid down for Carlile is kept at the end.

Revised later the same day: a cold paper's agreement figures are reportable, and kappa is
withheld on the cold papers by count only.

The purpose is narrow. Every trigger in this instrument rests on a judgement,
and a judgement made once by one coder is not a measurement. This protocol
makes ten fields measurable and says plainly what cannot be claimed until they
are.

---

## The cold papers: who codes

**Coder 1 is the extraction session** (changed on 28 Sep). One fresh session
per paper extracts the corpus and its sidecar under `EXTRACTION_BRIEF.md`, with
the PDF and nothing else. The extractor is the same model and setting for all
four papers.

**Coder 2 is another frontier model, from a different vendor than the
extractor**. Named on 28 Sep: Opus 5.5, in incognito claude.ai chats, one
fresh chat per stage, at one effort setting for every stage and paper. The
setting is recorded before the first stage is sent.

So on the cold papers **both coders are models**, with the limitation stated
below.

**The PI opens every session.** No session that can reach the project's folder
extracts or codes: a session that can reach a file has received it.

**Who may not code a paper a second time, without exception:**

- A session that has read `attack.md`, any card, any attack result, the
  project's working notes, the glossary, an agreement log, the corpus, or the
  sidecar.
- The session that extracted the paper, and any session that reviewed its
  extraction.
- Whoever did the v5 migration coding of that paper. Coding a field and then
  double-coding your own coding measures nothing. No cold paper has been
  migrated; the bar stands for when one is.
- A chat that has already coded another stage of the paper, or any stage of
  another paper. Each stage gets a chat of its own, so that nothing carries
  over between A, A2, V and B.
- A session that builds the packs or holds their keys, and any agent it starts.
  Agents are checks, never coders.

**A person may still code.** What is asked of a person stands as it did:
familiar with qualitative research, able to read the paper in full, and with no
stake in the outcome. Whether a colleague codes a slice of a paper is open. The
colleague who reviewed version 2 of the link rules on 1 Oct had the Pratt paper
and the whole rules file; if she codes a slice, it cannot include linking. The
disqualifications above bind a person as they bind a session.

**What a coder is told** is what `CODING_INSTRUCTIONS.md` says: the general
purpose, a study of how qualitative papers arrange their evidence. Nothing
about seams, moves, readings, or what any code is expected to trigger. Telling
a coder that `core` gates a move is enough to bias `core`. The message that
opens each chat is fixed, and is written by the pack builder into that stage's
SEND file. After it, the PI types `continue` and nothing else. If the chat asks
a question, the fixed reply in the SEND file is the only answer.

---

## What a coder receives

Three files for each stage, and nothing else:

1. `CODING_INSTRUCTIONS.md`.
2. The paper's PDF.
3. That stage's workbook, from the pack that `build_cold_pack.py` builds from
   the frozen corpus.

**No corpus file.** The blind corpus of the Carlile round is retired, and
`corpus_blind.json` goes to nobody. A workbook prints only the fields listed
for its tabs in the builder's header.

**Never sent:** the corpus or its sidecar; an earlier stage's sheet, blank or
returned; any agreement figure; the extraction's log; anything from the pack's
`key` folder.

**Never printed in any workbook:** a link's direction, basis or confidence;
`core`; `stated_as`; a gap's kind; a pair's `drawn_by_authors`, basis,
`held_comparable` or `differs_in`; the resolution period or its basis; voice;
gloss relation; `data_type`; the extraction's own confidence; and every `notes`
field. These are what is being coded, or they give it away. Any of them visible
to a coder is contamination, not agreement.

The attack bundle is cut differently, and the two are not to be confused: the
attacker loses directions and bases, and keeps `core` and `stated_as`
(`prepare_attack.py`). A coder is shown none of the coded fields.

The builder stops when a text that it would print states coder 1's answer: a
period description that says where the story closes, a pair text that says what
the paper does with the pair, a voice row that still opens with a voice cue. A
neutral text is then written to a file, with the reason recorded, and passed to
the builder.

---

## What is coded, in four stages

Ten fields, in four stages. **Each stage comes back before the next is sent.**
That is the plan's rule, and it is kept for every paper. Its first reason was
one coder's memory: every stage asks for something that a later workbook prints.
With a fresh chat for every stage that reason no longer bites. What remains is
that each return is read in and checked before the next stage goes out. Whether
stages may be sent side by side has not been decided. Until it is, they are not.

| stage | field | coded from | what rests on it |
|---|---|---|---|
| **A** | `Claim.outcome`, every claim | the claim's statement and the paper | the outcome test reads it, so every direction code rests on it |
| **A2** | `Claim.asserted_direction`, the claims that name an outcome | the claim, with the corpus's outcome printed | the other half of the pairing that decides `with` against `against` |
| **V** | `voice`, every fragment | the page, never the stub | keeps the author's interpretation out of the evidence column: the audit's voice rule |
| **B** | `ClaimLink.direction`, every link | the stub alone, never the paper | coupling uniformity, and every seam |
| **B** | `Claim.core` | the claim and the paper | `focalization_shift` fires on units beneath no core claim |
| **B** | `Claim.stated_as` | the paper's language | `counterfactual_ending` fires on a ventured claim |
| **B** | `DeclaredGap.kind` | the gap's statement and the paper | an `unresolved_question` gap fires `counterfactual_ending` |
| **B** | `ContrastPair.drawn_by_authors` | the two episodes and the paper | the strength of the licence for `construct_inversion` |
| **B** | `PaperMeta.resolution_period` | the periods and the paper | `boundary_shift` reads where the arc closes |
| **B** | `gloss_relation`, every glossed fragment | the stub, the gloss and the fragments beside it | the gloss-divergence detector, and `fragment_over_gloss` |

**All links, not only the contested ones.** Coding only the links the first
coder found difficult measures agreement on difficulty, not agreement on the
field.

**Direction is coded from the stub alone,** and the reason is written before
the code is chosen. A reason may cite only what its stub prints.

**Voice is coded from the page,** and so it is its own stage, sent before any
workbook that prints stubs. An interpretive stub opens with a voice marker,
which states the answer. Stage V prints each fragment's page and its stub with
that opening removed. The pack's key lists the rows where it was removed: a
mismatch that a coder notes there between the description and the page is the
builder's doing.

**Stage A2 prints the corpus's outcome,** not the coder's own from Stage A, and
asks which way the claim pushes it. That isolates the judgement, and it keeps
an outcome that the two coders worded with opposite signs from showing up as a
false disagreement about direction.

---

## Procedure

`<paper_id>` is the paper's id, as `bechky_2020`. Every command is run in the
folder.

1. **Freeze the corpus first,** with its sidecar: `<paper_id>_v1.json` and
   `<paper_id>_v1_voice_gloss.json`, both registered with their hashes. No
   fragment is added, split or re-stubbed once coding begins, or the two
   codings are of different objects.

2. **Build the pack, once.**

   ```
   python3 -B build_cold_pack.py <paper_id>_v1.json <the extraction log> packs/<paper_id> \
       --sidecar=<paper_id>_v1_voice_gloss.json \
       [--periods=<file.json>] [--pairs=<file.json>] [--v-descriptions=<file.json>]
   ```

   The extraction log is the one that goes with the frozen corpus. The three
   options in brackets carry the neutral texts of the section above, where the
   builder asked for them. The pack holds four workbooks in `attach/`, a SEND
   file for each stage, and a key in `key/`, which goes to no
   coder. The key records the hashes of the corpus and of the sidecar, and
   `agreement.py` later takes no other.

   **A pack is never built again after a stage has gone out.** A reply that
   comes back as text carries row ids only, and nothing in it says which pack
   it answered.

3. **The PI sends A, then A2, then V, then B,** each in a fresh chat, after the
   stage before it is back.

4. **Each stage is read in with `intake_coder2.py`.**

   ```
   python3 -B intake_coder2.py packs/<paper_id>/attach/<the stage's workbook> \
       --key=packs/<paper_id>/key/<paper_id>_pack_key.json \
       --text=reply_<paper_id>_STAGE_<X>.txt \
       --out=returned_<paper_id>_STAGE_<X>_coder2.xlsx
   ```

   A stage comes back as the text of every reply, put into one file in the
   order received, or as the workbook itself (`--workbook=` in place of
   `--text=`). Name the file for its paper and stage when it arrives, as
   above. The intake checks the return against the workbook as sent. Its
   output carries a record of its own: the paper, the stage, the workbook that
   was sent, the file the answers came in, and a digest of every cell.
   The output goes to nobody. **A returned workbook
   is never edited.** `agreement.py` reads none without that record, and
   refuses one in which a cell has changed since the intake. If a stage must
   be read in again, read it in again from what the coder returned: the intake
   does not take its own output as a coder's workbook.

   **Look at what the intake lists under CHECK BY HAND** before the stage is
   filed: rows answered more than once, a code longer than its reason, and, in
   Stages A and A2, each row where a cell that was read as `none` held more
   words.

5. **Agreement is computed when each sheet returns.**

   ```
   python3 -B agreement.py --paper <paper_id>_v1.json \
       --sidecar=<paper_id>_v1_voice_gloss.json \
       --key=packs/<paper_id>/key/<paper_id>_pack_key.json \
       --log=<PAPER>_AGREEMENT_LOG.md \
       --label="<who the two coders are>" \
       --a=returned_<paper_id>_STAGE_A_coder2.xlsx [--a2=...] [--v=...] [--b=...] \
       [--readings=<paper_id>_readings.json] [--against=<the check's results>]
   ```

   It writes the paper's agreement log from the stages that are back, and
   writes it whole again at the next stage. The log is never edited by hand:
   the same files and the same label give the same log.

   **`--label=` is the one line that says what the figures compare:** model
   against model, with the name and the setting of each coder. It is required
   for a real pack, so that no cold paper's figure goes unlabelled. The
   paper's agreement log states the line, and it is typed the same at every
   run.

6. **Two things are judged by reading,** because their wording differs between
   any two coders: whether two outcome wordings name the same thing (Stage A),
   and whether two asserted directions push the printed outcome the same way
   (Stage A2). The reader's calls go into the readings file, whose form is in
   the header of `agreement.py`. The file says who made the calls and on which
   codes. For that, run the log once without calls: its table of files gives,
   for each stage, the first sixteen digits of the digest of the workbook's
   coding tabs, and the readings file carries them under `judged_on`. The
   digest changes when a cell changes and not when a file is saved again, so a
   call stays good for the codes it was made on and is refused beside any
   others. The log prints both wordings side by side with each call, so that
   the PI can check every one.

   **How `none` is read.** In Stages A and A2 an answer counts as `none` by
   one rule, the intake's: it begins with `none`, `no outcome`, `no
   direction`, `n/a`, `na`, `null` or a hyphen. A wording that means none in
   other words is read as an outcome named. The reader can then call it
   `coder 2 means none`, wherever coder 2 names an outcome or gives a
   direction, and the log gives Stage A's figure both ways. The rule cuts the
   other way too: a cell that begins with one of those words is read as `none`
   whatever follows. The intake lists each such row when the stage is read in
   (step 4), and no call turns that reading back.

7. **The `against` check** runs once, after both codings of all papers and
   before any disagreement is discussed (`AGAINST_CHECK.md`). With fewer than
   four papers coded, when and on what it runs is the PI's to say.
   `build_against_check.py` builds its table from the frozen corpora and the
   returned Stage B workbooks, which must carry the intake's record, and reads
   the answers back. The file of results that it writes goes to `agreement.py`
   with `--against=`.

8. **The recheck:** at least ten days after a paper's Stage B returns, a sample
   of rows is coded again in a fresh session that has none of the earlier
   codes. Its builder is not written yet.

9. **Nothing is discussed until every paper is coded,** and the recheck with
   them (the last section of the coding instructions). Talking over
   one paper's disagreements would show a coder how the other reads before the
   next paper.

**Where a cold paper's second coding is recorded.** Not in the corpus: a frozen
corpus is never changed. The second coding is the four returned workbooks,
filed under the names above, for nobody. The
paper's agreement log is written from them. The audit under coder 2's coding
is computed from them by `agreement.py`; where a file of coder 2's voice and
gloss relation is wanted, `make_voice_sidecar.py` writes one from the returned
Stage V and Stage B workbooks. `CLAIM_EXTRACTION.md` says to record a second
coder in the corpus's `meta`. That was Carlile's way, in v4.4, and it does not
apply to a frozen cold corpus.

---

## Disagreement

**Disagreement is the measurement. It is not a problem to be resolved away.**

- Agreement is computed **before** any discussion. A rate computed after the
  coders, or the people who run them, have talked is a rate about the
  conversation. The script cannot know when a figure was computed: that it was
  computed first is this procedure's to ensure.
- Every disagreement is recorded with both codes and both reasons. The
  paper's agreement log does this: coder 2's reason comes from the sheet, and
  coder 1's from the corpus or the sidecar, where they record one.
- If a disagreement is later reconciled, the corpus takes the reconciled code
  **and the figure from before the reconciliation stands as the reported
  number.** Reconciliation improves the corpus. It never improves the
  statistic.
- A disagreement that survives discussion stays unresolved in the log. A field
  that two coders cannot converge on after seeing each other's reason is a
  finding about that field, and it belongs in the limitations.

---

## What may be reported

**Agreement is reported per field, never pooled.** The fields differ widely in
base rate and in scale. One figure across `direction`, with hundreds of
judgements and four values, and `resolution_period`, with one judgement, means
nothing.

**Every figure is labelled for what it compares.**

- On Carlile the corpus's codes were made by a model session. A figure that
  sets the corpus, or the blind session, beside the human coder is
  human against model. Human-against-model agreement is reportable, labelled
  as such. The two figures that set the corpus beside the blind session have a
  model on both sides.
- On the cold papers both coders are models, so every cold-paper figure
  is **model against model**. Such a figure is reportable, labelled as model
  against model, with the limitation stated beside it (fixed on 7 Oct 2026).
  The limitation is this. Agreement between two models is
  not agreement between two people, and either model may have read the paper
  in training, so its codes are not independent of the paper in the way a
  naive reader's would be.
- A paper's agreement log carries its label on its first page (step 5).

**Kappa on the cold papers is withheld by count only:** for a field with fewer
than ten comparable judgements. Such a field gets raw agreement with the
denominator printed. A kappa is also reported as undefined when both coders use
one and the same code throughout. So `stated_as` and `gloss_relation` get a
kappa wherever a paper has ten rows or more, and the resolution period, one
judgement a paper, never does. This rule was fixed on 7 Oct 2026, before any
sheet of a cold paper had come back. A kappa on three instances is noise with a
Greek letter on it.

Carlile's logs follow an older rule, which the script still applies to
Carlile: no kappa for `stated_as`, `resolution_period` and `gloss_relation` at
any size, and none under ten judgements. The three fields were named on
Carlile's scale: one ventured claim, one judgement, three glosses. The
appendix has to say that the two rules differ.

**A kappa that is given comes with a 95% interval,** on the cold papers: 2,000
resamples of the rows, as in the link tests. A resample in which both coders
use one code throughout has no kappa and is left out, and the log says how
many resamples gave one whenever some did not. The log carries two cautions.
The ends of an interval move with the seed, and more where a field has few
rows: on made-up tables by about a hundredth at some hundreds of rows, by a
few hundredths at about fifty, and by as much as 0.14 at ten to fifteen.
And rows are resampled one by one, though links cluster by claim and by
fragment, so the interval for direction is likely too narrow.

**Direction** is reported for all comparable links and again for the links on
directional claims, which carry both an outcome and an asserted direction.
`with` or `against` on a claim that is not directional is counted and listed as
invalid by schema. Such an `against` is left out of the counts of `against`
and given in a row of its own.

**Asserted direction is judged on sign,** and outcome on whether a claim is
directional or not. The wording of either is never scored: it is set side by
side and read.

**Results that rest on `against` are reported twice** once the `against` check
has run: with all `against` links, and with the links that check flags counted
as `illustrates`. In a paper's log the counts of `against` and the audit are
given both ways. The agreement on direction is not: it stands as coded.

**What a paper's log holds,** per coding where it applies: uniformity coverage
under the outcome test; `against` codes, and whether any claim reaches two;
glosses and their relation; the moves parameterised; agreement per field. It
holds a little more than that list: the uniformity rate where coverage allows
one, the links counted and those left out by the voice rule, and a cross table
for each field. The rest of what the plan reports per paper is kept elsewhere:
the pinned predictions and how they fared, in no file; the extraction's miss
rate, from the coverage check; and the hours.

**Until a field is double-coded, nothing resting on it is reportable:**

- no seam, and no coupling uniformity rate, without `direction`;
- no `focalization_shift` result without `core`;
- no `counterfactual_ending` result without `stated_as` and `DeclaredGap.kind`;
- no `construct_inversion` licence claim without `drawn_by_authors`;
- no `boundary_shift` result without `resolution_period`;
- no gloss-divergence rate, and no `fragment_over_gloss` result, without
  `gloss_relation`.

A reading generated from a single-coded trigger may still be written, attacked
and learned from. It may not carry a number into a paper.

---

## Carlile 2002: the protocol as it was applied

Carlile was coded before the cold-paper protocol existed. Its five agreement
logs rest on this page as it then stood and on how the round was run. Where
the two differ, it is said below.

- **The second coder was a person** (24 and 25 Sep), told the general purpose
  and nothing else. A model was barred from coding: "Any number reported is a
  number about human coders." That rule went when a model became coder 2.
- **She received** the paper, a blind corpus with every coded field stripped,
  the coding instructions (now `CODING_INSTRUCTIONS_carlile.md`) and blank
  sheets. That is how it was done: `build_second_coder_pack.py` built them,
  and left `CLAIM_EXTRACTION.md` out on purpose. The page then still named
  `CLAIM_EXTRACTION.md` as what she would read.
- **The stages were A, A2 and B,** with voice as the last tab of Stage B. The
  voice tab printed stubs from the pre-rewrite corpus (v4.3), because seven
  v4.4 stubs carry voice markers. Tabs 1 and 7 of that workbook still printed
  the marked stubs, which is why voice is now a stage of its own.
- **The small-n rule** of the page then: raw agreement with the denominator
  for `stated_as`, `resolution_period` and `gloss_relation`, never a kappa.
  That no kappa is given where every judgement falls in one category is not
  the page's rule: it is the reading of `STAGE_A2_DIRECTION_LOG.md`.
  `T6_RECODE_LOG.md` prints a kappa for `stated_as` all the same, against the
  page's rule; the script withholds it.
- **A disagreement log ships with the corpus:** `DISAGREEMENT_LOG.md`.
- **The blind session was a model.** Its kappa of 0.686 against the human
  coder was at first held to be unreportable under the rule above, and was
  later reported, labelled as human against model.

`agreement.py --selftest` reproduced those logs' figures for direction, core
and outcome (here it is a stub: Carlile's files are not here). Run on the four
returned sheets,
`agreement.py` gives the raw agreement of the other fields. It does not give
everything else: it withholds the two kappas that `T6_RECODE_LOG.md` prints
for `stated_as`, and round 1's figures for the other fields cannot be made
again, because the round-1 sheet was not kept. Asserted direction was
judged by reading.

---

## What a second coding does not fix

It measures whether two coders apply a definition the same way. It cannot tell
you that the definition is worth applying. A field that both coders assign
identically, and that turns out to gate nothing, is a reliable measurement of
nothing.

It also cannot repair **coverage**. A claim is assessed only when it has
enough directional links, and a second coder does not add links. Perfect
agreement on `direction` would leave a paper-level rate withheld exactly as it
is withheld today.

And it does not test the link itself. Both codings of direction are made on
the links that the extraction drew, under brief v2's rule. Two tests of a
sharper definition of a link did not pass (`LINK_TEST_RESULT.md`,
`LINK_TEST2_RESULT.md`), and nothing is coded under either.
