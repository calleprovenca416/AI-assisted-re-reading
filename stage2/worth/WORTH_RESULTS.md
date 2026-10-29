# Worth beside the markers: the wager test's 29 readings

Written by `score_worth.py` from the PI's worth ratings (stage2/worth/worth_sheet_filled_2.xlsx,
filed unchanged; the PI's first sheet, worth_sheet_filled.xlsx, had
three readings blank), stage2/markers/KEY.json, the four marker
replies in stage2/marker_replies and the system's cards. Arms: system (the generation chats,
which wrote from each paper's record, without the PDF), middle (the reading chats: the same
prompt with the PDF), plain (the plain chats: the PDF and a plain prompt).

Worth is the PI's, on the sheet's scale: 0 not worth pursuing, 1 some interest, 2 worth a
scholar's time, 3 a strong opening. **The PI's rating is declared not blind:** the PI had seen every
reply before the PI rated, and the plain arm's form can be told apart (the markers' packs' blinding
is partial). A reading left without a worth is reported as not rated and is left out of every
mean and test.

**Pratt's marker figures are below the bar:** kappa 0.593, under 0.60; they are
reported by a decision of 11 Oct 2026, made after the result, and weigh less than Bechky's.

**Not rated:** none.

**Rated late:** P12, P14, B06 (plain arm): blank on the PI's first sheet and
rated on the second, after the PI had been told their arm. Each arm's mean is also given
without them.

## 1. Worth by arm

### Pratt

| | system (the generation chats) | middle (the reading chats) | plain (the plain chats) |
|---|---|---|---|
| readings | 5 | 5 | 5 |
| rated | 5 | 5 | 5 |
| mean worth | 0.60 | 1.00 | 1.40 |
| mean worth without the readings rated late | 0.60 | 1.00 | 1.67 |
| rated 0 / 1 / 2 / 3 | 3 / 1 / 1 / 0 | 1 / 3 / 1 / 0 | 1 / 1 / 3 / 0 |
| rated 2 or more | 1 of 5 | 1 of 5 | 3 of 5 |
| sentences per reading, mean | 12.6 | 8.2 | 19.8 |

### Bechky

| | system (the generation chats) | middle (the reading chats) | plain (the plain chats) |
|---|---|---|---|
| readings | 4 | 5 | 5 |
| rated | 4 | 5 | 5 |
| mean worth | 1.75 | 0.60 | 2.00 |
| mean worth without the readings rated late | 1.75 | 0.60 | 2.00 |
| rated 0 / 1 / 2 / 3 | 0 / 1 / 3 / 0 | 3 / 1 / 1 / 0 | 0 / 0 / 5 / 0 |
| rated 2 or more | 3 of 4 | 1 of 5 | 5 of 5 |
| sentences per reading, mean | 16.8 | 7.8 | 17.4 |

### Both papers

| | system (the generation chats) | middle (the reading chats) | plain (the plain chats) |
|---|---|---|---|
| readings | 9 | 10 | 10 |
| rated | 9 | 10 | 10 |
| mean worth | 1.11 | 0.80 | 1.70 |
| mean worth without the readings rated late | 1.11 | 0.80 | 1.86 |
| rated 0 / 1 / 2 / 3 | 3 / 2 / 4 / 0 | 4 / 4 / 2 / 0 | 1 / 1 / 8 / 0 |
| rated 2 or more | 4 of 9 | 2 of 10 | 8 of 10 |
| sentences per reading, mean | 14.4 | 8.0 | 18.6 |

## 2. Worth beside the markers, by arm

Each marker's cell gives Opus 5.5 / GPT 6 Astra. Facts found: the sentences coded R, RI or RA
over those that report (every code but N). Warrant: a U (not printed) or C (contradicted) in the
position of the reading's warrant.

### Pratt (markers below the bar)

| | system (the generation chats) | middle (the reading chats) | plain (the plain chats) |
|---|---|---|---|
| mean worth (rated) | 0.60 | 1.00 | 1.40 |
| facts found | 82% / 58% | 89% / 72% | 87% / 75% |
| contradicted sentences (C) | 6 / 7 | 0 / 0 | 1 / 3 |
| not printed (U) | 0 / 1 | 0 / 3 | 2 / 4 |
| readings with a U or C as warrant | 0 / 0 | 0 / 0 | 0 / 2 |
| rated 2 or more, warrant clear for both markers | 1 of 5 rated | 1 of 5 rated | 2 of 5 rated |
| rated 2 or more, no C for either marker | 1 of 5 rated | 1 of 5 rated | 2 of 5 rated |
| the attack: killed / survived | 5 / 0 | not attacked | not attacked |

### Bechky

| | system (the generation chats) | middle (the reading chats) | plain (the plain chats) |
|---|---|---|---|
| mean worth (rated) | 1.75 | 0.60 | 2.00 |
| facts found | 95% / 87% | 100% / 93% | 98% / 70% |
| contradicted sentences (C) | 2 / 3 | 0 / 1 | 0 / 4 |
| not printed (U) | 0 / 0 | 0 / 1 | 0 / 5 |
| readings with a U or C as warrant | 0 / 0 | 0 / 2 | 0 / 4 |
| rated 2 or more, warrant clear for both markers | 3 of 4 rated | 1 of 5 rated | 1 of 5 rated |
| rated 2 or more, no C for either marker | 2 of 4 rated | 1 of 5 rated | 2 of 5 rated |
| the attack: killed / survived | 2 / 2 | not attacked | not attacked |

### Both papers (Pratt's markers below the bar)

| | system (the generation chats) | middle (the reading chats) | plain (the plain chats) |
|---|---|---|---|
| mean worth (rated) | 1.11 | 0.80 | 1.70 |
| facts found | 89% / 74% | 95% / 81% | 93% / 73% |
| contradicted sentences (C) | 8 / 10 | 0 / 1 | 1 / 7 |
| not printed (U) | 0 / 1 | 0 / 4 | 2 / 9 |
| readings with a U or C as warrant | 0 / 0 | 0 / 2 | 0 / 6 |
| rated 2 or more, warrant clear for both markers | 4 of 9 rated | 2 of 10 rated | 3 of 10 rated |
| rated 2 or more, no C for either marker | 3 of 9 rated | 2 of 10 rated | 4 of 10 rated |
| the attack: killed / survived | 7 / 2 | not attacked | not attacked |

## 3. Reading by reading

Sorted by paper, arm and reading. Found: facts found, R, RI and RA over the sentences that
report. Each marker's cell gives Opus 5.5 / GPT 6 Astra. Warrant: yes if that marker codes a U
or C in the warrant position. A worth marked (late) was given on the PI's second sheet, after the PI
had been told the reading's arm.

### Pratt (markers below the bar)

| reading | arm | move | sentences | worth | the PI's note | found | U | C | warrant | attack |
|---|---|---|---|---|---|---|---|---|---|---|
| P04 | system | construct inversion | 15 | 0 | don’t see any worthwhile opening. | 11/11 / 7/10 | 0 / 0 | 0 / 0 | no / no | killed |
| P09 | system | counterfactual ending | 11 | 2 | Not bad. It's quite interesting proposition; worth investigating further | 6/6 / 6/8 | 0 / 0 | 0 / 0 | no / no | killed |
| P10 | system | construct inversion | 12 | 1 | worth checking against the case; but I don't think it's very likely to create a theoretical opening | 7/11 / 4/9 | 0 / 0 | 4 / 4 | no / no | killed |
| P11 | system | focalization shift | 12 | 0 | not worth exploring | 6/8 / 5/7 | 0 / 1 | 0 / 1 | no / no | killed |
| P13 | system | construct inversion | 13 | 0 | not worth exploring | 7/9 / 3/9 | 0 / 0 | 2 / 2 | no / no | killed |
| P02 | middle | boundary shift | 6 | 1 | worth checking against the case; but I don't think it's very likely to create a theoretical opening | 4/5 / 4/5 | 0 / 0 | 0 / 0 | no / no | not attacked |
| P06 | middle | construct fission | 9 | 1 | worth checking against the case; but I don't think it's very likely to create a theoretical opening | 4/5 / 3/5 | 0 / 0 | 0 / 0 | no / no | not attacked |
| P07 | middle | construct inversion | 7 | 2 | Not bad. It's quite interesting proposition; worth investigating further | 3/4 / 4/5 | 0 / 1 | 0 / 0 | no / no | not attacked |
| P08 | middle | counterfactual ending | 11 | 1 | worth checking against the case; but I don't think it's very likely to create a theoretical opening | 8/8 / 8/10 | 0 / 0 | 0 / 0 | no / no | not attacked |
| P15 | middle | focalization shift | 8 | 0 | not worth exploring | 6/6 / 4/7 | 0 / 2 | 0 / 0 | no / no | not attacked |
| P01 | plain | — | 18 | 1 | worth checking against the case; but I don't think it's very likely to create a theoretical opening | 10/10 / 11/12 | 0 / 1 | 0 / 0 | no / no | not attacked |
| P03 | plain | — | 21 | 2 | I think this is quite interesting. Could be developed further. Sounds consistent with other identity-related research. | 12/15 / 13/17 | 0 / 1 | 0 / 0 | no / yes | not attacked |
| P05 | plain | — | 20 | 2 | Not bad. It's quite interesting proposition; worth investigating further | 11/12 / 12/16 | 0 / 0 | 1 / 1 | no / no | not attacked |
| P12 | plain | — | 21 | 0 (late) | not worth exploring | 10/13 / 9/15 | 1 / 2 | 0 / 2 | no / yes | not attacked |
| P14 | plain | — | 19 | 2 (late) | Not bad. It's quite interesting proposition; worth investigating further | 11/12 / 10/13 | 1 / 0 | 0 / 0 | no / no | not attacked |

### Bechky

| reading | arm | move | sentences | worth | the PI's note | found | U | C | warrant | attack |
|---|---|---|---|---|---|---|---|---|---|---|
| B04 | system | counterfactual ending | 13 | 1 | interesting; but I doubt it's a real opening | 9/10 / 8/10 | 0 / 0 | 1 / 2 | no / no | survived |
| B09 | system | construct inversion | 21 | 2 | worth checking with the paper; something interesting here. | 17/17 / 16/17 | 0 / 0 | 0 / 0 | no / no | killed |
| B10 | system | focalization shift | 15 | 2 | worth checking with the paper; something interesting here. | 11/13 / 9/13 | 0 / 0 | 1 / 1 | no / no | survived |
| B13 | system | construct inversion | 18 | 2 | worth checking with the paper; something interesting here. | 15/15 / 15/15 | 0 / 0 | 0 / 0 | no / no | killed |
| B01 | middle | counterfactual ending | 9 | 0 | not worth investigating | 8/8 / 8/8 | 0 / 0 | 0 / 0 | no / no | not attacked |
| B03 | middle | construct fission | 6 | 1 | worth investigating a bit; doubt it's going to change the incumbent story. | 4/4 / 3/4 | 0 / 0 | 0 / 1 | no / yes | not attacked |
| B08 | middle | construct inversion | 9 | 0 | not worth investigating | 7/7 / 7/7 | 0 / 0 | 0 / 0 | no / no | not attacked |
| B11 | middle | construct inversion | 7 | 0 | not worth investigating | 4/4 / 3/4 | 0 / 1 | 0 / 0 | no / yes | not attacked |
| B14 | middle | construct fission | 8 | 2 | worth checking with the paper; something interesting here. | 4/4 / 4/4 | 0 / 0 | 0 / 0 | no / no | not attacked |
| B02 | plain | — | 17 | 2 | worth checking with the paper; something interesting here. | 13/13 / 9/13 | 0 / 2 | 0 / 0 | no / yes | not attacked |
| B05 | plain | — | 14 | 2 | worth checking with the paper; something interesting here. | 10/10 / 8/11 | 0 / 0 | 0 / 2 | no / yes | not attacked |
| B06 | plain | — | 18 | 2 (late) | worth checking with the paper; something interesting here. | 13/14 / 9/15 | 0 / 1 | 0 / 1 | no / yes | not attacked |
| B07 | plain | — | 18 | 2 | worth checking with the paper; something interesting here. | 12/12 / 10/14 | 0 / 1 | 0 / 0 | no / no | not attacked |
| B12 | plain | — | 20 | 2 | worth checking with the paper; something interesting here. | 14/14 / 13/17 | 0 / 1 | 0 / 1 | no / yes | not attacked |

## 4. Other cuts

### The attack and worth (the system's readings)

- killed: 7 readings, mean worth 1.00; P04 0, P09 2, P10 1, P11 0, P13 0, B09 2, B13 2.
- survived: 2 readings, mean worth 1.50; B04 1, B10 2.

### How far worth goes with facts found, and with length

Spearman's rank correlation over the rated readings; p two-sided, by 20,000 seeded shuffles.
With so few readings, only a large correlation is told apart from chance.

| | Pratt | Bechky | both papers |
|---|---|---|---|
| worth and facts found, Opus 5.5 | +0.08 (p 0.79, n 15) | -0.10 (p 0.64, n 14) | +0.11 (p 0.58, n 29) |
| worth and facts found, GPT 6 Astra | +0.56 (p 0.04, n 15) | -0.39 (p 0.17, n 14) | +0.18 (p 0.34, n 29) |
| worth and sentences in the reading | +0.06 (p 0.85, n 15) | +0.71 (p 0.01, n 14) | +0.41 (p 0.03, n 29) |

### The gap in mean worth between arms

The first arm's mean worth minus the second's, over the rated readings. p two-sided, by every
relabelling of the two arms' readings within each paper (for both papers together, within each
paper at once).

| arms | Pratt | Bechky | both papers |
|---|---|---|---|
| system against middle (the reading chats) | -0.40 (p 0.683) | +1.15 (p 0.087) | +0.31 (p 0.594) |
| system against plain (the plain chats) | -0.80 (p 0.333) | -0.25 (p 0.444) | -0.59 (p 0.122) |
| system against middle and plain together | -0.60 (p 0.334) | +0.45 (p 0.497) | -0.14 (p 0.815) |
| middle (the reading chats) against plain (the plain chats) | -0.40 (p 0.683) | -1.40 (p 0.048) | -0.90 (p 0.036) |

### Worth by move (system and middle; the plain arm has no moves)

| move | system (the generation chats) | middle (the reading chats) |
|---|---|---|
| construct inversion | P04 0, P10 1, P13 0, B09 2, B13 2 | P07 2, B08 0, B11 0 |
| counterfactual ending | P09 2, B04 1 | P08 1, B01 0 |
| focalization shift | P11 0, B10 2 | P15 0 |
| construct fission | — | P06 1, B03 1, B14 2 |
| boundary shift | — | P02 1 |
