# 05 — The sprint

[Chapter 04](04-words.md) named the words. This chapter is the sprint. The check scores the order of the sentences you write in `work/sprint.md`. The suite comes before usability sign-off.

You do not build the Module 1 packs again. Today's drop is the one chapter 01 built. You read the copy in this folder. The checks run in chapter 10. Do not run them from this page.

## Read this file

Open [timing.md](packet/release/notices/timing.md). Search for `receipt-late`. The suite has to cover that switch before anyone signs off the scripts.

## Replace the sprint

Chapter 01 copied [sprint.md](packet/templates/sprint.md) to [work/sprint.md](work/sprint.md). The full path is `Module 02/Lesson 03/Student_Copy/work/sprint.md`. If that link does not open, `work/` is not there yet. Run the prepare command in [chapter 01](01-setup.md), then come back to this page. The copy already has the headings and empty sections under them. Do not type into the empty sections. This block replaces the whole file. It does not replace the template in `packet/templates`.

Open `work/sprint.md`. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. Paste. Save.

```text
# Sprint

## First

Write the suite. Pin the clock. Cover the receipt switch.

## Later

Usability sign-off comes after the suite is red on receipt-late.
```

The first section has to mention the suite before the page mentions usability. The check looks for that order. It does not print the two words it looked for.

Read the file back. You should see the heading `Sprint`, then `First`, then `Later`. The suite sentence is under First. The sign-off sentence is under Later. The switch name is on the Later line. If both sentences sit under the same heading, select the whole file, delete it, and paste the block again.

Next: [06 — The calendar](06-the-calendar.md).
