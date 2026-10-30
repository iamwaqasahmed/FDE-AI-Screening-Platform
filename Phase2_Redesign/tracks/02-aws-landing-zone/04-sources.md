# Sources opened

Research date: 30 October 2026. Quotes and table readings in the other notes come from these pages on that date. Model and Region tables change. Open them again before a design that depends on a specific model being in-region.

These notes contain no prices. Pages that mention billing point at a pricing page or say that a charge exists. The 15 October 2026 blog says to label any reference Region used while Saudi Region prices are unpublished.

## Regions

- https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html — 34 Regions; `me-south-1` geography Bahrain; `me-central-1` geography United Arab Emirates; both opt-in; no Saudi geography; `sa-east-1` is São Paulo.
- https://docs.aws.amazon.com/global-infrastructure/latest/regions/doc-history.html — Bahrain launched 30 July 2019; UAE launched 29 August 2022; newest row on the page is New Zealand, 2 September 2025; no Saudi launch.
- https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ — 39 Geographic Regions claimed; announced plans for more Regions in the Kingdom of Saudi Arabia and Chile; core services at Region launch listed; Amazon Bedrock is not in that core list. GovCloud appears in the North America list, which the 34-Region account table does not include.
- https://aws.amazon.com/blogs/migration-and-modernization/how-to-plan-your-migration-to-the-aws-region-in-saudi-arabia/ — 15 October 2026. First Saudi Region on track for December 2026. "Before the Region opens." Location alone does not establish compliance. Shared responsibility includes where data, backups, and replicas are stored.

## Bedrock

- https://docs.aws.amazon.com/bedrock/latest/userguide/endpoints-region-availability.html — `bedrock-runtime` listed for `me-central-1` and `me-south-1`. An endpoint is not an in-region model.
- https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html — HTML opened and parsed. In-region, geo, and global definitions. Nova Lite and Nova Pro in-region in `me-central-1` only. Claude Sonnet 5.5 and GPT-5.6 Sol global-only in both Gulf Regions. No in-region model found for `me-south-1`.
- https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html — call `GetInferenceProfile` and read destination Regions; do not trust the prefix alone. Geographies named on the model page: US, Canada, EU, Asia Pacific, Japan, Australia, India.
- https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html — global versus geographic routing; destination may be a Region the account has not enabled; `inferenceRegion` in CloudTrail; encryption on the AWS network.
- https://docs.aws.amazon.com/bedrock/latest/userguide/geographic-cross-region-inference.html — prompts and outputs may leave the source Region and stay in the geography; abuse-detection copies stored in the destination Region.
- https://docs.aws.amazon.com/bedrock/latest/userguide/abuse-detection.html — zero operator access, with listed exceptions. Up to 30 days for specified OpenAI traffic and for all Claude Fable 5 and Fable 5.1 traffic. Cross-Region retention follows the destination Region.
- https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html — per-Region modes, including `none` and `default`. A setting in one Region does not apply to the destination of a cross-Region call.
- https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html — shared responsibility, CloudTrail recommendation, warning on free-form fields, model deployment accounts. Model providers do not get customer prompts from those accounts.
- https://aws.amazon.com/bedrock/faqs/ — content is not used to improve base models and is not shared with model providers; inputs and outputs are not used to train Nova, Titan, or third-party models; FAQ sentence on storage in the Region where you use Bedrock; customized models remain where the API call is processed; PrivateLink is a private network path; HIPAA eligibility and GDPR wording. Read this FAQ next to the cross-Region user guide, not instead of it.

## Services used in the design

- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html — Fargate runs the container; `FARGATE` compatibility; load balancer target type `ip`.
- https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html and https://docs.aws.amazon.com/lambda/latest/dg/configuration-timeout.html — function timeout 900 seconds.
- https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html — `.waitForTaskToken`, one-year execution quota, `HeartbeatSeconds` example of 600, SQS example that this design does not copy.
- https://docs.aws.amazon.com/AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-extensions.html — `pgvector` on RDS for PostgreSQL.
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.VectorDB.html — Aurora can run `pgvector` as a Bedrock knowledge base. That integration is rejected here.
- https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html — EventBridge routes events to targets.
- https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html — MSK is a managed Apache Kafka cluster. Rejected for this flow.
- https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html — Cognito is a user directory and token service, not the national identity provider.
- https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html — interface endpoints and private DNS. The page says interface endpoints are billed per hour per Availability Zone and per GB, and it links to the pricing page. No figure is copied here.
- https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html — cost budgets and the lag before a notification.
- https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html — Cost and Usage Reports to an S3 bucket; first report can take up to 24 hours; intra-month files are estimates.
- https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/benefits-of-using-multiple-aws-accounts.html — why one account is not the production pattern.

## Scanners and the emulator we do not center

- https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/security-formatting-best-practices.html — cdk-nag and Checkov named as development checks.
- https://docs.aws.amazon.com/cdk/v2/guide/policy-validation-synthesis.html — synthesis-time validation does not cover later console or API changes.
- https://java.testcontainers.org/modules/localstack/ — not an AWS page. Starting 23 March 2026, `localstack/localstack` requires `LOCALSTACK_AUTH_TOKEN` or the container fails to start.
