# Three asks

**Days 1 and 2. Product manager, architect, and consultant.** Take the three asks one at a time. A yes to the bundle is a yes to each of them.

## The date

Note 05 proves it. Do not quote the roadmap date as the answer. The roadmap is one of the documents the path checks.

## The site

The memo asks for a second site so the pilot covers a hospital clinic as well as primary care. Read the Week 3 memo again. It names the sites the vendor may still receive. A hospital clinic is not on that list.

Then read clause 1 of `dsa-retinalytics-2025` and `dpia-vendor-2024`. Week 3 used clause 3, the region. Clause 1 is the one that shares hospital studies. An agreement the Chief Digital Officer has already approved is not a lawful basis. The data protection officer decides. Do not invent the decision. `allowed` is false until that decision exists, and it does not.

## The variation

The value over the whole term decides the route. `procurement-thresholds` says so, and it says a requirement may not be split to stay under a ceiling. The roadmap item for the vendor contract carries the value. `vendor-contract-2024` states no scope and no value. It is not an agreement you can vary into a pilot.

No procurement starts before the funding gate that approves it. Whether a variation would be lawful anyway is the procurement lead's call, in writing. Do not make that call.

`assumed_holds` is whether the value is inside the direct-award ceiling. It is not whether the date works.

## Fill these findings

| Item | What it holds |
|---|---|
| `second_site` | `site`, `is_hospital`, `allowed`, `memo`, `agreement`, `dpia`, `decided_by`, `allowed_sites` |
| `procurement_route` | `value`, `route`, `direct_award_ceiling`, `lead_weeks_min`, `lead_weeks_max`, `gate`, `gate_date`, `assumed_route`, `assumed_holds` |

`memo` is the Week 3 document id. `decided_by` is the name on that memo, not a role title. `allowed_sites` is the list the memo names. `route` is the value from `procurement_routes.csv`, underscores included. `gate` is `G2`.

**A miss that looks like progress.** "Add the site later, once the date is fixed." The site is not a date. It is a decision the data protection officer has not made, and the files already contradict the agreement that would be used to justify it.

**Finish.** You can say, with a document for each, why the site is not yours to add and why the contract is not a direct award.

Next: [The backlog](04-the-backlog.md).
