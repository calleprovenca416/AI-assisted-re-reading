# Readings from given places

The attached PDF is a published qualitative paper. The attached `PLACES.md`
gives four places in it. Each place is a claim the paper makes and a passage of
the paper, with two readings of what the passage shows. Both readings have fair
ground in the paper.

For each place, write one alternative reading of the paper: a plausible
re-telling of the paper's own account that starts from this place and uses its
evidence in a way the paper does not. Each reading is a wager: it says what the
evidence would support if read this way.

Give each reading in six fields:

1. **place**: the place it starts from, as `PLACES.md` numbers it.
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
      "place": "Place 1",
      "wager": "...",
      "evidence": [{"page": "p. ..", "job": "..."}],
      "what_it_would_take_to_cohere": {"observation": "...", "printed": false, "pages": []},
      "strains_against": [{"page": "p. ..", "why": "..."}],
      "who_could_complete_it": "..."
    }
  ]
}
```
