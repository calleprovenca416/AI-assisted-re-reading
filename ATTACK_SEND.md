# The wagers, attack: your steps

Written 11 Oct 2026 (T29): GPT 6 Astra attacks each card in a chat of its own.
Eleven chats: the nine cards of the two generation chats, and two copies of the
Pratt card on the ventured claims (31) broken on purpose, to see whether the
attacker kills what it should. For you alone; it goes into no chat. The chats
can run side by side, and alongside the baseline chats.

**Eleven fresh ChatGPT Temporary Chats:** GPT 6 Astra at max; memory, custom
instructions and web search off; no project. Note each chat's start time.

| chat | attach the three files in |
|---|---|
| Pratt, CP01 | chats/28_attack_pratt_CP01 |
| Pratt, CP02 | chats/29_attack_pratt_CP02 |
| Pratt, CP03 | chats/30_attack_pratt_CP03 |
| Pratt, ventured claims | chats/31_attack_pratt_C56 |
| Pratt, the unit | chats/32_attack_pratt_unit |
| Bechky, CP01 | chats/33_attack_bechky_CP01 |
| Bechky, CP02 | chats/34_attack_bechky_CP02 |
| Bechky, DG02 | chats/35_attack_bechky_DG02 |
| Bechky, the unit | chats/36_attack_bechky_unit |
| broken copy x | chats/37_attack_x |
| broken copy y | chats/38_attack_y |

Each folder holds `attack.md`, `card_for_attack.json` and
`corpus_for_attack.json`. Attach the three from one folder only, and nothing
else: no PDF.

**Paste this message as it is:**

```
I've attached three files: attack.md, card_for_attack.json and corpus_for_attack.json.

Read attack.md in full first, then the card, then the corpus. Then do what attack.md asks, and return the single JSON object it specifies, as a file if you can, otherwise as one code block.

Work only from the three attached files. Do not search the web, and set aside anything you know about the paper, its author or its subject from elsewhere.
```

**Then**, only if a reply stops before the JSON object's last closing brace,
type `continue` and nothing else. If the object is complete, type nothing, even
if it came in more than one block, and save it as it is. If it asks a question,
reply: "Please follow attack.md as written: where it leaves a choice open, make
the one it supports best." Never say anything about the card, the paper, the
project or what we hope for, and never say which copies are broken.

**Keep each chat open** until its file is checked: a Temporary Chat cannot be
reopened.

**Bring back** each chat's first complete JSON object, saved in replies/ as
reply_28_attack.json to reply_38_attack.json, by its chat's number, with the
chat's start and end times and your word that it ran as these steps say.
