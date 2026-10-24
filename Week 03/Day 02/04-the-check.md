# The check

From `problem_simulation`, with your work directory filled in:

```text
python -m alwaha.check model --release rel-w3d2 --work "..\Week 03\Day 02\work"
python -m alwaha.check lora --release rel-w3d2 --work "..\Week 03\Day 02\work"
```

`chk-w3-model` scores the adapter on the held-out slice, the cost, the latency, the quota, and the residency note. A miss says the prompt baseline is still the served model, extraction F1 is outside the budget, intent F1 is outside the budget, the cost is over the price cap, the call sends phi to ext-large, the hash is not on reg-models, the gpu count is over the quota, hours questions are not left on retrieval, or dna is not a tabular model. It does not print a hash, a GPU count, a price, an F1, or a gold label.

`slice-lora` passes when the registered adapter clears the floor and the prompt baseline does not. An `ext-large` call at the published token count fails the cap. If the prompt path is pointed at the adapter, the miss says the prompt baseline clears the slice.

A watermarked file copied into `work/` fails the check. The message does not print the watermark.

On `practice`, the instructor can show the gateway refusal:

```text
python -m alwaha.demo.gateway --profile practice
```

The line says the gateway refused the prompt. It does not print the watermark.

Then write `work/knowledge.md` from [templates/knowledge.md](templates/knowledge.md), with two short answers:

1. Which problem stays on retrieval?
2. Which hash is legal to serve?

The day is done when both checks print `passed` and the knowledge file has both answers.
