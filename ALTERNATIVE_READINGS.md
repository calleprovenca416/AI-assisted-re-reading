# Alternative readings

The attached PDF is a published qualitative paper. Write alternative readings of
it: plausible re-tellings of the paper's own account that use its evidence in a
way the paper does not. Each reading is a wager: it says what the evidence would
support if read this way.

Write up to five readings. Give each in five fields:

1. **wager**: the reading, in plain prose.
2. **evidence**: the passages of the paper it rests on, each cited by the
   journal's page number, with what each passage does in the reading.
3. **what it would take to cohere**: the observation that would settle whether
   the reading holds, and whether the paper prints it.
4. **strains against**: what in the paper sits awkwardly with the reading, and
   why.
5. **who could complete it**: a kind of person or evidence, not a named
   individual.

Do not quote more than eight words of the paper in a row. Paraphrase, and cite
the page.

Return a single JSON object and nothing else:

```json
{
  "paper": "author and year, as the paper prints them",
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
