# Readings from places the paper leaves open

The attached PDF is a published qualitative paper. Find up to four places in it
where careful readers could read the same passage two ways, each reading with
fair ground in the paper.

For each place, write one alternative reading of the paper: a plausible
re-telling of the paper's own account that starts from this place and uses its
evidence in a way the paper does not. Each reading is a wager: it says what the
evidence would support if read this way.

Give each reading in six fields:

1. **place**: the passage, by the journal's page number, and the two readings
   of it, in a sentence each.
2. **wager**: the reading, in plain prose.
3. **evidence**: the passages of the paper it rests on, each cited by the
   journal's page number, with what each passage does in the reading.
4. **what it would take to cohere**: the observation that would settle whether
   the reading holds, and whether the paper prints it.
5. **strains against**: what in the paper sits awkwardly with the reading, and
   why.
6. **who could complete it**: a kind of person or evidence, not a named
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
      "place": {"page": "p. ..", "reading_one": "...", "reading_two": "..."},
      "wager": "...",
      "evidence": [{"page": "p. ..", "job": "..."}],
      "what_it_would_take_to_cohere": {"observation": "...", "printed": false, "pages": []},
      "strains_against": [{"page": "p. ..", "why": "..."}],
      "who_could_complete_it": "..."
    }
  ]
}
```
