# 06 — The baseline

[Chapter 05](05-the-sprint.md) sequenced the sprint. This chapter replaces the prompt, the letter relabel, and the message intent.

You replace three files under `work/`, in this order:

1. [prompt.py](work/app/prompt.py), under Replace the prompt
2. [extract.py](work/app/extract.py), under Replace the letter relabel
3. [intent.py](work/app/intent.py), under Replace the message intent

Paste only those three blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged. The tests are copied and not replaced. Do not paste a test.

Scroll down to the heading Replace the prompt. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. Two more Replace headings follow it. Use the four steps from [chapter 05](05-the-sprint.md) on each one. The section How the replacement works sits above the first Replace heading. Read it. Do not paste it. Every code block above that Replace heading is a picture or a check. You do not paste those.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, run `prepare_work.py` from the course folder and paste this chapter again from the chapter source. Do not repair the spaces by hand.

Do not run the suite on this page. The suite command is in [chapter 08](08-the-advanced.md). It is not a check. The checks are only in [chapter 10](10-finish.md).

The prompt stays the weak baseline. `extract` in `prompt.py` still types every letter and leaves the sub-specialty blank. `intent` in `prompt.py` still returns `status`. That is expected. Do not copy `relabel` or `classify` into `prompt.py`. A prompt file that copies the adapter makes `slice-lora` say `the prompt baseline clears the slice`.

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the comment at the top of each one. Do not edit them. The first block you copy is under Replace the prompt, further down this page.

Open [letters.jsonl](packet/release/slices/letters.jsonl) and [messages.jsonl](packet/release/slices/messages.jsonl). You already did this in chapter 03. The shells below do not follow those rows.

1. [prompt.py](packet/app/prompt.py). Search for `Send the letter fields`. That sentence is the shell. It serves the prompt and sends phi to `ext-large`. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/prompt.py](work/app/prompt.py) is under Replace the prompt.

```text
"""Send the letter fields to the external model.

served returns true, so this prompt is marked as the served one.
target names ext-large and sets phi. extract copies the item id,
sets the source type to typed, and leaves the sub-specialty
empty. intent returns status. None of these functions read the
row text.
"""

from __future__ import annotations


def served() -> bool:
    """Report that this prompt is the one being served."""
    # True means this prompt is the model on the endpoint.
    return True


def target() -> dict:
    """Name ext-large and turn phi on.

    The model name is ext-large. phi is set, so the call this
    row describes includes phi.
    """
    return {"model": "ext-large", "phi": True}


def extract(row: dict) -> dict:
    """Copy the item id, mark the letter typed, and leave the sub-specialty blank.

    row must carry item_id. The text is not read. The source
    type is typed. The sub-specialty is an empty string.
    """
    return {"item_id": row["item_id"], "source_type": "typed", "sub_specialty": ""}


def intent(row: dict) -> str:
    """Return the status label.

    row is not read. The text of the message does not change
    the label.
    """
    return "status"
```

2. [extract.py](packet/app/extract.py). Search for `Leave the extraction fields blank`. That sentence is the shell. The next block is a picture of that file. Do not paste it.

```text
"""Leave the extraction fields blank.

relabel copies the item id and returns an empty source type and
an empty sub-specialty. The letter text is not read.
"""

from __future__ import annotations


def relabel(row: dict) -> dict:
    """Copy the item id and leave both labels empty.

    row must carry item_id. Any text on the row is ignored. The
    source type and the sub-specialty are empty strings.
    """
    # The letter text is not consulted. Both labels stay blank.
    return {"item_id": row["item_id"], "source_type": "", "sub_specialty": ""}
```

3. [intent.py](packet/app/intent.py). Search for `Call every message a status question`. That sentence is the shell. The next block is a picture of that file. Do not paste it.

```text
"""Call every message a status question.

classify does not read the message. The label is status for
every row.
"""

from __future__ import annotations


def classify(row: dict) -> str:
    """Return the status label.

    row is not read. The text of the message does not change
    the label this function returns.
    """
    # Every message receives the same label.
    return "status"
```

The pictures end here. The next heading is How the replacement works. Read it. It is not a paste. The first paste is the next heading that starts with Replace.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

The prompt is a baseline. It is not the model you serve.

`target` stays on `local-small` and leaves phi off. `served` is false. `extract` on this file always returns typed with a blank sub-specialty, and `intent` always returns status. That weakness is the point. The real letter reading is `extract.py`. The real message reading is `intent.py`. Do not copy those into the prompt. The shell sent letter fields to `ext-large` and marked the prompt as served.

The score this day calls F1 is the share of fields that match. It is not a precision-and-recall F1. For a letter, the two fields are source type and sub-specialty. For a message, the one field is the intent. The price cap's `f1_floor` is the line that share has to clear. The prompt's always-typed, always-status answers stay under that line. The held-out letters are not in the packet. They use the same text rules, which is why you do not need their rows.

`relabel` in the extract file reads the text. Phone or photo, scan, retina, and pediatric follow the same rules as Week 3 Day 1. Phone or photo wins when the word scan is also there. A letter that names neither sub-specialty stays blank.

`classify` returns one intent. The first matching rule wins. An emergency phrase wins even when the same sentence also says referral or asks for a slot. Cancel is checked before book, so a cancellation is not read as a booking. The word referral counts as status, so that rule stays last. A message that matches nothing is other. The shell called every message status, including "Cancel this visit."

Before you paste, say why the prompt is allowed to be wrong, and which file is not allowed to be wrong.

This section adds no file and no command.

## Replace the prompt

This block replaces [work/app/prompt.py](work/app/prompt.py). The full path is `Week 03/Day 02/Student_Copy/work/app/prompt.py`. It does not replace the packet copy. A long block is still one file. This one is `prompt.py`.

Open that work file. The path must contain `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. Paste. Save.

```text
"""Score a weak local prompt. Do not serve it.

Chapter 06 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell sends the letter fields to ext-large and marks the prompt
as served. While that shell is the file that runs, the model check
says the prompt baseline is still the served model, and the call
sends phi to ext-large. The check does not name the model.

extract and intent stay the weak baseline. Every letter is typed,
and every message is status. That is expected. Pointing those two
functions at the adapter makes slice-lora say the prompt baseline
clears the slice.
"""

from __future__ import annotations


def served() -> bool:
    """The weak prompt is scored. It is not the model that is served."""
    # A served prompt is the model on the endpoint. This one is not.
    return False


def target() -> dict:
    """The baseline call stays on local-small, with phi left off.

    The shell returns ext-large and sets phi. This call does not.
    """
    return {"model": "local-small", "phi": False}


def extract(row: dict) -> dict:
    """Always type the letter and leave the sub-specialty blank.

    row is one letter. The item id is copied. The text is not read.
    A real relabel lives in extract.py. Do not copy it here.
    """
    return {"item_id": row["item_id"], "source_type": "typed", "sub_specialty": ""}


def intent(row: dict) -> str:
    """Always call the message a status question.

    row is one message. The text is not read. A real classifier
    lives in intent.py. Do not copy it here. "Cancel this visit."
    stays status. That is expected.
    """
    return "status"
```

Open [work/app/prompt.py](work/app/prompt.py). Search inside that file, not inside this chapter. You should see `Do not serve it.` You should still see `typed` and `status`. That is expected. Those two words are the weak baseline. You should not see `Send the letter fields to the external model.` If you see that sentence, you pasted the picture.

## Replace the letter relabel

This block replaces [work/app/extract.py](work/app/extract.py). The full path is `Week 03/Day 02/Student_Copy/work/app/extract.py`. It does not replace the packet copy.

Open that work file. The path must contain `Student_Copy\work`. If the path contains `packet`, close it. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. Copy the lines inside the block below. Do not copy the backtick lines. Paste. Save.

```text
"""Relabel a letter from the text.

Chapter 06 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell returns an empty source type and an empty sub-specialty.
While that shell is the file that runs, the model check says
extraction F1 is outside the budget. The check does not print an F1
or a gold label.
"""

from __future__ import annotations


def relabel(row: dict) -> dict:
    """Read the letter text and fill the two fields.

    row carries item_id and text. The item id is copied. The text
    decides the sub-specialty and the source type. A letter that
    names neither specialty stays blank. A letter that is not a
    phone, a photo, or a scan stays typed.
    """
    text = row["text"].lower()
    # Retina wins when both specialty words are present.
    if "retina" in text:
        sub_specialty = "retina"
    elif "pediatric" in text:
        sub_specialty = "pediatric"
    else:
        sub_specialty = ""
    # A phone photo is a photo. The word scan marks a scan.
    if "phone" in text or "photo" in text:
        source_type = "photo"
    elif "scan" in text:
        source_type = "scan"
    else:
        source_type = "typed"
    return {"item_id": row["item_id"], "source_type": source_type, "sub_specialty": sub_specialty}
```

Open [work/app/extract.py](work/app/extract.py). Search inside that file, not inside this chapter. You should see `elif "pediatric" in text:`. You should still see `typed`. That is expected. A letter that is not a phone, a photo, or a scan stays typed. You should not see `Leave the extraction fields blank.` If you see that sentence, you pasted the picture.

## Replace the message intent

This block replaces [work/app/intent.py](work/app/intent.py). The full path is `Week 03/Day 02/Student_Copy/work/app/intent.py`. It does not replace the packet copy.

Open that work file. The path must contain `Student_Copy\work`. If the path contains `packet`, close it. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. Copy the lines inside the block below. Do not copy the backtick lines. Paste. Save.

```text
"""Tag the gold intent. An emergency phrase wins over a status question.

Chapter 06 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell calls every message a status question. While that shell
is the file that runs, the model check says intent F1 is outside
the budget. The check does not print an F1 or a gold label.
"""

from __future__ import annotations

# An emergency phrase is checked before status, referral, or book.
_EMERGENCY = ("chest pain", "cannot wait", "person now")


def classify(row: dict) -> str:
    """Return one intent for the message text.

    row carries text. The first matching rule wins. An emergency
    phrase wins even when the same sentence also asks for status
    or a slot. A message that matches nothing is other.
    """
    text = row["text"].lower()
    if any(phrase in text for phrase in _EMERGENCY):
        return "emergency"
    # Later rules are ordinary requests. Order is the priority.
    if "reschedule" in text:
        return "reschedule"
    if "cancel" in text:
        return "cancel"
    if "book" in text:
        return "book"
    if "document" in text or "bring" in text:
        return "info"
    if "closed" in text or "complaint" in text:
        return "complaint"
    if "status" in text or "referral" in text:
        return "status"
    return "other"
```

Open [work/app/intent.py](work/app/intent.py). Search inside that file, not inside this chapter. You should see `cannot wait`. You should still see `return "status"`. That is expected. A status question that has no emergency phrase stays status. You should not see `Call every message a status question.` If you see that sentence, you pasted the picture.

This page is done when those three searches pass in the three work files. The packet copies are still the shells. That is expected. Do not run a check from this page.

Next: [07 — The adapter](07-the-adapter.md).
