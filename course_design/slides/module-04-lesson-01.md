# Module 4, Lesson 1 — Guardrails — Security and governance

Facilitator only.

## Objective

The hidden attack set fails to move a booking, a canary, or an approval, and the DPIA is filled.

## Teach before the lab

The attack library, residency, deletion, the breach clock, and risk tiers.

## Case

Attacks, the PHI-in-logs notice, the checklist, and the first data-subject requests. Release `rel-m04-l01`. The 72-hour clock starts at this release's case timestamp.

## Lab and trap

Turn on guardrails, close stale `iam` access, complete `tpl-dpia`, and handle one access and one deletion request. The trap is testing only direct injection, or deleting the database row and leaving the vector index.

## Check and demo

`chk-m04-l01-redteam`, `chk-m04-l01-privacy`, `chk-m04-l01-access`, `chk-m04-l01-fair`. Show `atk-indirect` on `practice` booking a slot the letter asked for.
