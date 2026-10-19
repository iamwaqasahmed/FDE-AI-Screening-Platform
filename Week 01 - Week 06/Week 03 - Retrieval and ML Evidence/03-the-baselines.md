# The baselines

**Day 1. Software engineer.** Two retrievers are already written. Both read the Markdown, score a question by word overlap, and ignore status, dates, and site. Your index has to beat them on the questions where that loses. It does not have to beat them on a slice they already answer.

Print the questions, then run each retriever. From `Week 01 - Week 06`:

```text
python -m course evidence_check.questions --data data --out questions.jsonl
python -m course evidence_check.baseline --name keyword --data data --out keyword.jsonl
python -m course evidence_check.baseline --name tfidf --data data --out tfidf.jsonl
python -m course evidence_check.score --answers keyword.jsonl --data data --baseline
python -m course evidence_check.score --answers tfidf.jsonl --data data --baseline
```

`--baseline` waives the model-register check. These two files are not a system you would ship. They are the floor. The score command prints a rate per slice and the ids that failed. It does not print the expected answer.

`--data` defaults to `data`. Point it at another build when you rerun.

## Stop. Read ten losses.

Open ten failed questions and the document the retriever cited. You are looking for the reason, not for a better vector. Sort what you find into the loss table in [the retrieval card](templates/retrieval-card.md). The reasons that show up here are a draft cited as if it bound, a superseded document, the wrong site, a fact that is only in the original, and a forwarded copy cited instead of the record.

Write the overall percent each command printed, as an integer, into the card. The checker looks for those two integers.

A technique earns its place only on a slice these two lost. If you add a dense embedding later, name the slice it moved. If it moved nothing, leave it out.

**A miss that looks like progress.** Swapping the retriever for vectors before you can say which slice moved.

**Finish.** `questions.jsonl` exists. Both baseline files have been scored. The loss table names the failures you read, and the card quotes both overall percents.

Next: [Index with status and dates](04-index-with-status-and-dates.md).
