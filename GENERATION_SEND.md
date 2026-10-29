# The wagers, generation: your steps

Written 11 Oct 2026 (T29): the system's own route on Pratt and Bechky, one
generation chat per paper. For you alone; it goes into no chat. The two chats
can run side by side, and the four of `BASELINE_SEND.md` with them.

**Two fresh incognito claude.ai chats**, outside any project: Fable 5.1 at max,
as in the four baseline chats; web search, research and every connector off;
file creation on, with its network access off; no profile preferences or style
active. The same settings in all six chats. Note each chat's start time.

| chat | attach the three files in | and nothing else |
|---|---|---|
| Pratt | chats/22_pratt_generation | no PDF |
| Bechky | chats/23_bechky_generation | no PDF |

Each folder holds `STAGE2_PROMPT.md`, `dossier_for_generation.txt` and
`corpus_for_generation.json`. Attach the three from one folder only, and never
mix the two papers' files. No PDF: this chat knows the paper only through its
record.

**Paste this message as it is:**

```
I've attached three files: STAGE2_PROMPT.md, dossier_for_generation.txt and corpus_for_generation.json.

Read STAGE2_PROMPT.md in full first, then the dossier, then the corpus. Then do what STAGE2_PROMPT.md asks, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the three attached files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

**Then** type `continue` and nothing else, if it stops. If it asks a question,
reply: "Please follow STAGE2_PROMPT.md as written: where it leaves a choice
open, make the one it supports best, or decline the entry with your reason."
Never say anything about the paper, the project or what we hope for.

**Keep each chat open** until its file is checked: an incognito chat
cannot be reopened.

**Bring back** each chat's JSON, saved in replies/ as
reply_22_pratt_generation.json and reply_23_bechky_generation.json, with the
chat's start and end times and your word that it ran as these steps say.
`intake_stage2.py` then files each card, runs the mechanical checks and lists
the cards that go on to the attack.
