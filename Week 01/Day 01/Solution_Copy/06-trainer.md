# 06 — Trainer session

Students can skip this page. The answers are in chapters 01 through 05.

Use this page after the attempt. Teach one block, then the next. Have their `work/` folder and this solution open.

## Before you start

Leave these closed: `problem_simulation/build`, `problem_simulation/alwaha/engagement/catalog.py`, and `course_design`.

Do not open the sample letter or `credentials/dev.json` on a screen. Do not paste the watermark into a slide or a prompt.

From the repository root, both checks print `passed`:

```text
cd problem_simulation
python -m alwaha.check repo --work "../Week 01/Day 01/Solution_Copy/work" --profile practice
python -m alwaha.check interview --work "../Week 01/Day 01/Solution_Copy/work" --profile practice
```

## Block 1 — The sentence

Open their `notes/my-page.md`.

Ask what they would refuse to build from the sponsor's sentence alone.

Take one claim, and one sentence they can point at in a kickoff file.

## Block 2 — The access request

Open their `work/access-request.md` beside [chapter 02](02-the-reading-and-the-request.md).

Show the four lines. Say the requester can be their own name. Hanan Al-Salem is only the example.

A form that looks done and still fails has a blank after the colon, or the value on the next line.

## Block 3 — 2023

Have them read their `notes/reading-notes.md` first. Then show the two columns in chapter 02.

The write-up: a busy season, low usage, and a plan to revisit a front door.

The minutes: no evaluation set, patient data sent to a public model, no named owner, and no decision to turn the bot back on.

The usual miss is treating the write-up as the whole story.

## Block 4 — The scan

Open [chapter 03](03-the-pipeline.md). Say the success line: `scan passed.`

The scan fails when `work/` holds the sample letter, a private key, or the watermark outside `credentials/`.

To show a failure, copy the sample letter to a junk file in a throwaway copy of `work/`, run `python scan.py`, and let the room see the line that names `sample letter marker` and the junk file. Delete the junk file before the next check. Do not display the letter.

## Block 5 — One interview

Open [chapter 04](04-the-interviews.md). Read one transcript aloud, the medical director or the data protection officer.

Say why this pair: triage, and where patient data may go. Another pair can pass.

Show the order: the goal first, then what that answer is made of.

A miss is a third script, a follow-up asked first, or a confident sentence labeled `fact`. `pol-clinical-safety` is not in today's kickoff, so naming it stays a claim.

When the check says an interview is incomplete, it will not name the missing fact. Send them back to the goals on the card.

Say these two sentences once, and tell the room to keep them out of the notes. Pasting either one fails the check:

- `The assistant may set clinical urgency.`
- `The external model may receive identified patient data.`

The check says `notes contain a banned sentence` and does not repeat the sentence.

## Block 6 — Knowledge and zones

Open [chapter 05](05-knowledge.md) beside their `work/knowledge.md`.

G0 names the problem, the users, and the sponsor. Naming them is not the same as accepting the sentence. A pilot is G3.

The assistant may see code they wrote, the tests, and the published rule. Patient data, secrets, unpublished documents, the sample letter, and the watermark stay out.

Zones: `h-nakhl`, `h-safra`, and `h-ain` in `zone-hospital`. `h-wadi` in `zone-private`. `zone-public` is the external model and has no hospital.

The usual miss is calling today a pilot, or placing a hospital in `zone-public`.

Both checks can print `passed` while this file is still thin. You grade this file.

## Close

Keep this pipeline and these notes. The next morning brings a new pack. Leave later day folders closed.

Misses to keep in your pocket: treating the sponsor's sentence as the problem, calling today a pilot, a third interview, a follow-up asked first, the sample letter or the watermark copied into `work/`, and a confident sentence labeled `fact`.
