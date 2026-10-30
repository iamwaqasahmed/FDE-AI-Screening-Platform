# Region and residency

Opened 30 October 2026. Re-open the linked pages before treating a model or a Region as current. The full URL list is in [04-sources.md](04-sources.md).

## What was opened

**AWS Regions user guide** (`docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html`). The page says an AWS account has 34 Regions. The table includes:

- `me-south-1`, Middle East (Bahrain), 3 Availability Zones, geography Bahrain, opt-in required.
- `me-central-1`, Middle East (UAE), 3 Availability Zones, geography United Arab Emirates, opt-in required.

Both are in the "disabled by default" list. Regions introduced after 20 March 2019 must be enabled before use. `sa-east-1` is South America (São Paulo), geography Brazil. The table has no Region whose geography is Saudi Arabia.

**Document history** for that same guide. The newest launch on the page is Asia Pacific (New Zealand), `ap-southeast-6`, 2 September 2025. Middle East (UAE) is recorded as launched 29 August 2022. Middle East (Bahrain) is recorded as launched 30 July 2019. There is no Saudi launch row.

**Global infrastructure page** (`aws.amazon.com/about-aws/global-infrastructure/regions_az/`). The page says the cloud spans 124 Availability Zones within 39 Geographic Regions, with announced plans for 7 more Availability Zones and 2 more AWS Regions in the Kingdom of Saudi Arabia, and Chile. Its North America list includes the two AWS GovCloud (US) Regions, which the 34-Region account table excludes. These notes do not invent a sum that forces 34 and 39 to match. Neither page lists a live Region code in Saudi Arabia.

**Migration blog, 15 October 2026** (`aws.amazon.com/blogs/migration-and-modernization/how-to-plan-your-migration-to-the-aws-region-in-saudi-arabia/`). Authors Yusuf Sheikh and Stefan Visscher. The post says the first Region in Saudi Arabia is on track to launch in December 2026, that teams can assess workloads before the Region opens, and that the Region was announced at LEAP 2026 in Riyadh. It also says location alone does not establish compliance. Under the shared responsibility model, AWS is responsible for security of the cloud, and the customer is responsible for security in the cloud, including where data is stored and where backups and replicas go. The same post says a new Region launches with a core set of services that grows later, and that the Regional Services List is the check. The infrastructure page's "included in all Region launches" list does not name Amazon Bedrock. Do not assume a December 2026 Region includes Bedrock on day one.

## Bedrock: endpoint, model, and route are three different facts

**Endpoints page.** `bedrock-runtime` is described as available in every Region where Bedrock is offered. The Middle East table on that page lists `me-central-1` and `me-south-1`. An endpoint in a Region means you can call the API there. It does not mean the model executes there.

**Model table** (`models-region-compatibility.html`), HTML opened 30 October 2026, icons read as `supported` or `not-supported` rather than the stripped markdown view.

In-Region means the page's own definition: the request is processed entirely in the Region you specify.

Parsed result:

- `me-central-1`: Amazon Nova Lite is in-region only. Amazon Nova Pro is in-region and also marked Geo. Global is not supported for Nova Pro in that row.
- `me-central-1`: Nova 2 Lite, Claude Sonnet 5.5, Claude Haiku 5.5, Claude Opus 5.5, Claude Fable 5, Claude Fable 5.1, and GPT-5.6 Sol, Terra, and Luna are global cross-Region only. In-Region is not supported for those rows.
- `me-south-1`: no parsed model row had In-Region supported. Claude Sonnet 5.5 and GPT-5.6 Sol are examples that are global only from Bahrain. Those models are not in Bahrain.

There is no Saudi row, because there is no Saudi Region code on the Regions table.

**Geographic profiles** are defined for US, Canada, EU, Asia Pacific, Japan, Australia, and India. The opened pages do not define a Middle East geography. Nova Pro's Geo mark in the UAE is not a Gulf boundary. The inference-profiles page says to call `GetInferenceProfile` from each source Region and to read the destination Regions in the response. It says not to trust the geography prefix alone.

**Global profiles** route to a supported commercial Region worldwide. The cross-Region page says this can include Regions the account has not enabled. CloudTrail in the source Region records `additionalEventData.inferenceRegion` as the place that processed the call. Traffic stays on the AWS network and is encrypted. That is a network statement, not a residency statement.

## What "data stays in the Region" covers

Use it only for an in-region model id, with no geography prefix and no `global.` prefix, in the Region you actually called. On 30 October 2026 the only such text models found in the Gulf were Nova Lite and Nova Pro, and only in `me-central-1`. That Region's geography is the United Arab Emirates.

The Bedrock FAQ says customer content is not used to improve the base models and is not shared with model providers. A later FAQ answer says AWS and third-party providers will not use Bedrock inputs or outputs to train Amazon Nova, Amazon Titan, or third-party models. The same FAQ says content processed by Bedrock is encrypted and stored at rest in the Region where you are using Bedrock. Customized models remain in the Region where the API call is processed.

## What that phrase does not cover

The cross-Region user guide is the page that describes inference profiles. For a geographic profile, prompts and outputs may move outside the source Region and stay inside that geography. Abuse-detection copies, when stored, are stored in the destination Region. A global profile has no geographic restriction.

The abuse-detection page says Bedrock uses a zero-operator-access model except for the cases it lists. Those cases include retention of up to 30 days for classifier-flagged traffic on listed OpenAI models, and retention of up to 30 days of all traffic for Claude Fable 5 and Claude Fable 5.1, with possible human review by AWS. If cross-Region inference is enabled, those retained copies are stored in the destination Region. The data-retention page adds per-Region modes. `none` is the mode that page describes as zero data retention. `default` follows the model policy and may still retain data for safety. A retention setting in the source Region does not pull a global call back into that Region.

PrivateLink, which the FAQ offers for a private path from a VPC to Bedrock, keeps that path off the public internet. It does not change the destination Region of a global profile.

HIPAA eligibility and GDPR wording on the FAQ are not a finding that data is in Saudi Arabia. The 15 October 2026 blog says an in-country Region is something a regulated customer can evaluate, and that location alone does not establish compliance.

## The split

**Stays off AWS.** PHI, national identifiers, and clinical text. The fictional national directory. Any prompt, embedding request, log line, trace attribute, queue body, or fine-tuning set that contains them. The place they run is the laptop, on a Docker network or other local network the diagram may call a private VPC. That network is not created in an AWS account.

**May run on AWS.** Public pages and public files after a check that they contain none of the records above. The catalog of those files. Vectors computed on the laptop from public text and stored as numbers. Counts, latency, and status codes with identifiers removed. The CDK application and the CI scans of it.

**Must not be used for the regulated records**, even though some of these services are the right tools for the public half:

- Amazon Bedrock in every current Region, including in-region Nova in the UAE and every global profile from Bahrain or the UAE.
- Amazon Cognito as a directory of national identifiers.
- S3, RDS, Aurora, DynamoDB, OpenSearch, MSK, SQS, EventBridge payloads, CloudWatch Logs, X-Ray attributes, and Secrets Manager, whenever the payload would be PHI, a national ID, or clinical text.

De-identified metrics are produced on the laptop. Only the aggregate is sent to CloudWatch.
