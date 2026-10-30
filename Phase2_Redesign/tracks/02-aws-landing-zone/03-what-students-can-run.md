# What students can run

## Without a paid account

The checks that matter for this track run on the laptop against the template and the public API. They do not prove that a Region exists, and they do not prove residency.

**AWS CDK synthesis.** `cdk synth` emits the CloudFormation the app would deploy. That artifact is what the scanners read.

**cdk-nag.** AWS Prescriptive Guidance describes cdk-nag as an open-source tool that checks CDK constructs against rule packs during synthesis. Run it on the app. A finding is a failed lab, not a warning to suppress so the command exits zero. Suppress a rule only with a written reason that matches a control in [02-service-choices.md](02-service-choices.md), such as an interface endpoint you intentionally left out until pricing is read.

**Checkov.** The same Prescriptive Guidance page names Checkov as a static scan of CloudFormation, Terraform, and Kubernetes. Run it on the synthesized template.

**Limit of synth-time policy checks.** The CDK policy-validation page says synthesis checks do not see later console edits or API calls, and they do not survive someone changing the template after synthesis. A green local run is evidence about the template you just synthesized. AWS CloudFormation hooks or AWS Config would be the ongoing check, and those need an account.

**The public API on the laptop.** Run the container against a local PostgreSQL with `pgvector`, public fixture files, and OpenTelemetry spans printed locally. Approval of a fixture calls the same state-machine contract the Step Functions callback would call: a token, an object key, allow or deny. No AWS credentials are required for that path.

**LocalStack is not the core path.** The Testcontainers for Java LocalStack module, opened 30 October 2026, says that starting 23 March 2026 the `localstack/localstack` image requires `LOCALSTACK_AUTH_TOKEN` or the container fails to start. That page is a Testcontainers page, not an AWS page. An emulator with a token still does not implement the Regions table, Bedrock destination Regions, service control policies, or Cost and Usage Reports. Do not use a LocalStack run as evidence for any claim in [01-region-and-residency.md](01-region-and-residency.md).

## What a teaching account can demonstrate

The whitepaper *Organizing Your AWS Environment Using Multiple Accounts* says multiple accounts are how you separate environments, constrain sensitive data, and limit the scope of a bad event. It also says an account is the default cost boundary. One account fails that production bar on purpose.

A single teaching account can still show the public half:

- A Region parameter that is not described as Saudi Arabia. `me-south-1` and `me-central-1` stay disabled unless a later lab is explicitly about opt-in, and even then they are Bahrain and the UAE.
- A VPC with private subnets for tasks and RDS, public subnets only for the load balancer, an S3 gateway endpoint, and interface endpoints only after the PrivateLink pricing page has been read.
- An IAM task role and an execution role, and no long-lived access key in the image.
- An S3 bucket for public objects, block public access, and a KMS key. A bucket policy that refuses to be the clinical archive.
- RDS PostgreSQL for the public catalog, Secrets Manager for its password.
- The Step Functions state machine and the EventBridge route from the public bucket.
- A cost budget and, if you want the line items, a Cost and Usage Report delivered to a bucket in that same account.
- CloudWatch metrics and X-Ray traces of the public API.

Deploy is optional. The scanners are the required evidence.

## What one account cannot demonstrate

- Service control policies. Those attach to an organization, not to a lone account's good intentions.
- A separate log-archive account and a separate workload account. The whitepaper's blast-radius claim needs more than one account.
- An organization-wide Cost and Usage Report owned by a management account. A report in the teaching account covers that account.
- Residency in the Kingdom. No template can, until a Region whose geography is Saudi Arabia appears on the Regions table and the services you need are on the Regional Services List.
- A national identity provider. Cognito in this account would be a user pool you invented.

Write the production target as a short account list beside the lab: a management account, a security or log account, and a workload account, with the regulated system still outside AWS until an in-Kingdom Region is actually open and a compliance review says a given workload may move. The 15 October 2026 blog's own test is workload-by-workload, including where replicas and backups would live. The lab does not perform that move.
