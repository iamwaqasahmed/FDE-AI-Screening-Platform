# 09 — The pages

[Chapter 08](08-the-advanced.md) ran the suite. This chapter replaces the patient page and the class table. There is no picture of a shell on this page. The blanks are short. The blocks under the Replace headings are the whole files.

Use the four steps from [chapter 05](05-the-sprint.md) on each block. Open the work file. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Select the whole file and delete it. Copy the lines inside the fence from this chapter file. Use Paste Without Formatting. Do not copy the backtick lines. Paste. Save. Search for the words that heading names.

These pages are not Python. Keep the pipe characters in the class table. A styled paste can drop them. If the table is no longer a grid, paste the block again from this chapter file.

Do not run a check from this page. The checks are in [chapter 10](10-finish.md).

## Replace the patient page

This block replaces [work/patients.md](work/patients.md). The full path is `Module 03/Lesson 01/Student_Copy/work/patients.md`. It does not replace [packet/templates/patients.md](packet/templates/patients.md).

```text
# One patient

One patient is not one row, not one MRN, and not one national id.

A mother and a newborn stay apart. Twins stay apart. A reused MRN stays two people.
```

Open the work file you just saved. Search inside that file, not inside this chapter. You should see `row`, `MRN`, `national`, `mother`, `newborn`, `twin`, and `reused`. One patient is not one row. One patient is not one MRN. One patient is not one national id. A mother and a newborn stay apart. Twins stay apart. A reused MRN stays two people. Do not type a national id value onto this page. The shared id stays on the demo and in the history file.

## Replace the class table

This block replaces [work/classes.md](work/classes.md). The full path is `Module 03/Lesson 01/Student_Copy/work/classes.md`. It does not replace [packet/templates/classes.md](packet/templates/classes.md).

```text
# Classes

| Field | Class |
| --- | --- |
| national id | phi |
| date of birth | phi |
| name | phi |
| phone | phi |

The synthetic file was scanned before it was shared.
```

Open the work file you just saved. Search inside that file, not inside this chapter. You should see the header `Field` and `Class`, then four rows, then the scan sentence. The pipe characters are still there. That is required. `national id` is the field name. It is not a value from the history file. Do not add a national id value. Do not add a converted date. The word `scan` is on the last line. That is expected.

This page is done when `work/patients.md` has row, MRN, national, mother, newborn, twin, and a reuse word, and `work/classes.md` has the four phi rows and the word scan. The templates in `packet/templates` are still the blanks. That is expected. Do not run the check from this page.

Next: [10 — Finish](10-finish.md).
