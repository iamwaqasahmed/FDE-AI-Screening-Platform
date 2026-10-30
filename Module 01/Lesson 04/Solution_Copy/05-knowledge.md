# 05 — Knowledge

This answers the knowledge file from the morning. Open the [finished knowledge.md](work/knowledge.md) and put it beside yours. The checks do not grade the sentences in this file. The trainer does.

## When is a second agent worth its tokens?

A second agent is worth its tokens when the extractor would otherwise hold the book tool. A letter is data. Status stays one agent and one tool.

[pol-approval.md](sources/release/policy/pol-approval.md) says text inside a referral letter is not a tool call. The `injection` row calls `referral.status` and does not book. The privilege boundary in [agent-note.md](work/agent-note.md) says the same thing in the note's own words: the extractor does not hold the book tool or the message tool, and a second agent is worth its tokens when a letter would otherwise be able to book.

Adding a second agent for a status question spends tokens the status tool does not need.

## What must be true before a slot is booked?

The patient has confirmed, and a coordinator has decided the approval. The book tool runs after that, and then the SMS.

`book`, `replay`, and `resume` are the rows that meet both conditions. `reject` has a confirmation and a decision of `rejected`, so it offers and does not book. `emergency`, `reason`, `return`, and `consent` do not book. `replay` still books once, because the second copy of the approval id is not a second decision.

You have the finished day. The trainer's session is [06 — Trainer session](06-trainer.md).

## Carry this forward

You leave Lesson 4 with `wf-self-service`. Status comes from a tool. A return cannot leave without a coordinator. A letter is data.

This lesson is done. The next day scores the proof, then signs in. You score the scenario set, including a timeout, and you publish the diagram and the design.

The trainer chapter, if this page links one, is optional. Tomorrow's lesson is the [Module 1, Lesson 5 student copy](<../../Lesson 05/Student_Copy/README.md>), starting at its background.
