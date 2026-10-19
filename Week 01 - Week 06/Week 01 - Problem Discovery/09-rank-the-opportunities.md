# Rank the opportunities

**Day 5.** Eight opportunities are in the drop. The workshop, the board paper, and the surveys each propose an order. Those orders are not a value model.

Use these keys, in `ranking.order`. Every key once.

| Key | The opportunity |
|---|---|
| `identity_resolution` | One record per person across the keys |
| `letter_bureau_fix` | Reconcile dispatches and reissue lost letters |
| `reminder_targeting` | Send reminders where they change attendance |
| `dna_prediction` | Predict who will not attend |
| `fast_track_scheduling` | Schedule the fast-track clinic slots |
| `call_deflection` | Self-service answers for contact-centre calls |
| `grader_triage_ai` | Use the vendor score to order the primary-care queue |
| `vendor_model_expansion` | Let the vendor model grade at every site |

## Rules the order has to satisfy

You cannot compute the hidden net values from this drop. You can still refuse a bad order.

- Nothing with a blocker goes first. `vendor_model_expansion` is blocked by the missing clinical safety owner and by the data-protection limit on hospital studies. `grader_triage_ai` is blocked by the missing owner. `fast_track_scheduling` is blocked while the consultant vacancy has cut the slots.
- A dependent opportunity comes after what it needs. Identity resolution comes before did-not-attend prediction, reminder targeting, grader triage, and vendor expansion. The letter fix comes before call deflection and reminder targeting.
- The opportunity with the highest defensible net value is first. The vendor expansion is last. The largest claim in the board paper is not the highest net value.

## Two traps

`workshop` records the dot-vote winner: `top_idea`, the `top_opportunity` it maps to, and `is_highest_net`. The votes are in `engagement/workshop/dot_votes.csv`. The idea text is in that file. The winner is not the highest net value.

`voiced_vs_costly` records `most_voiced` from the two surveys (staff `top_problem` plus patient `theme`) and `same`. The loudest complaint is not the costliest problem. Set `same` to false, and do not spend the brief arguing that the loudest theme is the one to fund first.

**Finish.** The order respects the blockers and the prerequisites, and the workshop winner is labelled as a vote rather than a value.

Next: [Write the brief](10-write-the-brief.md).
