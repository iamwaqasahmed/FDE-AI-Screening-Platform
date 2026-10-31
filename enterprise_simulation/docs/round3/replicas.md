# Replica copies

`commands()` in `src/access/round3/replicas.py` returns 9 commands. Ids start with `cmd-r3e-`. Stream ids start with `r3e-`. Ref is `R3E-SYNC`. Each `occurred_at` is on 2027-01-18 or 2027-01-19 and ends in `Z`.

## Cursors

Both `ReplicaCursor` rows name source stream `r3e-sync` and file `cedar-r3e-2027-01-18`.

| Replica | seq_caught | Command | When |
| --- | --- | --- | --- |
| cedar-copy | 14 | `cmd-r3e-cursor-cedar` | 2027-01-18T22:10:00Z |
| cascade-copy | 10 | `cmd-r3e-cursor-cascade` | 2027-01-18T22:16:00Z |

## Exports

Both `ReplicaExport` rows use that same file id and amount 90.

| Replica | Currency | Command | When |
| --- | --- | --- | --- |
| cedar-copy | USD | `cmd-r3e-export-cedar` | 2027-01-19T14:40:00Z |
| cascade-copy | CAD | `cmd-r3e-export-cascade` | 2027-01-19T14:46:00Z |

## File, handset, and board

`cmd-r3e-slot-filed` is hospital `SlotFiled` on `r3e-sync`: site `cedar-ridge`, booking date 2027-01-18, `trailer_ok` true.

`cmd-r3e-handset-1` and `cmd-r3e-handset-2` share idempotency key `r3e-sms-1`. Attempts are 1 and 2. The second status is `redelivered`. The transcripts are "Northline visit filed at Cedar Ridge." and "Northline visit booked at Cedar Ridge."

`cmd-r3e-queue-depth` records visible backlog 120, oldest age 5400 seconds, and a live consumer. `cmd-r3e-desk-note` says the morning board was printed from cascade-copy.
