# 08 — The advanced path

[Chapter 07](07-the-adapter.md) registered the adapter. This chapter replaces the rank fit, the domain filter, and the preference edit. Then you run the suite.

You replace three files under `work/`, in this order:

1. [qlora.py](work/app/qlora.py), under Replace the rank fit
2. [domain.py](work/app/domain.py), under Replace the domain filter
3. [prefs.py](work/app/prefs.py), under Replace the preference edit

Paste only those three blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged. Do not paste a test. The tests are copied and not replaced.

Scroll down to the heading Replace the rank fit. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. Two more Replace headings follow it. Use the four steps from [chapter 05](05-the-sprint.md) on each one. The section How the replacement works sits above the first Replace heading. Read it. Do not paste it. Every code block above that Replace heading is a picture or a check. You do not paste those.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, run `prepare_work.py` from the course folder and paste chapters 05 through 08 again from the chapter source. Do not repair the spaces by hand.

The two checks do not require these three files. You still replace them. You do not delete them. The suite imports them. A deleted file fails the suite.

Do not run a check on this page. The checks are only in [chapter 10](10-finish.md).

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the comment at the top of each one. Do not edit them. The first block you copy is under Replace the rank fit, further down this page.

Open [ds-domain.jsonl](packet/release/domain/ds-domain.jsonl) and [ds-prefs.jsonl](packet/release/prefs/ds-prefs.jsonl). A domain line has `text` and no item id. The preference pair has `draft` and `edited`.

1. [qlora.py](packet/app/qlora.py). Search for `Spend a full LoRA rank`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/qlora.py](work/app/qlora.py) is under Replace the rank fit.

```text
"""Spend a full LoRA rank, even when the quota is smaller.

fit ignores the GPU quota. It turns the requested rank into a
GPU count in groups of eight, and it never asks for fewer than
one GPU. The method name on the result is lora. The rank is
returned unchanged.
"""

from __future__ import annotations


def fit(rank: int, gpus: int) -> dict:
    """Turn the rank into a LoRA GPU count and leave the quota unread.

    rank is the requested rank and is copied into the result.
    gpus is not read, so a smaller quota does not lower the
    count. The count is at least one, and it steps up by one
    GPU for each group of eight ranks. The method is lora.
    """
    # Round the rank up into groups of eight, and keep at least one GPU.
    need = max(1, (rank + 7) // 8)
    return {"gpus": need, "method": "lora", "rank": rank}
```

2. [domain.py](packet/app/domain.py). Search for `Train on every row`. That sentence is the shell. The next block is a picture of that file. Do not paste it.

```text
"""Train on every row, including the extraction letters.

keep copies the whole list and returns it in the same order. A
row that carries an item id stays beside a row that does not.
Nothing is filtered.
"""

from __future__ import annotations


def keep(rows: list[dict]) -> list[dict]:
    """Return every row, in the same order.

    rows may mix domain lines and extraction letters. This
    function does not look at keys. The new list holds the same
    row objects.
    """
    # A new list, with every row kept.
    return list(rows)
```

3. [prefs.py](packet/app/prefs.py). Search for `Return the coordinator draft unchanged`. That sentence is the shell. The next block is a picture of that file. Do not paste it.

```text
"""Return the coordinator draft unchanged.

revise returns the same string it was given. No word is expanded
and no word is removed.
"""

from __future__ import annotations


def revise(draft: str) -> str:
    """Return the draft as it arrived.

    draft is the coordinator sentence. This function does not
    scan it.
    """
    # The sentence is handed back with every word still in place.
    return draft
```

The pictures end here. The next heading is How the replacement works. Read it. It is not a paste. The first paste is the next heading that starts with Replace.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

The two checks do not load these files. The suite does. Do not delete them.

`fit` is the QLoRA path. It does not train a network. It maps a rank onto a GPU count. Thirty-two ranks share one GPU. The GPU count is the smaller of what the rank needs and what the quota allows. The requested rank is kept. Rank 32 still fits the one GPU in the quota file. The shell spent a full LoRA rank even when the quota was smaller, and it named the method `lora`.

`keep` keeps a domain line only when the row has no item id. A domain line is unlabeled text. An extraction letter carries an item id and is a different job, so it is left out. The shell trained on every row, including those letters.

`revise` expands "sugar clinic" to endocrinology and leaves the clause id in place. `crit-endo-v3` is the endocrinology clause from Week 1 Day 3. The function drops the word Friday and the token `2027-03-10` by replacing them with spaces. It does not call the Week 1 calendar. The word `the` stays, so the line reads `the endocrinology`. That wording is what the test expects. Do not tidy it into a smoother sentence. The shell returned the coordinator draft unchanged.

Before you paste, say what `fit` is not allowed to exceed, and which rows `keep` throws away.

This section adds no file and no command.

## Replace the rank fit

This block replaces [work/app/qlora.py](work/app/qlora.py). The full path is `Week 03/Day 02/Student_Copy/work/app/qlora.py`. It does not replace the packet copy.

Open that work file. The path must contain `Student_Copy\work`. If the path contains `packet`, close it. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. Copy the lines inside the block below. Do not copy the backtick lines. Paste. Save.

```text
"""Fit a higher rank in the same GPU count.

Chapter 08 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell spends a full LoRA rank even when the quota is smaller.
The two checks do not load this file. The suite does. Do not delete
it.
"""

from __future__ import annotations


def fit(rank: int, gpus: int) -> dict:
    """Return a QLoRA fit that does not ask for more GPUs than gpus.

    rank is the requested rank. gpus is the quota count. Thirty-two
    ranks share one GPU. The GPU count is the smaller of the need
    and the quota. The requested rank is kept.
    """
    # One GPU covers ranks 1 through 32. The next band needs another.
    need = max(1, (rank + 31) // 32)
    # The quota wins when the band would ask for more GPUs.
    return {"gpus": min(need, gpus), "method": "qlora", "rank": rank}
```

Open [work/app/qlora.py](work/app/qlora.py). Search inside that file, not inside this chapter. You should see `(rank + 31) // 32`. You should not see `(rank + 7) // 8`. If you see the second line, you pasted the picture.

## Replace the domain filter

This block replaces [work/app/domain.py](work/app/domain.py). The full path is `Week 03/Day 02/Student_Copy/work/app/domain.py`. It does not replace the packet copy.

Open that work file. The path must contain `Student_Copy\work`. If the path contains `packet`, close it. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. Copy the lines inside the block below. Do not copy the backtick lines. Paste. Save.

```text
"""Keep unlabeled domain text. Leave the extraction letters out.

Chapter 08 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell trains on every row, including the extraction letters.
The two checks do not load this file. The suite does. Do not delete
it.
"""

from __future__ import annotations


def keep(rows: list[dict]) -> list[dict]:
    """Keep a row only when it has no item id.

    rows are domain lines and letters mixed together. A letter
    carries an item id. A domain line does not. The letter is left
    out. The text of a domain line is kept as it arrived.
    """
    unlabeled = [row for row in rows if "item_id" not in row]
    return unlabeled
```

Open [work/app/domain.py](work/app/domain.py). Search inside that file, not inside this chapter. You should see `Leave the extraction letters out.` You should not see `return list(rows)`. If you see that return, you pasted the picture.

## Replace the preference edit

This block replaces [work/app/prefs.py](work/app/prefs.py). The full path is `Week 03/Day 02/Student_Copy/work/app/prefs.py`. It does not replace the packet copy.

Open that work file. The path must contain `Student_Copy\work`. If the path contains `packet`, close it. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. Copy the lines inside the block below. Do not copy the backtick lines. Paste. Save.

```text
"""Expand shorthand, keep the clause id, and drop a date the calendar cannot keep.

Chapter 08 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell returns the coordinator draft unchanged. The two checks
do not load this file. The suite does. Do not delete it.
"""

from __future__ import annotations


def revise(draft: str) -> str:
    """Expand sugar clinic, drop Friday and a fixed date, and drop two tokens.

    draft is the coordinator sentence. The clause id is left in
    place. sugar clinic becomes endocrinology. Friday and the date
    become spaces, so the following split can drop them. The tokens
    on and a bare period are dropped. The other words stay, in order.
    """
    text = draft.replace("sugar clinic", "endocrinology").replace("Friday", " ").replace("2027-03-10", " ")
    # on and a period are glue. They are not part of the edited line.
    return " ".join(word for word in text.split() if word not in {"on", "."})
```

Open [work/app/prefs.py](work/app/prefs.py). Search inside that file, not inside this chapter. You should see `calendar cannot keep`. `Friday` is still on the replace line. That is expected. The word is there so the edit can drop it. You should not see `Return the coordinator draft unchanged.` If you see that sentence, you pasted the picture.

## Search before the suite

These strings exist in the replaced work files. A pasted picture fails the search. Open the work file named in the row. A match in this chapter does not count. A match in `packet/` does not count.

| Work file | Search for this | You should find it |
| --- | --- | --- |
| [prompt.py](work/app/prompt.py) | `Do not serve it.` | Yes. `typed` and `status` are still in the file. That is expected. You should not see `Send the letter fields to the external model.` |
| [extract.py](work/app/extract.py) | `elif "pediatric" in text:` | Yes. `typed` is still a source type. That is expected. You should not see `Leave the extraction fields blank.` |
| [intent.py](work/app/intent.py) | `cannot wait` | Yes. `return "status"` is still in the file. That is expected. You should not see `Call every message a status question.` |
| [adapter.py](work/app/adapter.py) | `"rank": 8` | Yes. You should not see `cloud["hash"]` |
| [route.py](work/app/route.py) | `date_of_birth` | Yes. `ext-large` is still on the refuse line. That is expected. You should not see `Allow every call` |
| [cost.py](work/app/cost.py) | `Price the token count on local-small.` | Yes. You should not see `price.ext_large_per_1k` |
| [qlora.py](work/app/qlora.py) | `(rank + 31) // 32` | Yes. You should not see `(rank + 7) // 8` |
| [domain.py](work/app/domain.py) | `Leave the extraction letters out.` | Yes. You should not see `return list(rows)` |
| [prefs.py](work/app/prefs.py) | `calendar cannot keep` | Yes. `Friday` is still on the replace line. That is expected. You should not see `Return the coordinator draft unchanged.` |

If a row fails, you pasted a picture or you skipped that file. The prompt, letter, and intent rows are the blocks in [chapter 06](06-the-baseline.md). The adapter, router, and cost rows are the blocks in [chapter 07](07-the-adapter.md). The rank, domain, and preference rows are the blocks above. Paste the failed row's block again from that chapter. Search the work file, not the packet file.

## Run the suite

Leave the window you used for the demo. That window is inside `problem_simulation`, and this command is not. Open a new terminal in the course folder, the same way as chapter 01. `dir` should list `problem_simulation` and `Week 03`. If chapter 01 told you to use `py`, use `py` here.

```text
cd "Week 03/Day 02/Student_Copy/work"
python -m unittest discover -s tests -q
```

If the `cd` line says the path cannot be found, this window is not the course folder. Open a new one and run both lines again. Do not chain `cd ..` to climb out of another folder.

If you run this command before the app files are replaced, it fails. That failure is the shell. The tests are already the shared tests. The app is still the shell. Finish the Replace headings on chapters 06, 07, and 08, then run it again.

You should see a line that starts with `Ran 12 tests`, then a blank line, then `OK`. A line of dashes can sit above the `Ran` line. The time on the `Ran` line can differ. There is no `FAIL` and no `ERROR`. The prompt returns after `OK`.

`Ran 12 tests` also appears when the suite fails. Read the line under it. That line has to be `OK`. If the line is `FAILED`, the shell is still in place. One test can pass while the others fail. That is still the shell. Do not stop at the `Ran` line.

A `FAIL` block names a file under `tests\`, such as `test_prompt.py`. The app file to replace is the same name without `test_`. `test_prompt.py` means [prompt.py](work/app/prompt.py). `test_extract.py` means [extract.py](work/app/extract.py). The same pattern holds for intent, adapter, route, cost, qlora, domain, and prefs. Do not edit the test. The tests are shared. Use the search table, then paste that app file again from the chapter that owns it.

If the terminal says `SyntaxError` or `IndentationError`, run this from the course folder:

```text
python "Week 03/Day 02/Student_Copy/prepare_work.py"
```

A second run erases the pasted files. Paste chapters 05 through 08 again from the chapter source. Do not repair the spaces by hand. Then run the suite again. Do not run `prepare_work.py` on this page unless the terminal shows `SyntaxError` or `IndentationError`.

A green suite can still fail chapter 10. The suite does not read the four pages. The checks do.

This page is done when the suite prints `Ran 12 tests` and `OK`, and the nine searches above pass in the work files.

Next: [09 — The pages](09-the-pages.md).
