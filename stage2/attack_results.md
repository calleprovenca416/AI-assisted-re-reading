# The wager test's attack: results

Written by script on 11 Oct 2026 from the eleven attack replies (GPT 6 Astra, one
Temporary Chat per card, run by the PI) and the cards on which
`record_attack.py` recorded them. Modes A, C, F, G and the record were decided
mechanically before the attack, and every card cleared them. B is import, E is
contradiction. Citations are the fragment ids each verdict gives.

| chat | paper | move | status | B import | E contradiction |
|---|---|---|---|---|---|
| 28 | Pratt | construct_inversion, CP01 | killed | **killed**, F94, F95, F97, F98 | clear |
| 29 | Pratt | construct_inversion, CP02 | killed | **killed**, F97, F103, F16, F62 | clear |
| 30 | Pratt | construct_inversion, CP03 (analyst-drawn pair) | killed | **killed**, F83, F106 | clear |
| 31 | Pratt | counterfactual_ending, ventured claims (read on C56) | killed | **killed**, F123, F43, F44, F45, F72, F90, F91, F92, F98, F125 | clear |
| 32 | Pratt | focalization_shift, current and former distributors | killed | **killed**, F10, F11, F23, F25, F35, F64 | clear |
| 33 | Bechky | construct_inversion, CP01 | killed | **killed**, F98, F101, F102, F142, F143 | clear |
| 34 | Bechky | construct_inversion, CP02 | killed | **killed**, F146, F91, F98, F101, F102, F103, F161 | clear |
| 35 | Bechky | counterfactual_ending, DG02 (read on C19) | survived_attack | clear | clear |
| 36 | Bechky | focalization_shift, forensic biology (DNA) | survived_attack | clear | clear |
| 37 | Pratt | calibration copy x of 31: planted import | killed | **killed**, F123, F43, F44, F45, F72 | clear |
| 38 | Pratt | calibration copy y of 31: planted contradiction | killed | **killed**, F123, F43, F44, F45, F72, F125, F97 | **killed**, F97 |

**The nine cards:** 7 killed, 2 survived; every kill is under B.
**Calibration:** copy x, with a planted import, killed under B on the planted clause,
which its verdict quotes; copy y, with a planted undeclared contradiction, killed under E
on F97 and under B on the planted claim. The original of both (31) was killed under B on
other grounds.
