# Cost and owners

**Day 4. Consultant and product manager.** The incident has a price, and it has owners. Neither is the number of dispatch rows.

## The price

`engagement/economics/unit_costs.csv` prices a letter and a reprint differently. A second copy costs a letter. A re-send costs a reprint. Holds cost nothing: you are not printing them.

Do not price every dispatch row. The first copy of a letter that was meant to be sent is the ordinary cost of the programme. The incident is the copies, and the reprints of the ones that never went.

Quote the duplicate cost, the re-send cost, and the total, in pounds. A pound either way is enough.

## Who decides

The catalogue and the component list both name the programme manager as the owner of letters. The data protection officer decides whether a chase file may sit with the bureau. The agreement does not. The bureau corrects its notice, and it keeps the evidence until the retention date you already computed. The records manager has no copy of the chase template in the handover. The clinical safety owner in `handover/owners.csv` is still blank. Do not invent any of these decisions, and do not invent the owner.

## Fill these findings

| Item | What it holds |
|---|---|
| `incident_cost` | `duplicates_gbp`, `resends_gbp`, and `total_gbp` |

**A miss that looks like progress.** Pricing the dispatch rows as letters sent. That number is the bureau's invoice for a normal week plus the copies. The incident is the copies.

**Finish.** The three amounts are filled from the unit costs and your own counts. You can name the person who owns the re-send, and the decision that is still the data protection officer's.

Next: [Write the incident note](14-write-the-incident-note.md).
