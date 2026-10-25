# Capacity

## Serve

lora-extract, lora-intent, and lora-local run on one process. An unregistered hash stays unloaded.

## Batch

The batched local rate is the one the sheet names for a batch. The unbatched rate misses the window.

## Route

The referral batch stays off ext-large. Public text may use ext-large.

## Quota

Chat and the batch share one pool. Chat keeps a reserve.

## Scale

Pre-scale from p-forecast. A start at the peak misses the first window.

## Price

Today's price.ext_large_per_1k replaces yesterday's price. A plan at yesterday's price is rejected. The table records SAR at today's price.

## Backlog

The campaign backlog finishes inside 48 hours.
