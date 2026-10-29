# T27: the figures for the proposal: Bechky 2020

Written by `build_figures.py` from the results files that each row names. Nothing in it is typed, and nothing here changes a figure of any results file. Every kappa of the cold papers' codings is model against model: coder 1 is the extraction (ChatGPT), coder 2 is Opus 5.5. Rows marked *new* hold figures that no results file held before (see the script's docstring).

## 1. The record

| figure | value | source |
|---|---|---|
| First return: fragments (of them coded `reported` by its own voice file) | 168 (99 `reported`) | `bechky_2020_corpus.json`, `bechky_2020_voice_gloss.json` |
| First return: claims; links by direction | 23 claims; 290 links: 59 `with`, 0 `against`, 221 `illustrates`, 10 `qualifies` | `bechky_2020_corpus.json` |
| The PI's coverage check: passages listed | 15 (16 lines, of which 1 repeat(s) an earlier line) | `bechky_2020_coverage_list.txt` |
| The coverage chat: what it added to the first return, and what of the first return it changed | 4 fragments, 0 claims, 3 links added; changed: none; in the head: printed_fragment_count | `bechky_2020_corpus.json` and `bechky_2020_coverage_corpus.json`, record by record |
| The frozen record: fragments, claims, links; what the freeze changed in the coverage chat's return | 172 fragments, 23 claims, 293 links; records added: 0; changed: none; in the head: fieldwork_scale | `bechky_2020_v1.json`, `bechky_2020_coverage_corpus.json` |
| The frozen record: claims that name an outcome (directional), core, stated as | 18 directional of 23; 7 core; 19 established, 4 ventured | `bechky_2020_v1.json` (`agreement.directional_claims`) |
| The frozen record: voice, coder 1's (the extraction's sidecar) | 70 `author_insight`, 102 `reported` | `bechky_2020_v1_voice_gloss.json` |

## 2. Agreement, model against model

| figure | value | source |
|---|---|---|
| Records compared | 172 fragments, 23 claims (18 directional), 293 links | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage A: whether a claim names an outcome | n = 23; raw agreement 0.957 (22 of 23); kappa 0.881 (95% interval 0.57 to 1.00; 1,995 of 2,000 resamples gave a kappa) | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage A: claims where both name an outcome, the two wordings by reading | 17 claims: 1 different variable, 14 match, 2 polarity inverted | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage A2: the asserted direction's sign, by reading | 18 claims sent; coder 2 gives a direction on 18, none on 0; the sign by reading: 18 agree | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage V: voice | n = 172; raw agreement 0.936 (161 of 172); kappa 0.865 (95% interval 0.78 to 0.94) | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage B: link direction, all links | n = 293; raw agreement 0.918 (269 of 293); kappa 0.796 (95% interval 0.72 to 0.87) | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage B: link direction, links to directional claims | n = 231; raw agreement 0.896 (207 of 231); kappa 0.778 (95% interval 0.70 to 0.85) | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage B: core | n = 23; raw agreement 0.696 (16 of 23); kappa 0.309 (95% interval -0.14 to 0.70) | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage B: stated as | n = 23; raw agreement 1.000 (23 of 23); kappa 1.000 (95% interval 1.00 to 1.00; 1,975 of 2,000 resamples gave a kappa) | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage B: gap kind | n = 3; raw agreement 1.000 (3 of 3); kappa withheld (fewer than 10 judgements) | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage B: pair drawn by authors | n = 2; raw agreement 1.000 (2 of 2); kappa withheld (fewer than 10 judgements) | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage B: resolution period | n = 1; raw agreement 1.000 (1 of 1); kappa withheld (fewer than 10 judgements) | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage B: gloss relation | n = 20; raw agreement 0.700 (14 of 20); kappa 0.318 (95% interval -0.10 to 0.70) | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |

## 3. `against` and the audit, in both versions

| figure | value | source |
|---|---|---|
| `against` links, coder 1 (the extraction), as coded | none | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| `against` links, coder 1 (the extraction), with the flagged links as `illustrates` | none (flagged: 0; answered 4a: 0) | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| `against` links, coder 2 (Opus 5.5), as coded | 5 on 1 claim(s); at most 5 on one claim (C02); claims with two or more: C02 | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| `against` links, coder 2 (Opus 5.5), with the flagged links as `illustrates` | none (flagged: 5; answered 4a: 0) | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| The audit under coder 1, as coded | coverage 0.111 (2 of 18 directional claims assessed); seams: 0 | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| The audit under coder 1, with the flagged links as `illustrates` | coverage 0.111 (2 of 18 directional claims assessed); seams: 0 | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| The audit under coder 2, as coded | coverage 0.111 (2 of 18 directional claims assessed); seams: 0 | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| The audit under coder 2, with the flagged links as `illustrates` | coverage 0.111 (2 of 18 directional claims assessed); seams: 0 | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| The audit's floor and rule | no rate is reported under coverage 0.60; a claim is assessed with at least 4 `with` or `against` links from fragments not in the author's voice | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |

## 4. The wager test (T29)

| figure | value | source |
|---|---|---|
| The system's readings (cards) and the attack (GPT 6 Astra) | 4 cards: 2 killed (2 of them under B, import), 2 survived | `stage2/attack_results.md` |
| The markers (Opus 5.5 and GPT 6 Astra), seven codes *new* | 158 of 193 sentences agree (0.819); kappa 0.706 (95% interval 0.62 to 0.78); the interval is new | `stage2/marker_results/RESULTS.md`; the interval from the two replies and the key (new) |
| The markers, four groups (a diagnostic only) | agreement 0.860, kappa 0.711 | `stage2/marker_results/RESULTS.md` |
| By arm, Opus 5.5 / GPT 6 Astra: resolution rate (R, RI, RA) | system 95% / 87%; middle 100% / 93%; plain 98% / 70% | `stage2/marker_results/RESULTS.md` |
| By arm, Opus 5.5 / GPT 6 Astra: strict rate (R) | system 75% / 71%; middle 81% / 74%; plain 86% / 63% | `stage2/marker_results/RESULTS.md` |
| By arm, Opus 5.5 / GPT 6 Astra: sentences that report (not N) | system 55 / 55; middle 27 / 27; plain 63 / 70 | `stage2/marker_results/RESULTS.md` |
| The PI's worth, system arm (0 to 3; declared not blind) | mean 1.75 over 4 readings; rated 2 or more: 3 of 4 | `stage2/worth/worth_joined.json`, checked against `stage2/worth/WORTH_RESULTS.md` |
| The PI's worth, middle arm (0 to 3; declared not blind) | mean 0.60 over 5 readings; rated 2 or more: 1 of 5 | `stage2/worth/worth_joined.json`, checked against `stage2/worth/WORTH_RESULTS.md` |
| The PI's worth, plain arm (0 to 3; declared not blind) | mean 2.00 over 5 readings; rated 2 or more: 5 of 5; without the 1 rated late, mean 2.00 | `stage2/worth/worth_joined.json`, checked against `stage2/worth/WORTH_RESULTS.md` |
| Gap in the PI's mean worth (declared not blind), system against middle (the reading chats) (p by relabelling) | +1.15 (p 0.087) | `stage2/worth/WORTH_RESULTS.md` |
| Gap in the PI's mean worth (declared not blind), system against plain (the plain chats) (p by relabelling); the plain arm's mean includes the readings the PI rated late | -0.25 (p 0.444) | `stage2/worth/WORTH_RESULTS.md` |
| Gap in the PI's mean worth (declared not blind), middle (the reading chats) against plain (the plain chats) (p by relabelling); the plain arm's mean includes the readings the PI rated late | -1.40 (p 0.048) | `stage2/worth/WORTH_RESULTS.md` |

## 5.1 Added after the plan: T31, the judges (Gemini 3.1 Pro)

| figure | value | source |
|---|---|---|
| Rows where the two codings differ, as the judge sorted them | 35 rows: both held 11; only coder 1's held 11; only coder 2's held 12; neither held 1 | `judge_results.json`, checked against `JUDGE_RESULTS.md` |
| How far the judge can be trusted: statements both codings made, and none made, held | both made: 12 of 14 held; neither made: 1 of 7 held | `judge_results.json` |

## 5.2 Added after the plan: T32, readings at places

| figure | value | source |
|---|---|---|
| Its markers (Opus 5.5 and GPT 6 Astra), seven codes *new* | 121 of 150 sentences agree; kappa 0.669 (95% interval 0.56 to 0.77); the interval is new | `places_marker_results.json`; the interval from the two replies and the key (new) |
| By chat: readings | places given (chat 45): 4; places found (chat 46): 4 | `PLACES_RESULTS.md` |
| By chat: worth, mean | places given (chat 45): 1.50; places found (chat 46): 1.50 | `PLACES_RESULTS.md` |
| By chat: worth 3, 2, 1, 0 | places given (chat 45): 0, 2, 2, 0; places found (chat 46): 0, 2, 2, 0 | `PLACES_RESULTS.md` |
| By chat: resolution (Opus 5.5 / GPT 6 Astra) | places given (chat 45): 91% / 93%; places found (chat 46): 88% / 92% | `PLACES_RESULTS.md` |

## 5.3 Added after the plan: T33, the matching test

| figure | value | source |
|---|---|---|
| Arm A (the PDF only): the two coders' groupings, pair kappa *new* | kappa 0.923 (95% interval 0.67 to 1.00); the interval is new | `matching_results.json`; the interval by resampling the readings (new) |
| Arm B (the PDF and the reference): grouping by claim number, pair kappa *new* | kappa 0.886 (95% interval 0.67 to 1.00); the interval is new | `matching_results.json`; the interval by resampling the readings (new) |
| Arm B: grouping by judgment, pair kappa *new* | kappa 0.846 (95% interval 0.62 to 1.00); the interval is new | `matching_results.json`; the interval by resampling the readings (new) |
| Agreement with the PI's grouping, arm A (mean of the two coders) *new* | kappa 0.628 (95% interval 0.34 to 0.89); the interval is new | `matching_results.json`; the interval by resampling the readings (new) |
| Agreement with the PI's grouping, arm B by claim number *new* | kappa 0.762 (95% interval 0.49 to 0.96); the interval is new | `matching_results.json`; the interval by resampling the readings (new) |
| Agreement with the PI's grouping, arm B by judgment *new* | kappa 0.777 (95% interval 0.51 to 0.96); the interval is new | `matching_results.json`; the interval by resampling the readings (new) |
| Difference B - A | -0.037 (95% interval -0.30 to 0.29) | `matching_results.json` |
| Difference Bj - A | -0.077 (95% interval -0.37 to 0.28) | `matching_results.json` |
| Difference P_B - P_A | 0.134 (95% interval -0.09 to 0.38) | `matching_results.json` |
| Difference P_Bj - P_A | 0.149 (95% interval 0.02 to 0.32) | `matching_results.json` |
| Arm B's two coders' claim tags on the 28 readings *new* | kappa 0.836 (95% interval 0.68 to 0.96); the interval is new | `matching_results.json`; the interval by resampling the readings (new) |
| Claims the readings contest, by arm B's tags (of the paper's 23) | 9 under both coders' tags; 11 under either | `matching_results.json` |
| Recurrence across vendors (Q2) | of the 5 points two or more Fable chats reached, both GPT 6 Astra runs reached 3; 7 of the 10 new readings joined a group with an earlier one | `matching_results.json` |
| Arm B's citations of passages for the 28 readings, by the frozen record's voice (described, not tested) | 240 of 271 name reported material; 52 distinct passages, 42 of them reported | `matching_results.json`; distinct passages from `reply_53_match_b_opus.json` and `reply_54_match_b_astra.json` |
| The PI's worth (described, not tested: the PI knew their source, and rated after the results): the 10 new readings, and the 18 earlier ones | new: mean 2.40 (3: 4, 2: 6, 1: 0, 0: 0); earlier: mean 1.44 (3: 0, 2: 11, 1: 4, 0: 3) | `MATCHING_WORTH.md` |

## 5.4 Added after the plan: T34, the author's own worth

| figure | value | source |
|---|---|---|
| The author's ratings of the wager test's readings of the paper | no reply in | `author_ratings_key.json`; the folder |

## 5.5 Added after the plan: T35, the second extraction

| figure | value | source |
|---|---|---|
| Q1: the first return's 23 claims found in the other return | 21 by chat 56 (Opus 5.5), 21 by chat 57 (GPT 6 Astra), 21 by both | `second_extraction_results.json` |
| Q1: the new return's 39 claims found in the other return | 27 by chat 56 (Opus 5.5), 30 by chat 57 (GPT 6 Astra), 27 by both | `second_extraction_results.json` |
| Q1: the first return's 7 core claims found in the other return | 6 by chat 56, 6 by chat 57, 6 by both | `second_extraction_results.json` |
| Q1: the new return's 9 core claims found in the other return | 9 by chat 56, 9 by chat 57, 9 by both | `second_extraction_results.json` |
| Q1: the two matchers' agreement on claim pairs (the bar: 0.60) | kappa 0.661 (95% interval 0.46 to 0.86); 28 pairs by chat 56, 55 by chat 57 | `second_extraction_results.json` |
| Q2: passages outside the tables, the first return's found in the other | 83 of 128 (0.65) by both matchers | `second_extraction_results.json` |
| Q2: passages outside the tables, the new return's found in the other | 94 of 127 (0.74) by both matchers | `second_extraction_results.json` |
| Q2: passages with the table cells, the first return's found in the other | 123 of 168 (0.73) by both matchers | `second_extraction_results.json` |
| Q2: passages with the table cells, the new return's found in the other | 135 of 168 (0.80) by both matchers | `second_extraction_results.json` |
| Q2: the matchers' agreement on passage pairs | kappa 1.000: the two passage maps are identical, so this says nothing of the matchers' judgement | `second_extraction_results.json` |
| Q3: voice on the matched passages, first return against new (the bar: 0.80) | 130 of 140 alike; kappa 0.788 (95% interval 0.65 to 0.90); beside 0.865 for two codings of one extraction | `second_extraction_results.json` |
| Q3: voice on the matched passages, first / new | author_insight / author_insight: 25; author_insight / reported: 8; reported / author_insight: 2; reported / reported: 105 | `second_extraction_results.json` |
| The first return's passages coded `author_insight`, found again | 32 of 69 | `second_extraction_results.json` |
| The first return's passages coded `reported`, found again | 91 of 99 | `second_extraction_results.json` |
| The two returns: claims, core claims, passages, voice | first: 23 claims (7 core), 168 passages, 69 author_insight, 99 reported; new: 39 claims (9 core), 168 passages, 28 author_insight, 140 reported | `second_extraction_results.json` |
| The plan's answers, as the scorer gives them | Q1, the claims: repeat in part; Q2, the passages: repeat in part (with the table cells: repeat in part); Q3, voice: less steady (the voice kappa is at least 0.60 and under 0.80) | `second_extraction_results.json` |
| The first return: its `with` links, and how many rest on a passage it codes `author_insight` (new) *new* | 46 of 59 | `bechky_2020_corpus.json`, `bechky_2020_voice_gloss.json` (new) |
| The new return: its `with` links, and how many rest on a passage it codes `author_insight` (new) *new* | 13 of 72 | `bechky_2020_x2_corpus.json`, `bechky_2020_x2_voice_gloss.json` (new) |
