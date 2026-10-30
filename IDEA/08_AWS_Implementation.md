# 8 — AWS implementation

Checked against AWS documentation opened 30 October 2026. Re-read the Regions table and the Bedrock model table before freezing any lab text. Those tables move.

## Facts the design obeys

- The Regions guide listed 34 Regions and no geography of Saudi Arabia. `me-south-1` is Bahrain. `me-central-1` is the United Arab Emirates. Both are opt-in and are other countries. `sa-east-1` is São Paulo. A migration blog dated 15 October 2026 still described a first Saudi Region as planned, not open. Location does not establish compliance. A new Region’s day-one list does not include Bedrock.
- A Bedrock endpoint in Bahrain or the UAE means the API exists there. Bahrain had no in-region model on the table that was opened. In the UAE, Nova Lite and Nova Pro were the in-region text models found. Other named models were global-only from those Regions. A global profile runs in a commercial Region the service chooses. Named geographies on that page did not include a Middle East profile. Abuse detection can retain some traffic in the destination Region.
- SQS standard queues are at-least-once. A consumer must tolerate duplicates. A visibility timeout and a dead-letter queue belong in the template.
- Step Functions can wait on a task token until success or failure is sent, from the same account, with a heartbeat so a lost reviewer does not wait forever. That token proves the workflow resumed. It does not prove a coordinator authorized a write.

## What the account is

One teaching account, stated as such. Production would split security, logs, and workloads. This exercise shows the seams.

The account holds the Desk’s coordination plane: public objects, identifiers, hashes, a queue, a state machine whose payload is ids, a task role, a key, filtered logs, and a budget alarm.

The account does not hold referral letters, national identifiers, quotations, wages, gold, or a model resource. Restricted bytes stay in `access` on the laptop, which stands in for the cluster’s private zone.

## Services and why

| Job | Service | Why this one | Why not the alternative |
| --- | --- | --- | --- |
| Public API | ECS on Fargate behind an ALB | Same image contract as the local bundle. No cluster to operate | Lambda’s short maximum wait is a poor home for a person. EKS adds a control plane the investigation does not need |
| Human wait | Step Functions `.waitForTaskToken` | The wait survives a process restart | The token is not the capability. The tool still checks `capability` |
| Events | SQS and a dead-letter queue | At-least-once is the lesson | FIFO does not remove the business key. A streaming cluster has no job here |
| Public files | S3, versioning, block public access, hash manifest | The nightly file and public leaflets | A public bucket |
| Transactional store, if the outbox leaves the laptop | RDS Postgres in private subnets | One transaction for the business row and the outbox | DynamoDB hides that transaction. A search cluster is a second system |
| Keys | KMS customer-managed key, Secrets Manager | The database password and tokens | Secrets in the task definition |
| Identity | IAM role for the task | The task is the principal | A user-pool product as a national identity provider |
| Network | VPC, private subnets, gateway endpoint for S3 | The data path is not a public IP | A public subnet for convenience |
| Signals | CloudWatch metrics and a log filter. Spans carry document id and tool hash | The incident is the served document | Prompt bodies. Attribute names from an unstable telemetry spec are not frozen into the checker |
| Cost | AWS Budgets in the template | An alarm before any optional apply | A copied currency total from a spreadsheet |
| Change | CloudFormation or CDK. A policy pack runs locally | `synth` plus rules catches a public bucket, a wildcard principal, a plaintext secret, a model resource, and a forbidden payload field | A local cloud emulator that requires a vendor token |

## What runs with no account

`cdk synth` and the policy pack. A unit test loads the state-machine definition and requires the callback pattern, a heartbeat, and a payload schema with no letter and no national id. The student’s binding for INV-08 includes endpoint region, processor region, and class.

## Optional live apply

The student’s own account. Create the budget alarm before the first apply. Destroy at the end. The course does not store credentials. This apply is not required to open INV-09.

## Model calls

None on this path. Public text is an object. If a future Regions table shows a Saudi geography and an in-region model, a later author may reopen a public-only call. Until that row exists, a model resource fails the template. An in-region processor that matches the endpoint still does not admit restricted bytes, and a Gulf region is not the Kingdom.
