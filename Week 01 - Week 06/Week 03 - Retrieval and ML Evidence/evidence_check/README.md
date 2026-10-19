# evidence_check

Scores a Week 3 folder against `truth/gold/evidence.json`. Participants run it. They do not run `evidence_check.key`.

From `Week 01 - Week 06`:

```text
python -m course evidence_check --work <folder> [--data data] [--rerun]
python -m course evidence_check.questions --data <build> --out questions.jsonl
python -m course evidence_check.baseline --name keyword|tfidf --data <build> --out <file>
python -m course evidence_check.score --answers <file> [--data <build>] [--baseline]
python -m course evidence_check.key --data <build>
```

`--rerun` grades computed findings, answers, redactions, and the extract. It skips the contract, the card, and the note. `--baseline` waives the model-register check for the keyword and TF-IDF files.

Pass: 80 percent of items, 60 percent in every role, answers at 0.80 and 0.30 above the better baseline, refusal and injection complete, redaction recall 0.95 and precision 0.60, the extract rules, and 80 percent of the contract, card, and note facts with no banned sentence.
