# Who was not reached

**Days 2 and 3. Be the data scientist, then the ML specialist.** You published the reconciliation as the software engineer. Here you use it, and you publish the people.

## C-07

Lost chase requests inside the bound, not every lost request. An invitation that was lost is a different letter. A chase letter to someone already seen, or flagged deceased or moved, is a letter that should not have been sent. It is not someone the clinic still needs to reach.

Count the local ids. Then count the people, through the Week 2 clusters, on the rows whose kind is `registry`. Two local ids in one cluster are one person. The letters are still a sample of the visits, and the clinic letters are still a sample, so the count remains an upper bound. Set `is_upper_bound` to true.

## The pilot scope

C-03's set is the Week 2 bound intersected with the captures the Week 3 memo still allows. Intersect that set with the lost chase local ids. What remains is the pilot-scope people who were not reached. It is still an upper bound.

## The clock

The referral message has a hospital number, or it does not. A blank hospital number is not a hospital clinic. Where the number is present, `handover/pacs/` says which hospital it belongs to. One number belongs to one hospital.

The specialist clock is the clause in force at that hospital on the referral date. Week 2's `pathway_rules.csv` is the regression. A hospital with no local rule is on the national text, and the national text sets no specialist clock. Do not invent one.

For the lost local ids inside the bound that do have a local clock, the days over are the days from the referral date to 26 October 2026, minus the limit. Record how many have a clock, which documents those clocks are, and the median days over.

## Fill these findings

| Item | What it holds |
|---|---|
| `chase_lost_people` | `local_ids`, `people`, and `is_upper_bound` true |
| `pilot_scope_lost` | `local_ids`, and `is_upper_bound` true |
| `clock_breaches` | `with_clock`, `clause_ids`, and `median_days_over` |

`clause_ids` are document ids. A median within a day of a careful count is enough.

**A miss that looks like progress.** Quoting the lost chase requests as a number of people. The requests are rows. C-07 asked for people, and it asked for the ones still in the bound.

**Finish.** C-07 can point at a number of people, labelled as an upper bound. You can name the clinics whose own clock applies, and the ones where it does not.

Next: [The contract and the agreement](07-the-contract-and-the-agreement.md).
