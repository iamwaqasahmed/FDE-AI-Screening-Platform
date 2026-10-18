# Operating points and drift

**Day 4. ML specialist.** The model card in `corpus/ai-governance/ai-model-card-requirements.md` asks for sensitivity and specificity by age band, performance by site, performance by camera and firmware, image quality limits, and a drift trigger. Fill [the evaluation sheet](templates/evaluation-sheet.md) in that order, on the restricted cohort, against adjudication. Specificity can sit in the sheet. The checker asks for the sensitivity.

## The points

Use a Wilson 95 percent interval, not a point on its own. The groups are: all adjudicated rows in scope, age `75+`, age under 75, the claim population, and each allowed site. The claim population is age under 75 and `quality_shown` of 6 or more. `quality_shown` is the 0 to 10 figure in the retrospective file. Record `sensitivity`, `low`, `high`, and `positives` for each. A group with few positives has a wide interval. Write the width down. It is the reason a small cell cannot carry a headline.

## The cameras

`handover/devices/camera_inventory.xlsx` is maintained by hand. The retrospective file has the firmware that was on the camera when the photograph was taken.

At the outreach site, find the first `capture_date` of firmware `3.1.0` and the mean vendor score before and after. The inventory column for that site still says something else. That lag is a finding. The scores move. Say whether they fall.

At the primary-care sites the later firmware does not carry that score shift. If the routine-grade sensitivity falls there while the mean score does not, the graders moved, not the camera. Name that site. Market Eye Clinic has a firmware upgrade in the inventory and no scored captures in the retrospective file. An upgrade that was never scored is a count of zero, not a missing analysis.

Write one drift trigger you would actually monitor: a drop in mean score, or a drop in sensitivity against adjudication, after a firmware change at a named site.

## Fill these findings

| Item | What it holds |
|---|---|
| `operating_points` | `all`, `age_75_plus`, `age_under_75`, `claim_population`, and `sites`. Each is `sensitivity`, `low`, `high`, `positives` |
| `firmware_drift` | The outreach site, `firmware`, `first_capture`, `score_before`, `score_after`, `scores_fall`, `inventory_firmware`, `inventory_lags`, `market_site`, `market_scored`, `label_drift_site`, the before and after sensitivity and score on that site, and `primary_scores_fall` |

**A miss that looks like progress.** One sensitivity for the whole file, because the model card's subgroup lines were still blank and the overall number looked enough.

**Finish.** The sheet is filled from the restricted cohort. Both findings match it. The drift trigger names a site and a measure.

Next: [Check the claims](12-check-the-claims.md).
