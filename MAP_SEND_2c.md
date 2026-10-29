# The map test (T39): step 1 of round 2, the missing readings (chats 81 and 82)

Written 18 Oct 2026, after chat 77's third part vanished, chat 78's second part
came without an opening for R13, and both chats were closed. Everything in
`MAP_SEND_2.md` and `MAP_SEND_2b.md` holds but for what is said here: two fresh
Gemini chats (Gemini 4 Argon at Thinking Level High, temporary, with the
settings of chats 64 and 66), each with the four files from its folder of chats/
(81_bechky_place_argon and 82_pratt_place_argon, the same files as chats 77 and
78 had) and your PDF. Each chat is asked only for the readings still missing.
For you alone; it goes into no chat.

**Paste this message as it is** in chat 81:

```
I've attached five files: a paper, as a PDF, PLACEMENT_TASK.md, SETTLED_MAP_bechky.md, RELATION_READINGS_bechky.md and T37_CODES_bechky.md.

Read PLACEMENT_TASK.md in full first, then the paper, then the other three files. Then do what PLACEMENT_TASK.md asks, but only for readings R21 to R30 of RELATION_READINGS_bechky.md, in order.

Give your answer in two parts, so that no single reply is long. Each part is one JSON object of the form PLACEMENT_TASK.md specifies, as one code block: the first with readings R21 to R25, the second with R26 to R30. Give the first part now, and the second when I type continue.

Work only from the paper and the four files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

**and this one** in chat 82:

```
I've attached five files: a paper, as a PDF, PLACEMENT_TASK.md, SETTLED_MAP_pratt.md, RELATION_READINGS_pratt.md and T37_CODES_pratt.md.

Read PLACEMENT_TASK.md in full first, then the paper, then the other three files. Then do what PLACEMENT_TASK.md asks, but only for readings R10 to R17 of RELATION_READINGS_pratt.md, in order.

Give your answer as one JSON object of the form PLACEMENT_TASK.md specifies, as one code block.

Work only from the paper and the four files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

**Then**, in chat 81, type `continue` and nothing else once the first part
is in. If a reply vanishes, or stops before its last closing brace, type:
"Please give that part again." If it vanishes a second time, type: "Please
give that part one reading per reply, each as one JSON object of the same
form: the first now, and each next when I type continue." If the chat asks a
question, offers to go on, or places only some of the readings asked for,
reply: "Please follow PLACEMENT_TASK.md as written, for the readings my first
message asks for: place every one of them, in order, and where it leaves a
choice open, make the one it supports best." Never say anything about the
project, the other chats or what we hope for. If a window shows a web search
or a source being read, note it.

**Keep each chat open** until its replies are checked: a temporary chat cannot
be reopened, and while it is open, a fault can be put right in it with one line.

**Bring back** each reply as it came, numbered in the order it came: from chat
81, `reply_81_bechky_place_argon_part1.json` (R21 to R25) and
`reply_81_bechky_place_argon_part2.json` (R26 to R30), going on to `_part3` and
beyond if a part came one reading per reply; from chat 82,
`reply_82_pratt_place_argon.json`; saved in replies/. Note as well each chat's
start and end times, the model's name and thinking setting as the app showed
them, how many times a reply had to be asked for again, and whether any window
showed a search; and, for chats 77 and 78, the same as far as you have it, the
four runs that vanished included. The replies are joined with the parts of chats
77 and 78 by the script fixed before any part was opened, and each joined reply
is checked by the plan's checks as one.
