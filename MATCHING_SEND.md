# The matching test (T33): your grouping and the four coder chats

Written 14 Oct 2026, by `MATCHING_TEST_PLAN.md`, before the readings of chats 49
and 50 were opened. For you alone; it goes into no chat.

## 1. Your grouping, first

`grouping_sheet.xlsx`, at the top of your folder once the readings are built.
Give every reading a group label as its Instructions sheet says: the same label
for readings that make the same point. Do it before you open any of chats 51 to
54, since you will see their replies when you run them. Save it as
`grouping_sheet_filled.xlsx`, with no other change, in replies/. Under an hour.

## 2. The four coder chats, once your sheet is sent

They can run side by side.

**Two fresh incognito claude.ai chats**, outside any project: Opus 5.5 at Extra;
web search, research and every connector off; file creation on, with its
network access off; no profile preferences or style active.

**Two fresh ChatGPT Temporary Chats:** GPT 6 Astra at max; memory, custom
instructions and web search off; no project.

Note each chat's start time.

| chat | in | attach the files in | and |
|---|---|---|---|
| 51, arm A | Claude | chats/51_match_a_opus | your PDF of Bechky (2020) |
| 52, arm A | ChatGPT | chats/52_match_a_astra | your PDF of Bechky (2020) |
| 53, arm B | Claude | chats/53_match_b_opus | your PDF of Bechky (2020) |
| 54, arm B | ChatGPT | chats/54_match_b_astra | your PDF of Bechky (2020) |

The folders of chats 51 and 52 hold `MATCHING_A.md` and `READINGS_matching.md`;
those of chats 53 and 54 hold `MATCHING_B.md`, `READINGS_matching.md` and
`REFERENCE_bechky.md`. Nothing else: the PDF you gave the coders, unannotated
and with no project word in its file name, and no other file. Attach the files
as they are, without opening them.

**Paste this message as it is** in chats 51 and 52:

```
I've attached three files: a paper, as a PDF, MATCHING_A.md and READINGS_matching.md.

Read MATCHING_A.md in full first, then the paper, then the readings. Then do what MATCHING_A.md asks for every reading, in order, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper and the two files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

**and this one** in chats 53 and 54:

```
I've attached four files: a paper, as a PDF, MATCHING_B.md, READINGS_matching.md and REFERENCE_bechky.md.

Read MATCHING_B.md in full first, then the paper, then the reference, then the readings. Then do what MATCHING_B.md asks for every reading, in order, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper and the three files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

**Then**, each time a reply stops before the JSON object's last closing brace,
type `continue` and nothing else. If the object is complete, type nothing, even
if it came in more than one block. If the chat asks a question, offers to go on,
or says it has done only some of the readings, reply, in chats 51 and 52:
"Please follow MATCHING_A.md as written: list every reading once, in order, put
every reading in exactly one group, and return the single JSON object it
specifies."; in chats 53 and 54 the same with MATCHING_B.md. Give the same
answer once more if a chat's reply does not count, and nothing else. Never say
anything about the readings, who wrote them, the project or what we hope for.

**Keep each chat open** until its file is checked.

**Bring back** each chat's JSON, saved in replies/ as
`reply_51_match_a_opus.json`, `reply_52_match_a_astra.json`,
`reply_53_match_b_opus.json` and `reply_54_match_b_astra.json`, with each chat's
start and end times and your word that it ran as these steps say. If a JSON came
in parts, save each part as it came, in order, to be joined.

## 3. Your worth sheet, after your grouping

`worth_sheet_matching.xlsx`, given once your grouping sheet is in: the readings
of chats 49 and 50, each rated 0 to 3 as its Instructions sheet says. Save it as
`worth_sheet_matching_filled.xlsx` in replies/. About ten minutes.
