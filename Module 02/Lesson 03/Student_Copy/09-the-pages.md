# 09 — The pages

[Chapter 08](08-the-receipt.md) ran the suite. This chapter writes the four pages the second check reads. The checks run in chapter 10. Do not run them from this page.

You replace four files. Each one uses the same four steps.

1. Open the work file named in that section. Do not open the template in `packet/templates` for the paste.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy the lines inside that section's block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it.
4. Paste. Save. Keep every pipe character. If the paste lands as one long line, or a column is missing, select the whole file, delete it, and paste again. Do not repair a table by hand.

## Why a row says what it says

Open these. You do not edit them, and you do not paste them into `work/`.

1. [scripts.jsonl](packet/release/usability/scripts.jsonl). `status-short` and `caregiver` are `foundation`. `phone-only` is `advanced`. Do not add `phone-only` to the table.
2. [access.md](packet/release/standards/access.md). Four clause ids. The usability page cites each one.
3. [receipt.json](packet/release/clock/receipt.json). Search for `switch`. The value is `receipt-late`. The definition of done uses that name.
4. [timing.md](packet/release/notices/timing.md). Search for `SMS partner`. The receipt leaves the private cloud for that partner.
5. [zones.md](packet/kickoff/world/zones.md). Search for `zone-private`. The calendar stays there. The receipt starts there.

## Replace the usability page

Chapter 01 copied [usability.md](packet/templates/usability.md) to [work/usability.md](work/usability.md). The full path is `Module 02/Lesson 03/Student_Copy/work/usability.md`. Use the four steps at the top of this page on that work file. Do not type into the empty cells. This block replaces the whole file. It does not replace the template in `packet/templates`.

`status-short` is a short message, so one row cites `plain-language`. The control on that task has a name, so the next row cites `named-control`. The `caregiver` script is a caregiver finishing the task, so one row cites `caregiver-complete`. That task has one next step, so the last row cites `one-action`. Both scripts are finished, so the middle column is `yes`.

```text
# Usability

| script | finished | clause |
| --- | --- | --- |
| status-short | yes | plain-language |
| status-short | yes | named-control |
| caregiver | yes | caregiver-complete |
| caregiver | yes | one-action |
```

The columns are `script`, `finished`, and `clause`. Leave both pipes on each row.

Read the file back. You should see `status-short` twice and `caregiver` twice. You should see `yes` in the finished column. You should see the four clause ids. You should not see `phone-only`. The check says a usability script is unfinished when one of those two scripts is missing or the finished cell is not `yes`. It says an accessibility clause is missing when one of the four ids is absent. It does not name the script or the clause.

## Replace the definition of done

This block replaces [work/dod.md](work/dod.md). It does not replace [packet/templates/dod.md](packet/templates/dod.md). Use the four steps at the top of this page. The full path is `Module 02/Lesson 03/Student_Copy/work/dod.md`.

The sentence names the switch you read in `receipt.json`. The suite goes red when that switch is on. The demo's second line was `switch on: failed`. That line did not print the switch name. This page is where you label it.

```text
# Definition of done

receipt-late is on this list. The suite goes red when that switch is on.
```

Read the file back. You should see `receipt-late`. You should see `red`. The check says the fault is not in the definition of done when either one is missing. The message does not name the switch.

## Replace the zone page

This block replaces [work/crossings.md](work/crossings.md). It does not replace [packet/templates/crossings.md](packet/templates/crossings.md). Use the four steps at the top of this page. Keep every pipe character. The columns are `case`, `from`, and `to`.

The receipt starts in `zone-private` and goes to the SMS partner. The calendar stays in `zone-private`.

```text
# Zone crossing

| case | from | to |
| --- | --- | --- |
| receipt | zone-private | partner |
| calendar | zone-private | zone-private |
```

Read the file back. You should see a receipt row and a calendar row. The receipt row leaves `zone-private` for `partner`. Both cells on the calendar row are `zone-private`. The check says a zone-crossing case is missing when either row is wrong. It does not name the case.

## Replace the fixture note

This block replaces [work/fixtures.md](work/fixtures.md). It does not replace [packet/templates/fixtures.md](packet/templates/fixtures.md). Use the four steps at the top of this page.

The journey reads the recorded fixture in the pack. It asserts the mock state. It does not copy the file. Leave [model.json](packet/release/fixtures/model.json) where it is.

```text
# Fixture

The journey reads the recorded fixture in the pack. It asserts the mock state. It does not copy the file.
```

Read the file back. You should see `fixture` and `state`. You should not see the watermark. The check says the fixture note is missing when either word is absent.

Next: [10 — Finish](10-finish.md).
