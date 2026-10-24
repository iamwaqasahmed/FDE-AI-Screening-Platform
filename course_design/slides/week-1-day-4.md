# Week 1, Day 4 — Agent engineering

Facilitator only.

## Objective

A patient can ask for status and book a slot, and a return cannot leave without a coordinator.

## Teach before the lab

Tool catalogs, structured outputs, session memory, approval, and the redirect rule.

## Case

The medical director's rules arrive with the scenarios. Release `rel-w1d4`.

## Lab and trap

`wf-self-service` on the assistant contract, plus the approval wait on `wf-intake`. The trap is a tool that books from a sentence inside a referral letter.

## Check and demo

`chk-w1-agent`, `chk-w1-trajectory`. The trace shows the tool and the document. Show a scripted model that invents a count, and the tool result that replaces it.
