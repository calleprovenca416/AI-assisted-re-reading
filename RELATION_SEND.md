# The relation test (T37): your steps

Written 16 Oct 2026, by `RELATION_TEST_PLAN.md`, after the plan was fixed. Six
chats in two rounds, with your check and your coding between them, about 1.5
hours in all. For you alone; it goes into no chat.

**Now: step 1 only.** The files for steps 2 to 4 are built from the replies of
step 1.

## Step 1. Chats 62 and 63: the planted readings (about 10 minutes, side by side)

**Two fresh incognito claude.ai chats**, outside any project: Fable 5.1 at
max; web search, research and every connector off; file creation on, with its
network access off; no profile preferences or style active. These are the
settings of the wager test's plain chats. Note each chat's start time.

| chat | paper | attach, from | and |
|---|---|---|---|
| 62 | Bechky | chats/62_bechky_planted_fable: `PLANTED_SPEC_bechky.md` | your PDF of Bechky (2020) |
| 63 | Pratt | chats/63_pratt_planted_fable: `PLANTED_SPEC_pratt.md` | your PDF of Pratt (2000) |

The PDF is the one you gave the coders before, unannotated and with no
project word in its file name. Nothing else goes in. Attach the file as it is.
If the app will not take a `.md` file, rename it to `.txt` and change nothing
else.

**Paste this message as it is** in chat 62:

```
I've attached two files: a paper, as a PDF, and PLANTED_SPEC_bechky.md.

Read PLANTED_SPEC_bechky.md in full first, then the paper. Then do what PLANTED_SPEC_bechky.md asks, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper and the file. Do not search the web.
```

**and this one** in chat 63:

```
I've attached two files: a paper, as a PDF, and PLANTED_SPEC_pratt.md.

Read PLANTED_SPEC_pratt.md in full first, then the paper. Then do what PLANTED_SPEC_pratt.md asks, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper and the file. Do not search the web.
```

**Then**, only if a reply stops before the JSON object's last closing brace,
type `continue` and nothing else. If the object is complete, type nothing, even
if it came in more than one block. If the chat asks a question, reply: "Please
follow the specification as written: where it leaves a choice open, make the
one it supports best." Never say anything about the project or what we hope
for. If a window shows a web search or a source being read, note it.

**Keep each chat open** until its file is checked: an incognito chat
cannot be reopened.

**Bring back** each chat's first complete JSON object, saved in replies/ as
`reply_62_bechky_planted_fable.json` and `reply_63_pratt_planted_fable.json`,
with each chat's start and end times and your word that it ran as these steps
say. If a JSON came in parts, save each part as it came, in order, to be joined.

## Step 2. Your check of the four planted readings (about 10 minutes)

On `planted_check.xlsx`, at the top of your folder and sent in our
conversation once step 1's replies are checked: for each planted reading, its
claim and what it was written to do to that claim. Say of each whether it does
it: yes or no, and a note if you like. Save it as
`planted_check_filled.xlsx`.

## Step 3. Your coding of twelve readings (about 40 minutes)

On `relation_sheet.xlsx`, also at the top of your folder: six readings of each
paper, drawn from the real ones. For each, the claim it bears on most directly
and what it does to that claim, as the sheet explains; the cells offer the
choices. **Please fill it before you open any of chats 64 to 67, and say so
when you send it.** Leave `relation_key.json` closed until the coders' replies
are in. Save it as `relation_sheet_filled.xlsx`.

Steps 2 and 3 can be done in either order.

## Step 4. Chats 64 to 67: the coders (about 20 minutes, side by side)

After step 3. **Two fresh Gemini chats:** Gemini 3.1 Pro at its deepest
thinking setting (Thinking High, Extra thorough, as in chats 43 and 44), in a
temporary chat; outside any Gem; personal context and saved info off; no apps
or extensions; no Deep Research and no Canvas. **Two fresh ChatGPT Temporary
Chats:** GPT 6 Astra at max; memory, custom instructions and web search off; no
project. Note the model's name as each app shows it, and each chat's start
time.

| chat | paper | coder | attach, from | and |
|---|---|---|---|---|
| 64 | Bechky | Gemini 3.1 Pro | chats/64_bechky_relation_gemini: `RELATION_CODING.md`, `CLAIMS_bechky.md`, `RELATION_READINGS_bechky.md` | your PDF of Bechky (2020) |
| 65 | Bechky | GPT 6 Astra | chats/65_bechky_relation_astra: the same three | your PDF of Bechky (2020) |
| 66 | Pratt | Gemini 3.1 Pro | chats/66_pratt_relation_gemini: `RELATION_CODING.md`, `CLAIMS_pratt.md`, `RELATION_READINGS_pratt.md` | your PDF of Pratt (2000) |
| 67 | Pratt | GPT 6 Astra | chats/67_pratt_relation_astra: the same three | your PDF of Pratt (2000) |

The same PDF as in step 1. Nothing else goes in. Attach the files as they
are, without opening them.

**Paste this message as it is** in chats 64 and 65:

```
I've attached four files: a paper, as a PDF, RELATION_CODING.md, CLAIMS_bechky.md and RELATION_READINGS_bechky.md.

Read RELATION_CODING.md in full first, then the paper, then the claims and the readings. Then do what RELATION_CODING.md asks for every reading, in order, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper and the three files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

**and this one** in chats 66 and 67:

```
I've attached four files: a paper, as a PDF, RELATION_CODING.md, CLAIMS_pratt.md and RELATION_READINGS_pratt.md.

Read RELATION_CODING.md in full first, then the paper, then the claims and the readings. Then do what RELATION_CODING.md asks for every reading, in order, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper and the three files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

The two messages differ only in the files' names.

**Then**, each time a reply stops before the object's last closing brace, type
`continue` and nothing else. If the object is complete and codes every
reading, type nothing, even if it came in more than one block. If the chat
asks a question, offers to go on, or says it has coded only some readings,
reply: "Please follow RELATION_CODING.md as written: code every reading, in
order, and where it leaves a choice open, make the one it supports best."
Never say anything about the readings, who wrote them, the project or what we
hope for. If a window shows a web search or a source being read, note it.

**Keep each chat open** until its file is checked: a temporary chat
cannot be reopened.

**Bring back** each chat's first complete JSON object, saved in replies/ as
`reply_64_bechky_relation_gemini.json`, `reply_65_bechky_relation_astra.json`,
`reply_66_pratt_relation_gemini.json` and `reply_67_pratt_relation_astra.json`,
with each chat's start and end times, the model's name as the app showed it,
your word that it ran as these steps say, and whether any window showed a
search. If a JSON came in parts, save each part as it came, in order, to be
joined.
