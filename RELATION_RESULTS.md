# The relation test (T37): results

Written by `score_relation_test.py score` (sha256 opens 2e49c8f0) by `RELATION_TEST_PLAN.md`, from the key `relation_key.json` (opens b8598261), the PI's coding sheet `relation_sheet_filled.xlsx` (opens e27bf648), the PI's check of the planted readings `planted_check_filled.xlsx` (opens 2f2df729), and the four coders' replies: chat 64 `reply_64_bechky_relation_gemini.json` (opens 1b1d2bd4), chat 65 `reply_65_bechky_relation_astra.json` (opens 5d7fdc19), chat 66 `reply_66_pratt_relation_gemini.json` (opens 19fcfb13), chat 67 `reply_67_pratt_relation_astra.json` (opens 37017d24).

Described, not tested: the plan fixes no bar. Agreement between the coders shows that the coding can be repeated across two vendors, not that it is right; the PI's sample and the planted readings speak to that, and both are small. A type says what a reading does to a claim of the index, not whether it holds or is worth pursuing. The readings are coded as written, not as standard statements. GPT 6 Astra codes ten readings its own model wrote; Gemini none.

**Checks:** the key is the builder's, from the inputs as they are; the readings files and the blank sheets are the key's; all four replies count and quote no span of over eight words; on both of the PI's sheets no cell outside the yellow ones changed, and every answer reads.

## M1. The two coders on the main type (43 real readings)

| readings | types: agree | types: kappa | levels: agree | levels: kappa |
|---|---|---|---|---|
| Bechky (28) | 18 | 0.449 | 20 | 0.145 |
| Pratt (15) | 10 | 0.559 | 13 | 0.659 |
| both papers (43) | 28 | 0.511 | 33 | 0.360 |

Both papers, types: 95% interval 0.306 to 0.686 (2000 of 2000 resamples gave a kappa).

Both papers, levels: 95% interval 0.042 to 0.640 (2000 of 2000 resamples gave a kappa).

**Bechky, types:**

| Gemini in rows, Astra in columns | `inverts` | `other_mechanism` | `rereads_evidence` | `challenges_premise` | `complements` |
|---|---|---|---|---|---|
| `inverts` | 1 | 1 | 0 | 0 | 0 |
| `other_mechanism` | 0 | 12 | 0 | 0 | 7 |
| `rereads_evidence` | 0 | 0 | 4 | 0 | 0 |
| `challenges_premise` | 0 | 0 | 2 | 1 | 0 |
| `complements` | 0 | 0 | 0 | 0 | 0 |

**Bechky, levels:**

| Gemini in rows, Astra in columns | `inverts` | `dismantles` | `complements` |
|---|---|---|---|
| `inverts` | 1 | 1 | 0 |
| `dismantles` | 0 | 19 | 7 |
| `complements` | 0 | 0 | 0 |

**Pratt, types:**

| Gemini in rows, Astra in columns | `inverts` | `other_mechanism` | `rereads_evidence` | `challenges_premise` |
|---|---|---|---|---|
| `inverts` | 3 | 0 | 1 | 0 |
| `other_mechanism` | 0 | 3 | 0 | 0 |
| `rereads_evidence` | 1 | 1 | 2 | 1 |
| `challenges_premise` | 0 | 1 | 0 | 2 |

**Pratt, levels:**

| Gemini in rows, Astra in columns | `inverts` | `dismantles` |
|---|---|---|
| `inverts` | 3 | 1 |
| `dismantles` | 1 | 10 |

**Both papers, types:**

| Gemini in rows, Astra in columns | `inverts` | `other_mechanism` | `rereads_evidence` | `challenges_premise` | `complements` |
|---|---|---|---|---|---|
| `inverts` | 4 | 1 | 1 | 0 | 0 |
| `other_mechanism` | 0 | 15 | 0 | 0 | 7 |
| `rereads_evidence` | 1 | 1 | 6 | 1 | 0 |
| `challenges_premise` | 0 | 1 | 2 | 3 | 0 |
| `complements` | 0 | 0 | 0 | 0 | 0 |

**Both papers, levels:**

| Gemini in rows, Astra in columns | `inverts` | `dismantles` | `complements` |
|---|---|---|---|
| `inverts` | 4 | 2 | 0 |
| `dismantles` | 1 | 29 | 7 |
| `complements` | 0 | 0 | 0 |

## M2. The main claim

| readings | the same main claim | of those, the same main type |
|---|---|---|
| Bechky (28) | 21 | 14 |
| Pratt (15) | 10 | 7 |
| both papers (43) | 31 | 21 |

## M3. The planted readings

| reading | its claim | written to be | the PI | Gemini | Astra |
|---|---|---|---|---|---|
| Bechky R02 | C04 | complements | confirmed | missed (C04 challenges_premise; C13 complements, C18 other_mechanism) | missed (C04 challenges_premise; C13 complements, C18 other_mechanism) |
| Bechky R13 | C05 | inverts | confirmed | caught (C05 inverts; C17 other_mechanism, C18 other_mechanism) | caught (C05 inverts; C17 other_mechanism, C18 other_mechanism) |
| Pratt R05 | C02 | other_mechanism | confirmed | caught (C02 other_mechanism; C12 inverts, C24 complements) | caught (C02 other_mechanism; C11 other_mechanism, C24 restates) |
| Pratt R11 | C13 | restates | confirmed | caught (C13 restates; C12 restates, C15 restates) | caught (C13 restates; C15 restates, C17 restates) |

Gemini 3.1 Pro: of the 4 the PI confirmed, caught 3, caught aside 0, missed 1.

GPT 6 Astra at max: of the 4 the PI confirmed, caught 3, caught aside 0, missed 1.

## M4. Against the PI, on the PI's twelve

| | readings | the same main claim | the same main type | the same level |
|---|---|---|---|---|
| Gemini against the PI, Bechky | 6 | 3 | 4 | 5 |
| Gemini against the PI, Pratt | 6 | 5 | 6 | 6 |
| Gemini against the PI, both papers | 12 | 8 | 10 | 11 |
| Astra against the PI, Bechky | 6 | 4 | 4 | 5 |
| Astra against the PI, Pratt | 6 | 5 | 5 | 5 |
| Astra against the PI, both papers | 12 | 9 | 9 | 10 |
| Gemini against Astra, Bechky | 6 | 3 | 4 | 4 |
| Gemini against Astra, Pratt | 6 | 4 | 5 | 5 |
| Gemini against Astra, both papers | 12 | 7 | 9 | 9 |

Each count on its own: the same main type is counted whether or not the main claim is the same.

## M5. Described

**Each coder's types and levels, on the 43 real readings:**

| | `inverts` | `other_mechanism` | `rereads_evidence` | `challenges_premise` | `complements` | `restates` | `none` |
|---|---|---|---|---|---|---|---|
| Gemini 3.1 Pro | 6 | 22 | 9 | 6 | 0 | 0 | 0 |
| GPT 6 Astra at max | 5 | 18 | 9 | 4 | 7 | 0 | 0 |

| | inverts | dismantles | complements | restates | none |
|---|---|---|---|---|---|
| Gemini 3.1 Pro | 6 | 37 | 0 | 0 | 0 |
| GPT 6 Astra at max | 5 | 31 | 7 | 0 | 0 |

**The PI's worth by level, where the two coders agree on the level:**

| level | readings | mean worth | worths |
|---|---|---|---|
| inverts | 4 | 1.25 | 0, 1, 2, 2 |
| dismantles | 29 | 1.52 | 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3 |
| complements | 0 | — | — |
| restates | 0 | — | — |
| none | 0 | — | — |

The PI's worth was given on three occasions knowing different things (the sheets of 11 Oct, of T32 and of T33), so these means are described, not compared.

**Levels by the chat that wrote the reading (Bechky):**

| coder | chat | inverts | dismantles | complements | restates | none |
|---|---|---|---|---|---|---|
| Gemini 3.1 Pro | 23 | 0 | 4 | 0 | 0 | 0 |
| Gemini 3.1 Pro | 26 | 1 | 4 | 0 | 0 | 0 |
| Gemini 3.1 Pro | 27 | 1 | 4 | 0 | 0 | 0 |
| Gemini 3.1 Pro | 46 | 0 | 4 | 0 | 0 | 0 |
| Gemini 3.1 Pro | 49 | 0 | 5 | 0 | 0 | 0 |
| Gemini 3.1 Pro | 50 | 0 | 5 | 0 | 0 | 0 |
| GPT 6 Astra at max | 23 | 0 | 4 | 0 | 0 | 0 |
| GPT 6 Astra at max | 26 | 1 | 4 | 0 | 0 | 0 |
| GPT 6 Astra at max | 27 | 0 | 5 | 0 | 0 | 0 |
| GPT 6 Astra at max | 46 | 0 | 3 | 1 | 0 | 0 |
| GPT 6 Astra at max | 49 | 0 | 2 | 3 | 0 | 0 |
| GPT 6 Astra at max | 50 | 0 | 2 | 3 | 0 | 0 |

**Levels by arm (Pratt):**

| coder | arm | inverts | dismantles | complements | restates | none |
|---|---|---|---|---|---|---|
| Gemini 3.1 Pro | system | 2 | 3 | 0 | 0 | 0 |
| Gemini 3.1 Pro | middle | 2 | 3 | 0 | 0 | 0 |
| Gemini 3.1 Pro | plain | 0 | 5 | 0 | 0 | 0 |
| GPT 6 Astra at max | system | 1 | 4 | 0 | 0 | 0 |
| GPT 6 Astra at max | middle | 2 | 3 | 0 | 0 | 0 |
| GPT 6 Astra at max | plain | 1 | 4 | 0 | 0 | 0 |

## Each reading

| reading | source | Gemini | Astra | the PI | worth |
|---|---|---|---|---|---|
| Bechky R01 | M16 | C18 other_mechanism | C18 other_mechanism |  | 3 |
| Bechky R02 | planted (chat 62) | C04 challenges_premise | C04 challenges_premise |  |  |
| Bechky R03 | M26 | C05 other_mechanism | C05 other_mechanism |  | 2 |
| Bechky R04 | M09 | C10 other_mechanism | C10 complements |  | 2 |
| Bechky R05 | M13 | C18 other_mechanism | C05 other_mechanism | C18 other_mechanism | 2 |
| Bechky R06 | M21 | C16 rereads_evidence | C16 rereads_evidence |  | 2 |
| Bechky R07 | M15 | C03 other_mechanism | C03 other_mechanism | C03 other_mechanism | 2 |
| Bechky R08 | M03 | C04 challenges_premise | C04 challenges_premise |  | 2 |
| Bechky R09 | M04 | C05 challenges_premise | C16 rereads_evidence |  | 2 |
| Bechky R10 | M20 | C20 inverts | C10 inverts |  | 0 |
| Bechky R11 | M27 | C10 other_mechanism | C10 complements |  | 1 |
| Bechky R12 | M14 | C02 rereads_evidence | C02 rereads_evidence |  | 1 |
| Bechky R13 | planted (chat 62) | C05 inverts | C05 inverts |  |  |
| Bechky R14 | M11 | C10 other_mechanism | C10 complements |  | 2 |
| Bechky R15 | M28 | C17 other_mechanism | C17 complements |  | 2 |
| Bechky R16 | M17 | C05 other_mechanism | C14 complements | C14 complements | 2 |
| Bechky R17 | M07 | C05 other_mechanism | C05 other_mechanism |  | 2 |
| Bechky R18 | M25 | C05 other_mechanism | C05 other_mechanism |  | 3 |
| Bechky R19 | M05 | C19 challenges_premise | C19 rereads_evidence |  | 1 |
| Bechky R20 | M18 | C18 other_mechanism | C18 other_mechanism |  | 3 |
| Bechky R21 | M01 | C05 other_mechanism | C14 complements |  | 3 |
| Bechky R22 | M23 | C17 other_mechanism | C17 other_mechanism | C01 rereads_evidence | 2 |
| Bechky R23 | M24 | C17 other_mechanism | C17 other_mechanism |  | 2 |
| Bechky R24 | M08 | C18 other_mechanism | C21 other_mechanism |  | 2 |
| Bechky R25 | M02 | C18 other_mechanism | C18 other_mechanism |  | 1 |
| Bechky R26 | M06 | C18 rereads_evidence | C18 rereads_evidence |  | 0 |
| Bechky R27 | M10 | C17 other_mechanism | C03 other_mechanism | C03 other_mechanism | 0 |
| Bechky R28 | M19 | C16 rereads_evidence | C16 rereads_evidence |  | 2 |
| Bechky R29 | M12 | C21 inverts | C21 other_mechanism | C21 inverts | 2 |
| Bechky R30 | M22 | C17 other_mechanism | C17 complements |  | 2 |
| Pratt R01 | P14 | C07 other_mechanism | C07 other_mechanism | C07 other_mechanism | 2 |
| Pratt R02 | P04 | C23 rereads_evidence | C29 rereads_evidence | C29 rereads_evidence | 0 |
| Pratt R03 | P09 | C56 inverts | C56 inverts | C56 inverts | 2 |
| Pratt R04 | P02 | C28 rereads_evidence | C08 challenges_premise |  | 1 |
| Pratt R05 | planted (chat 63) | C02 other_mechanism | C02 other_mechanism |  |  |
| Pratt R06 | P07 | C29 inverts | C29 inverts |  | 2 |
| Pratt R07 | P11 | C09 challenges_premise | C09 challenges_premise |  | 0 |
| Pratt R08 | P13 | C20 inverts | C20 rereads_evidence | C20 inverts | 0 |
| Pratt R09 | P15 | C13 rereads_evidence | C13 rereads_evidence | C13 rereads_evidence | 0 |
| Pratt R10 | P03 | C12 other_mechanism | C12 other_mechanism |  | 2 |
| Pratt R11 | planted (chat 63) | C13 restates | C13 restates |  |  |
| Pratt R12 | P01 | C20 other_mechanism | C07 other_mechanism |  | 1 |
| Pratt R13 | P08 | C09 inverts | C09 inverts |  | 1 |
| Pratt R14 | P06 | C27 challenges_premise | C12 challenges_premise | C27 challenges_premise | 1 |
| Pratt R15 | P10 | C28 rereads_evidence | C28 other_mechanism |  | 1 |
| Pratt R16 | P05 | C07 challenges_premise | C01 other_mechanism |  | 2 |
| Pratt R17 | P12 | C09 rereads_evidence | C09 inverts |  | 0 |

---

*Notes added below the scorer's output on 17 Oct; the text above is the scorer's, unchanged.*

**The Google coder was Gemini 4 Argon, not Gemini 3.1 Pro.** Chats 64 and 66 ran on Gemini 4 Argon at Thinking Level High; every "Gemini 3.1 Pro" and "Gemini" above is that model. The coders are still of two vendors. The four chats ran as their steps say, with no search seen; GPT 6 Astra took about 4 minutes a chat and Argon about 7.

**Checked independently.** Every figure above, the 590 items of the tables among them, was recomputed from the plan, a written statement of the scorer's definitions, the key, the four replies and the PI's sheets, with separate code: all agree. The intervals' third decimals sit next to near-ties among the resampled kappas (one place either way would print 0.688 for 0.686, and 0.041 for 0.042). The PI's note marks Bechky R27 as a condensed R07, which the PI coded alike.

**Described, from the tables above:**
- Of the 15 real readings on which the coders' main types differ, 10 differ on the same main claim, and 7 are one split, all on Bechky: Argon codes other_mechanism where Astra codes complements. Argon codes no real reading complements.
- Six of those seven were written by GPT 6 Astra's own model (chats 49 and 50). Of those ten readings, Astra codes six complements and Argon all ten other_mechanism. One of the ten is in the PI's sample, Bechky R16; the PI coded it as Astra did, complements, on the same claim. The plan names this as a limit; the pattern is described, not tested.
- Both coders missed the same planted reading, Bechky R02, written to complement C04: both coded it challenges_premise on C04, the type that comes before complements in the brief's order.
- One reading names its own move, Pratt R08 ("inversion"); Argon and the PI coded it inverts, Astra rereads_evidence.
- The PI's coding of the twelve took about 90 minutes, against the plan's 40.

**Complements, and the brief's order.** On the 43 real readings unless said:
- Argon gives complements as no reading's main type, but 18 times as the type of an other claim, on 16 readings (12 times on 11 Bechky readings). Astra gives it as the main type on 7 readings, and 22 times as an other claim's type, on 20 readings, which include those 7.
- Of the seven splits (Argon other_mechanism, Astra complements), two differ on the main claim: on Bechky R16 and R21, Argon's main relation is other_mechanism on C05, with C14 complements among its other claims, and Astra's is complements on C14, as the PI's is on R16 (R21 is not in the PI's sample). The other five, Bechky R04, R11, R14, R15 and R30, are on the same claim.
- On R04 and R14, Argon's reasons say the reading credits another mechanism in part; on the other five splits they describe an outright replacement. On R04, R11 and R14, Astra's reasons say the reading adds to the paper's account; on R15 and R30, that it keeps the paper's cause for the reform's timing and credits its content to a prior source, which is in substance the other mechanism Argon names. None of the fourteen reasons on the seven splits names an order, a rule or a type.
- In the brief, complements comes fifth of the six types, and when more than one fits, the first that fits is given; its example settles a reading that could be said both to put another mechanism in place and to add a condition as other_mechanism. The brief draws no line where its types meet. Three of complements' four kinds of change sit next to earlier types: adding a condition (as the example shows) and adding a mechanism, next to other_mechanism ("in place of the paper's"); and changing the claim's scope, next to challenges_premise (a boundary the claim takes for granted).
- The planted complement, Bechky R02 against C04: both coders code it challenges_premise on C04, each with C13 complements and C18 other_mechanism as its other claims.

**Agreement as a filter.**
- On the PI's twelve, the coders agree on the type on 9, and the PI gives the same type on 8 of them; on 5 of the 9 they also share the main claim, and the PI matches both on claim and type on 4. On Bechky R22 the coders give other_mechanism on C17, and the PI gives rereads_evidence on C01, which both coders list among their other claims. Of the three on which the types differ, the PI sides with Argon on Bechky R29 and Pratt R08 (inverts) and with Astra on Bechky R16 (complements).
- Across the 43, the coders agree on the type on 28, and on both claim and type on 21. Keeping only the 28 would drop 15: all 7 that Astra codes complements, and 3 of the 7 that either coder codes inverts (Bechky R29, Pratt R08 and Pratt R17), two of which, R29 and R08, the PI coded inverts.
- Inverts, other_mechanism and challenges_premise together hold 34 readings by Argon's codes and 27 by Astra's; 24 by both coders (22 of them with the same type), 37 by either.

**By source.**
- Pratt, five readings to an arm: the coders code other_mechanism for 3 (Argon) and 4 (Astra) of the plain arm's readings, and for one of the other ten (Astra, a reading of the system arm); the system and middle arms' readings are otherwise inverts, rereads_evidence or challenges_premise. The contrast is between the plain arm and the other two.
- Bechky: as a main type, complements appears only in Astra's codes, 6 of its 7 on the ten readings of chats 49 and 50, all ten of which Argon codes other_mechanism.

**Worth beside type,** on the readings both coders give the same type, by paper:

| Type | Bechky: readings | Bechky: mean worth | Pratt: readings | Pratt: mean worth |
|---|---|---|---|---|
| inverts | 1 | 0 | 3 | 1.67 |
| other_mechanism | 12 | 2.00 | 3 | 1.67 |
| rereads_evidence | 4 | 1.25 | 2 | 0 |
| challenges_premise | 1 | 2.00 | 2 | 0.50 |

In each paper, the readings both coders code rereads_evidence got a lower mean worth than those both code other_mechanism. But four of the eight cells hold one or two readings, and type travels with source: the ten Bechky readings of chats 49 and 50, all other_mechanism by Argon's codes, average 2.40; outside them, the Bechky readings both coders code other_mechanism average 1.625 (8 readings), against 1.25 for rereads_evidence (4), and all 18 average 1.44. Bechky's 28 real readings average 1.79, Pratt's 15 average 1.00. Described, not tested; the PI rated worth on three occasions, knowing different things.

**Checked independently.** Every figure in these notes was recomputed from `relation_results.json`, `relation_key.json` and the coders' brief, `RELATION_CODING.md`, with separate code: all agree.
