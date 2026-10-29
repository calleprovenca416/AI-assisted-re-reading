# Alternative readings, from the citation alone

The message names a published qualitative paper by its citation. You are not
given the paper. Write alternative readings of it from what you know of it:
plausible re-tellings of the paper's own account that use its evidence in a
way the paper does not. Each reading is a wager: it says what the evidence would
support if read this way.

First say, in one or two sentences, what you know of this paper and how sure
you are (the field `what_you_know`). If you do not know it, say so, and write
the readings you can.

Write up to five readings. Give each in five fields:

1. **wager**: the reading, in plain prose.
2. **evidence**: the passages of the paper it rests on, as you recall them,
   each with the journal's page number where you recall it, and with what
   each passage does in the reading.
3. **what it would take to cohere**: the observation that would settle whether
   the reading holds, and whether the paper prints it.
4. **strains against**: what in the paper sits awkwardly with the reading, and
   why.
5. **who could complete it**: a kind of person or evidence, not a named
   individual.

Do not quote more than eight words of the paper in a row. Paraphrase, and cite
the page where you recall it.

Return a single JSON object and nothing else:

```json
{
  "paper": "author and year, as the citation gives them",
  "what_you_know": "...",
  "readings": [
    {
      "reading_id": "R1",
      "wager": "...",
      "evidence": [{"page": "p. ..", "job": "..."}],
      "what_it_would_take_to_cohere": {"observation": "...", "printed": false, "pages": []},
      "strains_against": [{"page": "p. ..", "why": "..."}],
      "who_could_complete_it": "..."
    }
  ]
}
```
