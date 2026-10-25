# 05 — The sprint

[Chapter 04](04-words.md) named the words. This chapter is the sprint. The check scores the order of the words in `work/sprint.md`. The cluster job comes first, then the relabel, then the sample, then the scan. Adjudication is on that list.

You do not build the pack again. Today's drop is the one chapter 01 built. You read the copies in this folder. This page has one block to paste. It is under Replace the sprint. There is no picture of a shell on this page, and there is no Python. The checks run in chapter 10. Do not run them from this page.

The same four steps are used on every later paste:

1. Open the work file named under the Replace heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from the chapter file, not from a preview. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Read the file back and look for the words that heading names.

## Read this file

Open [data-request.md](packet/release/notices/data-request.md). Search for `approved`. The request is the full history. The sprint is where you write the order of the work. The cluster job comes first, because one patient is not one row. The relabel, the sample, and the scan come after it. Adjudication is booked before the labels are used.

## Replace the sprint

Chapter 01 copied [sprint.md](packet/templates/sprint.md) to [work/sprint.md](work/sprint.md). The full path is `Week 03/Day 01/Student_Copy/work/sprint.md`. If that link does not open, `work/` is not there yet. Run the prepare command in [chapter 01](01-setup.md), then come back to this page. The copy already has the heading and an empty section under it. Do not type into the empty section. This block replaces the whole file. It does not replace the template in `packet/templates`.

Open `work/sprint.md`. The path must contain `Student_Copy\work`. If the path contains `packet`, close it and open the work copy. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. Paste. Save.

```text
# Sprint

## Order

The cluster job, then the relabel, then the synthetic sample, then the scan.

Adjudication time is booked with the coordinators before the labels are used.
```

The lines have to mention cluster, then relabel, then sample, then scan, in that order. The check looks for that order. It also looks for adjudication. It does not print the four words it looked for.

Open [work/sprint.md](work/sprint.md). Search inside that file, not inside this chapter. You should see the heading `Sprint`, then `Order`, then the cluster sentence, then the adjudication sentence. The word `sample` sits on the cluster sentence, between relabel and scan. That is expected. The check is looking for the word `sample`, and that word is on the same line as `synthetic`. If the four words are in another order, select the whole file, delete it, and paste the block again.

This page is done when `work/sprint.md` has cluster, then relabel, then sample, then scan, in that order, and it mentions adjudication. The template in `packet/templates` is still the blank. That is expected. Do not run a check from this page.

Next: [06 — The clusters](06-the-clusters.md).
