# 05 — The sprint

[Chapter 04](04-words.md) named the words. This chapter is the sprint. The check scores the order of the sentences you write in `work/sprint.md`. The deploy comes before the readout.

You do not build the Module 1 packs again. Today's drop is the one chapter 01 built. You read the copy in this folder. This page has one block to paste. It is under Replace the sprint. The check runs in chapter 10. Do not run it from this page.

## Read this file

Open [guide.md](packet/release/endpoint/guide.md). Search for `ns-team`. The image is deployed into that namespace before anyone books the readout.

## Replace the sprint

Chapter 01 copied [sprint.md](packet/templates/sprint.md) to [work/sprint.md](work/sprint.md). The full path is `Module 02/Lesson 04/Student_Copy/work/sprint.md`. If that link does not open, `work/` is not there yet. Run the prepare command in [chapter 01](01-setup.md), then come back to this page. The copy already has the headings and empty sections under them. Do not type into the empty sections. This block replaces the whole file. It does not replace the template in `packet/templates`.

Open `work/sprint.md`. The path must contain `Student_Copy\work`. If the path contains `packet`, close it and open the work copy. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. Paste. Save.

```text
# Sprint

## First

Build the image in CI and deploy it to the team namespace.

## Later

Book the readout after the deploy.
```

The first section has to mention the deploy before the page mentions the readout. The check looks for that order. It does not print the two words it looked for.

Read the file back. You should see the heading `Sprint`, then `First`, then `Later`. The deploy sentence is under First. The readout sentence is under Later. The word deploy also appears again on the Later line, after the readout. That is expected. The first deploy is the one that has to come first. If both sentences sit under the same heading, select the whole file, delete it, and paste the block again.

Next: [06 — The image](06-the-image.md).
