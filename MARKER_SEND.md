# The wagers, marking: your steps

Written 11 Oct 2026 (T29, step 5): every reading of the three arms, the system's
nine cards with the middle arm's ten and the plain arm's ten, put in one form,
cited by page, shuffled and unlabeled, then marked sentence by sentence by two
markers per paper, one Claude and one ChatGPT. Fable 5.1 wrote every reading, so
it marks none. Four chats. For you alone; it goes into no chat. The four can run
side by side.

**Two fresh incognito claude.ai chats**, outside any project: Opus 5.5 at
Extra, the setting of coder 2's chats and of the `against` check; web search,
research and every connector off; file creation on, with its network access
off; no profile preferences or style active.

**Two fresh ChatGPT Temporary Chats:** GPT 6 Astra at max, the setting of the
attack chats; memory, custom instructions and web search off; no project.

Note each chat's start time.

| chat | in | attach the two files in | and |
|---|---|---|---|
| 39, Pratt | Claude | chats/39_mark_pratt_opus | your PDF of Pratt (2000) |
| 40, Pratt | ChatGPT | chats/40_mark_pratt_astra | your PDF of Pratt (2000) |
| 41, Bechky | Claude | chats/41_mark_bechky_opus | your PDF of Bechky (2020) |
| 42, Bechky | ChatGPT | chats/42_mark_bechky_astra | your PDF of Bechky (2020) |

Each folder holds `MARKING.md` and the paper's readings: `READINGS_pratt.md`,
15 readings in 203 numbered sentences, or `READINGS_bechky.md`, 14 readings in
193. Nothing else: the PDF you gave the coders, unannotated and with no project
word in its file name, and no other file.

**Paste this message as it is** in the two Pratt chats:

```
I've attached three files: a paper, as a PDF, MARKING.md and READINGS_pratt.md.

Read MARKING.md in full first, then the paper, then the readings. Then do what MARKING.md asks for every numbered sentence of the readings, in order, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper and the two files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

**and this one** in the two Bechky chats:

```
I've attached three files: a paper, as a PDF, MARKING.md and READINGS_bechky.md.

Read MARKING.md in full first, then the paper, then the readings. Then do what MARKING.md asks for every numbered sentence of the readings, in order, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper and the two files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

The two messages differ only in the readings file's name.

**Then**, each time a reply stops before the JSON object's last closing brace,
type `continue` and nothing else; with some 200 sentences, a chat may need it
more than once. If the object is complete and codes every sentence, type
nothing, even if it came in more than one block. If the chat asks a question,
offers to go on, or says it has coded only some of the sentences, reply:
"Please follow MARKING.md as written: code every sentence, in order, and where
a sentence is unclear, give your best code and say why in its note." Never say
anything about the readings, who wrote them, the project or what we hope for.

**Keep each chat open** until its file is checked: neither an incognito chat nor
a Temporary Chat can be reopened.

**Bring back** each chat's JSON, saved in replies/ as
reply_39_mark_pratt_opus.json, reply_40_mark_pratt_astra.json,
reply_41_mark_bechky_opus.json and reply_42_mark_bechky_astra.json, with the
chat's start and end times and your word that it ran as these steps say. If a
chat's JSON came in parts, save each part as it came, in order
(reply_39_part1.txt, reply_39_part2.txt, and so on), to be joined.
