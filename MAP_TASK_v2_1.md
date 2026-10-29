# How the paper's claims rest on one another

You have two files besides this one: a published qualitative paper, as a PDF,
and a map sheet of the paper. The sheet records the paper's claims, numbered
C01 onward; its passages, numbered F01 onward, each summarised in a line or
two; its contrast pairs, declared gaps and absences; and a list of numbered
pairs of claims. Every record in the sheet is a summary, not the paper's
words: check the page.

Your task is to map the paper's argument as printed: which of its core claims
rest directly on which other claims, and how; which of its construct names
name one construct; and, where the sheet says so, how the paper's explanatory
factors line up across its units and its contrast pairs. You do not judge
whether the paper is right or its evidence good: only how its argument is
built.

## How to read the sheet

- **core:** the claim carries the paper's contribution.
- **established** or **ventured:** ventured means the paper hedges the claim:
  it proposes, suggests or speculates.
- **outcome:** what the claim explains; `none` when it explains nothing.
- **constructs:** the constructs the claim invokes, as the sheet names them.
- **passages,** by how each bears on the claim: `with`, the passage reports the
  claim's outcome going the way the claim says; `against`, it reports the
  outcome going the other way, or occurring without the condition the claim
  names as its cause; `illustrates`, it reports the setting, the conditions or
  the phenomenon, but nothing about the outcome; `qualifies`, it bounds or
  limits the claim.
- **unit:** the group, site or case a passage comes from.
- **contrast pair:** two episodes set side by side, held comparable in some
  respects and different in others.
- **declared gap:** a limit the paper states. **Absence:** evidence the paper
  does not have, or has and does not print.

## Part 1. The pairs

Each numbered pair asks whether a core claim rests on another claim, its base:
in "does C01 rest on C14?", C01 is the claim and C14 the base.

**Rests on.** A claim Cj rests on a claim Ci if, with Ci set aside, the
paper's case for Cj as stated is weaker: Cj loses support, its mechanism loses
a premise, its ranking loses a term, or it loses its point. Any of these
counts, whether or not something else in the paper still supports Cj;
strength, below, says how much is left. Sharing a theme, a setting or a
passage is not enough. This is not entailment: it is argumentative
dependence.

**Setting Ci aside.** Set aside Ci and only Ci: the paper's statement of it,
and its support (the passages listed under it alone read otherwise, its
mechanism replaced). Every other claim stays as the paper states it, with
its own support, its passages included: a passage the sheet lists under both
Ci and Cj stays with Cj, as Cj's own, and counts for Cj as it stands, and one
listed under Ci and another claim Ck stays with Ck. Where Cj's account takes
Ci's outcome as a step, Cj still loses that step as Ci states it, even when
every passage listed under Ci is also listed under Cj; under strength, the
shared passages can then count as another source.

**Direct ties only.** A pair asks about a direct tie. If what Ci gives Cj
passes through another claim Ck (Ci is a case, a part or a step of Ck, and Ck
is what the paper uses for Cj), then with Ci set aside and Ck kept as stated,
Cj loses nothing: answer `rests_on` false, and name Ck in the reason. The tie
is recorded as Cj resting on Ck. The same test settles a pair where the paper
draws on both Ci and Ck for Cj: keep Ck as stated and set Ci aside. If Ck
still gives Cj everything Ci gave, the tie runs through Ck, however often the
paper names Ci. If Ci gives Cj something Ck does not (a case, a passage or a
step that Ck leaves out), Cj rests on Ci directly, and its strength counts
only what Ci alone gives.

**The four types.** If Cj rests on Ci, say how:

- `evidential`: Cj's support is Ci or its instances.
- `mechanistic`: Cj's mechanism presupposes Ci's outcome.
- `comparative`: Cj ranks explanations, and Ci is a term in the ranking.
- `significance`: Cj stays true if Ci falls, but loses its theoretical point.

**The test.** Set Ci aside, and ask these questions in this order. The first
yes gives the type; if every answer is no, Cj does not rest on Ci.

1. Does Cj rank or weigh explanations against one another, with Ci itself one
   of the explanations it ranks? `comparative`. A case or a unit that the
   ranked explanations are applied to is not one of them: for such a case, go
   on to the next question.
2. Does Cj's account of how its outcome comes about take Ci's outcome (its
   occurring, or its not occurring) as a step or a condition of that process?
   `mechanistic`. Answer no when Ci's outcome is a case of Cj's own outcome,
   the same outcome, or a part of it. Answer no, too, when the sheet gives
   `none` as the outcome of Cj or of Ci: one has no process for the other's
   outcome to enter, or no outcome to give.
3. Is Ci, or a passage the sheet lists under Ci and not under Cj, part of what
   the paper offers to show that Cj holds (a case, an instance, a part or a
   finding), so that without it Cj has less support? `evidential`.
4. Does Cj keep all its support, but lose what the paper offers it to show or
   explain? `significance`. Answer yes only if the paper itself says that what
   Cj is offered for is Ci, and give the page where it says so. Belonging to
   the same argument, or one claim being broader than the other, is not
   enough.

**Strength.** For each edge, how much of the paper's case for Cj as stated is
left without Ci:

- `necessary`: for some part of Cj as stated, nothing else in the paper gives
  it what Ci gives (its support, its mechanism's premise, its term, or its
  point). In particular, Ci is necessary when it is the only case of one side
  of what Cj states: the only case in which Cj's outcome occurs, or does not
  occur, or the only case of a condition or a clause that Cj names.
- `contributing`: something else in the paper gives every part of Cj what Ci
  gives, so Cj is weaker without Ci but keeps all its parts.

Something else counts only if it gives Cj that on its own evidence. A claim
that is a case, a part or a restatement of Ci, a claim that rests on Ci, and a
passage the sheet lists under Ci and not under Cj are not another source. A
passage listed under both is Cj's own, as in setting Ci aside: it is another
source when it gives Cj, by itself, what Ci gives.

**For each pair, give:** the pair's number; its claim and base, as the sheet
lists them; `rests_on`, true or false; and a reason, in one sentence. For an
edge (`rests_on` true), also its type, its strength, its basis (in a few words,
what shows the tie: the sheet's ids where it has them, or what the paper says,
in your own words) and the page of the paper the edge rests on.

A pair asks about one direction only: whether Cj rests on Ci says nothing about
whether Ci rests on Cj. Some listed pairs have a tie and some do not, in no
particular order: answer each on its own.

## Part 2. Further edges

The list does not pair every core claim with every other claim. Give up to
ten edges that it does not ask about, each a core claim resting directly on
another claim, by the test of part 1; if you find fewer than ten, give those
you find. Rank them from the one the paper's argument depends on most,
necessary edges before contributing ones, and list them in that order. Look first, for each
core claim, at the claims its statement names or presupposes and at those
whose passages the sheet lists under it. Give each with its claim, base,
type, strength, basis, page and reason, as in part 1. Part 2 is a search for
what the list misses, and it is read apart from part 1: an edge you do not
give in part 2 is not a no, whether you give ten edges or fewer.

## Part 3. The registry of constructs

The sheet lists every construct name in the claims, as written. Group the names
that name one construct in this paper: names that can stand in for each other
in every claim that uses either without changing what the claim says, such as
the same thing under another wording, in the singular or the plural, or with a
qualifier the paper drops elsewhere. Do not group two things the paper keeps
apart, a part with its whole, or a kind with its general term. A qualifier
marks a kind only where the paper sets the qualified name against another
kind of the same thing, or says that the general term covers more than it; a
qualifier that some claims add and others drop, with no other kind set
against it, names the same construct. Do not group two names that a claim's
statement names as two things: one acting on the other, one set against the
other, or the two given as separate items. Two names in one claim's list of
constructs are not enough on their own, since that list can give one thing
in two wordings. Give each group of two or more names, with a canonical
name: the one of its names that the most claims use, and on a tie the first
of them in the sheet's list. A name that stands alone needs no entry.

## Part 4. The paper's explanatory factors

Where the sheet says part 4 applies: the factors the paper itself uses to
explain why its outcome differs across its units or between the two sides of
its contrast pairs. Name each at the level at which the paper compares its
units, as something that differs from one unit to another, not as a feature of
one unit or one episode. Give each a short name, the claim that states it as a
general factor (where several do, the one with the lowest number), and an id,
X1, X2 and so on, in the order of those claims. Give as many as the paper
uses, and add none of your own.

## Part 5. The comparative table

Where the sheet says part 5 applies: for each unit it names there, once each,
the unit's outcome (`+` the unit shows the outcome the paper explains across
its units, `-` it does not, `?` the paper does not say) and each factor's value
in that unit (`+` present or high, `-` absent or low, `?` the paper does not
say), with the ids of the claims and passages that show them. Name each unit
exactly as the sheet does.

## Part 6. The contrast controls

Where the sheet says part 6 applies: for each contrast pair it names, once each,
whether each factor is the same on both sides (`held`), differs between them
(`varies`), or is not said (`unclear`), judged from what the paper says of the
two sides themselves: a value the paper gives only for the kind of episode a
side belongs to counts only where the paper applies it to that side. Give as
ids the passages about the two sides and the claims that state their values.

## An example

From a made-up paper, not the one attached: a study of three hospital wards
taking up a safety checklist. Its claims: **C1** (core), wards take up the
checklist when their senior nurse endorses it; **C2**, Ward A's senior nurse
endorsed it, and the ward took it up within a month; **C3**, Ward B's senior
nurse, alone of the three, did not endorse it, and the ward never took it up;
**C4**, endorsing senior nurses put checklist time into the staff rota; **C5**
(core), staff took up the checklist because, with its time in the
rota, they no longer had to choose between it and patient care; **C6** (core;
outcome `none`), endorsement, not training, explains which wards took the
checklist up; **C7** (core), senior nurses hold an authority over practice that
the formal hierarchy does not record; **C8**, Ward C's senior nurse endorsed it
too, and the ward took it up; **C9**, Ward A's senior nurse found the rota time
by cancelling a weekly meeting.

- **Does C1 rest on C2?** Yes: `evidential`, `contributing`. Ward A is one of
  the cases C1 is drawn from; Ward C (C8) is another of the same kind, so
  every part of C1 keeps support without C2.
- **Does C5 rest on C4?** Yes: `mechanistic`, `necessary`. C5's support is its
  own passages, staff saying they no longer had to choose; what it needs from
  C4 is C4's outcome, time in the rota, and nothing else in the paper supplies
  it.
- **Does C5 rest on C9?** No. What C5 needs is C4's outcome, time in the rota;
  C9 tells how one ward found that time. With C9 set aside and C4 kept as
  stated, C5 loses nothing: the tie runs through C4, and the edge is C5 on C4.
  The paper also mentions the cancelled meeting where it reports C5's
  interviews, but C9 gives C5 nothing that C4 does not, so the answer stays
  no.
- **Does C6 rest on C1?** Yes: `comparative`, `necessary`. C6 ranks endorsement
  above training as the explanation; if endorsement did not explain uptake, the
  ranking would come out otherwise.
- **Does C6 rest on C3?** Yes: `evidential`, `necessary`. Ward B is a case, not
  one of the explanations C6 ranks, and C6 has no outcome, so the first two
  questions give no; Ward B is part of what shows C6, and as the only ward
  without endorsement it is the only case of one side of C6's comparison.
- **Does C7 rest on C1?** Yes: `significance`, `necessary`. The interviews that
  show the senior nurses' authority stand whether or not endorsement explains
  uptake, so C7 stays true without C1; but the paper offers that authority as
  what made endorsement work, and without C1 it explains nothing.
- **Does C5 rest on C3?** No. C5 explains uptake on the endorsed wards; Ward
  B's case gives it no reason and takes none away.

The order of the questions settles the close calls. C1 is also part of what
shows C6, but C6 ranks explanations and C1 is one of them, so the first
question gives `comparative`. C4 might seem part of C5's support, but what C5
needs from it is its outcome, a step in C5's account, so the second question
gives `mechanistic`. Ward A's uptake, in C2, is a case of C1's outcome, not a
step in how it comes about, so for C1 and C2 the second question gives no and
the third gives `evidential`.

## Rules

- Answer every listed pair once, in the sheet's order.
- Judge from the paper. The sheet's records are summaries and pointers; where
  one seems to differ from the paper, go by the paper and say so in the reason.
- Do not quote more than eight words of the paper in a row. Paraphrase, and
  cite the page.
- Work only from the paper and these files. Do not search the web.

## What to return

A single JSON object and nothing else, as a file if you can, otherwise as one
code block. Where the sheet says a part does not apply, give its list empty.
Write `+`, `-` and `?` as shown, with a plain hyphen for minus.

```json
{
  "paper": "author and year, as the paper prints them",
  "pairs": [
    {
      "pair": "P001",
      "claim": "C..",
      "base": "C..",
      "rests_on": true,
      "type": "mechanistic",
      "strength": "necessary",
      "basis": "...",
      "page": "p. ..",
      "reason": "..."
    },
    {
      "pair": "P002",
      "claim": "C..",
      "base": "C..",
      "rests_on": false,
      "reason": "..."
    }
  ],
  "further_edges": [
    {
      "claim": "C..",
      "base": "C..",
      "type": "evidential",
      "strength": "contributing",
      "basis": "...",
      "page": "p. ..",
      "reason": "..."
    }
  ],
  "registry": [
    {"canonical": "...", "names": ["...", "..."]}
  ],
  "factors": [
    {"id": "X1", "name": "...", "claim": "C.."}
  ],
  "units": [
    {"unit": "...", "outcome": "+", "values": {"X1": "+", "X2": "?"}, "ids": ["C..", "F.."]}
  ],
  "contrasts": [
    {"contrast": "CP01", "controls": {"X1": "held", "X2": "varies"}, "ids": ["F..", "F.."]}
  ]
}
```
