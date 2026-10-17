# The status rule

Overlap decides which section inside the allowed documents is best. Status decides which documents are allowed.

Two cases:

- For every other question, search only documents whose manifest status is `in_force`. A draft can outscore them and still must not be returned.
- If the question asks whether the 14-day target is current policy, the draft is allowed. Return a passage from `sop-urgent-draft`. Copy `status` as `draft`. Do not relabel it `in_force`.

That second case is how the agent can say "there is a 14-day proposal, and it is not issued." Returning the draft with status `in_force` is the failure this module exists to prevent.

The issued procedure also says the draft is not current policy. Citing that file for the 14-day question is a reasonable sentence and the wrong document for this check. The checker expects the draft file, labeled as a draft.

Next: [Five questions](05-five-questions.md).
