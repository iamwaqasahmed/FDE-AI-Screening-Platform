# Week 4, Day 3 — Serving and the surge

Facilitator only.

## Objective

Chat holds its latency while a batch is running, inside the token budget.

## Teach before the lab

Batching, quotas, cold starts, and the price change.

## Case

The forecast, the new external price, and 12,000 referrals. Release `rel-w4d3`.

## Lab and trap

Serve the registered adapters, run `load-chat` and `load-batch` together, and record tokens per second and SAR. The trap is sending the batch to `ext-large` because it is faster today.

## Check and demo

`chk-w4-slo` (load portion), `slice-surge`. Show a scale-from-zero run on `practice` missing the first window.
