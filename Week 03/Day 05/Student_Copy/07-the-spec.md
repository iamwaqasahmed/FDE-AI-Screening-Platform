# 07 — The spec

[Chapter 06](06-the-fix.md) replaced the repair, the second run, and the label cost. This chapter replaces the backlog, the stage gate, and the work workflow.

You replace three files under `work/`, in this order:

1. [backlog.py](work/app/backlog.py), under Replace the backlog
2. [gates.py](work/app/gates.py), under Replace the stage gate
3. [.github/workflows/ci.yml](work/.github/workflows/ci.yml), under Replace the improvement gate

Paste only those three blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged. Do not paste a test. The tests are copied and not replaced.

Scroll down to the heading Replace the backlog. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. Two more Replace headings follow it. The four steps from [chapter 05](05-the-sprint.md) are repeated above each paste. The section How the replacement works sits above the first Replace heading. Read it. Do not paste it. Every code block above that Replace heading is a picture. You do not paste a picture.

The first two files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. The workflow is YAML. `improvement-gate:` starts with two spaces. If the terminal later shows `SyntaxError` or `IndentationError`, open a terminal in the course folder and run `python "Week 03/Day 05/Student_Copy/prepare_work.py"`. Then paste chapters 05, 06, and 07 again from the chapter source. Do not repair the spaces by hand. A second run of that command puts the commented gate back. Paste this chapter's workflow again after that.

Do not run a check on this page. The checks are only in [chapter 10](10-finish.md).

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the comment at the top of each Python file. Do not edit them.

Open [seed.json](packet/release/backlog/seed.json). Search for `story_id`. Open [stage-gate.md](packet/release/gates/stage-gate.md). Search for `risk`. That file names the risk tier. It does not name the citation requirement. On Windows, `.github` is hidden. In File Explorer, open View and tick Hidden items. On macOS, in Finder, press Command+Shift+period. The three blocks below are pictures. The first paste is the heading Replace the backlog, further down.

1. [backlog.py](packet/app/backlog.py). Search for `Keep every sponsor story`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/backlog.py](work/app/backlog.py) is under the Replace heading for this file.

```text
"""Keep every sponsor story.

kept discards the story and returns true.
"""

from __future__ import annotations


def kept(story: dict) -> bool:
    """Keep the story.

    story is discarded. The return is true.
    """
    # Every story is kept.
    del story
    return True
```

2. [gates.py](packet/app/gates.py). Search for `Send the citation requirement to go-live`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/gates.py](work/app/gates.py) is under the Replace heading for this file.

```text
"""Send the citation requirement to go-live.

gate_for discards the requirement id and returns the go-live gate.
"""

from __future__ import annotations


def gate_for(requirement_id: str) -> str:
    """Return the go-live gate.

    requirement_id is discarded. The gate does not depend on the id.
    """
    # Every requirement id gets this same gate.
    del requirement_id
    return "G4"
```

3. [ci.yml](packet/.github/workflows/ci.yml). Search for `# improvement-gate:`. That commented line is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml) is under the Replace heading for this file.

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
  # improvement-gate:
  #   Week 3 fills this job. It stays commented until the second run exists.
```

You are done reading. The next heading, Replace the backlog, is the first paste on this page.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

The brief is not the sponsor sentence. These two functions are how that decision shows up in code. The pages you paste later are where a reader sees it.

`kept` drops a story whose id is in the non-goal set. Triage and the other blocked stories are that set. A story with no id is kept. The shell kept every sponsor story, including the ones the memo marked `blocked`.

`gate_for` puts the citation requirement on the risk tier. Every other requirement id returns an empty gate. G1 is that tier. The shell left the citation requirement with no gate, so the spec could not say which approval it sits under.

Before you paste, say what a non-goal does to a backlog story, and which requirement receives a gate.

This section adds no file and no command.

## Replace the backlog

This block replaces [work/app/backlog.py](work/app/backlog.py). The full path is `Week 03/Day 05/Student_Copy/work/app/backlog.py`. It does not replace the copy in `packet/app`.

1. Open the work file named here, [work/app/backlog.py](work/app/backlog.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Drop the sponsor stories that are non-goals.`

```text
"""Drop the sponsor stories that are non-goals.

The non-goal set holds the story ids that are dropped. kept returns
false for those ids. Any other story id is kept. A story with no id
is kept.
"""

from __future__ import annotations

# These two stories are non-goals. The citation story is not in this set.
_NON_GOALS = {"p-triage", "vendor-bot"}


def kept(story: dict) -> bool:
    """Return whether the story stays on the backlog.

    story may carry a story_id. An id in the non-goal set is dropped.
    """
    # A non-goal is not kept. Every other story id is kept.
    return story.get("story_id") not in _NON_GOALS
```

You should see `Drop the sponsor stories that are non-goals.` You should not see `Keep every sponsor story.` If you still see that shell sentence, you pasted the picture. Delete the work file and paste the block under this heading again. `p-triage` and `vendor-bot` can still appear. That is expected. They are the stories that are dropped.

## Replace the stage gate

This block replaces [work/app/gates.py](work/app/gates.py). The full path is `Week 03/Day 05/Student_Copy/work/app/gates.py`. It does not replace the copy in `packet/app`.

1. Open the work file named here, [work/app/gates.py](work/app/gates.py). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Put the citation requirement on the risk tier.`

```text
"""Put the citation requirement on the risk tier.

The citation requirement id returns the risk tier. Every other
requirement id returns an empty gate.
"""

from __future__ import annotations


def gate_for(requirement_id: str) -> str:
    """Return the gate name for a requirement id.

    requirement_id is the id being placed. The citation requirement
    returns the risk tier. Any other id returns an empty string.
    """
    # The citation requirement sits on the risk tier named in the stage-gate file.
    if requirement_id == "req-cite":
        return "G1"
    # Any other requirement id has no gate from this function.
    return ""
```

You should see `Put the citation requirement on the risk tier.` You should not see `Send the citation requirement to go-live.` If you still see that shell sentence, you pasted the picture. Delete the work file and paste the block under this heading again. `req-cite` can still appear. That is expected. It is the requirement this function places. You should not see `G4`.

## Replace the improvement gate

This block replaces [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml). The full path is `Week 03/Day 05/Student_Copy/work/.github/workflows/ci.yml`. It does not replace the copy in `packet/.github`. Open that link from this chapter. You do not need to browse to the folder first. If the link does not open, the folder is hidden. On Windows, in File Explorer, open View and tick Hidden items. On macOS, in Finder, press Command+Shift+period. Then open the full path.

1. Open the work file named here, [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `tests.test_remeasure`.

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
  improvement-gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: regression
        run: python -m unittest tests.test_remeasure -q
```

You should see `tests.test_remeasure`. You should see a line `improvement-gate:` with two spaces and no hash. The letters `improvement-gate` can still appear. That is expected. You should not see `# improvement-gate:`. If you still see the hash, you pasted the picture, or a second run of `prepare_work.py` put the comment back. Delete the work file and paste the block under this heading again. The `test` job stays. That is expected.

This page is done when the backlog, the stage gate, and the work workflow show the new sentences, and the shell sentences are gone. Do not run a check from this page.

Next: [08 — The personal lab](08-the-personal.md).
