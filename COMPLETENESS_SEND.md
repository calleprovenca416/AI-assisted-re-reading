# The completeness test (T38): your steps

Written 17 Oct 2026, by `COMPLETENESS_TEST_PLAN.md`, after the plan was fixed.
Five chats in two rounds, about 40 minutes in all, mostly waiting; no coding or
judging of yours. For you alone; it goes into no chat.

**Now: round 1 only.** The files of round 2 are built from the replies of
round 1.

## Round 1. Chats 68, 69 and 70 (about 20 minutes, side by side)

**Three fresh incognito claude.ai chats**, outside any project: Opus 5.5 at
Extra; web search, research and every connector off; file creation on, with
its network access off; no profile preferences or style active. These are the
settings of T35's chat 56. Note each chat's start time.

| chat | paper | attach, from | and |
|---|---|---|---|
| 68 | Bechky | chats/68_bechky_check_opus: `COMPLETENESS_CHECK.md`, `CHECK_SHEET_bechky.md`, `EXTRACTION_BRIEF.md` | your PDF of Bechky (2020) |
| 69 | Pratt | chats/69_pratt_check_opus: `COMPLETENESS_CHECK.md`, `CHECK_SHEET_pratt.md`, `EXTRACTION_BRIEF.md` | your PDF of Pratt (2000) |
| 70 | Bechky | chats/70_bechky_ready_test_opus: `MATCH_PASSAGES_TO_Q.md`, `PASSAGES_AND_Q_bechky.md` | your PDF of Bechky (2020) |

The PDF is the one you gave the coders before, unannotated and with no project
word in its file name. Nothing else goes in. Attach the files as they are,
without opening them. If the app will not take a `.md` file, rename it to
`.txt` and change nothing else.

**Paste this message as it is** in chat 68:

```
I've attached four files: a paper, as a PDF, COMPLETENESS_CHECK.md, CHECK_SHEET_bechky.md and EXTRACTION_BRIEF.md.

Read COMPLETENESS_CHECK.md in full first, then the brief, the sheet and the paper. Then do what COMPLETENESS_CHECK.md asks, from the paper's first page to its last, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper and the three files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

**this one** in chat 69:

```
I've attached four files: a paper, as a PDF, COMPLETENESS_CHECK.md, CHECK_SHEET_pratt.md and EXTRACTION_BRIEF.md.

Read COMPLETENESS_CHECK.md in full first, then the brief, the sheet and the paper. Then do what COMPLETENESS_CHECK.md asks, from the paper's first page to its last, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper and the three files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

**and this one** in chat 70:

```
I've attached three files: a paper, as a PDF, MATCH_PASSAGES_TO_Q.md and PASSAGES_AND_Q_bechky.md.

Read MATCH_PASSAGES_TO_Q.md in full first, then the paper, then PASSAGES_AND_Q_bechky.md. Then do what MATCH_PASSAGES_TO_Q.md asks for every line, L01 to L15, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper and the two files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

**Then**, each time a reply stops before the object's last closing brace, type
`continue` and nothing else. If the object is complete, type nothing, even if
it came in more than one block. If the chat asks a question, offers to go on,
or says it has done only part of the paper or of the lines, reply: "Please
follow the task file as written: do all of it, and where it leaves a choice
open, make the one it supports best." Never say anything about the lists, who
made them, the project or what we hope for. If a window shows a web search or
a source being read, note it.

**Keep each chat open** until its file is checked: an incognito chat
cannot be reopened.

**Bring back** each chat's first complete JSON object, saved in replies/ as
`reply_68_bechky_check_opus.json`, `reply_69_pratt_check_opus.json` and
`reply_70_bechky_ready_test_opus.json`, with each chat's start and end times,
your word that it ran as these steps say, and whether any window showed a
search. If a JSON came in parts, save each part as it came, in order, to be
joined.

## Round 2. Chats 71 and 72 (about 15 minutes, side by side)

Once the judges' files are built. **Two fresh Gemini chats:** Gemini 4 Argon at
Thinking Level High, in a temporary chat; outside any Gem; personal context and
saved info off; no apps or extensions; no Deep Research and no Canvas. These are
the settings of chats 64 and 66. Note the model's name as the app shows it, and
each chat's start time.

| chat | paper | attach, from | and |
|---|---|---|---|
| 71 | Bechky | chats/71_bechky_judge_argon: `JUDGE_MISSES.md`, `CHECK_SHEET_bechky.md`, `EXTRACTION_BRIEF.md`, `TWO_PASSAGE_LISTS_bechky.md` | your PDF of Bechky (2020) |
| 72 | Pratt | chats/72_pratt_judge_argon: `JUDGE_MISSES.md`, `CHECK_SHEET_pratt.md`, `EXTRACTION_BRIEF.md`, `TWO_PASSAGE_LISTS_pratt.md` | your PDF of Pratt (2000) |

The same PDF as in round 1. Nothing else goes in.

**Paste this message as it is** in chat 71:

```
I've attached five files: a paper, as a PDF, JUDGE_MISSES.md, CHECK_SHEET_bechky.md, EXTRACTION_BRIEF.md and TWO_PASSAGE_LISTS_bechky.md.

Read JUDGE_MISSES.md in full first, then the brief, the sheet and the paper, then the two lists. Then do both parts of what JUDGE_MISSES.md asks, for every line of both lists, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper and the four files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

**and this one** in chat 72:

```
I've attached five files: a paper, as a PDF, JUDGE_MISSES.md, CHECK_SHEET_pratt.md, EXTRACTION_BRIEF.md and TWO_PASSAGE_LISTS_pratt.md.

Read JUDGE_MISSES.md in full first, then the brief, the sheet and the paper, then the two lists. Then do both parts of what JUDGE_MISSES.md asks, for every line of both lists, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper and the four files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

**Then** as in round 1: `continue` only when a reply stops before the object's
last closing brace; the same one reply to a question; nothing about the lists,
who made them, the project or what we hope for. **Keep each chat open** until
its file is checked.

**Bring back** each chat's first complete JSON object, saved in replies/ as
`reply_71_bechky_judge_argon.json` and `reply_72_pratt_judge_argon.json`, with
each chat's start and end times, the model's name as the app showed it, your
word that it ran as these steps say, and whether any window showed a search.
