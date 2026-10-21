# The week

**Day 1. You.**

Week 1 ended with a brief. Identity resolution and the letter fix came first. The vendor model did not. The registry extract you profiled is now the old one.

This morning the ministry moved the extract to schema version 3 and reissued a batch of registry numbers. "Today" is 12 October 2026. Your job is not to start the pilot. It is to make one cluster per real person, to count people the authority can defend, and to keep that count alive when the feed changes.

Nothing here is a real patient's record. Do not grade a photograph, and do not give clinical advice.

## The hats

You wear every hat below. Two contracts in `engagement/workstreams/contracts.csv` set the order of your work. C-01 and C-02 both say the data-engineer work publishes identity clusters, and both say to rerun after this drop. You need those clusters, for the ML-specialist work and the data-scientist work, by the end of Day 3.

| Hat | The hard question this week |
|---|---|
| Be the data engineer | One cluster per person. A shared name and date of birth is not enough, and neither is one cluster per hospital number |
| Be the data scientist | The pathway rule that applied at that site on that date, and the overdue cohort counted in people |
| Be the ML specialist | The vendor cohort keyed by person. A capture is not a person, and a random split leaks people |
| Be the software engineer | The APIs at week 2. Version 3 of the service is not version 3 of the file |
| Be the architect | Contracts that fail loudly, and a warehouse model that cites the clause it implements |
| Be the product manager | A release date the freeze allows. The last registry window was 6 October |
| Be the consultant | The data note. Every number quoted in Week 1 changes meaning, and two decisions have no owner |

Do not drop a question.

## Out of scope

Evaluating the vendor model. That is Week 3. Autonomous grading, and any referral a grader has not signed. The pilot stays stopped.

## Where the work lives

`work/week-02/`, or a folder outside the repo. The checker does not care which, as long as the files are the ones named in the [guide](README.md).

**Finish.** You can name the two contracts that need clusters by Day 3, and the two things this week will not do.

Next: [Open the drop](02-open-the-drop.md).
