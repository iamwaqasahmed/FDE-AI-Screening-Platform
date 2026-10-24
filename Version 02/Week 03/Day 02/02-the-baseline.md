# The baseline

Copy [app](app) to `Week 03/Day 02/work/app`. Copy [tests](tests) to `Week 03/Day 02/work/tests`. Leave the copies in this folder unchanged, and edit the copies.

The same tests sit in both folders. They fail on the shell. They pass on the copy once the shell's choices are fixed.

The shell sends national id, date of birth, name, and phone to `ext-large`. It prices that call from `price.ext_large_per_1k`, which is over the cap in [budget/price-cap.json](../../data/rel-w3d2/budget/price-cap.json).

Score extraction and intent on the dev slices:

- [slices/letters.jsonl](../../data/rel-w3d2/slices/letters.jsonl)
- [slices/messages.jsonl](../../data/rel-w3d2/slices/messages.jsonl)

A prompt on `local-small` that always types a letter and always calls a message `status` stays under the F1 floor. Do not serve that prompt.

Hours questions are in [slices/hours.jsonl](../../data/rel-w3d2/slices/hours.jsonl). They are not a model call.

From `work`:

```text
python -m unittest discover -s tests -q
```
