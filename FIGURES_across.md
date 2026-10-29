# T27: the figures for the proposal: across the two papers

Written by `build_figures.py` from the results files that each row names. Nothing in it is typed, and nothing here changes a figure of any results file. Every kappa of the cold papers' codings is model against model: coder 1 is the extraction (ChatGPT), coder 2 is Opus 5.5. Rows marked *new* hold figures that no results file held before (see the script's docstring).

The link tests (on Pratt, 29 Sep to 6 Oct) are not in these tables: their figures stand in `LINK_TEST_RESULT.md` and `LINK_TEST2_RESULT.md`, run B and run C included, each checked independently when it was written.

## The counts the pinned predictions are read on (their words are in no file)

| figure | value | source |
|---|---|---|
| P1, Bechky 2020: Stage A, whether a claim names an outcome | 22 of 23; kappa 0.881 (95% interval 0.57 to 1.00; 1,995 of 2,000 resamples gave a kappa) | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| P2, Bechky 2020: the most `against` links on any one claim, coder 1 / coder 2, as coded and with the flagged links as `illustrates` | as coded 0 / 5; with the flags 0 / 0 | `BECHKY_AGREEMENT_LOG.md` (agreement.py's record) |
| P3 and P5, Bechky 2020: first return's fragments coded `reported` (all fragments) | 99 (168) | `bechky_2020_corpus.json`, `bechky_2020_voice_gloss.json` |
| P4, Bechky 2020: first return's ventured claims with a linked fragment | 2 of 4 (0.50) | `bechky_2020_corpus.json` |
| P5, Bechky 2020: first return's claims | 23 | `bechky_2020_corpus.json` |
| P1, Pratt 2000: Stage A, whether a claim names an outcome | 53 of 60; kappa 0.483 (95% interval 0.13 to 0.78) | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| P2, Pratt 2000: the most `against` links on any one claim, coder 1 / coder 2, as coded and with the flagged links as `illustrates` | as coded 1 / 1; with the flags 0 / 1 | `PRATT_AGREEMENT_LOG.md` (agreement.py's record) |
| P3 and P5, Pratt 2000: first return's fragments coded `reported` (all fragments) | 92 (121) | `pratt_2000_corpus.json`, `pratt_2000_voice_gloss.json` |
| P4, Pratt 2000: first return's ventured claims with a linked fragment | 12 of 18 (0.67) | `pratt_2000_corpus.json` |
| P5, Pratt 2000: first return's claims | 52 | `pratt_2000_corpus.json` |

## T31 over both papers

| figure | value | source |
|---|---|---|
| Statements both codings made, held; statements neither made, held | both made: 35 of 46; neither made: 1 of 23 | `judge_results.json` |

## T29 over both papers

| figure | value | source |
|---|---|---|
| The PI's worth over both papers, system arm (declared not blind) | mean 1.11 over 9 readings; rated 2 or more: 4 of 9 | `stage2/worth/worth_joined.json`, checked against `stage2/worth/WORTH_RESULTS.md` |
| The PI's worth over both papers, middle arm (declared not blind) | mean 0.80 over 10 readings; rated 2 or more: 2 of 10 | `stage2/worth/worth_joined.json`, checked against `stage2/worth/WORTH_RESULTS.md` |
| The PI's worth over both papers, plain arm (declared not blind) | mean 1.70 over 10 readings; rated 2 or more: 8 of 10; without the 3 rated late, mean 1.86 | `stage2/worth/worth_joined.json`, checked against `stage2/worth/WORTH_RESULTS.md` |
| Gap in the PI's mean worth (declared not blind) over both papers, system against middle (the reading chats) (p by relabelling within each paper) | +0.31 (p 0.594) | `stage2/worth/WORTH_RESULTS.md` |
| Gap in the PI's mean worth (declared not blind) over both papers, system against plain (the plain chats) (p by relabelling within each paper); the plain arm's mean includes the readings the PI rated late | -0.59 (p 0.122) | `stage2/worth/WORTH_RESULTS.md` |
| Gap in the PI's mean worth (declared not blind) over both papers, middle (the reading chats) against plain (the plain chats) (p by relabelling within each paper); the plain arm's mean includes the readings the PI rated late | -0.90 (p 0.036) | `stage2/worth/WORTH_RESULTS.md` |
| The system's readings the attack killed: the PI's worth (declared not blind) | 7 readings, mean worth 1.00 | `stage2/worth/worth_joined.json`, checked against `stage2/worth/WORTH_RESULTS.md` |
| The system's readings the attack survived: the PI's worth (declared not blind) | 2 readings, mean worth 1.50 | `stage2/worth/worth_joined.json`, checked against `stage2/worth/WORTH_RESULTS.md` |

## Models and times by step, from the list below

| figure | value | source |
|---|---|---|
| extraction (Bechky 2020, Pratt 2000) | 3 chat(s); Opus 5.5 (1); ChatGPT 5.6, naming itself GPT 5.6 Sol (1); ChatGPT, naming itself GPT 5.6 Sol (1); 2026-09-27, 2026-10-06; no start and end on record; a length as recorded for 2 | `chats_models_hours.json` |
| brief review (separate chat) (Pratt 2000) | 1 chat(s); ChatGPT Astra (1); date not on record; no start and end on record | `chats_models_hours.json` |
| model check | 5 chat(s); ChatGPT, naming itself 5.6 Sol (1); ChatGPT, naming itself GPT-5.6 Sol (1); ChatGPT, naming itself GPT-6 (3); 2026-10-05, 2026-10-06, 2026-10-08, 2026-10-09, 2026-10-15; no start and end on record | `chats_models_hours.json` |
| run C (named in passing only) | 1 chat(s); GPT 6 Astra (1); 2026-10-06; no start and end on record | `chats_models_hours.json` |
| coverage chat (Bechky 2020, Pratt 2000) | 2 chat(s); ChatGPT, named GPT 5.6 Sol in its saved reply (1); ChatGPT, naming itself GPT-6 (1); 2026-10-07, 2026-10-09; no start and end on record; a length as recorded for 2 | `chats_models_hours.json` |
| second coding (Bechky 2020, Pratt 2000) | 8 chat(s); Opus 5.5 (8); 2026-10-08, 2026-10-09; start and end on record for 6: 10, 20, 3, 5, 4, 45 min (87 min in all); a length as recorded for 2 more | `chats_models_hours.json` |
| against check | 1 chat(s); Opus 5.5 (1); 2026-10-09; start and end on record for 1: 3 min (3 min in all) | `chats_models_hours.json` |
| T29 generation (Bechky 2020, Pratt 2000) | 2 chat(s); Fable 5.1 (2); 2026-10-11; start and end on record for 1: 26 min (26 min in all); a length as recorded for 1 more | `chats_models_hours.json` |
| T29 baseline middle (Bechky 2020, Pratt 2000) | 2 chat(s); Fable 5.1 (2); 2026-10-11; no start and end on record | `chats_models_hours.json` |
| T29 baseline plain (Bechky 2020, Pratt 2000) | 2 chat(s); Fable 5.1 (2); 2026-10-11; no start and end on record | `chats_models_hours.json` |
| T29 attack (Bechky 2020, Pratt 2000) | 11 chat(s); GPT 6 Astra (11); 2026-10-11; no start and end on record | `chats_models_hours.json` |
| T29 marker (Bechky 2020, Pratt 2000) | 4 chat(s); Opus 5.5 (2); GPT 6 Astra (2); 2026-10-11; start and end on record for 4: 18, 10, 21, 10 min (59 min in all) | `chats_models_hours.json` |
| T31 judge (Bechky 2020, Pratt 2000) | 2 chat(s); Gemini 3.1 Pro (1); Gemini Pro (1); 2026-10-13; no start and end on record | `chats_models_hours.json` |
| T32 readings (Bechky 2020) | 2 chat(s); Fable 5.1 (2); 2026-10-13; no start and end on record | `chats_models_hours.json` |
| T32 marker (Bechky 2020) | 2 chat(s); Opus 5.5 (1); GPT 6 Astra (1); 2026-10-13; no start and end on record; a length as recorded for 2 | `chats_models_hours.json` |
| T33 plain second vendor (Bechky 2020) | 2 chat(s); GPT 6 Astra (2); 2026-10-14; no start and end on record | `chats_models_hours.json` |
| T33 coder arm A (Bechky 2020) | 2 chat(s); Opus 5.5 (1); GPT 6 Astra (1); 2026-10-14; no start and end on record; a length as recorded for 2 | `chats_models_hours.json` |
| T33 coder arm B (Bechky 2020) | 2 chat(s); Opus 5.5 (1); GPT 6 Astra (1); 2026-10-14; no start and end on record; a length as recorded for 2 | `chats_models_hours.json` |
| T35 second extraction (Bechky 2020) | 1 chat(s); ChatGPT, naming itself GPT-6 (1); 2026-10-15; no start and end on record; a length as recorded for 1 | `chats_models_hours.json` |
| T35 matcher (Bechky 2020) | 2 chat(s); Opus 5.5 (1); GPT 6 Astra (1); 2026-10-15; no start and end on record; a length as recorded for 2 | `chats_models_hours.json` |
| T36 citation only (Bechky 2020, Pratt 2000) | 4 chat(s); Fable 5.1 (2); GPT 6 Astra (2); 2026-10-16; no start and end on record; a length as recorded for 4 | `chats_models_hours.json` |
| T37 planted readings (Bechky 2020, Pratt 2000) | 2 chat(s); Fable 5.1 (2); 2026-10-17; no start and end on record | `chats_models_hours.json` |
| T37 coder (Bechky 2020, Pratt 2000) | 4 chat(s); Gemini 4 Argon (2); GPT 6 Astra (2); 2026-10-17; no start and end on record; a length as recorded for 4 | `chats_models_hours.json` |
| T38 checker (Bechky 2020, Pratt 2000) | 2 chat(s); Opus 5.5 (2); 2026-10-17; no start and end on record; a length as recorded for 2 | `chats_models_hours.json` |
| T38 ready test (Bechky 2020) | 1 chat(s); Opus 5.5 (1); 2026-10-17; no start and end on record; a length as recorded for 1 | `chats_models_hours.json` |
| T38 judge (Bechky 2020, Pratt 2000) | 2 chat(s); Gemini 4 Argon (2); 2026-10-17; no start and end on record; a length as recorded for 2 | `chats_models_hours.json` |
| T39 map (Bechky 2020, Pratt 2000) | 4 chat(s); Opus 5.5 (2); GPT 6 (2); 2026-10-18; no start and end on record; a length as recorded for 4 | `chats_models_hours.json` |
| T39 placement (Bechky 2020, Pratt 2000) | 4 chat(s); Gemini 4 Argon (4); 2026-10-18; no start and end on record; a length as recorded for 2 | `chats_models_hours.json` |
| T39 openings check (Bechky 2020, Pratt 2000) | 2 chat(s); GPT 6 (2); 2026-10-18; no start and end on record; a length as recorded for 2 | `chats_models_hours.json` |
| T39 map task feedback (Bechky 2020) | 2 chat(s); Argon (as the file names it) (1); ChatGPT (as the file names it; the model not named) (1); 2026-10-18; no start and end on record | `chats_models_hours.json` |
| step 10 example: titles (Bechky 2020) | 1 chat(s); Opus 5.5 (1); 2026-10-20; start and end on record for 1: 14 min (14 min in all) | `chats_models_hours.json` |

## Models, settings and times of every chat, as recorded

| figure | value | source |
|---|---|---|
| extraction, Pratt 2000 | Opus 5.5, maximum effort, incognito claude.ai chat; date not on record | `chats_models_hours.json` |
| extraction, Pratt 2000 | ChatGPT 5.6, naming itself GPT 5.6 Sol, Temporary Chat; memory, custom instructions and web search off; 2026-09-27; the last files came 45 minutes after the first | `chats_models_hours.json` |
| brief review (separate chat), Pratt 2000 | ChatGPT Astra, max (named 'ChatGPT Astra max'); a separate chat; its settings were not recorded; date not on record | `chats_models_hours.json` |
| model check | ChatGPT, naming itself 5.6 Sol, a separate chat (kind not stated); 2026-10-05 | `chats_models_hours.json` |
| run C (named in passing only) | GPT 6 Astra, under 'Work' in ChatGPT, the only place Astra can be chosen; 2026-10-06 | `chats_models_hours.json` |
| chat 8: extraction, Bechky 2020 | ChatGPT, naming itself GPT 5.6 Sol, High thinking effort, Temporary Chat under 'Chat'; memory, custom instructions, web search, connectors off; 2026-10-06, 20:06 to ?; chat's own working time 48 min 37 s over six passes; 57 minutes from the start to the last download | `chats_models_hours.json` |
| model check | ChatGPT, naming itself GPT-5.6 Sol, Temporary Chat (address ends temporary-chat=true); the 'Chat'/'Work' switch and the effort are not shown; 2026-10-06 | `chats_models_hours.json` |
| chat 9: coverage chat, Bechky 2020 | ChatGPT, named GPT 5.6 Sol in its saved reply, High thinking effort; Temporary Chat under 'Chat'; memory, custom instructions, web search, connectors off; 2026-10-07, 12:40 to ?; Worked for 9m 5s (its saved reply) | `chats_models_hours.json` |
| chat 10: second coding, Bechky 2020 | Opus 5.5, Extra, fresh incognito claude.ai chat outside any project; web search, research, connectors off; tools off; 2026-10-08, 07:15 to ?; about 5 minutes | `chats_models_hours.json` |
| second coding, Bechky 2020 | Opus 5.5, Extra, fresh incognito claude.ai chat outside any project; web search, research, connectors off; 2026-10-08, 07:25 to ?; about 3 minutes | `chats_models_hours.json` |
| chat 12: second coding, Bechky 2020 | Opus 5.5, Extra, fresh incognito claude.ai chat outside any project; web search, research, connectors off; 2026-10-08, 07:45 to 07:55 (10 min) | `chats_models_hours.json` |
| chat 13: second coding, Bechky 2020 | Opus 5.5, Extra, fresh incognito claude.ai chat outside any project; web search, research, connectors off; continue typed whenever it stopped; 2026-10-08, 08:05 to 08:25 (20 min) | `chats_models_hours.json` |
| model check | ChatGPT, naming itself GPT-6, Temporary Chat; 2026-10-08 | `chats_models_hours.json` |
| model check | ChatGPT, naming itself GPT-6, Temporary Chat; 2026-10-09 | `chats_models_hours.json` |
| coverage chat, Pratt 2000 | ChatGPT, naming itself GPT-6, High thinking effort, fresh Temporary Chat under 'Chat'; memory, custom instructions, web search, connectors off; 2026-10-09, 10:31 to ?; worked for 10 min 30 s (its own first line) | `chats_models_hours.json` |
| chat 17: second coding, Pratt 2000 | Opus 5.5, Extra, fresh incognito claude.ai chat outside any project; web search, research, connectors off; 2026-10-09, 11:33 to 11:36 (3 min) | `chats_models_hours.json` |
| second coding, Pratt 2000 | Opus 5.5, Extra, fresh incognito claude.ai chat outside any project; web search, research, connectors off (as for Stage A); 2026-10-09, 11:41 to 11:46 (5 min) | `chats_models_hours.json` |
| second coding, Pratt 2000 | Opus 5.5, Extra, fresh incognito claude.ai chat outside any project; web search, research, connectors off (as for the stages before); 2026-10-09, 11:49 to 11:53 (4 min) | `chats_models_hours.json` |
| second coding, Pratt 2000 | Opus 5.5, Extra, fresh incognito claude.ai chat outside any project; web search, research, connectors off (as for the stages before); stops for continue not on record; 2026-10-09, 11:58 to 12:43 (45 min) | `chats_models_hours.json` |
| chat 21: against check | Opus 5.5, Extra, fresh incognito claude.ai chat outside any project; web search, research, connectors off; AGAINST_CHECK.md and the table only; 2026-10-09, 19:51 to 19:54 (3 min) | `chats_models_hours.json` |
| chat 22: T29 generation, Pratt 2000 | Fable 5.1, max, fresh incognito chat; file creation on, network access off; no profile preferences or style; bundle files, no PDF; 2026-10-11, 10:18 to 10:44 (26 min) | `chats_models_hours.json` |
| chat 23: T29 generation, Bechky 2020 | Fable 5.1, max, fresh incognito chat; file creation on, network access off; no profile preferences or style; bundle files, no PDF; 2026-10-11; after continue, about 8 more minutes before Fable's revised reply | `chats_models_hours.json` |
| chat 24: T29 baseline middle, Pratt 2000 | Fable 5.1, max, fresh incognito chat; file creation on, network access off; no profile preferences or style; READING_PROMPT.md and the PDF; 2026-10-11 | `chats_models_hours.json` |
| chat 25: T29 baseline plain, Pratt 2000 | Fable 5.1, max, fresh incognito chat; file creation on, network access off; no profile preferences or style; ALTERNATIVE_READINGS.md and the PDF; 2026-10-11 | `chats_models_hours.json` |
| chat 26: T29 baseline middle, Bechky 2020 | Fable 5.1, max, fresh incognito chat; file creation on, network access off; no profile preferences or style; READING_PROMPT.md and the PDF; 2026-10-11 | `chats_models_hours.json` |
| chat 27: T29 baseline plain, Bechky 2020 | Fable 5.1, max, fresh incognito chat; file creation on, network access off; no profile preferences or style; ALTERNATIVE_READINGS.md and the PDF; 2026-10-11 | `chats_models_hours.json` |
| chat 28: T29 attack, Pratt 2000 | GPT 6 Astra, max, fresh ChatGPT Temporary Chat; memory, custom instructions, web search off (by ATTACK_SEND.md); 2026-10-11 | `chats_models_hours.json` |
| chat 29: T29 attack, Pratt 2000 (by `stage2/attack_results.md`) | GPT 6 Astra, max, fresh ChatGPT Temporary Chat; memory, custom instructions, web search off (by ATTACK_SEND.md); 2026-10-11 | `chats_models_hours.json` |
| chat 30: T29 attack, Pratt 2000 (by `stage2/attack_results.md`) | GPT 6 Astra, max, fresh ChatGPT Temporary Chat; memory, custom instructions, web search off (by ATTACK_SEND.md); 2026-10-11 | `chats_models_hours.json` |
| chat 31: T29 attack, Pratt 2000 | GPT 6 Astra, max, fresh ChatGPT Temporary Chat; memory, custom instructions, web search off (by ATTACK_SEND.md); 2026-10-11 | `chats_models_hours.json` |
| chat 32: T29 attack, Pratt 2000 (by `stage2/attack_results.md`) | GPT 6 Astra, max, fresh ChatGPT Temporary Chat; memory, custom instructions, web search off (by ATTACK_SEND.md); 2026-10-11 | `chats_models_hours.json` |
| chat 33: T29 attack, Bechky 2020 (by `stage2/attack_results.md`) | GPT 6 Astra, max, fresh ChatGPT Temporary Chat; memory, custom instructions, web search off (by ATTACK_SEND.md); 2026-10-11 | `chats_models_hours.json` |
| chat 34: T29 attack, Bechky 2020 (by `stage2/attack_results.md`) | GPT 6 Astra, max, fresh ChatGPT Temporary Chat; memory, custom instructions, web search off (by ATTACK_SEND.md); 2026-10-11 | `chats_models_hours.json` |
| chat 35: T29 attack, Bechky 2020 | GPT 6 Astra, max, fresh ChatGPT Temporary Chat; memory, custom instructions, web search off (by ATTACK_SEND.md); 2026-10-11 | `chats_models_hours.json` |
| chat 36: T29 attack, Bechky 2020 | GPT 6 Astra, max, fresh ChatGPT Temporary Chat; memory, custom instructions, web search off (by ATTACK_SEND.md); 2026-10-11 | `chats_models_hours.json` |
| chat 37: T29 attack, Pratt 2000 (by `stage2/attack_results.md`); calibration copy x of 31: planted import | GPT 6 Astra, max, fresh ChatGPT Temporary Chat; memory, custom instructions, web search off (by ATTACK_SEND.md); 2026-10-11 | `chats_models_hours.json` |
| chat 38: T29 attack, Pratt 2000; calibration copy y of 31: planted contradiction | GPT 6 Astra, max, fresh ChatGPT Temporary Chat; memory, custom instructions, web search off (by ATTACK_SEND.md); calibration copy y; 2026-10-11 | `chats_models_hours.json` |
| chat 39: T29 marker, Pratt 2000 | Opus 5.5, Extra, in claude.ai (by MARKER_SEND.md); MARKING.md, the readings file and the PDF; 2026-10-11, 14:28 to 14:46 (18 min) | `chats_models_hours.json` |
| chat 40: T29 marker, Pratt 2000 | GPT 6 Astra, max, in ChatGPT (by MARKER_SEND.md); MARKING.md, the readings file and the PDF; 2026-10-11, 14:29 to 14:39 (10 min) | `chats_models_hours.json` |
| chat 41: T29 marker, Bechky 2020 | Opus 5.5, Extra, in claude.ai (by MARKER_SEND.md); MARKING.md, the readings file and the PDF; 2026-10-11, 14:49 to 15:10 (21 min) | `chats_models_hours.json` |
| chat 42: T29 marker, Bechky 2020 | GPT 6 Astra, max, in ChatGPT (by MARKER_SEND.md); MARKING.md, the readings file and the PDF; 2026-10-11, 14:45 to 14:55 (10 min) | `chats_models_hours.json` |
| chat 43: T31 judge, Pratt 2000 | Gemini 3.1 Pro, advanced reasoning, Thinking High (Extra thorough), temporary mode; 2026-10-13 | `chats_models_hours.json` |
| chat 44: T31 judge, Bechky 2020 | Gemini Pro, the Pro model at its deepest thinking, a temporary chat if offered (by the steps; its model and mode not confirmed); 2026-10-13 | `chats_models_hours.json` |
| chat 45: T32 readings, Bechky 2020 | Fable 5.1, max, fresh incognito claude.ai chat with the wager test's settings; PLACE_READINGS.md, PLACES.md and the PDF; 2026-10-13 | `chats_models_hours.json` |
| chat 46: T32 readings, Bechky 2020 | Fable 5.1, max, fresh incognito claude.ai chat with the wager test's settings; OPEN_PLACES.md and the PDF; 2026-10-13 | `chats_models_hours.json` |
| chat 47: T32 marker, Bechky 2020 | Opus 5.5, Extra, incognito (ran as the steps say); 2026-10-13; 20 minutes | `chats_models_hours.json` |
| chat 48: T32 marker, Bechky 2020 | GPT 6 Astra, max, Temporary Chat (ran as the steps say); 2026-10-13; 12 minutes | `chats_models_hours.json` |
| chat 49: T33 plain second vendor, Bechky 2020 | GPT 6 Astra, max, fresh ChatGPT Temporary Chat; the PDF and ALTERNATIVE_READINGS.md; 2026-10-14 | `chats_models_hours.json` |
| chat 50: T33 plain second vendor, Bechky 2020 | GPT 6 Astra, max, fresh ChatGPT Temporary Chat; the PDF and ALTERNATIVE_READINGS.md; 2026-10-14 | `chats_models_hours.json` |
| chat 51: T33 coder arm A, Bechky 2020 | Opus 5.5, Extra, incognito (T33 coders' set-up, by MATCHING_SEND.md); MATCHING_A.md and the readings file, no reference; 2026-10-14, 11:05 to ?; around 5 minutes each | `chats_models_hours.json` |
| chat 52: T33 coder arm A, Bechky 2020 | GPT 6 Astra, max, Temporary Chat (T33 coders' set-up, by MATCHING_SEND.md); MATCHING_A.md and the readings file, no reference; 2026-10-14, 11:05 to ?; around 5 minutes each | `chats_models_hours.json` |
| chat 53: T33 coder arm B, Bechky 2020 | Opus 5.5, Extra, incognito (T33 coders' set-up, by MATCHING_SEND.md); MATCHING_B.md, the readings file and REFERENCE_bechky.md; 2026-10-14, 11:05 to ?; around 5 minutes each | `chats_models_hours.json` |
| chat 54: T33 coder arm B, Bechky 2020 | GPT 6 Astra, max, Temporary Chat (T33 coders' set-up, by MATCHING_SEND.md); MATCHING_B.md, the readings file and REFERENCE_bechky.md; 2026-10-14, 11:05 to ?; around 5 minutes each | `chats_models_hours.json` |
| model check | ChatGPT, naming itself GPT-6, Temporary Chat (address ends temporary-chat=true); the 'Chat'/'Work' switch and the effort are not shown; 2026-10-15 | `chats_models_hours.json` |
| chat 55: T35 second extraction, Bechky 2020 | ChatGPT, naming itself GPT-6, thinking High, fresh Temporary Chat under 'Chat'; memory, custom instructions, web search, connectors off; 2026-10-15, 10:35 to ?; chat's working time 61 min 10 s over six passes | `chats_models_hours.json` |
| chat 56: T35 matcher, Bechky 2020 | Opus 5.5, Extra, fresh incognito claude.ai chat outside any project; web search, research, connectors off; file creation on, network access off; 2026-10-15, 12:04 to ?; 5 minutes (its window: Thought for 1m 34s) | `chats_models_hours.json` |
| chat 57: T35 matcher, Bechky 2020 | GPT 6 Astra, max, fresh ChatGPT Temporary Chat; memory, custom instructions, web search off; 2026-10-15, 12:04 to ?; about 7 minutes (2 minutes longer than Opus) | `chats_models_hours.json` |
| chat 58: T36 citation only, Bechky 2020 | Fable 5.1, max, fresh incognito claude.ai chat outside any project; web search, research and every connector off; file creation on, network access off; no profile preferences or style; CITATION_ONLY_READINGS.md only, no PDF; 2026-10-16, 19:40 to ?; 3 to 4 minutes | `chats_models_hours.json` |
| chat 59: T36 citation only, Bechky 2020 | GPT 6 Astra, max, fresh ChatGPT Temporary Chat; memory, custom instructions and web search off; no project; CITATION_ONLY_READINGS.md only, no PDF; 2026-10-16, 19:40 to ?; 3 to 4 minutes | `chats_models_hours.json` |
| chat 60: T36 citation only, Pratt 2000 | Fable 5.1, max, fresh incognito claude.ai chat outside any project; web search, research and every connector off; file creation on, network access off; no profile preferences or style; CITATION_ONLY_READINGS.md only, no PDF; 2026-10-16, 19:45 to ?; 3 to 4 minutes | `chats_models_hours.json` |
| chat 61: T36 citation only, Pratt 2000 | GPT 6 Astra, max, fresh ChatGPT Temporary Chat; memory, custom instructions and web search off; no project; CITATION_ONLY_READINGS.md only, no PDF; 2026-10-16, 19:45 to ?; 3 to 4 minutes | `chats_models_hours.json` |
| chat 62: T37 planted readings, Bechky 2020 | Fable 5.1, max, fresh incognito claude.ai chat outside any project; web search, research and every connector off; file creation on, network access off; no profile preferences or style; PLANTED_SPEC_bechky.md and the PDF; asked in the same chat to shorten its two readings, the shortened reply the one used; 2026-10-17 | `chats_models_hours.json` |
| chat 63: T37 planted readings, Pratt 2000 | Fable 5.1, max, fresh incognito claude.ai chat outside any project; web search, research and every connector off; file creation on, network access off; no profile preferences or style; PLANTED_SPEC_pratt.md and the PDF; asked in the same chat to shorten its two readings, the shortened reply the one used; 2026-10-17 | `chats_models_hours.json` |
| chat 64: T37 coder, Bechky 2020 | Gemini 4 Argon, Thinking Level High, in place of the planned Gemini 3.1 Pro; fresh temporary Gemini chat outside any Gem; personal context and saved info off; no apps or extensions; no Deep Research and no Canvas; RELATION_CODING.md, CLAIMS_bechky.md, RELATION_READINGS_bechky.md and the PDF; 2026-10-17, 09:45 to ?; about 7 minutes | `chats_models_hours.json` |
| chat 65: T37 coder, Bechky 2020 | GPT 6 Astra, max, fresh ChatGPT Temporary Chat; memory, custom instructions and web search off; no project; RELATION_CODING.md, CLAIMS_bechky.md, RELATION_READINGS_bechky.md and the PDF; 2026-10-17, 09:45 to ?; about 4 minutes | `chats_models_hours.json` |
| chat 66: T37 coder, Pratt 2000 | Gemini 4 Argon, Thinking Level High, in place of the planned Gemini 3.1 Pro; fresh temporary Gemini chat outside any Gem; personal context and saved info off; no apps or extensions; no Deep Research and no Canvas; RELATION_CODING.md, CLAIMS_pratt.md, RELATION_READINGS_pratt.md and the PDF; 2026-10-17, 09:55 to ?; about 7 minutes | `chats_models_hours.json` |
| chat 67: T37 coder, Pratt 2000 | GPT 6 Astra, max, fresh ChatGPT Temporary Chat; memory, custom instructions and web search off; no project; RELATION_CODING.md, CLAIMS_pratt.md, RELATION_READINGS_pratt.md and the PDF; 2026-10-17, 09:55 to ?; about 4 minutes | `chats_models_hours.json` |
| chat 68: T38 checker, Bechky 2020 | Opus 5.5, Extra, fresh incognito claude.ai chat outside any project; web search, research and every connector off; file creation on, network access off; no profile preferences or style; COMPLETENESS_CHECK.md, CHECK_SHEET_bechky.md, EXTRACTION_BRIEF.md and the PDF; 2026-10-17, 21:55 to ?; 3 minutes (not said whether for each chat or for the three side by side) | `chats_models_hours.json` |
| chat 69: T38 checker, Pratt 2000 | Opus 5.5, Extra, fresh incognito claude.ai chat outside any project; web search, research and every connector off; file creation on, network access off; no profile preferences or style; COMPLETENESS_CHECK.md, CHECK_SHEET_pratt.md, EXTRACTION_BRIEF.md and the PDF; 2026-10-17, 21:55 to ?; 3 minutes (not said whether for each chat or for the three side by side) | `chats_models_hours.json` |
| chat 70: T38 ready test, Bechky 2020 | Opus 5.5, Extra, fresh incognito claude.ai chat outside any project; web search, research and every connector off; file creation on, network access off; no profile preferences or style; MATCH_PASSAGES_TO_Q.md, PASSAGES_AND_Q_bechky.md and the PDF; 2026-10-17, 21:55 to ?; 3 minutes (not said whether for each chat or for the three side by side) | `chats_models_hours.json` |
| chat 71: T38 judge, Bechky 2020 | Gemini 4 Argon, Thinking Level High, fresh temporary Gemini chat outside any Gem; personal context and saved info off; no apps or extensions; no Deep Research and no Canvas; JUDGE_MISSES.md, CHECK_SHEET_bechky.md, EXTRACTION_BRIEF.md, TWO_PASSAGE_LISTS_bechky.md and the PDF; after the task, a second question put in the same chat before it was closed: where the brief was unclear, contradictory or impossible to apply; 2026-10-17, 22:15 to ?; 6 minutes | `chats_models_hours.json` |
| chat 72: T38 judge, Pratt 2000 | Gemini 4 Argon, Thinking Level High, fresh temporary Gemini chat outside any Gem; personal context and saved info off; no apps or extensions; no Deep Research and no Canvas; JUDGE_MISSES.md, CHECK_SHEET_pratt.md, EXTRACTION_BRIEF.md, TWO_PASSAGE_LISTS_pratt.md and the PDF; after the task, a second question put in the same chat before it was closed: where the brief was unclear, contradictory or impossible to apply; 2026-10-17, 22:15 to ?; 6 minutes | `chats_models_hours.json` |
| chat 73: T39 map, Bechky 2020 | Opus 5.5, High, fresh incognito claude.ai chat outside any project; web search, research and every connector off; file creation on, network access off; no profile preferences or style; MAP_TASK.md, MAP_SHEET_bechky.md and the PDF; 2026-10-18, 17:10 to ?; about 10 minutes (one length given for the four map chats, from one start) | `chats_models_hours.json` |
| chat 74: T39 map, Bechky 2020 | GPT 6, thinking High in ChatGPT's Chat mode, fresh Temporary Chat; memory, custom instructions and web search off; no project; MAP_TASK.md, MAP_SHEET_bechky.md and the PDF; 2026-10-18, 17:10 to ?; about 10 minutes (one length given for the four map chats, from one start) | `chats_models_hours.json` |
| chat 75: T39 map, Pratt 2000 | Opus 5.5, High, fresh incognito claude.ai chat outside any project; web search, research and every connector off; file creation on, network access off; no profile preferences or style; MAP_TASK.md, MAP_SHEET_pratt.md and the PDF; 2026-10-18, 17:10 to ?; about 10 minutes (one length given for the four map chats, from one start) | `chats_models_hours.json` |
| chat 76: T39 map, Pratt 2000 | GPT 6, thinking High in ChatGPT's Chat mode, fresh Temporary Chat; memory, custom instructions and web search off; no project; MAP_TASK.md, MAP_SHEET_pratt.md and the PDF; 2026-10-18, 17:10 to ?; about 10 minutes (one length given for the four map chats, from one start) | `chats_models_hours.json` |
| chat 77: T39 placement, Bechky 2020 | Gemini 4 Argon, Thinking Level High, fresh temporary Gemini chat outside any Gem; personal context and saved info off; no apps or extensions; no Deep Research and no Canvas; PLACEMENT_TASK.md, SETTLED_MAP_bechky.md, RELATION_READINGS_bechky.md, T37_CODES_bechky.md and the PDF; after four runs whose reply vanished at its end, asked for its reply in three parts: parts 1 and 2 (R01 to R20) came and are used, part 3 vanished; 2026-10-18 | `chats_models_hours.json` |
| chat 78: T39 placement, Pratt 2000 | Gemini 4 Argon, Thinking Level High, fresh temporary Gemini chat outside any Gem; personal context and saved info off; no apps or extensions; no Deep Research and no Canvas; PLACEMENT_TASK.md, SETTLED_MAP_pratt.md, RELATION_READINGS_pratt.md, T37_CODES_pratt.md and the PDF; after four runs whose reply vanished at its end, asked for its reply in two parts: part 1 (R01 to R09) is used; part 2 came without one reading's opening and is not used; 2026-10-18 | `chats_models_hours.json` |
| chat 79: T39 openings check, Bechky 2020 | GPT 6, thinking High in ChatGPT's Chat mode, fresh Temporary Chat; memory, custom instructions and web search off; no project; OPENINGS_CHECK.md and OPENINGS_bechky.md, no PDF; 2026-10-18, 23:00 to ?; 5 minutes | `chats_models_hours.json` |
| chat 80: T39 openings check, Pratt 2000 | GPT 6, thinking High in ChatGPT's Chat mode, fresh Temporary Chat; memory, custom instructions and web search off; no project; OPENINGS_CHECK.md and OPENINGS_pratt.md, no PDF; 2026-10-18, 23:00 to ?; 3 minutes | `chats_models_hours.json` |
| chat 81: T39 placement, Bechky 2020 | Gemini 4 Argon, Thinking Level High, fresh temporary Gemini chat outside any Gem; personal context and saved info off; no apps or extensions; no Deep Research and no Canvas; the four files of chat 77 and the PDF; asked only for Bechky's R21 to R30, in two parts, both used; 2026-10-18, 22:45 to ?; about 7 minutes (one length given for chats 81 and 82, from one start) | `chats_models_hours.json` |
| chat 82: T39 placement, Pratt 2000 | Gemini 4 Argon, Thinking Level High, fresh temporary Gemini chat outside any Gem; personal context and saved info off; no apps or extensions; no Deep Research and no Canvas; the four files of chat 78 and the PDF; asked only for Pratt's R10 to R17, in one part, used; 2026-10-18, 22:45 to ?; about 7 minutes (one length given for chats 81 and 82, from one start) | `chats_models_hours.json` |
| T39 map task feedback, Bechky 2020 | Argon (as the file names it), given only the paper, MAP_TASK.md and MAP_SHEET_bechky.md, and asked where the instructions might make two coders diverge and how to improve the task; settings not recorded; 2026-10-18 | `chats_models_hours.json` |
| T39 map task feedback, Bechky 2020 | ChatGPT (as the file names it; the model not named), given only the paper, MAP_TASK.md and MAP_SHEET_bechky.md, and asked where the instructions might make two coders diverge and how to improve the task; settings not recorded; 2026-10-18 | `chats_models_hours.json` |
| step 10 example: titles, Bechky 2020 | Opus 5.5, a separate session, given only the two-sentence openings of the 28 real readings, from the placement replies (chats 77 and 81), and told to open nothing else; 2026-10-20, 11:43 to 11:57 (14 min) | `chats_models_hours.json` |

## The PI's own time, as recorded

| figure | value | source |
|---|---|---|
| PI coverage check, Bechky 2020 | about 3.5 hours; the plan gave two hours (2026-10-07) | `chats_models_hours.json` |
| PI coverage check, Pratt 2000 | about 3.5 hours (2026-10-08, from 11:50) | `chats_models_hours.json` |
| PI worth rating (T29) | length not on record (2026-10-11) | `chats_models_hours.json` |
| PI worth rating (T29, three late ratings) | length not on record (2026-10-11) | `chats_models_hours.json` |
| PI worth rating (T32), Bechky 2020 | length not on record (2026-10-13) | `chats_models_hours.json` |
| PI grouping (T33), Bechky 2020 | length not on record (2026-10-14) | `chats_models_hours.json` |
| PI worth rating (T33), Bechky 2020 | length not on record (2026-10-14) | `chats_models_hours.json` |
| PI matching (T36) | about an hour; about 45 minutes had been estimated (2026-10-16) | `chats_models_hours.json` |
| PI check of the planted readings (T37) | length not on record (2026-10-17) | `chats_models_hours.json` |
| PI relation coding (T37) | about 90 minutes; about 40 had been estimated (2026-10-17) | `chats_models_hours.json` |
| PI settling of the two maps (T39) | more than 2 hours, both papers together (2026-10-18) | `chats_models_hours.json` |
| PI comparison of the two accounts (T39) | about 30 minutes (2026-10-19) | `chats_models_hours.json` |
