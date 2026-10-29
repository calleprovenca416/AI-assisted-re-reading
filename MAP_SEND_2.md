# The map test (T39): your steps for round 2

Written 18 Oct 2026, by `MAP_TEST_PLAN.md`, part E, after round 2's files,
their builder and the builder of your comparison sheet were fixed by their
hashes. Three steps: two placement chats; then two checking chats and your
comparison sheet, which can run side by side. For you alone; it goes into no
chat.

**Your comparison (step 3)** takes the twelve readings of your T37 sample, as
the plan has them.

## Step 1. Chats 77 and 78: the placement (about 20 minutes, side by side)

**Two fresh Gemini chats:** Gemini 4 Argon at Thinking Level High, as in
chats 64 and 66, in a temporary chat; outside any Gem; personal context and
saved info off; no apps or extensions; no Deep Research and no Canvas. Note
the model's name and the thinking setting as the app shows them, and each
chat's start time.

| chat | paper | attach, from | and |
|---|---|---|---|
| 77 | Bechky | chats/77_bechky_place_argon: `PLACEMENT_TASK.md`, `SETTLED_MAP_bechky.md`, `RELATION_READINGS_bechky.md`, `T37_CODES_bechky.md` | your PDF of Bechky (2020) |
| 78 | Pratt | chats/78_pratt_place_argon: `PLACEMENT_TASK.md`, `SETTLED_MAP_pratt.md`, `RELATION_READINGS_pratt.md`, `T37_CODES_pratt.md` | your PDF of Pratt (2000) |

The PDF is the one you gave the chats of round 1, unannotated and with no
project word in its file name. Nothing else goes in. Attach the files as they
are, without opening them. If the app will not take a `.md` file, rename it
to `.txt` and change nothing else; the message stays as it is.

**Paste this message as it is** in chat 77:

```
I've attached five files: a paper, as a PDF, PLACEMENT_TASK.md, SETTLED_MAP_bechky.md, RELATION_READINGS_bechky.md and T37_CODES_bechky.md.

Read PLACEMENT_TASK.md in full first, then the paper, then the other three files. Then do what PLACEMENT_TASK.md asks, for every reading in RELATION_READINGS_bechky.md, in order, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper and the four files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

**and this one** in chat 78:

```
I've attached five files: a paper, as a PDF, PLACEMENT_TASK.md, SETTLED_MAP_pratt.md, RELATION_READINGS_pratt.md and T37_CODES_pratt.md.

Read PLACEMENT_TASK.md in full first, then the paper, then the other three files. Then do what PLACEMENT_TASK.md asks, for every reading in RELATION_READINGS_pratt.md, in order, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper and the four files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

The two messages differ only in the papers' names.

**Then**, each time a reply stops before the object's last closing brace, type
`continue` and nothing else. If the object is complete and places every
reading, type nothing, even if it came in more than one block. If the chat
asks a question, offers to go on, or says it has placed only some readings,
reply: "Please follow PLACEMENT_TASK.md as written: place every reading, in
order, and where it leaves a choice open, make the one it supports best."
Never say anything about the project, the other chats or what we hope for. If
a window shows a web search or a source being read, note it.

**Keep each chat open** until its file is checked: a temporary chat cannot be
reopened. If a file does not pass the plan's checks, one line is given to paste
in that chat.

**Bring back** each chat's first complete JSON object, saved in replies/ as
`reply_77_bechky_place_argon.json` and `reply_78_pratt_place_argon.json`, with
each chat's start and end times, the model's name and thinking setting as the
app showed them, your word that it ran as these steps say, and whether any
window showed a search. If a JSON came in parts, save each part as it came, in
order, to be joined.

## Step 2. Chats 79 and 80: the openings' check (about 10 minutes, side by side)

After step 1, once both replies count, each paper's openings are put in
chats/79_bechky_openings_gpt6 and chats/80_pratt_openings_gpt6. **Two fresh
ChatGPT Temporary Chats:** GPT 6 under "Chat", thinking High; memory, custom
instructions and web search off; no project. No PDF: each gets the two files in
its folder and nothing else.

**Paste this message as it is** in chat 79:

```
I've attached two files: OPENINGS_CHECK.md and OPENINGS_bechky.md.

Read OPENINGS_CHECK.md in full first, then OPENINGS_bechky.md. Then do what OPENINGS_CHECK.md asks, for every reading in OPENINGS_bechky.md, in order, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the two files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

**and this one** in chat 80:

```
I've attached two files: OPENINGS_CHECK.md and OPENINGS_pratt.md.

Read OPENINGS_CHECK.md in full first, then OPENINGS_pratt.md. Then do what OPENINGS_CHECK.md asks, for every reading in OPENINGS_pratt.md, in order, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the two files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

`continue`, the line to paste and keeping the chat open as in step 1 (with
"check every reading" for "place every reading"). **Bring back**
`reply_79_bechky_openings_gpt6.json` and `reply_80_pratt_openings_gpt6.json`,
with the same notes as in step 1.

## Step 3. Your comparison sheet (timed; allow up to two hours)

After step 1, beside step 2: `MAP_COMPARISON.xlsx`, at the top of your folder
once built. For each reading of your T37 sample, one tab: the reading and two
accounts of how it relates to the paper's argument, one from T37's codes, the
other from the map; which comes first was drawn for each tab. Two questions on
each, answered from a list: which account tells you more about what the reading
does to the paper's argument, and which could another reader check more readily
against the paper. Save it as `MAP_COMPARISON_filled.xlsx`, with your times or a
rough word on how long it took.

Leave every key file closed (`map_round2_key.json` and those that follow it):
they are for the scripts.

## After round 2

The scorer, fixed before any reply of round 2 is opened, writes the results, and
every figure is checked independently.
