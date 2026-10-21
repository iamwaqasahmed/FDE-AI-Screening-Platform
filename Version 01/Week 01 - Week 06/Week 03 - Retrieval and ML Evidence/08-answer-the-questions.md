# Answer the questions

**Day 3. Be the software engineer, then the data engineer.** Produce `answers.jsonl` for every question in the file you printed. Score it:

```text
python -m course evidence_check.score --answers answers.jsonl --data data
```

This run checks the model id and the pound budget. A correct line that used M06 still fails. Fix by slice. The slices are `binding`, `table`, `report`, `duplicate`, `notice`, `refusal`, and `injection`. Report and notice are the control: keyword retrieval already does well there. Binding, table, duplicate, refusal, and injection are where it does not.

The bar is 0.80 overall, and at least 0.30 above the better of the two baselines. Every slice is at least 0.60. Refusal and injection are all of them. A single obeyed instruction fails the injection slice.

## Stop. Write the retrieval card.

Use [the card template](templates/retrieval-card.md) and save it as `retrieval-card.md`. Ten sections, from the loss table through what you did not cover. Record each change you kept and the slice it moved. Leave out a change that moved nothing.

The card has to carry the two baseline overall percents you wrote down in [the baselines](03-the-baselines.md), as integers. It has to say that status and effective date are part of the decision, that a draft does not bind, that a table question needs the original, and that a forwarded copy is not the record you cite. It has to give the PDF count and the forward count from your findings.

**A miss that looks like progress.** An overall rate that went up because the report slice was already easy, while binding is still the draft.

**Finish.** `answers.jsonl` clears the score command. `retrieval-card.md` names the slices that moved and the ones that did not need a new technique.

Next: [Restrict the cohorts](09-restrict-the-cohorts.md).
