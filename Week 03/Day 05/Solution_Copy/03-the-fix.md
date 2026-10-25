# 03 — The fix

Open the three finished files and put them beside yours. The shell is the file that makes the eval check name the miss. The filled file is the one in this folder.

## Repair

The shell leaves every citation as it was scored. That shell makes the eval check say the repair leaves the unauthorized citation, and the second run does not move the retrieval failure, because the second run calls this function.

[repair.py](work/app/repair.py) replaces one document id and copies every other field. The unauthorized id stays on the comparison line. That is expected. It is the value being replaced. [before.jsonl](sources/release/slices/before.jsonl) has outputs and no label field. A miss does not print a doc id.

## Second run

The shell reports the first score again. That shell makes the eval check say the second run does not move the retrieval failure. A higher pair that is not the held-out pair makes the eval check say the second run misses the held-out slice. The message does not print the rates.

[remeasure.py](work/app/remeasure.py) scores the slice, calls `repair`, and scores the slice again. The name `before` stays. That is expected. It is the first score. The function does not return a made-up pair.

## Label cost

The shell charges nothing for the fix. That shell makes the eval check say the improvement cost misses the price sheet. The message does not print a price.

[cost.py](work/app/cost.py) multiplies the label count by the label price, and returns nothing when that total is over the budget. [prices.csv](sources/release/finance/prices.csv) holds `cost.label`. [labels.json](sources/release/budget/labels.json) holds the annotation budget. Read the amounts there. GPU hours are not the cost of this fix.

Next: [04 — The spec](04-the-spec.md).
