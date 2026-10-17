# Refusals

Three requests stop before a care decision is invented.

| Request | Reason | What does not happen |
|---|---|---|
| What grade is this retina? | `diagnosis` | No grade is produced. The drop has no picture. |
| Refer this patient without a grader | `unsigned_referral` | No referral is written |
| The model calls the 14-day draft current policy | `draft_as_policy` | `status` stays `draft`. `refused` is true |

The first two are refused from the question itself. The model is not asked to improvise a grade.

The third happens after `retrieve`. If the passage status is `draft` and the model's sentence says the target is current policy, the loop replaces that sentence with a refusal. An answer that says the draft is not in force is not this refusal. That answer is allowed, and the status in `result` is still `draft`.

Next: [Three sites](05-three-sites.md).
