# The baselines

**Day 3. Be the software engineer.** Two retrievers are already written. Both read one document and stop. Your Week 3 index does the same: it cites the document it ranked first. Several questions this week are wrong if that is all you cite.

Print the questions, then run each retriever. From `Week 01 - Week 06`:

```text
python -m course graph_check.questions --data data --out questions.jsonl
python -m course graph_check.baseline --name keyword --data data --out keyword.jsonl
python -m course graph_check.baseline --name tfidf --data data --out tfidf.jsonl
python -m course graph_check.score --answers keyword.jsonl --data data --baseline
python -m course graph_check.score --answers tfidf.jsonl --data data --baseline
```

`--baseline` waives the model-register check. These two files are the floor. Score your Week 3 answers on this question file as well, if you still have the index. It will lose where the answer is not in the document it cites.

`--data` defaults to `data`. Point it at another build when you rerun.

## Stop. Read ten losses.

Open ten failed questions and the document the retriever cited. Sort them by the hop that was missing.

- A second record. The local id is in the question. The request id, the dispatch count, and the hospital number are not.
- A second document. The document that cites, supersedes, or constrains another document. One of them is not enough.
- A second source. A notice and a ticket. A catalogue row and the file it describes. An agreement and a freeze.

Write the loss table in [the graph card](templates/graph-card.md). Write the overall percent each command printed, as an integer. The checker looks for those two integers.

A graph earns its place only on a slice these two lost. If you add an embedding later, name the slice it moved. If it moved nothing, leave it out.

**A miss that looks like progress.** Standing up a graph database before you can name the slice it will move.

**Finish.** `questions.jsonl` exists. Both baseline files have been scored. The loss table names the missing hop, and the card quotes both overall percents.

Next: [Build the graph](10-build-the-graph.md).
