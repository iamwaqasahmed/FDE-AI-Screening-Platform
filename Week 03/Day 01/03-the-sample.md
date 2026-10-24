# The sample

Read [guidelines/ann-v1.md](../../data/rel-w3d1/guidelines/ann-v1.md) and [guidelines/ann-v2.md](../../data/rel-w3d1/guidelines/ann-v2.md). The development labels are [letters/adjudicated.jsonl](../../data/rel-w3d1/letters/adjudicated.jsonl). The clerk file is [letters/clerk.jsonl](../../data/rel-w3d1/letters/clerk.jsonl). Do not copy the clerk file into `work/`. It carries a watermark.

The shell copies ann-v1. ann-v2 sets the source type and the sub-specialty from the text.

Read [cards/fidelity.json](../../data/rel-w3d1/cards/fidelity.json) and [budget/labels.json](../../data/rel-w3d1/budget/labels.json). The shell copies a real letter. The sample has to sit inside the card, include the rare sub-specialty, and carry no national id and no watermark.

The shell scan accepts every file. Scan before you share.

The architect copies [templates/classes.md](templates/classes.md) to `work/classes.md`. National id, date of birth, name, and phone are phi.

`pit.py` joins features as of the invite time. `budget.py` spends the label budget on the uncertain rows. Those two are the advanced path. The three checks do not require them.
