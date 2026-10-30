# Module 1, Lesson 3 — Intake — Workflow orchestration

Facilitator only.

## Objective

The participant can run `wf-intake` from `referral.submitted` to a held approval.

## Teach before the lab

Events, the working-day SLA calendar, idempotency, and tool calls inside a workflow.

## Case

The stream and the SLA policy arrive. Release `rel-m01-l03`.

## Lab and trap

Implement intake against the dev mocks: extract, retrieve, duplicate check, suggest a clinic, and stop for a human. The trap is counting Friday as a working day, or booking `h-ain` live.

## Check and demo

`chk-events`. The diagram shows the human step. Show an out-of-order pair on `practice`.
