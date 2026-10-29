# T39, measure 8: a rough ranking of the readings by the map

Fable's score (proposed on 19 Oct), unchanged, and its check against the PI's worth, as `MAP_TEST_PLAN.md`'s addition of 19 Oct 2026 defines them. Exploratory: not a criterion of T39. Written by `rank_map_readings.py` (sha256 opens c52a8dab).

A coding's score: the labels on the paper's core claims, weighted contested 3, unsupported 2, weakened 1, idle ½, restated 0, over 3 × the core claims. A reading's score is the lower of its two codings' (first: `gemini`; second: `astra`). Stars from the score rounded to two decimals: ≥ 0.60 five, 0.40–0.59 four, 0.25–0.39 three, 0.10–0.24 two, below 0.10 one. Flag: the two codings give different stars. Cost: the passages in the reading's evidence list. It measures how much of the argument a reading would bring down if it were right, not whether it is right.

## Bechky (7 core claims)

**The check:** Spearman's rho between the score and the PI's worth, 28 real readings: 0.039, permutation p 0.843 (8429 of 10,000 shuffles at least as far from zero). Read as fixed: **no clear relation at this size**.

Each coding's own score against the PI's worth: first -0.159, second 0.080. Mean score at each worth: 0: 0.270 (n 3); 1: 0.381 (n 4); 2: 0.291 (n 17); 3: 0.405 (n 4).

| reading | worth | first coding | second coding | score | stars | flag | cost |
|---|---|---|---|---|---|---|---|
| R22 | 2 | 0.62 | 0.62 | 0.62 | 5 |  | 8 |
| R23 | 2 | 0.62 | 0.62 | 0.62 | 5 |  | 6 |
| R03 | 2 | 0.57 | 0.57 | 0.57 | 4 |  | 13 |
| R05 | 2 | 0.57 | 0.57 | 0.57 | 4 |  | 25 |
| R12 | 1 | 0.62 | 0.57 | 0.57 | 4 | yes (5/4) | 14 |
| R26 | 0 | 0.52 | 0.52 | 0.52 | 4 |  | 12 |
| R01 | 3 | 0.48 | 0.57 | 0.48 | 4 |  | 6 |
| R19 | 1 | 0.48 | 0.48 | 0.48 | 4 |  | 19 |
| R20 | 3 | 0.48 | 0.48 | 0.48 | 4 |  | 5 |
| R25 | 1 | 0.52 | 0.48 | 0.48 | 4 |  | 14 |
| R24 | 2 | 0.43 | 0.43 | 0.43 | 4 |  | 4 |
| R07 | 2 | 0.48 | 0.38 | 0.38 | 3 | yes (4/3) | 9 |
| R17 | 2 | 0.38 | 0.38 | 0.38 | 3 |  | 8 |
| R18 | 3 | 0.43 | 0.38 | 0.38 | 3 | yes (4/3) | 6 |
| R28 | 2 | 0.43 | 0.33 | 0.33 | 3 | yes (4/3) | 13 |
| R29 | 2 | 0.31 | 0.31 | 0.31 | 3 |  | 10 |
| R06 | 2 | 0.29 | 0.29 | 0.29 | 3 |  | 15 |
| R09 | 2 | 0.52 | 0.29 | 0.29 | 3 | yes (4/3) | 15 |
| R21 | 3 | 0.38 | 0.29 | 0.29 | 3 |  | 12 |
| R08 | 2 | 0.31 | 0.17 | 0.17 | 2 | yes (3/2) | 16 |
| R10 | 0 | 0.43 | 0.14 | 0.14 | 2 | yes (4/2) | 5 |
| R27 | 0 | 0.48 | 0.14 | 0.14 | 2 | yes (4/2) | 5 |
| R04 | 2 | 0.43 | 0.00 | 0.00 | 1 | yes (4/1) | 5 |
| R11 | 1 | 0.14 | 0.00 | 0.00 | 1 | yes (2/1) | 7 |
| R14 | 2 | 0.29 | 0.00 | 0.00 | 1 | yes (3/1) | 5 |
| R15 | 2 | 0.48 | 0.00 | 0.00 | 1 | yes (4/1) | 5 |
| R16 | 2 | 0.43 | 0.00 | 0.00 | 1 | yes (4/1) | 13 |
| R30 | 2 | 0.48 | 0.00 | 0.00 | 1 | yes (4/1) | 3 |

The planted readings, which have no worth:

| reading | first coding | second coding | score | stars | flag | cost |
|---|---|---|---|---|---|---|
| R13 | 0.57 | 0.57 | 0.57 | 4 |  | 12 |
| R02 | 0.38 | 0.38 | 0.38 | 3 |  | 12 |

## Pratt (10 core claims)

**The check:** Spearman's rho between the score and the PI's worth, 15 real readings: -0.153, permutation p 0.592 (5923 of 10,000 shuffles at least as far from zero). Read as fixed: **no clear relation at this size**.

Each coding's own score against the PI's worth: first -0.209, second 0.029. Mean score at each worth: 0: 0.347 (n 5); 1: 0.440 (n 5); 2: 0.223 (n 5).

| reading | worth | first coding | second coding | score | stars | flag | cost |
|---|---|---|---|---|---|---|---|
| R09 | 0 | 0.70 | 0.70 | 0.70 | 5 |  | 9 |
| R14 | 1 | 0.70 | 0.73 | 0.70 | 5 |  | 7 |
| R10 | 2 | 0.63 | 0.63 | 0.63 | 5 |  | 8 |
| R15 | 1 | 0.60 | 0.60 | 0.60 | 5 |  | 8 |
| R04 | 1 | 0.45 | 0.45 | 0.45 | 4 |  | 5 |
| R08 | 0 | 0.48 | 0.45 | 0.45 | 4 |  | 4 |
| R12 | 1 | 0.48 | 0.45 | 0.45 | 4 |  | 11 |
| R17 | 0 | 0.45 | 0.48 | 0.45 | 4 |  | 8 |
| R03 | 2 | 0.20 | 0.20 | 0.20 | 2 |  | 13 |
| R02 | 0 | 0.17 | 0.13 | 0.13 | 2 |  | 6 |
| R06 | 2 | 0.13 | 0.13 | 0.13 | 2 |  | 5 |
| R16 | 2 | 0.12 | 0.70 | 0.12 | 2 | yes (2/5) | 12 |
| R01 | 2 | 0.03 | 0.03 | 0.03 | 1 |  | 10 |
| R07 | 0 | 0.00 | 0.00 | 0.00 | 1 |  | 5 |
| R13 | 1 | 0.45 | 0.00 | 0.00 | 1 | yes (4/1) | 7 |

The planted readings, which have no worth:

| reading | first coding | second coding | score | stars | flag | cost |
|---|---|---|---|---|---|---|
| R05 | 0.63 | 0.23 | 0.23 | 2 | yes (5/2) | 12 |
| R11 | 0.00 | 0.00 | 0.00 | 1 |  | 13 |

## Both papers together (secondary)

Spearman's rho over 43 real readings: -0.076, permutation p 0.630 (6300 of 10,000 shuffles). Read as fixed, as secondary: **no clear relation at this size**. Each coding's own score: first -0.162, second -0.038.

## Fable's twelve figures, recomputed

| paper | reading | Fable: first / second | recomputed | Fable's findings | cost | same |
|---|---|---|---|---|---|---|
| Pratt | R09 | 0.70 / 0.70 | 0.70 / 0.70 | 9 | 9 | yes |
| Pratt | R14 | 0.70 / 0.73 | 0.70 / 0.73 | 7 | 7 | yes |
| Bechky | R22 | 0.62 / 0.62 | 0.62 / 0.62 | 8 | 8 | yes |
| Bechky | R05 | 0.57 / 0.57 | 0.57 / 0.57 | 25 | 25 | yes |
| Pratt | R08 | 0.48 / 0.45 | 0.48 / 0.45 | 4 | 4 | yes |
| Bechky | R07 | 0.48 / 0.38 | 0.48 / 0.38 | 9 | 9 | yes |
| Bechky | R29 | 0.31 / 0.31 | 0.31 / 0.31 | 10 | 10 | yes |
| Pratt | R03 | 0.20 / 0.20 | 0.20 / 0.20 | 13 | 13 | yes |
| Pratt | R02 | 0.17 / 0.13 | 0.17 / 0.13 | 6 | 6 | yes |
| Bechky | R27 | 0.48 / 0.14 | 0.48 / 0.14 | 5 | 5 | yes |
| Pratt | R01 | 0.03 / 0.03 | 0.03 / 0.03 | 10 | 10 | yes |
| Bechky | R16 | 0.43 / 0.00 | 0.43 / 0.00 | 13 | 13 | yes |

Seed 20261027, one stream: Bechky's shuffles, then Pratt's, then both papers'. Inputs, by sha256:

- `map_results.json`: 0dfdeab883118c2a192fbb890efc2a958eb4bf3abc55c301a2996dc2847f396d
- `relation_results.json`: 5dff925eb5d23484ae44642628f29fd12e28366ef4db1e5fc907c4ad97a1fc47
- `map_round2_key.json`: 16203667c98851db4412f5ec1e58c9dabcbff9b666558a7ac5e85a6ce7b6b313
- `reply_77_bechky_place_argon.json`: 099915f0e41be3c0c0d1da89bf74a95b32d880e75bd1f7bad56555e6309c4677
- `reply_78_pratt_place_argon.json`: 3188febbc4a9923c5124d507ed41b5be65515c4e7e91225b024d1573fb7f6dbc
