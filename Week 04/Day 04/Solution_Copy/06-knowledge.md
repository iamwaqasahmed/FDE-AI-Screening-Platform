# 06 — Knowledge

[knowledge.md](work/knowledge.md) has two numbered lines.

1. Status reads still work when the model is down, and a booking offer falls back to the rules worker.
2. Renting wins the deadline because a 16-week purchase misses 8 February.

Both answers stay on their numbered lines. The first numbered line contains status. The second contains rent. `1. Yes.` does not count. A second sentence on the next line, without a number, does not count as the second answer.

A first line that misses status makes the slo check say `knowledge.md does not say what still works when the model is down`. A second line that misses rent makes it say `knowledge.md does not say why renting wins the deadline`. There is no separate line that says the file needs two answers. A knowledge miss fails `chk-w4-slo`.

The trainer's session is [chapter 07](07-trainer.md). Students can skip it.
