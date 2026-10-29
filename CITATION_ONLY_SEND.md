# The citation-only run (T36): your steps

Written 16 Oct 2026, by `CITATION_ONLY_PLAN.md`, after the plan was fixed. Four
chats, which can run side by side. For you alone; it goes into no chat.

**Two fresh incognito claude.ai chats**, outside any project: Fable 5.1 at
max; web search, research and every connector off; file creation on, with its
network access off; no profile preferences or style active. These are the
settings of the wager test's plain chats.

**Two fresh ChatGPT Temporary Chats:** GPT 6 Astra at max; memory, custom
instructions and web search off; no project. These are the settings of T33's
plain chats.

**Web search must be off in all four.** Note each chat's start time.

| chat | paper | model | attach the one file in |
|---|---|---|---|
| 58 | Bechky | Fable 5.1 | chats/58_bechky_citation_fable (CITATION_ONLY_READINGS.md) |
| 59 | Bechky | GPT 6 Astra | chats/59_bechky_citation_astra (CITATION_ONLY_READINGS.md) |
| 60 | Pratt | Fable 5.1 | chats/60_pratt_citation_fable (CITATION_ONLY_READINGS.md) |
| 61 | Pratt | GPT 6 Astra | chats/61_pratt_citation_astra (CITATION_ONLY_READINGS.md) |

Nothing else: no PDF, and no other file. Attach the file as it is, without
opening it.

**Paste this message as it is** in chats 58 and 59:

```
I've attached one file, CITATION_ONLY_READINGS.md. The paper is not attached. This is its citation:

Bechky, B. A. 2020. Evaluative spillovers from technological change: The effects of "DNA envy" on occupational practices in forensic science. Administrative Science Quarterly, 65(3): 606–643.

Read CITATION_ONLY_READINGS.md in full first. Then do what it asks, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Do not search the web, and use no tool to find the paper or anything written about it.
```

**and this one** in chats 60 and 61:

```
I've attached one file, CITATION_ONLY_READINGS.md. The paper is not attached. This is its citation:

Pratt, M. G. 2000. The good, the bad, and the ambivalent: Managing identification among Amway distributors. Administrative Science Quarterly, 45(3): 456–493.

Read CITATION_ONLY_READINGS.md in full first. Then do what it asks, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Do not search the web, and use no tool to find the paper or anything written about it.
```

The two messages differ only in the citation.

**Then**, only if a reply stops before the JSON object's last closing brace,
type `continue` and nothing else. If the object is complete, type nothing, even
if it came in more than one block, and save it as it is. If the chat asks a
question, reply: "Please follow the prompt as written: where it leaves a choice
open, make the one it supports best." Never say anything about the paper, the
project or what we hope for. If a window shows a web search or a source being
read, note it.

**Keep each chat open** until its file is checked: neither kind of chat can be
reopened.

**Bring back** each chat's first complete JSON object, saved in replies/ as
`reply_58_bechky_citation_fable.json`, `reply_59_bechky_citation_astra.json`,
`reply_60_pratt_citation_fable.json` and `reply_61_pratt_citation_astra.json`,
with each chat's start and end times, your word that it ran as these steps say,
and whether any window showed a search. If a JSON came in parts, save each part
as it came, in order, to be joined.

You will see these readings again on your matching sheet; nothing else is
asked of you now.
