# D — AWS architecture

The account is the National Desk’s coordination plane and the student’s delivery tooling. It is not the hospital record and it is not a place to send a referral letter to a model.

## Facts that bind the design

Opened 30 October 2026.

- On 30 October 2026 the AWS Regions guide listed 34 Regions and no geography of Saudi Arabia. `me-south-1` is Bahrain. `me-central-1` is the United Arab Emirates. Both are opt-in and are other countries. `sa-east-1` is São Paulo. A blog dated 15 October 2026 says the first Saudi Region is on track for December 2026 and that teams should plan before it opens. Location alone does not establish compliance. A new Region’s day-one service list does not include Bedrock. Labs must not invent a code and must not treat `sa-*` as the Kingdom.
- The Bedrock model table opened the same day: Bahrain had no in-region model. In the UAE, Nova Lite and Nova Pro were the in-region text models found. Other named models, including Claude and GPT rows, were global-only from those Regions. A global profile runs in a commercial Region Bedrock chooses. Named geographies do not include a Middle East profile. Abuse detection can keep some traffic, including all traffic for named Claude Fable models, for up to 30 days in the destination Region. An endpoint in Bahrain or the UAE means the API exists there. It does not mean the model executes there. Bedrock is off this course’s path until a Saudi Region is on the Regions table and an in-region model id is on that Region’s model table. Public leaflets are files.
- Step Functions can pause on `.waitForTaskToken` until `SendTaskSuccess` or `SendTaskFailure`. The token has to come back from the same account. A waiting task is bounded by the one-year execution quota. Heartbeats exist so a lost reviewer does not wait forever. This is the cloud picture of a coordinator approval. It is not a license to put the referral body in the state payload.
- SQS standard queues are at-least-once. EventBridge Pipes delete a batch after success and make the batch visible again after the visibility timeout on failure. The consumer has to be idempotent. The docs say to set the visibility timeout to at least six times the pipe’s enrichment plus target time, and to use a dead-letter queue.

## The landing zone a student is allowed to design

One account for the exercise. Say so. Production would split security, logs, and workloads. The exercise demonstrates the seams, not a full organization.

| Piece | Service | Job | Rejected |
| --- | --- | --- | --- |
| Network | VPC, private subnets, no public IP on the data path | The coordination tasks do not sit on the internet | A public subnet “for simplicity” |
| Edge | ALB in front of the Desk API | Health checks, TLS | API Gateway plus Lambda as the default for a multi-step tool loop. Lambda fits a short callback. It is a poor home for a workflow that waits on a person |
| Compute | ECS on Fargate for the Desk service | Same container contract as the local promotion bundle | EKS. The cohort does not need to operate a cluster to learn the boundary |
| Workflow | Step Functions, task token, payload is ids only | The wait survives a process restart | Putting the letter or the national id in the execution input |
| Queue | SQS plus a dead-letter queue | At-least-once events from the Desk | Assuming FIFO removes the need for an idempotency key. FIFO helps order inside a group. The tool can still see a duplicate |
| Files | S3 for the nightly file and public documents | Versioning, a manifest with a hash | A bucket policy that allows `*` |
| Database | RDS Postgres in private subnets, or Aurora if the lab needs a reader | The outbox and the session table when the student leaves SQLite | DynamoDB as the workflow store. The lesson is a transaction between the business row and the outbox. A single-table design hides that |
| Search | pgvector on that Postgres, for the public corpus only | The same filter-before-score rule | OpenSearch as a requirement. It is a reasonable later choice. It is a second system |
| Keys | KMS customer-managed key, Secrets Manager | Tokens and the database password | Secrets in the task definition |
| Identity | IAM roles for tasks. Cognito only as a stand-in the DPIA must name | The Desk’s own users in the exercise | Cognito as the national identity provider. It is not |
| Model | None. Public text is an object in the bucket. The private model stays in the simulator | A model call whose destination the student cannot name | Bedrock from Bahrain or the UAE, including Nova in `me-central-1`, because that Region is not in the Kingdom |
| Logs | CloudWatch with a data-protection policy or an equivalent filter, X-Ray or OTel spans that carry ids not bodies | The incident timeline | Logging the prompt |
| Cost | AWS Budgets on the account, a token ledger the application emits | The surge lesson’s money | A blended SAR figure copied from a spreadsheet |
| Change | CloudFormation or CDK. `cdk-nag` or a comparable rule set runs in CI | The promotion gate without an account | LocalStack as the thing the student must log into. The image’s auth-token requirement makes it a bad core dependency |
| Drill | A documented fault: scale the service to zero, or block the partner’s security group | The hypothesis | AWS Fault Injection Service as a required live experiment. It is an extension |

## Payload rule

The state machine, the queue, the bucket, and the logs carry identifiers and hashes. The hospital record stays in the simulator on the student’s machine, which stands in for the cluster’s private zone. A VPC endpoint design is drawn so that, in a real landing, the Desk would call the cluster over a private path. The exercise does not require the student to peer a real hospital network.

If a template contains a national-id pattern, a letter body, or a model request whose input is the letter, the policy check fails.

## What the student runs without an account

- The template synthesizes.
- `cdk-nag` (or the chosen pack) reports the public bucket, the wildcard principal, the missing encryption, and the log group with no retention.
- A unit test asserts the state-machine definition uses a task token and that the payload schema has no `letter` or `national_id` field.
- A cost note uses the pack’s prices, not a live bill.

A live `deploy` is a distinction. It uses the student’s own account, a budget alarm set before the first apply, and a destroy step. The course does not hold the credentials.

## Region choice, written so it can go stale

The lab tells the student to read the Regions table and to record the code they used. Until a Saudi geography appears on that table, the teaching stack is synthesized for a Region parameter the student names as “not the Kingdom,” and the DPIA says the account is a coordination plane outside the hospital. Bedrock stays out. A December 2026 announcement is not a row on the Regions table and not a model list.
