# Open the drop

**Day 1. Product manager and consultant.** This note is the release. `drops/week-6/` is open.

Read the memo, including the last paragraph. The sender agrees to be clinical safety owner. The acceptance is conditional. The owners register is a different file. Open `handover/owners.csv` and read the clinical safety owner row before you answer anyone.

`owner-governance` names a field. It does not name a person. The field is still blank, so the Week 5 veto still fires, and it still cites that document. What the drop makes false is any sentence that says no clinical safety owner exists. The Week 5 reply said the safety owner was unnamed. That sentence is now wrong. The register is still blank. Both of those can be true.

Nothing in this drop marks a condition done. Nothing in this drop tells patients or the press that the pilot has an owner.

## Stop. Write the impact log.

Use [the impact-log template](templates/impact-log.md) and save it as `impact-log.md`. One page.

- C-05 is delivered in full this week. C-06, C-07, and C-08 are consumed.
- C-01, C-02, C-03, and C-04 do not change. No contract row is rewritten.
- The owners register does not change. The stop does not lift.

The handoff is due the Friday of this week. The release date is on the drop's README. Friday is four days later.

## Fill these findings

| Item | What it holds |
|---|---|
| `drop_owner` | `owner`, `owner_role`, `named_on`, `conditions`, `register_owner`, `pilot_may_start`, `friday` |
| `outputs_changed` | `delivered`, `consumed`, `unchanged`, `changed` |

`conditions` is `CSO-1` through `CSO-5`. `register_owner` is the cell in `handover/owners.csv`, which is empty. `pilot_may_start` is false. `delivered` is `C-05`. `consumed` is `C-06`, `C-07`, and `C-08`. `unchanged` is `C-01` through `C-04`. `changed` is empty. Dates are `YYYY-MM-DD`.

**A miss that looks like progress.** "We have an owner, so the stop lifts." The memo says the opposite, and the register agrees with the memo's last paragraph, not with the first.

**Finish.** The impact log names what the memo changes and what the register does not. The two findings are filled from the drop, the owners file, and the contracts file.

Next: [Five conditions](03-five-conditions.md).
