# 07 — The note

[Chapter 06](06-the-agent.md) wrote the trace. This chapter fills the agent note. The checks read it. The note below is the page that makes that part of the checks pass. You still read what each section is, and you still keep the refusal sentence as the product decision.

## Copy the blank

Open a terminal in the course folder, the same way as chapter 01. Leave the window that is still inside `problem_simulation`. If chapter 01 told you to use `py` instead of `python`, use `py` here too.

```text
python "Module 01/Lesson 04/Student_Copy/prepare_work.py" note
```

You should see `Copied the blank agent note to work/agent-note.md.`

The blank you are copying is [agent-note.md](packet/templates/agent-note.md). Leave that file unchanged. After the command, edit the copy: [work/agent-note.md](work/agent-note.md). The link opens once the command has written the file. If it does not open, run the command again from the course folder, then open `Module 01/Lesson 04/Student_Copy/work`.

Run the command once. A second run replaces whatever you have written. If the command says to run it first with no extra word, do the chapter 01 command, then this one. The `note` command does not refresh the scripts.

## Replace the note

Select the whole copy and replace it with this block. Keep the three heading lines. The checks look for `referral.status` under the tool list, for the word extract and the word book or the word message under the privilege boundary, and for a refusal of at least three words.

```text
# Agent note

## Tool list

- `referral.status` reads the queue. The reply count is that result.
- `slots.offer` lists a slot, or names the constraint that blocks it.
- `slots.book` writes a booking. It waits for an approval id.
- `sms.send` runs after the booking.
- `referral.return` sends a return. It waits for an approval id.
- `safety.redirect` hands the conversation to a person.

## Privilege boundary

The extractor reads the letter and does not hold the book tool or the message tool. A second agent is worth its tokens when a letter would otherwise be able to book. Status stays one agent and one tool, `referral.status`.

## Refusal

A coordinator will answer, and this visit is not booked.
```

The tool list is the catalog from chapter 05, in the agent's own words. The privilege boundary is the architect's line: the part that reads a letter does not hold book or message. Status stays one agent and one tool. The refusal line is the product decision you are writing in this note. A coordinator will answer, and this visit is not booked. That sentence covers a rejection, a constraint, and a stored preference that cannot be reused.

That sentence is not what the trace stores. Do not edit `model.py` or `trace.json` so the reply text matches this note. After the run, compare the note with these reply texts. Status and reject say `Done.` Emergency says `A person will take this from here.` Consent says `Say what you need for this visit.` Reason says `No slot meets the constraint.` The check reads this note for a refusal of at least three words. It does not compare the note with those trace texts.

The checks do not score the wording beyond those pieces. If you add a sentence, keep the three headings and keep those words in the file.

Next: [08 — Finish](08-finish.md).
