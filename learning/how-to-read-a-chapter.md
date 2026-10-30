# How to read a replacement chapter

Many lessons from Module 1, Lesson 3 onward hand you a finished Python file to paste. The check runs that file again. A log or a trace you type by hand is not what it grades. Pasting is the way the file gets into `work/`. Reading is the way you can explain it afterward.

## Two kinds of block

A chapter often shows the shell first. The shell is the starter that fails the check. The chapter calls that block a picture. You do not paste a picture. The sentence it tells you to search for is the sentence that must not remain in `work/`.

The block under a heading that starts with Replace is the file you paste into `work/`. Paste that block only. Leave the copy in `packet/` unchanged.

If the chapter says everything above the first Replace heading is a picture, the section **How the replacement works** is the exception. Read it. Do not paste it.

## What to read in the file

The docstring at the top of a pasted file is the purpose. The check often searches for a sentence from that docstring, so the paste has to stay intact. The comments inside name the step the shell got wrong.

You do not need to memorize every helper. You need the path:

1. What arrives (an event, a letter, a span, a grant).
2. Which function decides.
3. What that function refuses to do.
4. What it writes, and which check reads that output.

The section How the replacement works on the chapter is that path, in the order the file actually uses. It adds no file and no command.

A line that starts with "Before you paste, say" is a question you answer in your head. It is not a file, and it is not a command. The next heading that starts with Replace is the paste.

## When the paste breaks

`SyntaxError` or `IndentationError` means the spaces moved. The chapter says to run `prepare_work.py` and paste again from the chapter file. Do not repair the spaces by hand. A styled paste is the usual cause.

## When the check fails

The finish chapter names the line and the chapter to reopen. Come back to How the replacement works and find the function that owns that line. Then look at the saved file under `work/`, not at the picture in the chapter.

## After the day

The solution copy is the same files, already saved. Open it when the finish chapter says Done is true. Read the morning section beside the finished file. The solution chapter names the decision the check prints.
