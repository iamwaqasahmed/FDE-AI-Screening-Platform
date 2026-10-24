# Week 4, Day 1 — Security and governance

Facilitator only.

## Objective

The hidden attack set fails to move a booking, a canary, or an approval, and the DPIA is filled.

## Teach before the lab

The attack library, residency, deletion, the breach clock, and risk tiers.

## Case

Attacks, the PHI-in-logs notice, the checklist, and the first data-subject requests. Release `rel-w4d1`. The 72-hour clock starts at this release's case timestamp.

## Lab and trap

Turn on guardrails, close stale `iam` access, complete `tpl-dpia`, and handle one access and one deletion request. The trap is testing only direct injection, or deleting the database row and leaving the vector index.

## Check and demo

`chk-w4-redteam`, `chk-w4-privacy`, `chk-w4-access`, `chk-w4-fair`. Show `atk-indirect` on `practice` booking a slot the letter asked for.
