# The second extraction of Bechky (T35): the results

Written by `score_second_extraction.py score`, as `SECOND_EXTRACTION_PLAN.md` fixes the figures (its sha256 ca72f71a5c7830eca683b2246a104f0c000f6afc4b566189fca0413f2869b1cf). List P is the first return, list Q the new; the lists file's sha256 is 8ffba0ddbaa3d4f74780483623f267ef263808f01ffd47c6bc07cc74c461e5ea. Matcher a is chat 56 (Opus 5.5 at Extra); matcher b is chat 57 (GPT 6 Astra at max).

## The replies

- **a, chat 56 (Opus 5.5 at Extra):** reply_56_match_lists_opus.json, sha256 cccb44ddecad58474333a0c8f599911980d8c6dc59ce1b92fe03c359e7209d9d: counts.
- **b, chat 57 (GPT 6 Astra at max):** reply_57_match_lists_astra.json, sha256 2ca01eb764ee8457706191cd7512cb590c1c746e29ebeb201810c021dfd89b7e: counts.

## The answers

- **Q1, the claims: repeat in part** (both matchers give this case). Case under a: 2; under b: 2; under both: 2; under either: 2. Pair kappa 0.661; kappa on whether an item is found 0.850, which decides nothing.
- **Q2, the passages outside the tables: repeat in part** (both matchers give this case). Case under a: 2; under b: 2; under both: 2; under either: 2. Pair kappa 1.000; kappa on whether an item is found 1.000, which decides nothing.
- **Q2, second reading: all passages, the table cells included: repeat in part** (both matchers give this case). Case under a: 2; under b: 2; under both: 2; under either: 2. Pair kappa 1.000; kappa on whether an item is found 1.000, which decides nothing.
- **Q3, voice on the passages both matchers pair: less steady** (the voice kappa is at least 0.60 and under 0.80). Kappa 0.788 on 140 pairs.

Cases: 1, repeat (f and s at least 0.80); 2, repeat in part (both at least 0.50); 3, do not repeat. f is the share of the first return's items found again, s the share of the new return's found in the first.

## Found again

| items | n | a | b | both | either |
|---|---|---|---|---|---|
| claims of the first return (f) | 23 | 0.91 (21 of 23) | 0.91 (21 of 23) | 0.91 (21 of 23) | 0.91 (21 of 23) |
| claims of the new return (s) | 39 | 0.69 (27 of 39) | 0.77 (30 of 39) | 0.69 (27 of 39) | 0.77 (30 of 39) |
| the first return's core claims | 7 | 0.86 (6 of 7) | 0.86 (6 of 7) | 0.86 (6 of 7) | 0.86 (6 of 7) |
| the new return's core claims | 9 | 1.00 (9 of 9) | 1.00 (9 of 9) | 1.00 (9 of 9) | 1.00 (9 of 9) |
| passages outside the tables, first return (f) | 128 | 0.65 (83 of 128) | 0.65 (83 of 128) | 0.65 (83 of 128) | 0.65 (83 of 128) |
| passages outside the tables, new return (s) | 127 | 0.74 (94 of 127) | 0.74 (94 of 127) | 0.74 (94 of 127) | 0.74 (94 of 127) |
| all passages, first return | 168 | 0.73 (123 of 168) | 0.73 (123 of 168) | 0.73 (123 of 168) | 0.73 (123 of 168) |
| all passages, new return | 168 | 0.80 (135 of 168) | 0.80 (135 of 168) | 0.80 (135 of 168) | 0.80 (135 of 168) |
| table cells, first return | 40 | 1.00 (40 of 40) | 1.00 (40 of 40) | 1.00 (40 of 40) | 1.00 (40 of 40) |
| table cells, new return | 41 | 1.00 (41 of 41) | 1.00 (41 of 41) | 1.00 (41 of 41) | 1.00 (41 of 41) |
| passages, first author_insight | 69 | 0.46 (32 of 69) | 0.46 (32 of 69) | 0.46 (32 of 69) | 0.46 (32 of 69) |
| passages, first reported | 99 | 0.92 (91 of 99) | 0.92 (91 of 99) | 0.92 (91 of 99) | 0.92 (91 of 99) |
| passages, new author_insight | 28 | 0.96 (27 of 28) | 0.96 (27 of 28) | 0.96 (27 of 28) | 0.96 (27 of 28) |
| passages, new reported | 140 | 0.77 (108 of 140) | 0.77 (108 of 140) | 0.77 (108 of 140) | 0.77 (108 of 140) |

## The matchers' agreement

Cohen's kappa, matcher a against matcher b, with 95% intervals from 2,000 bootstrap resamples (seed 20261018).

| kappa | over | value | 95% interval | resamples left out |
|---|---|---|---|---|
| claims: whether each is found | every claim of both lists | 0.850 | 0.664 to 1.000 | 0 |
| claims: whether each pair is named | 897 pairs of a claim of P and a claim of Q | 0.661 | 0.463 to 0.859 | 0 |
| passages outside the tables: whether each is found | every passage outside the tables, of both lists | 1.000 | 1.000 to 1.000 | 0 |
| passages outside the tables: whether each candidate pair is named | 1757 candidate pairs outside the tables | 1.000 | 1.000 to 1.000 | 0 |
| all passages: whether each is found | every passage of both lists | 1.000 | 1.000 to 1.000 | 0 |
| all passages: whether each candidate pair is named | 3451 candidate pairs | 1.000 | 1.000 to 1.000 | 0 |
| voice: the first return's code against the new return's | the passage pairs both matchers name | 0.788 | 0.652 to 0.903 | 0 |

## Voice on matched passages

Over the 140 passage pairs both matchers name: the two returns' codes agree on 130 (raw 0.929), kappa 0.788; beside the two codings of the first extraction's record, 161 of 172, kappa 0.865.

- first / new: author_insight / author_insight: 25
- first / new: author_insight / reported: 8
- first / new: reported / author_insight: 2
- first / new: reported / reported: 105

## Described, not tested

- **The first return:** 23 claims (7 core; stated_as {'established': 19, 'ventured': 4}); 168 passages, 40 of them table cells; voice {'author_insight': 69, 'reported': 99}.
- **The new return:** 39 claims (9 core; stated_as {'established': 34, 'ventured': 5}); 168 passages, 41 of them table cells; voice {'author_insight': 28, 'reported': 140}.
- **Claim pairs both matchers name:** 28; stated_as agrees on 27, core on 28.
- **Links, on each claim pair with each passage pair both name** (140 passage pairs): {'both link, different direction': 53, 'both link, same direction': 196, 'both link: illustrates / illustrates': 169, 'both link: illustrates / with': 12, 'both link: qualifies / against': 1, 'both link: qualifies / illustrates': 1, 'both link: qualifies / qualifies': 5, 'both link: with / illustrates': 39, 'both link: with / with': 22, 'first return only': 120, 'neither': 3261, 'new return only': 290}; links given twice for one pair: 0.
- **Matcher a's pairs:** 28 of claims (0 named one way only), 140 of passages (0 one way only); of the passage pairs, 0 more than one page apart, 0 with a page unknown, 0 outside the candidate pairs, and 0 of a table cell with a passage outside the tables.
- **Matcher b's pairs:** 55 of claims (0 named one way only), 140 of passages (0 one way only); of the passage pairs, 0 more than one page apart, 0 with a page unknown, 0 outside the candidate pairs, and 0 of a table cell with a passage outside the tables.
- **Passages per page, first return** (-1: no page): {'607': 1, '612': 3, '613': 20, '614': 3, '615': 4, '616': 9, '617': 5, '618': 2, '619': 10, '620': 4, '621': 5, '622': 4, '623': 10, '624': 7, '625': 5, '626': 4, '627': 6, '628': 5, '629': 3, '630': 5, '631': 7, '632': 7, '633': 26, '634': 5, '635': 4, '636': 1, '637': 3}
- **Passages per page, new return** (-1: no page): {'606': 1, '607': 5, '608': 7, '609': 3, '610': 5, '611': 3, '612': 3, '613': 19, '614': 4, '615': 2, '616': 8, '617': 6, '618': 3, '619': 7, '620': 2, '621': 6, '622': 6, '623': 8, '624': 4, '625': 4, '626': 4, '627': 4, '628': 6, '629': 5, '630': 5, '631': 5, '632': 6, '633': 25, '637': 1, '638': 1}

---

*Notes added below the scorer's output on 15 Oct; the text above is the scorer's, unchanged.*

**Checked independently.** From the plan, the scorer's documented definitions (not its code), the key, the lists file, the four files of the two returns, the two replies and these results, every figure was recomputed with separate code: some 9,140 comparisons (the key against the returns, the replies' checks, the 271 values of the JSON, the 28 bounds of the intervals, the answers, and the 488 numbers of this file), with no discrepancy. The bounds match exactly when each index is drawn with `random.randrange(n)`, as the scorer draws them.

**To read beside the figures.**

- **The two replies' passage sections are identical** in all 336 entries, byte for byte but for a final newline, while their claims differ in 25 of 62 entries. Each, recopied from its own chat, equals the file first saved. By what the two windows showed, chat 57 ran commands, read the paper's text and viewed six images before it replied; chat 56 shows about a minute and a half of thought and no command. So every passage figure is the same under each matcher, under both and under either, and every passage kappa is 1.000. The files cannot tell whether that is two judgements that agree or an alignment that leaves no room to differ.
- **On claims,** all 28 of chat 56's pairs are among chat 57's 55.
- **Two answers sit near their bars.** The claims' pair kappa, 0.661, which decides Q1, is under 0.60 in 25.5% of the resamples; the voice kappa, 0.788, is 0.80 or more in 42.4%.
- **What is not found again.** Of the first return's 45 passages without a counterpart, 37 are the author's account, and 15 are its last passages, on pp. 633 to 637. Of the new return's 33, 24 are the passages its pass 5 added (F145 to F168, nearly all on pp. 606 to 611, mainly from the paper's literature review by the chat's own account). Neither matcher finds a counterpart for the first return's C11 or C21 (one of its core claims), or for nine of the new return's claims.
- **The voice cues cut.** The coders' packs' rule, which the builder applies as the plan says, also cut "the paper reports that" from four stubs of list P, an opening the plan does not name among its three; and in 18 of the 103 stubs it cut, it made curly apostrophes straight. Nothing else of any printed text was changed.
- **The figure beside voice,** 0.865 (161 of 172), is from `BECHKY_AGREEMENT_LOG.md`.
