# The ruling

The morning is a stand-up. You have the Week 1 and Week 2 packs, the Day 1 shell, and nothing from later.

Open the release readme, [data/rel-w3d2/README.md](../../data/rel-w3d2/README.md). Then read:

1. [notices/ruling.md](../../data/rel-w3d2/notices/ruling.md)
2. [registry/reg-models.json](../../data/rel-w3d2/registry/reg-models.json)
3. [budget/quota.json](../../data/rel-w3d2/budget/quota.json)
4. [budget/price-cap.json](../../data/rel-w3d2/budget/price-cap.json)

From `problem_simulation`:

```text
python -m alwaha.interview --persona dpo --script "..\Week 03\Day 02\work\interviews\dpo.questions.txt"
python -m alwaha.interview --persona finance --script "..\Week 03\Day 02\work\interviews\finance.questions.txt"
```

Ask the DPO about patient data, then the ruling, then whether it is signed. Ask finance about the budget, then renting a GPU, then the quota and the cap. Write what you hear. The interview does not state the GPU count. That count is on the release.

The lead copies [templates/sprint.md](templates/sprint.md) to `work/sprint.md`. The order is the baseline, then the adapter, then the register, then the memo. The cloud fine-tune is closed.
