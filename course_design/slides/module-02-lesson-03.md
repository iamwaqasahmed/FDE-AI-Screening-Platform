# Module 2, Lesson 3 — The receipt — Testing and experience

Facilitator only.

## Objective

The suite fails when a seeded fault is switched on, and a low-literacy task can be finished.

## Teach before the lab

A deterministic clock, recorded model calls, contract tests, and usability scripts.

## Case

Receipt timing changes. Accessibility clauses arrive. Release `rel-m02-l03`.

## Lab and trap

Write unit tests for the calendar and the reply schema, pin the clock, record model responses, cover integration and end-to-end journeys, and run `ds-usability`. The trap is a test that sleeps for the old receipt delay.

## Check and demo

`chk-tests`, `chk-ux`. Show the suite going red when the receipt switch is flipped.
