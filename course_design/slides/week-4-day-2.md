# Week 4, Day 2 — Observability and the incident

Facilitator only.

## Objective

The participant can reconstruct the incident from telemetry, and can show that old clinic hours are no longer served.

## Teach before the lab

Traces, metrics, cost, drift, shadow traffic, and cache invalidation.

## Case

The replay, the Ramadan-hours circular, and `shadow-extract`. Release `rel-w4d2`.

## Lab and trap

Dashboard for latency, errors, and tool failures. Write the incident timeline. Drop cached hours on `document.changed`. The trap is a dashboard that only has CPU, or a cache that survives the circular.

## Check and demo

`chk-w4-incident`, `slice-cache`. Show a trace on `practice` with a tool, a hash, and a token count.
