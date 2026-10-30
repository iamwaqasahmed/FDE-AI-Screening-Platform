# 07 — The note

[Chapter 06](06-the-worker.md) wrote the log. This chapter fills the intake note. The check reads it. The note below is the page that makes that part of the check pass. You still read what each step is, and you still keep the acceptance line as the product decision.

## Copy the blank

Open a terminal in the course folder, the same way as chapter 01. Leave the window that is still inside `problem_simulation`. If chapter 01 told you to use `py` instead of `python`, use `py` here too.

```text
python "Module 01/Lesson 03/Student_Copy/prepare_work.py" note
```

You should see `Copied the blank intake note to work/intake.md.`

The blank you are copying is [intake.md](packet/templates/intake.md). Leave that file unchanged. After the command, edit the copy: [work/intake.md](work/intake.md). The link opens once the command has written the file. If it does not open, run the command again from the course folder, then open `Module 01/Lesson 03/Student_Copy/work`.

Run the command once. A second run replaces whatever you have written. If the command says to run it first with no extra word, do the chapter 01 command, then this one. The `note` command does not refresh the scripts.

## Replace the note

Select the whole copy and replace it with this block. Keep the heading lines. The check looks for a coordinator, or the word human, and it looks for an in-flight referral that keeps its criteria version.

```text
# Intake

## Steps

1. referral.submitted
2. extract
3. retrieve the criteria in force
4. duplicate check
5. suggest a clinic
6. a coordinator holds the approval

## Acceptance

The workflow stops when a coordinator holds the approval. It does not book.

## In-flight criteria

An in-flight referral keeps the criteria version it started with.
```

Step 6 is the human step. The acceptance line is the product decision: stop for that coordinator, and do not book. The in-flight line is a rule you are writing down. A referral that has already started keeps the criteria version it started with. A later criteria page does not replace that version. The worker you pasted does not store an old version. No event today changes the document after a referral has started. The check looks for the words in-flight, criteria, and version in this note.

The check does not score the wording beyond those pieces. If you add a sentence, keep the three headings and keep those words in the file.

Next: [08 — Finish](08-finish.md).
