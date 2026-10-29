# Two readings, written to a specification

The attached PDF is a published qualitative paper. Write two alternative readings of it, each about one of the paper's claims below, and each doing one particular thing to its claim. A claim's statement is a summary from an index of the paper, not the paper's words.

1. **About claim C05** (p. 606; p. 608; p. 617; p. 620; p. 625; pp. 627–628; p. 632; pp. 633–637): Occupational values filter evaluative comparisons: alignment with valued ways of doing good work supports adaptation, whereas a threat to those values promotes resistance. The reading must **invert** it: hold that the claim's outcome goes the other way under the condition the claim names, or that a process the claim states runs in the reverse order.

2. **About claim C04** (p. 606; p. 608; p. 617; p. 620; p. 625; pp. 627–628; p. 632; pp. 633–637): The technical compatibility between a benchmark technology and an occupation’s existing method shapes how feasible adaptation is, although compatibility by itself does not guarantee change. The reading must **complement** it: add a mechanism, a condition or a level to the claim, or change its scope, without denying it.

Write each as an alternative reading is written: a **wager** in plain prose, of 80 to 150 words, saying what the paper's evidence would support if read this way; and its **evidence**, the passages of the paper it rests on, each cited by the journal's page number, with what each passage does in the reading. Make it as plausible as the paper's evidence allows. Write it as a reading, not as an exercise: do not name the claim's number, and do not say what the reading does to the claim in the words above.

Do not quote more than eight words of the paper in a row. Paraphrase, and cite the page. Work only from the paper. Do not search the web.

Return a single JSON object and nothing else, as a file if you can, otherwise as one code block:

```json
{
  "paper": "author and year, as the paper prints them",
  "readings": [
    {
      "reading_id": "S1",
      "claim": "C05",
      "wager": "...",
      "evidence": [{"page": "p. ..", "job": "..."}]
    },
    {
      "reading_id": "S2",
      "claim": "C04",
      "wager": "...",
      "evidence": [{"page": "p. ..", "job": "..."}]
    }
  ]
}
```
