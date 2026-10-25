# 07 — Knowledge

Open the finished [knowledge.md](work/knowledge.md) and put it beside yours.

The check needs two numbered lines. A second sentence wrapped onto the next line does not count. Fewer than two numbered lines says `knowledge.md needs two answers`.

## Which problem stays on retrieval?

Hours questions for p-info stay on retrieval.

[ruling.md](sources/release/notices/ruling.md) says hours questions stay on retrieval. [hours.jsonl](sources/release/slices/hours.jsonl) is that slice. It is not a model call. The first numbered line has to contain a retrieval word and either `hour` or `p-info`. The finished line has both. While it does not, the check says `knowledge.md does not say which problem stays on retrieval`.

## Which hash is legal to serve?

The legal hash is lora-local on reg-models.

[reg-models.json](sources/release/registry/reg-models.json) is the register. The row whose id is `lora-local` and whose status is `approved` is the one that may be served. The second numbered line names that row. It does not print the hash. While the line is missing `lora-local` or `reg-models`, the check says `knowledge.md does not say which hash is legal to serve`.

The checks do not read the interview notes.

Next: [08 — Trainer session](08-trainer.md). Students can skip that page.
