# The completeness test (T38): the results

Written by `score_completeness_test.py score`, as `COMPLETENESS_TEST_PLAN.md` fixes the measures. The key's sha256 is f45cb6c49213d9b383cab572819d847684bf522db6902bf34d471a7b6e561e4d; the lists key's 5f930c46b59d8daff8def75b767f73201042a5b793592ab9f3a3d75f1c3cb836.

## The replies

- **chat 68, Bechky, the checker:** reply_68_bechky_check_opus.json, sha256 b615d3a3ba914a022541e4fa9be9dbca2182b0c0b76c2984ac902778564afa1b: counts.
- **chat 69, Pratt, the checker:** reply_69_pratt_check_opus.json, sha256 2a854382b1d99e79a4e405b76a9a31a2283ad762e826577e5ac32a8d602be450: counts.
- **chat 70, Bechky, the matcher:** reply_70_bechky_ready_test_opus.json, sha256 46b44b27f6f665c7c201c96879298d17455389b1beb7af9a1436f2239e3f1cc9: counts.
- **chat 71, Bechky, the judge:** reply_71_bechky_judge_argon.json, sha256 8a85e52abe9c23bd190d47132c61234003dd0d8e81677b439dba0599efe666dd: counts.
- **chat 72, Pratt, the judge:** reply_72_pratt_judge_argon.json, sha256 c6a1bb2a09b1a068999e0cb7733fc896b5d9955efea3164e856dbe1c53e6f5bd: counts.

## M1. The PI's passages that the checker lists

By the judge's pairs. Confirmed: those from which the coverage chat added a record.

| | the PI's passages | listed by the checker | confirmed | confirmed, listed |
|---|---|---|---|---|
| Bechky | 15 | 8 | 4 | 2 |
| Pratt | 14 | 12 | 10 | 9 |
| both papers | 29 | 20 | 14 | 11 |

## M2. The checker's lines, and what the judge says of them

| | lines | paired with the PI's | miss | covered | not in the brief | not found | unpaired | unpaired, miss |
|---|---|---|---|---|---|---|---|---|
| Bechky | 13 | 8 | 5 | 2 | 6 | 0 | 5 | 0 |
| Pratt | 19 | 12 | 3 | 14 | 2 | 0 | 7 | 0 |
| both papers | 32 | 20 | 8 | 16 | 8 | 0 | 12 | 0 |

A miss is a verdict of evidence, assertion or both. By verdict, on all the checker's lines:

- Bechky: evidence 2, assertion 3, both 0, covered 2, not_in_brief 6, not_found 0
- Pratt: evidence 1, assertion 2, both 0, covered 14, not_in_brief 2, not_found 0
- both papers: evidence 3, assertion 5, both 0, covered 16, not_in_brief 8, not_found 0

## M3. The ready test: the PI's Bechky passages in the second extraction (list Q)

By the matcher: found 15 of 15; with a passage of list Q 12 of 15; with a claim of list Q 11 of 15; with either 15 of 15. Of the 4 confirmed, with either: 4.

## M4. Described: the judge against the coverage chats, on the PI's passages

| | n | miss, added | miss, not added | not a miss, added | not a miss, not added | raw | kappa | not found, left out |
|---|---|---|---|---|---|---|---|---|
| Bechky | 15 | 2 | 8 | 2 | 3 | 0.333 | -0.154 | 0 |
| Pratt | 14 | 3 | 0 | 7 | 4 | 0.500 | 0.197 | 0 |
| both papers | 29 | 5 | 8 | 9 | 7 | 0.414 | -0.177 | 0 |

## M5. Described

**Bechky.**

- The judge's verdicts on the PI's lines: evidence 2, assertion 8, both 0, covered 4, not_in_brief 1, not_found 0.
- On the checker's: evidence 2, assertion 3, both 0, covered 2, not_in_brief 6, not_found 0.
- The checker's tests: evidence 10, assertion 3, both 0.
- Kinds of place, the PI's: footnote 2, paragraph 12, table 1; the checker's: figure 5, footnote 2, paragraph 5, table 1.
- Pages, the PI's: 606, 607, 608, 609, 610, 611, 612, 621, 622, 623, 633, 636, 637, 638; the checker's: 606, 607, 608, 609, 611, 612, 618, 621, 629, 630, 633, 637, 638.

**Pratt.**

- The judge's verdicts on the PI's lines: evidence 1, assertion 2, both 0, covered 9, not_in_brief 2, not_found 0.
- On the checker's: evidence 1, assertion 2, both 0, covered 14, not_in_brief 2, not_found 0.
- The checker's tests: evidence 11, assertion 8, both 0.
- Kinds of place, the PI's: figure 1, footnote 3, paragraph 10; the checker's: footnote 4, paragraph 15.
- Pages, the PI's: 459, 460, 461, 464, 465, 466, 467, 471, 473, 477, 478, 479, 481, 482, 486, 487; the checker's: 458, 459, 460, 461, 464, 465, 466, 467, 469, 470, 473, 474, 477, 478, 479, 480, 481, 482, 486, 487.

## Each line

No reason of any chat is printed. A line's id is its id in the judges' file; the PI's are H01 onward in the key, the checker's are numbered as it numbered them.

### Bechky

| id | whose | place | records added / test | pairs | verdict | matcher |
|---|---|---|---|---|---|---|
| A01 | the PI's H01 | pp. 606–607, the paragraph that runs over the page | none | B01 | assertion | L01: QP001, QC06 |
| A02 | the PI's H02 | p. 607, second full paragraph | none | — | assertion | L02: QP006 |
| A03 | the PI's H03 | p. 608, first full paragraph | none | B02 | assertion | L03: QP007, QP008, QC06 |
| A04 | the PI's H04 | p. 609, third full paragraph | none | B03 | assertion | L04: QP016 |
| A05 | the PI's H05 | p. 610, the paragraph above the subheading | none | — | assertion | L05: QC05 |
| A06 | the PI's H06 | pp. 610–611, the paragraph that runs over the page | none | — | assertion | L06: QP022, QC10 |
| A07 | the PI's H07 | p. 611, first full paragraph | none | — | assertion | L07: QP009, QP023, QP024, QC10, QC11 |
| A08 | the PI's H08 | pp. 611–612, the paragraph that runs over the page | F169 | B04 | covered | L08: QC12 |
| A09 | the PI's H09 | p. 612, footnote 1 | F170 | B05 | evidence | L09: QP025 |
| A10 | the PI's H10 | p. 621, footnote 4 | none | B09 | not_in_brief | L10: QP084 |
| A11 | the PI's H11 | pp. 622–623, the paragraph that runs over the page | F171 | — | covered | L11: QP090, QP091, QP092, QC24 |
| A12 | the PI's H12 | p. 633, Table 2, row "Values", column "Toxicology" | none | B12 | evidence | L12: QP161, QP163, QC29 |
| A13 | the PI's H13 | p. 636, third full paragraph | F172 | — | assertion | L13: QC03 |
| A14 | the PI's H14 | pp. 637–638, the paragraph that runs over the page | none | B13 | covered | L14: QP167, QC38 |
| A15 | the PI's H15 | p. 638, first full paragraph | none | — | covered | L15: QP168, QC01, QC39 |
| B01 | checker 1 | pp. 606–607, the paragraph that runs over the page | assertion | A01 | assertion |  |
| B02 | checker 2 | p. 608, first full paragraph | assertion | A03 | assertion |  |
| B03 | checker 3 | p. 609, third full paragraph | assertion | A04 | assertion |  |
| B04 | checker 4 | pp. 611–612, the paragraph that runs over the page | evidence | A08 | covered |  |
| B05 | checker 5 | p. 612, footnote 1 | evidence | A09 | evidence |  |
| B06 | checker 6 | p. 618, Figure 1 | evidence | — | not_in_brief |  |
| B07 | checker 7 | p. 618, Figure 2 | evidence | — | not_in_brief |  |
| B08 | checker 8 | p. 621, Figure 3 | evidence | — | not_in_brief |  |
| B09 | checker 9 | p. 621, footnote 4 | evidence | A10 | not_in_brief |  |
| B10 | checker 10 | p. 629, Figure 4 | evidence | — | not_in_brief |  |
| B11 | checker 11 | p. 630, Figure 5 | evidence | — | not_in_brief |  |
| B12 | checker 12 | p. 633, Table 2, Values row, Toxicology column | evidence | A12 | evidence |  |
| B13 | checker 13 | pp. 637–638, the paragraph that runs over the page | evidence | A14 | covered |  |

### Pratt

| id | whose | place | records added / test | pairs | verdict | matcher |
|---|---|---|---|---|---|---|
| A01 | the PI's H01 | p. 459, third full paragraph | F122 | B02 | not_in_brief |  |
| A02 | the PI's H02 | p. 460, footnote 6 | C53 | B05 | not_in_brief |  |
| A03 | the PI's H03 | p. 461, second full paragraph | F123 | B06 | evidence |  |
| A04 | the PI's H04 | pp. 464–465, the paragraph that runs over the page | none | B07 | covered |  |
| A05 | the PI's H05 | p. 466, second full paragraph | none | B08 | covered |  |
| A06 | the PI's H06 | p. 467, footnote 11 | C54 | B09 | assertion |  |
| A07 | the PI's H07 | p. 471, first full paragraph | none | — | covered |  |
| A08 | the PI's H08 | p. 473, footnote 13 | C55 | B11 | covered |  |
| A09 | the PI's H09 | p. 477, first full paragraph | F124, C56 | B13 | covered |  |
| A10 | the PI's H10 | p. 478, first full paragraph | F125, C57 | B14 | covered |  |
| A11 | the PI's H11 | p. 479, first full paragraph | C58 | B15 | covered |  |
| A12 | the PI's H12 | pp. 481–482, the paragraph that runs over the page | C59 | B17 | assertion |  |
| A13 | the PI's H13 | p. 482, Figure 2 | C60 | — | covered |  |
| A14 | the PI's H14 | pp. 486–487, the paragraph that runs over the page | none | B19 | covered |  |
| B01 | checker 1 | p. 458, second full paragraph | evidence | — | covered |  |
| B02 | checker 2 | p. 459, third full paragraph | evidence | A01 | not_in_brief |  |
| B03 | checker 3 | p. 460, second full paragraph | assertion | — | covered |  |
| B04 | checker 4 | p. 460, footnote 5 | evidence | — | covered |  |
| B05 | checker 5 | p. 460, footnote 6 | assertion | A02 | not_in_brief |  |
| B06 | checker 6 | p. 461, second full paragraph | evidence | A03 | evidence |  |
| B07 | checker 7 | pp. 464–465, the paragraph that runs over the page | assertion | A04 | covered |  |
| B08 | checker 8 | p. 466, second full paragraph | evidence | A05 | covered |  |
| B09 | checker 9 | p. 467, footnote 11 | assertion | A06 | assertion |  |
| B10 | checker 10 | pp. 469–470, the paragraph that runs over the page | evidence | — | covered |  |
| B11 | checker 11 | p. 473, footnote 13 | assertion | A08 | covered |  |
| B12 | checker 12 | p. 474, first full paragraph | evidence | — | covered |  |
| B13 | checker 13 | p. 477, first full paragraph | evidence | A09 | covered |  |
| B14 | checker 14 | p. 478, first full paragraph | evidence | A10 | covered |  |
| B15 | checker 15 | p. 479, first full paragraph | assertion | A11 | covered |  |
| B16 | checker 16 | pp. 480–481, the paragraph that runs over the page | evidence | — | covered |  |
| B17 | checker 17 | pp. 481–482, the paragraph that runs over the page | assertion | A12 | assertion |  |
| B18 | checker 18 | p. 486, first full paragraph | assertion | — | covered |  |
| B19 | checker 19 | pp. 486–487, the paragraph that runs over the page | evidence | A14 | covered |  |

---

*Notes added below the scorer's output on 17 Oct; the text above is the scorer's, unchanged.*

**The chats.** Chats 68, 69 and 70 (Opus 5.5 at Extra) ran as the steps say, side by side, in about three minutes; chats 71 and 72 (Gemini 4 Argon at Thinking Level High) ran as the steps say, six minutes each. No window showed a search. The PI's own coverage checks of 7 and 8 Oct took about 3.5 hours a paper; the plan's M5 puts the chats' times beside that, and the scorer, which reads no times, gives them here.

**Checked independently.** From the plan, a written statement of the scorer's definitions (not its code), the key, the lists key, the five replies and these results, every figure was recomputed with separate code: all 1,176 items compared agree (the hashes, the 278 figures of M1 to M5 in the JSON and here, and the 61 rows of each line), and 458 checks of the inputs pass (the lists key against the key and the checkers' replies, the judges' pairs and verdicts, the matcher's lines, the draw).

**Described, from the tables and the replies** (each counted by script first):
- **Pairing came down to the same place.** On 19 of the 20 pairs the two lines name their place in the same words, since the checker wrote its places in the forms of the PI's steps; the one exception is Bechky's cell of Table 2 (A12 and B12). No line is in two pairs. So M1 counts the places the two lists share, and the judge's pairing was hardly tested.
- **The judge judged each paired passage once.** On all 20 pairs it gave the two lines the same verdict, the same ids and the same reason word for word. So the verdict counts of M2 and M5 hold each paired passage once in each list, and all 8 of the checker's lines that the judge calls a miss are paired with one of the PI's.
- **None of the checker's 12 unpaired lines is judged a miss.** Bechky's five are Figures 1 to 5, which the judge calls exhibits taken from other sources, outside the brief; Pratt's seven it calls covered by the sheet.
- **The judge and the coverage chats lean opposite ways (M4).** On Bechky the judge calls 10 of the PI's 15 passages a miss, 8 of them assertions that no claim states, among them all seven of pp. 606–611, from which the coverage chat had added nothing, reading them as prior literature or as claims already recorded; and it calls covered two passages from which the coverage chat added fragments (pp. 611–612, F169; pp. 622–623, F171). On Pratt it calls 3 of the PI's 14 a miss, and calls covered (5) or outside the brief (2) seven passages from which the coverage chat added records. Pooled, chance agreement is about 0.50, so the kappa for both papers together, −0.177, is not a summary of the two; with 15 and 14 lines every kappa here is unsteady. M4 also sets aside the kind of record: Bechky's coverage chat added fragments only.
- **The ready test.** "Found" in M3 means that the matcher located the passage in the paper. It names an item of list Q for all 15 of the PI's Bechky passages, for three of them a claim alone (L05, L08, L13); of the four confirmed, two by passages and two by a claim alone. Nothing checks the matcher's choices.
- **Pratt's Figure 2.** The coverage chat's log places C59 at Figure 2 as well as at pp. 481–482; the key gives it to the line of pp. 481–482 alone, as the log's decision lines do, and the line of Figure 2 has C60 either way. At Figure 2 the coverage chat also rewrote the stub of F109, a change and not an addition, which the sheet the chats had does not show.

---

*A second note, added on 17 Oct: how the judge could read the brief otherwise than the coverage chats did, and whether it reads badly or the brief allows more than one reading. Counted by script from `completeness_key.json`, `completeness_lists_key.json` and the replies of chats 68, 69, 71 and 72; read against `EXTRACTION_BRIEF.md`, `JUDGE_MISSES.md`, the two sheets, the two coverage chats' logs, corpora and steps, and the first returns' logs. No paper was read for it: it rests on what the readers wrote about the passages. The text above is unchanged.*

**In short.** Of the 17 of the PI's passages on which the judge and the coverage chats part, 13 turn on what the extraction brief or the judge's task leaves open; the clear slips are two each, the judge's and the coverage chats'. Nothing in the files shows the judge misdescribing what a passage prints; on one passage (Pratt footnote 6) it reads what the passage asserts otherwise than the other two readers.

**Three readers on the PI's passages.** The judge (Gemini 4 Argon, chats 71 and 72); the coverage chats, whose decisions the key records, with their reasons in the section "Coverage additions" of their logs; and the checker (Opus 5.5, chats 68 and 69), which had the paper, the sheet and the brief, but not the PI's list, the coverage chats' records or the first returns' logs. Their footing differed. The coverage chats had the first return's corpus, voice file and log, not the sheet, and their message told them that a coverage check had found these passages and asked them to extract them; the judge's task told it that a line's place on a list says nothing about its verdict. Pratt's coverage chat ran on GPT-6, not on the model that extracted Pratt (`PRATT_COVERAGE_SEND.md`). On 17 of the PI's 29 passages the judge (a miss or not) and the coverage chats (a record added or not) part: Bechky 10 of 15, Pratt 7 of 14. On those 17 the checker's list (a line of its paired with the PI's) agrees with the judge on 6 and with the coverage chats on 11 (Bechky 5 and 5, Pratt 1 and 6); on 6 of the 17 it agrees only by not listing the passage (2 with the judge, 4 with the coverage chats).

**What each of the 17 turns on,** as grouped independently:
- **Points the extraction brief, or the judge's task, leaves open (11).**
  - *How finely to count a claim* (Bechky pp. 606–607, 607, 608, 610, 610–611 and 611): the coverage chat matched each paragraph to a claim already recorded (C01, C03, C06, C10, C11), on pp. 607 and 611 answering one point and passing over others; the judge found in each a relation that no claim states, as the checker did on pp. 606–607 and 608 (C06's statement names no occupations arising or disappearing). The brief's call to over-collect, and its rule that a new outcome or condition makes a new claim, lean the judge's way on pp. 606–608. Its rule that, for a claim with no outcome, a sentence spelling out one of its steps adds no claim can lean the coverage chat's way on p. 610 and p. 611, where it named C11, which has no outcome; on pp. 610–611 it named C03, which has one.
  - *The reach of the attribution test* (Pratt footnote 6 and Figure 2): whether a premise taken from earlier studies to set the fieldwork's length, or routes that a framework figure draws as extensions from other literatures, are the paper's own claims. On footnote 6 the judge read the premise as cited only, and also called the footnote a matter of method; the checker and the coverage chat read it as adopted (C53). The brief sends the methods section's facts to `fieldwork_scale` but sets no claim about method aside, and the index holds three (C46 to C48); since the paper builds on the premise, the test leans toward a claim. On Figure 2 the coverage chat added a claim (C60) and rewrote the stub of F109; the judge called the figure covered by F109, C01 and C30, none of which, as the sheet gives them, states those routes; the checker did not list it.
  - *Facts taken from other publications* (Pratt pp. 459 and 477): the brief does not say whether they are the paper's evidence. The judge left them out. So had the first returns on these passages, as their logs say (Bechky: Figures 1 to 5, footnote 4 and the literature review's background citations; Pratt: the cited background of pp. 458–460, and the outside turnover estimate, which serves only as the ground of absence A03); the coverage chats had those logs, the judge and the checker did not. It is no general rule of the first returns: Bechky's set footnotes 1 to 4 aside as context, though the judge called footnote 1 evidence, and Pratt's records facts about the firm, some from its own publications (F13, F24, F25), where the paper presents them as features of the setting. The checker and Pratt's coverage chat put them in (F122, F124); Pratt's coverage chat also added a claim at p. 477 (C56, on turnover) that neither the judge nor the checker names, and it left out the outside examples of pp. 486–487, as Bechky's left out those of pp. 637–638.
  - *Fragment or claim* (Pratt footnote 13): the author's generalization is on the sheet as a fragment (F70); the coverage chat added a claim (C55); the checker saw a further point, the contrast with social identity theory. The judge's task calls a passage covered when its content already stands on the sheet, whether in fragments or in claims, and a miss by assertion when no claim states it: here the two definitions pull apart. The sheet often pairs such a fragment with a claim (F40 and C15, F77 and C24, F78 and C25).
- **How fine a fragment should be (2):** Bechky pp. 611–612 (that forensic scientists work under the [6 words of Bechky (2020), p. 611]: F169 of the coverage chat) and pp. 622–623 (how the CMS method counts marks and sets its thresholds: F171). The judge took as enough the records it named, F03 on p. 612 with F01 (p. 607), F32, F37 and F39 (p. 616) and C02; and F71 and F72 (p. 623); none of them states what the coverage chat added, and its follow-up reply says why it took them so (point 7). The checker listed the first only. They turn on the brief because its rules on the unit of a fragment speak of events, not of descriptions.
- **The judge's slips (2):** Pratt pp. 478 and 479. Each paragraph reports a pattern across informants and explains it; the judge named the fragments (F93; F96 to F98) and, for the rest, claims about identification (C03 and C27; C28), not the paragraphs' relations (weak upline bonds where the drive to pursue the dream is gone: F125 and C57 of the coverage chat; mentoring ties made volatile by mixing business and friendship: C58). The checker and the coverage chat both saw a miss. On p. 479 the attribution test bears on it too, since the paragraph builds on cited work on mentoring; but the judge gave no such reason, and the records it named do not hold the mechanism.
- **The coverage chat's slips (2):** Bechky p. 609, where it answered the point on neighbouring occupations with C01 and passed over what both the judge and the checker describe as an account of legitimation (C09, on symbolic legitimacy, is another relation); and the cell of Table 2 (Values, Toxicology), where it judged only the cell's analysis (F149) and does not mention the quotation the cell prints, which no fragment records; under the brief a quoted utterance is a fragment. The judge's follow-up reply calls such mixed cells a gap in the brief (point 1).

**The checker's twelve unpaired lines, read again.** The note above says rightly that the judge calls none of them a miss; that is the judge's verdict, not a finding that they add nothing. Bechky's five are Figures 1 to 5, reprinted from other sources: the open point on outside material, on which the first return kept them out. On Pratt the judge calls all seven covered; on five (B01, B03, B04, B10, B12), and probably a sixth (B16), the records it names do not hold what the checker points to: two facts about the firm (B01); a point of method (B03); a belief distributors held (B04); members' own sayings (B10); the advice to approach family and friends first (B12); and the worry of ambivalent distributors over using friendships for profit (B16). On B18 a record it names (C04) states the checker's point in general terms. This rests on the checker's account of the passages, which nobody has checked against the paper. So on Pratt five or six of the checker's lines may be misses that the PI did not list.

**A pattern of this run.** On Pratt the judge was ready to call a passage covered: on pp. 478 and 479, on Figure 2, on those five or six lines, and on footnote 13, where its task allowed it. The coverage chat sided with it on two Pratt passages the checker listed (pp. 464–465 and 466), so the readiness is not the judge's alone. On Bechky it calls 10 of the PI's 15 passages a miss, 8 of them assertions on the theory pages; on evidence it was readier to call a passage covered (pp. 611–612 and 622–623, and pp. 637–638, which the checker listed). Its task defined "covered" as everything the brief would record already being on the sheet, but asked for one verdict per line, not for each item matched to a record, so nothing in the reply's form brought a ready "covered" into view.

**The judge's two follow-up replies.** After the test, and before closing chats 71 and 72, the PI asked each where the brief's instructions were unclear, contradictory or impossible to apply to its paper, and where it had to decide something the brief did not cover, with the section and the ids. Outside the plan, and described only: self-reports, written with the chat's verdicts in view, which explain its choices and do not test them.
- Of the open points among the 17, they name: the attribution test against one claim per relation on Bechky's theory pages; where the paper's evidence stops (reprinted figures and an outside definition; outside figures and examples on Pratt); and fragments of the author's insight that are also claims (F70 among them). The reach of the attribution test they name on other passages (Pratt footnote 11 and pp. 481–482).
- The Table 2 cell, counted here as the coverage chat's slip, the Bechky reply calls a gap in the brief.
- The Bechky reply's point 7 gives the rules by which the judge decided passages among the 17: a paragraph that holds a recorded claim and also a further assertion, of another condition or outcome, that no claim records is an assertion (A01, A07, also A13); and records on another page may cover a paragraph (A08, A11). Pratt pp. 478 and 479 hold such an unrecorded relation; neither reply names them, nor Pratt footnote 6.
- Among points outside the 17: the voice test against descriptions of routine work; claims that bundle several conditions; periods; the unit; the numbering of fragments added late; methods facts against `fieldwork_scale`; a restated claim whose page is missing from its location; and where a paragraph ends, with block quotes and footnotes attached.
- One span of the Bechky reply, ten words in a row that seem to be the paper's (point 2, p. 618), is left out of the filed copy, with a note in its place.

**One run.** One judge, one checker and two coverage chats, one run each. In T37, which coded how readings bear on the index's claims, the same Argon was level with the other coder against the PI's twelve readings (the same main type 10 and 9 times, claim 8 and 9, level 11 and 10), with one steady lean at a boundary that brief did not draw (`RELATION_RESULTS.md`).

**Checked independently, twice.** A first check recomputed every count with separate code, all reproduced, and grouped the 17 passages itself before it read any other grouping; its grouping and its corrections are taken above. A second check, with the judge's follow-up replies as well, checked this section's 150 statements with separate code: every count reproduces, and its points on wording, weight and what was left out are taken above.
