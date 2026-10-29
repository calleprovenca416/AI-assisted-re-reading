# The map test (T39): results

Every measure of `MAP_TEST_PLAN.md`'s part F, described, not tested, as `score_map_test.py` wrote them (its sha256 opens 190ab734). Map A is the Opus map, map B the GPT 6 map; the first coder is T37's Google coder, the second its OpenAI coder.

## Bechky

### F1, the maps' agreement, on the maps as built

- **Listed pairs (80):** an edge in both 25, in A only 2, in B only 8, in neither 45; raw agreement 0.875, kappa 0.735, positive agreement 0.833.
- **The type, on the 25 pairs both call edges:** agree 21, raw 0.84, kappa 0.574.

| map A \ map B | evidential | mechanistic | comparative | significance |
|---|---|---|---|---|
| evidential | 18 | 0 | 3 | 0 |
| mechanistic | 0 | 3 | 0 | 1 |
| comparative | 0 | 0 | 0 | 0 |
| significance | 0 | 0 | 0 | 0 |

- **The strength, on the 25 pairs both call edges:** agree 24, raw 0.96, kappa 0.884.

| map A \ map B | necessary | contributing |
|---|---|---|
| necessary | 5 | 1 |
| contributing | 0 | 19 |

- **The registries,** over the 780 pairs of the 40 construct names: together in A 3, in B 6, in both 3; positive agreement 0.667, raw 0.996.
- **The factors:** A 3, B 3, paired by their claims 3; A's unpaired none, B's none; unit outcomes, agree 4 of 4 (1.0); unit values, agree 12 of 12 (1.0); controls, agree 6 of 6 (1.0).
- **Further edges:** A 6, B 5, both 4 (C05 on C02, C21 on C04, C21 on C05, C21 on C08), of which alike in type and strength 2.
- **Edges among the candidates and the sampled pairs:** A 25 of 55 (0.455) and 2 of 25 (0.08); B 30 of 55 (0.545) and 3 of 25 (0.12).

### F2, the PI's settling

- **23 items:** constructs 3; further-one 3; further-type 2; pair-edge 10; pair-type 5.
- **The PI's choices:** constructs: B 3; further-one: A 3; further-type: A 1, B 1; pair-edge: A 10; pair-type: A 5; in all A 19, B 4.

### F3, the placement

- **Elements placed:** 279, by kind absence 1; claim 142; construct 33; contrast pair 10; declared gap 5; edge 49; factor 19; unit 20; readings with something off the map 30 of 30; with evidence 30; the openings' ties, by kind absence 1; claim 38; construct 1; contrast pair 6; declared gap 1; off-map 12; unit 1.
- **Planted R02** (written to C04, complements): placed on C04, C13, C16, C17, C18, X2, K31, U2, U3, U4; its claim among them.
- **Planted R13** (written to C05, inverts): placed on C05, C20, C16, C17, C18, C03, E14, E15, E16, X3, K22; its claim among them.

| reading | elements | evidence | off the map | ties |
|---|---|---|---|---|
| R01 | C18, C05, C04, C17, CP02, E12, E16, X2, X3, U3, U4 | F102, F109, F119, F123, F124, F125 | yes | contrast pair, claim |
| R02 | C04, C13, C16, C17, C18, X2, K31, U2, U3, U4 | F65, F66, F67, F98, F101, F102, F106, F109, F123, F124, F125, F157 | yes | claim, off-map |
| R03 | C05, C16, C17, C18, C15, C21, E14, E15, E16, X3, K22, K27, CP02 | F10, F26, F54, F85, F98, F102, F109, F118, F119, F122, F123, F124, F125 | yes | claim, off-map |
| R04 | C10, C20, C18, C05, E24, E27, K19, K22 | F06, F57, F113, F114, F128 | yes | claim, claim |
| R05 | CP02, C18, C17, C05, C04, E15, E16, X2, X3 | F90, F91, F94, F95, F96, F98, F100, F101, F102, F103, F109, F111, F120, F121, F122, F123, F124, F125, F126, F127, F128, F129, F149, F150, F166 | yes | contrast pair, claim |
| R06 | C16, C14, C13, C03, C04, E06, E10, U2, CP01 | F47, F48, F50, F51, F65, F66, F67, F68, F71, F73, F80, F100, F122, F124, F125 | yes | claim, contrast pair |
| R07 | C03, CP01, C17, C16, E07, X1 | F35, F66, F78, F98, F101, F102, F142, F143, F161 | yes | contrast pair, claim |
| R08 | C04, C13, C14, C05, C16, U1, K03, K15 | F28, F43, F45, F46, F48, F49, F50, F51, F68, F69, F92, F110, F145, F146, F147, F148 | yes | claim, unit |
| R09 | C05, C01, C03, C16, C17, C18, K17, K21, U2, U3, U4 | F65, F66, F67, F68, F71, F85, F98, F102, F103, F121, F122, F125, F126, F128, F129 | yes | claim, off-map |
| R10 | C20, C10, C18, C17, C05, E24, E26, E27, K22 | F06, F95, F113, F114, F128 | yes | claim, claim |
| R11 | C10, C20, C05, C17, C18, C19, DG02, E24, K14, K17, K22 | F06, F57, F95, F113, F114, F128, F165 | yes | claim, off-map |
| R12 | C02, C13, C17, C18, C01, E01, E17, E20, E21, K06 | F60, F82, F83, F85, F99, F100, F102, F105, F106, F122, F123, F127, F128, F129 | yes | claim, claim |
| R13 | C05, C20, C16, C17, C18, C03, E14, E15, E16, X3, K22 | F80, F98, F102, F103, F122, F123, F126, F127, F128, F163, F164, F167 | yes | claim, claim |
| R14 | C10, C20, C05, C17, C18, CP02, E24, K19, K22 | F06, F57, F95, F113, F114 | yes | contrast pair, claim |
| R15 | C17, C01, C02, C03, E04, E07, X1, U3 | F88, F89, F90, F98, F102 | yes | claim, claim |
| R16 | C14, C05, C13, C16, C17, C18, C21, K15, K26 | F47, F48, F49, F50, F51, F65, F66, F67, F68, F69, F122, F124, F125 | yes | claim, off-map |
| R17 | C05, C03, C04, C16, C17, C18, CP01, CP02, E14, E15, E16, DG01, DG03, A01, X1, X3 | F80, F84, F88, F90, F104, F123, F129, F164 | yes | claim, absence |
| R18 | C05, C03, C16, C17, C18, E14, E16, X1, X3, DG03 | F67, F80, F84, F98, F99, F129 | yes | claim, claim |
| R19 | C19, DG02, C01, C17, C02, C15, E04, E07, U3, K05, K14 | F41, F55, F57, F60, F62, F82, F89, F90, F98, F99, F101, F102, F122, F131, F151, F152, F153, F157, F165 | yes | claim, declared gap |
| R20 | C18, C04, C05, E12, E16, X2, X3, U4, CP02 | F109, F119, F123, F124, F125 | yes | claim, claim |
| R21 | C14, C16, C18, C13, C05, K15, K26, U2 | F47, F48, F49, F50, F65, F66, F67, F68, F69, F122, F124, F125 | yes | claim, off-map |
| R22 | C17, C02, C01, E04, C03, E07, K06, U3 | F34, F89, F90, F98, F99, F102, F103, F161 | yes | claim, claim |
| R23 | C17, C02, C01, E04, C03, E07, K06, U3 | F89, F90, F98, F99, F102, F161 | yes | construct, claim |
| R24 | C18, C21, E33, C03, C02, C05, K23, K11 | F106, F110, F121, F123 | yes | claim, off-map |
| R25 | C18, C04, X2, E12, C05, E16, C03, E08, K11, U4 | F62, F109, F111, F118, F119, F120, F122, F123, F124, F125, F139, F141, F150, F162 | yes | claim, off-map |
| R26 | C18, U4, C05, E16, C03, K11, X1, E08 | F30, F62, F109, F122, F123, F124, F125, F129, F139, F141, F153, F162 | yes | claim, off-map |
| R27 | C17, C03, C16, CP01, X1, E07 | F98, F101, F102, F143, F161 | yes | contrast pair, off-map |
| R28 | C16, C18, C14, C13, C04, C05, K17, U2, U4 | F47, F65, F66, F67, F68, F69, F71, F110, F122, F124, F125, F151, F153 | yes | claim, off-map |
| R29 | C21, C05, C16, C18, C17, C15, E29, K23, K29 | F54, F55, F57, F58, F74, F103, F113, F114, F127, F149 | yes | claim, off-map |
| R30 | C17, C01, E04, C03, X1, E07, K21 | F98, F99, F102 | yes | claim, claim |

### F4, the typed effects

- **Labels on core claims, under the first coder's codes:** contested 36; unsupported 36; weakened 103; restated 2; idle 2; readings with a label on a core claim besides contested 29.
- **Labels on core claims, under the second coder's codes:** contested 23; unsupported 29; weakened 81; restated 1; idle 2; readings with a label on a core claim besides contested 22.

| reading | worth | first coder: main | labels | second coder: main | labels |
|---|---|---|---|---|---|
| R01 | 3 | C18 other_mechanism | C03 weakened, C04 contested, C05 contested, C13 weakened, C20 weakened, C21 weakened | C18 other_mechanism | C01 unsupported, C03 unsupported, C04 unsupported, C05 contested, C13 weakened, C20 weakened, C21 weakened |
| R02 (planted) | none | C04 challenges_premise | C03 weakened, C04 contested, C05 weakened, C13 weakened, C20 weakened, C21 weakened | C04 challenges_premise | C03 weakened, C04 contested, C05 weakened, C13 weakened, C20 weakened, C21 weakened |
| R03 | 2 | C05 other_mechanism | C01 unsupported, C03 unsupported, C04 unsupported, C05 contested, C13 weakened, C20 weakened, C21 weakened | C05 other_mechanism | C01 unsupported, C03 unsupported, C04 unsupported, C05 contested, C13 weakened, C20 weakened, C21 weakened |
| R04 | 2 | C10 other_mechanism | C03 weakened, C04 unsupported, C05 weakened, C13 weakened, C20 contested, C21 weakened | C10 complements | none |
| R05 | 2 | C18 other_mechanism | C01 unsupported, C03 unsupported, C04 unsupported, C05 contested, C13 weakened, C20 weakened, C21 weakened | C05 other_mechanism | C01 unsupported, C03 unsupported, C04 unsupported, C05 contested, C13 weakened, C20 weakened, C21 weakened |
| R06 | 2 | C16 rereads_evidence | C03 weakened, C04 weakened, C05 weakened, C13 weakened, C20 weakened, C21 weakened | C16 rereads_evidence | C03 weakened, C04 weakened, C05 weakened, C13 weakened, C20 weakened, C21 weakened |
| R07 | 2 | C03 other_mechanism | C01 unsupported, C03 contested, C04 weakened, C05 weakened, C13 weakened, C20 weakened, C21 weakened | C03 other_mechanism | C03 contested, C04 weakened, C05 weakened, C13 weakened, C20 weakened, C21 weakened |
| R08 | 2 | C04 challenges_premise | C04 contested, C05 contested, C20 idle, C21 restated | C04 challenges_premise | C04 contested, C20 idle, C21 restated |
| R09 | 2 | C05 challenges_premise | C01 unsupported, C03 unsupported, C04 weakened, C05 contested, C13 weakened, C20 weakened, C21 weakened | C16 rereads_evidence | C03 weakened, C04 weakened, C05 weakened, C13 weakened, C20 weakened, C21 weakened |
| R10 | 0 | C20 inverts | C03 weakened, C04 unsupported, C05 weakened, C13 weakened, C20 contested, C21 weakened | C10 inverts | C20 contested |
| R11 | 1 | C10 other_mechanism | C20 contested | C10 complements | none |
| R12 | 1 | C02 rereads_evidence | C01 unsupported, C03 unsupported, C04 unsupported, C05 unsupported, C13 contested, C20 weakened, C21 weakened | C02 rereads_evidence | C01 unsupported, C03 unsupported, C04 unsupported, C05 unsupported, C13 unsupported, C20 weakened, C21 weakened |
| R13 (planted) | none | C05 inverts | C01 unsupported, C03 unsupported, C04 unsupported, C05 contested, C13 weakened, C20 weakened, C21 weakened | C05 inverts | C01 unsupported, C03 unsupported, C04 unsupported, C05 contested, C13 weakened, C20 weakened, C21 weakened |
| R14 | 2 | C10 other_mechanism | C05 contested, C20 contested, C21 restated | C10 complements | none |
| R15 | 2 | C17 other_mechanism | C01 contested, C03 unsupported, C04 weakened, C05 weakened, C13 weakened, C20 weakened, C21 weakened | C17 complements | none |
| R16 | 2 | C05 other_mechanism | C03 weakened, C04 unsupported, C05 contested, C13 weakened, C20 weakened, C21 weakened | C14 complements | none |
| R17 | 2 | C05 other_mechanism | C03 weakened, C04 weakened, C05 contested, C13 weakened, C20 weakened, C21 weakened | C05 other_mechanism | C03 weakened, C04 weakened, C05 contested, C13 weakened, C20 weakened, C21 weakened |
| R18 | 3 | C05 other_mechanism | C03 weakened, C04 unsupported, C05 contested, C13 weakened, C20 weakened, C21 weakened | C05 other_mechanism | C03 weakened, C04 weakened, C05 contested, C13 weakened, C20 weakened, C21 weakened |
| R19 | 1 | C19 challenges_premise | C01 contested, C03 unsupported, C04 weakened, C05 weakened, C13 weakened, C20 weakened, C21 weakened | C19 rereads_evidence | C01 contested, C03 unsupported, C04 weakened, C05 weakened, C13 weakened, C20 weakened, C21 weakened |
| R20 | 3 | C18 other_mechanism | C03 weakened, C04 contested, C05 contested, C13 weakened, C20 weakened, C21 weakened | C18 other_mechanism | C03 weakened, C04 contested, C05 contested, C13 weakened, C20 weakened, C21 weakened |
| R21 | 3 | C05 other_mechanism | C03 weakened, C04 weakened, C05 contested, C13 weakened, C20 weakened, C21 weakened | C14 complements | C03 weakened, C04 weakened, C05 weakened, C13 weakened, C20 weakened, C21 weakened |
| R22 | 2 | C17 other_mechanism | C01 contested, C03 unsupported, C04 unsupported, C05 unsupported, C13 unsupported, C20 weakened, C21 weakened | C17 other_mechanism | C01 contested, C03 unsupported, C04 unsupported, C05 unsupported, C13 unsupported, C20 weakened, C21 weakened |
| R23 | 2 | C17 other_mechanism | C01 contested, C03 unsupported, C04 unsupported, C05 unsupported, C13 unsupported, C20 weakened, C21 weakened | C17 other_mechanism | C01 contested, C03 unsupported, C04 unsupported, C05 unsupported, C13 unsupported, C20 weakened, C21 weakened |
| R24 | 2 | C18 other_mechanism | C03 weakened, C04 unsupported, C05 weakened, C13 weakened, C20 weakened, C21 contested | C21 other_mechanism | C03 weakened, C04 unsupported, C05 weakened, C13 weakened, C20 weakened, C21 contested |
| R25 | 1 | C18 other_mechanism | C03 contested, C04 unsupported, C05 contested, C13 weakened, C20 weakened, C21 weakened | C18 other_mechanism | C03 contested, C04 contested, C05 weakened, C13 weakened, C20 weakened, C21 weakened |
| R26 | 0 | C18 rereads_evidence | C03 contested, C04 unsupported, C05 contested, C13 weakened, C20 weakened, C21 weakened | C18 rereads_evidence | C03 contested, C04 unsupported, C05 contested, C13 weakened, C20 weakened, C21 weakened |
| R27 | 0 | C17 other_mechanism | C01 unsupported, C03 contested, C04 weakened, C05 weakened, C13 weakened, C20 weakened, C21 weakened | C03 other_mechanism | C03 contested |
| R28 | 2 | C16 rereads_evidence | C03 weakened, C04 unsupported, C05 contested, C13 weakened, C20 weakened, C21 weakened | C16 rereads_evidence | C03 weakened, C04 unsupported, C05 weakened, C13 weakened, C20 weakened, C21 weakened |
| R29 | 2 | C21 inverts | C05 contested, C20 idle, C21 contested | C21 other_mechanism | C05 contested, C20 idle, C21 contested |
| R30 | 2 | C17 other_mechanism | C01 contested, C03 unsupported, C04 weakened, C05 weakened, C13 weakened, C20 weakened, C21 weakened | C17 complements | none |

### F5, the openings' check

- **Faithful** 27, **not** 3: not faithful R07, R21, R28.

## Pratt

### F1, the maps' agreement, on the maps as built

- **Listed pairs (92):** an edge in both 22, in A only 3, in B only 15, in neither 52; raw agreement 0.804, kappa 0.57, positive agreement 0.71.
- **The type, on the 22 pairs both call edges:** agree 18, raw 0.818, kappa 0.651.

| map A \ map B | evidential | mechanistic | comparative | significance |
|---|---|---|---|---|
| evidential | 11 | 3 | 0 | 0 |
| mechanistic | 1 | 6 | 0 | 0 |
| comparative | 0 | 0 | 0 | 0 |
| significance | 0 | 0 | 0 | 1 |

- **The strength, on the 22 pairs both call edges:** agree 17, raw 0.773, kappa 0.321.

| map A \ map B | necessary | contributing |
|---|---|---|
| necessary | 2 | 1 |
| contributing | 4 | 15 |

- **The registries,** over the 4186 pairs of the 92 construct names: together in A 6, in B 6, in both 6; positive agreement 1.0, raw 1.0.
- **The factors:** A 3, B 3, paired by their claims 2; A's unpaired C27, B's C13; controls, agree 4 of 6 (0.667).
- **Further edges:** A 10, B 10, both 6 (C02 on C12, C02 on C20, C11 on C12, C13 on C17, C28 on C12, C29 on C12), of which alike in type and strength 1.
- **Edges among the candidates and the sampled pairs:** A 18 of 62 (0.29) and 7 of 30 (0.233); B 30 of 62 (0.484) and 7 of 30 (0.233).

### F2, the PI's settling

- **42 items:** contrast 2; factor-one 2; further-one 8; further-type 5; pair-edge 18; pair-type 7.
- **The PI's choices:** contrast: A 2; factor-one: A 2; further-one: A 4, B 2, own 2; further-type: A 1, B 4; pair-edge: A 17, B 1; pair-type: A 4, B 3; in all A 30, B 10, own 2.

### F3, the placement

- **Elements placed:** 140, by kind absence 3; claim 81; construct 14; contrast pair 5; declared gap 3; edge 22; factor 12; readings with something off the map 17 of 17; with evidence 17; the openings' ties, by kind absence 2; claim 17; contrast pair 3; declared gap 1; factor 2; off-map 9.
- **Planted R05** (written to C02, other_mechanism): placed on C02, C11, C12, E12, C24, C18, C05, C09, C26, C28, K06; its claim among them.
- **Planted R11** (written to C13, restates): placed on C12, C13, C15, C17, C20, E18, E21, E22, X1; its claim among them.

| reading | elements | evidence | off the map | ties |
|---|---|---|---|---|
| R01 | C07, C01, E03, C03, C27, C18, C38, C55, C34, K35, DG03 | F45, F46, F47, F70, F74, F88, F90, F107, F110, F123 | yes | claim, declared gap |
| R02 | CP03, C23, C29, C36, X3, K01, K24 | F79, F83, F84, F85, F104, F106 | yes | contrast pair, claim |
| R03 | C56, C27, C03, C07, E02, E09, C17, C22, DG03, K83 | F22, F24, F43, F44, F45, F72, F90, F91, F92, F98, F110, F123, F124 | yes | claim, off-map |
| R04 | C08, C28, E28, E30, C11, X1, K61 | F20, F37, F94, F98, F99 | yes | claim, claim |
| R05 | C02, C11, C12, E12, C24, C18, C05, C09, C26, C28, K06 | F11, F22, F23, F25, F48, F71, F74, F76, F77, F86, F98, F112 | yes | claim, claim |
| R06 | C29, E32, C22, X3, K01 | F74, F101, F103, F105, F107 | yes | claim, factor |
| R07 | C09, A01, K28, C36 | F10, F11, F22, F23, F35 | yes | claim, absence |
| R08 | CP02, C20, C21, E23, C29, X2 | F16, F62, F97, F103 | yes | contrast pair, claim |
| R09 | C13, C14, E20, C01, C21, K18 | F36, F112, F113, F114, F115, F116, F117, F118, F119 | yes | claim, claim |
| R10 | C12, C13, C16, C27, C30, E18, X1, CP01, DG01 | F32, F40, F57, F59, F60, F91, F102, F109 | yes | claim, off-map |
| R11 | C12, C13, C15, C17, C20, E18, E21, E22, X1 | F28, F30, F31, F32, F40, F41, F42, F43, F44, F45, F48, F49, F52 | yes | off-map, off-map |
| R12 | C07, C20, C22, C28, C29, E24, E32, X3 | F67, F68, F72, F74, F75, F76, F99, F104, F105, F106, F107 | yes | claim, off-map |
| R13 | C09, K28, A01, C28, C58 | F11, F16, F22, F23, F98, F99, F118 | yes | claim, absence |
| R14 | C12, C13, C15, C27, K67, X1, E18, E21, CP01 | F32, F35, F39, F90, F91, F94, F102 | yes | factor, off-map |
| R15 | C28, C27, CP01, X1, X2, C57, C58, E28, E29, E30 | F91, F94, F95, F96, F97, F98, F99, F125 | yes | contrast pair, off-map |
| R16 | C01, C07, C13, C14, C21, C57, C29, K73, K74, X1, X2, E18, E23 | F35, F36, F38, F62, F80, F93, F97, F112, F114, F115, F117, F119 | yes | claim, off-map |
| R17 | C09, A01, C07, K35, C11, C02, C20, C28, C29, C56 | F11, F23, F24, F25, F63, F98, F99, F123 | yes | claim, off-map |

### F4, the typed effects

- **Labels on core claims, under the first coder's codes:** contested 21; unsupported 54; weakened 13; restated 0; idle 6; readings with a label on a core claim besides contested 15.
- **Labels on core claims, under the second coder's codes:** contested 21; unsupported 50; weakened 13; restated 0; idle 4; readings with a label on a core claim besides contested 14.

| reading | worth | first coder: main | labels | second coder: main | labels |
|---|---|---|---|---|---|
| R01 | 2 | C07 other_mechanism | C01 weakened | C07 other_mechanism | C01 weakened |
| R02 | 0 | C23 rereads_evidence | C01 weakened, C20 weakened, C29 contested | C29 rereads_evidence | C01 weakened, C29 contested |
| R03 | 2 | C56 inverts | C01 weakened, C12 weakened, C27 contested, C34 weakened | C56 inverts | C01 weakened, C12 weakened, C27 contested, C34 weakened |
| R04 | 1 | C28 rereads_evidence | C01 unsupported, C02 unsupported, C11 unsupported, C20 unsupported, C28 contested, C29 unsupported, C34 idle | C08 challenges_premise | C01 unsupported, C02 unsupported, C11 unsupported, C20 unsupported, C28 contested, C29 unsupported, C34 idle |
| R05 (planted) | none | C02 other_mechanism | C01 unsupported, C02 contested, C11 unsupported, C12 contested, C20 unsupported, C27 unsupported, C28 unsupported, C29 unsupported, C34 weakened | C02 other_mechanism | C01 weakened, C02 contested, C11 contested |
| R06 | 2 | C29 inverts | C01 weakened, C29 contested | C29 inverts | C01 weakened, C29 contested |
| R07 | 0 | C09 challenges_premise | none | C09 challenges_premise | none |
| R08 | 0 | C20 inverts | C01 unsupported, C02 unsupported, C11 unsupported, C20 contested, C28 unsupported, C29 contested, C34 idle | C20 rereads_evidence | C01 unsupported, C02 unsupported, C11 unsupported, C20 contested, C28 unsupported, C29 unsupported, C34 idle |
| R09 | 0 | C13 rereads_evidence | C01 contested, C02 unsupported, C11 unsupported, C12 unsupported, C13 contested, C20 unsupported, C27 unsupported, C28 unsupported, C29 unsupported, C34 weakened | C13 rereads_evidence | C01 contested, C02 unsupported, C11 unsupported, C12 unsupported, C13 contested, C20 unsupported, C27 unsupported, C28 unsupported, C29 unsupported, C34 weakened |
| R10 | 2 | C12 other_mechanism | C01 unsupported, C02 unsupported, C11 unsupported, C12 contested, C20 unsupported, C27 contested, C28 unsupported, C29 unsupported, C34 weakened | C12 other_mechanism | C01 unsupported, C02 unsupported, C11 unsupported, C12 contested, C20 unsupported, C27 contested, C28 unsupported, C29 unsupported, C34 weakened |
| R11 (planted) | none | C13 restates | none | C13 restates | none |
| R12 | 1 | C20 other_mechanism | C01 unsupported, C02 unsupported, C11 unsupported, C20 contested, C28 unsupported, C29 contested, C34 idle | C07 other_mechanism | C01 unsupported, C02 unsupported, C11 unsupported, C20 contested, C28 unsupported, C29 unsupported, C34 idle |
| R13 | 1 | C09 inverts | C01 unsupported, C02 unsupported, C11 unsupported, C20 unsupported, C28 contested, C29 unsupported, C34 idle | C09 inverts | none |
| R14 | 1 | C27 challenges_premise | C01 unsupported, C02 unsupported, C11 unsupported, C12 contested, C13 unsupported, C20 unsupported, C27 contested, C28 unsupported, C29 unsupported, C34 weakened | C12 challenges_premise | C01 unsupported, C02 unsupported, C11 unsupported, C12 contested, C13 contested, C20 unsupported, C27 contested, C28 unsupported, C29 unsupported, C34 weakened |
| R15 | 1 | C28 rereads_evidence | C01 unsupported, C02 unsupported, C11 unsupported, C12 weakened, C20 unsupported, C27 contested, C28 contested, C29 unsupported, C34 weakened | C28 other_mechanism | C01 unsupported, C02 unsupported, C11 unsupported, C12 weakened, C20 unsupported, C27 contested, C28 contested, C29 unsupported, C34 weakened |
| R16 | 2 | C07 challenges_premise | C01 contested, C34 idle | C01 other_mechanism | C01 contested, C02 unsupported, C11 unsupported, C12 unsupported, C13 contested, C20 unsupported, C27 unsupported, C28 unsupported, C29 unsupported, C34 weakened |
| R17 | 0 | C09 rereads_evidence | C01 unsupported, C02 unsupported, C11 unsupported, C20 unsupported, C28 contested, C29 unsupported, C34 idle | C09 inverts | C01 unsupported, C02 unsupported, C11 contested, C20 unsupported, C28 contested, C29 unsupported, C34 idle |

### F5, the openings' check

- **Faithful** 13, **not** 4: not faithful R03, R04, R07, R08.

## F6, the PI's comparison

- **Which account tells you more about what the reading does to the paper's argument?** T37 0; map 12; the same 0; neither 0; unanswered 0 (Bechky: T37 0, map 6, the same 0, neither 0, unanswered 0; Pratt: T37 0, map 6, the same 0, neither 0, unanswered 0).
- **Which account could another reader check more readily against the paper?** T37 0; map 12; the same 0; neither 0; unanswered 0 (Bechky: T37 0, map 6, the same 0, neither 0, unanswered 0; Pratt: T37 0, map 6, the same 0, neither 0, unanswered 0).

| tab | question 1 | question 2 |
|---|---|---|
| Bechky R05 | map | map |
| Bechky R07 | map | map |
| Bechky R16 | map | map |
| Bechky R22 | map | map |
| Bechky R27 | map | map |
| Bechky R29 | map | map |
| Pratt R01 | map | map |
| Pratt R02 | map | map |
| Pratt R03 | map | map |
| Pratt R08 | map | map |
| Pratt R09 | map | map |
| Pratt R14 | map | map |

The PI's notes:

- **Bechky R05:** Account 2 is most helpful, although it is very long. A quick check reveals that it is longer by approx, 1000 characters than the reading itself
- **Bechky R07:** Account 2 is most helpful, although it is very long. A quick check reveals that it is longer by approx, 1000 characters than the reading itself
- **Bechky R16:** Account 2 is most helpful, although it is very long. A quick check reveals that it is longer by approx, 1000 characters than the reading itself
- **Bechky R22:** Account 1 is most helpful, although it is very long
- **Bechky R27:** Account 1 is most helpful, although it is very long
- **Bechky R29:** Account 2 is most helpful, although it is very long
- **Pratt R01:** Account 2 is most helpful, although it is very long
- **Pratt R02:** Account 1 is most helpful, although it is very long
- **Pratt R03:** Account 1 is most helpful, although it is very long
- **Pratt R08:** Account 1 is most helpful, although it is very long
- **Pratt R09:** Account 1 is most helpful, although it is very long
- **Pratt R14:** Account 2 is most helpful, although it is very long

## F7, the cost

- **round 1, the maps (chats 73 to 76):** chats 73 10, 74 10, 75 10, 76 10 minutes.
- **settling (both papers together):** the PI's minutes at least 120.
- **round 2, the placement (chats 77 and 78; then 81 and 82 for the readings left missing):** chats 77 none, 78 none, 81 7, 82 7 minutes.
- **round 2, the openings' check (chats 79 and 80):** chats 79 5, 80 3 minutes.
- **the PI's comparison sheet:** the PI's minutes 30.
- **The PI's comparison sheet's cells:** start none, end none, minutes none.

## The inputs

- `map_closure_bechky.json`: 7ff976788af4392a…
- `map_closure_pratt.json`: dde21e59c1423aa3…
- `map_comparison_answers.json`: 88120f289b7ba2a1…
- `map_comparison_key.json`: a7eca76c5501ba6a…
- `map_key.json`: 81c71b6cdb340edf…
- `map_openings_key.json`: 2e3f6bc95e22e93c…
- `map_round2_key.json`: 16203667c98851db…
- `map_settle_key_bechky.json`: 80b49e0bfef16306…
- `map_settle_key_pratt.json`: 0cccf8ab9c51557a…
- `map_settled_bechky.json`: 01b7fc1b3045c294…
- `map_settled_pratt.json`: 323c704a457c2b86…
- `map_times.json`: f6ea17875239f238…
- `relation_key.json`: b8598261afbe915c…
- `relation_results.json`: 5dff925eb5d23484…
- `reply_73_bechky_map_opus.json`: 8ffdfac4bc7e6a25…
- `reply_74_bechky_map_gpt6.json`: b0342c8102fe50fb…
- `reply_75_pratt_map_opus.json`: dc4400bad9a87827…
- `reply_76_pratt_map_gpt6.json`: 6fe55f7d4ebf28f4…
- `reply_77_bechky_place_argon.json`: 099915f0e41be3c0…
- `reply_78_pratt_place_argon.json`: 3188febbc4a9923c…
- `reply_79_bechky_openings_gpt6.json`: 9705b20d8620c2af…
- `reply_80_pratt_openings_gpt6.json`: adbcf240ecfed909…
