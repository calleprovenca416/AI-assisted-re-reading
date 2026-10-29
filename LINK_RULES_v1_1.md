# Linking rules, version 1.1

*29 September 2026. Supersedes version 1 (`LINK_RULES_v1.md`), which was
found open on five points before any coder saw it; the changes
are listed at the end. Written in full, and reviewed twice, before the test pairs
are drawn again; `link_test_freeze.json` and `link_test_key.json` record the
order. Who may receive this file: nobody (—). Part A is sent to coders word for word inside
`LINK_TEST_NEW.md`; Part B never is.*

Brief v2 asks one question of every fragment–claim pair: does the fragment bear on
the claim, and which way does it run? It never defines "bears on", its direction
box gives one code to cases that fit a claim and to cases that run against it, and
a claim has an outcome but no condition and no kind. These rules split the one
question into separate judgments, each defined, and take direction out of the
coder's hands:

- for each claim, its **condition**, pinned to the printed direction, and its
  **form**;
- **what the stub shows** of the claim's condition and outcome, judged on the stub
  alone;
- **what kind of passage** it is, a report or the author's reading, judged on the
  paper;
- **how the paper uses the passage** for the claim, judged on the paper: the
  author's own link.

The code (`with`, `against`, `illustrates`, `qualifies`, or no link) is then
derived from the stub observations by a fixed table for the claim's form (Part B).
Coders never see that table.

---

## Part A — the rules as coders receive them

### What you are looking at

You have a table drawn from a published qualitative research paper, and, for some
of the judgments, the paper itself. The table lists some of the paper's
**claims**: things the paper asserts, in its own voice, about how something works.
Each claim is printed with its statement, the page or pages where the paper makes
it, its **outcome** (what the claim says gets affected, or `none`) and its
**asserted direction** (which way the claim says the outcome goes).

The table also lists **pairs**. Each pair joins one claim to one **fragment**: a
piece of evidence the paper prints, such as an event, a quotation, an observation
or a table cell, summarised in a short **stub**, with the page where it appears.
Fragments carry labels such as K07, and one fragment can appear in several pairs.
Someone else wrote the claim statements, outcomes, directions and stubs. Take them
as given, and make the judgments the rules below ask for.

The pairs were drawn from the paper for this exercise. Some join a passage and a
claim that the paper connects, and some do not. Do not assume either.

### Four rules

1. **Only this paper.** Do not search the web. If you recognise the paper or its
   author, set aside everything you know from elsewhere.
2. **Code what the definitions say.** Do not ask what any answer is used for.
   Knowing which answer leads where can tilt a borderline call without your
   noticing.
3. **Write the reason before you choose the code.** It is easy to pick a code and
   then justify it; the reverse is harder and more honest.
4. **When a case is genuinely unclear,** give your best answer and add `| unclear`
   at the end of its line.

### Each claim: its condition and its form

For every claim in the table, record two things. Work from the claim's statement,
outcome and asserted direction as printed. Where they seem not to fit together, go
by the printed outcome and asserted direction, and say so in your reason.

**Condition.** The state that the printed asserted direction says brings the
outcome about, in a short noun phrase worded as that state. For *the more people
must sign off, the longer the decision takes*, the condition is *many people
having to sign off*. For *when the routine fails, mistakes reach the table*, it is
*the routine failing*. If the printed outcome is `none`, the condition is `none`.

**Form.** What kind of relation the claim asserts. Choose one.

| form | the claim says | an invented example |
|---|---|---|
| `produces` | the condition raises, lowers or brings about the outcome: "the more X, the more Y", "when X, then Y". A claim about what happens when something fails is `produces`, with the failure as its condition | *Time pressure makes cooks skip the tasting step.* |
| `requires` | the outcome cannot happen without the condition: "only when", "only if", "cannot without" | *A dish leaves the kitchen only after the head chef has tasted it.* |
| `maps` | the claim sorts cases by a condition and gives a different kind of outcome for each | *Cooks trained in hotels become sticklers for routine; cooks trained in family restaurants become improvisers.* |
| `none` | the condition makes no systematic difference to the outcome | *How long a cook has worked in the kitchen makes no difference to how often they skip the tasting step.* |
| `describes` | the printed outcome is `none`, and only then: the claim defines a term, describes a practice, a process, a setting or a kind, or says how the research was done | *The kitchen runs a three-stage tasting routine.* |

A claim whose printed outcome is `none` is always `describes`, and a claim with a
printed outcome never is, even a claim about how the research was done. Code the relation
the claim asserts, not how firmly it asserts it. If a claim asserts more than one
relation, code the one whose outcome is the printed outcome, and say so in your
reason. For a `maps` claim, the condition is what the claim sorts cases by: *where
the cook trained*.

### Each pair: three judgments

For every pair you make three judgments. The first is about **the stub** alone.
The second and third are about **the passage**: the sentence or sentences in the
paper that the stub summarises, found on the fragment's page and read with the
paragraph around it and the heading it sits under.

**1. What does the stub show?** From the stub alone.

Judge from the stub: not from the paper, not from the neighbouring fragments, not
from what you know about how organisations work, and not from an inference. Use
the condition and form you recorded for the claim, and the claim's printed outcome
and asserted direction.

| observation | code |
|---|---|
| **condition** | `present`: the stub shows the claim's condition holding. `absent`: the stub shows it not holding, or failing. `not shown`: the stub says nothing about it |
| **outcome** | `as asserted`: the stub shows the outcome going the way the asserted direction says. `other way`: the stub shows it going the opposite way, or not occurring. `not shown`: the stub says nothing about the outcome itself |
| **other cause** | `yes`: the stub puts the outcome down to something other than the claim's condition. `no` otherwise |
| **bounded** | `yes`: the stub shows the claim holding in one circumstance and not in another, where the difference is something the claim's statement does not mention, such as a kind of person, a setting or a time. `no` otherwise, including a stub that shows only a case where the claim fails |

An absence you would have to infer does not count. Code `absent` only if the stub
shows the condition not holding, and `present` only if the stub shows it holding.
Code the outcome against the asserted direction as printed, whatever the
condition: if the claim says the outcome rises and the stub shows it falling, that
is `other way`, even when the stub also shows the condition absent. Keep the
outcome's polarity as it is; do not re-sign it. If the stub shows the condition or
the outcome only in part, code what it shows and say "partly" in your reason.

**Both sides.** If the stub shows cases on both sides of the claim's own
condition, code the condition `present` and the outcome as it went where the
condition held, and say "both sides" in your reason. This is not `bounded`, which
is about a difference the claim does not mention.

**One fact, one role.** If the only thing the stub shows could count either as the
condition or as the outcome, code it as the outcome, and code the condition `not
shown`. Code the condition `present` or `absent` only when the stub shows it apart
from the outcome. When the condition is a practice working or failing, judge it
from what the stub shows of the practice itself, never from whether the outcome
came about.

For the claim *time pressure makes cooks skip the tasting step* (condition: time
pressure; outcome: skipping the tasting step; asserted direction: under time
pressure, cooks skip it):

| stub | condition | outcome | other cause | bounded |
|---|---|---|---|---|
| During the dinner rush, with every ticket overdue, a cook skips tasting the sauce. | present | as asserted | no | no |
| A cook skips the tasting step. | not shown | as asserted | no | no |
| A cook skips the tasting step on a slow afternoon with no orders waiting. | absent | as asserted | no | no |
| During the dinner rush, a cook tastes every dish before it leaves. | present | other way | no | no |
| On a slow afternoon, a cook tastes every dish before it leaves. | absent | other way | no | no |
| A cook skips the step because the recipe card has gone missing. | not shown | as asserted | yes | no |
| In the rush, the new cooks skip the step while the senior cooks keep tasting. | present | as asserted | no | yes |
| In the rush the cooks skip the step; on quiet afternoons they taste every dish. | present | as asserted | no | no |
| The kitchen is quiet on a weekday afternoon. | absent | not shown | no | no |
| The kitchen has a new head chef. | not shown | not shown | no | no |

For the claim *when the tasting routine works, dishes go out right* (condition:
the tasting routine working; outcome: dishes going out right; asserted direction:
when the routine works, dishes go out right):

| stub | condition | outcome | other cause | bounded |
|---|---|---|---|---|
| A dish went out over-salted. | not shown | other way | no | no |
| The cook skipped the routine's second tasting, and the dish went out over-salted. | absent | other way | no | no |
| Every tasting was done, and the dishes went out right. | present | as asserted | no | no |

Three forms need a word more.

- **`maps`.** Condition: `present` if the stub shows one of the conditions the
  claim sorts by, `not shown` otherwise; never `absent`. Outcome: `as asserted`
  if the stub shows the kind of outcome the claim gives for that condition, `other
  way` if it shows a different kind. If the stub shows a kind of outcome but none
  of the claim's conditions, code condition `not shown`, and outcome `as asserted`
  if the claim gives that kind of outcome for any of its conditions, `other way`
  if it gives it for none. If the printed direction does not say which kind of
  outcome goes with which condition, code the outcome `not shown`.
- **`none`.** Condition: `present` if the stub shows the claim's condition or its
  outcome at all, in one case or across cases, `not shown` otherwise; never
  `absent`. Outcome: `as asserted` only if the stub reports, across cases, that
  the outcome did not vary with the condition; `other way` if it reports, across
  cases, that the two varied together; `not shown` otherwise, including every
  single case.
- **`describes`.** Condition: `not shown`. Outcome: `as asserted` if the stub
  shows an instance of what the claim describes, `other way` if it shows a case
  that departs from it, `not shown` otherwise.

**2. What kind of passage is it?** From the paper.

| code | means |
|---|---|
| `report` | the paper shows you something that happened, was said, or was the case: one event, one utterance, one document or record, or a pattern across cases stated without explaining it |
| `reading` | the author's own interpretation: the author explains why something happened, says what something meant, or sets out their own framework, including figures and tables that present it |

A passage about one event is a `report` even when the author also explains that
event. What people in the setting said or thought, reported across cases in the
author's words, is a `report`, and so is a reason they gave or held, reported as
theirs: it is what they said or thought, not the author's explanation. A pattern
across cases is a `report` when the passage says what recurred without the author
explaining why, even when it uses the author's own categories. If a passage says
both what recurred and the author's own explanation of why, code `reading`.

| passage (invented) | kind |
|---|---|
| One evening the sous-chef sent a sauce back for more salt. | `report` |
| Several cooks said they skipped the tasting step when tickets piled up. | `report` |
| The cooks who became improvisers tended to taste less. | `report` |
| The cooks who became improvisers tasted less, and several said the routine felt like a cage. | `report` |
| The cooks who became improvisers tasted less, which the author puts down to their training in family restaurants. | `reading` |
| A figure sets out the author's three stages of kitchen learning. | `reading` |

**3. How does the paper use this passage for this claim?** From the paper.

| code | means |
|---|---|
| `evidence` | the paper presents the passage as showing, supporting or illustrating this claim |
| `qualification` | the paper presents the passage as a limit to this claim, an exception to it, or a case that runs against it |
| `restatement` | the passage is the paper stating this claim's own relation, or part of it: the sentence the claim was taken from, a later restatement or summary of it, or a figure or table that presents it. A passage that reports cases in which the relation shows is not a restatement, unless the claim was taken from that passage |
| `none` | the paper does not use the passage for this claim |

Judge this for every passage, whatever its kind: it is about what the paper does
with the passage.

The paper uses a passage for a claim in one of two ways. Either it says so: it
introduces or discusses the passage in terms of the claim (*for example*, *as one
cook put it*, *this shows*, *by contrast*, *one exception*). Or it places the
passage inside its argument for the claim, as an instance of it, in the paragraph
that makes the claim or in the paragraphs that develop it, and does not present it
for a different point. Sharing the claim's topic, setting or people is not enough.
Nor is appearing in the same section, if the paper uses the passage there for a
different point.

**A broad claim and a narrow one.** Where the paper argues a narrow claim that
spells out a step or a part of a broader claim, placement counts only for the
narrow claim. A passage placed in that argument is used for the broader claim only
if the paper ties it to the broader claim in words.

A paper often states a claim in several places; a passage used for any statement
of the claim counts. A passage can be used for more than one claim.

| what the paper does with the passage (invented) | claim | use |
|---|---|---|
| states that tasting catches seasoning errors, then gives the sous-chef's salt correction "for example" | *tasting catches seasoning errors* | `evidence` |
| the same salt correction, which sits in that argument | *the kitchen's routine keeps quality up*, a broader claim of which the first spells out a part | `none`, unless the paper ties the passage to this claim in words |
| adds "one exception: in the rush, errors got through even when every dish was tasted" | *tasting catches seasoning errors* | `qualification` |
| sums up: "tasting, in short, catches seasoning errors" | *tasting catches seasoning errors* | `restatement` |
| describes the dishwasher's schedule in the same section, to explain staffing | *tasting catches seasoning errors* | `none` |

*(End of Part A.)*

---

## Part B — how the codes are derived (never sent to a coder)

### Three kinds of link

| layer | a pair belongs to it when | what it records |
|---|---|---|
| **author link** | use is `evidence` or `qualification`, whatever the kind | the paper's own connection between a passage and its claim |
| **statement** | use is `restatement` | where the paper states the claim; never evidence for it |
| **evidence link** | kind is `report`, use is not `restatement`, and the table below gives a code other than no link (the evidence test) | printed evidence bearing on the claim, whether or not the paper draws the connection |

A pair can be both an author link and an evidence link, or either alone. An author
link on a `reading` records that the paper leans on its own interpretation; it is
never an evidence link.

### The code on an evidence link

`c` is the condition observation (`P` present, `A` absent, `N` not shown), `o` the
outcome (`S` as asserted, `O` other way, `N` not shown), `x` other cause, `b`
bounded.

1. A `reading`, a `restatement`, or c = N and o = N and b = no: **no link**.
2. b = yes: **`qualifies`**.
3. Otherwise, by form. `produces` is read as a tendency (the condition brings the
   outcome about; other things may too), `requires` as necessity:

| c | o | `produces` | `requires` | `maps` |
|---|---|---|---|---|
| P | S | `with` | `with` | `with` |
| N | S | `with` · outcome only | `with` · outcome only | `illustrates` · outcome only |
| A | O | `illustrates` · negative case | `illustrates` · negative case | (never A) |
| P | O | `against` | `illustrates` · condition without outcome | `against` |
| A | S | `illustrates` · outcome without condition | `against` | (never A) |
| P or A | N | `illustrates` · condition only | `illustrates` · condition only | `illustrates` · condition only |
| N | O | `illustrates` · outcome other way, condition unknown | `illustrates` · outcome other way, condition unknown | `illustrates` |

For `maps`, a condition coded `absent` is read as `not shown`, under every
reading and before anything else. Other cause: for
`produces` and `maps`, o = S with x = yes is `illustrates` · other cause, whatever
c is. For `requires` it is only flagged: another cause refutes necessity only when
the stub shows the condition absent, which the table already covers.

| `none` | code |
|---|---|
| o = S | `with` |
| o = O | `against` |
| o = N, c = P (or A, read as P) | `illustrates` |

| `describes` | code |
|---|---|
| o = S | `illustrates` |
| o = O | `qualifies` |

### Why the table reads as it does

- **A tendency is tested where the condition holds.** A case with the condition
  and the outcome supports it; a case with the condition and not the outcome runs
  against it. A case without the condition says nothing about a tendency, whether
  the outcome came about (other things can bring it about) or not (a negative
  case fits, but does not test).
- **Necessity is tested where the outcome occurs.** A dish that left untasted runs
  against *a dish leaves only after the head chef tastes it*; a tasted dish that
  was sent back does not.
- **An outcome alone stays `with`** for `produces` and `requires`, as decided on
  27 September, flagged so it can be counted apart. For `maps` it is `illustrates`:
  naming a kind of outcome shows nothing about which condition sorts into it.
- **One fact, one role** keeps an outcome from being counted a second time as its
  own condition, which is how a practice's "success" came to be read off its
  result.

### Four readings, all computed

Every result is computed under all four. The rule for the disputed cases is shown
rather than chosen in advance:

| reading | outcome only | negative case (`produces`) | outcome without condition (`produces`) | other cause (`produces`) |
|---|---|---|---|---|
| **v1.1** (the table above) | `with` | `illustrates` | `illustrates` | `illustrates` |
| **strict** | `illustrates` | `illustrates` | `illustrates` | `illustrates` |
| **covariation** | `illustrates` | `with` | `against` | `illustrates` |
| **v2 literal** (brief v2's box read word for word) | `with` | `against` | `against` | `against` |

Under the covariation reading, an outcome as asserted with another cause named is
still `illustrates`, as in version 1.1. In the v2 literal reading every form
except `describes` is read as `produces`:
an outcome the other way is `against` whatever the condition, and an outcome as
asserted is `against` if the condition is absent or another cause is named. For
the check of whether a coder applied v2 as written, the v2 literal reading is also
computed from the stub observations alone, ignoring kind and use.

Each reading gives a five-value code (`with`, `against`, `illustrates`,
`qualifies`, no link) and a three-value code (`with`, `against`, neither).

---

## Part C — left out of version 1.1, deliberately

- **Markers**, observable signs for each claim's condition and outcome. Without
  them, matching a stub to an abstract outcome is still a judgment; the test shows
  whether it is reliable.
- **A fixed specification of each claim**, the condition and form supplied in the
  table by a separate stage. Version 1.1 pins the condition to the printed
  direction instead, and the test measures agreement on form.
- **A claim map** and links derived through it. Version 1.1 never links a broad
  claim automatically, and its broad-and-narrow rule limits placement to the
  narrow claim.
- **Splitting a claim that asserts two relations.** Coders code the relation
  whose outcome is printed and flag the other.
- **Same-event marks and episode ids; a confidence scale; paragraph anchors.**

---

## Part D — what each rule answers

| the problem in brief v2 (the reviews and the audit) | the rule here |
|---|---|
| "bears on" is never defined | the paper's use (judgment 3) defines the author link; the evidence test (Part B) defines an evidence link. Topic, setting or people are not enough for either |
| links to the broad claim are made by hand (C01: 98) | a broad claim gets a passage only if the paper ties it there in words; placement counts only for the narrow claim; nothing links automatically |
| a negative case is coded both ways (F93 and F99; F97 and F98) | the outcome is recorded against the printed direction; the table decides; the readings show the alternatives |
| a practice's success is read off its own outcome (C20) | one fact, one role; the condition is pinned to the printed direction |
| an absent condition or another cause counts `against` any claim | only a `requires` claim is run against by an absent condition |
| categorical and null claims cannot be represented | the forms `maps` and `none` |
| the author's readings and restatements count as support | a `reading` is never an evidence link; `restatement` is its own layer; the paper's use is judged for every passage |
| aggregate reports fit neither voice code | a pattern stated without the author's explanation is a `report`, with a tie rule when the author also explains it |
| the voice test's ambiguous case: people's reasoning across events | a reason people gave or held, reported as theirs, is a `report`; only the author's own explanation makes a pattern a `reading` |
| direction is judged on a stub that may have lost facts | direction stays on the stub, judged before the coder has the paper; the page re-check measures what the paper adds |
| base rates prime coders ("most will not be `against`") | no base rates are stated |

---

## Changes from version 1

Version 1 was frozen and a sample drawn, then an independent review found the
following before any coder saw either. Both were set aside. Version 1.1 is frozen,
with a new seed recorded in the freeze, and a new sample drawn, before any coder
sees either. The 18 hard cases stay the same by design. A second review of version
1.1, before its freeze, added items 8 to 12.

1. **The condition is pinned** to the printed asserted direction, `requires` is
   limited to "only when" claims, a printed outcome of `none` is always
   `describes`, and "follow the statement" is replaced by "go by the printed
   outcome and direction" (review, finding 1).
2. **One fact, one role:** a fact that could be the condition or the outcome is
   the outcome; a practice's success is never read off its result (finding 1).
3. **The paper's use is judged for every passage.** Version 1 allowed `evidence`
   only for a report, which tied the author link to the kind of passage and told
   coders which answer led where (finding 2).
4. **A broad claim and a narrow one:** placement counts only for the narrow claim
   (finding 3).
5. **The passage is defined** as the sentences the stub summarises; a tie rule for
   a pattern that also explains; a pattern in the author's own categories is a
   report; worked examples for judgments 2 and 3 (finding 4).
6. **Part B reads `produces` as a tendency throughout.** Version 1 counted a
   negative case as `with` while treating an outcome without its condition as
   irrelevant, which favours `with`. `maps` no longer counts an outcome alone as
   `with`, `maps` and `none` never take `absent`, and the missing `none` cells are
   filled. A covariation reading is added (finding 6).
7. **Stubs are judged before the coder has the paper;** the paper is attached
   after the third reply, and the page re-check list only after the fifth
   (findings 5 and 7).
8. **A claim's own source sentence** is a `restatement` even when it reports a
   pattern (second review, finding 1).
9. **A reason people gave or held, reported as theirs, is part of a report;** only
   the author's own explanation makes a pattern a `reading`. The examples say so
   (second review, finding 2).
10. **Both sides:** a stub with cases on both sides of the claim's own condition is
    coded where the condition held (second review, finding 6).
11. **Smaller wording:** a condition worded as a state; `describes` only for a
    printed `none`; a `maps` claim whose printed direction gives no mapping has
    its outcome `not shown`; two orderings in Part B stated (second review,
    findings 5 and 6).
12. **The v2 arm works from the table alone,** as the new arm's stub judgments do,
    so the two are compared on the same material (second review, finding 5).
