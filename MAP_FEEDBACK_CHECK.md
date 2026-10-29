# The map test (T39): the blind attribution of the maps' disagreements, beside the PI's feedback file

*19 Oct 2026, at the end of T39.* The feedback file (`Feedback_map_task_instructions.txt`) was to be opened only at the very end of the test, and its value judged by where the maps' disagreements can be put down to the map task's instructions. Counts made by script; the comparison of points is a reading, set out so that it can be checked line by line.

## What was done

- **First, the attribution.** Made independently, with only `MAP_TASK.md`, the two map sheets, the coders' two fixed messages, the four map replies and the two settle keys (the 23 and 42 items where the maps differ, with both answers and reasons), and not the feedback file, it judged for each disagreement whether it can be put down to the instructions. Its report is at the foot.
- **Then the feedback file** (sha256 opens 3a15cbab) was opened for this comparison. Its text had been read once before, when it arrived on 18 Oct; it was used for nothing until now, and the attribution did not see it. It holds two responses, Argon's and ChatGPT's, each given `MAP_TASK.md`, Bechky's map sheet and the paper, and asked where the instructions might make two coders diverge, without seeing any map.

## The attribution, in short

All 65 disagreements trace to the instructions: 46 fully and 19 in part, none to the paper alone, none to the coders' message. By each item's main point:

| point | Bechky | Pratt | raised in the feedback |
|---|---|---|---|
| T3, chained ties: no rule for a claim tied to another only through an intermediate claim | 0 | 13 | ChatGPT, section 2 (direct and indirect dependencies) |
| T9, further edges: an optional selection of up to ten | 3 | 8 | Argon, Part 2; ChatGPT, section 12 |
| T7, strength: what the base gives, and whether a nested claim is another source | 3 | 7 | Argon, Part 1 (necessary or contributing in asymmetric cases, naming P051); ChatGPT, section 5 |
| T4, Q2 when a claim has no outcome, and whether a component is a step or a finding | 2 | 6 | Argon, Part 1 (the outcome-none paradox); ChatGPT, section 4 |
| T8, significance: what a claim's point is | 5 | 0 | Argon, Part 1 (directionality under significance, naming P003, P020 and P052); ChatGPT, section 5 |
| T2, passages shared by the two claims | 3 | 1 | Argon, Part 1 (the shared-passage trap); ChatGPT, section 3 |
| T1, the threshold: losing the reason or merely less support | 1 | 2 | ChatGPT, section 1 (competing thresholds) |
| T6, Q1: does a case claim count among the ranked explanations | 3 | 0 | ChatGPT, section 5 (naming P036, P056 and P076) |
| T10, the registry: a droppable qualifier or a kind; near-synonyms | 3 | 0 | Argon, Part 3 (naming both sets that split); ChatGPT, section 10 (the legitimacy names) |
| T11, a factor's level, and which claim states it | 0 | 2 | Argon, Part 4 (factor count); ChatGPT, section 6 |
| T12, held or not said in a contrast | 0 | 2 | Argon, Part 6; ChatGPT, section 9 |
| T5, an outcome that does not occur, as a condition | 0 | 1 | not raised |
| **all** | **23** | **42** | 11 of 12 points raised |

## Beside the feedback

- **The points:** the feedback raised 11 of the 12 points the attribution found, all but the outcome that does not occur. By main point, 23 of Bechky's 23 disagreements and 41 of Pratt's 42 fall under a point it raised, though it saw only Bechky's sheet. The largest single cause, chained ties (13 of Pratt's items, 11 of them on its umbrella claim C01), is ChatGPT's second point.
- **The pairs, Bechky:** the feedback named 41 of the 80 listed pairs as at risk (Argon 36, ChatGPT 10); 10 of them split (24%), against 15 of all 80 (19%). The split pairs it named: P003, P020, P035, P036, P047, P051, P052, P056, P074, P076. Never named: P015, P022, P037, P042, P073.
- **The construct names:** all three of Bechky's registry splits were named (the legitimacy names; meaning making and occupational interpretation), as were other name sets on which the two maps agreed.
- **Raised, with no disagreement:** the DNA unit in Part 5; the factors' order and count; the pathways' polarity and their coding as present or absent; held or varies in Bechky's two contrasts (Bechky's factors, units and controls agreed in full); the reciprocal pairs among C03 to C05 (P002, P049, P062, P071, none split); literature and method claims as bases (of the 11 pairs named for it, 1 split, P047); and the formats of basis, page and ids, which the test does not measure.

## How it reads

- As a list of where the instructions leave room, the feedback is close to complete: nearly every point behind a real disagreement is in it, with a fix, and the fixes for chained ties and for claims with no outcome would reach the most items.
- As a forecast of which items would split, it is broad: it named about half the pairs, about a quarter of those split, against a fifth of all pairs, and several of its main worries produced no disagreement.
- Limits: the attribution was asked whether each disagreement could be put down to the instructions, and found a point behind every one; neither it nor this comparison could read the paper; the feedback saw only Bechky; one attribution and two feedback responses.

## The attribution's report

All 65 disagreements are classified, 23 for Bechky and 42 for Pratt. **None came out "no"**: 46 trace fully to the instructions ("yes": 13 Bechky, 33 Pratt) and 19 partly (10 Bechky, 9 Pratt). None traces to the message to coders, which only sets reading order and output format. The classification and the counts below were made by a script that checks every item id and kind against both settle keys.

**Tags used in the table** (each is a place in MAP_TASK.md where the text is ambiguous, silent or self-conflicting):

| Tag | Point | Where in MAP_TASK.md |
|---|---|---|
| T1 | Threshold. The definition asks that Cj lose its reason, but a contributing edge and Q3 only need less support. | Part 1, Rests on vs Strength and Q3 (l. 40–45, 62–73) |
| T2 | Whether setting Ci aside also strips passages Ci shares with Cj or with a nested claim. | Part 1, Rests on and Q3 (l. 40–42, 62–64) |
| T3 | No rule on a chained tie, where Ci supports Cj only through an intermediate claim. | Part 1, Rests on / The test |
| T4 | Q2 is unclear when Cj's outcome is `none`, and for a component claim: is it a step or a finding? | Part 1, The test Q2; How to read the sheet, outcome (l. 23, 59–61) |
| T5 | Q2 says nothing about an account that turns on Ci's outcome *not* occurring. | Part 1, Q2 |
| T6 | Q1: does a case claim that applies the ranked explanation count as one of the ranked explanations? | Part 1, Q1; An example (l. 57–58, 155–157) |
| T7 | Strength: what Ci gives (a specific term or side, or support in general), and whether a nested claim counts as another source. | Part 1, Strength (l. 68–73) |
| T8 | What a claim's "point" is. | Part 1, significance type and Q4 (l. 43–45, 52, 65–66) |
| T9 | Further edges are an optional selection of up to ten, ranked loosely, so leaving one out is not a "no". | Part 2 (l. 87–89) |
| T10 | Is a qualifier droppable, or does it mark a kind? No test for near-synonyms. | Part 3 (l. 93–99) |
| T11 | At what level to name a factor, and which claim states it. | Part 4 (l. 103–107) |
| T12 | "Held" vs "not said": may a side's value be inferred from the class the episode belongs to? | Part 6 (l. 120–123) |

## 1. Item table

| Paper | Item | Kind | Attr. | Part (tag) | Reason |
|---|---|---|---|---|---|
| Bechky | S001 P003 C05←C01 | pair-edge | yes | Part 1 significance/Q4 (T8) | Both say C05 keeps its support; they split on whether its role inside the umbrella claim C01 counts as its point. |
| Bechky | S002 P015 C20←C05 | pair-edge | partly | T8, T4 | A finds a point for C20 (outcome none) that needs C05; B argues from derivation only; also a different reading of p. 637. |
| Bechky | S003 P020 C04←C01 | pair-edge | yes | T8 | Same split as S001. |
| Bechky | S004 P022 C20←C04 | pair-edge | partly | T8, T4, T7 | As S002; A grades it contributing because C05 shares the point. |
| Bechky | S005 P035 C05←C13 | pair-edge | partly | Rests on + Q3 (T2), T1 | B's basis is passages listed under both claims; open whether shared passages make a tie; C05's support is also read differently. |
| Bechky | S006 P036 C21←C18 | pair-type | yes | Q1 + example (T6) | The unit claim is both a case and a work-based explanation; the example only shows a general claim being ranked. |
| Bechky | S007 P037 C21←C10 | pair-edge | partly | T4, T1 | C10 supplies a premise (that the work differs) to a ranking with no outcome; the test doesn't place premises; content split too. |
| Bechky | S008 P042 C20←C13 | pair-edge | partly | T2, T1 | As S005: B's passages F145–F150 and F166 belong to both claims. |
| Bechky | S009 P047 C05←C10 | pair-edge | yes | T1, T4, T2 | Both say the unit descriptions show the differing values on their own; they split on whether that still leaves a contributing tie. |
| Bechky | S010 P051 C03←C17 | pair-type | yes | Strength (T7) | Both treat toxicology as the only immediate-route case; "what Ci gives" can mean that side's support or support overall. |
| Bechky | S011 P052 C03←C01 | pair-edge | yes | T8 | Same split as S001. |
| Bechky | S012 P056 C21←C17 | pair-type | yes | T6 | As S006. |
| Bechky | S013 P073 C13←C04 | pair-edge | partly | T2, T1 | As S005: B's passages F85, F100, F106 and F145–F147 belong to both claims. |
| Bechky | S014 P074 C13←C02 | pair-type | yes | Q2 (T4), T8 | C13 has no outcome; A applies Q2 to a condition it presupposes, B goes on to Q4; both rate it necessary. |
| Bechky | S015 P076 C21←C16 | pair-type | yes | T6 | As S006. |
| Bechky | S016 C04←C02 (A only) | further-one | yes | Part 2 (T9) | Optional ranked selection; B listed only five and nowhere rejects this edge. |
| Bechky | S017 C21←C04 | further-type | yes | T7 | Values and technique make up one work side: necessary if each half is a term, contributing if the side is. |
| Bechky | S018 C21←C05 | further-type | yes | T7 | As S017. |
| Bechky | S019 C01←C09 (A only) | further-one | yes | T9 | As S016. |
| Bechky | S020 C13←C10 (B only) | further-one | partly | T9, T2, T4 | A selection issue, but A's answers on C10 elsewhere (P037, P047) point to a real split. |
| Bechky | S021 legitimacy / symbolic legitimacy | constructs | partly | Part 3 (T10) | "Symbolic" may be a droppable qualifier or mark a kind (part and whole); neither map gives a reason. |
| Bechky | S022 meaning making / occupational interpretation | constructs | partly | T10 | No test for near-synonyms at different levels of generality; no reasons given. |
| Bechky | S023 occupational / symbolic legitimacy | constructs | partly | T10 | The same decision as S021, counted again. |
| Pratt | S001 P002 C01←C35 | pair-edge | yes | T4, T1, T3 | B makes C35's motivation link a step of C01's process (C01 has no outcome); A checks only C01's evidence and finds it stands. |
| Pratt | S002 P003 C01←C12 | pair-type | yes | T4, T7 | A component of an umbrella claim with no outcome: step or finding? Strength turns on whether C13, C12's instance, counts as another source. |
| Pratt | S003 P004 C28←C07 | pair-edge | yes | T2 | A's tie runs through F21, a passage of both claims; B says the pattern rests on the branch, not the reverse. |
| Pratt | S004 P006 C01←C23 | pair-edge | yes | T3, T4 | Sub-step of C20; A counts only direct ties to C01, B counts chained ones as mechanistic. |
| Pratt | S005 P013 C01←C14 | pair-edge | yes | T3, T4 | Sub-step of C13; same split. |
| Pratt | S006 P016 C01←C54 | pair-edge | partly | T3, T4 | A chained tie, plus a different reading of footnote 11 (an aside, or part of the mechanism). |
| Pratt | S007 P018 C01←C17 | pair-edge | yes | T3, T4 | Sub-step of C13; same split. |
| Pratt | S008 P023 C01←C21 | pair-edge | yes | T3, T4 | Sub-step of C20; same split. |
| Pratt | S009 P028 C11←C17 | pair-edge | partly | T3 | Sub-step of C13 (both accept C11←C13); they also differ on whether C11's account needs renewed seekership. |
| Pratt | S010 P035 C01←C13 | pair-type | yes | T4 | Type only: is the component practice a step or a finding? |
| Pratt | S011 P038 C01←C25 | pair-edge | yes | T3, T4 | Sub-step of C20; same split. |
| Pratt | S012 P039 C01←C18 | pair-edge | partly | T3, T2 | All of C18's passages sit under C01; they also differ on whether C18 is offered for C01 or for C38. |
| Pratt | S013 P040 C13←C54 | pair-edge | partly | T1 | Does a reinforcing side account count as a tie? Also read footnote 11's direction differently. |
| Pratt | S014 P046 C01←C20 | pair-type | yes | T4, T7 | As S002; strength turns on whether C21–C23, parts of C20, count as another source. |
| Pratt | S015 P048 C20←C23 | pair-type | yes | T4 | C23's outcome is one element of C20's (F79); Q2's line between a case and a step doesn't cover components. |
| Pratt | S016 P058 C20←C22 | pair-type | partly | T7 | What C22 gives: encapsulation in general, or blocking outside sources? Also whether C21 yields encapsulation. |
| Pratt | S017 P062 C34←C01 | pair-type | partly | T7, T8 | Both say significance; they differ on how much of C34's point survives without C01. |
| Pratt | S018 P068 C34←C33 | pair-edge | yes | T1 | B asks whether C33 is required, A whether it adds support; also whether a ventured proposition can count. |
| Pratt | S019 P076 C01←C22 | pair-edge | yes | T3, T4 | Sub-step of C20; same split. |
| Pratt | S020 P081 C20←C58 | pair-edge | partly | T3 | C58 explains why the mentoring condition failed; does that indirect route support C20? Also what the paper offers C58 for. |
| Pratt | S021 P083 C28←C20 | pair-edge | yes | Q2 (T5) | C28 turns on C20's outcome not forming; nothing says whether an absent outcome counts as a condition. |
| Pratt | S022 P084 C01←C15 | pair-edge | yes | T3, T4 | Sub-step of C13; same split. |
| Pratt | S023 P085 C01←C26 | pair-edge | partly | T3, T2 | C26's passages sit under C01; they also differ on whether C26 is offered for C01 or for C34. |
| Pratt | S024 P086 C13←C14 | pair-type | partly | T7, T2 | A's other source for the step is F28, which is itself one of C14's passages. |
| Pratt | S025 P087 C01←C24 | pair-edge | yes | T3, T4 | Sub-step of C20; same split. |
| Pratt | S026 C02←C12 | further-type | yes | T7, T2 | A counts C13 as another source of seekership; C13 is C12's instance and shares F48–F49 with it. |
| Pratt | S027 C11←C12 | further-type | yes | T7, T2 | As S026. |
| Pratt | S028 C27←C12 (A only) | further-one | yes | T9, T5 | Both maps used all ten slots; the edge also rests on an absent outcome, the kind B rejects in S021. |
| Pratt | S029 C28←C12 | further-type | yes | T7, T2 | As S026. |
| Pratt | S030 C29←C12 | further-type | yes | T7, T2 | As S026. |
| Pratt | S031 C12←C13 (A only) | further-one | yes | T9 | Ten-slot cap; nothing in B's map rejects it. |
| Pratt | S032 C13←C17 | further-type | yes | T4 | C17 has the same outcome as C13 (seekership); step or finding is not settled. |
| Pratt | S033 C34←C17 (B only) | further-one | yes | T9 | Ten-slot cap; A's own reason in S007 links C17 to C34. |
| Pratt | S034 C01←C19 (B only) | further-one | yes | T9, T3, T4 | Ten-slot cap, plus A's direct-only approach to C01. |
| Pratt | S035 C11←C20 (B only) | further-one | yes | T9 | Ten-slot cap. |
| Pratt | S036 C29←C20 (A only) | further-one | yes | T9, T5 | Ten-slot cap; a partial-outcome tie like S021. |
| Pratt | S037 C29←C21 (B only) | further-one | yes | T9, T3 | Ten-slot cap; B names the component (C21), A the practice (S036). |
| Pratt | S038 C34←C27 (A only) | further-one | yes | T9 | Ten-slot cap. |
| Pratt | S039 A's X1, from C27 | factor-one | yes | Part 4 (T11) | The same seekership factor as B's X1 (both say it varies in CP01), tied to a different claim at a different level. |
| Pratt | S040 B's X1, from C13 | factor-one | yes | T11 | Mirror of S039. |
| Pratt | S041 CP02, factor F3 | contrast | yes | Part 6 (T12) | A's ids add class-level passages on outsider ties (F99, F107); B's add only the claims and the two episodes. |
| Pratt | S042 CP03, factor F2 | contrast | yes | T12 | Same pattern: A adds F79, F107, C02 and C29 for upline ties. |

## 2. Points that account for most items

Counts are each item's main point; the figure in brackets counts every item the point is involved in.

| Point | Bechky | Pratt |
|---|---|---|
| T3: chained ties | 0 | 13 (16) |
| T9: further-edge selection | 3 | 8 |
| T7: strength, what Ci gives / nested claims | 3 (4) | 7 (9) |
| T4: Q2 with no outcome, and components | 2 (6) | 6 (16) |
| T8: significance, what a claim's point is | 5 (6) | 0 (1) |
| T2: shared passages | 3 (5) | 1 (8) |
| T1: threshold conflict | 1 (5) | 2 (3) |
| T6: Q1 scope | 3 | 0 |
| T10: registry rules | 3 | 0 |
| T11: factor level / which claim | 0 | 2 |
| T12: held vs not said | 0 | 2 |
| T5: absent outcome | 0 | 1 (3) |

- **Pratt:** one policy split over C01 accounts for 13 items. C01 is the umbrella claim, its outcome is none, and the sheet lists nearly every passage under it. A ties C01 only to its direct findings; B ties it to every sub-step, as mechanistic contributing edges.
- **Bechky:** the significance split runs both ways. B finds C03, C04 and C05 drawing their point from the umbrella claim C01; A finds C20 drawing its point from C04 and C05.

## 3. Items decided on thin grounds

None is left undecided outright, but these calls are less secure:

- **Bechky S021–S023:** neither map gives a reason, so it cannot be told whether they applied Part 3 differently or read the paper's usage differently. They are marked partly; they could be yes. S021 and S023 are the same decision counted twice.
- **Pratt S039–S042:** no reasons either; these are attributed from the names, claims and cited ids alone. S039 and S040 are one disagreement that the settle key split into two factors (F1 and F4).
- **Pratt S006 and S013, Bechky S002 and S004:** whether these are yes or partly depends on what footnote 11 and p. 637 actually do, which cannot be checked without the paper.
