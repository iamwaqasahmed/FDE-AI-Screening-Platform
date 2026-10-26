# 03 — The request

[Chapter 02](02-the-role.md) said you hold all five parts. This chapter is the data request, the history, and the four lines the demo prints.

## What you do on this page

Three steps. You do not edit a file. You do not paste a block from this page into `work/`.

1. Open each linked file. In Cursor or VS Code, Ctrl+click the link on Windows, or Command+click on macOS. If the link does not open, the path is in the sentence beside it.
2. Search that file. Press Ctrl+F on Windows or Command+F on macOS, then type the word this page names. A fenced block under Read the request or Read the history is a picture. Leave the picture on this page.
3. Run the command under Run the demo. That block is a command, not a picture. You should see four lines. Then keep reading this page through the history rows. The last line of the page names chapter 04.

## Read the request

Open [data-request.md](packet/release/notices/data-request.md). Search for `approved`. The next block is a picture of that file. Do not paste it.

```text
# Data request

The data request is approved. This pack is the full history, not the Week 1 sample.

Patient data still stays off the external model ext-large. An export needs a classification check before it is shared.

Case date: 2027-01-24.
```

Open [ann-v2.md](packet/release/guidelines/ann-v2.md). Search for `photo`. The next block is a picture of that file. Do not paste it.

```text
# ann-v2

ann-v2 adds a source type and requires the sub-specialty when the text names one.

If the text says phone or photo, the source type is photo. If it says scan, and it does not say phone or photo, the source type is scan. Otherwise the source type is typed.

If the text says retina, the sub-specialty is retina. If it says pediatric, the sub-specialty is pediatric. Otherwise the sub-specialty stays blank.
```

Open [clinics.md](packet/release/catalog/clinics.md). Search for `June 2024`. The next block is a picture of that file. Do not paste it.

```text
# Clinics

The catalog still defines the endocrinology clinic code END-01.

In June 2024, h-wadi changed that clinic to ENDO-CLN. Rows before June 2024 keep END-01.
```

## Run the demo

Leave the window you used for `prepare_work.py`. Open a terminal in the course folder. If that window is already inside `problem_simulation`, skip the `cd` line and run the python line.

```text
cd problem_simulation
python -m alwaha.demo.merge --profile practice
```

You should see four lines, and nothing else. The prompt returns after the fourth line.

1. The first line is the mother's MRN. It is computed for `practice`. Do not type it onto a page.
2. The second line is the newborn's MRN. It is a different value. It is computed. Do not type it.
3. The third line is the national id those two rows share. It is computed. Do not type it.
4. The fourth line is `These two MRNs stay two people.`

If you see more than four lines, or you do not see that fourth sentence, the command was not `python -m alwaha.demo.merge --profile practice`. Run that command again from `problem_simulation`.

## Read the history

Open [identifiers.jsonl](packet/release/history/identifiers.jsonl). Each row is one long line. A search can land in the middle of that line. Read the whole line, and do not copy it. Every row has the same keys. The next block is the list of keys. The dots are not the values. The values are in the file. Do not paste this block.

```text
{"as_of": "...", "check_digit": "...", "clinic_code": "...", "district": "...", "dob": "...", "era": "...", "facility": "...", "merge_state": "...", "merge_with": "...", "mrn": "...", "name": "...", "national_id": "...", "phone": "...", "relation": "...", "replaces": "...", "row_id": "..."}
```

Search inside that file, not inside this chapter.

| Search for this | What you are reading |
| --- | --- |
| `"row_id": "mother"` | The mother's row. The `mrn` on this row is the first demo line. The `national_id` is the third demo line. Leave both values in the file |
| `"row_id": "newborn"` | The newborn's row. `relation` is `newborn`. The `mrn` is the second demo line. The `national_id` matches the mother's. Leave both values in the file |
| `"row_id": "twin-a"` | One twin. `relation` is `twin`. The phone matches `twin-b`. The national id does not |
| `"row_id": "twin-b"` | The other twin. Same phone. A different national id |
| `"row_id": "reuse-a"` | One person. The `mrn` matches `reuse-b`. The national id does not |
| `"row_id": "reuse-b"` | A second person on the reused MRN |
| `"row_id": "hijri-end"` | `dob` is `1448-07-29`. `era` is empty. That is a Hijri date. Do not write a converted day on this page |
| `"row_id": "hijri-start"` | `dob` is `1448-08-01`. `era` is empty |
| `"row_id": "clinic-before"` | `clinic_code` is `END-01`. `as_of` is `2024-05-01`. `facility` is `h-wadi` |
| `"row_id": "clinic-after"` | `clinic_code` is `ENDO-CLN`. `as_of` is `2024-07-01`. `facility` is `h-wadi` |
| `"row_id": "iqama"` | `replaces` names the visitor row's national id. Read that field in the file. Do not copy the id |
| `"check_digit": "fail"` | A failed check digit. The row is still a person |

Open [waitlist.jsonl](packet/release/history/waitlist.jsonl). Each row is one long line, with `flag`, `mrn`, `national_id`, and `row_id`. Search inside that file.

| Search for this | What it means |
| --- | --- |
| `death-late` | A removal proposal. The person stays in the cluster file |
| `seen-elsewhere` | A removal proposal. The person stays in the cluster file |
| `bounced` | This row stays |
| `resubmitted` | This row stays |
| `"flag": ""` | An empty flag. This row stays |

Do not copy an `mrn` or a `national_id` from this file onto a page. Finding the flag is enough.

## What you are deciding

Week 1's open item was one person stored as two rows. Today that shape is the Iqama row. Its `replaces` field names the visitor row's national id. Those two rows are one person.

The other rows are the opposite shape. A mother and a newborn who share a national id stay two people. Twins who share a phone stay two people. A reused MRN stays two people. A failed check digit does not remove a person. A Hijri month boundary stays on the civil day. After June 2024, endocrinology at h-wadi is ENDO-CLN. Rows before that keep END-01. June 2024 starts, in the clinic file, on `2024-06-01`.

This page is done when those four demo lines are on the screen, you have found `1448-07-29` and `1448-08-01` in the history file, and you have not copied a picture or an id into `work/`. The other rows can wait. Later chapters name them again.

Next: [04 — Words](04-words.md).
