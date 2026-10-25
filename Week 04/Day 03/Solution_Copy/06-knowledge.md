# 06 — Knowledge

[knowledge.md](work/knowledge.md) has two numbered lines.

1. Reactive scaling misses the first minutes because the cold start is still running.
2. The price change punished sending the batch to ext-large.

Both answers stay on their numbered lines. `1. Yes.` does not count. A second sentence on the next line, without a number, does not count as the second answer.

Fewer than two numbered lines makes the slo check say `knowledge.md needs two answers`. A first line that misses `cold` makes it say `knowledge.md does not say why reactive scaling misses the first minutes`. A second line that misses `ext-large` makes it say `knowledge.md does not say what the price change punished`. A knowledge miss fails only the slo check.

The trainer's session is [chapter 07](07-trainer.md). Students can skip it.
