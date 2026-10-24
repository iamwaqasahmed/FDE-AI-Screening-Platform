# The index

Copy [app](app) to `Week 03/Day 03/work/app`. Copy [tests](tests) to `Week 03/Day 03/work/tests`. Leave the copies in this folder unchanged, and edit the copies.

The same tests sit in both folders. They fail on the shell. They pass on the copy once the shell's choices are fixed.

The shell embed gives every text the same vector. The shell index is empty. The shell chunk drops the clause id. The shell search ranks by that vector and keeps every status, including a draft and an unauthorized document.

Read the dev questions in [slices/retrieve.jsonl](../../data/rel-w3d3/slices/retrieve.jsonl). They have no answers. Index the snapshot, then apply the change feed. `local-embed` is the vector. A code in the question is a lexical hit.

From `work`:

```text
python -m unittest discover -s tests -q
```
