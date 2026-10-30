# E — From the laptop to AWS

The contracts move. The topology changes where a trust boundary or a durability requirement changes. Everything else stays a drawing.

## What stays the same

| Local fact | Cloud fact |
| --- | --- |
| Idempotency key on the tool | The same key. SQS will deliver again |
| Outbox row in the same commit as the business row | The same transaction on RDS. A queue publish can still happen twice. The consumer stores ids |
| Capability checked inside `book` | The same check. Step Functions pausing is not the authorization |
| Audience filter before score | The same filter in front of pgvector |
| Digest pinned, non-root, no secret in the image | The same image on Fargate. The execution role is not a long-lived key in the image |
| Case clock | Tests still pass the clock in. Production uses the service clock and records it |
| PHI denied to the external model | An IAM and a route policy, not a sentence in a prompt |

## What has to be redesigned

| Local shortcut | Why it breaks | Cloud shape |
| --- | --- | --- |
| SQLite file on one disk | A second task cannot share it safely | RDS in private subnets, or one task and an honest note that this is still one writer |
| Session row in process memory | A new task is a new process | The session table, cookie id not equal to the subject |
| In-memory slot lock | Two tasks, two memories | A version column. Update where version matches. FHIR `busy-tentative` remains the name of the hold |
| Fixture model | There is no fixture in the account | Public corpus, in-region model id, or no model call. The private model stays on the hospital side of the drawing |
| `print` logs | They become a log group | Allow-list fields. A data-protection filter. A canary must not appear |
| One folder called `zone-hospital` | An account is not a hospital | The simulator stays local. The account holds the Desk plane |
| Copying a budget number | The account has a real bill | Budgets alarm, plus the application’s token ledger |

## Educational sequence

The student does not rebuild the assistant in AWS from the first gate.

1. **Through module 6** the running system is local. Each gate ends with four lines: what would cross into an account, what must not, which local module is the contract, which AWS service is the candidate. Those lines are a decision record, not a deployment.
2. **Module 7** is the first apply-or-synthesize. The template contains the network, the task, the state machine with ids only, the queue, the bucket, the key, and the budget. The checker is local.
3. **Module 8** runs the game day against the local simulator even when the account exists. The account drill is the distinction: block a security group, show the breaker, show that a retry did not book twice.

A student who never opens an account can still finish. Their AWS evidence is the template, the policy findings, and the payload schema. A student who deploys shows a destroy, an alarm, and a bill that stayed inside the budget they set.

## The failure this progression is built to prevent

Two full implementations of every lesson. That doubles the course and teaches the cloud as a translation of the laptop. The FDE skill is the boundary: the same key, a different place the bytes are allowed to sit, and a written reason when the design does not move.
