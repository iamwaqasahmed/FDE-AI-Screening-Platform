# The governance pack

**Day 4. ML specialist, architect, and consultant.** Two systems, two tiers. Do not collapse them.

The Week 5 agent searches, summarises, and drafts, and a person reads every output. That is tier 2. `agent_tier` is 2.

The vendor triage pilot ranks a worklist. `ai-risk-tier-policy` makes that tier 3. Tier 3 needs eight things before a pilot. Read the policy and copy the list into `required`.

## The eight, as of today

| Status | Requirements |
|---|---|
| `missing` | Register entry, transparency record, model card, named clinical safety owner, human oversight plan, incident runbook entry. Nothing in the handover holds them. The memo does not fill the register, so the named owner is missing, not conditional. |
| `conflict` | DPIA signed by the data protection officer. `dsa-retinalytics-2025` does not match `dpia-vendor-2024`. |
| `evidenced` | Subgroup evaluation. Week 3 is that evidence, and it is the evidence that keeps the pilot stopped. |
| `conditional` | Empty. Do not park the owner here. |

## Stop. Write the two records.

`governance/transparency-record.yaml` from [the transparency template](templates/transparency-record.yaml). Draft it as it would have to read if it were published today.

- `owner` is the Chief Digital Officer, the owner on the vendor row. Not the clinical director. Her name does not belong in a record the register does not support.
- `supplier` is the vendor on the data sharing agreement.
- `tier` is 3. `data_classification` is `official-sensitive`.
- `hosting_region` names the EU region. It does not say the region is approved.
- `sites_in_scope` is the Week 3 list, exactly. The scored cohort in the governance gold still includes a site the memo removed. Do not copy that list.
- `start_date` holds no date.
- `human_in_the_loop` says a grader signs. `contact_for_challenge` is the screening programme.

`governance/model-card.yaml` from [the model-card template](templates/model-card.yaml). Fill it from the restricted Week 3 evaluation, not from the proposal.

- The operating point is the cut you used, and the sensitivity on the restricted, adjudicated cohort.
- Report sensitivity at age 75 and over, and under 75, separately.
- Name the sites that remain in that evaluation.
- The claimed sensitivity does not hold overall. Name the population it does hold on, in the proposal's words.
- Name the site where sensitivity moved after the firmware change, the before and the after, and that the camera inventory lags.
- Say the output is advisory.

These sentences fail the card on their own: "The model meets the claimed sensitivity of 0.95." "The model grades photographs." "The training data excludes hospital studies."

## Fill these findings

| Item | What it holds |
|---|---|
| `tier_three` | `system`, `tier`, `required`, `missing`, `conflict`, `conditional`, `evidenced`, `agent_tier` |
| `model_evidence` | `cut`, `sensitivity`, `age_75_plus`, `age_under_75`, `sites`, `claimed`, `claim_holds_overall`, `claim_population`, `drift_site`, `drift_before`, `drift_after`, `inventory_lags` |

`system` is `vendor triage pilot`. `tier` is `3`. Rates are the Week 3 figures. `claim_holds_overall` is false. `inventory_lags` is true when the inventory's firmware is behind the captures.

**A miss that looks like progress.** Quoting 0.95, or copying the sites off the scored file before the Week 3 cut. The claim is a subgroup. The sites are the memo's list.

**Finish.** The transparency record names no one the register does not name, and the model card can be checked against Week 3.

Next: [The hazard log](13-the-hazard-log.md).
