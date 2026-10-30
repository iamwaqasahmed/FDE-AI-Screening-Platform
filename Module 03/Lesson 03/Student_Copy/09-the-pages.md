# 09 — The pages

[Chapter 08](08-the-advanced.md) ran the suite. This chapter replaces the refusal and the audience table. There is no picture of a shell on this page, and there is no Python. The checks run in chapter 10. Do not run them from this page.

You replace two files under `work/`:

1. [refusal.md](work/refusal.md), under Replace the refusal
2. [audience.md](work/audience.md), under Replace the audience table

The four steps from [chapter 05](05-the-sprint.md) are repeated above each paste. Leave the copies in `packet/templates` unchanged. The packet templates stay blank.

## Replace the refusal

Chapter 01 copied [refusal.md](packet/templates/refusal.md) to [work/refusal.md](work/refusal.md). The full path is `Module 03/Lesson 03/Student_Copy/work/refusal.md`. This block replaces the whole file. It does not replace the template in `packet/templates`.

1. Open the work file named here, [work/refusal.md](work/refusal.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `no document` and `cannot see`.

```text
# Refusal

When no document is in force, say that no document binds the answer.

When the asker cannot see the document, say it is not for them.
```

Open [work/refusal.md](work/refusal.md). Search inside that file, not inside this chapter. You should see `no document` and `cannot see`. The template in `packet/templates` is still only the heading. That is expected.

## Replace the audience table

Chapter 01 copied [audience.md](packet/templates/audience.md) to [work/audience.md](work/audience.md). The full path is `Module 03/Lesson 03/Student_Copy/work/audience.md`. This block replaces the whole file. It does not replace the template. Keep the pipe characters. A preview can drop them. Open this chapter's `.md` file before you copy. After you save, the patient line still starts with `| patient |`. A table without the pipes is not the table the check reads.

1. Open the work file named here, [work/audience.md](work/audience.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `asker` and `audiences`.

```text
# Audience

| asker | audiences |
| --- | --- |
| patient | public |
| staff | public, staff |
| records | public, staff, restricted |
```

Open [work/audience.md](work/audience.md). Search inside that file, not inside this chapter. You should see a row that starts with `| patient |` and the cell `public`. That row must not contain `staff` or `restricted`. The staff row contains `public` and `staff`, and it must not contain `restricted`. The records row contains `restricted`. The pipe characters are still there. If a pipe is missing, select the whole file, delete it, and paste the block again.

This page is done when `work/refusal.md` contains `no document` and `cannot see`, and `work/audience.md` has the three rows with the pipe characters. Do not run a check from this page.

Next: [10 — Finish](10-finish.md).
