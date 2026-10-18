# Debrief — vendor evidence

The restricted cohort is 8,348 captures, 40 rejected, 423 adjudicated. The routine label is missing on 0.40 of the captures.

**The gap.** At the 0.50 cut, sensitivity against the routine grade is 0.763. Against adjudication it is 0.875, Wilson 0.801 to 0.924, on 112 positives. The gap is 0.112. The routine grade is the noisy reference. Latent disease, which is not in the drop, sits at 0.892 on this cohort. Adjudication is the closer of the two labels you can actually see.

**Graders, against adjudication, inside the restricted sample.** HL over-calls most, 0.206 of 34 rows. TB is next, 0.179 of 56. AX misses most, 0.286 of 21, and does not over-call. ES does not disagree with the lead grader in this sample.

**Operating points against adjudication.**

| Group | Sensitivity | Low | High | Positives |
|---|---|---|---|---|
| All | 0.875 | 0.801 | 0.924 | 112 |
| 75+ | 0.556 | 0.373 | 0.724 | 27 |
| Under 75 | 0.976 | 0.918 | 0.994 | 85 |
| Claim population | 0.974 | 0.911 | 0.993 | 78 |
| Hill Counties Health Centre | 0.882 | 0.766 | 0.945 | 51 |
| Oakridge Primary Care | 0.869 | 0.762 | 0.932 | 61 |

The claim population is under 75 and `quality_shown` of 6 or more. 0.95 sits inside that interval and outside the interval for the whole sample. The 75+ interval runs from 0.373 to 0.724. It cannot carry a headline.

**Firmware.** River Outreach firmware 3.1.0 first appears on 2025-02-03. Mean score 0.246 before, 0.195 after. The inventory still says 2.1.0. Those captures are outside the memo, so a cohort that obeys the memo never sees this shift. It is still the drift trigger: a firmware change that moves the score.

Oakridge Primary Care moves the other way. Routine sensitivity falls from 0.850 to 0.766 after firmware 2.2.1, while the mean score rises from 0.264 to 0.297. The camera did not get worse. The graders did. Primary-care scores do not fall. Market Eye Clinic is on firmware 4.2.0 in the inventory and has no scored captures.

**The proposals.** Retinalytics claims 0.95. It does not hold on the adjudicated cohort. It holds on the population named in the PDF table, not in the Markdown. ClearSight's 2021 deployment was stopped; the minutes are `board-minutes-2021-06` and the post-mortem `postmortem-ai-pilot-2021` blames accuracy. OptiVue's instruction is `proposal-optivue-2026`.

Hospital studies are `proposal-retinalytics-2026`, and the memo blocks them. "Needs no local evaluation" is `proposal-clearsight-2026`, and the tier 3 rule requires a subgroup evaluation. The instruction is OptiVue.

Back to the [debrief](../16-debrief.md).
