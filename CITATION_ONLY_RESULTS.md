# The citation-only run (T36): results

Written by `score_citation_only.py score` (sha256 opens f39c16cc) by `CITATION_ONLY_PLAN.md`, from the key `citation_only_key.json` (opens 6016fe30), the PI's sheet `citation_matching_sheet_filled.xlsx` (opens 96a35fac), checked against the blank `citation_matching_sheet.xlsx` (opens e1028686), and the four replies: `reply_58_bechky_citation_fable.json` (opens 4bd2224e), `reply_59_bechky_citation_astra.json` (opens 14ae4ba3), `reply_60_pratt_citation_fable.json` (opens afea2883), `reply_61_pratt_citation_astra.json` (opens 281145b1).

Described, not tested: the plan fixes no bar. The PI ran the chats and is not blind to the source of what the PI matched; the sheet did not say which chat wrote which reading. One run per model and paper. A point reached without the paper is available without the paper's text, from memory of the paper or of writing about it, or by inference from the citation and the field; the run cannot say which. Pratt's readings are matched to single readings, Bechky's to the PI's groups, so the two papers' figures are not alike in kind.

**Checks:** the blank sheet and the four replies are the key's, and all four replies count; no wager or what_you_know holds a quoted span of more than eight words; on the PI's sheet no cell outside the yellow ones changed, and every match reads.

## M1. The readings made without the paper

| paper | model | readings | placed with readings made with the paper | marked none, a new point |
|---|---|---|---|---|
| Bechky | Fable 5.1 (chat 58) | 5 | 3 | 2 |
| Bechky | GPT 6 Astra (chat 59) | 5 | 4 | 1 |
| Bechky | both | 10 | 7 | 3 |
| Pratt | Fable 5.1 (chat 60) | 5 | 3 | 2 |
| Pratt | GPT 6 Astra (chat 61) | 4 | 1 | 3 |
| Pratt | both | 9 | 4 | 5 |

## M2. Bechky: the PI's groups of 14 Oct reached without the paper

| the PI's group | readings made with the paper | found twice with the paper | reached by Fable 5.1 | reached by GPT 6 Astra |
|---|---|---|---|---|
| Verifiability | 2 |  | — | X10 |
| Capacity | 6 | yes | — | — |
| DNA Subjective | 1 |  | — | — |
| firearms already changed | 3 | yes | — | — |
| Different Demands | 2 | yes | — | — |
| Local Challenge | 2 |  | X06 | X05 |
| Power Competition | 1 |  | — | X07 |
| Staff Sorting | 4 | yes | — | — |
| Accreditation | 6 | yes | X08 | — |
| Status | 1 |  | X01 | X09 |

- **Reached by Fable 5.1:** 3 of 10 groups (Local Challenge, Accreditation, Status); of the 5 found twice with the paper, 1 (Accreditation).
- **Reached by GPT 6 Astra:** 4 of 10 groups (Verifiability, Local Challenge, Power Competition, Status); of the 5 found twice with the paper, 0.
- **Reached by either model:** 5 of 10 groups (Verifiability, Local Challenge, Power Competition, Accreditation, Status); of the 5 found twice with the paper, 1 (Accreditation).

## M3. Pratt: the readings made with the paper that have a counterpart without it

| arm | readings made with the paper | with a counterpart from Fable 5.1 | from GPT 6 Astra | from either |
|---|---|---|---|---|
| system | 5 | 0 | 1 | 1 |
| middle | 5 | 2 | 0 | 2 |
| plain | 5 | 2 | 0 | 2 |
| all | 15 | 4 | 1 | 5 |

Named: P03 (plain) by X17 (Fable 5.1); P04 (system) by X11 (GPT 6 Astra); P06 (middle) by X16 (Fable 5.1), X17 (Fable 5.1); P08 (middle) by X16 (Fable 5.1); P14 (plain) by X18 (Fable 5.1).

## M4. What each model says it knows of each paper

**Chat 58, Bechky, Fable 5.1:**

> I know this paper at the level of its argument: an ethnography of a U.S. crime laboratory showing that the rise of DNA analysis, with its probabilistic match statistics and protocol-driven work, changed the standards by which courts, lawyers, and scientific critics judged the comparison disciplines (latent prints, firearms/toolmarks, trace and the like), a condition practitioners called 'DNA envy,' and that examiners in those disciplines altered their testimony, documentation and verification, and interpretive caution in response, which Bechky names an evaluative spillover from technological change, a route by which a technology reshapes occupations that never adopt it. I am fairly confident of the thesis and the broad shape of the findings but not of page placement; the pages below are reconstructed from the article's span (theory early, methods around 613-616, findings through the late 610s to early 630s, discussion from the mid-630s) and should be read as approximate.

**Chat 59, Bechky, GPT 6 Astra:**

> I know the citation and infer from its title that the article examines how DNA's standing as a forensic technology affects practices in other forensic occupations. I do not reliably recall the paper's empirical passages, its particular findings, or their page numbers, so the readings below are explicitly conditional wagers rather than claims about what its text actually documents; I cannot establish what observations it prints or what passages contradict them.

**Chat 60, Pratt, Fable 5.1:**

> I know this paper fairly well: an ethnography of Amway distributors (participant observation over roughly three years, interviews with current and former distributors, analysis of the tapes and literature) that coins sensebreaking, pairs it with sensegiving, and argues that one identification programme yields identification, disidentification, or ambivalent identification depending on how much sense is broken and how coherently it is re-given. I am confident about the argument and the named practices (dream building, positive programming, encapsulation or seclusion, upline mentoring) and much less sure of exact page numbers, which below are my estimates within 456-493, and of specifics such as interview counts.

**Chat 61, Pratt, GPT 6 Astra:**

> I know the paper's subject at a general level: organizational identification and ambivalence among Amway distributors, including the possibility of simultaneous attraction to and distance from an organization. I do not reliably remember its passages, observations, or journal page locations; the readings below are conditional wagers, not claims that I have verified the paper's evidence.

## The readings made without the paper, and the PI's matches

**X01** (Bechky, chat 58, Fable 5.1, its reading 2, `reading_id` R2). **Match:** Status. **Note:** Similar to M12 (the responses are moves for standing and resources inside the lab.)

'DNA envy' is literally envy: a story of status and resources inside the laboratory. Federal backlog money, hires with graduate degrees, new space, and management attention flowed to DNA, while apprenticeship-trained pattern examiners experienced relative decline. The practice changes are status-repair projects (science talk, certification, verification rituals) aimed at recovering standing with lab leadership, peers, and funders; the courtroom is a secondary stage. The evaluative standard is the vehicle, but the process is stratification within one organization.

**X02** (Bechky, chat 58, Fable 5.1, its reading 3, `reading_id` R3). **Match:** none. **Note:** No group contests the pathway factor with the formalizability of each craft’s knowledge

Differences in how the pattern disciplines responded are explained by how far each body of knowledge could be formalized, not by how hard DNA-based evaluation hit them. Latent prints, with a named method, automated search databases, and emerging error-rate studies, moved toward quantification; firearms and toolmark examiners defended experiential judgment; trace evidence contracted. DNA set the vocabulary, but the fault line was the epistemic structure of each craft, whether it had a population-level reference to compute against. The spillover reorganized a standing craft-versus-science divide rather than creating new pressure.

**X03** (Bechky, chat 58, Fable 5.1, its reading 5, `reading_id` R5). **Match:** none. **Note:** ceremonial change, decoupled from bench practice, noone makes it. 

The spillover produced ceremonial, front-stage change while bench practice stayed as it was. Hedged testimony, new report phrases, and verification sign-offs satisfied lawyers and management, but examiners kept reaching conclusions the way they always had. What the paper reads as changed occupational practice is a decoupled layer of accountability work; the craft persisted beneath it, and the envy was managed rather than resolved.

**X04** (Bechky, chat 59, GPT 6 Astra, its reading 4, `reading_id` R4). **Match:** none. **Note:** No group contests status imitation reading that the paper does not make

So-called envy could conceal genuine epistemic reform. The contrast with DNA might prompt practitioners in other forensic fields to revisit error, uncertainty, and the limits of expert judgment. The alternative story is not one of status imitation but of learning from a technology that exposes weaknesses in established occupational habits; losing prestige could make better science possible.

**X05** (Bechky, chat 59, GPT 6 Astra, its reading 2, `reading_id` R2). **Match:** Local Challenge. **Note:** weak form of M07/ M25; of course some differences (different level)

The spillover may travel mainly through courtroom expectations rather than through admiration among scientists. Once DNA establishes a powerful image of forensic certainty, prosecutors, defense attorneys, and judges may demand that unrelated forensic techniques be reported and defended in comparable terms. The occupation's changed practice would then be an adaptation to a new legal audience, not simply a change in its own beliefs about good science.

**X06** (Bechky, chat 58, Fable 5.1, its reading 1, `reading_id` R1). **Match:** Local Challenge. **Note:** Similar alternative of M07/m25

The practice changes track the activation of a legal audience, not DNA technology as such. Post-conviction exonerations, the 2009 National Academy of Sciences report, Daubert-style admissibility fights, and the 2009 Melendez-Diaz ruling forcing analysts onto the stand all intensified adversarial scrutiny of forensic testimony in the same years. DNA supplied lawyers with an idiom (error rates, match probabilities), but the cause was the courtroom's changed demands. Had the same scrutiny arrived with a different emblem, the same hedging, documentation, and verification would have followed, and the spillover runs from the legal field to the lab, with the technology as vocabulary rather than trigger.

**X07** (Bechky, chat 59, GPT 6 Astra, its reading 5, `reading_id` R5). **Match:** Power Competition. **Note:** Same claim contested (status and power matter less) and the same kind of alternative as M08.

The deeper story might be an internal struggle over occupational jurisdiction. DNA's ascent could unsettle who gets to define a forensic conclusion, which specialists control a case, and how technicians, analysts, and investigators divide expertise. Apparent changes in technique may be moves in negotiations over authority and task ownership rather than direct spillovers of one technology's evaluative standard.

**X08** (Bechky, chat 58, Fable 5.1, its reading 4, `reading_id` R4). **Match:** Accreditation. **Note:** Same alternative as M10, M15, M22–M24, M28 (change is an accreditation/quality-management step)

The documentation, verification, and reporting changes diffused through accreditation and quality management (ASCLD/LAB and ISO/IEC 17025 regimes, and the FBI's quality standards for DNA tied to database access), carried by quality managers and lab directors. DNA's quality regime became the lab-wide template because it was the one federally mandated one; the pattern units' new routines are regulatory isomorphism administered from the top, and 'DNA envy' is the shop-floor name for a management-driven change. The mechanism is organizational diffusion of rules, not courtroom evaluation of expertise.

**X09** (Bechky, chat 59, GPT 6 Astra, its reading 1, `reading_id` R1). **Match:** Status. **Note:** X09 stresses resources (staff, equipment, cases) where M12 stresses rank and irreplaceability; M12 itself opens with envy of DNA’s equipment, money and staff.

What looks like occupational emulation of DNA might instead be competition over scarce organizational resources. Forensic specialists may adopt DNA-like routines because supervisors, funders, or investigators channel staff, equipment, and desirable cases toward practices they regard as modern and reliable. On this reading, changes in practice are strategic bids for institutional support, with epistemic improvement a possible by-product rather than the original motive.

**X10** (Bechky, chat 59, GPT 6 Astra, its reading 3, `reading_id` R3). **Match:** Verifiability. **Note:** Same alternative as M01/M17

The consequential change may be in how forensic knowledge is made legible, not primarily in how material traces are examined. DNA's apparent clarity could encourage other specialties to adopt standardized reports, calibrated claims, or numerical presentations, making unlike kinds of evidence look comparable. That would be a story of commensuration: the presentation format becomes an authority-producing technology in its own right, even where the underlying inferences remain different.

**X11** (Pratt, chat 61, GPT 6 Astra, its reading 4, `reading_id` R4). **Match:** P04. **Note:** Both dissolve “ambivalent” as a member type into audience-bound conduct

The contradictory identifications may reside less in enduring inner attitudes than in the different explanations distributors must give to different audiences. One account of membership is persuasive among recruits or fellow distributors; another is needed with skeptical relatives or friends. Ambivalence would then be something accomplished in conversations to sustain credibility across incompatible audiences.

**X12** (Pratt, chat 60, Fable 5.1, its reading 5, `reading_id` R5). **Match:** none. **Note:** no P reading makes it

The organization teaches a transferable technique: dismantle a taken-for-granted identity (the job, the broke friend, the negative relative) by setting it beside a dream and naming the gap. The technique is not organization-specific, and disidentifiers are not people in whom sensegiving failed but people who learned sensebreaking well and turned it on the system itself, with the tools business as the real business and the upline as the real customer. Their exit narratives mirror the plan, inverted. Ambivalents are those who have half-applied the technique and cannot settle which object to break. Encapsulation and the policing of anything negative are the organization's own acknowledgment that what it teaches is reversible.

**X13** (Pratt, chat 60, Fable 5.1, its reading 3, `reading_id` R3). **Match:** none. **Note:** no P reading makes it

The object of identification in the data is a line of sponsorship and a mentor, not Amway. The corporation is a distant licensor; the upline organization runs the meetings, sells the tools, and does the counseling. On this reading the three valences are not three attitudes toward one object but splits across objects: people identify with their upline and the community while disliking the corporation's products or prices; or embrace the products and the free-enterprise ideal while rejecting the tools business. Ambivalence is the residue produced when a multi-target structure is pushed through a single-target typology, and disidentification is often loyalty to one target expressed as rejection of another.

**X14** (Pratt, chat 61, GPT 6 Astra, its reading 2, `reading_id` R2). **Match:** none. **Note:** Close to P12 but P12’s point is that the types are stances toward a ledger, contesting the money ruling-out (p. 463), which X14 does not contest.

Distributors' mixed identification may be a sensible way to manage an uncertain economic commitment. Expressing belief in the opportunity sustains selling and recruitment, while maintaining doubts preserves a story about oneself that can survive disappointment or departure. Ambivalence then functions as a practical hedge, not simply an uncomfortable identity state to be resolved.

**X15** (Pratt, chat 61, GPT 6 Astra, its reading 3, `reading_id` R3). **Match:** none. **Note:** no P reading makes it. Although P01 shares the idea that outsiders help build the boundary, but its main point is sorting by the audience’s valence

Negative public judgments of Amway may not merely threaten distributors' identification; they may help produce its intensity. Being treated as outsiders can give members a shared grievance and a reason to trust insiders more than nonmembers. On this reading, the apparent opposition between attraction and aversion is part of a boundary-making cycle through which criticism from outside strengthens commitment inside.

**X16** (Pratt, chat 60, Fable 5.1, its reading 2, `reading_id` R2). **Match:** P08, P06. **Note:** Same claim contested with same alternative

The three outcomes are an economic exposure map. The system of tapes, books, functions and counseling is itself a business sold to distributors by their uplines, so a distributor's attitude to Amway tracks their net position in two markets at once. Identification is found among those whose position is positive or visibly improving (a Diamond upline, growing legs); ambivalence is the state of people who have sunk real money and time without return and cannot yet write it off; disidentification is the response of those who conclude that they, not the soap, were the product. What Pratt calls the meaning void is dissonance over unrecouped investment, and what he calls sensegiving works mainly by raising the cost of exit.

**X17** (Pratt, chat 60, Fable 5.1, its reading 1, `reading_id` R1). **Match:** P03, P06. **Note:** Same alternative

The void Pratt attributes to dream building is largely imported. The sample is skewed toward people who were already discontented (the paper's own seekers) or who were susceptible to a pitch promising a different life, and the organization's work is less to break sense than to recognize an existing fracture and hand it a vocabulary. On this reading the three outcomes track pre-entry condition rather than organizational practice: entrants with a sharp, specific grievance against their job identify; those with a diffuse unease become ambivalent; those brought in by a spouse or friend, with no void of their own, disidentify or drift out. Sensebreaking is a sorting device that reveals who arrived broken, not a treatment that breaks.

**X18** (Pratt, chat 60, Fable 5.1, its reading 4, `reading_id` R4). **Match:** P14. **Note:** Same point. 

The outcomes are stages of one career rather than types of member. Nearly everyone is identified in the months after sensegiving; ambivalence sets in as results lag behind the dream while the system's demands continue; disidentification, or a quiet fading out, follows at or after exit. Cross-sectional sampling of current members at different tenures, together with retrospective ex-members, freezes a sequence into a taxonomy. On this reading the organization's practices explain the first stage well and the others hardly at all; time in grade does the rest, and the repeated weekly and quarterly sensegiving is best understood as a machine for re-identifying people who are drifting down the sequence.

**X19** (Pratt, chat 61, GPT 6 Astra, its reading 1, `reading_id` R1). **Match:** none. **Note:** no P reading makes it

What looks like ambivalence toward one organization may be a mismatch between the organizations a distributor has in mind. A person can feel loyal to a sponsor, immediate distributor group, or imagined entrepreneurial community while mistrusting Amway as a corporate name. On this reading, the central process is switching among identification targets, rather than managing two opposing feelings about a single target.

---

*Notes added below the scorer's output on 16 Oct; the text above is the scorer's, unchanged.*

**How a match is read.** The PI judged the readings made with the paper much more substantiated than those made from the citation alone, though they share themes. Read with the plan, a match is on the point, the same claim contested with the same alternative, not on the substance. A reading made with the paper that shares its point with one made from the citation alone is flagged as available without the paper's text, and keeps its standing on its own evidence. The PI's notes also grade some matches, for instance as a weak form of a group's point.

**Checked independently.** From the plan, the key, the blank and the filled sheet, the four replies, `matching_results.json`, stage2/markers/KEY.json and these results, every figure was worked out again with separate code: the filled sheet against the blank, the key against the replies, M1 to M4, and each reading's match and note. **All agree.** Besides, seven of the Pratt cells were typed loosely (two P numbers in lower case, five "none" with a space after it), which the scorer's rules read as written, and the workbook was saved again in Excel, which changed formats and two row heights but no value.
