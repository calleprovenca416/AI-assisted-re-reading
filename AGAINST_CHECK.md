# Checking `against` links

You will receive this file and one table, and nothing else. Each row of the
table pairs a claim from a published research paper with one piece of the
paper's evidence, summarised in a one-sentence **stub**. A coder has coded each
of these links `against`: the evidence runs against the claim.

Your job is to say, for each row, which kind of `against` it is, or that it is
none of them. Judge from the claim and the stub only. You do not see the paper
and do not need it. Set aside anything you know about the paper, its author or
its subject from elsewhere.

## The three kinds

A claim names a condition and an outcome, and asserts a direction: which way the
outcome goes when the condition holds. Evidence runs against a claim in one of
three ways.

1. **The condition was present, and the outcome went the other way.** The stub
   shows the claim's condition holding, and the outcome going the opposite way
   to the asserted direction.
2. **The outcome occurred without the condition.** The stub shows the outcome
   going the asserted way, and the stub shows the named cause absent.
3. **Another cause.** The stub shows the outcome going the asserted way, and
   the stub puts the outcome down to another cause, not to the condition.

If a row is none of these, answer 4 and add the letter that fits:

- **4a**: the outcome went the other way, and the stub shows the condition
  absent;
- **4b**: the outcome went the other way, and the stub says nothing about the
  condition;
- **4c**: the stub does not report the outcome at all;
- **4x**: anything else. Say what it is.

An absence you would have to infer does not count. A condition is absent only
if the stub shows it absent, and present only if the stub shows it present.
Keep the outcome's polarity as it is; do not re-sign it.

## An example

The claim: *time pressure makes cooks skip the tasting step*. The condition is
time pressure. The outcome is skipping the tasting step. The asserted direction:
under time pressure, cooks skip it.

| stub | answer |
|---|---|
| During the dinner rush, with every ticket overdue, a cook tastes every dish before it leaves. | 1 |
| A cook skips the tasting step on a slow afternoon with no orders waiting. | 2 |
| A cook skips the step because the recipe card has gone missing. | 3 |
| On a slow afternoon, a cook tastes every dish before it leaves. | 4a |
| A cook tastes every dish before it leaves. | 4b |
| The kitchen is quiet on a weekday afternoon. | 4c |

## What to give back

For every row, in the order given, write:

- the row's id;
- one line of reason that cites only what the stub says;
- your answer: 1, 2, 3, 4a, 4b, 4c or 4x.

Write the reason before you choose the answer. Put them in your reply as plain
text, one row per line, like this:

`R07 | the cook tastes every dish, and the stub says nothing about how busy the kitchen was | 4b`

Do not change the rows or recode the links. Say only which kind each one is. If
a row is genuinely unclear, give your best answer and add "| unclear" at the
end of its line.
