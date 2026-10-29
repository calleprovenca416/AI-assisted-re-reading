# MAP_TASK_v2_1.md checked against T39's 65 items

*19 Oct 2026.* The check was made independently, with only `MAP_TASK_v2_1.md`, the two map sheets and the two settle keys: not the PI's settling or the PI's answers, not `MAP_TASK_v2.md` or its check, not the change notes, the feedback file, `MAP_TASK.md` or the papers. Its brief was the one the check of v2 had, with v2.1 in place of v2. It judged, item by item, whether v2.1's text decides the item. Its report and item table are below. The comparisons that follow them were made afterwards, by script.

## The verdicts

| paper | text | A | B | void | paper needed | open | items |
|---|---|---|---|---|---|---|---|
| Bechky | v2.1 | 3 | 1 | 3 | 14 | 2 | 23 |
| Bechky | v2 | 8 | 1 | 3 | 11 | 0 | 23 |
| Pratt | v2.1 | 12 | 1 | 8 | 19 | 2 | 42 |
| Pratt | v2 | 9 | 2 | 8 | 20 | 3 | 42 |
| all | v2.1 | 15 | 2 | 11 | 33 | 4 | 65 |
| all | v2 | 17 | 3 | 11 | 31 | 3 | 65 |

No item came out "other" in either check. Void: all eleven are further edges only one map gave, in both.

## Beside the PI's answers

The PI's answers: the PI's settling of 18 Oct, with the PI's answers of 19 Oct on seven of its items (`map_settle_revisions.json`).

- **v2.1:** where it decides for A or B (17 items), it gives the PI's answer in 17 and the other in 0.
- **v2,** set beside the same answers: of its 20 items for A or B, the PI's answer in 18 and the other in 2 (Bechky S021, Bechky S023); beside the PI's settling of 18 Oct, as `MAP_TASK_v2_CHECK.md` reports, the other in 7.

## Against the check of v2

15 items changed verdict: A to open, 1; A to paper, 6; B to paper, 1; open to paper, 1; paper to A, 5; paper to open, 1. The deciding text is the second check's, as its table gives it.

| item | what | v2 | v2.1 | the PI's answer | v2.1's deciding text |
|---|---|---|---|---|---|
| Bechky S010 | P051 C03<-C17 | A | open | A | only-case clause vs shared-passage clause |
| Bechky S017 | C21<-C04 | A | paper | A | Strength (`necessary`, every part); exclusion and shared-passage clauses |
| Bechky S018 | C21<-C05 | A | paper | A | same as S017 |
| Bechky S021 | legitimacy + symbolic legitimacy | A | paper | B | Part 3, qualifier sentence |
| Bechky S022 | meaning making + occupational interpretation | paper | open | B | Part 3, stand-in test |
| Bechky S023 | occupational legitimacy + symbolic legitimacy | A | paper | B | Part 3, qualifier sentence |
| Pratt S001 | P002 C01<-C35 | paper | A | A | none-outcome clause; direct-tie rule (second sentence) |
| Pratt S006 | P016 C01<-C54 | paper | A | A | none-outcome clause; direct-tie rule (second sentence) |
| Pratt S008 | P023 C01<-C21 | A | paper | A | none-outcome clause; direct-tie rule, last sentence |
| Pratt S011 | P038 C01<-C25 | paper | A | A | none-outcome clause; direct-tie rule |
| Pratt S015 | P048 C20<-C23 | B | paper | B | same-outcome clause |
| Pratt S020 | P081 C20<-C58 | paper | A | A | direct-tie rule; stays-with-Ck clause |
| Pratt S021 | P083 C28<-C20 | A | paper | A | Q2 (occurring or not occurring); shared-passage clause |
| Pratt S024 | P086 C13<-C14 | open | paper | A | step-kept clause; shared-passage clause |
| Pratt S025 | P087 C01<-C24 | paper | A | A | none-outcome clause; direct-tie rule |

Pratt S015 moved with no change to the rule that decided it in v2 (the second question's clause on a case, the same outcome or a part of it, the same words in both texts): the first check read the part from the sheet's outcome lines and its summary of F79, noting that it relied on the sheet's wording; the second wants the page. That move is a difference between the two checks, not between the two texts.

## Beside the lighter settling

With the PI's answers in place of the PI's settling on the five items the PI revised, the items that change some reading's labels on the core claims (each tried both ways, the rest as the PI now answers them, by script, with `build_map_settle.py`'s own code):

| paper | items that change labels | decided by v2.1, A or B | void in v2.1 | need the paper or open |
|---|---|---|---|---|
| Bechky | 12 | 4 (S006, S009, S012, S015) | 2 (S016, S020) | 6 (S002, S004, S007, S010, S013, S014) |
| Pratt | 12 | 0 | 4 (S028, S031, S036, S038) | 8 (S002, S003, S014, S015, S021, S026, S029, S030) |
| all | 24 | 4 | 6 | 14 |

Under the PI's settling of 18 Oct the items that change labels were 22 (`MAP_SETTLE_LIGHT_EXAMPLE.md`); with the PI's answers they are 24 (Pratt S002, S026 and S030 now change labels, S020 no longer does).

## Where v2.1's own wording is at fault

Of the eleven places the check names, two come from sentences v2.1 added:

- **Direct ties, the new second sentence** (its place 3): it does not repeat the condition that Ci is a case, a part or a step of Ck, so two claims that give Cj the same thing could each be routed through the other.
- **The shared-passage sentence against the only-case rule** (its place 1): a passage Cj shares with Ci about the one case of a side can count as another source, which would undo the only-case rule (Bechky S010, open; the same sits under the agreed Bechky edges P039 and P054).

Its place 2 (a passage listed under the base and a third claim) is the clash v2.1 meant to settle, still read two ways where the third question and the exclusions count such a passage as the base's.

Also outside the 65 items: in the agreed Pratt registry the two coders gave the turnover group different canonical names, and part 3's tie rule (the same in v2 and v2.1) picks "membership turnover", map B's; the PI's settled map has "turnover", map A's.

## The check's report

All 65 items are judged. The revised text settles 28 of them: 15 for coder A, 2 for coder B and 11 void. It leaves 33 needing the paper and 4 open, and it makes no item "other". In 11 of the 33 paper items it already rules out one coder's answer or that coder's stated reason.

| | A | B | other | void | paper | open | total |
|---|---|---|---|---|---|---|---|
| bechky | 3 | 1 | 0 | 3 | 14 | 2 | 23 |
| pratt | 12 | 1 | 0 | 8 | 19 | 2 | 42 |
| all | 15 | 2 | 0 | 11 | 33 | 4 | 65 |

**What settles the A, B and void items:**
- **Void (11):** these are all the further-one items. Part 2's last sentence means an edge a coder leaves out no longer counts as a no. In pratt S034, coder B's edge also has a type the text now rules out.
- **A in pratt (12):** most are edges into C01. The sheet gives C01 no outcome, so question 2 rules out B's mechanistic type. All of the base claim's passages are already listed under C01, so the direct-ties rule sends the tie through C13 or C20, which both coders already accept as bases of C01. The other three are S009, S010 (type only) and S020.
- **A in bechky (3):** S006, S012 and S015. Question 1 makes a unit's claim a case, not a term in the ranking, so these edges are evidential.
- **B (2):**
  - Bechky S009: coder A's own premise, together with the clause that the step is lost even when passages are shared.
  - Pratt S032: the sheet gives the same outcome for both claims.

**Why 33 items need the paper:**
- **Question 4 (significance):** bechky S001–S004, S011 and S014. Each needs the paper's own statement. In S014 coder A's type is already ruled out.
- **Question 3 (is the base offered as support?):** bechky S005, S007, S008, S013; pratt S003, S012, S013, S018, S023.
- **Strength:** bechky S017, S018; pratt S002, S014, S016, S017, S021, S024, S026, S027, S029, S030.
  - In most of these the text strikes the other source a coder named, because a case or part of the base no longer counts. The answer then turns on whether a passage listed under both claims gives the claim the same thing on its own.
  - In pratt S027 that route may support coder A on a different ground.
- **Single facts:**
  - Pratt S008: passage F121 is listed under C21 alone.
  - Pratt S015: whether C23's outcome is part of C20's.
  - Bechky S021 and S023: whether the paper sets symbolic legitimacy against another kind of legitimacy.
  - Pratt S041 and S042: whether the paper applies a kind-level description to the two individuals in the contrast.

**The 4 open items:**
- **Bechky S010:** the "only case" rule points to coder A, but the passages listed under both claims can count as another source.
- **Bechky S022:** the two names have different head words, so the qualifier rule doesn't reach them and only the stand-in test remains.
- **Pratt S039 and S040:** these are one factor, named at the process level by A and the practice level by B. The text doesn't choose a level, or say whether a claim stating two factors together counts for the lowest-number rule.

**New ambiguities in the revised text:**
1. **"Only case" against shared passages (Part 1, Strength):** the two clauses can point opposite ways. The same clash affects agreed bechky edges P039 and P054.
2. **"Setting Ci aside" against question 3 and the strength exclusions:** they disagree on whether a passage listed under the base and a third claim, but not the claim, stays with the third claim or counts as the base's.
3. **Direct-ties rule, second sentence:** it drops the first sentence's case-part-or-step condition. Read that way, two overlapping claims each route through the other and both pairs come out false (pratt C01 on C12 and C01 on C13).
4. **Direct-ties rule, last sentence:** it lists case, passage or step, but not the "finding" that question 3 counts.
5. **"By itself" (shared-passage clause):** there's no guide for figure or summary passages, nor on whether several claims together can be "something else".
6. **Strength exclusions:** they don't say whether a part of a case of the base counts as a part of the base.
7. **Question 2's same-outcome clause:** it doesn't say whether to compare the sheet's outcome lines or the paper.
8. **Question 4:** it doesn't say how explicit the paper's own statement must be.
9. **Part 4:** see S039 and S040 above.
10. **Part 6:** it doesn't say whether a side's member belonging to the kind is enough for the kind's value to apply.

One difference outside the 65 items: in the agreed pratt groupings, the two coders give the turnover group different canonical names. Part 3's tie rule picks "membership turnover", coder B's.

Nothing in the task, the sheets or the items was changed. The full table, with the deciding text and one sentence per item, and the ambiguity notes follow.

The passage overlaps were computed by script; a second script confirms that all 65 items are present and that no six words in a row in the table come from the source files.

## The check's item table

Verdicts: A, B, other, void, paper, open (as defined in the brief).
Notation: Cj<-Ci means "does Cj rest on Ci". ev = evidential, mech = mechanistic,
comp = comparative, sig = significance; nec = necessary, contr = contributing.
"Sheet fact" = a field the v2.1 text itself points to (an outcome given as none,
which passages the sheet lists under which claim, the claim the sheet names for
a unit). Passage overlaps were computed by script.
Rule names used below:
- none-outcome clause = Part 1, test question 2, its last two sentences.
- same-outcome clause = Part 1, question 2, the sentence on a case of Cj's outcome.
- unit clause = Part 1, question 1, its second sentence.
- sig clause = Part 1, question 4 (the paper itself must say so, with page).
- direct-tie rule = Part 1, "Direct ties only" paragraph.
- step-kept clause = Part 1, "Setting Ci aside", last sentence.
- stays-with-Ck clause = Part 1, "Setting Ci aside", second sentence.
- only-case clause = Part 1, Strength, second sentence of `necessary`.
- exclusion clause = Part 1, the paragraph after Strength, second sentence.
- shared-passage clause = same paragraph, last sentence.
- Part 2 no-no clause = Part 2, last sentence.

## Bechky (23)

| id | kind | item | A | B | verdict | deciding text | why |
|---|---|---|---|---|---|---|---|
| S001 | pair-edge | P003 C05<-C01 | no edge | sig nec | paper | sig clause | B's edge needs the paper's own statement that C05 is offered for C01's point, and the coders disagree on that, so the page decides. |
| S002 | pair-edge | P015 C20<-C05 | sig nec | no edge | paper | sig clause (C20 outcome none rules out mech) | Only a significance tie is possible, and whether p. 637 itself offers C20 to explain C05 is asserted by A and not addressed by B. |
| S003 | pair-edge | P020 C04<-C01 | no edge | sig nec | paper | sig clause | As S001: the edge turns on whether the paper itself states C04's point is C01, which is not agreed. |
| S004 | pair-edge | P022 C20<-C04 | sig contr | no edge | paper | sig clause; Strength | Whether the paper offers C20 for C04 needs the page; if it does, A's ground for contributing (C05 carries the point) covers values, not technique, so even A's strength is not secured. |
| S005 | pair-edge | P035 C05<-C13 | no edge | ev contr | paper | Q3; stays-with-Ck clause | Every C13 passage not under C05 is also under another claim (C04, C11, C16, C18), so it turns on whether the paper offers C13's readings as support for C05, which needs the paper. |
| S006 | pair-type | P036 C21<-C18 | ev contr | comp contr | A | unit clause, then none-outcome clause, then Q3 | C18 is the sheet's claim for the narcotics unit, a case to which the ranked accounts apply, so Q1 is no, Q2 is no (C21 outcome none) and Q3 gives evidential. |
| S007 | pair-edge | P037 C21<-C10 | no edge | ev contr | paper | Q3 (Q1 also arguable) | Whether C10 (or F58/F27, its passages outside C21) is among the support the paper gives C21 needs the page; the text gives the test but the coders disagree on the fact. |
| S008 | pair-edge | P042 C20<-C13 | no edge | ev contr | paper | Q3; stays-with-Ck clause | Both outcomes are none so only Q3 is live, and whether the paper offers C13's differing readings to show C20 needs the paper. |
| S009 | pair-edge | P047 C05<-C10 | no edge | mech contr | B | Q2 with step-kept clause; Strength | Both coders say C05 needs the units to hold different values (A's own premise), which is C10's sheet outcome, and v2.1 says that step is lost even when passages are shared; both agree the unit accounts also show it, so contributing. |
| S010 | pair-type | P051 C03<-C17 | ev nec | ev contr | open | only-case clause vs shared-passage clause | B's ground (other units give the contrasting side) fails, and the only-case clause, with the agreed fact that toxicology is the one immediate-route unit, points to A; but C03 itself lists F88, F98, F152, F161 on the same episode, and the shared-passage clause can make them another source. |
| S011 | pair-edge | P052 C03<-C01 | no edge | sig nec | paper | sig clause | As S001: whether the paper itself says C03's point is C01 is the disputed fact. |
| S012 | pair-type | P056 C21<-C17 | ev contr | comp contr | A | unit clause, none-outcome clause, Q3 | C17 is the sheet's claim for the toxicology unit, so it is a case, not a ranked term, and the sequence gives evidential. |
| S013 | pair-edge | P073 C13<-C04 | no edge | ev contr | paper | Q3 | C13's outcome is none, so only Q3 is live, and whether the paper offers C04's technical-fit material to show C13 needs the paper. |
| S014 | pair-type | P074 C13<-C02 | mech nec | sig nec | paper | none-outcome clause; Q3; sig clause | A's mechanistic type is ruled out because C13's outcome is none; whether the edge is sig (B) needs the paper to say C13 is offered for C02 (and Q3 is asked first). |
| S015 | pair-type | P076 C21<-C16 | ev contr | comp contr | A | unit clause, none-outcome clause, Q3 | C16 is the sheet's claim for the firearms unit, so not a ranked term; evidential. |
| S016 | further-one | C04<-C02 | mech nec | none | void | Part 2 no-no clause | B's silence on a part 2 edge is no longer a no, so nothing is in dispute. |
| S017 | further-type | C21<-C04 | comp nec | comp contr | paper | Strength (`necessary`, every part); exclusion and shared-passage clauses | B's ground (the values term also supports the work side) fails because C21 names technique as its own part; but F166 and F172 are listed under both C04 and C21 and may by themselves give the technique term, which needs the page. |
| S018 | further-type | C21<-C05 | comp nec | comp contr | paper | same as S017 | Mirror of S017 for the values term: B's ground fails, and whether shared F166/F172 alone give the values term needs the page. |
| S019 | further-one | C01<-C09 | mech contr | none | void | Part 2 no-no clause | One-sided part 2 edge; the omission is not a no. |
| S020 | further-one | C13<-C10 | none | ev contr | void | Part 2 no-no clause | One-sided part 2 edge; the omission is not a no. |
| S021 | constructs | legitimacy + symbolic legitimacy | apart | group | paper | Part 3, qualifier sentence | Group unless the paper sets symbolic legitimacy against another kind or says the general term covers more; no claim in the sheet does, but the paper's review (p. 610) has to be checked. |
| S022 | constructs | meaning making + occupational interpretation | apart | group | open | Part 3, stand-in test | The names differ in head word, so the qualifier rule does not reach them, and whether either can replace the other in C11, C12 and C13 without changing them is left to judgment. |
| S023 | constructs | occupational legitimacy + symbolic legitimacy | apart | group | paper | Part 3, qualifier sentence | Same deciding fact as S021; C09's statement names one thing, and its construct list alone does not keep them apart. |

## Pratt (42)

Pratt C01 and C34 have outcome none on the sheet, so no edge into C01 or C34
can be mechanistic. C01 lists F03, F05, F17, F19, F21 and every passage
F27-F119, so nearly all of any base's passages stay with C01 as its own. Both
coders agree C01 rests on C13 (S010) and on C20 (S014), C13 rests on C15
(P065), and C20 rests on C21 as its first step (P079).

| id | kind | item | A | B | verdict | deciding text | why |
|---|---|---|---|---|---|---|---|
| S001 | pair-edge | P002 C01<-C35 | no edge | mech contr | A | none-outcome clause; direct-tie rule (second sentence) | Mechanistic is ruled out, all C35 passages are C01's own, and both reasons treat C35 as the self-discrepancy content that C13 (via C15) already states, so C13 kept leaves C01 nothing to lose. |
| S002 | pair-type | P003 C01<-C12 | ev contr | mech nec | paper | none-outcome clause; Q3; exclusion and shared-passage clauses | Type is settled for A (evidential); A's ground for contributing fails because C13 is a case of C12 (the sheet's C13 wording; both reasons), so strength turns on whether a shared passage such as F108 or F109 alone gives C01 what C12 gives: A if so, other (ev nec) if not. |
| S003 | pair-edge | P004 C28<-C07 | ev contr | no edge | paper | Q3 | C07's shared passages (F21, F88, F96, F99) stay with C28, so it turns on whether the paper offers the general pattern, or F19/F27, as support for C28, which the coders dispute. |
| S004 | pair-edge | P006 C01<-C23 | no edge | mech contr | A | none-outcome clause; direct-tie rule | Both reasons place C23 inside positive programming (C20), C20 is an agreed base of C01, and C23's passages are all C01's or C20's own (F10), so the tie runs through C20. |
| S005 | pair-edge | P013 C01<-C14 | no edge | mech contr | A | none-outcome clause; direct-tie rule | Both reasons make C14 a part of dream building (C13, whose statement names tying aspirations to the self), every C14 passage is C01's own, so the tie runs through C13. |
| S006 | pair-edge | P016 C01<-C54 | no edge | mech contr | A | none-outcome clause; direct-tie rule (second sentence) | Both reasons place C54 inside why dream building motivates; its passages are all C01's own and it adds no case or step C13 leaves out. |
| S007 | pair-edge | P018 C01<-C17 | no edge | mech contr | A | none-outcome clause; direct-tie rule | Both treat C17 as the sustaining part of dream building, which C13's statement names; all its passages are C01's own. |
| S008 | pair-edge | P023 C01<-C21 | no edge | mech contr | paper | none-outcome clause; direct-tie rule, last sentence | B's type is ruled out and C21 is an agreed step of C20, but F121 (footnote 15) is listed under C21 alone, a passage C20 leaves out: if the paper offers it for C01 the edge is direct evidential (other), if not the answer is A. |
| S009 | pair-edge | P028 C11<-C17 | no edge | mech contr | A | direct-tie rule | C17 is the sustaining part of C13 (both reasons), C13 is the agreed mechanistic base of C11 (P009) and its statement keeps the motivation active, so whatever step C17 gives C11 runs through C13; F43-F52 are support for that step, not a step C11 takes (as in the task's C5/C9 example). |
| S010 | pair-type | P035 C01<-C13 | ev contr | mech contr | A | none-outcome clause; Q3 | Both say an edge, contributing; mechanistic is ruled out, so Q3 gives evidential. |
| S011 | pair-edge | P038 C01<-C25 | no edge | mech contr | A | none-outcome clause; direct-tie rule | Both reasons make C25 part of positive programming's sensegiving (C20); all its passages are C01's own. |
| S012 | pair-edge | P039 C01<-C18 | no edge | ev contr | paper | Q3; direct-tie rule | All C18 passages are C01's own, so the edge turns on whether the paper offers C18's finding for C01 (B) or for C38 (A), and C13's statement does not name C18's breadth effect, so the routing rule does not settle it. |
| S013 | pair-edge | P040 C13<-C54 | no edge | mech contr | paper | Q2 with step-kept clause; direct-tie rule | Whether C13's account takes the motivating force of self-linked goals as a step, or footnote 11 runs the other way as A says, needs the page; all C54 passages are C13's own. |
| S014 | pair-type | P046 C01<-C20 | ev contr | mech nec | paper | none-outcome clause; Q3; exclusion and shared-passage clauses | Type is settled for A; A's ground (C21-C23 document the same practice) fails because they are parts or steps of C20, so strength turns on whether a shared passage such as F79 alone gives C01 what C20 gives: A if so, other (ev nec) if not. |
| S015 | pair-type | P048 C20<-C23 | mech contr | ev contr | paper | same-outcome clause | If C23's outcome (reliance on organizational sources) is part of C20's (encapsulated sensemaking), Q2 is no and B is right; the sheet's F79 summary describes it as part, but the coders disagree and the page decides. |
| S016 | pair-type | P058 C20<-C22 | mech contr | mech nec | paper | Strength; shared-passage clause | Whether C21 gives C20 encapsulation on its own evidence (A's ground) needs the paper, and shared F72/F73 may by themselves supply social or ideological encapsulation. |
| S017 | pair-type | P062 C34<-C01 | sig nec | sig contr | paper | Strength (`contributing` needs something else) | Both agree the type; B names no other source of C34's point, but whether one exists (for example C56 or C42) needs the paper. |
| S018 | pair-edge | P068 C34<-C33 | ev contr | no edge | paper | Rests-on paragraph (any loss counts); Q3 | B's ground (C33 is not required) is no longer the test, but whether p. 483 offers C33 toward C34 is asserted by A only. |
| S019 | pair-edge | P076 C01<-C22 | no edge | mech contr | A | none-outcome clause; direct-tie rule | Both reasons make C22 a part of positive programming (C20); every C22 passage is C01's own. |
| S020 | pair-edge | P081 C20<-C58 | no edge | ev contr | A | direct-tie rule; stays-with-Ck clause | C58's only passages (F96-F98) are also listed under C28, an agreed base of C20 (P054), and both reasons tie C58 to the disidentification failures, so C28 kept gives C20 all C58 gave. |
| S021 | pair-edge | P083 C28<-C20 | mech nec | no edge | paper | Q2 (occurring or not occurring); shared-passage clause | B's ground (C28 does not presuppose successful encapsulation) is answered by the not-occurring words, and B's own reason states the absence of insider sensegiving as the cause, so an edge follows; whether shared F99 alone gives that condition decides necessary (A) or contributing (other). |
| S022 | pair-edge | P084 C01<-C15 | no edge | mech contr | A | none-outcome clause; direct-tie rule | C15 is the agreed middle step of C13 (P065), C13 is an agreed base of C01, and every C15 passage is C01's own. |
| S023 | pair-edge | P085 C01<-C26 | no edge | ev contr | paper | Q3 | All C26 passages are C01's own and C26 is not a part of any agreed base of C01, so it turns on whether the paper offers C26's finding toward C01 or only toward C34. |
| S024 | pair-type | P086 C13<-C14 | mech contr | mech nec | paper | step-kept clause; shared-passage clause | A's ground is F28, listed under both C14 and C13, which v2.1 now admits as another source if it alone gives C13 the incorporation step; whether it does needs the page. |
| S025 | pair-edge | P087 C01<-C24 | no edge | mech contr | A | none-outcome clause; direct-tie rule | Both reasons place C24 inside the enactment of positive programming (C20); all its passages are C01's own. |
| S026 | further-type | C02<-C12 | mech contr | mech nec | paper | exclusion clause; shared-passage clause | A's only named other source, C13, is a case of C12 and so not another source, which points to B; but F109 is listed under both C12 and C02 and may alone give the seekership step. |
| S027 | further-type | C11<-C12 | mech contr | mech nec | paper | exclusion clause; shared-passage clause | A's ground (C13) is excluded as in S026, but F108, under both C12 and C11, appears on the sheet to state the very step, so contributing may follow on a different ground; the page decides. |
| S028 | further-one | C27<-C12 | mech contr | none | void | Part 2 no-no clause | One-sided part 2 edge. |
| S029 | further-type | C28<-C12 | mech contr | mech nec | paper | exclusion clause; shared-passage clause | As S026 (shared F109); also unclear whether C15, a step of C12's case C13, counts as a part of C12. |
| S030 | further-type | C29<-C12 | mech contr | mech nec | paper | exclusion clause; shared-passage clause | As S026 (shared F109). |
| S031 | further-one | C12<-C13 | ev nec | none | void | Part 2 no-no clause | One-sided part 2 edge. |
| S032 | further-type | C13<-C17 | mech contr | ev contr | B | same-outcome clause, then Q3 | The sheet gives both outcomes as seekership, the same outcome, so Q2 is no and Q3 gives evidential. |
| S033 | further-one | C34<-C17 | none | ev contr | void | Part 2 no-no clause | One-sided part 2 edge. |
| S034 | further-one | C01<-C19 | none | mech nec | void | Part 2 no-no clause (and none-outcome clause) | One-sided, so no dispute; separately, B's type is one the text now rules out, since C01's outcome is none. |
| S035 | further-one | C11<-C20 | none | mech contr | void | Part 2 no-no clause | One-sided part 2 edge. |
| S036 | further-one | C29<-C20 | mech nec | none | void | Part 2 no-no clause | One-sided part 2 edge. |
| S037 | further-one | C29<-C21 | none | mech nec | void | Part 2 no-no clause | One-sided part 2 edge. |
| S038 | further-one | C34<-C27 | ev contr | none | void | Part 2 no-no clause | One-sided part 2 edge. |
| S039 | factor-one | F1, A: successful sensebreaking, C27 | given | none | open | Part 4, level sentence and lowest-number rule | B's F4 (S040) is the same seekership factor at the practice level, so the dispute is name and claim; the text does not choose process or practice level, and whether joint statements (C02, C03, C07) count as stating it decides between C27 and a lower claim. |
| S040 | factor-one | F4, B: dream building generates seekership, C13 | none | given | open | Part 4, as S039 | Mirror of S039: at the practice level C07 states it jointly and C13's own outcome is seekership, so whether C13 or C07 is the claim, or the process name wins, is left open. |
| S041 | contrast | CP02, F3 (distancing from outsiders) | held | unclear | paper | Part 6, kind-level sentence | Neither side's passage (F97, F103) mentions outsider ties on the sheet; A's held seems to rest on the kind-level F99/F107, which counts only if the paper applies it to those two members. |
| S042 | contrast | CP03, F2 (upline bonds) | held | unclear | paper | Part 6, kind-level sentence | F104 says nothing of upline ties on the sheet; A's held draws on kind-level F79/F107, which counts only where the paper extends it to that member. |

## Counts

| sheet | A | B | other | void | paper | open | total |
|---|---|---|---|---|---|---|---|
| bechky | 3 | 1 | 0 | 3 | 14 | 2 | 23 |
| pratt | 12 | 1 | 0 | 8 | 19 | 2 | 42 |
| all | 15 | 2 | 0 | 11 | 33 | 4 | 65 |

Where the text excludes one coder's answer but the page must still decide:
- excludes B, leaves A or other: pratt S002, S008, S014, S021.
- excludes A, leaves B or other: bechky S014.
- removes A's stated ground, leans B unless a shared passage counts: pratt S026, S029, S030; leans A on a new ground: pratt S027.
- removes B's stated ground, leans A unless a shared passage counts: bechky S017, S018; pratt S018 (edge itself still needs the page).

## Places in v2.1 where two careful coders could still part

1. Only-case clause against the shared-passage clause (Part 1, Strength and the
   paragraph after it). When Cj itself lists passages on the same unit as Ci,
   Ci is still the one case of that side, yet those passages are Cj's own and
   may count as another source. Bechky S010; the same clash sits under the
   agreed bechky edges P039 and P054.
2. Stays-with-Ck clause against Q3 and the exclusion clause. A passage listed
   under Ci and some Ck but not Cj stays with Ck when Ci is set aside, yet Q3
   counts it as Ci's support for Cj and the exclusion clause bars it as another
   source. Bechky S005, S008, S013, S017, S018.
3. Direct-tie rule, second sentence. It drops the first sentence's condition
   that Ci be a case, part or step of Ck. Read without it, two claims that give
   Cj the same thing each route through the other and both pairs come out
   false (pratt C01 on C12 and C01 on C13).
4. Direct-tie rule, last sentence. Its list of what Ck may leave out (case,
   passage, step) omits the finding that Q3 lists, so a claim whose passages
   Cj already holds may or may not give Cj something (pratt S012, S023).
5. Shared-passage clause, the words "by itself". No guide to whether a figure
   or summary passage (pratt F108, F109, F79; bechky F166, F172) alone gives
   what a whole claim gives; nor whether "something else" may be several
   claims taken together (bechky S009).
6. Exclusion clause. Unclear whether a part of a case of Ci (pratt C15, a step
   of C13, which is a case of C12) is itself a part of Ci.
7. Q2 same-outcome clause. It compares outcomes worded differently on the
   sheet; whether "part of" is read off the outcome lines or the paper is
   unsaid (pratt S015).
8. Q4. How explicit the paper's own statement must be (for instance a general
   statement of the paper's contribution) is unsaid (bechky S001, S003, S011).
9. Part 4. The level sentence contrasts unit with episode but does not choose
   between a process name and a practice name for one variable, and the
   lowest-number rule does not say whether a claim stating two factors jointly
   states each one (pratt S039, S040).
10. Part 3. The qualifier rule covers names sharing a head word; for names
    worded differently (bechky S022) only the stand-in test remains.
11. Part 6. "Applies it to that side" does not say whether placing a side's
    member in the kind (for example F103 under inactive distributors) is
    enough (pratt S041, S042).

Aside, outside the 65 items: the agreed pratt registry gives the turnover group
two canonical names (A turnover, B membership turnover); both names have one
claim each, and the Part 3 tie rule picks the first in the sheet's list,
membership turnover.
