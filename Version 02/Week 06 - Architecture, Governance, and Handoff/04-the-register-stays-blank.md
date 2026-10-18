# The register stays blank

**Day 2. Product manager.** The memo says nothing in the register changes until every condition is confirmed. Draft the changes. Do not apply them.

## What stays open

`handover/owners.csv`. The clinical safety owner cell stays empty. Write that empty value into the finding. Do not write the memo's sender into it.

Two rows in `raci.csv` have a blank accountable: the clinical safety case, and the pilot go or no-go. They stay blank. The responsible names on those rows are not the owner.

R-02, no named clinical safety owner, stays open. I-10, clinical safety owner not appointed, stays open. A name in a memo is not a closed risk. `keep_open` is those two ids.

## What should be open again

R-11 was closed. The mitigation says joiner, mover, and leaver checks monthly. `security-authentication-standard` says access is removed within one working day. Note 07 shows the accounts that still have access. `reopen` is R-11. You record that. You do not edit the register.

R-08 stays closed. Its mitigation names a control, and note 07 will show that the booking log went quiet after the incident window. Do not reopen it because the incident once existed.

## The roadmap and the gate

RM-09, the clinical safety case, has a blank owner. Leave it blank in the finding.

G3 is the pilot readiness gate. Read its date, its approver, and its condition. The condition needs a safety case signed by the named owner. `passes` is false. The date is also before testing can finish on the Week 5 earliest path. Either reason is enough. Record the date and the approver from the file.

## Fill these findings

| Item | What it holds |
|---|---|
| `register_state` | `owners_register`, `raci_blank`, `keep_open`, `reopen`, `rm09_owner`, `g3` |

`owners_register` is empty. `raci_blank` is the two activity names. `keep_open` is `I-10` and `R-02`. `reopen` is `R-11`. `rm09_owner` is empty. `g3` holds `date`, `approver`, and `passes`.

**A miss that looks like progress.** Closing R-02 because a name now exists. The risk is that no one is named in the register. The register is what the rule reads.

**Finish.** You can list the drafts, the person who would approve each one, and the files you did not change.

Next: [The estate as it runs](05-the-estate-as-it-runs.md).
