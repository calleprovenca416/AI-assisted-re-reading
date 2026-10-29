# pratt_2000: agreement between the two codings

Pratt, M. G. 2000. The good, the bad, and the ambivalent: Managing identification among Amway distributors. Administrative Science Quarterly, 45(3): 456–493.

Written by `agreement.py --paper` from the files in the table below, and written whole again whenever a stage returns. It is not edited by hand: the same files, and the same line on who the coders are, give the same log. It carries no date.

- **Coder 1** is the extraction: the corpus, and the extraction's sidecar for voice and gloss relation. **Coder 2** is the second coding: the returned workbooks.
- **Who they are:** Model against model. Coder 1: the extraction, ChatGPT 5.6 in a Temporary Chat (27 Sep), with the additions of a coverage chat that named itself GPT-6 (9 Oct), which the second count leaves out. Coder 2: Opus 5.5 at Extra, one incognito claude.ai chat per stage.
- Every figure is **per field and never pooled.** Each is computed from the files as they stand, with no notion of a discussion or a reconciliation: nothing here is merged into the corpus, and no figure changes with what is agreed later. That the coding came back before any disagreement was discussed is the protocol's to ensure (`SECOND_CODER.md`), and the script cannot know it.
- **Kappa** is withheld for a field with fewer than 10 comparable judgements, by count only, and is undefined when both coders use one and the same code throughout. Carlile's logs also withheld it for three named fields at any size; on the cold papers that part of the rule was dropped before any sheet came back (7 Oct 2026).
- **A kappa that is given comes with a 95% interval:** 2,000 resamples of the rows with replacement (seed 20261007), and the 2.5th and 97.5th percentiles of their kappas. A resample in which both coders use one code throughout has no kappa and is left out; where that happens, the figure says how many resamples gave one. Two cautions. The ends move with the seed, and more where a field has few rows: on made-up tables, by about a hundredth at some hundreds of rows, by a few hundredths at about fifty, and by as much as 0.14 at ten to fifteen. And rows are resampled one by one, though links cluster by claim and by fragment, so the interval for direction is likely too narrow.
- **By reading** marks a call that a reader made: whether two outcome wordings name the same thing, and whether two asserted directions push the printed outcome the same way. The script counts the calls. Where a call says that coder 2's wording means `none`, it also gives Stage A's figure a second time, with that call applied. The calls were made by: a reader other than the two coders, on 9 Oct 2026: the calls on the outcome wordings, from the two outcome wordings, read beside the claim's statement, coder 1's asserted direction and coder 2's reason; the calls on the sign, from the two directions, read beside the printed outcome and coder 2's reason.
- The corpus has 125 fragments, 60 claims and 452 links. 56 of the claims are directional: they carry both an outcome and an asserted direction.

| what | file | sha256 opens |
|---|---|---|
| coder 1: the corpus | `pratt_2000_v1.json` | a4810cc03d9a4392 |
| coder 1: the sidecar | `pratt_2000_v1_voice_gloss.json` | 7e26bffb2e5cc8cd |
| the pack's key (builder version 1.3, 7 Oct 2026) | `pratt_2000_pack_key.json` | 1d28c84d498dca17 |
| coder 2: Stage A | `returned_pratt_2000_STAGE_A_coder2.xlsx` | 250dcce2ca58504f |
| Stage A as it came, read in from a text | `reply_pratt_2000_STAGE_A.txt` | 6d6d82851d91dbaf |
| Stage A: the digest of its coding tabs (for `judged_on`) | — | c2bd310392bc1d26 |
| coder 2: Stage A2 | `returned_pratt_2000_STAGE_A2_coder2.xlsx` | 3699be60bcdad0eb |
| Stage A2 as it came, read in from a text | `reply_pratt_2000_STAGE_A2.txt` | 0cd13daf225215ec |
| Stage A2: the digest of its coding tabs (for `judged_on`) | — | e81684486438e24e |
| coder 2: Stage V | `returned_pratt_2000_STAGE_V_coder2.xlsx` | 871734aa5e98ce65 |
| Stage V as it came, read in from a text | `reply_pratt_2000_STAGE_V.txt` | 8d98ff0e11c7762f |
| Stage V: the digest of its coding tabs (for `judged_on`) | — | 190ef6144809b129 |
| coder 2: Stage B | `returned_pratt_2000_STAGE_B_coder2.xlsx` | 9f268d85fc7aa10d |
| Stage B as it came, read in from a text | `reply_pratt_2000_STAGE_B.txt` | 5145367ef3037dad |
| Stage B: the digest of its coding tabs (for `judged_on`) | — | 60818e428872cb3c |
| the readings | `pratt_2000_readings.json` | 9a87a1210105d3b3 |
| the `against` check's results | `against_check_results.json` | cdb54145104e9308 |
| written by | `agreement.py` | 8f2e14619558395f |

## Stage A: the outcome of every claim (section 0)

**Directional or not:** n = 60; raw agreement 0.883 (53 of 60); kappa 0.483 (95% interval 0.13 to 0.78).

| coder 1 in rows, coder 2 in columns | `directional` | `none` |
|---|---|---|
| `directional` | 49 | 7 |
| `none` | 0 | 4 |

**One coder names an outcome and the other writes `none`: 7 claims.**

Where coder 2 alone names an outcome, a reader may call the wording `coder 2 means none`. No other call applies there, because there are no two wordings to compare.

| claim | coder 1 | coder 2 | coder 2's reason | by reading | note |
|---|---|---|---|---|---|
| C06 | identification type | none | A correspondence used to tell identification states apart: valence and state are matched, not one affecting the other, and the paper words the dependence both ways (p. 462 against p. 485). Hard; considered "type of identification". | — | — |
| C08 | organizational identification | none | Denies a relationship: prospecting is said not to relate to identification, so nothing is said to be affected and no direction is asserted. | — | — |
| C09 | organizational identification | none | Denies an effect: financial success is said not to settle identification, so nothing is said to be affected and no direction is asserted. | — | — |
| C10 | organizational identification | none | Denies an effect: demographics are said not to account for identification differences, so nothing is said to be affected and no direction is asserted. | — | — |
| C11 | identification type | none | The paper's overall framing of where identification comes from; identification is named as a product of sensemaking, but not which way anything pushes it. Considered "type of identification". | — | — |
| C36 | influence of identification on later sensemaking | none | States a two-way relation between identification and sensemaking (residue and lens); nothing is said to go up or down. | — | — |
| C53 | learning of organizational culture | none | Says when culture learning is settled (the first six months), which means the period matters; it names no cause pushing learning one way. Considered "learning of the organization's culture". | — | — |

**Both name an outcome: 49 claims.** Whether the two wordings name the same thing is judged by reading. The calls: match 45, polarity inverted 1, different variable 3, unclear 0, coder 2 means none 0, not yet judged 0.

| claim | coder 1 | coder 2 | by reading | note |
|---|---|---|---|---|
| C02 | positive identification | positive identification with the organization | match | the same, with the organization named |
| C03 | nonpositive identification outcomes | non-positive identification (deidentification, disidentification or ambivalence) | match | the same, with the three non-positive forms named |
| C04 | reliance on value-based control | need for shared organizational values as a means of control | match | coder 2 names the need for values as control, which is coder 1's own direction |
| C07 | identification type | type of identification with Amway | match | the same, in other words |
| C12 | seekership | seekership | match | the same word |
| C13 | seekership | meaning void in the distributor's sense of self | different variable | coder 2 names the void or deficit in the self that dream building creates, which coder 1's direction treats as the condition of seekership |
| C14 | incorporation of dreams into the self | incorporation of dreams into the sense of self | match | the same, in other words |
| C15 | motivation to change the current self | motivation to change the current self | match | the same words |
| C16 | strength of identity-deficit motivation | motivational force of identity deficits | match | the same, in other words |
| C17 | seekership | persistence of seekership | match | coder 2 names the persistence of seekership, which coder 1's direction says is sustained |
| C18 | breadth of life tied to distributor identity | extent of a distributor's life intertwined with the distributor identity | match | the same, in other words |
| C19 | search for self-related meaning | search for meaning about the self | match | the same, in other words |
| C20 | encapsulated sensemaking | encapsulated sensemaking | match | the same words |
| C21 | strength of mentor-protege relationships | strength of upline-downline bonds | match | the same ties: coder 1 calls them mentor and protege, coder 2 upline and downline |
| C22 | encapsulation | social and ideological encapsulation of members | match | the same, with its two kinds named |
| C23 | reliance on organizational sources in sensemaking | reliance on organizational sources for sensemaking | match | the same, in other words |
| C24 | salience of distributor identity in sensemaking | self-definition as a distributor | match | both name how strongly the distributor identity holds: coder 1 in later interpretation, coder 2 in self-definition |
| C25 | belief in the superiority of Amway relationships | belief [7 words of Pratt (2000), p. 474] | match | the same, in other words |
| C26 | continued enactment of identification-management practices | continued engagement in sensebreaking (dream building) | match | coder 2 names the dream building part of the practices coder 1 names |
| C27 | organizational identification | deidentification or failure to identify | polarity inverted | coder 1 names identification, which weakens or fails to form; coder 2 names its failure or loss, which results |
| C28 | disidentification | disidentification | match | the same word |
| C29 | ambivalent identification | ambivalent identification | match | the same words |
| C30 | ease of identification management | ease of managing members' identification | match | the same, in other words |
| C31 | need for strict insider-outsider boundaries | need for [6 words of Pratt (2000), p. 483] | match | the same, in other words |
| C32 | member compliance | compliance with organizational demands | match | the same, in other words |
| C33 | receptivity to further identification-management practices | amenability to further sensebreaking and sensegiving | match | the same, with the practices named |
| C35 | motivation for identification | [6 words of Pratt (2000), p. 487] | match | the same, in other words |
| C38 | depth of organizational identification | depth of identification | match | the same, in other words |
| C39 | professional identification | strength of identification with the profession | match | the same, in other words |
| C40 | sense of common purpose | members' sense of common purpose | match | the same, in other words |
| C41 | organizational functioning | organizational functioning | match | the same words |
| C42 | costs of identification management | costs to members and organizations | match | the same, in other words |
| C43 | felt purpose and communal belonging | sense of purpose and community among active distributors | match | the same, in other words |
| C44 | member loyalty and commitment | members' loyalty and commitment | match | the same words |
| C45 | visibility of focal dynamics | ease of theory building | different variable | coder 1 names the visibility of the dynamics; coder 2 names the theory building that the visibility serves, which the statement names as what is aided |
| C46 | strength of interpretive assertions | strength of assertions about interpretations | match | the same, in other words |
| C47 | informant trust | informants' trust in the researcher | match | the same, in other words |
| C48 | opportunity to ask atypical questions | researcher's opportunity to ask unusual questions | match | the same, in other words |
| C49 | stability of organization-consistent sensemaking | strength of [7 words of Pratt (2000), p. 474] | match | both name the hold of the Amway-consistent sensemaking: coder 1 its stability, coder 2 the strength of its context |
| C50 | motivation for organizational attachment | [6 words of Pratt (2000), p. 487] | match | the same motive: coder 1 calls it attachment to the organization, coder 2 identifying with it |
| C51 | motivation for continuous improvement | motivation for continued improvement | match | the same, in other words |
| C52 | practical suitability of intensive identification management | suitability of the identification-management practices for an organization | match | the same, in other words |
| C54 | motivational force of goals | motivating force of goals | match | the same, in other words |
| C55 | permeability of the insider–outsider boundary | in-group or out-group standing of a person | different variable | coder 1 names the permeability of the boundary; coder 2 names a person's standing on one side of it or the other |
| C56 | membership turnover | member turnover | match | the same, in other words |
| C57 | strength of upline ties | seeking out and bonding with upline distributors | match | the same ties: coder 1 their strength, coder 2 seeking out and bonding with the upline |
| C58 | volatility of mentoring relationships | volatility of mentoring relationships | match | the same words |
| C59 | seekership | seekership | match | the same word |
| C60 | encapsulated sensemaking | encapsulated sensemaking | match | the same words |

**Both write `none`: 4 claims.** C01, C05, C34, C37.

## Stage A2: the asserted direction (section 0b)

56 claims name an outcome in the corpus, and only those were sent, each with the corpus's outcome printed. Coder 2 gives a direction on 53 and writes `none` on 3.

**Sign, by reading.** The wording of a direction differs between any two coders, so what is judged is whether both push the printed outcome the same way. No kappa is computed. The calls: agree 51, disagree 0, unclear 2, coder 2 means none 0, not yet judged 0.

| claim | the outcome as printed | coder 1 | coder 2 | sign, by reading | note |
|---|---|---|---|---|---|
| C02 | positive identification | [5 words of Pratt (2000), p. 476] succeed, positive identification becomes more likely | [5 words of Pratt (2000), p. 476] succeed, positive identification forms (more positive identification) | agree | both: more positive identification when both practices succeed |
| C03 | nonpositive identification outcomes | when either sensebreaking or sensegiving fails, deidentification, disidentification, or ambivalent identification becomes more likely | When sensebreaking or sensegiving fails, nonpositive identification outcomes become more likely | agree | both: the non-positive forms more likely when either practice fails |
| C04 | reliance on value-based control | less direct supervision and fewer conventional cues increase the need for value-based control | The less direct supervision and conventional workplace cues an organization has, the more it relies on value-based control | agree | both: less supervision and fewer cues, more reliance on values as control |
| C06 | identification type | positive, negative, mixed, and weak emotional evaluations correspond respectively to positive, oppositional, ambivalent, and absent identification | When the emotional reaction to Amway is positive, identification is positive; when negative, disidentification; when both, ambivalent; when there is no strong reaction, no identification | agree | the outcome is a category, and both give the same mapping of reaction to type |
| C07 | identification type | different success combinations of dream building and positive programming correspond to different identification states | [6 words of Pratt (2000), p. 463] both succeed, identification is positive; when dream building fails, there is no identification or it breaks; when dream building succeeds and positive programming fails, disidentification; when positive programming only partly succeeds, ambivalent identification | unclear | the outcome is a category; coder 1 says only that the type follows the combination of the two practices, coder 2 gives the mapping, so there is no sign of coder 1's to set beside it |
| C11 | identification type | different motivated-sensemaking outcomes lead to positive, absent, oppositional, or ambivalent identification | When members are motivated to make sense of themselves in harmony with the organization, identification is positive; in opposition to it, disidentification; both, ambivalent; when there is no such motivation, no identification | unclear | the outcome is a category; coder 1 says only that different sensemaking outcomes lead to different types, coder 2 gives the mapping, so there is no sign of coder 1's to set beside it |
| C12 | seekership | more successful sensebreaking increases seekership | When sensebreaking succeeds, seekership arises (more seekership) | agree | both up |
| C13 | seekership | when dream building successfully links aspirations to the self and sustains identity deficits, seekership increases | When dream building is carried out and takes hold, seekership is created and kept going (more seekership) | agree | both up |
| C14 | incorporation of dreams into the self | more choice, familiarity, and emotional engagement make incorporation of dreams into the self more likely | The more a dream is personalized through choice, familiarity and emotional appeal, the more readily it is incorporated into the self | agree | both up |
| C15 | motivation to change the current self | a larger current–ideal self discrepancy increases motivation to change the current self | When a distributor compares a desired future self with the current self, motivation to change the current self increases | agree | both up; coder 2's condition is the comparison itself, coder 1's the size of the gap |
| C16 | strength of identity-deficit motivation | greater dissatisfaction with the current identity strengthens the motivational effect of an identity deficit | When people are in crisis or unhappy with their current identity, identity-deficit motivation is stronger | agree | both up |
| C17 | seekership | continued dream building sustains or renews seekership over time | The more continually dream building is repeated, the more seekership is sustained | agree | both: seekership sustained |
| C18 | breadth of life tied to distributor identity | more sustained dream building links more life domains to the distributor identity | The longer dream building goes on, the broader the part of life tied to the distributor identity | agree | both up |
| C19 | search for self-related meaning | greater seekership increases the search for meaning about the self | When seekership is present, the search for self-related meaning increases | agree | both up |
| C20 | encapsulated sensemaking | more successful positive programming increases encapsulated sensemaking | When positive programming succeeds, encapsulated sensemaking occurs (more of it) | agree | both up |
| C21 | strength of mentor-protege relationships | more enacted economic and emotional support strengthens mentor-protege relationships | When upline mentors give both economic and emotional support, mentor-protege relationships are stronger | agree | both up |
| C22 | encapsulation | stronger relationship barriers increase social and ideological encapsulation | The more outside relationships are revalued downward against the Amway standard, the more encapsulation | agree | both up; coder 2's condition is the revaluing that builds the barriers coder 1 names |
| C23 | reliance on organizational sources in sensemaking | more encapsulation increases reliance on upline and other Amway sources while reducing outside influence | The more encapsulated a member is, the more they rely on organizational sources in sensemaking | agree | both up |
| C24 | salience of distributor identity in sensemaking | more self-chosen distributor behavior increases distributor-consistent sensemaking | The more a member freely chooses to act as a distributor, the more salient the distributor identity becomes in sensemaking | agree | both up |
| C25 | belief in the superiority of Amway relationships | either acceptance or rejection by a prospect can strengthen belief that Amway relationships are superior | When members try to sponsor family and friends, belief in the superiority of Amway relationships strengthens, whether the prospects join or refuse | agree | both: the belief strengthens whether prospects join or refuse |
| C26 | continued enactment of identification-management practices | stronger positive identification increases continued participation in dream building and related reenactment | When members positively identify, continued enactment of the identification-management practices increases | agree | both up |
| C27 | organizational identification | when sensebreaking fails, organizational identification weakens, fails to form, or dissolves | When sensebreaking fails, organizational identification is absent or dissolves (less identification) | agree | both down |
| C28 | disidentification | successful sensebreaking combined with failed sensegiving increases disidentification | When sensebreaking succeeds but sensegiving fails, disidentification increases | agree | both up |
| C29 | ambivalent identification | successful sensebreaking combined with partially successful sensegiving increases ambivalent identification | When sensebreaking succeeds but sensegiving only partly succeeds, ambivalent identification results (more of it) | agree | both up |
| C30 | ease of identification management | greater selection of people predisposed to seekership makes identification management easier | When an organization selects people already disposed to seekership, identification management becomes easier | agree | both: easier |
| C31 | need for strict insider-outsider boundaries | more favorable outsider regard reduces the need for strict insider-outsider boundaries | The more favorably outsiders regard the organization, the less the need for strict insider-outsider boundaries | agree | both down |
| C32 | member compliance | more positive identification increases willingness to follow organizational requests | When members positively identify, member compliance increases | agree | both up |
| C33 | receptivity to further identification-management practices | more positive identification increases receptivity to further sensebreaking and sensegiving | When members positively identify, receptivity to further identification-management practices increases | agree | both up |
| C35 | motivation for identification | a stronger current–ideal self discrepancy increases motivation to identify by creating a need for meaning | When there is a discrepancy between current and ideal self, motivation for identification increases | agree | both up |
| C36 | influence of identification on later sensemaking | once identification forms, it increasingly shapes subsequent sensemaking | Once an identification has formed, it shapes later sensemaking (influence present, not absent) | agree | both: the influence is there once identification forms; coder 1 says it grows, coder 2 that it is present |
| C38 | depth of organizational identification | more identity domains bound to the organization produce deeper identification | The more facets of a person's identity are bound up in the organization, the deeper the identification | agree | both up |
| C39 | professional identification | combining sensebreaking with encapsulating sensegiving increases professional identification | When self-unsettling practices are paired with encapsulating relationships and demands, professional identification is stronger | agree | both up |
| C40 | sense of common purpose | more encapsulated sensemaking helps sustain common purpose when face-to-face contact is infrequent | When encapsulated sensemaking is fostered in a dispersed workforce, sense of common purpose is retained (higher than it would otherwise be) | agree | both: the common purpose kept up |
| C41 | organizational functioning | stronger positive identification can improve organizational functioning | The stronger the positive identification, the better the organizational functioning | agree | both up |
| C42 | costs of identification management | more intensive identification management can increase individual and organizational costs | The more intensively identification is managed, the greater the costs to members and the organization | agree | both up |
| C43 | felt purpose and communal belonging | greater integration of previously separate life domains through Amway increases felt purpose and communal belonging | When Amway brings work, family and religion into one identity framework, felt purpose and communal belonging increase | agree | both up |
| C44 | member loyalty and commitment | when job security is weaker, stronger cultures can increase member loyalty and commitment | The stronger the organizational culture, the more member loyalty and commitment, where job security no longer supplies it | agree | both up |
| C45 | visibility of focal dynamics | more extreme cases make focal dynamics more visible for theory development | The more extreme the case, the more visible the focal dynamics | agree | both up |
| C46 | strength of interpretive assertions | using multiple kinds of data strengthens interpretive assertions through triangulation | When several kinds of data are used and triangulated, interpretive assertions are stronger | agree | both up |
| C47 | informant trust | more direct participation in informants’ work can increase informant trust | When the researcher does the same work as informants, informant trust increases | agree | both up |
| C48 | opportunity to ask atypical questions | a semiovert researcher role increases opportunities to ask questions that ordinary coworkers might not ask | When the researcher's role is semiovert, the opportunity to ask atypical questions increases | agree | both up |
| C49 | stability of organization-consistent sensemaking | when either prospect acceptance or refusal leaves a balanced relationship configuration, organization-consistent sensemaking can become more stable | When the relationship triad stays balanced (as it does whether prospects join or refuse), organization-consistent sensemaking becomes more stable | agree | both: more stable |
| C50 | motivation for organizational attachment | more seekership can increase motivation for organizational attachment in part-time, contingent, or voluntary settings | When seekership is created in part-time, contingent or voluntary members, motivation for organizational attachment increases | agree | both up |
| C51 | motivation for continuous improvement | more seekership can increase motivation for continuous improvement during prolonged professional socialization | When seekership is maintained during long socialization, motivation for continuous improvement is sustained (higher) | agree | both: kept up, so higher |
| C52 | practical suitability of intensive identification management | a larger labor pool increases the practical suitability of identification-management practices that produce high turnover | The larger the organization's labor pool, the more suitable intensive identification management is | agree | both up |
| C53 | learning of organizational culture | newcomers' first half-year has particular importance for acquiring key elements of an organization's culture | In the first six months after entry, learning of organizational culture is greater than later | agree | both put more of the learning in the first six months; coder 2 notes that the footnote calls the period critical rather than fuller |
| C54 | motivational force of goals | goals connected to a person’s self-concept carry greater motivational force | When goals are tied to a person's sense of self, their motivational force is greater | agree | both up |
| C55 | permeability of the insider–outsider boundary | interest from an outsider or continued tolerance of an inactive or unsupportive contact can leave the boundary more permeable than a fixed group division | When outsiders show interest or members lapse, classification bends and does not hold: permeability is higher than other theories of in-group and out-group posit | agree | both: the boundary more permeable |
| C56 | membership turnover | less uniformly successful identification management is associated with greater turnover | The less consistently the practices secure identification, the higher the membership turnover | agree | both: less consistent success, more turnover |
| C57 | strength of upline ties | when an active drive to seek meaning through Amway is absent, consultation and closeness with upline distributors decrease | When members have no ongoing need to change themselves through Amway, upline ties are weaker (less strength) | agree | both down |
| C58 | volatility of mentoring relationships | when mentoring combines business and social ties, the likelihood of conflict or negative reactions increases | When a mentoring tie mixes business interest with personal closeness, its volatility is higher | agree | both up |
| C59 | seekership | self-invalidating practices other than dream building can stimulate a search for renewed self-meaning | When organizational practices invalidate a member's current self, seekership arises (more seekership), with or without dream building | agree | both up |
| C60 | encapsulated sensemaking | stronger inward bonds, managed contacts, and supportive outsiders can increase organization-centered meaning-making | When organizations build cohesive, distinct groups, manage members' contacts and co-opt favorable outsiders, encapsulated sensemaking increases | agree | both up |

**Coder 2 writes `none`: 3 claims.**

| claim | the outcome as printed | coder 1 | coder 2's reason |
|---|---|---|---|
| C08 | organizational identification | among people already recruited, variation in prospecting does not systematically raise or lower identification | Claim denies a relationship: every member was recruited, so prospecting does not vary among members and identification cannot move with it (fn. 7); a null, not a direction. I would have used a "no effect" code if one existed. |
| C09 | organizational identification | greater financial success does not systematically produce stronger or more positive identification | Claim says identification did not follow financial success either way: successful people quit and unsuccessful ones loved Amway (p. 463); it asserts absence of a relationship. I would have used "no effect". |
| C10 | organizational identification | visible demographic differences do not show a systematic increase or decrease in identification | Claim says visible demographics [9 words of Pratt (2000), p. 463] (p. 463); a hedged null with no direction. "No effect" is the code I would have wanted. |

## Stage V: voice (section V)

**Voice:** n = 125; raw agreement 0.968 (121 of 125); kappa 0.908 (95% interval 0.80 to 0.98).

| coder 1 in rows, coder 2 in columns | `reported` | `author_insight` |
|---|---|---|
| `reported` | 95 | 0 |
| `author_insight` | 4 | 26 |

The pack builder took an opening voice cue off the description of 36 rows, which the key lists. Their fragments are marked * below. Where coder 2 notes that such a description and the page disagree, that is the builder's doing.

**Disagreements: 4.**

| row | fragment | location | coder 1 | coder 2 | coder 1's reason | coder 2's reason |
|---|---|---|---|---|---|---|
| V.53 | F53* | pp. 469–470 | `author_insight` | `reported` | The passage organizes positive programming into an interpreted sensegiving process spanning multiple observations. | describes what the practice consisted of and what distributors learn from the upline mentor, largely in the setting's terms. Flag: general description in the author's voice; nearby sentences (positive relationships "become a source of meaning") are interpretive |
| V.63 | F63* | pp. 471–472 | `author_insight` | `reported` | The author interprets mentoring advice as shaping members' self-understanding and insulating them from outsiders. | reports what mentors do: guide on books and tapes, advise on marriage, parenting and religion, help members avoid non-supporters. Flag: wrapped in functional claims ("key", "critical in helping to insulate", "creating relationship barriers") that are the author's; a hard row |
| V.65 | F65* | p. 472 | `author_insight` | `reported` | The passage interprets comparisons among relationships as a revaluing process that privileges Amway ties. | reports how work relationships "are promoted" and "seen", with the setting's sayings quoted ("J.O.B."). Flag: reasoning of people across events in the author's voice; the paragraph's opening sentence is his claim, and the description words it analytically |
| V.125 | F125* | p. 478 | `author_insight` | `reported` | The paragraph connects an absent or waning interest in Amway with weaker upline ties across interviewees, rather than presenting one bounded incident. | says these people did not form strong bonds with distributors; what was the case. Flag: "[6 words of Pratt (2000), p. 478]" is motive across people in the author's voice, "Not surprisingly" ties it to his model, and the description's "had little reason to" leans further |

## Stage B: sections 1 to 7

### 1. Direction

**All comparable links:** n = 452; raw agreement 0.867 (392 of 452); kappa 0.714 (95% interval 0.64 to 0.78).

**Links on directional claims:** n = 322; raw agreement 0.814 (262 of 322); kappa 0.642 (95% interval 0.56 to 0.72).

| coder 1 in rows, coder 2 in columns | `illustrates` | `with` | `against` | `qualifies` |
|---|---|---|---|---|
| `illustrates` | 266 | 7 | 1 | 0 |
| `with` | 46 | 125 | 1 | 0 |
| `against` | 3 | 0 | 0 | 0 |
| `qualifies` | 1 | 1 | 0 | 1 |

**Disagreements: 60.**

| row | fragment | claim | coder 1 | coder 2 | coder 1's basis | coder 2's reason |
|---|---|---|---|---|---|---|
| 1.33 | F23 | C09 | `qualifies` | `illustrates` | Interviewees could not or would not provide comparable net-profit figures and disagreed about accounting, which limits how directly financial success can be assessed. | Stub reports unclear and disputed profit figures; nothing about identification. |
| 1.60 | F33 | C18 | `with` | `illustrates` | The episode ties distributing simultaneously to career choice, helping others, and religious purpose, showing more life domains bound to the distributor role even though the duration of dream building is unstated. | Stub reports an upline framing distributing as a calling; it does not report any distributor's areas of life becoming tied to the identity. |
| 1.64 | F34 | C18 | `with` | `illustrates` | The distributor links an altruistic caregiving project to the Amway business, adding another life domain to the distributor identity. | Stub reports one dream to be funded by Amway; how much of her life is tied to being a distributor is not reported. |
| 1.80 | F39 | C14 | `with` | `illustrates` | The researcher treats personal freedom as his own dream and reports strong excitement about it, showing a self-relevant aspiration taking hold. | Stub reports the emotion condition (excitement); the dream becoming part of his sense of self is not reported. |
| 1.81 | F39 | C54 | `with` | `illustrates` | The researcher recounts strong excitement about a dream of personal freedom even while doubting it could be realized. | Stub reports a feeling (excitement despite doubt), not force on his willingness to act. |
| 1.83 | F40 | C12 | `illustrates` | `with` | The fragment shows the self being unsettled by dream building, but its reported outcome is pressure to change rather than seekership itself. | Stub reports the practice leaving the current self feeling inadequate and pushing members to change: the unsettled, discontented state the outcome names, though not called seekership. |
| 1.84 | F40 | C13 | `illustrates` | `with` | Dream building creates the identity deficit named by the claim, while the stub stops short of reporting seekership. | Stub reports dream building producing an identity deficit that pushed members toward change: the outcome going the asserted way. |
| 1.89 | F41 | C15 | `with` | `illustrates` | The present self is negatively evaluated and members are urged to change in order to reach desired futures. | Stub reports how contentment was framed and that change was urged (the deficit side); it does not report distributors being moved to change. |
| 1.90 | F41 | C16 | `with` | `illustrates` | The stub shows dissatisfaction with the present self being cultivated alongside stronger pressure to change. | Stub does not report motivation being stronger or weaker with prior dissatisfaction. |
| 1.123 | F49 | C19 | `with` | `illustrates` | The seekers use dreams to interpret present dissatisfaction and direct self-change, showing self-related meaning seeking. | Stub reports dissatisfaction and a drive to change; a search for interpretations of who they are is not reported. |
| 1.128 | F50 | C32 | `with` | `illustrates` | The fragment reports sustained behavior aligned with demanding business goals, an instance of compliance-like action, though positive identification is not stated in the stub. | Stub reports self-chosen sacrifices; no organizational request is mentioned. |
| 1.131 | F51 | C32 | `with` | `illustrates` | Repeated nightly business activity and downline support show behavior consistent with strong compliance, while the cause is not given in the stub. | Stub reports what he does night after night; no organizational request is mentioned. |
| 1.139 | F53 | C23 | `with` | `illustrates` | The mentor is described as defining which relationships and information should be treated as desirable, directly shifting interpretive reliance toward organizational sources. | Stub reports the mentor defining desirable relationships and information; members' reliance on such sources is not reported. |
| 1.168 | F61 | C43 | `illustrates` | `with` | The large network of dependable personal support resembles community, but the stub does not report integrated purpose across life domains. | Stub reports a felt community (about a hundred people he can count on, valued as an intangible benefit); the joining of life domains is not mentioned. |
| 1.174 | F63 | C23 | `with` | `illustrates` | The stub reports reliance on mentors for business, family, and religious advice while outside critics are screened out. | Stub reports advice being offered on many matters; members' reliance on it is not reported. |
| 1.186 | F67 | C42 | `with` | `illustrates` | The episode records a personal-relationship cost associated with prioritizing Amway participation. | Stub reports a refusal; it names no cost, loss or strain to him or the organization. |
| 1.189 | F68 | C55 | `illustrates` | `with` | The instructions about unsupportive spouses describe contacts whose status is not an immediate simple outsider exclusion. | Step 1 unclear: if this claim were false, this stub would instead say unsupportive spouses were to be treated like any other unsupportive outsider; it says members were to keep trying to bring them in. |
| 1.199 | F71 | C22 | `with` | `illustrates` | The guidance to reduce contact with unsupportive close others is itself a relationship barrier that narrows members’ social exposure. | Stub reports what members were encouraged to do about unsupportive contacts (the barrier); encapsulation achieved is not reported. |
| 1.205 | F72 | C22 | `with` | `against` | Spending more time with Amway-supportive people and recruiting or training them is reported together with increased social encapsulation. | Stub reports encapsulation growing and puts it down to time spent with other distributors and to recruiting and training, not to barriers against outside relationships: the outcome with another cause. |
| 1.215 | F74 | C42 | `with` | `illustrates` | The fragment records a substantial interpersonal cost during early business participation. | Step 1 unclear (a hardship is named): if this claim were false, this stub would instead say the same, that friends' harsh reactions made the first months hard; the hardship is put to outsiders, not presented as a cost of the practices. |
| 1.219 | F75 | C42 | `with` | `illustrates` | The stub reports damaged or avoided personal relationships associated with distributor recruiting activity. | Stub reports non-members keeping away; no cost to members or the organization is named. |
| 1.223 | F76 | C42 | `with` | `illustrates` | The observed mutual distancing is an interpersonal cost of the identification-management environment. | Stub reports mutual distancing; no cost is named. |
| 1.239 | F80 | C21 | `with` | `illustrates` | The interviewee describes a close upline relationship as necessary support for continuing in a difficult business. | Stub says a close upline relationship is needed to stay active; it does not report how strong any tie was or what made it so. |
| 1.256 | F84 | C36 | `with` | `illustrates` | The distributor’s Amway-related identity frame changes how she interprets people previously regarded as friends. | Stub reports how she read the refusal; it does not say an identification, or any Amway frame, shaped that reading. |
| 1.268 | F86 | C32 | `with` | `illustrates` | The positively identified members enthusiastically promote the organizational lifestyle, a form of organization-aligned behavior. | Stub reports promoting and re-enacting; no organizational request or demand is mentioned. |
| 1.275 | F88 | C02 | `with` | `illustrates` | Figure 1 maps successful sensebreaking and successful sensegiving to positive identification. | Stub says the figure ties success combinations to identification states but not which to which; the direction for positive identification is not carried (wanted a code for "outcome named, direction missing"). |
| 1.276 | F88 | C03 | `with` | `illustrates` | The figure maps practice failures to broken, oppositional, or ambivalent outcomes. | Stub does not say which combinations lead to the nonpositive states; the direction is not carried. |
| 1.279 | F88 | C27 | `with` | `illustrates` | Figure 1 places failed sensebreaking on the path to absent or broken identification. | Stub does not say what follows when sensebreaking fails. |
| 1.280 | F88 | C28 | `with` | `illustrates` | Figure 1 places successful sensebreaking plus failed sensegiving on the path to disidentification. | Stub does not say which combination goes with disidentification. |
| 1.281 | F88 | C29 | `with` | `illustrates` | Figure 1 places successful sensebreaking plus partially successful sensegiving on the path to ambivalent identification. | Stub does not say which combination goes with ambivalent identification. |
| 1.283 | F89 | C12 | `with` | `illustrates` | The absence or loss of dissatisfaction is reported together with the absence of seekership-like motivation. | Stub reports seekership absent (dissatisfaction never arose, or lapsed); it does not say whether sensebreaking was tried or how it fared. |
| 1.292 | F90 | C42 | `with` | `illustrates` | The fragment concerns a former distributor whose organizational involvement ended, contributing to the turnover side of the costs claim. | Step 1 unclear (a departure is turnover): if this claim were false, this stub would instead say the same, that he lost interest and left; the exit is not presented as a cost of the practices. |
| 1.298 | F91 | C42 | `with` | `illustrates` | The nonrenewing distributor stops investing time in Amway, an instance of member exit or turnover. | Stub reports a non-renewal and puts it to her job having become satisfying; it is not presented as a cost of the practices. Considered against (turnover with another cause). |
| 1.303 | F92 | C42 | `with` | `illustrates` | The former distributor’s withdrawal is another instance of turnover, one of the costs named by the claim. | Stub reports a departure with a flat reason; it is not presented as a cost of the practices. |
| 1.306 | F93 | C20 | `against` | `illustrates` | The distributor becomes increasingly distant from upline and rejects their authority, the opposite of the strong mentor-based encapsulation described by the claim. | Stub reports his refusal to take uplines' word as law; whether positive programming worked on him is not stated, so his low reliance has no condition to set against. |
| 1.307 | F93 | C23 | `against` | `illustrates` | The distributor refuses to treat upline statements as authoritative, reporting low organizational-source reliance. | Stub is split: the members he describes defer wholly to uplines, he does not; nothing on encapsulation for either (wanted a "mixed" code). |
| 1.310 | F93 | C57 | `with` | `illustrates` | The departing member no longer treated upline guidance as authoritative, reporting a weaker upline connection without naming an alternative cause for it. | Stub reports his view of others' deference to uplines; his own consulting of, or closeness to, his upline is not reported. |
| 1.324 | F96 | C42 | `with` | `illustrates` | Distant and angry upline relationships among former distributors show an interpersonal cost associated with failed identification management. | Stub reports soured upline relationships among disidentifiers; not presented as a cost. |
| 1.330 | F97 | C42 | `with` | `illustrates` | The failed upline relationship is reported as a source of disenchantment, an individual cost of the identification-management arrangement. | Stub reports his complaint about his upline; no cost is named. |
| 1.333 | F98 | C21 | `against` | `illustrates` | The recruitment interaction is coercive and humiliating rather than practically and emotionally supportive, pointing away from a strong mentor bond. | Stub reports pressure at a sales presentation; neither support nor the strength of a mentoring tie is reported. |
| 1.335 | F98 | C42 | `with` | `illustrates` | The joining experience includes intense social pressure and humiliation, a direct individual cost. | Step 1 unclear (pressure and embarrassment are burdens): if this claim were false, this stub would instead say the same; the burden comes from a sales presentation, which the stub does not present as identification management. |
| 1.344 | F99 | C36 | `with` | `illustrates` | An oppositional identification becomes a frame through which upline friendliness is reinterpreted as self-interest. | Stub runs from interpretation to self-definition against Amway; it does not report an identification then shaping later interpretation. |
| 1.349 | F100 | C42 | `with` | `illustrates` | The archival message describes claimed family and credibility costs of affiliation, though it is an ex-member source rather than the author’s own assessment. | Stub reports a warning that affiliation can harm family and credibility: a warning, not a cost reported as incurred, and not tied to the practices. |
| 1.365 | F104 | C06 | `with` | `illustrates` | The distributor’s behavior combines prior visible involvement with immediate repudiation after outside criticism, indicating mixed evaluation. | Stub reports behaviour (showing off merchandise, then denying involvement); neither his feelings nor his identification state is stated. |
| 1.370 | F105 | C22 | `qualifies` | `with` | Rather than abandoning valued outside relationships, the distributor changes recruiting targets to protect them, limiting the extent of relationship barriers. | Stub reports the low end: he still counts outside relationships as important and shields them, and he keeps them. |
| 1.371 | F105 | C25 | `illustrates` | `against` | A lost friendship after recruiting changes later prospecting behavior, but the stub does not report stronger belief in Amway relationship superiority. | Stub reports a rejection treated as a loss to guard against: he goes on prizing outside relationships and steers recruiting away from them, the opposite of rejection confirming Amway ties; the claim is hedged ("can"). |
| 1.372 | F105 | C29 | `with` | `illustrates` | The distributor preserves important non-Amway ties even while remaining involved, consistent with only partial encapsulation on the ambivalent pathway. | Stub reports him still recruiting while protecting outside ties; a mixed identification is not stated. |
| 1.374 | F105 | C42 | `with` | `illustrates` | The episode records loss of a friendship as a cost associated with recruiting. | Stub reports a friendship lost through recruiting; it is put to the friend's reaction, not presented as a cost of the practices. |
| 1.377 | F106 | C23 | `illustrates` | `with` | Outside criticism changes enthusiasm and leads to avoidance, but the stub does not report increased reliance on upline sources. | Stub reports outside evaluations carrying force while he was in contact (enthusiasm weakened), and contact cut to stop it. |
| 1.378 | F106 | C29 | `illustrates` | `with` | The fragment shows competing role pulls and outside criticism during participation, but it does not assign the researcher an ambivalent identification state. | Step 1 unclear (ambivalence not named): if this claim were false, this stub would instead say input from critics alongside his Amway involvement left him settled; it says his enthusiasm wavered and he felt pulled between two roles. |
| 1.380 | F106 | C42 | `with` | `illustrates` | The researcher reports painful role strain and social avoidance during intensive participation, a direct individual cost. | Step 1 unclear (strain is the nearest thing to a cost in these rows): if this claim were false, this stub would instead say the same; the strain is put to the pull between colleagues and Amway, not presented as a cost of the practices. Closest of these rows to with. |
| 1.383 | F107 | C06 | `with` | `illustrates` | Strong upline attachment coexists with conflicting outsider influence and alternating behavior, matching a mixed emotional and behavioral state. | Stub reports their ties, the interpretations they received and their on-off activity; their emotional evaluation is not reported. |
| 1.397 | F109 | C02 | `with` | `illustrates` | The model places successful sensebreaking and sensegiving on the path to positive identification. | Stub says the figure leads to "differing identification outcomes" without saying which condition yields positive identification. |
| 1.398 | F109 | C03 | `with` | `illustrates` | The model places failures in the process on paths to nonpositive identification states. | Stub does not say what follows from a failure of either practice. |
| 1.402 | F109 | C27 | `with` | `illustrates` | The model sends failed sensebreaking toward absent or broken identification. | Stub does not say what follows when sensebreaking fails. |
| 1.403 | F109 | C28 | `with` | `illustrates` | The model sends successful sensebreaking plus failed sensegiving toward disidentification. | Stub does not say which route ends in disidentification. |
| 1.404 | F109 | C29 | `with` | `illustrates` | The model sends successful sensebreaking plus incomplete sensegiving toward ambivalent identification. | Stub does not say which route ends in ambivalent identification. |
| 1.415 | F111 | C40 | `with` | `illustrates` | The fragment reports a sense of shared purpose and community among active distributors, although the dispersed-workforce condition is not restated in the stub. | Stub reports individuals' sense of purpose and community and puts it to uniting work, family and religion; shared purpose across a dispersed workforce, and sensemaking, are not addressed. |
| 1.435 | F117 | C21 | `with` | `illustrates` | The reciprocal parent–child joking signals a close, family-like mentor relationship. | Step 1 unclear (a father/son exchange): if this claim were false, this stub would instead say the same; the stub marks both lines as jokes and reports a cookie, not the strength of the bond. |
| 1.450 | F125 | C20 | `illustrates` | `with` | The fragment describes weak access to mentors, relevant to positive programming, but does not itself describe the encapsulated-sensemaking outcome. | Stub reports the low end: no strong bonds formed with distributors, and upline advice not sought. |

### 2. Core

**`core`:** n = 60; raw agreement 0.917 (55 of 60); kappa 0.732 (95% interval 0.47 to 0.93).

| coder 1 in rows, coder 2 in columns | `true` | `false` |
|---|---|---|
| `true` | 9 | 1 |
| `false` | 4 | 46 |

**Disagreements: 5.**

| row | claim | coder 1 | coder 2 | coder 2's reason |
|---|---|---|---|---|
| 2.3 | C03 | `false` | `true` | The other half of the central result, and the paper's stated departure from work on positive attachment alone. |
| 2.6 | C06 | `false` | `true` | First of the three "key findings": it sets out the four states the model then explains, and returns among the contributions. Hesitated, because the argument needs the four states more than their emotional basis. |
| 2.7 | C07 | `false` | `true` | Second key finding, and the empirical pattern Figure 1 is built from. |
| 2.34 | C34 | `true` | `false` | Listed as the fourth contribution, but the paper says it only "implies" this and does not analyse it; the argument stands without it. Considered true. |
| 2.35 | C35 | `false` | `true` | The motive in "motivated sensemaking", and named among the contributions as a new motivator for identification; overlaps C12. |

### 3. Stated as

**`stated_as`:** n = 60; raw agreement 0.950 (57 of 60); kappa 0.886 (95% interval 0.75 to 1.00).

| coder 1 in rows, coder 2 in columns | `established` | `ventured` |
|---|---|---|
| `established` | 39 | 0 |
| `ventured` | 3 | 18 |

**Disagreements: 3.**

| row | claim | coder 1 | coder 2 | coder 2's reason |
|---|---|---|---|---|
| 3.25 | C25 | `ventured` | `established` | Introduced with "could lead to" and "can serve to", but the passage ends flat ("[12 words of Pratt (2000), p. 474]") and is framed as a way enactment "influenced sensemaking". Coded on the firmest sentence; a close call. |
| 3.56 | C56 | `ventured` | `established` | A flat counterfactual ("If the practices ... always worked ..., [8 words of Pratt (2000), p. 477]"). |
| 3.60 | C60 | `ventured` | `established` | The lead sentence is unhedged ("[13 words of Pratt (2000), p. 482]"), though it rests on what other literatures "suggest" and sits in a model called preliminary. Coded on the firmest sentence; a close call. |

### 4. Gap kind

**`gap kind`:** n = 4; raw agreement 0.750 (3 of 4); kappa withheld (fewer than 10 judgements).

| coder 1 in rows, coder 2 in columns | `scope_limit` | `absent_evidence` | `acknowledged_ambiguity` |
|---|---|---|---|
| `scope_limit` | 2 | 1 | 0 |
| `absent_evidence` | 0 | 0 | 0 |
| `acknowledged_ambiguity` | 0 | 0 | 1 |

**Disagreements: 1.**

| row | gap | coder 1 | coder 2 | coder 2's reason |
|---|---|---|---|---|
| 4.1 | DG01 | `scope_limit` | `absent_evidence` | n. 9 says the design produced no personality data, so the rival explanation stays open: a lack of evidence. Considered scope_limit (p. 457 puts it outside the paper's purpose) and rejected it because the footnote goes past "not our topic" to "cannot be totally ruled out"; unresolved_question also considered. |

### 5. Pair drawn by authors

**`pair drawn_by_authors`:** n = 3; raw agreement 1.000 (3 of 3); kappa withheld (fewer than 10 judgements).

| coder 1 in rows, coder 2 in columns | `true` | `false` |
|---|---|---|
| `true` | 2 | 0 |
| `false` | 0 | 1 |

**Disagreements: 0.**

### 6. Resolution period

**`resolution_period`:** n = 1; raw agreement 1.000 (1 of 1); kappa withheld (fewer than 10 judgements).

| coder 1 in rows, coder 2 in columns | `none` |
|---|---|
| `none` | 1 |

**Disagreements: 0.**

### 7. Gloss relation

**`gloss_relation`:** n = 11; raw agreement 0.818 (9 of 11); kappa 0.607 (95% interval -0.03 to 1.00; 1,999 of 2,000 resamples gave a kappa).

| coder 1 in rows, coder 2 in columns | `consistent` | `goes_beyond` |
|---|---|---|
| `consistent` | 6 | 1 |
| `goes_beyond` | 1 | 3 |

**Disagreements: 2.**

| row | fragment | coder 1 | coder 2 | coder 1's reason | coder 2's reason |
|---|---|---|---|---|---|
| 7.6 | F61 | `consistent` | `goes_beyond` | The informant explicitly describes unusually dependable personal ties within his group, which supports the summary of very strong upline-downline bonds. | The fragment reports very strong ties (about a hundred people he can count on), told from the upline's side; the gloss adds what produced them (successful mentoring), which the fragment does not say. |
| 7.9 | F67 | `goes_beyond` | `consistent` | The episode shows withdrawal from a friend's wedding role after a schedule conflict, while the gloss adds the interpretation that the friend was treated as unsupportive of the business. | On the page the distributor says the friend "deliberately" set the wedding against an Amway event, which carries the perceived lack of support. The stub drops that word; without it the gloss would go beyond a mere clash of dates. |

## `against` in each coding

Every link coded `against` on a directional claim, as coded, whatever the voice of its fragment. An `against` on a claim that names no outcome is invalid by schema: the `against` check is never sent it and the audit never counts it, so it is counted in the last row and nowhere else.

|  | coder 1 | coder 2 |
|---|---|---|
| links coded `against`, on directional claims | 3 | 2 |
| claims with at least one | 3 | 2 |
| the most on one claim | 1 (C20, C21, C23) | 1 (C22, C25) |
| claims with two or more | none | none |
| coded `against` on a claim that names no outcome: invalid by schema, and not counted above | 0 | 0 |

- Coder 1: F93→C20, F93→C23, F98→C21.
- Coder 2: F72→C22, F105→C25.
- Coded `against` by both: 0.

**With the links the `against` check flags counted as `illustrates`:**

|  | coder 1 | coder 2 |
|---|---|---|
| links coded `against`, on directional claims | 0 | 1 |
| claims with at least one | 0 | 1 |
| the most on one claim | 0 | 1 (C22) |
| claims with two or more | none | none |
| coded `against` on a claim that names no outcome: invalid by schema, and not counted above | 0 | 0 |
| links flagged (answered 4a to 4x) | 3: F93→C20, F93→C23, F98→C21 | 1: F105→C25 |
| of them, answered 4a | 0 | 0 |

## The audit under each coding

Coder 1's column is the corpus with the extraction's sidecar. Coder 2's column is the corpus with coder 2's codes in place of coder 1's (direction, core, stated as, gap kind and resolution period) and with coder 2's voice codes. Whether a pair was drawn by the authors changes no figure in this table. Which claims are directional is the corpus's in both, because both codings of direction were made against the outcome and the direction the corpus records. The voice rule is applied in both: a `with` or `against` link from a fragment coded `author_insight` is left out, and counted in the row "left out by the voice rule".

|  | coder 1 | coder 2 |
|---|---|---|
| directional claims | 56 | 56 |
| `with` and `against` links counted | 82 and 3 | 61 and 1 |
| left out by the voice rule | 90 `with`, 0 `against` | 72 `with`, 1 `against` |
| claims assessed (at least 4 counted links) | 9 | 6 |
| coverage | 0.161 | 0.107 |
| seams | none | none |
| uniformity rate | not reported: coverage is under 0.60 | not reported: coverage is under 0.60 |
| moves parameterised | construct_inversion, counterfactual_ending, focalization_shift | construct_inversion, counterfactual_ending, focalization_shift |

**With the links the `against` check flags counted as `illustrates`:**

|  | coder 1 | coder 2 |
|---|---|---|
| directional claims | 56 | 56 |
| `with` and `against` links counted | 82 and 0 | 61 and 0 |
| left out by the voice rule | 90 `with`, 0 `against` | 72 `with`, 1 `against` |
| claims assessed (at least 4 counted links) | 8 | 6 |
| coverage | 0.143 | 0.107 |
| seams | none | none |
| uniformity rate | not reported: coverage is under 0.60 | not reported: coverage is under 0.60 |
| moves parameterised | construct_inversion, counterfactual_ending, focalization_shift | construct_inversion, counterfactual_ending, focalization_shift |

## What this log does not hold

- Whether the pinned predictions held. They are stated apart, in no file.
- The extraction's miss rate, which comes from the coverage check, and the hours.
- Any reconciliation. Disagreements are discussed only when every paper is coded.
