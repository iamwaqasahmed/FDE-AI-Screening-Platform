# 07 — The gate

[Chapter 06](06-the-harness.md) scored the slices, kept the later window, and named the log rows. This chapter replaces the judge, the regression, and the work copy of the workflow.

You replace three files under `work/`, in this order:

1. [judge.py](work/app/judge.py), under Replace the judge
2. [gate.py](work/app/gate.py), under Replace the regression
3. [ci.yml](work/.github/workflows/ci.yml), under Replace the evaluation gate

Paste only those three blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged. The packet workflow stays commented. Do not paste a test. The tests are copied and not replaced.

Scroll down to the heading Replace the judge. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. Two more Replace headings follow it. The four steps from [chapter 05](05-the-sprint.md) are repeated above each paste. The section How the replacement works sits above the first Replace heading. Read it. Do not paste it. Every code block above that Replace heading is a picture. You do not paste a picture.

These files are Python, and the workflow is YAML. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. The workflow job line `evaluation-gate:` starts with two spaces. If the terminal later shows `SyntaxError` or `IndentationError`, run `prepare_work.py` from the course folder and paste chapters 05 through 07 again from the chapter source. Do not repair the spaces by hand. A second run of `prepare_work.py` puts the commented gate back. Paste this chapter's workflow again after that.

Do not run a check on this page. The checks are only in [chapter 10](10-finish.md). `gate.py` is the regression the suite runs. You do not delete it.

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the comment at the top of each code file. Do not edit them.

Open [calibration.jsonl](packet/release/slices/calibration.jsonl). Search for `cal-fluent-wrong`. A fluent row can still have a pass field of false. The judge follows the pass field.

1. [judge.py](packet/app/judge.py). Search for `when it is fluent`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/judge.py](work/app/judge.py) is under the Replace heading for this file.

```text
"""Mark a citation correct when it is fluent.

mark returns the fluent field. A fluent item is a pass. A missing
fluent field is not a pass.
"""

from __future__ import annotations


def mark(item: dict) -> bool:
    """Return whether the item is fluent.

    item is a citation record. The flag is the fluent field.
    """
    # The fluent field is the mark.
    return bool(item.get("fluent"))
```

2. [gate.py](packet/app/gate.py). Search for `Accept a citation when it is fluent`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/gate.py](work/app/gate.py) is under the Replace heading for this file.

```text
"""Accept a citation when it is fluent.

accepts returns the fluent flag. A fluent item is accepted. A
missing flag is rejected.
"""

from __future__ import annotations


def accepts(item: dict) -> bool:
    """Return whether the item is fluent.

    item is a citation record. The flag is the fluent field. A
    missing fluent field is false.
    """
    # The fluent field is the decision.
    return bool(item.get("fluent"))
```

3. [ci.yml](packet/.github/workflows/ci.yml). On Windows, `.github` is hidden. In File Explorer, open View and tick Hidden items. On macOS, in Finder, press Command+Shift+period. If the link does not open, tick Hidden items, then Ctrl+click it again. On macOS, Command+click it again. Search for `# evaluation-gate:`. That line is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml) is under the Replace heading for this file.

```text
name: ci
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: tests
        run: python -m unittest discover -s tests -q
  # evaluation-gate:
  #   Week 3 fills this job. It stays commented until the evaluation set exists.
```

The pictures end here. The next heading is How the replacement works. Read it. It is not a paste. The first paste is the next heading that starts with Replace.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

A judge that likes fluent text will mark a wrong citation correct. These two functions refuse that.

`mark` returns the calibration label, the `pass` field. A missing label is not a pass. The shell marked the citation correct because the sentence was fluent.

`accepts` returns that same label as a boolean. False is rejected. True is accepted. A missing label is rejected. That is the regression: a citation the calibration set calls wrong must fail even when it reads well.

The evaluation-gate job in the workflow is the placeholder Week 1 left commented. This chapter fills the job so the suite has somewhere to put this check. You still do not grade by hand.

Before you paste, say what the judge is required to copy, and what it is required to ignore.

This section adds no file and no command.

## Replace the judge

This block replaces [work/app/judge.py](work/app/judge.py). The full path is `Week 03/Day 04/Student_Copy/work/app/judge.py`. It does not replace the packet copy. A long block is still one file. This one is `judge.py`.

1. Open the work file named under this heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

```text
"""Mark a citation with the calibration label.

mark returns the pass field. A missing pass field is not a pass.
"""

from __future__ import annotations


def mark(item: dict) -> bool:
    """Return the calibration label.

    item is a citation record. The label is the pass field.
    """
    # The calibration label is the pass field.
    return bool(item.get("pass"))
```

Open [work/app/judge.py](work/app/judge.py). Search inside that file, not inside this chapter. You should see `Mark a citation with the calibration label.`. You should not see `Mark a citation correct when it is fluent`. If you see that text, you pasted the picture.

## Replace the regression

This block replaces [work/app/gate.py](work/app/gate.py). The full path is `Week 03/Day 04/Student_Copy/work/app/gate.py`. It does not replace the packet copy. A long block is still one file. This one is `gate.py`.

1. Open the work file named under this heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

```text
"""Reject a fluent citation that the calibration label marks wrong.

accepts returns the calibration label. A false label is rejected.
A true label is accepted. A missing label is rejected.
"""

from __future__ import annotations


def accepts(item: dict) -> bool:
    """Return the calibration label on the item.

    item is a citation record. The label is the pass field. A missing
    pass field is false.
    """
    # The regression follows the calibration label.
    return bool(item.get("pass"))
```

Open [work/app/gate.py](work/app/gate.py). Search inside that file, not inside this chapter. You should see `Reject a fluent citation that the calibration label marks wrong.`. You should not see `Accept a citation when it is fluent`. If you see that text, you pasted the picture.

## Replace the evaluation gate

This block replaces [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml). The full path is `Week 03/Day 04/Student_Copy/work/.github/workflows/ci.yml`. It does not replace the packet copy. The packet copy stays commented. A long block is still one file. This one is `ci.yml`. On Windows, `.github` is hidden. Tick Hidden items, then Ctrl+click the work link. On macOS, press Command+Shift+period, then Command+click the work link. If the path contains `packet`, close it and open the work copy.

1. Open the work file named under this heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

```text
name: ci
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: tests
        run: python -m unittest discover -s tests -q
  evaluation-gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: regression
        run: python -m unittest tests.test_gate -q
```

Open [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml). Search inside that file, not inside this chapter. You should see `name: regression`. The line `evaluation-gate:` has two spaces before it and no hash. The `test` job is still in the file, and it still runs `python -m unittest discover -s tests -q`. That is expected. You should not see `# evaluation-gate:`. If you see that text, you pasted the picture.

This page is done when the judge, the regression, and the work workflow show the sentences above. Do not run a check from this page.

Next: [08 — The advanced path](08-the-advanced.md).
