# 07 — The reply

[Chapter 06](06-the-calendar.md) counted the cluster week. This chapter replaces the reply schema and the two tests that call it.

You replace three files under `work/`: [schema.py](work/app/schema.py), [test_schema.py](work/tests/test_schema.py), and [test_journey.py](work/tests/test_journey.py). Leave the copies in `packet/` unchanged. The checks run in chapter 10. Do not run them from this page. Do not run the suite from this page.

## Read these files

Open these in the packet. Read the comment at the top of each one. Do not edit them.

1. [schema.py](packet/app/schema.py). Search for `reply.get("text")`. That line is the shell. A non-empty sentence passes. Search for `del state`. The journey ignores the mock state and looks for the word booked in the sentence.
2. [test_schema.py](packet/tests/test_schema.py). Search for `test_sentence_is_required`. An empty sentence fails, even when `intent` is present.
3. [test_journey.py](packet/tests/test_journey.py). Search for `The visit is booked`. The shell expects that sentence to pass while `booked` is false.
4. [model.json](packet/release/fixtures/model.json). Search for `intent`. Two fields. The text starts with `The visit is booked` and then a watermark. Leave the file in the packet. Do not copy it into `work/`. Do not paste it into a prompt. [pol-assistant-use.md](packet/kickoff/corpus/pol-assistant-use.md) says the watermark stays out of prompts.

The tests check says `the reply schema is missing` when a sentence with no intent still passes, or when an empty sentence with intent fails. It says `the journey followed the sentence` when the sentence is treated as the result. Neither message names a field.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

Two small functions, two different mistakes.

`schema_ok` looks at `intent`. A non-empty string passes. The sentence can be empty. A sentence with no intent fails. The shell treated a fluent sentence as proof the reply was well formed.

`journey_ok` does not read the reply at all. `del reply` is that decision, written down. The result is `booked` on the mock state. A fluent sentence can sit on a state that was not booked. The journey follows the state.

The shell followed the sentence. While it does, the check says the journey followed the sentence, or that the reply schema is missing.

Before you paste, say which function is allowed to ignore the model's words, and which field the schema actually requires.

This section adds no file and no command.

## Replace the schema

This block replaces [work/app/schema.py](work/app/schema.py). The full path is `Module 02/Lesson 03/Student_Copy/work/app/schema.py`. It does not replace [packet/app/schema.py](packet/app/schema.py).

Open [work/app/schema.py](work/app/schema.py). That is the work copy. Do not paste into the packet copy.

1. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
2. Copy from this chapter file, not from a preview. A preview can drop the spaces.
3. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it.
4. Paste as plain text. The line `def schema_ok` starts at the left edge. The lines inside the function start with four spaces. Save.

If the terminal later shows `SyntaxError` or `IndentationError`, do not repair the spaces by hand. Run `prepare_work.py` again from the course folder, then paste this block again from this chapter file, not from a preview. Paste the sprint again from [chapter 05](05-the-sprint.md) and the calendar files again from [chapter 06](06-the-calendar.md) if that second run restored them.

```text
"""Judge a reply by its fields. The sentence is not evidence.

Chapter 07 replaces the work copy with this file.
Leave the packet shell unchanged.

schema_ok is true when intent is a non-empty string. The sentence
can be empty. journey_ok ignores the reply and reads booked on the
state. While the shell is the file that runs, the tests check says
the reply schema is missing, and the journey followed the sentence.
"""

from __future__ import annotations


def schema_ok(reply: dict) -> bool:
    """True when intent is a non-empty string.

    reply is the model object. intent is the field the schema requires.
    text can be empty. A sentence with no intent fails.
    """
    intent = reply.get("intent")
    return isinstance(intent, str) and bool(intent)


def journey_ok(reply: dict, state: dict) -> bool:
    """True when the mock state says the visit was booked.

    reply is ignored. The sentence is not the result. state is the
    recorded outcome. booked is the flag on that outcome.
    """
    del reply
    return bool(state.get("booked"))
```

Read the file back. You should see `intent` in `schema_ok`. You should see `del reply` in `journey_ok`. The sentence is not what `journey_ok` reads.

## Replace the schema test

This block replaces [work/tests/test_schema.py](work/tests/test_schema.py). It does not replace [packet/tests/test_schema.py](packet/tests/test_schema.py). Use the same four steps on the work file. Copy from this chapter file, not from a preview.

```text
"""The reply schema requires intent, not a sentence.

Chapter 07 replaces the work copy with this file.
Leave the packet shell unchanged.

The tests check does not run this file. It calls schema_ok.
An empty sentence with intent passes. A sentence with no intent fails.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from schema import schema_ok


class SchemaTests(unittest.TestCase):
    """The reply schema requires intent, not a sentence."""
    def test_intent_without_a_sentence(self) -> None:
        """An empty sentence with intent status is accepted."""
        self.assertTrue(schema_ok({"intent": "status", "text": ""}))

    def test_sentence_without_intent(self) -> None:
        """A sentence with no intent is rejected.

        The words The visit is booked are still on this line.
        schema_ok does not trust them. It looks for intent.
        """
        self.assertFalse(schema_ok({"text": "The visit is booked."}))


if __name__ == "__main__":
    unittest.main()
```

Read the file back. You should see `The visit is booked` on the line that expects false. That sentence is still in the file. `schema_ok` does not trust it. The line that expects true has `intent` and an empty sentence.

## Replace the journey test

This block replaces [work/tests/test_journey.py](work/tests/test_journey.py). It does not replace [packet/tests/test_journey.py](packet/tests/test_journey.py). Use the same four steps on the work file. Copy from this chapter file, not from a preview.

```text
"""The journey asserts the mock state, not the sentence.

Chapter 07 replaces the work copy with this file.
Leave the packet shell unchanged.

The fixture stays in the pack. This file reads it. It does not copy it.
The tests check does not run this file. It calls journey_ok.
"""

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from schema import journey_ok

# parents[0] is tests. parents[1] is work. parents[2] is Student_Copy
# or Solution_Copy. parents[3] is Lesson 03. parents[4] is Module 02.
# parents[5] is the course folder. data/ sits there.
_ROOT = Path(__file__).resolve().parents[5]


class JourneyTests(unittest.TestCase):
    """The journey asserts the mock state, not the sentence."""
    def test_recorded_sentence_is_not_the_state(self) -> None:
        """A recorded sentence with booked false is not a booking.

        The fixture text is still loaded. journey_ok does not read it.
        The state says booked is false, so the result is false.
        """
        # Load the fixture sentence. The assertion trusts the state, not that sentence.
        reply = json.loads((_ROOT / "data" / "rel-m02-l03" / "fixtures" / "model.json").read_text(encoding="utf-8"))
        self.assertFalse(journey_ok(reply, {"outcome": "status", "booked": False}))

    def test_state_books_without_a_sentence(self) -> None:
        """An empty sentence still books when the state says booked.

        intent is present so the reply has a shape. The sentence is empty.
        booked on the state is what the assertion trusts.
        """
        # An empty sentence still books when the state says booked.
        self.assertTrue(journey_ok({"intent": "status", "text": ""}, {"booked": True}))


if __name__ == "__main__":
    unittest.main()
```

Read the file back. You should see `model.json` on the line that loads the fixture. The fixture still contains `The visit is booked`. `journey_ok` does not read that sentence. You should see `booked` on the state in both tests. You should not see a copy of the fixture under `work/`.

Do not run the suite yet. The receipt test in the shell still waits.

Next: [08 — The receipt](08-the-receipt.md).
