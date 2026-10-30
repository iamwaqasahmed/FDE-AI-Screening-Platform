# 05 — The sprint

[Chapter 04](04-words.md) named the words. This chapter is the sprint. The check scores the order of the words in `work/sprint.md`. Smoke comes first, then the change, then the readout, then the retro.

You do not build the packs again. Today's drops are the ones chapter 01 built. You read the copies in this folder. This page has one block to paste. It is under Replace the sprint. There is no picture of a shell on this page, and there is no Python. The checks run in chapter 10. Do not run them from this page.

The same four steps are used on every later paste:

1. Open the work file named under the Replace heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from the chapter file, not from a preview. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Read the file back and look for the words that heading names.

## Read this file

Open [cr-ain.md](packet/release/notices/cr-ain.md). Search for `Sequence`. The change is sequenced. The sprint is where you write that order. The smoke test is already done. It comes first.

## Replace the sprint

Chapter 01 copied [sprint.md](packet/templates/sprint.md) to [work/sprint.md](work/sprint.md). The full path is `Module 02/Lesson 05/Student_Copy/work/sprint.md`. If that link does not open, `work/` is not there yet. Run the prepare command in [chapter 01](01-setup.md), then come back to this page. The copy already has the heading and an empty section under it. Do not type into the empty section. This block replaces the whole file. It does not replace the template in `packet/templates`.

Open `work/sprint.md`. The path must contain `Student_Copy\work`. If the path contains `packet`, close it and open the work copy. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. Paste. Save.

```text
# Sprint

## Order

Smoke the URL, then sequence the change, then the readout, then the retro.
```

The line has to mention smoke, then change, then readout, then retro, in that order. The check looks for that order. It does not print the four words it looked for.

Read the file back. You should see the heading `Sprint`, then `Order`, then the one sentence. The word `sequence` sits on that sentence, between smoke and the change. That is expected. The check is looking for the word `change`, and that word is on the same line. If the four words are in another order, select the whole file, delete it, and paste the block again.

This page is done when `work/sprint.md` has smoke, then change, then readout, then retro, in that order. The template in `packet/templates` is still the blank. That is expected. Do not run a check from this page.

Next: [06 — The booking](06-the-booking.md).
