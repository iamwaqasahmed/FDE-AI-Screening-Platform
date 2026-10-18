# graph_check

Scores a Week 4 folder against `truth/gold/graph.json`. Participants run it. They do not run `graph_check.key`.

From `Version 02`:

```text
python -m course graph_check --work <folder> [--data data] [--rerun]
python -m course graph_check.questions --data <build> --out questions.jsonl
python -m course graph_check.baseline --name keyword|tfidf --data <build> --out <file>
python -m course graph_check.score --answers <file> [--data <build>] [--baseline]
python -m course graph_check.key --data <build>
```

`--rerun` grades computed findings, answers, the reconciliation, and the re-send. It skips the contract, the card, and the note. `--baseline` waives the model-register check for the keyword and TF-IDF files.

Pass: 80 percent of items, 60 percent in every role, answers at 0.80 and 0.30 above the better baseline, refusal and injection complete, the reconciliation and the re-send, and 80 percent of the contract, card, and note facts with no banned sentence.
