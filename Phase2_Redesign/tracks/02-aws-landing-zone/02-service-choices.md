# Service choices

Each service below has one job on the public side of the assistant. Regulated records do not enter these services. The residency reasons are in [01-region-and-residency.md](01-region-and-residency.md).

The teaching template pins a Region the account already has enabled and labels it as a teaching Region. Enabling Bahrain or the UAE does not create a Saudi Region.

## Compute

**Job.** Run the HTTP API that serves public content and records an approval of a public object.

**Choice.** Amazon ECS on AWS Fargate. Fargate runs the container without a cluster of EC2 instances. The task uses `requiresCompatibilities` of `FARGATE`, its own network interface, a task role, and an execution role. An Application Load Balancer in public subnets forwards to those tasks (`ip` target type, which the Fargate page requires for `awsvpc`). Amazon ECR holds the image.

**Reject Lambda as the API and as the wait.** The Lambda quotas page sets a function timeout of 900 seconds (15 minutes). Managed Instances can run longer for some asynchronous calls, up to 5,400 seconds. A person reviewing a public page does not fit in that window. The wait belongs in Step Functions.

**Reject Amazon EKS.** The workload is one service. EKS adds a Kubernetes control plane this lab does not operate. Fargate already runs the container.

## Workflow

**Job.** Pause while a person approves or rejects publication of one public object, then continue.

**Choice.** An AWS Step Functions callback (`.waitForTaskToken`). The service integration page describes this as the way to pause until `SendTaskSuccess` or `SendTaskFailure` returns the token. The execution input is the S3 key of a public object. The Fargate API stores the token next to that key in RDS and calls `SendTaskSuccess` with an allow or deny. The docs say a callback with no heartbeat can sit until the one-year execution quota. Set `HeartbeatSeconds`. The page's own example uses 600.

**Reject Amazon SQS as the workflow.** The same Step Functions page shows a pattern that puts the token on a queue. This lab's reviewer is the API, so the queue has no job. A queue is also the wrong system of record: the state machine already holds the wait, and a message body would be a second copy of the work item.

## Data

**Job.** Store rows for public objects: key, version, approval state, and a vector of public text.

**Choice.** Amazon RDS for PostgreSQL. The extension list opened with these notes includes `pgvector` (0.8.2 on the PostgreSQL 19 release-note rows). The API writes relational columns and the vector in one database. Embeddings are computed on the laptop from public text. The database receives the vector, not a Bedrock call.

**Reject Amazon Aurora.** Aurora PostgreSQL can also install `pgvector`. The Aurora page opened here is a Bedrock knowledge-base pattern. This design does not send text to Bedrock, and one lab catalog does not need an Aurora cluster.

**Reject Amazon DynamoDB.** The access pattern is a document row joined to its approval and its vector. DynamoDB is a key-value and document store. It is the wrong shape for this catalog.

## Search

**Job.** Nearest-neighbor lookup over vectors of public documents.

**Choice.** `pgvector` on the same RDS instance. One store, one backup boundary, no second cluster.

**Reject Amazon OpenSearch Service.** It would be another cluster with no query the Postgres catalog cannot serve at lab scale. A second cluster is also another place clinical text could be indexed later by mistake.

## Events

**Job.** When a new public object lands in the bucket, start the state machine.

**Choice.** Amazon EventBridge. It routes events from AWS services to targets. The rule matches object creation on the public bucket and targets the state machine. The event detail carries the object key.

**Reject Amazon MSK.** MSK runs Apache Kafka broker nodes in your subnets, at least one per Availability Zone you select. This flow is one bucket event to one execution. It has no consumer-group or replay job that would justify a Kafka cluster.

## Identity

**Job.** Let the Fargate task call S3, RDS credentials, Step Functions, and CloudWatch without long-lived keys.

**Choice.** IAM roles. The task role is what the container uses. The execution role pulls the image and reads the database secret. No access key is baked into the image.

**Reject Amazon Cognito as the national directory.** Cognito is a user directory and an OIDC token service for web and mobile apps, plus identity pools that exchange a token for AWS credentials. A user pool in AWS is a bad stand-in for the fictional national identity provider. National identifiers stay in the directory on the laptop. Do not map them into Cognito attributes. Workload identity for the public API remains the IAM task role.

## Network

**Job.** Let private tasks reach S3 and the AWS APIs they use without a public path for those calls.

**Choice.** A gateway VPC endpoint for S3. Interface VPC endpoints, which are AWS PrivateLink, for ECR, CloudWatch Logs, Secrets Manager, KMS, and STS, with private DNS so the SDK uses the normal Regional hostname. Tasks and RDS sit in private subnets. The load balancer is the public entry, and only for the public API.

The PrivateLink page says you are billed for each hour an interface endpoint is provisioned in each Availability Zone, and per GB processed. It points at the PrivateLink pricing page. These notes do not copy a figure. Create the interface endpoints only after reading that page. Until then, the template and the scanners are the lab.

**What PrivateLink does not do.** It does not move a Bedrock global profile into the source Region. This design does not create a Bedrock endpoint.

## Secrets and keys

**Job.** Encrypt the public bucket and the database, and keep the database password out of the task definition.

**Choice.** A KMS customer managed key for the bucket and for RDS storage. AWS Secrets Manager holds the RDS password. The task role can read that one secret.

**What they must not hold.** A national ID, a clinical note, or a prompt. Secrets Manager is a password store for the lab database, not an identity vault.

## Observability

**Job.** Show whether the public API is up, and trace a public request, without storing document text.

**Choice.** Amazon CloudWatch for request count, latency, and HTTP status. CloudWatch Logs for operational errors that name an object key and an error code. AWS X-Ray for the trace of the public request. The process emits OpenTelemetry spans. On a laptop those spans go to the console. In the teaching account they can be exported to X-Ray. Span attributes are route, status, and duration.

**What logs must not contain.** File bodies, prompts, national identifiers, or free-text clinical notes. The Bedrock data-protection page warns that free-form fields can show up in diagnostic logs. The same rule applies to this API's own logs.

## Cost

**Job.** Notice spend on the teaching account, and keep a line-item record.

**Choice.** One AWS Budgets cost budget with an email or Amazon SNS alert. The budgets page describes a monthly cost budget and says budget data can lag the charge. AWS Cost and Usage Reports delivers CSV line items to an S3 bucket you own. The CUR page says the first delivery can take up to 24 hours, updates at least daily are estimates until the invoice, and a report can be large enough to split across files.

Do not type a dollar target into this repository. The 15 October 2026 Saudi Region post says that where Regional prices are not published, any reference Region used for a model must be labeled as an assumption. Read the service pricing page on the day you set a budget.

A single account can create a budget and a CUR. An organization-wide report belongs in a management account. That is account design, covered in [03-what-students-can-run.md](03-what-students-can-run.md).
