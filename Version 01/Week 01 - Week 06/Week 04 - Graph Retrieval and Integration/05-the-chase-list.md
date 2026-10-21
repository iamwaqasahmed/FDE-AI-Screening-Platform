# The chase list

**Day 2. Be the data scientist, then the data engineer.** The drop's brief says who was chased. Read it. The programme asked for a chase letter for every local id whose latest referral message has no seen date.

That is Week 2's second step, not its fourth. A blank seen date is not proof the visit never happened. Week 2 already said so. The chase list is wider than the overdue cohort, and some of the letters went to people who should not have been chased.

## Apply the steps you already trust

Start from `handover/ophthalmology/messages.pipe`. Keep the latest referral for each local id. Keep those whose seen date is blank. That set is the chase list. Check it against the `referral-chase` rows in the request file. They are the same local ids.

Then do what Week 2 did next.

1. Read `handover/epr_letters/`. A seen date in the sentence, for that hospital number, fills a blank. Those people were already seen. The chase letter was a mistake.
2. Drop local ids whose version 3 flag is `DECEASED` or `MOVED`. The version 3 file is `drops/week-2/registry/current_v3.csv`.

What remains is the Week 2 upper bound. It has to match the bound you published in Week 2. If it does not, one of the two readings is wrong. Fix the reading. Do not average them.

Use [templates/cohort-notes.md](templates/cohort-notes.md). Write the count at each step.

## Contact status

Inside the bound, join to `reconciliation.csv`. A local id was reached once, reached twice, or not reached. Count those three. The letters that were printed twice are a harm of their own. The letters that were not printed are C-07, and the next note counts them in people.

## Fill these findings

| Item | What it holds |
|---|---|
| `contact_status` | `chased`, `seen`, `deceased`, `moved`, `bound`, `once`, `twice`, and `lost` |

`seen`, `deceased`, and `moved` are counted on the chase list, with seen taken out before the flags. `once`, `twice`, and `lost` are counted inside the bound. `bound` is the Week 2 upper bound.

**A miss that looks like progress.** Calling every chase letter a letter to an overdue person. The programme chased the blank seen date. Week 2 spent a day showing that blank is not the same as unseen.

**Finish.** The bound matches Week 2. You can say how many people inside it were printed twice, and how many were not printed.

Next: [Who was not reached](06-who-was-not-reached.md).
