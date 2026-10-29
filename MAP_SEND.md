# The map test (T39): your steps for round 1

Written 18 Oct 2026, by `MAP_TEST_PLAN.md`, after the plan was fixed. Four
chats, side by side, about 30 to 40 minutes. For you alone; it goes into no
chat.

**Now: round 1 only.** Your settling sheets and round 2's files are built from
round 1's replies.

## Round 1. Chats 73 to 76: the maps

**Two fresh incognito claude.ai chats,** outside any project: Opus 5.5 at
High; web search, research and every connector off; file creation on, with
its network access off; no profile preferences or style active. **Two fresh
ChatGPT Temporary Chats:** GPT 6 under "Chat", thinking High; memory, custom
instructions and web search off; no project. Note the model's name and the
thinking setting as each app shows them, and each chat's start time.

| chat | paper | coder | attach, from | and |
|---|---|---|---|---|
| 73 | Bechky | Opus 5.5, High | chats/73_bechky_map_opus: `MAP_TASK.md`, `MAP_SHEET_bechky.md` | your PDF of Bechky (2020) |
| 74 | Bechky | GPT 6, Chat, High | chats/74_bechky_map_gpt6: the same two | your PDF of Bechky (2020) |
| 75 | Pratt | Opus 5.5, High | chats/75_pratt_map_opus: `MAP_TASK.md`, `MAP_SHEET_pratt.md` | your PDF of Pratt (2000) |
| 76 | Pratt | GPT 6, Chat, High | chats/76_pratt_map_gpt6: the same two | your PDF of Pratt (2000) |

The PDF is the one you gave the coders of chats 64 to 67, unannotated and with
no project word in its file name. Nothing else goes in. Attach the files as
they are, without opening them. If an app will not take a `.md` file, rename
it to `.txt` and change nothing else; the message stays as it is.

**Paste this message as it is** in chats 73 and 74:

```
I've attached three files: a paper, as a PDF, MAP_TASK.md and MAP_SHEET_bechky.md.

Read MAP_TASK.md in full first, then the paper, then MAP_SHEET_bechky.md. Then do what MAP_TASK.md asks, for every pair the sheet lists, in order, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper and the two files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

**and this one** in chats 75 and 76:

```
I've attached three files: a paper, as a PDF, MAP_TASK.md and MAP_SHEET_pratt.md.

Read MAP_TASK.md in full first, then the paper, then MAP_SHEET_pratt.md. Then do what MAP_TASK.md asks, for every pair the sheet lists, in order, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper and the two files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

The two messages differ only in the sheet's name.

**Then**, each time a reply stops before the object's last closing brace, type
`continue` and nothing else. If the object is complete and answers every pair,
type nothing, even if it came in more than one block. If the chat asks a
question, offers to go on, or says it has answered only some pairs, reply:
"Please follow MAP_TASK.md as written: answer every pair, in order, and where
it leaves a choice open, make the one it supports best." Never say anything
about the project, other readings of the paper, or what we hope for. If a
window shows a web search or a source being read, note it.

**Keep each chat open** until its file is checked: an incognito or temporary
chat cannot be reopened. If a file does not pass the plan's checks, one line is
given to paste in that chat.

**Bring back** each chat's first complete JSON object, saved in replies/ as
`reply_73_bechky_map_opus.json`, `reply_74_bechky_map_gpt6.json`,
`reply_75_pratt_map_opus.json` and `reply_76_pratt_map_gpt6.json`, with each
chat's start and end times, the model's name and thinking setting as the app
showed them, your word that it ran as these steps say, and whether any window
showed a search. If a JSON came in parts, save each part as it came, in order,
to be joined.

Leave `map_key.json` closed: it is for the scripts.

## After round 1

Once the four replies count by the plan's checks: a settling sheet per paper, on
which you choose between the two maps wherever they differ (timed; one to two
hours were expected for both papers); then round 2, two placement chats and two
checking chats, and your comparison of twelve readings, each with its own steps.
