# Checking each opening against its reading

You have one file besides this one: readings of a published paper, numbered
R01 onward, each followed by its opening, two sentences another reader wrote
of it. The first sentence says what the reading opens in the paper's
argument; the second names the next investigation that would settle it.

For each reading, answer one question: **does the opening say what the
reading says, and nothing it does not?**

## How to judge

- **The first sentence** fails if it misstates the reading: if it makes the
  reading claim more or less than it does, turns its point into another, or
  credits it with a point it does not make.
- **The second sentence** names an investigation, which the reading need not
  propose. It fails only if what it would settle is not what the reading
  says.
- Judge the opening against the reading alone. You do not have the paper:
  do not judge whether the reading is right, well supported or worth
  pursuing, nor whether the opening is well written.
- An opening that is right on one sentence and wrong on the other is not
  faithful.

## What to give for each reading

1. **faithful:** `true` if the opening says what the reading says and nothing
   it does not; otherwise `false`.
2. **reason:** one sentence: what the opening gets right or where it departs
   from the reading.

## Rules

- Check every reading in the file, once, in its order.
- Do not quote more than eight words of a reading or an opening in a row.
  Paraphrase.
- Work only from the file. Do not search the web.

## What to return

A single JSON object and nothing else, as a file if you can, otherwise as one
code block:

```json
{
  "paper": "author and year, as the file's title gives them",
  "checks": [
    {"reading": "R01", "faithful": true, "reason": "..."}
  ]
}
```
