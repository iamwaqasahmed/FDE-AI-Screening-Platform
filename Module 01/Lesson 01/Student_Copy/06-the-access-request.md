# 06 — The access request

An access request is the cluster's record of what you asked to see. A value has to sit on the same line as its label. The checker treats an empty value as a missing field.

The blank form is [packet/kickoff/forms/access-request.md](packet/kickoff/forms/access-request.md). It has four labels: Requester, Data, Purpose, and Classification.

## Do this

Open a terminal in the course folder, the same way as chapter 01. Then run:

```text
cd "Module 01/Lesson 01/Student_Copy"
python prepare_work.py form
```

You should see `Copied the blank form to work/access-request.md`.

Open `work/access-request.md`. Replace the four empty lines with these, and put your own name after `Requester:`:

```text
- Requester: Your Name
- Data: the kickoff files and the watermarked dev credentials
- Purpose: Module 1 Lesson 1 interviews and the starter pipeline
- Classification: internal
```

You are the person asking. A persona name is someone you may interview, not the requester. Full history means the measurements and the files that arrive on later mornings. Those stay off the Data line. Today you ask for the kickoff and the dev credentials. The three labels, and when to use each one, are in [chapter 04](04-words.md). `internal` is the label for today's kickoff and the dev credentials.

Keep the hyphen and the label. The value stays on the same line, after the colon.

## You should now see

`work/access-request.md` has a value on each of the four lines. The headings of the form can stay. The checker reads those four lines and ignores a blank worksheet in `notes/`.

## If the check later says a field is missing

The value is on the line below the label, or the label was rewritten as a heading. Put the value back on the same line, after the colon, and keep the hyphen at the start of the line.

Next: [07 — The pipeline](07-the-pipeline.md).
