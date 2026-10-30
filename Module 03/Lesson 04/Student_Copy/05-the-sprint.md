# 05 — The sprint

[Chapter 04](04-words.md) named the words. This chapter is the sprint. The check scores the order of the words in `work/sprint.md`. The score comes first, then the failures, then the workshop. The workshop stays on evidence.

You do not build the pack again. Today's drop is the one chapter 01 built. You read the copies in this folder. This page has one block to paste. It is under Replace the sprint. There is no picture of a shell on this page, and there is no Python. The checks run in chapter 10. Do not run them from this page.

The same four steps are used on every later paste:

1. Open the work file named under the Replace heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from the chapter file, not from a preview. A preview is the rendered page. It can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

## Read this file

Open [hidden-test.md](packet/release/notices/hidden-test.md). Search for `grading`. Labels stay on the grading service. The sprint is where you write the order of the work: the score, then the failures, then the workshop. The workshop stays on evidence.

## Replace the sprint

Chapter 01 copied [sprint.md](packet/templates/sprint.md) to [work/sprint.md](work/sprint.md). The full path is `Module 03/Lesson 04/Student_Copy/work/sprint.md`. If that link does not open, `work/` is not there yet. Run the prepare command in [chapter 01](01-setup.md), then come back to this page. The copy already has the heading and an empty section under it. Do not type into the empty section. This block replaces the whole file. It does not replace the template in `packet/templates`. This block has no pipe table.

1. Open the work file named here, [work/sprint.md](work/sprint.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `evidence`.

```text
# Sprint

## Order

Score the extraction, the citation, and the journeys, then name the failures, then the workshop.

The workshop stays on evidence.
```

The lines have to mention score, then failure, then workshop, in that order. The check looks for that order. It also looks for the word `evidence`. It does not print those words back.

Open [work/sprint.md](work/sprint.md). Search inside that file, not inside this chapter. You should see the heading `Sprint`, then `Order`, then two sentences. The first sentence starts with `Score`. The second contains `evidence`. If the file is still only the heading and an empty Order section, the paste did not land. Select the whole file, delete it, and paste the block again. If those words are in another order, paste the block again. The template in `packet/templates` is still the blank. That is expected.

This page is done when `work/sprint.md` has score, then failure, then workshop, in that order, and it contains `evidence`. Do not run a check from this page.

Next: [06 — The harness](06-the-harness.md).
