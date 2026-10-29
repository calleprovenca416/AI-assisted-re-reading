# The markers of T32: agreement and rates

Written by `score_places_markers.py` from `reply_47_mark_places_opus.json`,
`reply_48_mark_places_astra.json` and `places_packs_key.json`, with the wager test's
checks, kappa and rates (`score_markers.py`). It says which chat wrote which reading:
for nobody until the PI's worth sheet is back. Arms: places given (chat 45, the readings
at the four places), places found (chat 46, the readings at places it found itself).
Rates are reported only if kappa on the seven codes is at least 0.60.

## The replies

- **Chat 47, Opus 5.5** (`reply_47_mark_places_opus.json`): paper given as "Bechky 2020"; 150 codes for the key's 150 sentences; N 33, R 86, RI 3, RA 16, P 10, U 0, C 2.
  Units: as the key, in order.
  Field rules: all followed.
  Longest quoted span in its notes: 4 words.
- **Chat 48, GPT 6 Astra** (`reply_48_mark_places_astra.json`): paper given as "Bechky 2020"; 150 codes for the key's 150 sentences; N 31, R 94, RI 6, RA 10, P 8, U 1, C 0.
  Units: as the key, in order.
  Field rules: all followed.
  Longest quoted span in its notes: 0 words.

## Agreement

150 sentences. Seven codes: the markers agree on 121 (0.807); Cohen's kappa **0.669**. Four groups (N; R, RI, RA; P; U, C), a diagnostic only: agreement 0.867, kappa 0.695.

Rows: Opus 5.5; columns: GPT 6 Astra.

| | N | R | RI | RA | P | U | C |
|---|---|---|---|---|---|---|---|
| **N** | 28 | 5 | · | · | · | · | · |
| **R** | 3 | 78 | 3 | · | 2 | · | · |
| **RI** | · | · | 2 | · | 1 | · | · |
| **RA** | · | 5 | 1 | 9 | 1 | · | · |
| **P** | · | 5 | · | · | 4 | 1 | · |
| **U** | · | · | · | · | · | · | · |
| **C** | · | 1 | · | 1 | · | · | · |

The cells off the diagonal with the most sentences:

- Opus N, Astra R: 5
- Opus P, Astra R: 5
- Opus RA, Astra R: 5
- Opus R, Astra N: 3
- Opus R, Astra RI: 3
- Opus R, Astra P: 2

## Rates by arm

Each cell gives Opus 5.5 / GPT 6 Astra.

| | places given (chat 45) | places found (chat 46) |
|---|---|---|
| readings | 4 | 4 |
| sentences | 81 | 69 |
| sentences that report (not N) | 66 / 67 | 51 / 52 |
| resolution rate (R, RI, RA) | 91% / 93% | 88% / 92% |
| strict rate (R) | 71% / 78% | 76% / 81% |
| P (reasoning stated) | 5 (2) / 5 (2) | 5 (2) / 3 (1) |
| U: warrant, mechanism, illustration | 0: 0, 0, 0 / 0: 0, 0, 0 | 0: 0, 0, 0 / 1: 0, 1, 0 |
| C: warrant, mechanism, illustration | 1: 1, 0, 0 / 0: 0, 0, 0 | 1: 1, 0, 0 / 0: 0, 0, 0 |
| drift | 0 / 1 | 1 / 2 |
| readings with a U or C as warrant | 1 / 0 | 1 / 0 |

## By reading

Each cell gives Opus 5.5 / GPT 6 Astra.

| reading | chat, reading | sentences | report | resolution | strict | P (stated) | U | C | drift | U or C as warrant |
|---|---|---|---|---|---|---|---|---|---|---|
| W01 | 46, R3 | 16 | 13 / 13 | 85% / 92% | 69% / 85% | 2 (1) / 1 (0) | 0 / 0 | 0 / 0 | 0 / 0 | no / no |
| W02 | 45, R3 | 20 | 15 / 15 | 100% / 100% | 67% / 73% | 0 (0) / 0 (0) | 0 / 0 | 0 / 0 | 0 / 0 | no / no |
| W03 | 46, R1 | 17 | 13 / 13 | 92% / 92% | 77% / 69% | 0 (0) / 1 (0) | 0 / 0 | 1 / 0 | 0 / 0 | yes / no |
| W04 | 45, R1 | 22 | 20 / 19 | 95% / 95% | 80% / 84% | 0 (0) / 1 (1) | 0 / 0 | 1 / 0 | 0 / 1 | yes / no |
| W05 | 46, R2 | 18 | 12 / 13 | 100% / 92% | 100% / 92% | 0 (0) / 1 (1) | 0 / 0 | 0 / 0 | 1 / 1 | no / no |
| W06 | 46, R4 | 18 | 13 / 13 | 77% / 92% | 62% / 77% | 3 (1) / 0 (0) | 0 / 1 | 0 / 0 | 0 / 1 | no / no |
| W07 | 45, R2 | 18 | 15 / 15 | 80% / 93% | 67% / 87% | 3 (0) / 1 (0) | 0 / 0 | 0 / 0 | 0 / 0 | no / no |
| W08 | 45, R4 | 21 | 16 / 18 | 88% / 83% | 69% / 67% | 2 (2) / 3 (1) | 0 / 0 | 0 / 0 | 0 / 0 | no / no |
