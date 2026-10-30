# 08 — The advanced path

Open this chapter after [10 — Finish](10-finish.md) prints `passed`. Those three checks do not read these replacements. The shells stay in `work/` until you paste. Do not delete them. If the lesson is out of time, leave the shells and open the next release the finish chapter names.

[Chapter 07](07-the-sample.md) replaced the sample and the scan. This chapter replaces the invite-time features and the label budget, then runs the suite.

The three checks do not import `pit.py` or `budget.py`. Replace both after those checks print `passed`. Do not delete them. When the files are present, the suite compares them with the invite cutoff and the budget. A missing file would fail this suite. It would not, by itself, fail the three checks. Leave the files in `work/app`.

You replace four files under `work/`, in this order:

1. [pit.py](work/app/pit.py), under Replace the features
2. [test_pit.py](work/tests/test_pit.py), under Replace the feature test
3. [budget.py](work/app/budget.py), under Replace the budget
4. [test_budget.py](work/tests/test_budget.py), under Replace the budget test

Paste only those four blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.

Scroll down to the heading Replace the features. It is the first heading on this page that starts with Replace. Use the four steps from [chapter 05](05-the-sprint.md) on each one. The section How the replacement works sits above the first Replace heading. Read it. Do not paste it. Every code block above that Replace heading is a picture or a check. You do not paste those.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, run `prepare_work.py` from the course folder and paste chapters 05 through 08 again from the chapter source. Do not repair the spaces by hand.

## Read these files

You are reading. You are not pasting yet.

Open [labels.json](packet/release/budget/labels.json). Search for `price`. The next block is a picture of that file. Do not paste it. `price` is the cost of one label. `sar` is the budget. The test below uses those two numbers. Do not type them into `pit.py`.

```text
{
  "price": 2,
  "sar": 6
}
```

1. [pit.py](packet/app/pit.py). Search for `del invite_on`. That line is the shell. The latest row wins, even when it is after the invite. The next block is a picture of that file. Do not paste it.

```text
"""Join the latest feature row.

This is the shell. Chapter 08 replaces the copy under work/app.
Leave this file in the packet unchanged.

features ignores the invite time and keeps the latest as_of.
The three checks do not call this file. The suite does.
"""

from __future__ import annotations


def features(rows: list[dict], invite_on: str) -> dict:
    """Return the district and insurance on the latest row.

    rows are the feature history. invite_on is ignored. The row
    with the greatest as_of is kept, even when it is after the
    invite.
    """
    del invite_on
    chosen = max(rows, key=lambda row: row["as_of"])
    return {"district": chosen["district"], "insurance": chosen["insurance"]}
```

2. [budget.py](packet/app/budget.py). Search for `del price, budget_sar`. That line is the shell. Every item is returned. The next block is a picture of that file. Do not paste it.

```text
"""Spend the label budget in list order.

This is the shell. Chapter 08 replaces the copy under work/app.
Leave this file in the packet unchanged.

spend returns every item and ignores the price and the budget.
The three checks do not call this file. The suite does.
"""

from __future__ import annotations


def spend(items: list[dict], price: float, budget_sar: float) -> list[str]:
    """Return every item id. Price and budget are ignored."""
    del price, budget_sar
    return [item["item_id"] for item in items]
```

Open [ci.yml](work/.github/workflows/ci.yml) and search inside that file, not inside this chapter. Press Ctrl+F there and type `unittest`. You should find it. The packet copy has the same line. You do not edit either file. If you cannot see the `.github` folder, it is hidden. The link still opens the file.

The pictures end here. The next heading is How the replacement works. Read it. It is not a paste. The first paste is the next heading that starts with Replace.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

The three checks do not call these files. The suite does. Do not delete them.

`features` keeps the latest row whose date is on or before the invite. A row after the invite is left out. The invite is the decision moment. A later district was not known then. Module 1 called that kind of cheat leakage: the result looks informed by a fact that had not happened. The shell kept the latest row in the file and ignored the invite, so a June district leaked into a March decision. The test's invite is `2026-03-01`. The January district `d-rim` is the one on or before that date. The result is the district and the insurance on the chosen row. No row early enough means an empty result.

`spend` buys labels where the current label is least sure. Uncertainty is that number on the item. The sort is uncertainty descending, then item id. The price of one label comes from the budget file. The function stops before the next price would pass the budget. At price 2 and budget 6, that is three items: `higher`, `high`, and `mid`. `low` stays in the list and stays out of the result. Outside this folder that spend is sometimes called active learning. The file's word is uncertainty. The shell returned every item and ignored the price.

Before you paste, say which date `features` is not allowed to see, and when `spend` stops.

This section adds no file and no command.

## Replace the features

This block replaces [work/app/pit.py](work/app/pit.py). The full path is `Module 03/Lesson 01/Student_Copy/work/app/pit.py`. It does not replace [packet/app/pit.py](packet/app/pit.py). It does not replace the test.

Open the work file. Select the whole file and delete it. Copy the lines inside the block below from this chapter file. Use Paste Without Formatting. Do not copy the backtick lines. Paste. Save.

```text
"""Features as of the invite time.

Chapter 08 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell keeps the latest row and ignores the invite time. The
three checks do not call this file. The suite does. When the file
is present, the invite date is the cutoff.
"""

from __future__ import annotations


def features(rows: list[dict], invite_on: str) -> dict:
    """Keep the latest row that is on or before the invite.

    rows are the feature history. invite_on is the invite date.
    A row after that date is left out. The result is the district
    and the insurance on the chosen row. No row early enough means
    an empty result.
    """
    chosen = None
    for row in rows:
        # Later than the invite is not a feature of the invite.
        if row["as_of"] <= invite_on and (chosen is None or row["as_of"] > chosen["as_of"]):
            chosen = row
    if chosen is None:
        return {}
    return {"district": chosen["district"], "insurance": chosen["insurance"]}
```

Open the work file you just saved. Search inside that file, not inside this chapter. You should see `<= invite_on`. You should not see `del invite_on`. If you see `del invite_on`, you pasted the picture. Paste this block again.

## Replace the feature test

This block replaces [work/tests/test_pit.py](work/tests/test_pit.py). The full path is `Module 03/Lesson 01/Student_Copy/work/tests/test_pit.py`. It does not replace the packet test.

Open the work file. Select the whole file and delete it. Copy the lines inside the block below from this chapter file. Use Paste Without Formatting. Do not copy the backtick lines. Paste. Save.

```text
"""The invite date keeps the earlier district.

Chapter 08 replaces the work copy with this file. Leave the packet
shell test unchanged.

The shell test expects the June row. This test expects the January
row, because the invite is in March. The line parents[1] stays as
it is.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from pit import features

ROWS = (
    {"as_of": "2026-01-01", "district": "d-rim", "insurance": "class-a"},
    {"as_of": "2026-06-01", "district": "d-wadi", "insurance": "class-b"},
)


class PitTests(unittest.TestCase):
    """The invite date keeps the earlier district."""
    def test_invite_time_keeps_the_earlier_district(self) -> None:
        """March keeps January. June is after the invite."""
        found = features(list(ROWS), "2026-03-01")
        self.assertEqual(found, {"district": "d-rim", "insurance": "class-a"})


if __name__ == "__main__":
    unittest.main()
```

Open the work file you just saved. Search inside that file, not inside this chapter. You should see `test_invite_time_keeps_the_earlier_district`. You should see `parents[1]`. Leave that line. `2026-06-01` is still in the rows. That row is after the invite. The result is `d-rim`. That is expected.

## Replace the budget

This block replaces [work/app/budget.py](work/app/budget.py). The full path is `Module 03/Lesson 01/Student_Copy/work/app/budget.py`. It does not replace [packet/app/budget.py](packet/app/budget.py). It does not replace the test.

Open the work file. Select the whole file and delete it. Copy the lines inside the block below from this chapter file. Use Paste Without Formatting. Do not copy the backtick lines. Paste. Save.

```text
"""Spend the label budget on the uncertain items.

Chapter 08 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell returns every item and ignores the price. The three
checks do not call this file. The suite does. When the file is
present, spending stops before the next price would pass the budget.
"""

from __future__ import annotations


def spend(items: list[dict], price: float, budget_sar: float) -> list[str]:
    """Buy the least certain items until the next price would not fit.

    items carry item_id and uncertainty. price is the cost of one
    label. budget_sar is the budget. The sort is uncertainty
    descending, then item_id. A tie on uncertainty keeps item_id
    order. The loop stops before spent plus price would pass the
    budget.
    """
    ordered = sorted(items, key=lambda item: (-item["uncertainty"], item["item_id"]))
    chosen = []
    spent = 0.0
    for item in ordered:
        # The next label would pass the budget, so stop.
        if spent + price > budget_sar:
            break
        chosen.append(item["item_id"])
        spent += price
    return chosen
```

Open the work file you just saved. Search inside that file, not inside this chapter. You should see `uncertainty`. You should not see `del price, budget_sar`. If you see that line, you pasted the picture. Paste this block again.

## Replace the budget test

This block replaces [work/tests/test_budget.py](work/tests/test_budget.py). The full path is `Module 03/Lesson 01/Student_Copy/work/tests/test_budget.py`. It does not replace the packet test.

Open the work file. Select the whole file and delete it. Copy the lines inside the block below from this chapter file. Use Paste Without Formatting. Do not copy the backtick lines. Paste. Save.

```text
"""Uncertain items are bought until the budget stops.

Chapter 08 replaces the work copy with this file. Leave the packet
shell test unchanged.

The shell test expects every item in list order. This test expects
the three least certain items, and not the low item. The line
parents[1] stays as it is.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from budget import spend

ITEMS = (
    {"item_id": "low", "uncertainty": 0.1},
    {"item_id": "mid", "uncertainty": 0.5},
    {"item_id": "high", "uncertainty": 0.9},
    {"item_id": "higher", "uncertainty": 0.95},
)


class BudgetTests(unittest.TestCase):
    """Uncertain items are bought until the budget stops."""
    def test_uncertain_items_stay_inside_the_budget(self) -> None:
        """Price 2 and budget 6 buy three items, highest uncertainty first."""
        self.assertEqual(spend(list(ITEMS), 2, 6), ["higher", "high", "mid"])


if __name__ == "__main__":
    unittest.main()
```

Open the work file you just saved. Search inside that file, not inside this chapter. You should see `test_uncertain_items_stay_inside_the_budget`. You should see `parents[1]`. Leave that line. `low` is still in the item list. It is not in the result. That is expected. The numbers `2` and `6` match `price` and `sar` in the budget file.

## Search before the suite

These strings exist in the replaced work files. A pasted picture fails the search. Open the work file named in the row. A match in this chapter does not count. A match in `packet/` does not count.

| Work file | Search for this | You should find it |
| --- | --- | --- |
| [dates.py](work/app/dates.py) | `return _from_hijri(value).isoformat()` | Yes. `_hijri_jd` is still in the file. That is expected |
| [codes.py](work/app/codes.py) | `2024-06-01` | Yes. `END-01` is still in the set. That is expected |
| [cluster.py](work/app/cluster.py) | `death-late` | Yes. You should not see `return len(rows)` |
| [labels.py](work/app/labels.py) | `ann-v2` | Yes. `scan` is still a source type. That is expected |
| [synthetic.py](work/app/synthetic.py) | `rare_sub_specialty` | Yes. You should not see `letters[:1]` |
| [scan.py](work/app/scan.py) | `CANARY-` | Yes. A clean line is still accepted. That is expected |
| [pit.py](work/app/pit.py) | `<= invite_on` | Yes. You should not see `del invite_on` |
| [budget.py](work/app/budget.py) | `uncertainty` | Yes. You should not see `del price, budget_sar` |
| [test_dates.py](work/tests/test_dates.py) | `test_month_boundary_stays_on_the_civil_day` | Yes |
| [test_codes.py](work/tests/test_codes.py) | `test_wadi_endo_changes_in_june_2024` | Yes |
| [test_cluster.py](work/tests/test_cluster.py) | `test_newborn_twins_and_a_reused_mrn_stay_split` | Yes |
| [test_labels.py](work/tests/test_labels.py) | `test_photo_and_retina_follow_ann_v2` | Yes |
| [test_synthetic.py](work/tests/test_synthetic.py) | `test_rare_class_has_no_real_id` | Yes. `clerk-row` is a stand-in. That is expected |
| [test_scan.py](work/tests/test_scan.py) | `test_watermark_and_national_id_are_refused` | Yes |
| [test_pit.py](work/tests/test_pit.py) | `test_invite_time_keeps_the_earlier_district` | Yes |
| [test_budget.py](work/tests/test_budget.py) | `test_uncertain_items_stay_inside_the_budget` | Yes |

If a row fails, you pasted a picture or you skipped that file. The date, code, and cluster rows are the blocks in [chapter 06](06-the-clusters.md). The label, sample, and scan rows are the blocks in [chapter 07](07-the-sample.md). The feature and budget rows are the blocks above. Paste the failed row's block again from that chapter. Search the work file, not the packet file.

## Run the suite

Leave the window you used for the demo. That window is inside `problem_simulation`, and this command is not. Open a new terminal in the course folder, the same way as chapter 01. `dir` should list `problem_simulation` and `Module 02`. If chapter 01 told you to use `py`, use `py` here.

```text
cd "Module 03/Lesson 01/Student_Copy/work"
python -m unittest discover -s tests -q
```

If the `cd` line says the path cannot be found, this window is not the course folder. Open a new one and run both lines again. Do not chain `cd ..` to climb out of another folder.

You should see a line that starts with `Ran 8 tests`, then a blank line, then `OK`. A line of dashes can sit above the `Ran` line. The time on the `Ran` line can differ. There is no `FAIL` and no `ERROR`. The prompt returns after `OK`.

If the line says `FAIL` or `ERROR`, a work file is still the shell, or a paste broke the indentation. Use the search table. Paste the failed file again from the chapter that owns it. If the terminal says `SyntaxError` or `IndentationError`, run this from the course folder:

```text
python "Module 03/Lesson 01/Student_Copy/prepare_work.py"
```

That puts the shells back. Paste chapters 05, 06, 07, and 08 again from the chapter source. Then run the suite again.

The suite does not read the pages. A green suite can still fail the checks in chapter 10. The three checks do not import `pit.py` or `budget.py`. The suite does. Leave both files in place.

This page is done when the suite prints `Ran 8 tests` and `OK`, and `work/app/pit.py` contains `<= invite_on`, and `work/app/budget.py` contains `uncertainty`. The packet copies still ignore the invite and return every item. That is expected.

Next: when this page's suite is green, open the next folder [10 — Finish](10-finish.md) names. The pages and the finish come before this chapter on the required path.
