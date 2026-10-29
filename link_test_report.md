# Link-definition test: results

Rules LINK_RULES_v1_1.md frozen 2026-09-29T09:20:24+00:00; sample built 2026-09-29T09:20:31+00:00, seed 29092026.

Each cell: Cohen's κ, Gwet's AC1 (steadier when one value dominates), raw agreement and n. Codes: five values (with, against, illustrates, qualifies, no link) and three (with, against, neither).

## v2 arm: chatgpt and opus

| field | random (42) | random linked | random unlinked | hard (18) |
|---|---|---|---|---|
| v2_link | κ 0.66, AC1 0.68, 83% of 42 | κ 0.46, AC1 0.88, 90% of 21 | κ 0.39, AC1 0.61, 76% of 21 | κ 0.61, AC1 0.85, 89% of 18 |
| v2_code | κ 0.71, AC1 0.72, 81% of 42 | κ 0.75, AC1 0.80, 86% of 21 | κ 0.44, AC1 0.70, 76% of 21 | κ 0.39, AC1 0.42, 56% of 18 |
| v2_code3 | κ 0.88, AC1 0.92, 95% of 42 | κ 0.80, AC1 0.82, 90% of 21 | κ 1.00, AC1 1.00, 100% of 21 | κ 0.45, AC1 0.53, 67% of 18 |

## new arm: chatgpt and opus

| field | random (42) | random linked | random unlinked | hard (18) |
|---|---|---|---|---|
| kind | κ 0.69, AC1 0.74, 86% of 42 | κ 0.79, AC1 0.83, 90% of 21 | κ 0.61, AC1 0.64, 81% of 21 | κ 1.00, AC1 1.00, 100% of 18 |
| use | κ 0.76, AC1 0.84, 88% of 42 | κ 0.77, AC1 0.79, 86% of 21 | κ 0.63, AC1 0.89, 90% of 21 | κ 0.55, AC1 0.60, 72% of 18 |
| author_link | κ 0.69, AC1 0.86, 90% of 42 | κ 0.67, AC1 0.75, 86% of 21 | κ 0.64, AC1 0.95, 95% of 21 | κ 0.37, AC1 0.52, 72% of 18 |
| condition | κ 0.76, AC1 0.92, 93% of 42 | κ 0.68, AC1 0.82, 86% of 21 | κ 1.00, AC1 1.00, 100% of 21 | κ 0.77, AC1 0.85, 89% of 18 |
| outcome | κ 0.43, AC1 0.71, 81% of 42 | κ 0.14, AC1 0.31, 62% of 21 | κ 1.00, AC1 1.00, 100% of 21 | κ 0.82, AC1 0.84, 89% of 18 |
| other_cause | κ 0.00, AC1 0.92, 93% of 42 | κ 0.00, AC1 0.90, 90% of 21 | κ 0.00, AC1 0.95, 95% of 21 | κ 0.00, AC1 0.88, 89% of 18 |
| bounded | κ —, AC1 1.00, 100% of 42 | κ —, AC1 1.00, 100% of 21 | κ —, AC1 1.00, 100% of 21 | κ —, AC1 1.00, 100% of 18 |
| evidence_link | κ 0.38, AC1 0.72, 81% of 42 | κ 0.16, AC1 0.46, 67% of 21 | κ 0.77, AC1 0.94, 95% of 21 | κ 0.88, AC1 0.90, 94% of 18 |
| code_v1 | κ 0.35, AC1 0.74, 79% of 42 | κ 0.22, AC1 0.58, 67% of 21 | κ 0.57, AC1 0.89, 90% of 21 | κ 0.89, AC1 0.93, 94% of 18 |
| code3_v1 | κ 0.23, AC1 0.86, 88% of 42 | κ -0.08, AC1 0.77, 81% of 21 | κ 0.64, AC1 0.95, 95% of 21 | κ 0.64, AC1 0.93, 94% of 18 |
| code_strict | κ 0.39, AC1 0.77, 81% of 42 | κ 0.18, AC1 0.58, 67% of 21 | κ 0.77, AC1 0.94, 95% of 21 | κ 0.77, AC1 0.85, 89% of 18 |
| code3_strict | κ 0.00, AC1 0.98, 98% of 42 | κ 0.00, AC1 0.95, 95% of 21 | κ —, AC1 1.00, 100% of 21 | κ 0.00, AC1 0.94, 94% of 18 |
| code_cov | κ 0.39, AC1 0.77, 81% of 42 | κ 0.18, AC1 0.58, 67% of 21 | κ 0.77, AC1 0.94, 95% of 21 | κ 0.77, AC1 0.85, 89% of 18 |
| code3_cov | κ 0.00, AC1 0.98, 98% of 42 | κ 0.00, AC1 0.95, 95% of 21 | κ —, AC1 1.00, 100% of 21 | κ 0.00, AC1 0.94, 94% of 18 |
| code_v2literal | κ 0.35, AC1 0.76, 79% of 42 | κ 0.22, AC1 0.58, 67% of 21 | κ 0.57, AC1 0.90, 90% of 21 | κ 0.90, AC1 0.93, 94% of 18 |
| code3_v2literal | κ 0.32, AC1 0.87, 88% of 42 | κ -0.08, AC1 0.77, 81% of 21 | κ 0.73, AC1 0.95, 95% of 21 | κ 0.83, AC1 0.93, 94% of 18 |

## Direction where both coders see a link

- v2, v2_code, random (42): κ 0.90, AC1 0.90, 95% of 21
- v2, v2_code, random linked: κ 0.89, AC1 0.89, 94% of 18
- v2, v2_code, random unlinked: κ —, AC1 1.00, 100% of 3
- v2, v2_code, hard (18): κ 0.33, AC1 0.39, 57% of 14
- v2, v2_code3, random (42): κ 0.90, AC1 0.90, 95% of 21
- v2, v2_code3, random linked: κ 0.89, AC1 0.89, 94% of 18
- v2, v2_code3, random unlinked: κ —, AC1 1.00, 100% of 3
- v2, v2_code3, hard (18): κ 0.33, AC1 0.39, 57% of 14
- new, code_v1, random (42): κ 0.50, AC1 0.53, 75% of 4
- new, code_v1, random linked: κ —, AC1 1.00, 100% of 2
- new, code_v1, random unlinked: κ 0.00, AC1 0.20, 50% of 2
- new, code_v1, hard (18): κ 1.00, AC1 1.00, 100% of 6
- new, code3_v1, random (42): κ 0.50, AC1 0.53, 75% of 4
- new, code3_v1, random linked: κ —, AC1 1.00, 100% of 2
- new, code3_v1, random unlinked: κ 0.00, AC1 0.20, 50% of 2
- new, code3_v1, hard (18): κ 1.00, AC1 1.00, 100% of 6

## Claim form

- form: κ 1.00, AC1 1.00, 100% of 33
- three-value code (v1.1), random rows whose claim got the same form from both: κ 0.23, AC1 0.86, 88% of 42

| claim | chatgpt: condition / form | opus: condition / form |
|---|---|---|
| C01 | none / describes | none / describes |
| C02 | both sensebreaking and sensegiving succeeding / produces | both sensebreaking and sensegiving succeeding / produces |
| C03 | either sensebreaking or sensegiving failing / produces | sensebreaking or sensegiving failing / produces |
| C06 | emotional valence of a persons reaction to amway / maps | the emotional valence of a persons reaction to amway / maps |
| C07 | success or failure combination of dream building and positive programming / maps | the success combination of dream building and positive programming / maps |
| C08 | variation in prospecting among already recruited members / none | variation in prospecting among already recruited members / none |
| C09 | greater financial success / none | greater financial success / none |
| C10 | visible demographic differences / none | visible demographic differences / none |
| C11 | motivated-sensemaking outcome about the self and organizational connection / maps | the outcome of motivated sensemaking about the self / maps |
| C12 | successful sensebreaking / produces | successful sensebreaking / produces |
| C13 | dream building successfully linking aspirations to the self and sustaining identity deficits / produces | dream building successfully linking aspirations to the self and sustaining identity deficits / produces |
| C14 | greater choice familiarity and emotional engagement in dreams / produces | dreams personalized around choice, familiarity and emotional appeal / produces |
| C18 | more sustained dream building / produces | sustained dream building / produces |
| C20 | more successful positive programming / produces | successful positive programming / produces |
| C21 | more enacted economic and emotional support from mentors / produces | mentors enacting both practical business help and personal care / produces |
| C22 | stronger relationship barriers / produces | strong barriers from revaluing outside relationships against the amway standard / produces |
| C23 | greater encapsulation / produces | encapsulation / produces |
| C25 | prospect acceptance or rejection / produces | a recruiting interaction ending in either acceptance or rejection by a prospect / produces |
| C26 | stronger positive identification / produces | positive identification having formed / produces |
| C27 | sensebreaking failing / produces | sensebreaking failing to create or sustain seekership / produces |
| C28 | successful sensebreaking combined with failed sensegiving / produces | sensebreaking succeeding while sensegiving fails / produces |
| C29 | successful sensebreaking combined with partially successful sensegiving / produces | sensebreaking succeeding while sensegiving is only partly effective / produces |
| C31 | more favorable outsider regard / produces | favorable outsider regard for the organization / produces |
| C34 | none / describes | none / describes |
| C35 | stronger current-ideal self discrepancy / produces | a large discrepancy between current and ideal self / produces |
| C36 | identification having formed / produces | identification having formed / produces |
| C37 | none / describes | none / describes |
| C40 | more encapsulated sensemaking when face-to-face contact is infrequent / produces | encapsulated sensemaking / produces |
| C42 | more intensive identification management / produces | intensive identification management / produces |
| C47 | more direct participation in informants work / produces | direct participation in informants work / produces |
| C49 | prospect acceptance or refusal leaving a balanced relationship configuration / produces | a balanced relationship configuration after a prospect accepts or refuses / produces |
| C50 | more seekership in part-time contingent or voluntary membership settings / produces | seekership / produces |
| C51 | more seekership during prolonged professional socialization / produces | seekership / produces |

## The new rules against v2, paired bootstrap on the 42 random rows

- link: κ(new) − κ(v2), 95% interval -0.66 to +0.07 (2000 resamples)
- three-value code: κ(new) − κ(v2), 95% interval -1.03 to -0.26 (1992 resamples)

## Within each model: its v2 codes against its own stub observations read by v2's box

Computed without kind or use, on the rows the model linked under v2.

- chatgpt: κ 0.60, AC1 0.65, 76% of 37
- opus: κ 0.52, AC1 0.64, 74% of 42

## Against the extractor's own codes (information only)

- new, chatgpt: κ 0.12, AC1 0.30, 43% of 60
- new, human: κ 0.22, AC1 0.37, 55% of 20
- new, opus: κ 0.22, AC1 0.37, 50% of 60
- v2, chatgpt: κ 0.52, AC1 0.57, 67% of 60
- v2, opus: κ 0.66, AC1 0.70, 77% of 60

## Stub against page: the re-check rows, within each coder

| coder | row | pair | stub: c / o / x / b | page: c / o / x / b | v1.1 code, stub → page |
|---|---|---|---|---|---|
| chatgpt | R01 | F24→C28 | not shown / not shown / no / no | not shown / not shown / no / no | no link → no link |
| chatgpt | R03 | F29→C13 | not shown / not shown / no / no | present / not shown / no / no | no link → illustrates |
| chatgpt | R18 | F98→C21 | not shown / not shown / no / no | absent / other way / no / no | no link → illustrates |
| chatgpt | R20 | F97→C21 | absent / not shown / no / no | absent / other way / no / no | illustrates → illustrates |
| chatgpt | R21 | F119→C51 | not shown / not shown / no / no | not shown / not shown / no / no | no link → no link |
| chatgpt | R26 | F69→C31 | absent / not shown / no / no | absent / other way / no / no | illustrates → illustrates |
| chatgpt | R27 | F25→C09 | present / not shown / no / no | present / not shown / no / no | illustrates → illustrates |
| chatgpt | R31 | F93→C27 | not shown / not shown / no / no | not shown / not shown / no / no | no link → no link |
| chatgpt | R36 | F24→C09 | present / not shown / no / no | present / not shown / no / no | illustrates → illustrates |
| chatgpt | R43 | F106→C01 | not shown / not shown / no / no | not shown / not shown / no / no | no link → no link |
| chatgpt | R47 | F93→C20 | not shown / other way / no / no | absent / other way / no / no | illustrates → illustrates |
| chatgpt | R49 | F47→C18 | not shown / as asserted / no / no | present / as asserted / no / no | with → with |
| chatgpt | R56 | F104→C03 | not shown / not shown / no / no | present / as asserted / no / no | no link → with |
| chatgpt | R57 | F85→C20 | not shown / as asserted / yes / no | not shown / as asserted / no / no | illustrates → with |
| chatgpt | R60 | F31→C14 | present / not shown / no / no | present / not shown / no / no | illustrates → illustrates |
| opus | R01 | F24→C28 | not shown / not shown / no / no | not shown / not shown / no / no | no link → no link |
| opus | R03 | F29→C13 | not shown / not shown / no / no | not shown / not shown / no / no | no link → no link |
| opus | R18 | F98→C21 | not shown / not shown / no / no | absent / other way / no / no | no link → illustrates |
| opus | R20 | F97→C21 | absent / not shown / no / no | absent / other way / no / no | illustrates → illustrates |
| opus | R21 | F119→C51 | not shown / not shown / no / no | not shown / not shown / no / no | no link → no link |
| opus | R26 | F69→C31 | absent / not shown / no / no | absent / other way / no / no | illustrates → illustrates |
| opus | R27 | F25→C09 | present / not shown / no / no | present / not shown / no / no | illustrates → illustrates |
| opus | R31 | F93→C27 | not shown / as asserted / no / no | not shown / as asserted / yes / no | with → illustrates |
| opus | R36 | F24→C09 | present / not shown / no / no | present / not shown / no / no | illustrates → illustrates |
| opus | R43 | F106→C01 | not shown / not shown / no / no | not shown / not shown / no / no | no link → no link |
| opus | R47 | F93→C20 | not shown / other way / no / no | not shown / other way / yes / no | illustrates → illustrates |
| opus | R49 | F47→C18 | not shown / not shown / no / no | present / as asserted / no / no | no link → with |
| opus | R56 | F104→C03 | not shown / not shown / no / no | present / as asserted / no / no | no link → with |
| opus | R57 | F85→C20 | not shown / as asserted / no / no | not shown / as asserted / no / no | with → with |
| opus | R60 | F31→C14 | present / not shown / no / no | present / not shown / no / no | illustrates → illustrates |

chatgpt: the page changed the derived code on 4 of 15 re-check rows.

opus: the page changed the derived code on 4 of 15 re-check rows.

## Your sheet against each model (new rules)

- chatgpt, kind: κ 0.83, AC1 0.93, 95% of 20
- chatgpt, use: κ 0.59, AC1 0.74, 80% of 20
- chatgpt, author_link: κ 0.58, AC1 0.63, 80% of 20
- chatgpt, evidence_link: κ 0.89, AC1 0.91, 95% of 20
- chatgpt, code3_v1: κ 1.00, AC1 1.00, 100% of 20
- opus, kind: κ 1.00, AC1 1.00, 100% of 20
- opus, use: κ 0.70, AC1 0.80, 85% of 20
- opus, author_link: κ 0.69, AC1 0.72, 85% of 20
- opus, evidence_link: κ 0.56, AC1 0.63, 80% of 20
- opus, code3_v1: κ -0.07, AC1 0.83, 85% of 20

## The hard cases

The two new-rules models agree on the five-value code (v1.1) for 17 of 18 hard rows. Two coders answering at random would agree on 8.7 on average, and on 12 or fewer 95% of the time.
New-rules models splitting alike rows into `with` and `against`: none.
v2 chats doing so (information): none.

| row | pair | extractor | new chatgpt | new human | new opus | v2 chatgpt | v2 opus |
|---|---|---|---|---|---|---|---|
| R02 | F99→C23 | with | reading/none; no link (reading) | reading/none; no link (reading) | reading/none; no link (reading) | against | with |
| R03 | F29→C13 | illustrates | report/evidence; no link | ?/?; ? | report/none; no link | illustrates | illustrates |
| R05 | F72→C20 | illustrates | reading/evidence; no link (reading) | ?/?; ? | reading/none; no link (reading) | with | with |
| R13 | F20→C08 | with | reading/restatement; no link (reading) | ?/?; ? | reading/restatement; no link (reading) | with | with |
| R16 | F83→C20 | no link | report/evidence; no link | ?/?; ? | report/evidence; with (outcome only) | with | with |
| R17 | F93→C23 | against | report/none; illustrates (outcome other way, condition unknown) | ?/?; ? | report/none; illustrates (outcome other way, condition unknown) | against | illustrates |
| R18 | F98→C21 | against | report/none; no link | ?/?; ? | report/none; no link | no link | no link |
| R20 | F97→C21 | with | report/none; illustrates (condition only) | report/evidence; illustrates (negative case) | report/none; illustrates (condition only) | illustrates | with |
| R24 | F10→C20 | illustrates | report/none; no link | ?/?; ? | report/none; no link | illustrates | illustrates |
| R27 | F25→C09 | illustrates | report/none; illustrates | report/evidence; illustrates | report/evidence; illustrates | no link | illustrates |
| R28 | F96→C28 | with | report/evidence; with (outcome only) | ?/?; ? | report/evidence; with | with | with |
| R33 | F109→C29 | with | reading/restatement; no link (reading) | ?/?; ? | reading/restatement; no link (reading) | illustrates | illustrates |
| R35 | F99→C20 | with | reading/evidence; no link (reading) | ?/?; ? | reading/none; no link (reading) | against | with |
| R36 | F24→C09 | illustrates | report/evidence; illustrates | ?/?; ? | report/evidence; illustrates | no link | illustrates |
| R38 | F88→C27 | with | reading/restatement; no link (reading) | ?/?; ? | reading/restatement; no link (reading) | illustrates | with |
| R45 | F73→C20 | with | reading/evidence; no link (reading) | ?/?; ? | reading/none; no link (reading) | with | with |
| R47 | F93→C20 | against | report/none; illustrates (outcome other way, condition unknown) | ?/?; ? | report/none; illustrates (outcome other way, condition unknown) | against | illustrates |
| R53 | F12→C20 | no link | report/none; no link | report/none; no link | report/none; no link | no link | no link |

## The pass bar

Recorded 2026-09-30T04:07:44+00:00. Pass only if all hold: on the 42 random rows, κ of at least 0.60 between the two model coders for the author link, the evidence link, and the three-value code under v1 and strict; κ for claim form of at least 0.60; the new rules no worse than v2 by more than 0.10 in κ for the link and the three-value code (the lower end of a paired bootstrap 95% interval); the two new-rules models agreeing on the five-value code for more of the 18 hard rows than two coders answering at random would 95% of the time; neither new-rules model giving `with` to one hard row and `against` to its twin. A κ that cannot be computed counts as not passed. The human check is a sense check, not gated.

- author_link, κ ≥ 0.60: κ 0.69: PASS
- evidence_link, κ ≥ 0.60: κ 0.38: NOT PASSED
- code3_v1, κ ≥ 0.60: κ 0.23: NOT PASSED
- code3_strict, κ ≥ 0.60: κ 0.00: NOT PASSED
- claim form, κ ≥ 0.60: κ 1.00: PASS
- link, no worse than v2 by more than 0.10: lower end -0.66: NOT PASSED
- three-value code, no worse than v2 by more than 0.10: lower end -1.03: NOT PASSED
- hard rows agreed beyond the random-answer 95th percentile: 17 against 12: PASS
- no alike hard rows split into with and against: 0 found: PASS

**Overall: NOT PASSED**
