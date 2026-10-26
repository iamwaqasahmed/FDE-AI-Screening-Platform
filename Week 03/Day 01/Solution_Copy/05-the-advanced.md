# 05 — The advanced path

Open the finished [pit.py](work/app/pit.py) and [budget.py](work/app/budget.py) and put them beside yours.

The three checks do not import these files. They can be absent and the three checks still pass. This finished folder keeps them. Do not delete them. When they are present, they have to keep the invite cutoff and the budget spend. The suite is what compares them.

## Features

`features` keeps the latest row whose `as_of` is on or before the invite date. A later row is left out. The result is the district and the insurance. No row early enough means an empty result.

The shell ignores the invite and keeps the latest `as_of`. On the test rows, that is the June district. The filled test uses invite `2026-03-01` and expects the January district `d-rim`.

## Budget

[labels.json](sources/release/budget/labels.json) has `price` and `sar`. The filled test uses price 2 and budget 6, which are the practice numbers in that file. `spend` sorts by uncertainty descending, then `item_id`, and stops before the next price would pass the budget. At that price and budget the result is `higher`, `high`, and `mid`. `low` stays in the item list and stays out of the result. That is expected.

The shell returns every item and ignores the price and the budget.

The workflow file is the same bytes as the packet. It runs the suite. It was copied and not replaced.

## The path through the files

The morning chapter [08-the-advanced.md](../Student_Copy/08-the-advanced.md) has the section How the replacement works. That section is the path through the files this page compares. Read it beside the finished file. The notes above are the decisions the check names.

Next: [06 — The pages](06-the-pages.md).
