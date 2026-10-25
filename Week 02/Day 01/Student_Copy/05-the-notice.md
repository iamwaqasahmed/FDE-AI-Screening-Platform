# 05 — The notice

[Chapter 04](04-words.md) named the words. This chapter is the reading and the sprint. The checks do not score the notice. They score the order of the sentences you write in `work/sprint.md`.

You do not build the Week 1 packs again. Today's drop is the one chapter 01 built. You read the copy in this folder. The checks run in chapter 08. Do not run them from this page.

## Read these two files

Open them in this order:

1. [fhir-v2.md](packet/release/notices/fhir-v2.md). Search for `FHIR v2`. The spec in this release is the one to generate from. A field from the hand-written client is gone. The notice does not ask you to type that field into the sprint.
2. [his-wadi.yaml](packet/release/openapi/his-wadi.yaml). Search for `his-wadi`. This is the spec. [Chapter 07](07-the-status.md) points the generator at this file.

Booking is a later day. A status question can be answered now. That is the whole notice.

## Replace the sprint

Chapter 01 copied [sprint.md](packet/templates/sprint.md) to [work/sprint.md](work/sprint.md). The full path is `Week 02/Day 01/Student_Copy/work/sprint.md`. The copy already has the headings and empty sections under them. Do not type into the empty sections. This block replaces the whole file. It does not replace the template in `packet/templates`.

Open `work/sprint.md`. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. Paste. Save.

```text
# Sprint

## First

Generate the his-wadi client from the spec. Sign in a patient and a coordinator. Answer a status question.

## Later

Booking waits until the client is in place.
```

The first section has to mention generating the client before the page mentions booking. The check looks for that order. It does not print the two words it looked for.

Read the file back. You should see the heading `Sprint`, then `First`, then `Later`. The generate sentence is under First. The booking sentence is under Later. If both sentences sit under the same heading, select the whole file, delete it, and paste the block again.

Next: [06 — Sign-in](06-the-sign-in.md).
