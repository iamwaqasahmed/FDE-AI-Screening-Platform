# 07 — The sample

[Chapter 06](06-the-clusters.md) replaced the cluster job. This chapter replaces the relabel, the synthetic sample, and the scan.

You replace six files under `work/`, in this order:

1. [labels.py](work/app/labels.py), under Replace the relabel
2. [test_labels.py](work/tests/test_labels.py), under Replace the label test
3. [synthetic.py](work/app/synthetic.py), under Replace the sample
4. [test_synthetic.py](work/tests/test_synthetic.py), under Replace the sample test
5. [scan.py](work/app/scan.py), under Replace the scan
6. [test_scan.py](work/tests/test_scan.py), under Replace the scan test

Paste only those six blocks. The blocks under Read these files are pictures. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged.

Scroll down to the heading Replace the relabel. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. Use the four steps from [chapter 05](05-the-sprint.md) on each Replace heading. Everything above that first Replace heading is a picture or a check. You do not paste it.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, run `prepare_work.py` from the course folder and paste chapters 05, 06, and 07 again from the chapter source. Do not repair the spaces by hand.

Do not copy `letters/clerk.jsonl` into `work/`. That file is not in the packet. The scan reads it from the built pack at `data/rel-w3d1/letters/clerk.jsonl`. It carries a watermark. The check message does not print the watermark.

Do not run the suite on this page. The suite command is in [chapter 08](08-the-advanced.md). The checks are only in [chapter 10](10-finish.md).

## Read these files

You are reading. You are not pasting yet. The first block you copy is under Replace the relabel, further down this page.

Open [ann-v1.md](packet/release/guidelines/ann-v1.md). Search for `phone photo`. The next block is a picture of that file. Do not paste it.

```text
# ann-v1

Clerk labels may leave the sub-specialty blank.

The source type is typed or scan. A phone photo is recorded as a scan.
```

Open [ann-v2.md](packet/release/guidelines/ann-v2.md). Search for `retina`. You read this file in chapter 03. ann-v2 reads the text. ann-v1 copies the clerk fields.

Open [adjudicated.jsonl](packet/release/letters/adjudicated.jsonl). These four rows are the development labels. They already follow ann-v2. The check scores other letters. Those other letters are in the clerk file, which you do not copy. The next block is a picture of the development file. Do not paste it.

```text
{"guideline": "ann-v2", "item_id": "d1", "source_type": "typed", "sub_specialty": "pediatric"}
{"guideline": "ann-v2", "item_id": "d2", "source_type": "photo", "sub_specialty": "retina"}
{"guideline": "ann-v2", "item_id": "d3", "source_type": "scan", "sub_specialty": ""}
{"guideline": "ann-v2", "item_id": "d4", "source_type": "typed", "sub_specialty": ""}
```

Open [fidelity.json](packet/release/cards/fidelity.json). Search for `rare_sub_specialty`. The card names the bands. The check does not print a rate. The next block is a picture of that file. Do not paste it.

```text
{
  "label_margin": {
    "retina": [
      0.3,
      0.7
    ]
  },
  "phrase": {
    "kindly": [
      0.2,
      0.6
    ]
  },
  "rare_sub_specialty": "retina",
  "sample_size": [
    4,
    8
  ],
  "specialty_mix": {
    "endo": [
      0.4,
      0.6
    ],
    "ophth": [
      0.4,
      0.6
    ]
  }
}
```

1. [labels.py](packet/app/labels.py). Search for `ann-v1`. That line is the shell. A phone photo stays a scan, and a blank sub-specialty stays blank. The next block is a picture of that file. Do not paste it.

```text
"""Copy the clerk label.

This is the shell. Chapter 07 replaces the copy under work/app.
Leave this file in the packet unchanged.

relabel keeps the clerk source type and sub-specialty, and sets
the guideline to ann-v1. While this shell is the file that runs,
the labels check says a phone photo is still a scan, a
sub-specialty is still blank, and the sample still follows ann-v1.
"""

from __future__ import annotations


def relabel(row: dict) -> dict:
    """Return the clerk fields under the old guideline.

    row is one letter. The text is not read. source_type and
    sub_specialty are copied. guideline is ann-v1.
    """
    return {
        "guideline": "ann-v1",
        "item_id": row["item_id"],
        "source_type": row["source_type"],
        "sub_specialty": row["sub_specialty"],
    }
```

2. [synthetic.py](packet/app/synthetic.py). Search for `letters[:1]`. That line is the shell. The first real letter becomes the sample. The next block is a picture of that file. Do not paste it.

```text
"""Copy a real letter into the synthetic sample.

This is the shell. Chapter 07 replaces the copy under work/app.
Leave this file in the packet unchanged.

sample returns the first letter and ignores the card. While this
shell is the file that runs, the synthetic check says the sample
misses the fidelity card, contains a watermark, and contains a
national id. The message does not print the watermark.
"""

from __future__ import annotations


def sample(letters: list[dict], card: dict) -> list[dict]:
    """Return the first real letter.

    letters are the clerk rows. card is ignored. The first row is
    the one the scan has to refuse.
    """
    del card
    return letters[:1]
```

3. [scan.py](packet/app/scan.py). Search for `return True`. That line is the shell. Every file is accepted. The next block is a picture of that file. Do not paste it.

```text
"""Accept every file.

This is the shell. Chapter 07 replaces the copy under work/app.
Leave this file in the packet unchanged.

accept returns true for every text. While this shell is the file
that runs, the synthetic check says the sample contains a
watermark and contains a national id. The message does not print
the watermark.
"""

from __future__ import annotations


def accept(text: str, national_ids: list[str]) -> bool:
    """Accept the text. The arguments are ignored."""
    del text, national_ids
    return True
```

The pictures end here. The next heading is the first paste.

## Replace the relabel

This block replaces [work/app/labels.py](work/app/labels.py). The full path is `Week 03/Day 01/Student_Copy/work/app/labels.py`. It does not replace [packet/app/labels.py](packet/app/labels.py). It does not replace the test.

Open the work file. Select the whole file and delete it. Copy the lines inside the block below from this chapter file. Use Paste Without Formatting. Do not copy the backtick lines. Paste. Save.

```text
"""Relabel a letter under ann-v2.

Chapter 07 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell copies the clerk fields and keeps the old guideline.
While that shell is the file that runs, the labels check says a
phone photo is still a scan, a sub-specialty is still blank, and
the sample still follows the old guideline.
"""

from __future__ import annotations


def relabel(row: dict) -> dict:
    """Set the source type and the sub-specialty from the text.

    row is one letter. Phone or photo in the text is source type
    photo. Scan, when the text does not say phone or photo, is
    source type scan. Anything else is typed. Retina and pediatric
    are read from the text. Any other sub-specialty stays blank.
    """
    text = row["text"].lower()
    # The sub-specialty comes from the words, not from the clerk field.
    if "retina" in text:
        sub_specialty = "retina"
    elif "pediatric" in text:
        sub_specialty = "pediatric"
    else:
        sub_specialty = ""
    # Phone or photo wins over the word scan.
    if "phone" in text or "photo" in text:
        source_type = "photo"
    elif "scan" in text:
        source_type = "scan"
    else:
        source_type = "typed"
    return {
        "guideline": "ann-v2",
        "item_id": row["item_id"],
        "source_type": source_type,
        "sub_specialty": sub_specialty,
    }
```

Open the work file you just saved. Search inside that file, not inside this chapter. You should see `ann-v2`. You should see `scan` on the line that sets the source type when the text says scan. That is expected. A real scan stays a scan. You should not see `ann-v1`. If you see `ann-v1`, you pasted the picture. Paste this block again.

## Replace the label test

This block replaces [work/tests/test_labels.py](work/tests/test_labels.py). The full path is `Week 03/Day 01/Student_Copy/work/tests/test_labels.py`. It does not replace the packet test.

Open the work file. Select the whole file and delete it. Copy the lines inside the block below from this chapter file. Use Paste Without Formatting. Do not copy the backtick lines. Paste. Save.

```text
"""A phone photo and a retina note follow ann-v2.

Chapter 07 replaces the work copy with this file. Leave the packet
shell test unchanged.

The shell test expects the clerk source type to stay scan and the
sub-specialty to stay blank. This test expects photo and retina.
The word scan remains in the input row. That is expected.
The line parents[1] stays as it is.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from labels import relabel


class LabelTests(unittest.TestCase):
    def test_photo_and_retina_follow_ann_v2(self) -> None:
        """Phone and retina in the text override the clerk fields."""
        row = {"item_id": "h1", "source_type": "scan", "sub_specialty": "", "text": "Phone photo from the retina service."}
        labeled = relabel(row)
        self.assertEqual(labeled["guideline"], "ann-v2")
        self.assertEqual(labeled["source_type"], "photo")
        self.assertEqual(labeled["sub_specialty"], "retina")


if __name__ == "__main__":
    unittest.main()
```

Open the work file you just saved. Search inside that file, not inside this chapter. You should see `test_photo_and_retina_follow_ann_v2`. You should see `parents[1]`. Leave that line. The input row still says `scan`. That is the clerk field. The result is `photo`. That is expected.

## Replace the sample

This block replaces [work/app/synthetic.py](work/app/synthetic.py). The full path is `Week 03/Day 01/Student_Copy/work/app/synthetic.py`. It does not replace [packet/app/synthetic.py](packet/app/synthetic.py). It does not replace the test.

Open the work file. Select the whole file and delete it. Copy the lines inside the block below from this chapter file. Use Paste Without Formatting. Do not copy the backtick lines. Paste. Save.

```text
"""A rare-class sample inside the fidelity card. Real letters stay out.

Chapter 07 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell returns the first real letter. While that shell is the
file that runs, the synthetic check says the sample misses the
fidelity card, contains a watermark, and contains a national id.
The message does not print the watermark or a rate.
"""

from __future__ import annotations


def sample(letters: list[dict], card: dict) -> list[dict]:
    """Return four invented rows that sit inside the card.

    letters are the clerk rows. They are not copied. card supplies
    the rare sub-specialty. Two rows are endocrinology and two are
    ophthalmology. Two rows name the rare sub-specialty. Two rows
    say Kindly. None of the rows carry an id.
    """
    del letters
    rare = card["rare_sub_specialty"]
    return [
        {"source_type": "typed", "specialty": "endo", "sub_specialty": rare, "text": "Kindly review endocrinology."},
        {"source_type": "typed", "specialty": "endo", "sub_specialty": "", "text": "Kindly review the sugar clinic."},
        {"source_type": "photo", "specialty": "ophth", "sub_specialty": rare, "text": "A clinic photo for the eye clinic."},
        {"source_type": "scan", "specialty": "ophth", "sub_specialty": "", "text": "A scanned page for the eye clinic."},
    ]
```

Open the work file you just saved. Search inside that file, not inside this chapter. You should see `rare_sub_specialty`. You should see `Kindly` on two rows. You should not see `letters[:1]`. If you see that slice, you pasted the picture. Paste this block again. The sample does not contain a history id. Do not add one.

## Replace the sample test

This block replaces [work/tests/test_synthetic.py](work/tests/test_synthetic.py). The full path is `Week 03/Day 01/Student_Copy/work/tests/test_synthetic.py`. It does not replace the packet test.

Open the work file. Select the whole file and delete it. Copy the lines inside the block below from this chapter file. Use Paste Without Formatting. Do not copy the backtick lines. Paste. Save.

```text
"""The sample keeps the rare class and drops the real letter.

Chapter 07 replaces the work copy with this file. Leave the packet
shell test unchanged.

The shell test expects the first letter to come back. This test
expects that letter's text to be absent, and two rows to carry the
rare sub-specialty. clerk-row is a stand-in in this test. It is
not a history id. The line parents[1] stays as it is.
"""

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from synthetic import sample


class SyntheticTests(unittest.TestCase):
    def test_rare_class_has_no_real_id(self) -> None:
        """The invented rows do not repeat the letter, and two name retina."""
        rows = sample([{"text": "clerk-row CANARY-x"}], {"rare_sub_specialty": "retina"})
        blob = json.dumps(rows)
        self.assertNotIn("clerk-row", blob)
        self.assertNotIn("CANARY", blob)
        self.assertEqual(sum(1 for row in rows if row["sub_specialty"] == "retina"), 2)


if __name__ == "__main__":
    unittest.main()
```

Open the work file you just saved. Search inside that file, not inside this chapter. You should see `test_rare_class_has_no_real_id`. You should see `parents[1]`. Leave that line. `clerk-row` on the letter is a stand-in in the test. It is not a history id. That is expected. `CANARY-x` is a stand-in mark. It is not the watermark in the clerk file. The check does not print that watermark.

## Replace the scan

This block replaces [work/app/scan.py](work/app/scan.py). The full path is `Week 03/Day 01/Student_Copy/work/app/scan.py`. It does not replace [packet/app/scan.py](packet/app/scan.py). It does not replace the test.

Open the work file. Select the whole file and delete it. Copy the lines inside the block below from this chapter file. Use Paste Without Formatting. Do not copy the backtick lines. Paste. Save.

```text
"""Refuse a watermark or a national id from the history.

Chapter 07 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell accepts every file. While that shell is the file that
runs, the synthetic check says the sample contains a watermark and
contains a national id. The message does not print the watermark.
"""

from __future__ import annotations


def accept(text: str, national_ids: list[str]) -> bool:
    """Return false when the text has the mark or a history id.

    text is the file being shared. national_ids are the history
    ids. A clean invented sentence is accepted. The mark prefix
    is refused. A non-empty history id found in the text is refused.
    """
    # The mark prefix is enough. The check does not ask this file to print it.
    if "CANARY-" in text:
        return False
    # An empty id is skipped. A real history id in the text is refused.
    return not any(item and item in text for item in national_ids)
```

Open the work file you just saved. Search inside that file, not inside this chapter. You should see `CANARY-`. A clean line is still accepted by the second return. That is expected. You should not see `del text`. If you see `del text`, you pasted the picture. Paste this block again.

## Replace the scan test

This block replaces [work/tests/test_scan.py](work/tests/test_scan.py). The full path is `Week 03/Day 01/Student_Copy/work/tests/test_scan.py`. It does not replace the packet test.

Open the work file. Select the whole file and delete it. Copy the lines inside the block below from this chapter file. Use Paste Without Formatting. Do not copy the backtick lines. Paste. Save.

```text
"""A mark or a listed token is refused. A clean line is accepted.

Chapter 07 replaces the work copy with this file. Leave the packet
shell test unchanged.

The shell test expects the marked line to be accepted. This test
expects that line to be refused, a listed token in the text to be
refused, and a clean sentence to be accepted. clerk-row is a
stand-in in this test. It is not a history id. The line parents[1]
stays as it is.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from scan import accept


class ScanTests(unittest.TestCase):
    def test_watermark_and_national_id_are_refused(self) -> None:
        """The mark and a listed token fail. A clean sentence passes."""
        self.assertFalse(accept("CANARY-x", ["clerk-row"]))
        self.assertFalse(accept("see clerk-row", ["clerk-row"]))
        # A clean invented sentence is still accepted.
        self.assertTrue(accept("Kindly review endocrinology.", ["clerk-row"]))


if __name__ == "__main__":
    unittest.main()
```

Open the work file you just saved. Search inside that file, not inside this chapter. You should see `test_watermark_and_national_id_are_refused`. You should see `parents[1]`. Leave that line. `clerk-row` is a stand-in. It is not a history id. That is expected. The clean sentence still has `assertTrue`. That is expected.

This page is done when you have saved all six work files. Search each one, not this chapter. `labels.py` has `ann-v2`. `test_labels.py` has `test_photo_and_retina_follow_ann_v2`. `synthetic.py` has `rare_sub_specialty`. `test_synthetic.py` has `test_rare_class_has_no_real_id`. `scan.py` has `CANARY-`. `test_scan.py` has `test_watermark_and_national_id_are_refused`. The packet copies still contain `ann-v1`, `letters[:1]`, and `return True`. That is expected. Do not run a command on this page. Do not run the check until [chapter 10](10-finish.md).

Next: [08 — The advanced path](08-the-advanced.md).
