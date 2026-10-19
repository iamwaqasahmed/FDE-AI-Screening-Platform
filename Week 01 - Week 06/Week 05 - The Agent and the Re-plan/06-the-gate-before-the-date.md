# The gate before the date

**Days 2 and 3. Consultant and product manager.** Gate 2 is on the critical path. A day lost there is a day lost at go-live. The gate is a business case, not a meeting.

Read `corpus/standards/business-case-template.md`. Five cases. A case left blank fails the gate. This note is the commercial case and the management case. The economic case is the benefits register.

## The double count

`benefits_register.csv` prices two rows at the same hourly rate. One is grader hours the triage would release. The other is agency hours not booked because those grader hours cover them. The agency hours sit inside the grader hours. C-04 is this correction.

The overlap is the smaller of the two annual values. The claimed cashable total is the sum of every row whose type is cashable. The corrected cashable total subtracts the overlap once. Quote the corrected figure. Do not quote the claimed total as if the overlap were not there.

## The management case

The template's management case includes clinical safety. The RACI still has a blank accountable on the safety case and on the go or no-go. `management_case_owner_missing` is true. Do not invent the owner. Week 6 is that decision, and it is not open.

## The risks

One risk was closed with an empty mitigation, and the freeze it names is still running. `reopen` is that risk's id. The risk whose title is the procurement route taking longer than planned is the one that matches the binding constraint. `binding` is that id. `highest_open` is the open risk with the highest score, and the lowest id on a tie. `open_count` is how many are open.

## Fill these findings

| Item | What it holds |
|---|---|
| `gate_two` | `gate`, `date`, `approver`, `benefit_pair`, `overlap_gbp`, `claimed_cashable_gbp`, `corrected_cashable_gbp`, `management_case_owner_missing` |
| `risk_updates` | `reopen`, `binding`, `highest_open`, `open_count` |

`benefit_pair` is `B-04` and `B-08`. Amounts are whole pounds. `gate` is `G2`. `approver` is the name on the gate, not the role.

**A miss that looks like progress.** Quoting the claimed cashable total. It is in the file. It counts the same hours twice.

**Finish.** You can say what Gate 2 still needs, in pounds and in a name that is missing, and which risk should be open again.

Next: [The public line](07-the-public-line.md).
