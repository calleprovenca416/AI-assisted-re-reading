# The wagers, baseline: your steps

Written 11 Oct 2026: both arms (T29). Four chats. On each paper, one is given
`READING_PROMPT.md`, the generation prompt with the paper in place of its record
(the middle arm), and one `ALTERNATIVE_READINGS.md`, a plain five-field prompt
(the plain arm). For you alone; it goes into no chat. They can run side by side
with the two of `GENERATION_SEND.md`.

**Four fresh incognito claude.ai chats**, outside any project: Fable 5.1 at
max, as in the two generation chats; web search, research and every connector
off; file creation on, with its network access off; no profile preferences or
style active. The same settings in all six chats. Note each chat's start time.

| chat | attach the file in | and |
|---|---|---|
| Pratt, middle | chats/24_pratt_reading (READING_PROMPT.md) | your PDF of Pratt (2000) |
| Pratt, plain | chats/25_pratt_plain (ALTERNATIVE_READINGS.md) | your PDF of Pratt (2000) |
| Bechky, middle | chats/26_bechky_reading (READING_PROMPT.md) | your PDF of Bechky (2020) |
| Bechky, plain | chats/27_bechky_plain (ALTERNATIVE_READINGS.md) | your PDF of Bechky (2020) |

Nothing else: the PDF you gave the coders, unannotated and with no project word
in its file name, and no other file.

**Paste this message as it is** in the two middle chats:

```
I've attached two files: a paper, as a PDF, and READING_PROMPT.md.

Read READING_PROMPT.md in full first, then the paper. Then do what READING_PROMPT.md asks, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

**and this one** in the two plain chats:

```
I've attached two files: a paper, as a PDF, and ALTERNATIVE_READINGS.md.

Read ALTERNATIVE_READINGS.md in full first, then the paper. Then do what ALTERNATIVE_READINGS.md asks, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the paper. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

The two messages differ only in the prompt's name, so that the two arms differ
only in their prompt.

**Then**, only if a reply stops before the JSON object's last closing brace,
type `continue` and nothing else. If the object is complete, type nothing, even
if it came in more than one block, and save it as it is: `continue` after a
complete object sets off a second pass, as it did in Bechky's generation chat.
If it asks a question, reply in a middle chat: "Please follow the prompt as
written: where it leaves a choice open, make the one it supports best, or
decline it with your reason."; in a plain chat: "Please follow the prompt as
written: where it leaves a choice open, make the one it supports best." Never
say anything about the paper, the project or what we hope for.

**Keep each chat open** until its file is checked: an incognito chat
cannot be reopened.

**Bring back** each chat's first complete JSON object (and anything it sends
after it, as a second file), saved in replies/ as reply_24_pratt_reading.json,
reply_25_pratt_plain.json, reply_26_bechky_reading.json and
reply_27_bechky_plain.json, with the chat's start and end times and your word
that it ran as these steps say.
