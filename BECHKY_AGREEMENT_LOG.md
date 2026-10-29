# bechky_2020: agreement between the two codings

Bechky, B. A. 2020. Evaluative spillovers from technological change: The effects of "DNA envy" on occupational practices in forensic science. Administrative Science Quarterly, 65(3): 606–643.

Written by `agreement.py --paper` from the files in the table below, and written whole again whenever a stage returns. It is not edited by hand: the same files, and the same line on who the coders are, give the same log. It carries no date.

- **Coder 1** is the extraction: the corpus, and the extraction's sidecar for voice and gloss relation. **Coder 2** is the second coding: the returned workbooks.
- **Who they are:** Model against model. Coder 1: the extraction, ChatGPT in a Temporary Chat at thinking effort High, which names itself GPT 5.6 Sol. Coder 2: Opus 5.5 at Extra, one incognito claude.ai chat per stage.
- Every figure is **per field and never pooled.** Each is computed from the files as they stand, with no notion of a discussion or a reconciliation: nothing here is merged into the corpus, and no figure changes with what is agreed later. That the coding came back before any disagreement was discussed is the protocol's to ensure (`SECOND_CODER.md`), and the script cannot know it.
- **Kappa** is withheld for a field with fewer than 10 comparable judgements, by count only, and is undefined when both coders use one and the same code throughout. Carlile's logs also withheld it for three named fields at any size; on the cold papers that part of the rule was dropped before any sheet came back (7 Oct 2026).
- **A kappa that is given comes with a 95% interval:** 2,000 resamples of the rows with replacement (seed 20261007), and the 2.5th and 97.5th percentiles of their kappas. A resample in which both coders use one code throughout has no kappa and is left out; where that happens, the figure says how many resamples gave one. Two cautions. The ends move with the seed, and more where a field has few rows: on made-up tables, by about a hundredth at some hundreds of rows, by a few hundredths at about fifty, and by as much as 0.14 at ten to fifteen. And rows are resampled one by one, though links cluster by claim and by fragment, so the interval for direction is likely too narrow.
- **By reading** marks a call that a reader made: whether two outcome wordings name the same thing, and whether two asserted directions push the printed outcome the same way. The script counts the calls. Where a call says that coder 2's wording means `none`, it also gives Stage A's figure a second time, with that call applied. The calls were made by: a reader other than the two coders, on 8 Oct 2026: the calls on the outcome wordings, from the two outcome wordings, read beside the claim's statement, coder 1's asserted direction and coder 2's reason; the calls on the sign, from the two directions, read beside the printed outcome and coder 2's reason.
- The corpus has 172 fragments, 23 claims and 293 links. 18 of the claims are directional: they carry both an outcome and an asserted direction.

| what | file | sha256 opens |
|---|---|---|
| coder 1: the corpus | `bechky_2020_v1.json` | 6f83d744cd1dd683 |
| coder 1: the sidecar | `bechky_2020_v1_voice_gloss.json` | e4b6d8c974a66614 |
| the pack's key (builder version 1.3, 7 Oct 2026) | `bechky_2020_pack_key.json` | ba615a627d7d96db |
| coder 2: Stage A | `returned_bechky_2020_STAGE_A_coder2.xlsx` | 59b8e53858272fa4 |
| Stage A as it came, read in from a text | `reply_bechky_2020_STAGE_A.txt` | 47750977a9820605 |
| Stage A: the digest of its coding tabs (for `judged_on`) | — | 07576edf30b96c2f |
| coder 2: Stage A2 | `returned_bechky_2020_STAGE_A2_coder2.xlsx` | 8b4e02ae2ba5bafd |
| Stage A2 as it came, read in from a text | `reply_bechky_2020_STAGE_A2.txt` | 04acc49e33c18308 |
| Stage A2: the digest of its coding tabs (for `judged_on`) | — | 6ff022ea724a9506 |
| coder 2: Stage V | `returned_bechky_2020_STAGE_V_coder2.xlsx` | 2b72532b79e96fec |
| Stage V as it came, read in from a text | `reply_bechky_2020_STAGE_V.txt` | 0e7c599354183b4f |
| Stage V: the digest of its coding tabs (for `judged_on`) | — | 38a752a4c9618e63 |
| coder 2: Stage B | `returned_bechky_2020_STAGE_B_coder2.xlsx` | 6c226f8fbefae310 |
| Stage B as it came, read in from a text | `reply_bechky_2020_STAGE_B.txt` | 4f0d047ef0c2ff0a |
| Stage B: the digest of its coding tabs (for `judged_on`) | — | a70dd114883218ac |
| the readings | `bechky_2020_readings.json` | f4309a0645840618 |
| the `against` check's results | `against_check_results.json` | cdb54145104e9308 |
| written by | `agreement.py` | 8f2e14619558395f |

## Stage A: the outcome of every claim (section 0)

**Directional or not:** n = 23; raw agreement 0.957 (22 of 23); kappa 0.881 (95% interval 0.57 to 1.00; 1,995 of 2,000 resamples gave a kappa).

| coder 1 in rows, coder 2 in columns | `directional` | `none` |
|---|---|---|
| `directional` | 17 | 1 |
| `none` | 0 | 5 |

**One coder names an outcome and the other writes `none`: 1 claim.**

Where coder 2 alone names an outcome, a reader may call the wording `coder 2 means none`. No other call applies there, because there are no two wordings to compare.

| claim | coder 1 | coder 2 | coder 2's reason | by reading | note |
|---|---|---|---|---|---|
| C10 | differentiation of occupational cultures | none | Names something that varies (occupational culture: values, preferred practices) and says work and field relationships produce the differences, but "different work, different culture" has no sign. Would otherwise have written "occupational culture". | — | — |

**Both name an outcome: 17 claims.** Whether the two wordings name the same thing is judged by reading. The calls: match 14, polarity inverted 2, different variable 1, unclear 0, coder 2 means none 0, not yet judged 0.

| claim | coder 1 | coder 2 | by reading | note |
|---|---|---|---|---|
| C01 | work practices of neighboring non-adopting occupations | change in the work practices of adjacent, non-adopting occupations | match | coder 2 names the change in the same work practices |
| C02 | scrutiny of neighboring forensic occupations | evaluative scrutiny of neighboring forensic occupations | match | the same scrutiny; coder 2 adds 'evaluative' |
| C03 | local work-practice change | strength of the impetus for local practice change | different variable | coder 2 keeps the claim's own word, the impetus for change; coder 1 names the change itself, in its outcome and in its direction |
| C04 | feasibility of local practice adaptation | feasibility of adaptation | match | — |
| C05 | local work-practice adaptation | adaptation of practice (as opposed to resistance) | match | both keep the adaptation polarity |
| C06 | occupational and workplace structure | reconfiguration of occupational arrangements (task boundaries, resource access, workplace relations, status) | match | the same arrangements; coder 2 names their reconfiguration and lists them |
| C08 | resistance to task change | capacity to resist technology-driven changes to tasks | match | coder 1's own direction speaks of the capacity to resist, which is coder 2's wording |
| C09 | symbolic occupational legitimacy | an occupation's symbolic legitimacy | match | — |
| C12 | visibility of interpretive processes | visibility of members' interpretations of and responses to field-level discourse | match | coder 2 says whose interpretations are made visible |
| C14 | perceived objectivity and credibility of DNA evidence | outsiders' perception of the evidence as objective and credible | match | coder 2 says whose perception it is |
| C15 | DNA envy and resentment | envy and resentment among other forensic occupations | match | coder 2 says who feels it |
| C16 | local firearms practice change | firearms examiners' resistance to changing local practice | polarity inverted | coder 1: local practice change, which decreases; coder 2: resistance to changing it |
| C17 | local toxicology practice change | speed of toxicologists' adoption of the reporting change | match | coder 1's direction is more rapid change; coder 2 names the speed outright |
| C18 | local narcotics practice change | narcotics analysts' retention of crystal testing | polarity inverted | coder 1: local practice change, which decreases; coder 2: retention of the old practice |
| C19 | extent of evaluative spillover | likelihood of evaluative spillover reaching an occupation | match | the likelihood and the extent of the same spillover |
| C22 | resistance to changing masking practices | ethnographers' resistance to altering masking practices | match | coder 2 says whose resistance |
| C23 | reach of evaluative spillovers | breadth of occupations and industries reached by evaluative spillovers | match | coder 2 spells out what the reach covers |

**Both write `none`: 5 claims.** C07, C11, C13, C20, C21.

## Stage A2: the asserted direction (section 0b)

18 claims name an outcome in the corpus, and only those were sent, each with the corpus's outcome printed. Coder 2 gives a direction on 18 and writes `none` on 0.

**Sign, by reading.** The wording of a direction differs between any two coders, so what is judged is whether both push the printed outcome the same way. No kappa is computed. The calls: agree 18, disagree 0, unclear 0, coder 2 means none 0, not yet judged 0.

| claim | the outcome as printed | coder 1 | coder 2 | sign, by reading | note |
|---|---|---|---|---|---|
| C01 | work practices of neighboring non-adopting occupations | when a technology becomes an evaluative benchmark in a shared field, pressure on the work practices of neighboring non-users increases | When evaluative spillover from a neighbouring occupation's technology is present, change in non-adopting occupations' work practices becomes possible (more change, not less) | agree | both toward more change in the practices; coder 2 signs it only as change against no change, and as a possibility |
| C02 | scrutiny of neighboring forensic occupations | as DNA profiling becomes a more authoritative benchmark, external evaluation of neighboring forensic groups increases across scientific, media, and courtroom arenas | The stronger one forensic technique's legitimacy, the more scrutiny of neighbouring forensic occupations | agree | — |
| C03 | local work-practice change | more immediate and locally encountered institutional pathways lead to more local practice change, while remote or nonurgent pathways lead to less | The more locally immediate the route by which the comparison arrives, the more local work-practice change; the more remote or nonurgent, the less | agree | coder 2 says the claim signs the impetus to change, and reads it through to the printed outcome |
| C04 | feasibility of local practice adaptation | greater compatibility between the comparison and an occupation’s existing technique makes adaptation more feasible, unless other features such as values block it | The more technically compatible the benchmark technology is with the occupation's existing method, the more feasible local practice adaptation (more feasible, not assured) | agree | coder 2 takes the sign from the concession, not the verb; both say the change is not assured |
| C05 | local work-practice adaptation | greater alignment between an evaluative comparison and occupational values leads to more adaptation, while greater value conflict leads to more resistance | The more the comparison aligns with what the occupation values in good work, the more local adaptation; the more it threatens those values, the less adaptation | agree | where the values conflict, coder 1 writes more resistance and coder 2 less adaptation |
| C06 | occupational and workplace structure | when a new technology is adopted, reconfiguration of occupational tasks, resources, relations, and status becomes more likely | When an occupation directly adopts a new technology, change in occupational and workplace structure becomes possible (more reconfiguration, not less) | agree | coder 2 signs it only as change against stability, and as a possibility, and says it would have written none had a signed rearrangement been asked for |
| C08 | resistance to task change | more professional power or authority leads to greater capacity to resist task changes | The more professional authority an occupation has, the more resistance to technology-driven change in its tasks | agree | coder 1's direction is on the capacity to resist; coder 2 reads it through to resistance, the printed outcome |
| C09 | symbolic occupational legitimacy | stronger association with a novel technology leads to greater symbolic legitimacy for its occupational users | The more an occupation is associated with novel technology, the higher its symbolic legitimacy | agree | coder 2: as a possibility |
| C10 | differentiation of occupational cultures | as occupational work practices and field relationships differ, the cultures, values, and preferred practices of the groups become more distinct | The more occupations' work and field relationships differ, the more differentiated their occupational cultures | agree | at Stage A coder 2 named no outcome for this claim; given coder 1's, it signs it the same way |
| C12 | visibility of interpretive processes | using in-situ ethnographic observation increases the ability to see interpretive and response processes that may otherwise remain hidden | When members are observed ethnographically in place rather than studied by other methods, visibility of their interpretive processes is higher | agree | — |
| C14 | perceived objectivity and credibility of DNA evidence | more visible, reviewable, and standardized representation of DNA analysis leads to greater perceived objectivity and credibility | The more DNA results are presented with statistics, error measures, reviewable outputs and rounds of review, the higher their perceived objectivity and credibility to outsiders | agree | — |
| C15 | DNA envy and resentment | greater legitimacy and resource privilege for DNA profiling leads to more envy and resentment among neighboring forensic groups | The more privileged DNA profiling's legitimacy and resources, the more DNA envy and resentment in other forensic occupations | agree | — |
| C16 | local firearms practice change | when the comparison is remote, technically incompatible, and contrary to holistic subjective judgment values, local firearms practice change decreases | When the comparison arrives by remote challenge, does not map onto the method, and conflicts with valued holistic subjective judgment, less (no) local firearms practice change | agree | both less change; coder 2 writes less (no) change |
| C17 | local toxicology practice change | an immediate local challenge combined with technical and value compatibility and prior preparation leads to more rapid local toxicology practice change | When the court threat is local and immediate, the change fits the instrumented method and error-avoidance values, and accreditation work is already under way, more and sooner local toxicology practice change | agree | coder 1: more rapid change; coder 2: more and sooner, in part a sign on timing |
| C18 | local narcotics practice change | when evaluative pressure is non-immediate and threatens autonomy, variety, and craft judgment, local narcotics practice change decreases even when an instrumented alternative is technically compatible | When pressure arrives through an internal professional debate without immediate compulsion and the implied change threatens valued autonomy, variety and craft judgment, less (no) local narcotics practice change, even where the technique is compatible | agree | both less change, even where the technique is compatible |
| C19 | extent of evaluative spillover | more overlap in audiences, activities, and interests leads to more evaluative spillover between occupations | The more occupations share evaluating audiences and overlap in activities or interests, the greater the extent of evaluative spillover; the weaker the overlap, the less | agree | — |
| C22 | resistance to changing masking practices | a strong commitment to source anonymity combined with a weakly immediate pathway leads to more resistance to changing masking practices | The more strongly source anonymity is valued and the less immediate the route by which the comparison arrives, the more resistance to changing masking practices | agree | — |
| C23 | reach of evaluative spillovers | broader workplace impact of digital technologies leads to wider evaluative spillovers across occupations and industries | The more workplaces digital technologies affect, the wider the reach of evaluative spillovers across occupations and industries | agree | — |

**Coder 2 writes `none`: 0 claims.**

## Stage V: voice (section V)

**Voice:** n = 172; raw agreement 0.936 (161 of 172); kappa 0.865 (95% interval 0.78 to 0.94).

| coder 1 in rows, coder 2 in columns | `reported` | `author_insight` |
|---|---|---|
| `reported` | 100 | 2 |
| `author_insight` | 9 | 61 |

The pack builder took an opening voice cue off the description of 76 rows, which the key lists. Their fragments are marked * below. Where coder 2 notes that such a description and the page disagree, that is the builder's doing.

**Disagreements: 11.**

| row | fragment | location | coder 1 | coder 2 | coder 1's reason | coder 2's reason |
|---|---|---|---|---|---|---|
| V.27 | F27* | p. 614 | `author_insight` | `reported` | The passage interprets several differences among the laboratory units as evidence that they function as neighboring but distinct occupations. | Mostly states what was the case: members identified as separate but related, had distinct associations, similar education, different training. FLAG: "neighboring occupations" is the author's own category, and the self-identification is given in her voice without quotation. |
| V.50 | F50* | p. 619 | `author_insight` | `reported` | The passage generalizes across review activity to explain DNA reporting as an interpretive and collective process. | Describes the routine review process (rounds of interpretation, back-and-forth, others drawn in). Note: the opening sentence on anomalies being "neatened" is interpretive and cited; the description leaves it out. |
| V.58 | F58* | p. 620 | `reported` | `author_insight` | The passage interprets training, methods, and relations with the justice system as producing distinct occupational cultures. | Author sets "in theory" against "in practice" and says work practices "resulted in" distinct cultures: her reading plus a causal explanation. FLAG: mixed; the training lengths (nine months; a year plus a year) are plain report. |
| V.65 | F65* | p. 621 | `author_insight` | `reported` | The passage explains what image documentation accomplishes for firearms judgments in court, rather than merely describing the images. | Describes the documentation practice with its rationale, which Adam states in the next sentence. FLAG: the rationale ("as it reinforces") is in the author's voice and explains the practice in general; ambiguous. |
| V.84 | F84* | p. 624 | `author_insight` | `reported` | The passage explains the absence of local practice change by connecting it to the distance of the criticism and lack of a local challenge. | States two things that were the case: practice unchanged, and no challenge to their testimony locally. MISMATCH: page sets these side by side ("did not motivate"); the description's "because" makes the explanation explicit. Read as an explanation it would be author_insight. |
| V.86 | F86 | p. 624 | `reported` | `author_insight` | The passage immediately characterizes the Tom-and-Pete exchange; under the brief's single-event rule, that interpretation belongs with the reported episode. | Author's account ("thus") of how examiners reasoned about statistics, ending in her own judgment that it would depart from their values. FLAG: could be read as the gloss on the single Tom and Pete conversation; it generalises to "the MCCL firearms examiners". |
| V.88 | F88* | p. 625 | `author_insight` | `reported` | The passage explains the toxicology change as a response to an imminent local courtroom challenge. | Author's words, but about one episode: one upcoming court challenge and the unit's change; it says why that went as it did. FLAG: coded under the one-event rule; "propelled" is the author's causal reading, and without that rule I would have said author_insight. |
| V.93 | F93* | p. 626 | `author_insight` | `reported` | The passage generalizes from the described workflow to characterize toxicology work as standardized, instrument-based, and legally familiar. | Descriptive summary of the workflow just shown and of the legal parties' familiarity with the report. Note: the author's own summarising words; page says "instrumental and standardized", not "highly". |
| V.100 | F100* | p. 627 | `author_insight` | `reported` | The passage explains why the measurement-uncertainty demand fit toxicologists' existing work and values. | Gives toxicologists' reading of the one challenge, plus the fact that ASCLD already asked for the standard. FLAG: coded under the one-event rule; the wording is the author's analytic vocabulary. MISMATCH: page attributes the fit to how toxicologists "interpreted" it; description states the fit as fact. |
| V.104 | F104* | p. 628 | `author_insight` | `reported` | The passage interprets the anticipated court challenge as unusually immediate because it would reach an MCCL analyst directly. | Characterises one event: an MCCL analyst to be challenged personally in court. FLAG: one-event rule; "institutional pathway" is the author's label. MISMATCH: page says "very direct and immediate"; the description's "unusually" adds a comparison. |
| V.106 | F106* | p. 628 | `author_insight` | `reported` | The passage combines regional method differences, instrument outputs, and analyst concern into an interpretation of the narcotics debate. | States regional technique preferences, the community's agreement, and the analysts' worry. FLAG: "seen as compatible" and the worry are views in the author's voice. MISMATCH: page says the debate concerned them; description says the instrument output "made" them worry. |

## Stage B: sections 1 to 7

### 1. Direction

**All comparable links:** n = 293; raw agreement 0.918 (269 of 293); kappa 0.796 (95% interval 0.72 to 0.87).

**Links on directional claims:** n = 231; raw agreement 0.896 (207 of 231); kappa 0.778 (95% interval 0.70 to 0.85).

| coder 1 in rows, coder 2 in columns | `illustrates` | `with` | `against` | `qualifies` |
|---|---|---|---|---|
| `illustrates` | 209 | 13 | 0 | 2 |
| `with` | 0 | 58 | 0 | 1 |
| `against` | 0 | 0 | 0 | 0 |
| `qualifies` | 1 | 2 | 5 | 2 |

**Disagreements: 24.**

| row | fragment | claim | coder 1 | coder 2 | coder 1's basis | coder 2's reason |
|---|---|---|---|---|---|---|
| 1.21 | F44 | C02 | `illustrates` | `with` | The stub reports that a published legal commentary urged traditional forensic specialties to look to DNA typing as their model for making identification work more scientific. | Stub has legal commentators holding traditional specialties up against DNA typing: outside evaluation of neighbours. |
| 1.26 | F48 | C14 | `qualifies` | `illustrates` | The stub reports that the author's account is that DNA analysts themselves regarded profiling as judgment-laden and untidy because instrument output could contain artifacts and samples could be dirty, degraded, or contaminated. | Stub gives the analysts' own view of the process as untidy; nothing on how outsiders perceived the evidence. |
| 1.58 | F77 | C05 | `illustrates` | `with` | The stub reports that the author's account is that good firearms examiners prized pattern recognition, experience, and trained subjectivity and resisted reducing identification to standardized numerical rules. | Stub has examiners who prize trained subjectivity resisting standardised numerical rules: resistance where values conflict. |
| 1.60 | F77 | C16 | `illustrates` | `with` | The stub reports that the author's account is that good firearms examiners prized pattern recognition, experience, and trained subjectivity and resisted reducing identification to standardized numerical rules. | Stub has firearms examiners resisting a move to standardised numerical rules, alongside the subjective-judgement value. Thin: not said to be MCCL or DNA-driven. |
| 1.68 | F85 | C04 | `illustrates` | `with` | The stub reports that when the author questioned Tom and Pete together about the meaning of a DNA-like standard, they focused on statistics and objectivity, rejected percentage-style bullet matches, and said experience creates internal thresholds that outsiders distrust because firearms conclusions are not numerical. | Stub has examiners rejecting percentage-style matches and saying their conclusions are not numerical: no fit, no adaptation. Thin: "rejected" is a stance, not stated unworkability. |
| 1.72 | F86 | C04 | `illustrates` | `with` | The stub reports that the author's account is that creating a DNA-like statistical population for firearm marks made little sense to the MCCL examiners and would also depart sharply from their commitment to holistic subjective identification. | Stub says a DNA-like statistical population for firearm marks made little sense to the examiners: adaptation not workable where method does not fit. |
| 1.75 | F87 | C01 | `qualifies` | `with` | The stub reports that the paper explains that the firearms challenge arrived through socially and physically distant venues and, combined with incompatible technique and an affront to occupational values, led MCCL examiners to reject changing their practice. | Stub has a challenge reaching non-DNA examiners, who rejected changing practice. Coded on the printed direction (pressure); the practice itself did not move, which a "reshape" reading would count against. |
| 1.77 | F87 | C04 | `illustrates` | `with` | The stub reports that the paper explains that the firearms challenge arrived through socially and physically distant venues and, combined with incompatible technique and an affront to occupational values, led MCCL examiners to reject changing their practice. | Stub credits the rejection of change partly to incompatible technique. It reports rejection, not feasibility by name. |
| 1.82 | F89 | C02 | `illustrates` | `qualifies` | The stub reports that the NAS report did not criticize toxicology directly but did emphasize the importance of assessing analytic accuracy and estimating error rates. | Stub says the NAS report did not criticise toxicology directly, only stressed accuracy and error rates: it limits how far scrutiny reached this neighbour. |
| 1.105 | F98 | C01 | `with` | `qualifies` | The stub reports that before the NAS report, MCCL was already adapting to ISO 17025 and toxicology had a multi-year plan to estimate measurement uncertainty; when the local court challenge became imminent, the unit accelerated that plan and prepared the needed statistical analysis. | Stub has a court challenge speeding a change in a non-DNA unit, but places the plan before the NAS report, under ISO work: it limits what the change owes to the later pressure. |
| 1.162 | F123 | C04 | `illustrates` | `qualifies` | The stub reports that robin described a workshop about a Daubert challenge to crystal testing and said MCCL could not handle its caseload without crystals because the laboratory had only two relevant instruments and instrument runs took too long. | Stub says doing without crystals was not manageable because of two instruments and long runs: feasibility limited by capacity, not technique fit. The claim's own "unless" leaves room, so not against. |
| 1.179 | F129 | C01 | `qualifies` | `with` | The stub reports that the paper explains that MCCL narcotics analysts resisted more standardized DNA-like instrument work because it conflicted with their valued autonomy and variety, and the professional debate did not create an immediate need to change. | Stub has DNA-like work pressed on a non-DNA group, who resisted it. Coded on the printed direction (pressure); practice did not change and the stub says there was no immediate need. |
| 1.192 | F134 | C02 | `qualifies` | `against` | The stub reports that the author's account is that toxicology did not face a scientific-pathway challenge in the comparison summarized by the table. | Stub reports no scientific-route challenge to toxicology in the comparison: scrutiny absent where the claim has it rising. One group, one arena; qualifies considered. |
| 1.194 | F135 | C02 | `qualifies` | `against` | The stub reports that the author's account is that narcotics did not face a scientific-pathway challenge in the comparison summarized by the table. | Stub reports no scientific-route challenge to narcotics in the comparison: scrutiny absent in that arena. Qualifies considered. |
| 1.200 | F137 | C02 | `qualifies` | `against` | The stub reports that the author's account is that toxicology did not face a public-pathway challenge in the comparison summarized by the table. | Stub reports no public-route challenge to toxicology in the comparison: scrutiny absent in that arena. Qualifies considered. |
| 1.202 | F138 | C02 | `qualifies` | `against` | The stub reports that the author's account is that narcotics did not face a public-pathway challenge in the comparison summarized by the table. | Stub reports no public-route challenge to narcotics in the comparison: scrutiny absent in that arena. Qualifies considered. |
| 1.211 | F141 | C02 | `qualifies` | `against` | The stub reports that the author's account is that narcotics did not face a court-pathway challenge in the comparison summarized by the table. | Stub reports no court-route challenge to narcotics in the comparison: scrutiny absent in that arena. Qualifies considered. |
| 1.255 | F155 | C01 | `illustrates` | `with` | The stub reports that the paper explains that public scrutiny produced broad outsider challenges, attorney networks produced local courtroom pressure, and professional insiders used the comparison in internal debates, with those routes shaping both urgency and the form of workplace change. | Stub has challenges and pressure reaching the groups by three routes and shaping the form of workplace change. |
| 1.256 | F155 | C03 | `illustrates` | `with` | The stub reports that the paper explains that public scrutiny produced broad outsider challenges, attorney networks produced local courtroom pressure, and professional insiders used the comparison in internal debates, with those routes shaping both urgency and the form of workplace change. | Stub says the routes shaped urgency and the form of workplace change, with courtroom pressure the local one. Thin: it does not say which route produced more change. |
| 1.259 | F156 | C19 | `illustrates` | `with` | The stub reports that the author's account is that the NAS elevation of DNA triggered evaluation of forensic occupations that did not themselves use DNA technology. | Stub has spillover reaching forensic occupations that do not use DNA: outcome present, nothing said about overlap. |
| 1.274 | F164 | C03 | `illustrates` | `with` | The stub reports that the author's account is that direct courtroom exposure created a change opportunity for toxicologists, whereas MCCL firearms examiners lacked that local exposure and did not treat colleagues’ distant challenges as a pressing local problem. | Stub: direct courtroom exposure created a change opportunity for toxicologists; firearms, without it, saw no pressing local problem. |
| 1.276 | F164 | C17 | `illustrates` | `with` | The stub reports that the author's account is that direct courtroom exposure created a change opportunity for toxicologists, whereas MCCL firearms examiners lacked that local exposure and did not treat colleagues’ distant challenges as a pressing local problem. | Stub: direct courtroom exposure created a change opportunity for toxicologists. |
| 1.279 | F166 | C04 | `illustrates` | `with` | The stub reports that the author's account is that firearms resisted because both its technique and its commitment to holistic subjective judgment conflicted with the DNA comparison; narcotics resisted despite having a technically compatible instrument because craft and variety mattered; toxicologists changed because both technique and error-avoidance values fit the comparison. | Stub: misfit on technique with resistance, fit with change, and a compatible instrument blocked by values; matches the direction including its "unless". |
| 1.281 | F166 | C10 | `illustrates` | `with` | The stub reports that the author's account is that firearms resisted because both its technique and its commitment to holistic subjective judgment conflicted with the DNA comparison; narcotics resisted despite having a technically compatible instrument because craft and variety mattered; toxicologists changed because both technique and error-avoidance values fit the comparison. | Stub sets three different value commitments beside three different techniques. |

### 2. Core

**`core`:** n = 23; raw agreement 0.696 (16 of 23); kappa 0.309 (95% interval -0.14 to 0.70).

| coder 1 in rows, coder 2 in columns | `true` | `false` |
|---|---|---|
| `true` | 4 | 3 |
| `false` | 4 | 12 |

**Disagreements: 7.**

| row | claim | coder 1 | coder 2 | coder 2's reason |
|---|---|---|---|---|
| 2.2 | C02 | `false` | `true` | The first link: without DNA as benchmark drawing scrutiny onto the neighbours there is no spillover to trace. Close to being setup for C01; kept because the abstract states it as the thing explored. |
| 2.13 | C13 | `true` | `false` | A real finding (each group read the comparison differently) but it serves C04 and C05, and the abstract does not carry it. Considered true. |
| 2.16 | C16 | `false` | `true` | One leg of the three-case comparison (remote route, misfit on technique and values); the pathway and values arguments lose their contrast without it. Considered false as a case-level instance of C03 to C05. |
| 2.17 | C17 | `false` | `true` | The only case where practice changed; the comparison cannot be made without it. Same hesitation as C16. |
| 2.18 | C18 | `false` | `true` | The case that separates values from technique (compatible method, still no change); C04's limit and C05 rest on it. Same hesitation as C16. |
| 2.20 | C20 | `true` | `false` | An observation about the analytic split the paper makes; the argument that technique and values each mattered stands without it. A section heading names it, so considered true. |
| 2.21 | C21 | `true` | `false` | A contrast with the status and power literature drawn in one discussion passage; it positions the contribution, but the three-condition argument stands without it. Closest call on this tab. |

### 3. Stated as

**`stated_as`:** n = 23; raw agreement 1.000 (23 of 23); kappa 1.000 (95% interval 1.00 to 1.00; 1,975 of 2,000 resamples gave a kappa).

| coder 1 in rows, coder 2 in columns | `established` | `ventured` |
|---|---|---|
| `established` | 19 | 0 |
| `ventured` | 0 | 4 |

**Disagreements: 0.**

### 4. Gap kind

**`gap kind`:** n = 3; raw agreement 1.000 (3 of 3); kappa withheld (fewer than 10 judgements).

| coder 1 in rows, coder 2 in columns | `scope_limit` | `absent_evidence` | `unresolved_question` |
|---|---|---|---|
| `scope_limit` | 1 | 0 | 0 |
| `absent_evidence` | 0 | 1 | 0 |
| `unresolved_question` | 0 | 0 | 1 |

**Disagreements: 0.**

### 5. Pair drawn by authors

**`pair drawn_by_authors`:** n = 2; raw agreement 1.000 (2 of 2); kappa withheld (fewer than 10 judgements).

| coder 1 in rows, coder 2 in columns | `true` |
|---|---|
| `true` | 2 |

**Disagreements: 0.**

### 6. Resolution period

**`resolution_period`:** n = 1; raw agreement 1.000 (1 of 1); kappa withheld (fewer than 10 judgements).

| coder 1 in rows, coder 2 in columns | `none` |
|---|---|
| `none` | 1 |

**Disagreements: 0.**

### 7. Gloss relation

**`gloss_relation`:** n = 20; raw agreement 0.700 (14 of 20); kappa 0.318 (95% interval -0.10 to 0.70).

| coder 1 in rows, coder 2 in columns | `consistent` | `goes_beyond` |
|---|---|---|
| `consistent` | 11 | 1 |
| `goes_beyond` | 5 | 3 |

**Disagreements: 6.**

| row | fragment | coder 1 | coder 2 | coder 1's reason | coder 2's reason |
|---|---|---|---|---|---|
| 7.1 | F49 | `goes_beyond` | `consistent` | The event supports the contamination problem and a clean rerun, but the gloss additionally attributes the process to judgment. | Incident shows contamination that cleared on a re-run with no cause found; the "judgment" half is carried by the sentence it illustrates (F48), not by the incident. Nothing contradicted. |
| 7.2 | F51 | `goes_beyond` | `consistent` | The remark reports wider laboratory participation; calling that participation shared judgment adds an interpretive step without contradicting it. | A remark that a report takes the wider lab matches "shared judgment", given F50's account of reviewers and others joining the interpretation. |
| 7.8 | F80 | `consistent` | `goes_beyond` | The examiner explicitly used defense questioning as a reason to reconsider practice, supporting both the immediate and later glosses about motivation for change. | First part fits (use criticism to re-examine practice). The p. 635 part turns one speaker into examiners with hearing experience being "more motivated", which the fragment cannot carry. F79, same gathering, has a speaker who also spoke of testifying under the criticism responding defensively; both can still be true. |
| 7.14 | F114 | `goes_beyond` | `consistent` | Taylor's career story shows his own dislike of routine toxicology work, while the gloss generalizes that preference to the narcotics group. | Taylor's dislike of paperwork-heavy toxicology and his move to other work fit the preference F113 reports for the group. |
| 7.17 | F119 | `goes_beyond` | `consistent` | The meeting clearly shows concern with processing speed, while the gloss additionally positions efficiency alongside the unit's broader commitment to thorough analysis. | The meeting shows analysts pressing for speed; "alongside thorough analysis" is F120's neighbouring point, not a claim about this meeting. |
| 7.19 | F127 | `goes_beyond` | `consistent` | Taylor contrasts specialized crystal training with easy instrument operation; the gloss adds the broader meaning of that contrast for craft expertise and judgment. | Saying anyone can run the instrument while crystals need training is the craft contrast; the "threat" sits in the lead-in F126 more than in Taylor's words. Mild; nothing contradicted. |

## `against` in each coding

Every link coded `against` on a directional claim, as coded, whatever the voice of its fragment. An `against` on a claim that names no outcome is invalid by schema: the `against` check is never sent it and the audit never counts it, so it is counted in the last row and nowhere else.

|  | coder 1 | coder 2 |
|---|---|---|
| links coded `against`, on directional claims | 0 | 5 |
| claims with at least one | 0 | 1 |
| the most on one claim | 0 | 5 (C02) |
| claims with two or more | none | C02 |
| coded `against` on a claim that names no outcome: invalid by schema, and not counted above | 0 | 0 |

- Coder 1: none.
- Coder 2: F134→C02, F135→C02, F137→C02, F138→C02, F141→C02.
- Coded `against` by both: 0.

**With the links the `against` check flags counted as `illustrates`:**

|  | coder 1 | coder 2 |
|---|---|---|
| links coded `against`, on directional claims | 0 | 0 |
| claims with at least one | 0 | 0 |
| the most on one claim | 0 | 0 |
| claims with two or more | none | none |
| coded `against` on a claim that names no outcome: invalid by schema, and not counted above | 0 | 0 |
| links flagged (answered 4a to 4x) | 0: none | 5: F134→C02, F135→C02, F137→C02, F138→C02, F141→C02 |
| of them, answered 4a | 0 | 0 |

## The audit under each coding

Coder 1's column is the corpus with the extraction's sidecar. Coder 2's column is the corpus with coder 2's codes in place of coder 1's (direction, core, stated as, gap kind and resolution period) and with coder 2's voice codes. Whether a pair was drawn by the authors changes no figure in this table. Which claims are directional is the corpus's in both, because both codings of direction were made against the outcome and the direction the corpus records. The voice rule is applied in both: a `with` or `against` link from a fragment coded `author_insight` is left out, and counted in the row "left out by the voice rule".

|  | coder 1 | coder 2 |
|---|---|---|
| directional claims | 18 | 18 |
| `with` and `against` links counted | 13 and 0 | 18 and 0 |
| left out by the voice rule | 46 `with`, 0 `against` | 55 `with`, 5 `against` |
| claims assessed (at least 4 counted links) | 2 | 2 |
| coverage | 0.111 | 0.111 |
| seams | none | none |
| uniformity rate | not reported: coverage is under 0.60 | not reported: coverage is under 0.60 |
| moves parameterised | construct_inversion, counterfactual_ending, focalization_shift | construct_inversion, counterfactual_ending, focalization_shift |

**With the links the `against` check flags counted as `illustrates`:**

|  | coder 1 | coder 2 |
|---|---|---|
| directional claims | 18 | 18 |
| `with` and `against` links counted | 13 and 0 | 18 and 0 |
| left out by the voice rule | 46 `with`, 0 `against` | 55 `with`, 0 `against` |
| claims assessed (at least 4 counted links) | 2 | 2 |
| coverage | 0.111 | 0.111 |
| seams | none | none |
| uniformity rate | not reported: coverage is under 0.60 | not reported: coverage is under 0.60 |
| moves parameterised | construct_inversion, counterfactual_ending, focalization_shift | construct_inversion, counterfactual_ending, focalization_shift |

## What this log does not hold

- Whether the pinned predictions held. They are stated apart, in no file.
- The extraction's miss rate, which comes from the coverage check, and the hours.
- Any reconciliation. Disagreements are discussed only when every paper is coded.
