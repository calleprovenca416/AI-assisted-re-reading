# T27: the figures for the proposal: Pratt 2000

Written by `build_figures.py` from the results files that each row names. Nothing in it is typed, and nothing here changes a figure of any results file. Every kappa of the cold papers' codings is model against model: coder 1 is the extraction (ChatGPT), coder 2 is Opus 5.5. Rows marked *new* hold figures that no results file held before (see the script's docstring).

## 1. The record

| figure | value | source |
|---|---|---|
| First return: fragments (of them coded `reported` by its own voice file) | 121 (92 `reported`) | `pratt_2000_corpus.json`, `pratt_2000_voice_gloss.json` |
| First return: claims; links by direction | 52 claims; 422 links: 152 `with`, 3 `against`, 264 `illustrates`, 3 `qualifies` | `pratt_2000_corpus.json` |
| The PI's coverage check: passages listed | 14 | `pratt_2000_coverage_list.txt` |
| The coverage chat: what it added to the first return, and what of the first return it changed | 4 fragments, 8 claims, 30 links added; changed: F109 (citing_claims, stub); 18 fragment(s) in their list of citing claims only; in the head: printed_fragment_count | `pratt_2000_corpus.json` and `pratt_2000_coverage_corpus.json`, record by record |
| The frozen record: fragments, claims, links; what the freeze changed in the coverage chat's return | 125 fragments, 60 claims, 452 links; records added: 0; changed: F21 (stub) | `pratt_2000_v1.json`, `pratt_2000_coverage_corpus.json` |
| The frozen record: claims that name an outcome (directional), core, stated as | 56 directional of 60; 10 core; 39 established, 21 ventured | `pratt_2000_v1.json` (`agreement.directional_claims`) |
| The frozen record: voice, coder 1's (the extraction's sidecar) | 30 `author_insight`, 95 `reported` | `pratt_2000_v1_voice_gloss.json` |

## 2. Agreement, model against model

| figure | value | source |
|---|---|---|
| Records compared | 125 fragments, 60 claims (56 directional), 452 links | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage A: whether a claim names an outcome | n = 60; raw agreement 0.883 (53 of 60); kappa 0.483 (95% interval 0.13 to 0.78) | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage A: claims where both name an outcome, the two wordings by reading | 49 claims: 3 different variable, 45 match, 1 polarity inverted | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage A2: the asserted direction's sign, by reading | 56 claims sent; coder 2 gives a direction on 53, none on 3; the sign by reading: 51 agree, 2 unclear | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage V: voice | n = 125; raw agreement 0.968 (121 of 125); kappa 0.908 (95% interval 0.80 to 0.98) | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage B: link direction, all links | n = 452; raw agreement 0.867 (392 of 452); kappa 0.714 (95% interval 0.64 to 0.78) | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage B: link direction, links to directional claims | n = 322; raw agreement 0.814 (262 of 322); kappa 0.642 (95% interval 0.56 to 0.72) | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage B: core | n = 60; raw agreement 0.917 (55 of 60); kappa 0.732 (95% interval 0.47 to 0.93) | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage B: stated as | n = 60; raw agreement 0.950 (57 of 60); kappa 0.886 (95% interval 0.75 to 1.00) | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage B: gap kind | n = 4; raw agreement 0.750 (3 of 4); kappa withheld (fewer than 10 judgements) | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage B: pair drawn by authors | n = 3; raw agreement 1.000 (3 of 3); kappa withheld (fewer than 10 judgements) | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage B: resolution period | n = 1; raw agreement 1.000 (1 of 1); kappa withheld (fewer than 10 judgements) | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| Stage B: gloss relation | n = 11; raw agreement 0.818 (9 of 11); kappa 0.607 (95% interval -0.03 to 1.00; 1,999 of 2,000 resamples gave a kappa) | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |

## 2. Agreement, model against model — the second count

| figure | value | source |
|---|---|---|
| Records compared | 120 fragments, 52 claims (48 directional), 412 links | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |
| Stage A: whether a claim names an outcome | n = 52; raw agreement 0.885 (46 of 52); kappa 0.519 (95% interval 0.14 to 0.81) | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |
| Stage A: claims where both name an outcome, the two wordings by reading | 42 claims: 2 different variable, 39 match, 1 polarity inverted | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |
| Stage A2: the asserted direction's sign, by reading | 48 claims sent; coder 2 gives a direction on 45, none on 3; the sign by reading: 43 agree, 2 unclear | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |
| Stage V: voice | n = 120; raw agreement 0.975 (117 of 120); kappa 0.927 (95% interval 0.83 to 1.00) | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |
| Stage B: link direction, all links | n = 412; raw agreement 0.876 (361 of 412); kappa 0.722 (95% interval 0.65 to 0.79) | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |
| Stage B: link direction, links to directional claims | n = 284; raw agreement 0.820 (233 of 284); kappa 0.654 (95% interval 0.57 to 0.74) | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |
| Stage B: core | n = 52; raw agreement 0.904 (47 of 52); kappa 0.722 (95% interval 0.43 to 0.93) | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |
| Stage B: stated as | n = 52; raw agreement 0.981 (51 of 52); kappa 0.957 (95% interval 0.86 to 1.00) | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |
| Stage B: gap kind | n = 4; raw agreement 0.750 (3 of 4); kappa withheld (fewer than 10 judgements) | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |
| Stage B: pair drawn by authors | n = 3; raw agreement 1.000 (3 of 3); kappa withheld (fewer than 10 judgements) | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |
| Stage B: resolution period | n = 1; raw agreement 1.000 (1 of 1); kappa withheld (fewer than 10 judgements) | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |
| Stage B: gloss relation | n = 11; raw agreement 0.818 (9 of 11); kappa 0.607 (95% interval -0.03 to 1.00; 1,999 of 2,000 resamples gave a kappa) | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |

## 3. `against` and the audit, in both versions

| figure | value | source |
|---|---|---|
| `against` links, coder 1 (the extraction), as coded | 3 on 3 claim(s); at most 1 on one claim (C20, C21, C23); claims with two or more: none | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| `against` links, coder 1 (the extraction), with the flagged links as `illustrates` | none (flagged: 3; answered 4a: 0) | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| `against` links, coder 2 (Opus 5.5), as coded | 2 on 2 claim(s); at most 1 on one claim (C22, C25); claims with two or more: none | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| `against` links, coder 2 (Opus 5.5), with the flagged links as `illustrates` | 1 on 1 claim(s); at most 1 on one claim (C22); claims with two or more: none (flagged: 1; answered 4a: 0) | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| The audit under coder 1, as coded | coverage 0.161 (9 of 56 directional claims assessed); seams: 0 | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| The audit under coder 1, with the flagged links as `illustrates` | coverage 0.143 (8 of 56 directional claims assessed); seams: 0 | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| The audit under coder 2, as coded | coverage 0.107 (6 of 56 directional claims assessed); seams: 0 | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| The audit under coder 2, with the flagged links as `illustrates` | coverage 0.107 (6 of 56 directional claims assessed); seams: 0 | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| The audit's floor and rule | no rate is reported under coverage 0.60; a claim is assessed with at least 4 `with` or `against` links from fragments not in the author's voice | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |

## 3. `against` and the audit, in both versions — the second count

| figure | value | source |
|---|---|---|
| `against` links, coder 1 (the extraction), as coded | 3 on 3 claim(s); at most 1 on one claim (C20, C21, C23); claims with two or more: none | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |
| `against` links, coder 1 (the extraction), with the flagged links as `illustrates` | none (flagged: 3; answered 4a: 0) | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |
| `against` links, coder 2 (Opus 5.5), as coded | 2 on 2 claim(s); at most 1 on one claim (C22, C25); claims with two or more: none | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |
| `against` links, coder 2 (Opus 5.5), with the flagged links as `illustrates` | 1 on 1 claim(s); at most 1 on one claim (C22); claims with two or more: none (flagged: 1; answered 4a: 0) | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |
| The audit under coder 1, as coded | coverage 0.167 (8 of 48 directional claims assessed); seams: 0 | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |
| The audit under coder 1, with the flagged links as `illustrates` | coverage 0.146 (7 of 48 directional claims assessed); seams: 0 | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |
| The audit under coder 2, as coded | coverage 0.104 (5 of 48 directional claims assessed); seams: 0 | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |
| The audit under coder 2, with the flagged links as `illustrates` | coverage 0.104 (5 of 48 directional claims assessed); seams: 0 | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |
| The audit's floor and rule | no rate is reported under coverage 0.60; a claim is assessed with at least 4 `with` or `against` links from fragments not in the author's voice | `PRATT_SECOND_COUNT_LOG.md` (second_count.py's record) |

## 4. The wager test (T29)

| figure | value | source |
|---|---|---|
| The system's readings (cards) and the attack (GPT 6 Astra) | 5 cards: 5 killed (5 of them under B, import), 0 survived | `stage2/attack_results.md` |
| The attack's calibration: two copies of one card, each broken on purpose | 2 copies: chat 37 killed; chat 38 killed | `stage2/attack_results.md` |
| The markers (Opus 5.5 and GPT 6 Astra), seven codes: below the bar of 0.60, reported by a decision of 11 Oct, made after the result *new* | 141 of 203 sentences agree (0.695); kappa 0.593 (95% interval 0.52 to 0.67); the interval is new | `stage2/marker_results/RESULTS.md`; the interval from the two replies and the key (new) |
| The markers, four groups (a diagnostic only): below the bar | agreement 0.754, kappa 0.595 | `stage2/marker_results/RESULTS.md` |
| By arm, Opus 5.5 / GPT 6 Astra: resolution rate (R, RI, RA) (below the bar; reported by a decision made after the result) | system 82% / 58%; middle 89% / 72%; plain 87% / 75% | `stage2/marker_results/RESULTS.md` |
| By arm, Opus 5.5 / GPT 6 Astra: strict rate (R) (below the bar; reported by a decision made after the result) | system 40% / 47%; middle 43% / 47%; plain 66% / 62% | `stage2/marker_results/RESULTS.md` |
| By arm, Opus 5.5 / GPT 6 Astra: sentences that report (not N) (below the bar; reported by a decision made after the result) | system 45 / 43; middle 28 / 32; plain 62 / 73 | `stage2/marker_results/RESULTS.md` |
| The PI's worth, system arm (0 to 3; declared not blind) | mean 0.60 over 5 readings; rated 2 or more: 1 of 5 | `stage2/worth/worth_joined.json`, checked against `stage2/worth/WORTH_RESULTS.md` |
| The PI's worth, middle arm (0 to 3; declared not blind) | mean 1.00 over 5 readings; rated 2 or more: 1 of 5 | `stage2/worth/worth_joined.json`, checked against `stage2/worth/WORTH_RESULTS.md` |
| The PI's worth, plain arm (0 to 3; declared not blind) | mean 1.40 over 5 readings; rated 2 or more: 3 of 5; without the 2 rated late, mean 1.67 | `stage2/worth/worth_joined.json`, checked against `stage2/worth/WORTH_RESULTS.md` |
| Gap in the PI's mean worth (declared not blind), system against middle (the reading chats) (p by relabelling) | -0.40 (p 0.683) | `stage2/worth/WORTH_RESULTS.md` |
| Gap in the PI's mean worth (declared not blind), system against plain (the plain chats) (p by relabelling); the plain arm's mean includes the readings the PI rated late | -0.80 (p 0.333) | `stage2/worth/WORTH_RESULTS.md` |
| Gap in the PI's mean worth (declared not blind), middle (the reading chats) against plain (the plain chats) (p by relabelling); the plain arm's mean includes the readings the PI rated late | -0.40 (p 0.683) | `stage2/worth/WORTH_RESULTS.md` |

## 5.1 Added after the plan: T31, the judges (Gemini 3.1 Pro)

| figure | value | source |
|---|---|---|
| Rows where the two codings differ, as the judge sorted them | 79 rows: both held 5; only coder 1's held 52; only coder 2's held 16; neither held 6 | `judge_results.json`, checked against `JUDGE_RESULTS.md` |
| How far the judge can be trusted: statements both codings made, and none made, held | both made: 23 of 32 held; neither made: 0 of 16 held | `judge_results.json` |

## 5.4 Added after the plan: T34, the author's own worth

| figure | value | source |
|---|---|---|
| The author's ratings of the wager test's readings of the paper | no reply in | `author_ratings_key_pratt.json`; the folder |
