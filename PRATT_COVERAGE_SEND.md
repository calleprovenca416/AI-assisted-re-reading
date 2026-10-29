# Pratt 2000: your steps for the coverage check and the coverage chat

*8 October 2026. Who may receive this file: nobody (—). It goes into no chat.
It is `BECHKY_COVERAGE_SEND.md` with Pratt's names and numbers; nothing in the
procedure is new but the model of the chat. The coverage chat runs on the
model that ChatGPT now gives, which names itself GPT-6, and not on the GPT 5.6
Sol that extracted Pratt on 27 Sep; what it adds is filed apart, and Pratt's
agreement figures are given a second time without it.*

## Part 1. Your coverage check

**What you need:** the paper's PDF, and the reading sheet
`pratt_2000_coverage_reading.md`. The sheet gives the 52 claims first, and
then, page by page, the 121 fragments and the claims located on each page. It
is for you alone, and goes into no chat.

1. **Read the 52 claims once,** at the head of the sheet. Nothing needs
   learning by heart: under each page the sheet gives that page's claims
   again, in words.
2. **Then read the paper section by section, paragraph by paragraph, with the
   sheet beside it.** The sheet has pages and no paragraphs, because the
   extraction recorded a page for each record and nothing finer. The
   fragments under a page mostly stand in the order of the page, because the
   extraction numbers them as it meets them; in Pratt's corpus the numbering
   steps back to an earlier page once, at F120, and the sheet says so. Tick
   each fragment off as you meet its passage.
3. Write one line for each passage that produced no fragment or no claim. In
   the words of the brief's own coverage sweep, that is a passage of which
   one of these holds, as you read it:
   - it prints evidence (an event, a quote, an observation, an archival item,
     a table cell), and no fragment covers it;
   - it asserts, in the paper's own voice, how something works, and none of
     the 52 claims covers it.

   Most paragraphs answer both with "no" in a few seconds. A page with no
   fragment is not by itself a miss. In doubt, it is your call: the chat may
   answer that a listed passage holds nothing, but the message does ask it
   to extract what you list. The brief says where misses hide: in footnotes,
   table notes and figure captions.
4. **Each line gives the page and the paragraph, and nothing else.** No
   reasons, and no word of what the passage says.
   - The chat sees only your lines, not this file. So write each line so that
     someone with only the PDF and that line finds the passage.
   - Count full paragraphs: `p. 470, first full paragraph`.
   - A paragraph that runs over a page break: `pp. 470–471, the paragraph
     that runs over the page`.
   - On the paper's first page: `p. 456, first paragraph after the abstract`.
   - What is not a paragraph, by its name: `p. 456, abstract`; `p. 470,
     footnote 2`; `p. 470, Table 1`.

   These lines show the form only. None of them is a suggestion.
5. Save the lines as plain text, one passage to a line.

The sheet's head names the pages with no fragment at all (eight: p. 461,
pp. 483–484, pp. 486–487 and pp. 489–491). They are a place to start, not a
finding: a page of references has none either.

**The time.** The plan gives this check two hours for every paper; Bechky's
took about three and a half. If the time is up before the paper is, it is
your call to stop or to go on; note the last page you reached.

## Part 2. The coverage chat

### What the chat gets

Five files and the message below, and nothing else:

1. `EXTRACTION_BRIEF.md`, version 2, as frozen on 27 Sep. Its sha256 opens
   72a98c29.
2. `pratt_2000_corpus.json`. Its sha256 opens b22a8f26.
3. `pratt_2000_voice_gloss.json`. Its sha256 opens 17fbb5f5.
4. `pratt_2000_extraction_log.md`. Its sha256 opens d897f145.
5. The paper's PDF, from your own copy.

The first four are the brief and the first return's three files: your
downloads after pass 5 on 27 Sep, byte for byte, under the names the brief
gives them.

**It does not get:** the reading sheet, this file, the audit's output, the
extraction chat's answer on the brief, the review of 28 Sep, any file of the
link tests, or any note on the return.

### Settings

As for the extraction, but for the model:

- ChatGPT, under "Chat" and not under "Work", in a **Temporary Chat**, not
  inside any project.
- Thinking effort at High.
- Memory off, custom instructions off, web search off, every connector off.
- **A fresh chat.** Not a chat of a model check.
- **The model.** By the model check of 8 Oct the chat now names itself
  GPT-6, not the GPT 5.6 Sol that extracted Pratt. It runs all the same,
  declared as such. Just before you start, ask a separate Temporary Chat
  "which model are you?", and keep a picture of its answer, as on 8 Oct.
- Note the time you start.

### Steps

1. Open the chat and attach the five files.
2. Paste the message below, with your list in place of its last line.
3. If it stops before it has given you the three files, type `continue` and
   nothing else.
   - If it asks what something is for, or which reading you prefer, reply:
     "Please follow the brief: make your best judgement and record it as a
     close call in the log."
   - Do not correct its content. If a format problem stops it, ask it to fix
     the format only.
4. Download the three updated files into a folder of their own, so that they
   are not mixed with the first return's. Keep their names as downloaded.
5. Copy the chat's messages, with the times, into one text file.
6. Type nothing else into the chat, and keep it open until the files are
   validated. A Temporary Chat cannot be reopened.

### The message

Paste it as it is, with your list in place of the last line:

```
I've attached five files: EXTRACTION_BRIEF.md, a PDF of a published research paper, and three files an earlier session produced from that paper under the brief: pratt_2000_corpus.json, pratt_2000_voice_gloss.json and pratt_2000_extraction_log.md. The earlier session completed all six passes.

A coverage check found the passages listed at the end of this message, which produced no fragment or no claim. Read the brief in full first, then the whole paper, then the three files. Then extract the listed passages following the brief — fragments, claims, links, voice and gloss — numbering on from the last id in each list. Do not change anything already recorded unless a new record requires it. If a listed passage holds no fragment and no claim under the brief, say why. Record every addition and change in the log under a heading "Coverage additions", and give me the three updated files.

Work only from the attached PDF. Do not search the web, and set aside anything you know about this paper or its author from elsewhere.

paper_id: pratt_2000
citation: Pratt, M. G. 2000. The good, the bad, and the ambivalent: Managing identification among Amway distributors. Administrative Science Quarterly, 45(3): 456–493.

Passages:
<page and paragraph, one per line>
```

## What to bring back

- the three updated files;
- your list, as you pasted it;
- the text file of the chat's messages, with their times;
- the start and end times, and anything you typed besides the message;
- the picture of the model check.

## What happens next

1. The three files are validated, with a format request in the chat only if
   one is needed. Nothing from the checks goes back into the chat.
2. They are filed under names of their own. The first return's three files
   stay as they came, and what the coverage chat added is kept apart from it,
   with the model it came from.
3. The wording check, and then the freeze as `pratt_2000_v1.json`.
4. The second coding, as for Bechky: four chats of coder 2, Opus 5.5 at
   Extra. Pratt's agreement figures are then given twice: on the frozen
   corpus, and without what the coverage chat added.
