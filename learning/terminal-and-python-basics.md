# Terminal and Python basics

Read this once if the setup chapter's commands are new. It adds no file and no command. The lesson's chapter is still the instruction.

## The terminal

A terminal is a window that runs one command at a time. Chapter 01 tells you how to open one already inside the course folder. The course folder is the folder that contains `problem_simulation` and `Module 01`.

`cd` changes the folder. `cd problem_simulation` moves into that folder. `cd ..` moves up one folder. On Windows, `dir` lists the names. On macOS and Linux, `ls` lists the names.

When a path contains a space, the chapter puts it in quotes: `cd "Module 01/Lesson 01/Student_Copy"`. Keep the quotes.

The prompt returns when the command has finished. A command that sits there with no prompt is still running. Chapter 01 of a later lesson says when to press Ctrl+C to stop one.

## Python

`python --version` prints the version. This course wants Python 3.12 or newer.

`python -m something` runs a module that is already installed with the course. You do not install a package for it. The chapter names the module.

`py` is the Windows launcher. Use it only when the chapter says `python` is not recognized. `python3` is the name macOS and Linux often use. Use the one command that prints a version, and keep using that name for the rest of the day.

## What a test printout is

A chapter that says to run unittest wants lines like these:

```text
Ran 1 test in 0.001s

OK
```

`Ran` counts the tests. `OK` means they passed. `FAILED` means at least one did not. A traceback is the block of file names above `FAILED`. Read the last file name. That is the file to reopen. Do not repair spaces by hand when the chapter says to paste the block again.

## Files you will see

JSON is a set of named values in braces. JSONL is one JSON value per line. CSV is a table with commas. YAML is a set of named values with indentation. You read them when a chapter says to open one. You do not need to write a new format.

## Pasting

Copy from the chapter file, not from a preview. Paste without formatting. The spaces at the start of a Python line are part of the program.
