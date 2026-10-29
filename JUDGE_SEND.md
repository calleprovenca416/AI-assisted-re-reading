# The judge chats: your steps

Written 13 Oct 2026 (T31): one judge chat per paper, on Gemini Pro, a vendor
that neither coding used. For you alone; it goes into no chat. The two chats can
run side by side, about 30 minutes each.

**Two fresh Gemini chats:** the Pro model, the newest the app offers, with its
deepest thinking setting if it offers a choice. Use a temporary chat if the app
has one. Outside any Gem; personal context and saved info off; no apps or
extensions; no Deep Research and no Canvas. Note the model's name as the app
shows it, and each chat's start time.

| chat | attach, from | and |
|---|---|---|
| 43, Pratt | chats/43_judge_pratt: `JUDGING.md` and `JUDGE_TABLE_pratt_part1.md` | your PDF of Pratt (2000) |
| 44, Bechky | chats/44_judge_bechky: `JUDGING.md` and `JUDGE_TABLE_bechky_part1.md` | your PDF of Bechky (2020) |

The PDF is the one you gave the coders, unannotated and with no project word in
its file name. Nothing else goes in. Attach the tables as they are, without
opening them. If the app will not take a `.md` file, rename it to `.txt` and
change nothing else.

**Paste this message as it is** in chat 43:

```
I've attached three files: a paper, as a PDF, JUDGING.md and JUDGE_TABLE_pratt_part1.md.

Read JUDGING.md in full first, then the paper, then the table. Then do what JUDGING.md asks for every row of the table, in order, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper and the two files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

**and this one** in chat 44:

```
I've attached three files: a paper, as a PDF, JUDGING.md and JUDGE_TABLE_bechky_part1.md.

Read JUDGING.md in full first, then the paper, then the table. Then do what JUDGING.md asks for every row of the table, in order, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper and the two files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

**When part 1's object is complete**, attach part 2 from the same folder
(`JUDGE_TABLE_pratt_part2.md` in chat 43, `JUDGE_TABLE_bechky_part2.md` in chat
44), in the same chat, and paste:

```
Here is part 2 of the table. Do what JUDGING.md asks for every row of it, in order, and return the single JSON object it specifies, with "part": 2, as a file if you can, otherwise as one code block.
```

**Then**, each time a reply stops before the object's last closing brace, type
`continue` and nothing else. If the object is complete and answers every row,
type nothing, even if it came in more than one block. If the chat asks a
question, offers to go on, or says it has answered only some rows, reply:
"Please follow JUDGING.md as written: answer every row, in order, and where a
row is unclear, answer unclear and say why." Never say anything about the
statements, who made them, the project or what we hope for.

**Keep each chat open** until its files are checked.

**Bring back** each part's JSON, saved in replies/ as
`reply_43_judge_pratt_part1.json`, `reply_43_judge_pratt_part2.json`,
`reply_44_judge_bechky_part1.json` and `reply_44_judge_bechky_part2.json`, with
the model's name as the app showed it, each chat's start and end times, and your
word that it ran as these steps say. If an object came in pieces, save each
piece as it came, in order (`reply_43_part1_a.txt`, `reply_43_part1_b.txt`, and
so on), to be joined.
