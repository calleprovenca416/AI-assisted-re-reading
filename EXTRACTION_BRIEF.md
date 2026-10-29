# Extraction brief

*Version 2, 27 September 2026. One extraction session per paper. The changes
from version 1 are listed at the end.*

You are recording one published qualitative research paper as structured data:
the evidence it prints, the claims it makes, and how the two connect. This is
part of a study of how qualitative papers arrange their evidence. You will work
from the attached PDF and nothing else.

The work has six passes, 0 to 5. Do them in order. When a pass is done, update
the three files, say in a few lines what the pass added, and stop. Wait for the
word **continue** before starting the next.

---

## Four rules

1. **Only this PDF.** Do not search the web. If you recognise the paper or its
   author, set aside everything you know from elsewhere — how it has been cited,
   summarised or criticised, the author's other work. Everything you record must
   be traceable to a page of this PDF.
2. **Your words, never the paper's.** Every stub, statement, gloss and basis is
   written in your own words. Do not copy sentences or phrases from the paper.
   The exceptions are names and labels the paper itself prints: pseudonyms, and
   the paper's own terms for its codes, themes and constructs. This applies to
   claim statements as much as to stubs, and it is hardest there: restate a
   claim in a sentence of your own rather than editing the paper's sentence.
   Every text field will be checked mechanically against the paper's text.
3. **Record what is printed; do not improve it.** Do not supply facts the paper
   does not print, repair gaps in its account, or settle ambiguities it leaves
   open. Where the paper is unclear, record it as unclear.
4. **Do not ask what any field is used for.** Some fields feed later steps, and
   knowing which answer leads where can tilt a borderline call without your
   noticing. Code what the definitions below say.

Two habits throughout. **Over-collect**: a fragment or claim you are unsure about
is better recorded with low confidence than dropped. And **write the reason
before you choose a code**: it is easy to pick a code and then justify it; the
reverse is harder and more honest.

---

## What you produce

Three files, named with the `paper_id` given in the opening message:

| file | contents |
|---|---|
| `<paper_id>_corpus.json` | the record, in the format at the end of this brief |
| `<paper_id>_voice_gloss.json` | two judgements per fragment, made in pass 4 |
| `<paper_id>_extraction_log.md` | the section map, the checks from pass 5, and the close calls |

Create the three files in pass 0 and keep them as files. After every pass,
update them with code and make all three available to download: the person
running the session saves them after each pass. Do not print their contents in
the chat, and do not build a page or viewer around them. The chat carries only
your short account of each pass.

If you cannot create files, output each pass as JSON in code blocks labelled with
the file and the part (for example `<paper_id>_corpus.json — fragments F01–F30`),
in batches of about 30 records per block.

**Page references** use the page numbers printed on the journal pages (for
example "p. 471"), not the PDF viewer's count. Add the section heading where it
helps ("Findings — Recruiting, p. 471"). For tables and figures: "Table 2, row 4,
p. 480".

---

## Pass 0 — Read and orient

Read the whole paper before recording anything: abstract to endnotes, including
tables, figures, footnotes and appendices.

Then fill the `meta` object and write the section map (each section heading with
its page range) into the log.

- `paper_id`, `citation`: exactly as given in the opening message.
- `periods`: the story's coarse phases, in order, as the paper itself divides
  time — usually three to six, labelled "P1", "P2", … Describe each in one line
  in the log. If the paper places some events before its story begins — an
  earlier attempt, last year's project — put a period "P0" first, for those
  events only. If the paper tells no story in time (for example, it describes an
  ongoing practice), use a single period "P1", give every fragment "P1", and say
  so in the log.
- `episode_start_period`: "P1", the period in which the story begins.
- `fieldwork_scale`: what the methods section says about the data — duration,
  sites, interviews, hours of observation, documents — in your words.
- `schema_version`: 4. `claim_layer_status`: "extracted". `second_coder`: null.
  `double_coded_fields`: []. `claim_layer_basis`: "Extracted in one session from
  the PDF under the extraction brief, version 2."
- Leave `resolution_period`, `resolution_basis`,
  `reports_outcome_after_resolution` and `printed_fragment_count` for later
  passes.

---

## Pass 1 — Fragments: the evidence the paper prints

A **fragment** is one piece of evidence the paper prints: one reported event, one
quoted utterance, one described observation, one field-note excerpt, one archival
item, one table cell that reports data. Where one event is narrated across two or
three sentences, it is one fragment; where one paragraph reports three distinct
events, it is three.

**An event's condition and its result are one fragment.** When the paper
narrates what led to something together with what came of it — a meeting and
what it decided, an argument and how it was received — both go in the same stub.
Do not split one event into a fragment for its cause and another for its result.

Seek fragments **throughout** the paper, not only in the findings. Introductions
often open with a vignette. A table of illustrative quotations is evidence: each
printed quotation or data cell in it is its own fragment. Footnotes can carry
evidence too.

Number fragments F01, F02, … in the order they appear.

| field | what goes in it |
|---|---|
| `fragment_id` | F01, F02, … |
| `stub` | what the fragment reports, in your words, in one sentence: who, what, when, as printed. See **Keeping the author's voice**, below |
| `text` | null, with `text_status` "withheld" |
| `data_type` | the channel through which the evidence was collected: `individual_interview`, `group_interview`, `meeting_transcript`, `quoted_speech_in_situ` (something said in the setting, recorded as it happened), `observation`, `field_note`, `archival`, `authorial_vignette` (a scene narrated by the author), or `unspecified` |
| `unit` | who is speaking or acting, as a group: an occupation, function, role or site. Choose one level for the whole paper — the level the paper itself uses to tell groups apart — and keep to it |
| `speaker_name` | the pseudonym, where the paper gives one; otherwise null |
| `period` | the one period, from `periods`, in which the **event described** happened — not when it was told. A fragment that spans periods gets the period of the event it centres on; note the span in `notes`. null when the paper tells a story but does not place this event in its time: the setting, a practice described in general, a vignette the paper never places against the story. Do not default to the first period |
| `author_code` | the paper's own label for this material, where it prints one (a code, theme or category name); otherwise null |
| `author_gloss` | the author's own summary of what **this one fragment** shows, where the author gives one, in your words; otherwise null. Keep it out of the stub |
| `citing_claims` | [] for now; filled in pass 3 |
| `location` | page, and table or figure cell where relevant |
| `extraction_confidence` | `high`, `medium` or `low`: how sure you are that the stub records what is printed |
| `notes` | provenance, for example "one of three quotations in Table 2, row 1", and the span where a fragment spans periods; otherwise null |

**Keeping the author's voice in the stub.** Paraphrase keeps content and loses
voice. If a sentence in which the author interprets — "for these workers, X was
a way of showing Y" — is paraphrased as "X showed Y", the result reads as a
report of fact. So where the source sentence is the author interpreting rather
than reporting, the stub opens with one of these markers, exactly as written:

- *the author's account is that …*
- *the paper explains that …*
- *for the author, …*

How to tell whether a sentence is the author interpreting: the test in pass 4.

**Stub versus gloss.** When the author characterises one specific reported
fragment ("this exchange shows that …"), that characterisation goes in the
fragment's `author_gloss` — not in its stub, and not as a fragment of its own.
When the author's interpretation spans several events, it is a fragment of its
own, and its stub carries a marker.

This holds wherever in the paper the characterisation appears. A later section
that returns to one printed event and reads it again — in the analysis, the
discussion or the conclusion — adds to that event's `author_gloss`; it is not a
new fragment. If the author characterises the same event in more than one
place, the gloss holds each part with its page, in the form "(p. N) …; (p. M) …".
A sentence that both reports and interprets is split: what happened goes in the
stub, and the author's reading of it goes in the gloss. Such a fragment is a
report, and its stub carries no marker (see the voice test in pass 4).

At the end of pass 1, set `printed_fragment_count` in `meta` to the number of
fragments.

---

## Pass 2 — Claims: what the paper asserts

A **claim** is something the paper asserts, in its own voice, about how
something works.

**Authorial commitment, not location.** Seek claims throughout the paper:
introduction, theory sections, findings, discussion, conclusion. A claim found in
the middle of the findings is still a claim. Claims cluster in these places, but
they are not confined to them: the abstract, sentence by sentence; the end of
each findings section, where the paper says what the section showed; the
discussion; any numbered propositions; the conclusion.

**The attribution test.** For a sentence in a literature review or theory
section, ask whether the paper is reporting what someone else holds, or asserting
it in its own voice. Only the second is a claim. Where the paper endorses another
author's position and builds on it, it is asserting it: record it as a claim and
note the attribution in `notes`.

Over-collect distinct claims. A claim with nothing beneath it is still worth
recording.

**One claim per relation.** A paper states its main claims more than once — in
the abstract, the introduction, after each findings section, in the conclusion —
and a restatement is not a new claim. Before recording a claim, check the claims
already recorded. If one asserts the same relation — the same condition, the
same outcome and the same sign — the new sentence restates it: add the new page
to that claim's `location`, and keep whichever wording is more general. A
different condition or a different outcome makes a new claim. For claims with no
outcome, a sentence that restates, illustrates or spells out a step of a
recorded claim is not a new claim. The aim is to draw the line where the paper
draws it: neither split one relation into several claims nor merge two into one.

Number claims C01, C02, … in the order they first appear.

| field | what goes in it |
|---|---|
| `claim_id` | C01, C02, … |
| `statement` | the claim in your words, in one or two sentences, stated plainly: how firmly the paper puts it goes in `stated_as`, not in the statement |
| `constructs` | the named things it is about — the paper's own construct names where it has them |
| `outcome` | see **Outcome**; null if the claim names nothing that varies |
| `asserted_direction` | see **Asserted direction**; null whenever `outcome` is null |
| `core` | true or false; see **Core** |
| `stated_as` | "established" or "ventured"; see **Stated as** |
| `location` | page |
| `decomposed_into` | the named sub-types, only if the paper itself splits the construct into kinds; otherwise [] |
| `extraction_confidence` | `high`, `medium` or `low` |
| `notes` | attribution or provenance; why a claim that names something that varies has no direction; the places where a claim stated more than once is hedged. Otherwise null |

**Outcome.** What does the claim say gets affected? Write it as a short noun
phrase — the thing that varies. *Time taken to reach a decision. Conflict
between two teams. Staff turnover.* Not a sentence, not the claim restated. If
the claim names nothing that varies, the outcome is null: plenty of claims
describe how something is rather than assert that one thing affects another, and
null is the right answer for those. Do not manufacture an outcome to fill the
field. Two claims can share an outcome.

**Asserted direction.** Given that outcome, which way does the claim say it
goes? Write it as a short conditional: *the more X, the harder Y*; *more A leads
to more B*; *when Z is present, W becomes possible*. Say plainly whether the
outcome goes up or down: "affects the time taken" is not a direction; "the more
people must sign off, the longer the decision takes" is. Keep the outcome's
polarity as you phrased it: if the outcome is a difficulty and the claim makes
things easier, write *less difficulty* rather than rewriting the outcome as ease.
If a claim names something that varies but asserts no direction on it — it says
the thing matters, not which way it goes — set both `outcome` and
`asserted_direction` to null and say why in `notes`.

**Core.** Does this claim carry the paper's contribution? true if the paper would
lose its argument without it; false if it is scaffolding, background, or a step
on the way to something else. A paper usually has a handful of core claims, not
one and not all of them. Do not aim for any particular number.

**Stated as.** How firmly does the paper put this claim? `established`: asserted
as something the paper has shown. `ventured`: hedged, offered, proposed,
suggested as worth considering. Judge the paper's language, not whether you find
the claim convincing. Watch for hedging that is only stylistic modesty, and for
confident phrasing around a claim the evidence does not really reach — both
directions of mismatch occur, and you are coding the phrasing. Where a claim is
stated in more than one place, code its firmest statement, and note the hedged
places.

**Before you stop.** Read down the whole claim list once more for any two claims
that assert the same relation, and for any claim with no outcome that restates,
illustrates or spells out a step of another. Merge each one you find. Two claims
that assert the same relation become the lower-numbered one, with whichever
wording is more general. A claim that restates, illustrates or spells out a step
of another becomes part of that other claim. Either way, the kept claim keeps
its number, its `outcome` and its `asserted_direction`; add the other claim's
pages to its `location`, keep the union of `constructs`, and judge `core` and
`stated_as` again. List the merges in the log. A merged claim's number is not
reused.

---

## Pass 3 — Links, pairs, gaps, absences, and the ending

### Links

Attach each fragment to every claim it bears on: the broad claim as well as the
narrow one. When a fragment bears on a narrow claim, check whether it also bears
on the broader claim the narrow one belongs to; if it does, link both. A
repeated illustration is still a link: if ten fragments illustrate one claim,
all ten are linked to it. A fragment can sit under several claims, and some
under none. Record each attachment as a link, and add the claim's id to the
fragment's `citing_claims`.

For every link, decide its **direction** by this test.

> **Direction in two steps. Read the claim's outcome first.**
>
> 1. **Does the stub report anything about the outcome itself?** If it reports
>    the setting, or the conditions, or the general phenomenon, but says nothing
>    about the outcome itself → `illustrates`, however well the fragment fits the
>    claim's subject matter. If this step is genuinely unclear, write the
>    tie-breaker below into the basis and code from it.
> 2. **If it does, which way did the outcome go?** The way the asserted
>    direction says → `with`. The opposite way, **or** the outcome occurred
>    without the condition the claim names as its cause → `against`. The stub
>    explicitly bounds or limits the claim → `qualifies`. The stub need not show
>    the condition: an outcome going the asserted way, with nothing said about
>    why, → `with`.
>
> Keep the outcome's polarity as it is; do not re-sign it.

**Claims with no outcome** have no direction to run: their links are
`illustrates` or `qualifies`, never `with` or `against`.

**The second half of `against`** is easy to miss, and it matters. A claim saying
*time pressure makes cooks skip the tasting step* is run against by a stub
showing a cook skipping the tasting step on a slow afternoon with no orders
waiting. The outcome is present, and the stub shows the named cause absent. It
is run against, too, by a stub in which a cook skips the step because the recipe
card has gone missing: the stub puts the outcome down to another cause.

**An outcome without its cause.** Had that stub said nothing about how busy the
kitchen was, or about why the step was skipped, the code would be `with`: the
outcome went the asserted way, and nothing in the stub shows it happening
without the cause. The second half of `against` needs a stub that shows the
condition absent, or that puts the outcome down to another cause and not to the
condition. An absence you would have to infer does not count.

**The tie-breaker.** When step 1 is genuinely unclear, write in the basis: *if
this claim were false, this stub would instead say ___.* If you cannot complete
the sentence, or it comes out the same as what the stub already says, the answer
is `illustrates`.

**Code from the stub, not from the paper.** Direction is judged on what the stub
records. This is deliberate, and it is the opposite of the rule for voice. If the
stub does not carry what you need, that is itself a finding: code what the stub
supports (unless the missing fact belongs to the same event: see **The basis**).

**The basis.** Every link has a one-line `basis`, written before you choose the
code. The basis may cite only what the fragment's stub says — not the
neighbouring fragment, not the surrounding paragraph, not what you know about how
organisations work, not an inference. If a direction needs a fact the stub does
not carry, check whether the paper prints that fact. If it belongs to the same
event, the stub is incomplete: add the fact to the stub, check the fragment's
other links against the new stub, and log the change with the link it was made
for. If it belongs to another event, that event is its own fragment, with the
next free number and its own link. If the paper does not print it, the direction
does not stand.

`against` is narrow. It does not mean "this is interesting" or "this also points
somewhere else". Most fragments will not be `against`, and that is expected.

Give each link a `confidence`: `high`, `medium` or `low`.

### Contrast pairs

Two episodes that are comparable on the page and came out differently, whether
or not the paper itself sets them side by side. Record a pair the paper does not
draw only where the page prints what makes the two comparable; do not assemble
one from your own sense of a telling comparison.

| field | what goes in it |
|---|---|
| `pair_id` | CP01, CP02, … |
| `episode_a`, `episode_b` | the two episodes, in your words |
| `held_comparable` | what makes them comparable, from what the page prints about each |
| `differs_in` | what differed between them |
| `fragments_a`, `fragments_b` | the fragment ids on each side; each side needs at least one |
| `drawn_by_authors` | true if the paper itself puts the two side by side and treats the contrast as meaningful; false if both episodes appear but the paper never compares them. The test is whether the comparison is on the page, not whether it is a reasonable comparison to make |
| `basis` | one line: what the page prints that makes this a pair — facts only |

### Declared gaps

Limits the paper states **about itself**, usually in a limitations section or the
discussion.

| field | what goes in it |
|---|---|
| `gap_id` | DG01, DG02, … |
| `statement` | the limit, in your words |
| `kind` | `scope_limit` (the paper says what it does not cover), `absent_evidence` (it says it lacks some evidence), `unresolved_question` (it names a question it leaves open), `acknowledged_ambiguity` (it says something is unclear or could be read two ways), `vocabulary_mismatch` (it says a term is used differently elsewhere) |
| `location` | page |
| `bears_on` | the claim ids it limits |

Some gaps sit between two kinds. Pick one, and say in the log which other kind
you considered and why you rejected it.

### Absences

Evidence the paper does not contain that bears on one of its claims, where the
page itself makes the absence visible: a group that appears in the story but is
never quoted or observed; data the methods section says were collected but that
are not shown; a point in the story the paper passes over.

| field | what goes in it |
|---|---|
| `absence_id` | A01, A02, … |
| `kind` | `not_collected`, `collected_not_printed` or `not_ascertainable` |
| `evidence_class` | what is missing, in a few words |
| `basis` | one line: what the page prints and what it does not — facts only |
| `bears_on` | claim ids |
| `source` | "extraction" |

Record absences only where the page shows them. Do not speculate about what the
study might have done.

### The ending

In which period does the paper's story close — the point after which it treats
the matter as settled? Set `meta.resolution_period`, and put what on the page
marks the ending in `meta.resolution_basis`. If the paper reports what happened
after that point, set `meta.reports_outcome_after_resolution` to true; otherwise
false. If you think the story does not close, leave `resolution_period` null and
say why in `resolution_basis`.

---

## Pass 4 — Voice and gloss relation

Two judgements, recorded in `<paper_id>_voice_gloss.json`, not in the corpus.
Each entry gets a one-line reason.

**Voice — for every fragment.** Is this fragment the paper **reporting**, or the
author **interpreting**?

| code | means |
|---|---|
| `reported` | the paper shows you something that happened, was said, or was the case |
| `author_insight` | the author's own interpretation of what was going on |

**Code this from the page, not from the stub.** Go to the location, find the
sentence, and code what the author wrote. This is the opposite of the rule for
direction, and the reversal is deliberate: voice is a fact about the original
sentence, and a stub cannot carry it reliably.

**The test.** If the sentence is the author's own words rather than a report of
what someone did or said, ask: can you point to the single reported event this
sentence characterises?

- If yes, it is a summary of that one event and belongs with it: `reported`.
  This holds even when the sentence also explains why that event went as it
  did, or says what it meant to the people in it: that part is the event's
  gloss.
- If no — it interprets across several events, or explains why something
  happened, or states what something meant — `author_insight`.

Most fragments will be `reported`. An author's explanation of why people behaved
as they did, across several events, is the clearest case of `author_insight`. So
is a sentence saying what an object meant or was worth to people in general. A
table or figure summarising the author's framework is usually `author_insight`
too. Where a sentence reports the reasoning of people in the setting across
several events, in the author's own voice and without quoting anyone, it is
genuinely ambiguous: code your best judgement and flag it. About one event, it
is `reported`, as above.

If a voice code does not match the stub — an `author_insight` fragment whose stub
has no marker, or a `reported` fragment whose stub has one — correct the stub in
the corpus and note the correction in the log.

**Gloss relation — for every fragment with an `author_gloss`.** How does the
author's summary sit against what the fragment reports?

| code | means |
|---|---|
| `consistent` | the summary says what the fragment supports, no more |
| `goes_beyond` | the summary adds something the fragment does not carry, without contradicting it |
| `diverges` | the summary and the fragment point different ways |
| `none` | no relation worth recording |

The distinction that matters is `goes_beyond` against `diverges`. Ask: could both
be true at once? If yes, it is `goes_beyond`. If believing the summary means
disbelieving part of the fragment, it is `diverges`. Read the neighbouring
fragments from the same episode, not only the one glossed: the relation may be
to one of them, especially where one event has ended up in more than one
fragment. If the gloss has more than one part, code the part that departs
furthest from what the fragment reports (`diverges` before `goes_beyond` before
`consistent`), and name that part in the reason.

---

## Pass 5 — Checks, and the final files

1. **Coverage sweep.** Walk the paper section by section. For each stretch of
   empirical prose that produced no fragment, and each stretch of assertion that
   produced no claim, either extract what you missed or say in the log why it is
   not evidence or not a claim. Silent stretches are either genuinely
   non-evidentiary or a miss; footnotes, table notes and figure captions are
   where misses hide. Anything you add now gets the next free number and every
   field, as in passes 1 to 4: its links, and for a fragment its voice and,
   where it has a gloss, its gloss relation. Update `printed_fragment_count`.
2. **One claim per relation.** Repeat the check from the end of pass 2. Merge any
   pair you find as described there, and move the merged claim's links and its
   ids in `citing_claims` and `bears_on` to the kept claim; where a fragment was
   linked to both, keep one link, with its direction coded against the kept
   claim. Log each merge.
3. **Claim closure.** List the claims with no fragments beneath them and the
   fragments attached to no claim. Both can be real properties of a paper. Do not
   force links to shorten either list. Record both lists in the log.
4. **Core claims with nothing beneath them.** For each core claim on that list,
   go through all the fragments once more, asking of each whether it bears on
   that claim. Link those that do, coding direction in the usual way. List in the
   log each link this step adds, or "none found" for the claim.
5. **Consistency.** Every id is unique. Every period that is not null is in
   `periods`. Every link names an existing fragment and claim, and every id in
   `citing_claims` and `bears_on` exists. `with` and `against` appear only on
   claims that have both an outcome and an asserted direction. Every claim with
   an outcome has an asserted direction. Every contrast pair has fragments on
   both sides and a basis. Every gap has a location. Every absence has a basis.
   Every fragment has one voice code, and every fragment with a gloss has a gloss
   relation. No stub, statement, gloss or basis copies the paper's wording.
6. **The log.** Counts — fragments; claims; links by direction; pairs; gaps;
   absences; voice codes; gloss relations. The section map and periods from pass
   0. The coverage and closure lists, and the links the core-claim step added.
   The claim merges from passes 2 and 5. The stub corrections from pass 4. And
   the close calls: the judgements you found hardest, each with one line on what
   made it hard.

Then finalise the three files.

---

## When you are unsure

Code your best judgement and say what made it hard, in the relevant `notes`
field or in the log. Never leave a required field empty, and never invent a code
that is not on the list. If you find yourself wanting a code that does not
exist, record the one you would have used in the log: it usually means the
scheme is missing something.

---

## Format

`<paper_id>_corpus.json` — one object with seven keys. Every record carries the
`paper_id`. Values in angle brackets are placeholders; lists of allowed values
are given as `a | b | c`.

```json
{
  "meta": {
    "paper_id": "<as given>",
    "citation": "<as given>",
    "periods": ["P1", "P2", "P3"],
    "episode_start_period": "P1",
    "resolution_period": "<a period, or null>",
    "resolution_basis": "<what on the page marks the ending>",
    "reports_outcome_after_resolution": false,
    "fieldwork_scale": "<duration, sites, interviews, observation, documents>",
    "printed_fragment_count": 0,
    "schema_version": 4,
    "claim_layer_status": "extracted",
    "claim_layer_basis": "Extracted in one session from the PDF under the extraction brief, version 2.",
    "second_coder": null,
    "double_coded_fields": []
  },
  "fragments": [
    {
      "paper_id": "<as given>",
      "fragment_id": "F01",
      "stub": "<one sentence, your words>",
      "text": null,
      "text_status": "withheld",
      "data_type": "individual_interview | group_interview | meeting_transcript | quoted_speech_in_situ | observation | field_note | archival | authorial_vignette | unspecified",
      "unit": "<group>",
      "speaker_name": null,
      "period": "<a period, or null>",
      "author_code": null,
      "author_gloss": null,
      "citing_claims": ["C01"],
      "location": "p. 000",
      "extraction_confidence": "high | medium | low",
      "notes": null
    }
  ],
  "claims": [
    {
      "paper_id": "<as given>",
      "claim_id": "C01",
      "statement": "<one or two sentences, your words>",
      "constructs": ["<construct>"],
      "outcome": "<noun phrase, or null>",
      "asserted_direction": "<short conditional, or null>",
      "core": false,
      "stated_as": "established | ventured",
      "location": "p. 000",
      "decomposed_into": [],
      "extraction_confidence": "high | medium | low",
      "notes": null
    }
  ],
  "claim_links": [
    {
      "paper_id": "<as given>",
      "fragment_id": "F01",
      "claim_id": "C01",
      "direction": "with | against | illustrates | qualifies",
      "basis": "<one line, citing only what the stub says>",
      "confidence": "high | medium | low"
    }
  ],
  "contrast_pairs": [
    {
      "paper_id": "<as given>",
      "pair_id": "CP01",
      "episode_a": "<episode>",
      "episode_b": "<episode>",
      "held_comparable": "<what makes them comparable>",
      "differs_in": "<what differed>",
      "fragments_a": ["F01"],
      "fragments_b": ["F02"],
      "basis": "<what the page prints>",
      "drawn_by_authors": true
    }
  ],
  "declared_gaps": [
    {
      "paper_id": "<as given>",
      "gap_id": "DG01",
      "statement": "<the limit, your words>",
      "kind": "scope_limit | absent_evidence | unresolved_question | acknowledged_ambiguity | vocabulary_mismatch",
      "location": "p. 000",
      "bears_on": ["C01"]
    }
  ],
  "absences": [
    {
      "paper_id": "<as given>",
      "absence_id": "A01",
      "kind": "not_collected | collected_not_printed | not_ascertainable",
      "evidence_class": "<what is missing>",
      "basis": "<what is printed and what is not>",
      "bears_on": ["C01"],
      "source": "extraction"
    }
  ]
}
```

`<paper_id>_voice_gloss.json`:

```json
{
  "paper_id": "<as given>",
  "voice": [
    {"fragment_id": "F01", "code": "reported | author_insight", "reason": "<one line>"}
  ],
  "gloss_relation": [
    {"fragment_id": "F07", "code": "consistent | goes_beyond | diverges | none", "reason": "<one line>"}
  ]
}
```

Use `null`, `true` and `false` as JSON values, not as strings. An empty list is
`[]`.

---

## Changes from version 1

Version 1 (26 September) was run once, to test the brief. Version 2 makes
explicit what version 1 intended, settles five points it left open, adds two
rules, and changes how the files are kept.

**Made explicit**

1. **One event, one fragment.** An event's condition and its result go in one
   fragment. A fact that a direction needs, if it belongs to the same event, is
   added to the stub (passes 1 and 3).
2. **Links.** Link each fragment to every claim it bears on, the broad claim as
   well as the narrow one; a repeated illustration is still a link (pass 3).
3. **Core claims.** A core claim with no fragment beneath it gets one more pass
   through all the fragments, and the links that pass adds are logged (pass 5).
4. **Stub versus gloss, everywhere.** A later re-reading of one printed event
   goes in that event's gloss, and a sentence that both reports and interprets
   is split between stub and gloss (pass 1).
5. **Periods.** "P0" holds events the paper places before its story. Material
   the paper does not place in its story's time has no period. A fragment that
   spans periods takes the period of the event it centres on. A paper with no
   story in time puts every fragment in "P1" (passes 0 and 1).
6. **Wording.** Rule 2 covers claim statements as much as stubs, and every text
   field is checked mechanically. A statement is put plainly; how firmly the
   paper puts it goes in `stated_as`.
7. **Pass 5.** Anything added in the coverage sweep gets every field, voice
   included, and claims are merged before the closure lists are made.
8. **Contrast pairs** are recorded whether or not the paper itself sets the two
   episodes side by side, but only where the page prints what makes them
   comparable (pass 3).
9. **Files.** The three files are kept as files and updated with code, with no
   page around them and no re-printing in the chat.

**Settled**

10. **An outcome without its cause.** A stub that shows the outcome going the
    asserted way is `with`, whether or not it shows the claim's condition. The
    second half of `against` needs the condition shown absent, or the outcome put
    down to another cause; an absence you would have to infer does not count
    (pass 3).
11. **Voice for a sentence about one event.** It is `reported` even when it also
    explains the event; the explanation is the event's gloss. The case left
    ambiguous is people's reasoning across several events (passes 1 and 4).
12. **`stated_as` for a claim stated in more than one place** follows its
    firmest statement (pass 2).
13. **Voice is decided by the test in pass 4 alone** (pass 1).
14. **Examples.** The examples for outcome, asserted direction, the author's
    voice and the second half of `against` are invented.

**New rules**

15. **One claim per relation.** A sentence that asserts the same relation as a
    recorded claim — the same condition, outcome and sign — adds its page to that
    claim. Checked at the end of pass 2 and again in pass 5.
16. **A gloss in more than one part** is coded on the part that departs furthest
    from what the fragment reports (pass 4).
