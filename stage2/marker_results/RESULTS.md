# The wager test's markers: agreement and rates

Written by `score_markers.py` from the four marker replies in stage2/marker_replies and
stage2/markers/KEY.json. Arms: system (the readings from the generation chats, written
from each paper's record), middle (the reading chats: the same prompt with the PDF),
plain (the plain chats: the PDF and a plain prompt). A paper's rates are reported only
if its kappa on the seven codes is at least 0.60, or, below it, where it has been
decided so, and then they are marked as below the bar.

## Pratt

### The replies

- **Chat 39, Opus 5.5** (`reply_39_mark_pratt_opus.json`): paper given as "Pratt 2000"; 203 codes for the key's 203 sentences; N 68, R 71, RI 33, RA 12, P 10, U 2, C 7.
  Units: as the key, in order.
  Field rules: all followed.
  Longest quoted span in its notes: 5 words.
- **Chat 40, GPT 6 Astra** (`reply_40_mark_pratt_astra.json`): paper given as "Pratt 2000"; 203 codes for the key's 203 sentences; N 55, R 80, RI 12, RA 11, P 27, U 8, C 10.
  Units: as the key, in order.
  Field rules: all followed.
  Longest quoted span in its notes: 0 words.

### Agreement

203 sentences. Seven codes: the markers agree on 141 (0.695); Cohen's kappa **0.593**. Four groups (N; R, RI, RA; P; U, C), a diagnostic only: agreement 0.754, kappa 0.595.

Rows: Opus 5.5; columns: GPT 6 Astra.

| | N | R | RI | RA | P | U | C |
|---|---|---|---|---|---|---|---|
| **N** | 47 | 4 | 5 | · | 10 | 2 | · |
| **R** | 1 | 65 | 1 | · | 1 | 3 | · |
| **RI** | 5 | 10 | 6 | · | 9 | 1 | 2 |
| **RA** | 1 | · | · | 11 | · | · | · |
| **P** | · | 1 | · | · | 6 | 2 | 1 |
| **U** | · | · | · | · | 1 | · | 1 |
| **C** | 1 | · | · | · | · | · | 6 |

By arm, the sentences on which the two markers give the same code (agreement only,
not a rate):

- system (generation chats): 42 of 63 (67%)
- middle (reading chats): 26 of 41 (63%)
- plain (plain chats): 73 of 99 (74%)

**Below the bar:** kappa 0.593 is below 0.60. The rates below are reported
by a decision of 11 Oct 2026, made after the result, as they stand: they rest on codes the two markers
agree on less than the bar requires, and weigh less than a paper's above it.
The cells off the diagonal with the most sentences:

- Opus RI, Astra R: 10
- Opus N, Astra P: 10
- Opus RI, Astra P: 9
- Opus N, Astra RI: 5
- Opus RI, Astra N: 5

### Rates by arm (below the bar)

Each cell gives Opus 5.5 / GPT 6 Astra.

| | system (generation chats) | middle (reading chats) | plain (plain chats) |
|---|---|---|---|
| readings | 5 | 5 | 5 |
| sentences | 63 | 41 | 99 |
| sentences that report (not N) | 45 / 43 | 28 / 32 | 62 / 73 |
| resolution rate (R, RI, RA) | 82% / 58% | 89% / 72% | 87% / 75% |
| strict rate (R) | 40% / 47% | 43% / 47% | 66% / 62% |
| P (reasoning stated) | 2 (1) / 10 (10) | 3 (0) / 6 (6) | 5 (1) / 11 (10) |
| U: warrant, mechanism, illustration | 0: 0, 0, 0 / 1: 0, 0, 1 | 0: 0, 0, 0 / 3: 0, 1, 2 | 2: 0, 2, 0 / 4: 1, 3, 0 |
| C: warrant, mechanism, illustration | 6: 0, 2, 4 / 7: 0, 6, 1 | 0: 0, 0, 0 / 0: 0, 0, 0 | 1: 0, 1, 0 / 3: 1, 1, 1 |
| drift | 0 / 0 | 0 / 0 | 3 / 12 |
| readings with a U or C as warrant | 0 / 0 | 0 / 0 | 0 / 2 |

## Bechky

### The replies

- **Chat 41, Opus 5.5** (`reply_41_mark_bechky_opus_as_sent.txt`): paper given as "Bechky 2020"; 193 codes for the key's 193 sentences; N 48, R 117, RI 11, RA 13, P 2, U 0, C 2. Came in two blocks, joined at B10-02 by the chat's own rule; 1 line of the chat's between them is not part of the object.
  Units: as the key, in order.
  Field rules: all followed.
  Longest quoted span in its notes: 2 words.
- **Chat 42, GPT 6 Astra** (`reply_42_mark_bechky_astra.json`): paper given as "Bechky 2020"; 193 codes for the key's 193 sentences; N 41, R 103, RI 8, RA 11, P 16, U 6, C 8.
  Units: as the key, in order.
  Field rules: all followed.
  Longest quoted span in its notes: 0 words.

### Agreement

193 sentences. Seven codes: the markers agree on 158 (0.819); Cohen's kappa **0.706**. Four groups (N; R, RI, RA; P; U, C), a diagnostic only: agreement 0.860, kappa 0.711.

Rows: Opus 5.5; columns: GPT 6 Astra.

| | N | R | RI | RA | P | U | C |
|---|---|---|---|---|---|---|---|
| **N** | 41 | 1 | · | · | 5 | 1 | · |
| **R** | · | 98 | 4 | · | 6 | 4 | 5 |
| **RI** | · | 3 | 4 | · | 3 | 1 | · |
| **RA** | · | 1 | · | 11 | · | · | 1 |
| **P** | · | · | · | · | 2 | · | · |
| **U** | · | · | · | · | · | · | · |
| **C** | · | · | · | · | · | · | 2 |

By arm, the sentences on which the two markers give the same code (agreement only,
not a rate):

- system (generation chats): 61 of 67 (91%)
- middle (reading chats): 35 of 39 (90%)
- plain (plain chats): 62 of 87 (71%)

### Rates by arm

Each cell gives Opus 5.5 / GPT 6 Astra.

| | system (generation chats) | middle (reading chats) | plain (plain chats) |
|---|---|---|---|
| readings | 4 | 5 | 5 |
| sentences | 67 | 39 | 87 |
| sentences that report (not N) | 55 / 55 | 27 / 27 | 63 / 70 |
| resolution rate (R, RI, RA) | 95% / 87% | 100% / 93% | 98% / 70% |
| strict rate (R) | 75% / 71% | 81% / 74% | 86% / 63% |
| P (reasoning stated) | 1 (0) / 4 (2) | 0 (0) / 0 (0) | 1 (0) / 12 (10) |
| U: warrant, mechanism, illustration | 0: 0, 0, 0 / 0: 0, 0, 0 | 0: 0, 0, 0 / 1: 1, 0, 0 | 0: 0, 0, 0 / 5: 4, 1, 0 |
| C: warrant, mechanism, illustration | 2: 0, 0, 2 / 3: 0, 0, 3 | 0: 0, 0, 0 / 1: 1, 0, 0 | 0: 0, 0, 0 / 4: 2, 1, 1 |
| drift | 0 / 3 | 0 / 0 | 2 / 4 |
| readings with a U or C as warrant | 0 / 0 | 0 / 2 | 0 / 4 |
