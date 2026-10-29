# The numbers of the proposal, and where each comes from

Every number that the abstract, the proposal (Part I) and its technical appendix (Part II) report from the pilot, or work out from the pilot's figures, set beside the file of this repository that holds it and the script that wrote that file: 689 numbers. Where no script gives a number, the row says how it was worked out: a sum of figures listed, a count over a file, an estimate made by hand from the times on record, or a page of the paper that a reading cites. A number is given as the proposal gives it, rounded where it rounds.

Not listed: the protocol's and the plan's own counts (the ten steps, the three standards, the cohorts' sizes, the plan's dates), labels (of sections, steps, chats, claims, readings and codes, and the models' names and versions), the years and pages of citations, and numbers that are plain words, such as "one condition".

A figure named by its id is in `figures.json`, which `build_figures.py` writes from the results files it names, and in the table of `FIGURES_bechky_2020.md`, `FIGURES_pratt_2000.md` or `FIGURES_across.md`; `replay.py` makes these files again from those it reads. A line of any other file is named by its section and the words it starts with.

## Abstract

| Number | In the text | From | Made by |
|---|---|---|---|
| 47 | “end to end: 47 readings were proposed,” | 9 + 10 + 10 + 4 + 4 + 10: the wager test's 29 readings (system 9, middle 10, plain 10: figures t29.worth.*), the 8 of the readings at places (bechky_2020.t32.readings) and the second vendor's 10 (bechky_2020.t33.recur). The abstract's “most checked sentence by sentence”: the wager test's 29 and the 8 at places, 37 in all, each sentence coded by two markers (`stage2/marker_results/RESULTS.md`, `PLACES_MARKER_RESULTS.md`); the second vendor's 10 were grouped (E.6), not marked | no script: the sum shown |

## Part I. Proposal

### 4. What we have done

| Number | In the text | From | Made by |
|---|---|---|---|
| three | “(2020). Models from three different vendors ran” | the vendors of the models the chats' record names (Anthropic, OpenAI, Google; E.1) | no script |
| three | “chat sessions over three weeks. Every” | the dates of the pilot's first and last sessions, 27 September and 20 October 2026 (figures `hours.step.extraction` and `hours.step.step 10 example: titles` in `FIGURES_across.md`, from chats_models_hours.json): 23 days, over three weeks | no script: the dates shown |
| 47 | “Models proposed 47 alternative readings,” | 9 + 10 + 10 + 4 + 4 + 10: the wager test's 29 readings (system 9, middle 10, plain 10: figures t29.worth.*), the 8 of the readings at places (bechky_2020.t32.readings) and the second vendor's 10 (bechky_2020.t33.recur). “most of them sentence by sentence”: the wager test's 29 and the 8 at places, 37 in all, each sentence coded by two markers (`stage2/marker_results/RESULTS.md`, `PLACES_MARKER_RESULTS.md`); the second vendor's 10 were grouped (E.6), not marked | no script: the sum shown |
| Seven, ten | “Seven of ten readings by a second” | figure `bechky_2020.t33.recur` in `FIGURES_bechky_2020.md`, from matching_results.json | `build_figures.py` |
| 28 | “groups the paper's 28 readings into” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`: “What step 10's entry would show” | a script not kept here (README) |
| ten | “28 readings into ten distinct points” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`, All 28 readings, behind the entry's link: “The link leads to every reading's” | a script not kept here (README) |
| five | “opens with the five points of highest” | the entry's points of highest reach (REPOSITORY_ENTRY_EXAMPLE_bechky.md, 'Points with the highest reach') | no script |
| five | “the repository: the five distinct points” | the entry's points of highest reach (REPOSITORY_ENTRY_EXAMPLE_bechky.md) | no script |
| 23 | “claims network: Bechky's 23 claims, joined” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`, Claims readings engage most often › Empirical claims: “The claims' network: CLAIM_NETWORK_bechky.html draws all” | a script not kept here (README) |
| 28 | “many of the 28 readings engage” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`: “What step 10's entry would show” | a script not kept here (README) |

### 6. Key risks

| Number | In the text | From | Made by |
|---|---|---|---|
| 28, 28 | “scholar could face 28 alternative readings” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`: “What step 10's entry would show” | a script not kept here (README) |
| ten | “28 readings were grouped into ten distinct points” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`, All 28 readings, behind the entry's link: “The link leads to every reading's” | a script not kept here (README) |
| five | “opens with the five points of” | the entry's points of highest reach (REPOSITORY_ENTRY_EXAMPLE_bechky.md) | no script |
| Two | “or reliably wrong. Two index fields” | the two fields of E.3 with kappa from 0.31 to 0.88 across the papers: whether a claim names an outcome and core claim (figures bechky_2020.A, pratt_2000.A, bechky_2020.B.core, pratt_2000.B.core) | no script |
| 0.60 | “fell just below the 0.60 bar” | `stage2/marker_results/RESULTS.md`, Pratt › Agreement: “Below the bar: kappa 0.593 is” | `score_markers.py` |
| 3.5 | “steps cost about 3.5 hours for” | figure `hours.pi_coverage_check_pratt` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| an hour | “check and about an hour to” | 2 / 2: the settling of the two maps, more than two hours for both (figure hours.pi_settling_t39), about one a map | no script: the sum shown |

## Part II. Technical appendix

### A.3 Principles that apply at every step

| Number | In the text | From | Made by |
|---|---|---|---|
| two | “it also made two kinds of” | E.3's outcome wordings and direction signs, matched by the coordinator | no script |
| eight | “spans longer than eight words.” | the scorers' quotation check: no quoted span of over eight words (each results file's checks, e.g. RELATION_RESULTS.md) | no script |

### B. Phase A: indexing a paper (the anchor)

| Number | In the text | From | Made by |
|---|---|---|---|
| 3.5 | “second reader, about 3.5 hours a” | figure `hours.pi_coverage_check_pratt` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 20, 29 | “papers: it listed 20 of the” | `COMPLETENESS_RESULTS.md`, M1. The PI's passages that the checker lists: “both papers” | `score_completeness_test.py` |
| 12 | “none of its 12 other lines” | `COMPLETENESS_RESULTS.md`, M2. The checker's lines, and what the judge says of them: “both papers” | `score_completeness_test.py` |
| 17 | “entries disagreed on 17 of the” | 8 + 9: the judge against the coverage chats on the reader's 29 passages: miss and not added 8, not a miss and added 9 (COMPLETENESS_RESULTS.md, M4) | no script: the sum shown |
| 29 | “17 of the 29 passages about” | `COMPLETENESS_RESULTS.md`, M4. Described: the judge against the coverage chats, on the PI's passages: “both papers” | `score_completeness_test.py` |

### C. Phase B: proposing and checking alternative readings

| Number | In the text | From | Made by |
|---|---|---|---|
| twelve | “written out for twelve readings, six” | a count over `map_comparison_key.json`: the twelve tabs of the comparison of accounts (map_comparison_key.json, T39) | `build_map_round2.py` |
| six | “for twelve readings, six of each” | a count over `map_comparison_key.json`: six of them Bechky's | `build_map_round2.py` |

### E. The pilot: set-up and results

| Number | In the text | From | Made by |
|---|---|---|---|
| 27 | “Bechky (2020) between 27 September and” | figure `hours.step.extraction` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 20 | “27 September and 20 October 2026” | figure `hours.step.step 10 example: titles` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 29 | “on Pratt from 29 September to” | the first link test's coder chats, 29 Sep (LINK_TEST_RESULT.md, written on 30 Sep) | no script |
| 6 | “29 September to 6 October, did” | figure `hours.run_C_6oct` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |

### E.1 Models, sessions and settings

| Number | In the text | From | Made by |
|---|---|---|---|
| three | “Frontier models from three vendors (Anthropic” | the vendors of the models the chats' record names | no script |
| five | “reply was filed; five extra sessions” | figure `hours.step.model check` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 3, 27, 6 | table row: Extraction | figure `hours.step.extraction` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 49 | table row: Extraction | about 48 + 37 / 60: the chat's own working time, 48 min 37 s over six passes (figure hours.bechky_extraction) | no script: the sum shown |
| six | table row: Extraction | figure `hours.bechky_extraction` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 45 | table row: Extraction | figure `hours.pratt_extraction` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 2, 7, 9 | table row: Coverage session (adds what the reader listed) | figure `hours.step.coverage chat` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 9 | table row: Coverage session (adds what the reader listed) | figure `hours.bechky_coverage_chat` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 11 | table row: Coverage session (adds what the reader listed) | about 10 + 30 / 60: its working time, 10 min 30 s (figure hours.pratt_coverage_chat) | no script: the sum shown |
| 8, 8, 9, six, 3, 45, 87 | table row: Second coding of the frozen index | figure `hours.step.second coding` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 2, 13 | table row: Third-model judge of the codings' disagreements | figure `hours.step.T31 judge` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 3 | table row: Second extraction of Bechky and its two | 1 + 2: the second extraction (figure hours.step.T35 second extraction, 1) and its matchers (hours.step.T35 matcher, 2) | no script: the sum shown |
| 15 | table row: Second extraction of Bechky and its two | figure `hours.step.T35 matcher` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 61 | table row: Second extraction of Bechky and its two | figure `hours.chat_55` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 5 | table row: Second extraction of Bechky and its two | figure `hours.chat_56` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 7 | table row: Second extraction of Bechky and its two | figure `hours.chat_57` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 3 | table row: Completeness checkers and matcher | 2 + 1: the checkers (figure hours.step.T38 checker, 2) and the matcher (hours.step.T38 ready test, 1) | no script: the sum shown |
| 17 | table row: Completeness checkers and matcher | figure `hours.step.T38 checker` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 3 | table row: Completeness checkers and matcher | figure `hours.chat_68` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 2, 17 | table row: Completeness judges | figure `hours.step.T38 judge` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 6 | table row: Completeness judges | figure `hours.chat_71` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 6 | table row: Readings, three arms | 2 + 2 + 2: figures hours.step.T29 generation, T29 baseline middle and T29 baseline plain, 2 each | no script: the sum shown |
| 11, one, 26 | table row: Readings, three arms | figure `hours.step.T29 generation` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 11, 11 | table row: Adversarial check of the index-only readings | figure `hours.step.T29 attack` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 4, 2, 2, 11, 10, 21 | table row: Sentence markers | figure `hours.step.T29 marker` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 4 | table row: Readings at places and their markers | 2 + 2: figures hours.step.T32 readings and T32 marker, 2 each | no script: the sum shown |
| 2, 13 | table row: Readings at places and their markers | figure `hours.step.T32 readings` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 20 | table row: Readings at places and their markers | figure `hours.chat_47` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 12 | table row: Readings at places and their markers | figure `hours.chat_48` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 6 | table row: Second vendor's readings and the grouping coders | 2 + 2 + 2: figures hours.step.T33 plain second vendor, T33 coder arm A and T33 coder arm B, 2 each | no script: the sum shown |
| 4 | table row: Second vendor's readings and the grouping coders | 2 + 1 + 1: GPT 6 Astra in the three steps (2, 1, 1) | no script: the sum shown |
| 2 | table row: Second vendor's readings and the grouping coders | 1 + 1: Opus 5.5 in the coders' steps | no script: the sum shown |
| 14 | table row: Second vendor's readings and the grouping coders | figure `hours.step.T33 coder arm A` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 5 | table row: Second vendor's readings and the grouping coders | figure `hours.chat_51` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 4, 2, 2, 16 | table row: Citation-only readings | figure `hours.step.T36 citation only` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 3, 4 | table row: Citation-only readings | figure `hours.chat_58` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 4, 2, 2, 17 | table row: Relation coders | figure `hours.step.T37 coder` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 7 | table row: Relation coders | figure `hours.chat_64` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 4 | table row: Relation coders | figure `hours.chat_65` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 4, 2, 2, 18 | table row: Argument maps | figure `hours.step.T39 map` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 10 | table row: Argument maps | figure `hours.chat_73` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 6 | table row: Placement and openings' check | 4 + 2: figures hours.step.T39 placement (4) and T39 openings check (2) | no script: the sum shown |
| 4 | table row: Placement and openings' check | figure `hours.step.T39 placement` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 2 | table row: Placement and openings' check | figure `hours.step.T39 openings check` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 18 | table row: Placement and openings' check | figure `hours.step.T39 placement` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 7 | table row: Placement and openings' check | figure `hours.chat_81` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 5 | table row: Placement and openings' check | figure `hours.chat_79` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 3 | table row: Placement and openings' check | figure `hours.chat_80` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| two | “extraction brief, the two sessions that” | figure `hours.step.T37 planted readings` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| two | “titles, and the two sessions asked” | figure `hours.step.T39 map task feedback` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| five | “diverge; with the five model checks” | figure `hours.step.model check` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 84 | “pilot ran about 84 sessions.” | 85 − 1: the 85 chats of the chats' record (figures hours.*, one per chat) less run C, a run of the link tests named in passing only (hours.run_C_6oct) | no script: the sum shown |

### E.2 The index: what the extraction returned, what the reader added, what was frozen

| Number | In the text | From | Made by |
|---|---|---|---|
| 168, 99 | table row: First return: passages (of them coded reported) | figure `bechky_2020.first.fragments` in `FIGURES_bechky_2020.md`, from bechky_2020_corpus.json, bechky_2020_voice_gloss.json | `build_figures.py` |
| 121, 92 | table row: First return: passages (of them coded reported) | figure `pratt_2000.first.fragments` in `FIGURES_pratt_2000.md`, from pratt_2000_corpus.json, pratt_2000_voice_gloss.json | `build_figures.py` |
| 23 | table row: First return: claims | figure `bechky_2020.first.claims_links` in `FIGURES_bechky_2020.md`, from bechky_2020_corpus.json | `build_figures.py` |
| 52 | table row: First return: claims | figure `pratt_2000.first.claims_links` in `FIGURES_pratt_2000.md`, from pratt_2000_corpus.json | `build_figures.py` |
| 290, 59, 0, 221, 10 | table row: First return: links, with / against / | figure `bechky_2020.first.claims_links` in `FIGURES_bechky_2020.md`, from bechky_2020_corpus.json | `build_figures.py` |
| 422, 152, 3, 264, 3 | table row: First return: links, with / against / | figure `pratt_2000.first.claims_links` in `FIGURES_pratt_2000.md`, from pratt_2000_corpus.json | `build_figures.py` |
| 15 | table row: Reader's completeness check: passages listed; time | figure `bechky_2020.coverage.list` in `FIGURES_bechky_2020.md`, from bechky_2020_coverage_list.txt | `build_figures.py` |
| 3.5 | table row: Reader's completeness check: passages listed; time | figure `hours.pi_coverage_check_bechky` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 14 | table row: Reader's completeness check: passages listed; time | figure `pratt_2000.coverage.list` in `FIGURES_pratt_2000.md`, from pratt_2000_coverage_list.txt | `build_figures.py` |
| 3.5 | table row: Reader's completeness check: passages listed; time | figure `hours.pi_coverage_check_pratt` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 4, 0, 3 | table row: Coverage session added: passages / claims / | figure `bechky_2020.coverage.chat` in `FIGURES_bechky_2020.md`, from bechky_2020_corpus.json and bechky_2020_coverage_corpus.json, record by record | `build_figures.py` |
| 4, 8, 30 | table row: Coverage session added: passages / claims / | figure `pratt_2000.coverage.chat` in `FIGURES_pratt_2000.md`, from pratt_2000_corpus.json and pratt_2000_coverage_corpus.json, record by record | `build_figures.py` |
| 172, 23, 293 | table row: Frozen index: passages / claims / links | figure `bechky_2020.frozen` in `FIGURES_bechky_2020.md`, from bechky_2020_v1.json, bechky_2020_coverage_corpus.json | `build_figures.py` |
| 125, 60, 452 | table row: Frozen index: passages / claims / links | figure `pratt_2000.frozen` in `FIGURES_pratt_2000.md`, from pratt_2000_v1.json, pratt_2000_coverage_corpus.json | `build_figures.py` |
| 18, 23 | table row: Claims that name an outcome (directional) | figure `bechky_2020.frozen.claims` in `FIGURES_bechky_2020.md`, from bechky_2020_v1.json (agreement.directional_claims) | `build_figures.py` |
| 56, 60 | table row: Claims that name an outcome (directional) | figure `pratt_2000.frozen.claims` in `FIGURES_pratt_2000.md`, from pratt_2000_v1.json (agreement.directional_claims) | `build_figures.py` |
| 7 | table row: Core claims | figure `bechky_2020.frozen.claims` in `FIGURES_bechky_2020.md`, from bechky_2020_v1.json (agreement.directional_claims) | `build_figures.py` |
| 10 | table row: Core claims | figure `pratt_2000.frozen.claims` in `FIGURES_pratt_2000.md`, from pratt_2000_v1.json (agreement.directional_claims) | `build_figures.py` |
| 19, 4 | table row: Claims stated as established / ventured | figure `bechky_2020.frozen.claims` in `FIGURES_bechky_2020.md`, from bechky_2020_v1.json (agreement.directional_claims) | `build_figures.py` |
| 39, 21 | table row: Claims stated as established / ventured | figure `pratt_2000.frozen.claims` in `FIGURES_pratt_2000.md`, from pratt_2000_v1.json (agreement.directional_claims) | `build_figures.py` |
| 70, 102 | table row: Voice, the extraction's codes: author_insight / reported | figure `bechky_2020.frozen.voice` in `FIGURES_bechky_2020.md`, from bechky_2020_v1_voice_gloss.json | `build_figures.py` |
| 30, 95 | table row: Voice, the extraction's codes: author_insight / reported | figure `pratt_2000.frozen.voice` in `FIGURES_pratt_2000.md`, from pratt_2000_v1_voice_gloss.json | `build_figures.py` |
| 23 | “For Bechky the 23 claims sort” | figure `bechky_2020.frozen` in `FIGURES_bechky_2020.md`, from bechky_2020_v1.json, bechky_2020_coverage_corpus.json | `build_figures.py` |
| 7 | “claims sort into 7 empirical, 15” | `CLAIM_KINDS_bechky.md`: “Empirical” | a script not kept here |
| 15 | “into 7 empirical, 15 theoretical and” | `CLAIM_KINDS_bechky.md`: “Theoretical” | a script not kept here |
| 1, 1 | “15 theoretical and 1 method claim” | `CLAIM_KINDS_bechky.md`: “Empirical” | a script not kept here |
| 6 | “method claim (1, 6 and 0” | `CLAIM_KINDS_bechky.md`: “Theoretical” | a script not kept here |
| 0 | “(1, 6 and 0 of them” | `CLAIM_KINDS_bechky.md`: “Method” | a script not kept here |
| 0, 290 | “almost never used (0 of 290” | figure `bechky_2020.first.claims_links` in `FIGURES_bechky_2020.md`, from bechky_2020_corpus.json | `build_figures.py` |
| 3, 422 | “of 290 links; 3 of 422)” | figure `pratt_2000.first.claims_links` in `FIGURES_pratt_2000.md`, from pratt_2000_corpus.json | `build_figures.py` |
| four, 60% | “with at least four with or” | figure `bechky_2020.audit.rule` in `FIGURES_bechky_2020.md`, from BECHKY_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 0.10 | “reached: coverage was 0.10 to 0.17” | figure `pratt_2000.second.audit.coder2.coded` in `FIGURES_pratt_2000.md`, from PRATT_SECOND_COUNT_LOG.md (second_count.py's record) | `build_figures.py` |
| 0.17 | “was 0.10 to 0.17 under either” | figure `pratt_2000.second.audit.coder1.coded` in `FIGURES_pratt_2000.md`, from PRATT_SECOND_COUNT_LOG.md (second_count.py's record) | `build_figures.py` |

### E.3 Agreement on the index's codes, and the index's repeatability

| Number | In the text | From | Made by |
|---|---|---|---|
| 95%, 2,000 | “Intervals are bootstrap 95% intervals over” | figure `bechky_2020.A` in `FIGURES_bechky_2020.md`, from BECHKY_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| ten | “is withheld under ten judgments.” | figure `bechky_2020.B.gap kind` in `FIGURES_bechky_2020.md`, from BECHKY_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 23, 0.957, 0.881, 0.57, 1.00 | table row: Whether a claim names an outcome | figure `bechky_2020.A` in `FIGURES_bechky_2020.md`, from BECHKY_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 60, 0.883, 0.483, 0.13, 0.78 | table row: Whether a claim names an outcome | figure `pratt_2000.A` in `FIGURES_pratt_2000.md`, from PRATT_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 17, 14, 1, 2 | table row: Where both name one: wordings match / | figure `bechky_2020.A_wordings` in `FIGURES_bechky_2020.md`, from BECHKY_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 49, 45, 3 | table row: Where both name one: wordings match / | figure `pratt_2000.A_wordings` in `FIGURES_pratt_2000.md`, from PRATT_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 1 | table row: Where both name one: wordings match / | figure `bechky_2020.A_wordings` in `FIGURES_bechky_2020.md`, from BECHKY_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 18, 18 | table row: The direction's sign, where both give one | figure `bechky_2020.A2` in `FIGURES_bechky_2020.md`, from BECHKY_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 51, 2, 53 | table row: The direction's sign, where both give one | figure `pratt_2000.A2` in `FIGURES_pratt_2000.md`, from PRATT_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 172, 0.936, 0.865, 0.78, 0.94 | table row: Voice | figure `bechky_2020.V` in `FIGURES_bechky_2020.md`, from BECHKY_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 125, 0.968, 0.908, 0.80, 0.98 | table row: Voice | figure `pratt_2000.V` in `FIGURES_pratt_2000.md`, from PRATT_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 293, 0.918, 0.796, 0.72, 0.87 | table row: Link direction, all links | figure `bechky_2020.B.direction` in `FIGURES_bechky_2020.md`, from BECHKY_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 452, 0.867, 0.714, 0.64, 0.78 | table row: Link direction, all links | figure `pratt_2000.B.direction` in `FIGURES_pratt_2000.md`, from PRATT_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 231, 0.896, 0.778, 0.70, 0.85 | table row: Link direction, links to directional claims | figure `bechky_2020.B.direction_directional` in `FIGURES_bechky_2020.md`, from BECHKY_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 322, 0.814, 0.642, 0.56, 0.72 | table row: Link direction, links to directional claims | figure `pratt_2000.B.direction_directional` in `FIGURES_pratt_2000.md`, from PRATT_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 23, 0.696, 0.309, −0.14, 0.70 | table row: Core claim | figure `bechky_2020.B.core` in `FIGURES_bechky_2020.md`, from BECHKY_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 60, 0.917, 0.732, 0.47, 0.93 | table row: Core claim | figure `pratt_2000.B.core` in `FIGURES_pratt_2000.md`, from PRATT_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 23, 1.000, 1.000 | table row: Stated as established or ventured | figure `bechky_2020.B.stated_as` in `FIGURES_bechky_2020.md`, from BECHKY_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 60, 0.950, 0.886, 0.75 | table row: Stated as established or ventured | figure `pratt_2000.B.stated_as` in `FIGURES_pratt_2000.md`, from PRATT_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 1.00 | table row: Stated as established or ventured | figure `bechky_2020.B.stated_as` in `FIGURES_bechky_2020.md`, from BECHKY_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| Four | “a model (A.3). Four smaller fields” | 4: the fields gap kind, pair drawn by authors, resolution period and gloss relation (figures bechky_2020.B.* and pratt_2000.B.*) | no script: the sum shown |
| 1 | “the index, with 1 to 20” | figure `bechky_2020.B.resolution_period` in `FIGURES_bechky_2020.md`, from BECHKY_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 20 | “with 1 to 20 judgments each” | figure `bechky_2020.B.gloss_relation` in `FIGURES_bechky_2020.md`, from BECHKY_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| five, one | “none, coder 2 five on one” | figure `bechky_2020.against.coder2.coded` in `FIGURES_bechky_2020.md`, from BECHKY_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| three, three | “Pratt, coder 1 three on three” | figure `pratt_2000.against.coder1.coded` in `FIGURES_pratt_2000.md`, from PRATT_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| two, two | “claims, coder 2 two on two” | figure `pratt_2000.against.coder2.coded` in `FIGURES_pratt_2000.md`, from PRATT_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| nine | “two on two; nine of the” | 0 + 5 + 3 + 1: the links flagged: Bechky's coder 2, 5; Pratt's coder 1, 3, and coder 2, 1 (figures *.against.*.check, 'flagged') | no script: the sum shown |
| ten | “nine of the ten were flagged” | 5 + 3 + 2: the `against` links coded: 5, 3 and 2 | no script: the sum shown |
| 11, 35, 11, 12, 1 | “both codings on 11 of Bechky's” | figure `bechky_2020.t31.differ` in `FIGURES_bechky_2020.md`, from judge_results.json, checked against JUDGE_RESULTS.md | `build_figures.py` |
| 79, 5, 52, 16, 6 | “1; on Pratt's 79 rows, both” | figure `pratt_2000.t31.differ` in `FIGURES_pratt_2000.md`, from judge_results.json, checked against JUDGE_RESULTS.md | `build_figures.py` |
| 35, 46, 1, 23 | “made it held 35 of 46” | figure `t31.planted` in `FIGURES_across.md`, from judge_results.json | `build_figures.py` |
| 23, 21 | table row: First index's 23 claims found in the | figure `bechky_2020.t35.claims.first` in `FIGURES_bechky_2020.md`, from second_extraction_results.json | `build_figures.py` |
| 39, 27 | table row: Second index's 39 claims found in the | figure `bechky_2020.t35.claims.new` in `FIGURES_bechky_2020.md`, from second_extraction_results.json | `build_figures.py` |
| 7 | table row: Core claims found: first's 7; second's 9 | figure `bechky_2020.t35.claims.first_core` in `FIGURES_bechky_2020.md`, from second_extraction_results.json | `build_figures.py` |
| 9 | table row: Core claims found: first's 7; second's 9 | figure `bechky_2020.t35.claims.new_core` in `FIGURES_bechky_2020.md`, from second_extraction_results.json | `build_figures.py` |
| 6 | table row: Core claims found: first's 7; second's 9 | figure `bechky_2020.t35.claims.first_core` in `FIGURES_bechky_2020.md`, from second_extraction_results.json | `build_figures.py` |
| 9 | table row: Core claims found: first's 7; second's 9 | figure `bechky_2020.t35.claims.new_core` in `FIGURES_bechky_2020.md`, from second_extraction_results.json | `build_figures.py` |
| 0.661, 0.46, 0.86 | table row: Matchers' agreement on claim pairs | figure `bechky_2020.t35.claims.kappa` in `FIGURES_bechky_2020.md`, from second_extraction_results.json | `build_figures.py` |
| 168 | table row: First index's 168 passages found in the | figure `bechky_2020.t35.passages_all.first` in `FIGURES_bechky_2020.md`, from second_extraction_results.json | `build_figures.py` |
| 128 | table row: First index's 168 passages found in the | figure `bechky_2020.t35.passages_out.first` in `FIGURES_bechky_2020.md`, from second_extraction_results.json | `build_figures.py` |
| 123, 0.73 | table row: First index's 168 passages found in the | figure `bechky_2020.t35.passages_all.first` in `FIGURES_bechky_2020.md`, from second_extraction_results.json | `build_figures.py` |
| 83, 0.65 | table row: First index's 168 passages found in the | figure `bechky_2020.t35.passages_out.first` in `FIGURES_bechky_2020.md`, from second_extraction_results.json | `build_figures.py` |
| 168 | table row: Second index's 168 passages found in the | figure `bechky_2020.t35.passages_all.new` in `FIGURES_bechky_2020.md`, from second_extraction_results.json | `build_figures.py` |
| 127 | table row: Second index's 168 passages found in the | figure `bechky_2020.t35.passages_out.new` in `FIGURES_bechky_2020.md`, from second_extraction_results.json | `build_figures.py` |
| 135, 0.80 | table row: Second index's 168 passages found in the | figure `bechky_2020.t35.passages_all.new` in `FIGURES_bechky_2020.md`, from second_extraction_results.json | `build_figures.py` |
| 94, 0.74 | table row: Second index's 168 passages found in the | figure `bechky_2020.t35.passages_out.new` in `FIGURES_bechky_2020.md`, from second_extraction_results.json | `build_figures.py` |
| 140, 130, 0.788, 0.65, 0.90 | table row: Voice on the 140 matched passages, first | figure `bechky_2020.t35.voice` in `FIGURES_bechky_2020.md`, from second_extraction_results.json | `build_figures.py` |
| 32, 69 | table row: First index's author_insight passages found again; its | figure `bechky_2020.t35.byvoice.author_insight` in `FIGURES_bechky_2020.md`, from second_extraction_results.json | `build_figures.py` |
| 91, 99 | table row: First index's author_insight passages found again; its | figure `bechky_2020.t35.byvoice.reported` in `FIGURES_bechky_2020.md`, from second_extraction_results.json | `build_figures.py` |
| 46, 59 | table row: with links resting on an author_insight passage: | figure `bechky_2020.t35.with_on_author.first` in `FIGURES_bechky_2020.md`, from bechky_2020_corpus.json, bechky_2020_voice_gloss.json (new) | `build_figures.py` |
| 13, 72 | table row: with links resting on an author_insight passage: | figure `bechky_2020.t35.with_on_author.new` in `FIGURES_bechky_2020.md`, from bechky_2020_x2_corpus.json, bechky_2020_x2_voice_gloss.json (new) | `build_figures.py` |
| 0.79 | “of one index (0.79 against 0.87).” | figure `bechky_2020.t35.voice` in `FIGURES_bechky_2020.md`, from second_extraction_results.json | `build_figures.py` |
| 0.87 | “index (0.79 against 0.87). What the” | figure `bechky_2020.V` in `FIGURES_bechky_2020.md`, from BECHKY_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |

### E.4 Completeness: the reader's check against a model checker

| Number | In the text | From | Made by |
|---|---|---|---|
| 15 | table row: Reader's passages listed | `COMPLETENESS_RESULTS.md`, M1. The PI's passages that the checker lists: “Bechky” | `score_completeness_test.py` |
| 14 | table row: Reader's passages listed | `COMPLETENESS_RESULTS.md`, M1. The PI's passages that the checker lists: “Pratt” | `score_completeness_test.py` |
| 29 | table row: Reader's passages listed | `COMPLETENESS_RESULTS.md`, M1. The PI's passages that the checker lists: “both papers” | `score_completeness_test.py` |
| 8 | table row: Of these, also listed by the checker | `COMPLETENESS_RESULTS.md`, M1. The PI's passages that the checker lists: “Bechky” | `score_completeness_test.py` |
| 12 | table row: Of these, also listed by the checker | `COMPLETENESS_RESULTS.md`, M1. The PI's passages that the checker lists: “Pratt” | `score_completeness_test.py` |
| 20 | table row: Of these, also listed by the checker | `COMPLETENESS_RESULTS.md`, M1. The PI's passages that the checker lists: “both papers” | `score_completeness_test.py` |
| 4, 2 | table row: Confirmed; confirmed and listed by the checker | `COMPLETENESS_RESULTS.md`, M1. The PI's passages that the checker lists: “Bechky” | `score_completeness_test.py` |
| 10, 9 | table row: Confirmed; confirmed and listed by the checker | `COMPLETENESS_RESULTS.md`, M1. The PI's passages that the checker lists: “Pratt” | `score_completeness_test.py` |
| 14, 11 | table row: Confirmed; confirmed and listed by the checker | `COMPLETENESS_RESULTS.md`, M1. The PI's passages that the checker lists: “both papers” | `score_completeness_test.py` |
| 13, 5 | table row: Checker's lines in all; judged a miss | `COMPLETENESS_RESULTS.md`, M2. The checker's lines, and what the judge says of them: “Bechky” | `score_completeness_test.py` |
| 19, 3 | table row: Checker's lines in all; judged a miss | `COMPLETENESS_RESULTS.md`, M2. The checker's lines, and what the judge says of them: “Pratt” | `score_completeness_test.py` |
| 32, 8 | table row: Checker's lines in all; judged a miss | `COMPLETENESS_RESULTS.md`, M2. The checker's lines, and what the judge says of them: “both papers” | `score_completeness_test.py` |
| 10 | table row: Reader's passages judged a miss | 2 + 8: miss, added and not added (COMPLETENESS_RESULTS.md, M4, Bechky) | no script: the sum shown |
| 3 | table row: Reader's passages judged a miss | 3 + 0: the same, Pratt | no script: the sum shown |
| 13 | table row: Reader's passages judged a miss | 5 + 8: the same, both papers | no script: the sum shown |
| 3.5 | table row: Time: reader; checker; judge | figure `hours.pi_coverage_check_bechky` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 3 | table row: Time: reader; checker; judge | figure `hours.chat_68` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 6 | table row: Time: reader; checker; judge | figure `hours.chat_71` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 3.5 | table row: Time: reader; checker; judge | figure `hours.pi_coverage_check_pratt` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 3 | table row: Time: reader; checker; judge | figure `hours.chat_69` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 6 | table row: Time: reader; checker; judge | figure `hours.chat_72` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 17 | “a miss on 17 of the” | 8 + 9: the judge against the coverage chats: miss and not added 8, not a miss and added 9 (COMPLETENESS_RESULTS.md, M4) | no script: the sum shown |
| 29 | “17 of the 29; a fresh” | `COMPLETENESS_RESULTS.md`, M4. Described: the judge against the coverage chats, on the PI's passages: “both papers” | `score_completeness_test.py` |
| 13, 17, two | “agent traced 13 of the” | `COMPLETENESS_RESULTS.md`, Each line › Pratt: “In short. Of the 17 of” | `score_completeness_test.py` |
| 15, 12, 11, 15 | “coverage session. All 15 of the” | `COMPLETENESS_RESULTS.md`, M3. The ready test: the PI's Bechky passages in the second extraction: “By the matcher: found 15 of” | `score_completeness_test.py` |

### E.5 Readings: three arms, an adversarial check, and the sentence markers

| Number | In the text | From | Made by |
|---|---|---|---|
| 5 | “without the paper (5 for Pratt” | figure `pratt_2000.wager.attack` in `FIGURES_pratt_2000.md`, from stage2/attack_results.md | `build_figures.py` |
| 4 | “(5 for Pratt, 4 for Bechky)” | figure `bechky_2020.wager.attack` in `FIGURES_bechky_2020.md`, from stage2/attack_results.md | `build_figures.py` |
| 5 | “giving compact cards (5 each); and” | figure `pratt_2000.wager.worth.middle` in `FIGURES_pratt_2000.md`, from stage2/worth/worth_joined.json, checked against stage2/worth/WORTH_RESULTS.md | `build_figures.py` |
| 5 | “would settle it (5 each). An” | figure `pratt_2000.wager.worth.plain` in `FIGURES_pratt_2000.md`, from stage2/worth/worth_joined.json, checked against stage2/worth/WORTH_RESULTS.md | `build_figures.py` |
| 5, 5 | “card: it killed 5 of Pratt's” | figure `pratt_2000.wager.attack` in `FIGURES_pratt_2000.md`, from stage2/attack_results.md | `build_figures.py` |
| 2, 4 | “Pratt's 5 and 2 of Bechky's” | figure `bechky_2020.wager.attack` in `FIGURES_bechky_2020.md`, from stage2/attack_results.md | `build_figures.py` |
| 203, 141, 0.695 | table row: Sentences coded; the two markers agree | figure `pratt_2000.wager.markers` in `FIGURES_pratt_2000.md`, from stage2/marker_results/RESULTS.md; the interval from the two replies and the key (new) | `build_figures.py` |
| 193, 158, 0.819 | table row: Sentences coded; the two markers agree | figure `bechky_2020.wager.markers` in `FIGURES_bechky_2020.md`, from stage2/marker_results/RESULTS.md; the interval from the two replies and the key (new) | `build_figures.py` |
| 0.60 | table row: Kappa, seven codes (95% interval); the bar | `stage2/marker_results/RESULTS.md`: “if its kappa on the seven” | `score_markers.py` |
| 0.593, 0.52, 0.67 | table row: Kappa, seven codes (95% interval); the bar | figure `pratt_2000.wager.markers` in `FIGURES_pratt_2000.md`, from stage2/marker_results/RESULTS.md; the interval from the two replies and the key (new) | `build_figures.py` |
| 0.706, 0.62, 0.78 | table row: Kappa, seven codes (95% interval); the bar | figure `bechky_2020.wager.markers` in `FIGURES_bechky_2020.md`, from stage2/marker_results/RESULTS.md; the interval from the two replies and the key (new) | `build_figures.py` |
| 0.595 | table row: Kappa, four groups of codes (a diagnostic) | figure `pratt_2000.wager.markers4` in `FIGURES_pratt_2000.md`, from stage2/marker_results/RESULTS.md | `build_figures.py` |
| 0.711 | table row: Kappa, four groups of codes (a diagnostic) | figure `bechky_2020.wager.markers4` in `FIGURES_bechky_2020.md`, from stage2/marker_results/RESULTS.md | `build_figures.py` |
| 82%, 58%, 89%, 72%, 87%, 75% | table row: Share of reporting sentences resolved against the | figure `pratt_2000.wager.rates.resolution` in `FIGURES_pratt_2000.md`, from stage2/marker_results/RESULTS.md | `build_figures.py` |
| 95%, 87%, 100%, 93%, 98%, 70% | table row: Share of reporting sentences resolved against the | figure `bechky_2020.wager.rates.resolution` in `FIGURES_bechky_2020.md`, from stage2/marker_results/RESULTS.md | `build_figures.py` |
| 40%, 47%, 43%, 47%, 66%, 62% | table row: Share resolved under the strictest code, Opus | figure `pratt_2000.wager.rates.strict` in `FIGURES_pratt_2000.md`, from stage2/marker_results/RESULTS.md | `build_figures.py` |
| 75%, 71%, 81%, 74%, 86%, 63% | table row: Share resolved under the strictest code, Opus | figure `bechky_2020.wager.rates.strict` in `FIGURES_bechky_2020.md`, from stage2/marker_results/RESULTS.md | `build_figures.py` |
| 0.60 | table row: Reader's worth, 0 to 3, not blind: | figure `pratt_2000.wager.worth.system` in `FIGURES_pratt_2000.md`, from stage2/worth/worth_joined.json, checked against stage2/worth/WORTH_RESULTS.md | `build_figures.py` |
| 1.00 | table row: Reader's worth, 0 to 3, not blind: | figure `pratt_2000.wager.worth.middle` in `FIGURES_pratt_2000.md`, from stage2/worth/worth_joined.json, checked against stage2/worth/WORTH_RESULTS.md | `build_figures.py` |
| 1.40 | table row: Reader's worth, 0 to 3, not blind: | figure `pratt_2000.wager.worth.plain` in `FIGURES_pratt_2000.md`, from stage2/worth/worth_joined.json, checked against stage2/worth/WORTH_RESULTS.md | `build_figures.py` |
| 1.75 | table row: Reader's worth, 0 to 3, not blind: | figure `bechky_2020.wager.worth.system` in `FIGURES_bechky_2020.md`, from stage2/worth/worth_joined.json, checked against stage2/worth/WORTH_RESULTS.md | `build_figures.py` |
| 0.60 | table row: Reader's worth, 0 to 3, not blind: | figure `bechky_2020.wager.worth.middle` in `FIGURES_bechky_2020.md`, from stage2/worth/worth_joined.json, checked against stage2/worth/WORTH_RESULTS.md | `build_figures.py` |
| 2.00 | table row: Reader's worth, 0 to 3, not blind: | figure `bechky_2020.wager.worth.plain` in `FIGURES_bechky_2020.md`, from stage2/worth/worth_joined.json, checked against stage2/worth/WORTH_RESULTS.md | `build_figures.py` |
| 1.11, 9 | “mean worth was 1.11 for the” | figure `t29.worth.system` in `FIGURES_across.md`, from stage2/worth/worth_joined.json, checked against stage2/worth/WORTH_RESULTS.md | `build_figures.py` |
| 0.80, 10 | “arm (9 readings), 0.80 for the” | figure `t29.worth.middle` in `FIGURES_across.md`, from stage2/worth/worth_joined.json, checked against stage2/worth/WORTH_RESULTS.md | `build_figures.py` |
| 1.70, 10 | “middle (10) and 1.70 for the” | figure `t29.worth.plain` in `FIGURES_across.md`, from stage2/worth/worth_joined.json, checked against stage2/worth/WORTH_RESULTS.md | `build_figures.py` |
| −0.59, 0.122 | “system against plain −0.59 (p 0.122)” | figure `t29.gap.system_plain` in `FIGURES_across.md`, from stage2/worth/WORTH_RESULTS.md | `build_figures.py` |
| −0.90, 0.036 | “middle against plain −0.90 (p 0.036).” | figure `t29.gap.middle_plain` in `FIGURES_across.md`, from stage2/worth/WORTH_RESULTS.md | `build_figures.py` |
| seven, 1.00 | “(p 0.036). The seven system readings” | figure `t29.attack_worth.killed` in `FIGURES_across.md`, from stage2/worth/worth_joined.json, checked against stage2/worth/WORTH_RESULTS.md | `build_figures.py` |
| two, 1.50 | “averaged 1.00, the two that survived” | figure `t29.attack_worth.survived` in `FIGURES_across.md`, from stage2/worth/worth_joined.json, checked against stage2/worth/WORTH_RESULTS.md | `build_figures.py` |
| two | “reading starts from (two sessions, four” | figure `hours.step.T32 readings` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| four | “from (two sessions, four readings each” | figure `bechky_2020.t32.readings` in `FIGURES_bechky_2020.md`, from PLACES_RESULTS.md | `build_figures.py` |
| 0.669, 0.56, 0.77 | “gave markers' kappa 0.669 (0.56 to” | figure `bechky_2020.t32.markers` in `FIGURES_bechky_2020.md`, from places_marker_results.json; the interval from the two replies and the key (new) | `build_figures.py` |
| 1.50 | “0.77) and worth 1.50 in both” | figure `bechky_2020.t32.worth` in `FIGURES_bechky_2020.md`, from PLACES_RESULTS.md | `build_figures.py` |
| four | “both sessions. The four readings of” | figure `bechky_2020.t32.readings` in `FIGURES_bechky_2020.md`, from PLACES_RESULTS.md | `build_figures.py` |
| 28 | “not among the 28 Bechky readings” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`: “What step 10's entry would show” | a script not kept here (README) |
| 47 | “entry use; the 47 readings of” | 9 + 10 + 10 + 4 + 4 + 10: as in Part I, section 4: the wager test's 29, the 8 at places and the second vendor's 10 | no script: the sum shown |

### E.6 Recurrence across vendors, and the matching of readings

| Number | In the text | From | Made by |
|---|---|---|---|
| ten | “the paper, proposed ten readings of” | figure `bechky_2020.t33.recur` in `FIGURES_bechky_2020.md`, from matching_results.json | `build_figures.py` |
| two | “of Bechky in two runs. Two” | figure `hours.step.T33 plain second vendor` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 28 | “Astra) grouped all 28 readings of” | figure `bechky_2020.t33.claims` in `FIGURES_bechky_2020.md`, from matching_results.json; the interval by resampling the readings (new) | `build_figures.py` |
| 0.923 | “agreed with kappa 0.923 in arm” | figure `bechky_2020.t33.A` in `FIGURES_bechky_2020.md`, from matching_results.json; the interval by resampling the readings (new) | `build_figures.py` |
| 0.886 | “arm A and 0.886 (by claim” | figure `bechky_2020.t33.B` in `FIGURES_bechky_2020.md`, from matching_results.json; the interval by resampling the readings (new) | `build_figures.py` |
| 0.846 | “claim number) or 0.846 (by judgment)” | figure `bechky_2020.t33.Bj` in `FIGURES_bechky_2020.md`, from matching_results.json; the interval by resampling the readings (new) | `build_figures.py` |
| 0.628 | “grouping, agreement was 0.628 in arm” | figure `bechky_2020.t33.P_A` in `FIGURES_bechky_2020.md`, from matching_results.json; the interval by resampling the readings (new) | `build_figures.py` |
| 0.762 | “arm A and 0.762 or 0.777” | figure `bechky_2020.t33.P_B` in `FIGURES_bechky_2020.md`, from matching_results.json; the interval by resampling the readings (new) | `build_figures.py` |
| 0.777 | “and 0.762 or 0.777 in arm” | figure `bechky_2020.t33.P_Bj` in `FIGURES_bechky_2020.md`, from matching_results.json; the interval by resampling the readings (new) | `build_figures.py` |
| 0.134, −0.09, 0.38 | “the reader by 0.134 by the” | figure `bechky_2020.t33.diff.P_B-P_A` in `FIGURES_bechky_2020.md`, from matching_results.json | `build_figures.py` |
| 0.149, 0.02, 0.32 | “to 0.38) and 0.149 as judged” | figure `bechky_2020.t33.diff.P_Bj-P_A` in `FIGURES_bechky_2020.md`, from matching_results.json | `build_figures.py` |
| 0.923 | “coders agreed at 0.923 in arm” | figure `bechky_2020.t33.A` in `FIGURES_bechky_2020.md`, from matching_results.json; the interval by resampling the readings (new) | `build_figures.py` |
| 0.80 | “the bar of 0.80. Of the” | `MATCHING_TEST_PLAN.md`, What counts as an answer, fixed now: “1. Repeatable without the reference: A” | the plan, fixed before the replies |
| five, three, 7, 10 | “0.80. Of the five points that” | figure `bechky_2020.t33.recur` in `FIGURES_bechky_2020.md`, from matching_results.json | `build_figures.py` |
| 9, 23, 11 | “arm B's tags, 9 of the” | figure `bechky_2020.t33.contested` in `FIGURES_bechky_2020.md`, from matching_results.json | `build_figures.py` |
| ten | “results, gave the ten new readings” | 4 + 6: the new readings rated: 3 four, 2 six (figure bechky_2020.t33.worth) | no script: the sum shown |
| 2.40, 1.44 | “mean worth of 2.40 against 1.44” | figure `bechky_2020.t33.worth` in `FIGURES_bechky_2020.md`, from MATCHING_WORTH.md | `build_figures.py` |
| eighteen | “1.44 for the eighteen earlier ones” | 0 + 11 + 4 + 3: the earlier readings rated: 3 none, 2 eleven, 1 four, 0 three (the same figure) | no script: the sum shown |

### E.7 The citation-only control

| Number | In the text | From | Made by |
|---|---|---|---|
| 5, 3, 2 | table row: Bechky | `CITATION_ONLY_RESULTS.md`, M1. The readings made without the paper: “Bechky” | `score_citation_only.py` |
| 5, 4, 1 | table row: Bechky | `CITATION_ONLY_RESULTS.md`, M1. The readings made without the paper: “Bechky” | `score_citation_only.py` |
| 5, 3, 2 | table row: Pratt | `CITATION_ONLY_RESULTS.md`, M1. The readings made without the paper: “Pratt” | `score_citation_only.py` |
| 4, 1, 3 | table row: Pratt | `CITATION_ONLY_RESULTS.md`, M1. The readings made without the paper: “Pratt” | `score_citation_only.py` |
| 5, 10, 1, 5 | “either model reached 5 of the” | `CITATION_ONLY_RESULTS.md`, M2. Bechky: the PI's groups of 14 Oct reached without the paper: “Reached by either model” | `score_citation_only.py` |
| 5, 15 | “it. On Pratt, 5 of the” | `CITATION_ONLY_RESULTS.md`, M3. Pratt: the readings made with the paper that have a counterpart: “all” | `score_citation_only.py` |
| 1, 5 | “without it (system 1 of 5” | `CITATION_ONLY_RESULTS.md`, M3. Pratt: the readings made with the paper that have a counterpart: “system” | `score_citation_only.py` |
| 2 | “of 5, middle 2, plain 2).” | `CITATION_ONLY_RESULTS.md`, M3. Pratt: the readings made with the paper that have a counterpart: “middle” | `score_citation_only.py` |
| 2 | “middle 2, plain 2). Asked what” | `CITATION_ONLY_RESULTS.md`, M3. Pratt: the readings made with the paper that have a counterpart: “plain” | `score_citation_only.py` |

### E.8 Relation coding: which claim a reading bears on, and how

| Number | In the text | From | Made by |
|---|---|---|---|
| 43 | “each of the 43 real readings” | `RELATION_RESULTS.md`, M1. The two coders on the main type (43 real readings): “both papers (43)” | `score_relation_test.py` |
| 4 | “real readings and 4 planted ones” | `RELATION_RESULTS.md`, M3. The planted readings: “Gemini 3.1 Pro: of the 4” | `score_relation_test.py` |
| 28, 18, 0.449, 20, 0.145 | table row: Bechky (28) | `RELATION_RESULTS.md`, M1. The two coders on the main type (43 real readings): “Bechky (28)” | `score_relation_test.py` |
| 21 | table row: Bechky (28) | `RELATION_RESULTS.md`, M2. The main claim: “Bechky (28)” | `score_relation_test.py` |
| 15, 10, 0.559, 13, 0.659 | table row: Pratt (15) | `RELATION_RESULTS.md`, M1. The two coders on the main type (43 real readings): “Pratt (15)” | `score_relation_test.py` |
| 10 | table row: Pratt (15) | `RELATION_RESULTS.md`, M2. The main claim: “Pratt (15)” | `score_relation_test.py` |
| 43, 28, 0.511 | table row: Both (43) | `RELATION_RESULTS.md`, M1. The two coders on the main type (43 real readings): “both papers (43)” | `score_relation_test.py` |
| 0.31, 0.69 | table row: Both (43) | `RELATION_RESULTS.md`, M1. The two coders on the main type (43 real readings): “Both papers, types: 95% interval 0.306” | `score_relation_test.py` |
| 33, 0.360 | table row: Both (43) | `RELATION_RESULTS.md`, M1. The two coders on the main type (43 real readings): “both papers (43)” | `score_relation_test.py` |
| 0.04, 0.64 | table row: Both (43) | `RELATION_RESULTS.md`, M1. The two coders on the main type (43 real readings): “Both papers, levels: 95% interval 0.042” | `score_relation_test.py` |
| 31 | table row: Both (43) | `RELATION_RESULTS.md`, M2. The main claim: “both papers (43)” | `score_relation_test.py` |
| 3, 4 | “Each coder caught 3 of the” | `RELATION_RESULTS.md`, M3. The planted readings: “Gemini 3.1 Pro: of the 4” | `score_relation_test.py` |
| twelve, 10, 8 | “own coding of twelve readings, Argon” | `RELATION_RESULTS.md`, M4. Against the PI, on the PI's twelve: “Gemini against the PI, both papers” | `score_relation_test.py` |
| 9, 9 | “on 8, Astra 9 and 9.” | `RELATION_RESULTS.md`, M4. Against the PI, on the PI's twelve: “Astra against the PI, both papers” | `score_relation_test.py` |
| 15, 7 | “9. Of the 15 readings on” | `RELATION_RESULTS.md`, Each reading: “Of the 15 real readings on” | `score_relation_test.py` |
| 6, 7 | “a complement, and 6 of the” | `RELATION_RESULTS.md`, Each reading: “Six of those seven were written” | `score_relation_test.py` |
| twelve, 90 | “reader's coding of twelve readings took” | `RELATION_RESULTS.md`, Each reading: “The PI's coding of the twelve” | `score_relation_test.py` |

### E.9 Argument maps, settling and placement

| Number | In the text | From | Made by |
|---|---|---|---|
| 80 | table row: Listed claim pairs | `MAP_RESULTS.md`, Bechky › F1, the maps' agreement, on the maps as built: “Listed pairs (80)” | `score_map_test.py` |
| 92 | table row: Listed claim pairs | `MAP_RESULTS.md`, Pratt › F1, the maps' agreement, on the maps as built: “Listed pairs (92)” | `score_map_test.py` |
| 25, 2, 8, 45 | table row: An edge in both maps / A | `MAP_RESULTS.md`, Bechky › F1, the maps' agreement, on the maps as built: “Listed pairs (80)” | `score_map_test.py` |
| 22, 3, 15, 52 | table row: An edge in both maps / A | `MAP_RESULTS.md`, Pratt › F1, the maps' agreement, on the maps as built: “Listed pairs (92)” | `score_map_test.py` |
| 0.875, 0.735 | table row: Edge agreement: raw; kappa | `MAP_RESULTS.md`, Bechky › F1, the maps' agreement, on the maps as built: “Listed pairs (80)” | `score_map_test.py` |
| 0.804, 0.57 | table row: Edge agreement: raw; kappa | `MAP_RESULTS.md`, Pratt › F1, the maps' agreement, on the maps as built: “Listed pairs (92)” | `score_map_test.py` |
| 21, 25, 0.574 | table row: Type agreement on the shared edges: agree; | `MAP_RESULTS.md`, Bechky › F1, the maps' agreement, on the maps as built: “The type, on the 25 pairs both call” | `score_map_test.py` |
| 18, 22, 0.651 | table row: Type agreement on the shared edges: agree; | `MAP_RESULTS.md`, Pratt › F1, the maps' agreement, on the maps as built: “The type, on the 22 pairs both call” | `score_map_test.py` |
| 24, 25, 0.884 | table row: Strength agreement on the shared edges: agree; | `MAP_RESULTS.md`, Bechky › F1, the maps' agreement, on the maps as built: “The strength, on the 25 pairs both call” | `score_map_test.py` |
| 17, 22, 0.321 | table row: Strength agreement on the shared edges: agree; | `MAP_RESULTS.md`, Pratt › F1, the maps' agreement, on the maps as built: “The strength, on the 22 pairs both call” | `score_map_test.py` |
| 23 | table row: Items the reader settled; chosen from A | `MAP_FEEDBACK_CHECK.md`, The attribution's report: “All 65 disagreements are classified, 23” | no script: an attribution made by reading (README) |
| 19, 4 | table row: Items the reader settled; chosen from A | `MAP_RESULTS.md`, Bechky › F2, the PI's settling: “The PI's choices” | `score_map_test.py` |
| 0 | table row: Items the reader settled; chosen from A | 0: the reader's own choices on Bechky: none listed (MAP_RESULTS.md, line 34) | no script: the sum shown |
| 42 | table row: Items the reader settled; chosen from A | `MAP_FEEDBACK_CHECK.md`, The attribution's report: “All 65 disagreements are classified, 23” | no script: an attribution made by reading (README) |
| 30, 10, 2 | table row: Items the reader settled; chosen from A | `MAP_RESULTS.md`, Pratt › F2, the PI's settling: “The PI's choices” | `score_map_test.py` |
| 30 | table row: Readings placed on the settled map, all | `MAP_RESULTS.md`, Bechky › F3, the placement: “Elements placed” | `score_map_test.py` |
| 28 | table row: Readings placed on the settled map, all | 30 − 2: less the planted R02 and R13 (MAP_RESULTS.md, lines 39 and 40) | no script: the sum shown |
| 2 | table row: Readings placed on the settled map, all | 2: the planted R02 and R13 | no script: the sum shown |
| 27 | table row: Readings placed on the settled map, all | `MAP_RESULTS.md`, Bechky › F5, the openings' check: “Faithful” | `score_map_test.py` |
| 17 | table row: Readings placed on the settled map, all | `MAP_RESULTS.md`, Pratt › F3, the placement: “Elements placed” | `score_map_test.py` |
| 15 | table row: Readings placed on the settled map, all | 17 − 2: less the planted R05 and R11 (MAP_RESULTS.md, lines 151 and 152) | no script: the sum shown |
| 2 | table row: Readings placed on the settled map, all | 2: the planted R05 and R11 | no script: the sum shown |
| 13 | table row: Readings placed on the settled map, all | `MAP_RESULTS.md`, Pratt › F5, the openings' check: “Faithful” | `score_map_test.py` |
| two | “human reader about two hours; the” | figure `hours.pi_settling_t39` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 10 | “sessions took about 10 minutes each” | figure `hours.chat_73` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 7 | “4 Argon) about 7, the openings'” | figure `hours.chat_81` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 5 | “openings' check (GPT-6) 5 and 3.” | figure `hours.chat_79` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 3 | “(GPT-6) 5 and 3. A fresh” | figure `hours.chat_80` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 65, 65, 46, 19 | “each of the 65 disagreements could” | `MAP_FEEDBACK_CHECK.md`, The attribution, in short: “All 65 disagreements trace to the” | no script: an attribution made by reading (README) |
| 12 | “in part, under 12 points (chained” | `MAP_FEEDBACK_CHECK.md`, Beside the feedback: “The points” | no script: an attribution made by reading (README) |
| two | “and so on); two models that” | figure `hours.step.T39 map task feedback` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 11, 12 | “diverge had raised 11 of the” | `MAP_FEEDBACK_CHECK.md`, Beside the feedback: “The points” | no script: an attribution made by reading (README) |
| twelve | “For twelve readings, six” | a count over `map_comparison_key.json`: the twelve tabs of the comparison (map_comparison_key.json) | `build_map_round2.py` |
| six | “For twelve readings, six of each” | a count over `map_comparison_key.json`: six of them Bechky's | `build_map_round2.py` |
| 12 | “the argument on 12 of 12” | `MAP_RESULTS.md`, F6, the PI's comparison: “Which account tells you more about what the” | `score_map_test.py` |
| 12 | “on 12 of 12 and could” | a count over `map_comparison_key.json`: the twelve tabs of the comparison (map_comparison_key.json) | `build_map_round2.py` |
| 12 | “more readily on 12 of 12” | `MAP_RESULTS.md`, F6, the PI's comparison: “Which account could another reader check more readily” | `score_map_test.py` |
| 12 | “on 12 of 12, though every” | a count over `map_comparison_key.json`: the twelve tabs of the comparison (map_comparison_key.json) | `build_map_round2.py` |
| three | “was very long, three of them” | a count over `MAP_RESULTS.md`: the PI's notes on three of the twelve tabs (MAP_RESULTS.md) | `score_map_test.py` |
| 1,000 | “it at about 1,000 characters longer” | `MAP_RESULTS.md`, F6, the PI's comparison: “Bechky R05” | `score_map_test.py` |
| 2,932 | “page, runs to 2,932 words for” | `MAP_ACCOUNT_SHORT_EXAMPLE_v2.md`, Lengths: “all twelve” | a script not kept here |
| twelve | “words for the twelve against 6,921.” | a count over `map_comparison_key.json`: the twelve readings of the comparison | `build_map_round2.py` |
| 6,921 | “the twelve against 6,921.” | `MAP_ACCOUNT_SHORT_EXAMPLE_v2.md`, Lengths: “all twelve” | a script not kept here |

### E.10 Reach against worth

| Number | In the text | From | Made by |
|---|---|---|---|
| 3, 2, 1, 0 | “claims (engaged directly 3, support in” | `RANKING_CHECK.md`: “A coding's score: the labels on” | `rank_map_readings.py` |
| 0.039, 28, 0.843 | “reader's worth was 0.039 over Bechky's” | `RANKING_CHECK.md`, Bechky (7 core claims): “The check: Spearman's rho between the” | `rank_map_readings.py` |
| −0.153, 15, 0.592 | “p 0.843) and −0.153 over Pratt's” | `RANKING_CHECK.md`, Pratt (10 core claims): “The check: Spearman's rho between the” | `rank_map_readings.py` |
| −0.076 | “0.592); over both, −0.076. The ranking” | `RANKING_CHECK.md`, Both papers together (secondary): “Spearman's rho over 43 real readings:” | `rank_map_readings.py` |
| five, 0.60, 0.40, 0.59 | “sorts scores into five bands (0.60” | `rank_map_readings.py`: “"gemini; second: astra). Stars from the” | the script's own rule |
| 0.25, 0.39, 0.10, 0.24, 0.10 | “0.40 to 0.59, 0.25 to 0.39” | `rank_map_readings.py`: “"0.25–0.39 three, 0.10–0.24 two, below 0.10” | the script's own rule |
| 14 | “in different bands: 14 of Bechky's” | a count over `ranking_check.json`: the flagged real readings (ranking_check.json) | `rank_map_readings.py` |
| 28 | “14 of Bechky's 28 readings and” | `RANKING_CHECK.md`, Bechky (7 core claims): “The check: Spearman's rho between the” | `rank_map_readings.py` |
| 2 | “28 readings and 2 of Pratt's” | a count over `ranking_check.json`: the same, Pratt | `rank_map_readings.py` |
| 15 | “2 of Pratt's 15. The worth” | `RANKING_CHECK.md`, Pratt (10 core claims): “The check: Spearman's rho between the” | `rank_map_readings.py` |
| 14, 15 | “arms, 14 of Bechky's and 15” | `AUTHOR_RATINGS_PLAN.md`: “How the paper's author rates the” (14), and its change of 15 Oct: “his 15 readings of the wager” (15); the numbers in `author_ratings_key.json` and `author_ratings_key_pratt.json` | `build_author_readings.py` (the keys) |
| 9, 14 | “Bechky rated 9 of her 14,” | the author's numbers, kept by the lead researcher, not in this repository: the readings she rated, of the 14 | a count over her numbers |
| 0.89 | “with a mean worth of 0.89” | the author's numbers, kept by the lead researcher, not in this repository: 8 points over the 9 readings she rated | no script: the mean shown |
| two | “0.89 (two marks she queried” | the author's numbers, kept by the lead researcher, not in this repository: the two marked with a question mark, read as written | a count over her numbers |
| 9 | “one paper and 9 readings, an” | the author's numbers, kept by the lead researcher, not in this repository: the readings she rated | a count over her numbers |

### E.11 The repository's entry for Bechky (worked example)

| Number | In the text | From | Made by |
|---|---|---|---|
| 28, six | “pilot's files: the 28 readings of” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`: “What step 10's entry would show” | a script not kept here (README) |
| 18 | “runs (Fable 5.1, 18 in four” | 4 + 5 + 5 + 4: Fable 5.1's runs: chats 23, 26, 27 and 46 (the entry's notes, 'The runs') | no script: the sum shown |
| four | “5.1, 18 in four runs; GPT” | 4: the four chats | no script: the sum shown |
| 10 | “GPT 6 Astra, 10 in two)” | 5 + 5: GPT 6 Astra's runs: chats 49 and 50 (the entry's notes, 'The runs') | no script: the sum shown |
| two | “Astra, 10 in two), which our” | 2: the two chats | no script: the sum shown |
| ten | “E.6) put in ten distinct points” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`, Points with the highest reach: “Reach is how much of the” | a script not kept here (README) |
| twelve, five | “opening (at most twelve words, never” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`, How this example was made: “Titles” | a script not kept here (README) |
| five | “row copied), the five of highest” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`, Points with the highest reach: “Reach is how much of the” | a script not kept here (README) |
| 0.62 | “of highest reach (0.62, 0.57, 0.57” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`, Points with the highest reach: “1” | a script not kept here (README) |
| 0.57, 0.57 | “highest reach (0.62, 0.57, 0.57, 0.43” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`, Points with the highest reach: “2” | a script not kept here (README) |
| 0.43 | “(0.62, 0.57, 0.57, 0.43, 0.38, all” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`, Points with the highest reach: “4” | a script not kept here (README) |
| 0.38 | “0.57, 0.57, 0.43, 0.38, all "Moderate"” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`, Points with the highest reach: “1” | a script not kept here (README) |
| four | “on the entry's four levels: Marginal” | the entry's levels: Marginal, Moderate, High and Max (REPOSITORY_ENTRY_EXAMPLE_bechky.md, line 11) | no script |
| 0.29, 0.69, 0.89 | “levels: Marginal to 0.29, Moderate to” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`, Points with the highest reach: “Reach is how much of the” | a script not kept here (README) |
| 15, 28, 8 | “filter (core) by 15 of 28” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`, Claims readings engage most often › Theoretical claims: “Engaged by 15 of the 28” | a script not kept here (README) |
| 13 | “narcotics case by 13 and the” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`, Claims readings engage most often › Empirical claims: “Engaged by 13 of the 28” | a script not kept here (README) |
| 12 | “toxicology case by 12. Eight of” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`, Claims readings engage most often › Empirical claims: “Engaged by 12 of the 28” | a script not kept here (README) |
| Eight, 15, 5, 7, one, one | “case by 12. Eight of the” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`, Claims readings engage most often › Empirical claims: “8 of the paper's 15 theoretical” | a script not kept here (README) |
| six | “entry's notes: the six runs used” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`: “What step 10's entry would show” | a script not kept here (README) |
| four, one | “six runs used four prompts and” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`, How this example was made: “The runs” | a script not kept here (README) |
| three | “for faithfulness, and three rest on” | `MAP_RESULTS.md`, Bechky › F5, the openings' check: “Faithful” | `score_map_test.py` |
| 23 | “outside), draws the 23 claims joined” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`, Claims readings engage most often › Empirical claims: “The claims' network: CLAIM_NETWORK_bechky.html draws all” | a script not kept here (README) |
| 28 | “One of the 28 readings generated” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`: “What step 10's entry would show” | a script not kept here (README) |
| 635 | “their home laboratories (p. 635); one” | Bechky (2020), p. 635, as reading R17 cites it | the paper, not in this repository |
| 623, 624 | “a spur to improve (pp. 623–624).” | Bechky (2020), pp. 623–624, as reading R17 cites them | the paper, not in this repository |
| 624, 632 | “did not change (pp. 624, 632), whereas” | Bechky (2020), pp. 624 and 632, as reading R17 cites them | the paper, not in this repository |
| 625 | “case challenging its results (p. 625).” | Bechky (2020), p. 625, as reading R17 cites it | the paper, not in this repository |
| 0.38 | “its reach is 0.38 (Moderate). The” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`, Points with the highest reach: “5” | a script not kept here (README) |
| five | “fifth among its five points, by” | `REPOSITORY_ENTRY_EXAMPLE_bechky.md`, Points with the highest reach: “Reach is how much of the” | a script not kept here (README) |
| 623 | “the critics instead (p. 623), and” | Bechky (2020), p. 623, as reading R17 cites it | the paper, not in this repository |
| 627 | “its values and its plans (p. 627).” | Bechky (2020), p. 627, as reading R17 cites it | the paper, not in this repository |

### E.12 Human time

| Number | In the text | From | Made by |
|---|---|---|---|
| 3.5 | “completeness check, about 3.5 hours a” | figure `hours.pi_coverage_check_pratt` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| twelve, 90 | “the coding of twelve readings' relations” | `RELATION_RESULTS.md`, Each reading: “The PI's coding of the twelve” | `score_relation_test.py` |
| two | “two maps, about two hours; grouping” | figure `hours.pi_settling_t39` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 45 | “returned within about 45 to 100” | the sheets of T32 and T33 came back 44 to 49 minutes after they were placed (figures hours.pi_worth_t32, hours.pi_grouping_t33, hours.pi_worth_t33), by hand from their times | no script |
| 100 | “about 45 to 100 minutes of” | the sheet of T29 came back 99 minutes after it was sent (figure hours.pi_worth_t29: 19:20 to 20:59) | no script |
| twelve | “the comparison of twelve accounts, about” | a count over `map_comparison_key.json`: the twelve tabs of the comparison (map_comparison_key.json) | `build_map_round2.py` |
| 30 | “twelve accounts, about 30 minutes. Model” | figure `hours.pi_comparison_t39` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| an hour | “the paper, around an hour; settling” | the lead researcher's words, 'It took around an hour' (figure hours.pi_matching_t36) | no script |
| 3 | “sessions ran from 3 to 61” | figure `hours.pratt_stage_A` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 61 | “from 3 to 61 minutes. The” | figure `hours.chat_55` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |

### E.13 Limits of the pilot's validity evidence

| Number | In the text | From | Made by |
|---|---|---|---|
| four | “was checked against four planted readings” | `RELATION_RESULTS.md`, M3. The planted readings: “Gemini 3.1 Pro: of the 4” | `score_relation_test.py` |
| twelve | “source and coded twelve readings' relations” | `RELATION_RESULTS.md`, Each reading: “The PI's coding of the twelve” | `score_relation_test.py` |
| 0.31 | “core mark (kappa 0.31 on Bechky)” | figure `bechky_2020.B.core` in `FIGURES_bechky_2020.md`, from BECHKY_AGREEMENT_LOG.md (agreement.py's record) | `build_figures.py` |
| 0.51 | “codes with kappa 0.51 and on” | `RELATION_RESULTS.md`, M1. The two coders on the main type (43 real readings): “both papers (43)” | `score_relation_test.py` |
| 0.59 | “sentence check at 0.59, is reported” | figure `pratt_2000.wager.markers` in `FIGURES_pratt_2000.md`, from stage2/marker_results/RESULTS.md; the interval from the two replies and the key (new) | `build_figures.py` |

### F.1 Fixing and registering the protocol (January)

| Number | In the text | From | Made by |
|---|---|---|---|
| twelve | “map task (the twelve points of” | `MAP_FEEDBACK_CHECK.md`, Beside the feedback: “The points” | no script: an attribution made by reading (README) |

### F.2 Two cohorts and the comparison they serve (February to April)

| Number | In the text | From | Made by |
|---|---|---|---|
| 43 | “on the pilot's 43 readings.” | `RELATION_RESULTS.md`, M1. The two coders on the main type (43 real readings): “both papers (43)” | `score_relation_test.py` |

### F.5 Indicative sizing and approvals

| Number | In the text | From | Made by |
|---|---|---|---|
| 7.5 | “paper costs about 7.5 hours of” | about 3.5 + 1 + 2.5 + 0.5: the sum of the parts that follow, rating and coding at the middle of 2 to 3 | no script: the sum shown |
| 3.5 | “(the completeness check 3.5, settling the” | figure `hours.pi_coverage_check_pratt` in `FIGURES_across.md`, from chats_models_hours.json | `build_figures.py` |
| 1 | “the map about 1, rating and” | 2 / 2: the two maps' settling, more than two hours for both (figure hours.pi_settling_t39) | no script: the sum shown |
| 2 | “rating and coding 2 to 3” | rating and coding a paper, by hand from E.12's times: the coding of twelve readings' relations, about 90 minutes, and the worth sheets, 45 to 100 minutes | no script |
| 3 | “coding 2 to 3, matching the” | the same estimate's upper end | no script |
| 0.5 | “citation-only readings about 0.5) and 3” | 1 / 2: the matching of the citation-only readings, around an hour for both papers (figure hours.pi_matching_t36) | no script: the sum shown |
| 3 | “about 0.5) and 3 to 5” | the model sessions a paper, by hand from E.1's times | no script |
| 5 | “and 3 to 5 hours of” | the same estimate's upper end | no script |
| 90 | “author's review: about 90 to 120” | 7.5 × 12: 7.5 hours for 12 papers, two cohorts of six | no script: the sum shown |
| 120 | “about 90 to 120 hours of” | 7.5 × 16: for 16, two of eight | no script: the sum shown |

### G. The research artifact: prototype and repository

| Number | In the text | From | Made by |
|---|---|---|---|
| 71 | “folder and runs 71 steps there” | `README.md`, Replaying the results: “replay.py copies this folder into a” | `replay.py`, as the README reports its run |
| 169 | “the one filed: 169 files come” | `README.md`, Replaying the results: “71 of 71 steps pass; 169” | `replay.py`, as the README reports its run |
| nine | “byte but for nine workbooks' save” | `README.md`, Replaying the results: “replay names them: nine workbooks (the” | `replay.py`, as the README reports its run |
| five | “save times, and five results files” | `README.md`, Replaying the results: “only in the time they were” | `replay.py`, as the README reports its run |
