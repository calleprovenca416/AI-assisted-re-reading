# Grouping readings of a paper by the point they make, with a reference

You are given a published qualitative paper, as a PDF; a file of readings of it,
`READINGS_matching.md`; and a reference for the paper, `REFERENCE_bechky.md`.
Each reading proposes another way of reading the paper's own account: it
contests something the paper claims and puts something else in its place. Your
job is not to judge whether a reading is good or true. It is to say, for each
reading, which claim of the reference it contests, what it rests on and what it
puts in that claim's place, and then to group the readings that make the same
point.

The reference was made from the paper before any of the readings was written.
It lists the paper's claims, numbered C01 to C23, each with its statement and
the pages where the paper makes it; and the passages of the paper's evidence,
numbered F01 to F172, each with its page, the group or unit it concerns, its
voice (`reported`: it reports what happened, what was done or what someone said;
`author's account`: the author's own account, across events) and a one-sentence
summary. A summary is a pointer, not the passage: check the page.

The readings are numbered M01 onward and come in no particular order. They were
written in different ways and at different lengths.

---

## 1. Each reading

For every reading, in order, give:

- **claim:** the number of the claim in the reference that the reading's main
  point contests most directly. A reading's main point is the one its wager
  states first. The claim it contests most directly is the one whose statement
  that point denies, replaces or re-explains; where a claim about one unit,
  group or episode and a general claim both fit, give the specific one. If the
  main point contests no claim in the reference, give `none`, and say in
  `none_note`, in one sentence, what it contests.
- **other_claims:** the numbers of up to three other claims of the reference
  that the reading also contests, or an empty list.
- **passages:** the numbers of up to five passages of the reference that the
  reading's case rests on most, or an empty list.
- **alternative:** what the reading puts in that claim's place, in one sentence
  of at most 30 words.

## 2. The groups

Then put the readings in groups. Two readings make the same point, and go in one
group, when they contest the same claim of the paper with the same alternative
account, whatever their wording, emphasis or evidence. Each reading is grouped
by its main point. A reading whose point no other reading makes is a group of
its own. Every reading goes in exactly one group. Give each group a short
statement of its point.

## An example, from a made-up paper

A made-up paper on restaurant kitchens claims that cooks under time pressure
skip the tasting step because they value speed over care (claim 1), and that
head chefs who taste every dish themselves keep the step alive (claim 2). Four
readings of it:

- R1: The step is skipped because the recipe cards go missing in the rush, not
  because cooks value speed.
- R2: What the paper calls valuing speed is the absence of the cards: without
  them, no one knows what a dish should taste like.
- R3: Cooks skip the step in the rush because the head chef forbids tasting at
  the pass.
- R4: The head chefs who taste everything are those who arrive before the rush
  begins, so the step survives only where the evening starts calm.

R1, R2 and R3 each contest claim 1, and R4 contests claim 2. R1 and R2 put the
same alternative in claim 1's place, the missing cards: one group. R3 puts
another, the head chef's rule: a group of its own, though its claim is the same.
R4 is a group of its own. The groups are {R1, R2}, {R3} and {R4}.

---

## Rules

- Work only from the paper, the readings file and the reference. Do not search
  the web, and set aside anything you know about the paper, its author or its
  subject from elsewhere.
- Use the reference's numbers exactly as it gives them (C07, F112).
- List every reading once, in order. Do not skip, merge or split readings.
- Put every reading in exactly one group.
- Do not rate the readings, rank them, or say which you prefer.
- Do not quote more than eight words of the paper, or of a reading, in a row.

## Output

Return a single JSON object and nothing else:

```json
{
  "paper": "the author's surname and the year",
  "readings": [
    {"reading": "M01", "claim": "C07", "other_claims": ["C02"],
     "passages": ["F31", "F40"], "alternative": "...", "none_note": ""}
  ],
  "groups": [
    {"group": "G1", "point": "...", "readings": ["M01", "M07"]}
  ]
}
```

Every reading of the file appears once under `readings` and once under
`groups`. Number the groups G1 onward. `none_note` is empty unless `claim` is
`none`.
