# Judging statements about a paper

You have been given a paper, as a PDF, this file, and a table of statements
about the paper. The table comes in two parts. Part 1 comes first. Part 2 comes
once you have returned your answers to part 1.

## What to do

Each row of the table gives one statement: in part 1, about a claim the paper
makes; in part 2, about what a passage of the paper shows of a claim. For each
statement, answer one question:

**Could a careful reader of this paper, reading it closely and fairly, hold this
statement?**

| answer | use it when |
|---|---|
| `yes` | the paper gives the statement fair ground: a careful reader could hold it, even if you would read the paper otherwise |
| `no` | the paper rules the statement out, or gives it no ground |
| `unclear` | you cannot tell, for instance because you cannot find the passage; say why |

You are not asked which statement is best, or whether you agree with it. Two
statements in the table may say different things about the same claim or the
same passage. Judge each on its own: both, one or neither may have fair ground.

## How to judge

- **Judge from the paper.** Read each claim where the paper makes it, at the
  pages given, and each passage where the paper prints it.
- **A claim is given as a reader summed it up.** Where the summary and the paper
  differ, go by the paper.
- **In part 2, a passage is given by its page and by a reader's summary that
  points to it.** The summary only helps you find the passage. Judge what the
  passage itself shows, not the summary. Where the two differ, go by the passage.
- **In part 2, "what it says is affected" and "which way" are given as a reader
  recorded them.** Take them as given when you judge a statement about the
  passage.
- **Use nothing but the paper.** Do not search the web, and set aside what you
  know about the paper, its author or its subject from elsewhere.
- **Write your reason before your answer:** what in the paper the statement
  rests on or runs against, with the page, quoting a few words at most.

## Output

For each part, return one JSON object, as a file if you can, otherwise as one
code block:

```json
{
  "part": 1,
  "answers": [
    {"row": "ABCD", "reason": "...", "page": "p. ..", "answer": "yes"}
  ]
}
```

Give every row of the part, in the order of the table. `page` is where you found
what your reason rests on, several separated by semicolons, or null. `answer` is
`yes`, `no` or `unclear`.

If a reply stops before the object is complete, you will be asked to continue:
carry on from the row where you stopped.
