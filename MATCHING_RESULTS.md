# The matching test (T33): results

Written by `score_matching.py` from the files below, by `MATCHING_TEST_PLAN.md`. Kappas are pair kappas (Cohen's kappa on whether each pair of readings is put together); intervals are 95% bootstrap intervals of a difference, 2,000 resamples of the readings, seed 20261014.

## The files

| what | file | sha256 opens |
|---|---|---|
| key | `matching_key.json` | faaba978f4d0842a |
| blank | `grouping_sheet.xlsx` | e82e24e29fe71cd5 |
| sheet | `grouping_sheet_filled.xlsx` | b7f5d8ba181857dd |
| a1 | `reply_51_match_a_opus.json` | 901ce65243fad044 |
| a2 | `reply_52_match_a_astra.json` | e256f5720e64e112 |
| b1 | `reply_53_match_b_opus.json` | a6b0b0102f5c3162 |
| b2 | `reply_54_match_b_astra.json` | cd4d08241e31cce7 |

## The checks

- **a1:** counts.
- **a2:** counts.
- **b1:** counts.
- **b2:** counts.
- **sheet:** counts.

## Q1: does the reference make the count repeatable?

| figure | value |
|---|---|
| A, chats 51 and 52 | 0.923 |
| B, chats 53 and 54 by rule | 0.886 |
| Bj, chats 53 and 54 judged | 0.846 |
| Bp, chats 53 and 54 by rule, finer | 0.886 |
| P_A, arm A with the PI | 0.628 |
| P_B, arm B by rule with the PI | 0.762 |
| P_Bj, arm B judged with the PI | 0.777 |
| P_Bp, arm B by rule, finer, with the PI | 0.762 |

| difference | value | 95% interval | resamples left out |
|---|---|---|---|
| B - A | -0.037 | -0.298 to 0.292 | 0 |
| Bj - A | -0.077 | -0.368 to 0.276 | 0 |
| Bp - A | -0.037 | -0.298 to 0.292 | 0 |
| P_B - P_A | 0.134 | -0.092 to 0.382 | 0 |
| P_Bj - P_A | 0.149 | 0.020 to 0.324 | 0 |
| P_Bp - P_A | 0.134 | -0.092 to 0.382 | 0 |

**The answer, by rule:** repeatable without the reference (A is at least 0.80).

**The second reading, judged:** repeatable without the reference (A is at least 0.80).

**Neither arm finds the PI's points:** no.

**Claim agreement in arm B** (Cohen's kappa on the claim numbers, `none` a code): 0.836.

## Every pair of groupings

| groupings | pair kappa | adjusted Rand index |
|---|---|---|
| A1 A2 | 0.923 | 0.923 |
| A1 B1 | 0.754 | 0.754 |
| A1 B2 | 0.650 | 0.650 |
| A1 B1j | 0.954 | 0.954 |
| A1 B2j | 0.801 | 0.801 |
| A1 B1p | 0.754 | 0.754 |
| A1 B2p | 0.650 | 0.650 |
| A1 P | 0.662 | 0.662 |
| A2 B1 | 0.683 | 0.683 |
| A2 B2 | 0.584 | 0.584 |
| A2 B1j | 0.877 | 0.877 |
| A2 B2j | 0.728 | 0.728 |
| A2 B1p | 0.683 | 0.683 |
| A2 B2p | 0.584 | 0.584 |
| A2 P | 0.595 | 0.595 |
| B1 B2 | 0.886 | 0.886 |
| B1 B1j | 0.798 | 0.798 |
| B1 B2j | 0.689 | 0.689 |
| B1 B1p | 1.000 | 1.000 |
| B1 B2p | 0.886 | 0.886 |
| B1 P | 0.697 | 0.697 |
| B2 B1j | 0.691 | 0.691 |
| B2 B2j | 0.838 | 0.838 |
| B2 B1p | 0.886 | 0.886 |
| B2 B2p | 1.000 | 1.000 |
| B2 P | 0.828 | 0.828 |
| B1j B2j | 0.846 | 0.846 |
| B1j B1p | 0.798 | 0.798 |
| B1j B2p | 0.691 | 0.691 |
| B1j P | 0.703 | 0.703 |
| B2j B1p | 0.689 | 0.689 |
| B2j B2p | 0.838 | 0.838 |
| B2j P | 0.850 | 0.850 |
| B1p B2p | 0.886 | 0.886 |
| B1p P | 0.697 | 0.697 |
| B2p P | 0.828 | 0.828 |

## Q2: do the openings recur across vendors?

- Groups in the PI's grouping: 10.
- Groups found twice (readings of at least two of chats 23, 26, 27 and 46): 5; of them holding a reading of chat 49 or 50: 3.
- New readings sharing a group with an earlier one: 7 of 10.
- Groups holding a reading of chat 49: 5; of them holding a reading of chat 50: 4.

**The answer:** recur across vendors (3 of 5 groups found twice hold a new reading).

## Q3: readings that fit no claim of the reference

Chat 53 gives `none` to 0 of 28 readings, chat 54 to 1, both to 0.

## The groupings, reading by reading

| reading | chat | P | A1 | A2 | B1 claim | B2 claim | B1j | B2j |
|---|---|---|---|---|---|---|---|---|
| M01 | 50 | verifiability | 0 | 0 | C14 | C14 | 0 | 0 |
| M02 | 46 | capacity | 1 | 1 | C18 | C18 | 1 | 1 |
| M03 | 23 | dna subjective | 2 | 2 | C02 | none | 2 | 2 |
| M04 | 26 | firearms already changed | 3 | 3 | C16 | C16 | 3 | 3 |
| M05 | 23 | different demands | 4 | 4 | C19 | C19 | 4 | 4 |
| M06 | 26 | capacity | 5 | 5 | C18 | C18 | 5 | 5 |
| M07 | 27 | local challenge | 6 | 6 | C05 | C05 | 6 | 6 |
| M08 | 50 | power competition | 7 | 7 | C18 | C18 | 7 | 7 |
| M09 | 49 | staff sorting | 8 | 8 | C10 | C10 | 8 | 8 |
| M10 | 26 | accreditation | 9 | 9 | C03 | C17 | 9 | 9 |
| M11 | 50 | staff sorting | 8 | 8 | C10 | C10 | 8 | 8 |
| M12 | 27 | status | 10 | 10 | C21 | C21 | 10 | 10 |
| M13 | 23 | capacity | 1 | 11 | C18 | C18 | 1 | 1 |
| M14 | 26 | different demands | 11 | 12 | C13 | C02 | 11 | 11 |
| M15 | 23 | accreditation | 9 | 9 | C03 | C17 | 9 | 9 |
| M16 | 50 | capacity | 1 | 1 | C18 | C18 | 1 | 1 |
| M17 | 49 | verifiability | 0 | 0 | C14 | C14 | 0 | 0 |
| M18 | 49 | capacity | 1 | 1 | C18 | C18 | 1 | 1 |
| M19 | 27 | firearms already changed | 12 | 13 | C16 | C16 | 3 | 3 |
| M20 | 26 | staff sorting | 8 | 8 | C10 | C10 | 8 | 8 |
| M21 | 46 | firearms already changed | 12 | 13 | C16 | C16 | 3 | 3 |
| M22 | 49 | accreditation | 13 | 14 | C17 | C17 | 12 | 9 |
| M23 | 46 | accreditation | 13 | 14 | C17 | C17 | 12 | 9 |
| M24 | 27 | accreditation | 13 | 14 | C17 | C17 | 12 | 9 |
| M25 | 49 | local challenge | 6 | 6 | C05 | C05 | 6 | 6 |
| M26 | 27 | capacity | 14 | 15 | C05 | C05 | 13 | 12 |
| M27 | 46 | staff sorting | 8 | 8 | C10 | C10 | 8 | 8 |
| M28 | 50 | accreditation | 13 | 14 | C17 | C17 | 12 | 9 |

## The voice of the passages arm B names, by the PI's groups (described, not tested)

| PI's group | readings | reported | author's account |
|---|---|---|---|
| verifiability | M01, M17 | 14 | 6 |
| capacity | M02, M06, M13, M16, M18, M26 | 59 | 1 |
| dna subjective | M03 | 8 | 2 |
| firearms already changed | M04, M19, M21 | 27 | 3 |
| different demands | M05, M14 | 19 | 1 |
| local challenge | M07, M25 | 12 | 8 |
| power competition | M08 | 6 | 2 |
| staff sorting | M09, M11, M20, M27 | 39 | 0 |
| accreditation | M10, M15, M22, M23, M24, M28 | 47 | 7 |
| status | M12 | 9 | 1 |

The limits known in advance are those of `MATCHING_TEST_PLAN.md`.

---

## Added after the scorer ran

*Notes added below the scorer's output on 14 Oct; the text above is the
scorer's, unchanged.*

- **The caveat of the plan's dated change.** The PI's grouping (P) was
  made after the four coder chats ran, with their replies in hand; it is not
  blind to them. Every figure that uses P carries this caveat: P_A, P_B, P_Bj,
  P_Bp, their differences, the cases' test of P_B against P_A, "neither arm
  finds the PI's points", all of Q2 and the voice table's grouping. The
  figures between the coders (A, B, Bj, Bp, their differences and the claim
  agreement) do not use P.
- **Checked independently:** every figure was recomputed from the inputs with
  separate code, and all 700 comparisons agree, the cases and answers following
  from the plan's rules, and `matching_results.json` agreeing with this file.
  B1p and B2p came out the same as B1 and B2 (within every claim's group the
  passages join all its readings), and two of the PI's labels end in a space
  and capitals vary, which the scorer's rule for labels settles.
