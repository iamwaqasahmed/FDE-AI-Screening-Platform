# Week 3, Day 1 — Data, annotation, and synthetic text

Facilitator only.

## Objective

One person-level waitlist, labels that follow `ann-v2`, and a synthetic sample that passes the fidelity card.

## Teach before the lab

Identity, Hijri conversion, guideline versions, agreement, and fidelity.

## Case

The data request is approved. Adjudication and the label budget arrive. Release `rel-w3d1`.

## Lab and trap

Build clusters, convert dates, relabel a slice to `ann-v2`, generate a rare-class sample, and scan for canaries. The trap is merging a mother and a newborn, or training on clerk labels after the guideline changed.

## Check and demo

`chk-w3-identity`, `chk-w3-labels`, `chk-w3-synthetic`. Show a false merge on `practice` as two MRNs and one national id.
