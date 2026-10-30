# I — References opened for this phase

Dates are the dates on the pages or the date this phase opened them, 30 October 2026. Phase 1 sources stay in the `Idea_*` folders. They are not copied here unless this phase relied on them again.

## AWS

- AWS Regions guide, 34 Regions, no Saudi geography, `me-south-1` Bahrain, `me-central-1` UAE, `sa-east-1` São Paulo: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- AWS migration blog, 15 October 2026, Saudi Region still planned: https://aws.amazon.com/blogs/migration-and-modernization/how-to-plan-your-migration-to-the-aws-region-in-saudi-arabia/
- Bedrock, in-region, geographic, and global inference: https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html
- Bedrock, geographic cross-region inference: https://docs.aws.amazon.com/bedrock/latest/userguide/geographic-cross-region-inference.html
- Bedrock abuse detection, retention in the destination Region: https://docs.aws.amazon.com/bedrock/latest/userguide/abuse-detection.html
- Step Functions, wait for a callback with a task token: https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html
- Step Functions, human-approval tutorial: https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-human-approval.html
- SQS, at-least-once delivery: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html
- EventBridge Pipes, SQS source, visibility timeout guidance: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-sqs.html

Confirm region codes on the day a lab is written. This phase did not freeze a code for a Kingdom region because the pages above did not publish one.

## Carried from Phase 1 because the design uses them

- GDS, discovery, including a stop: https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works
- OWASP Top 10 for LLM Applications 2025: https://genai.owasp.org/llm-top-10/
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI 600-1: https://doi.org/10.6028/NIST.AI.600-1
- PDPL English PDF (translation; Arabic governs): https://sdaia.gov.sa/en/SDAIA/about/Documents/PersonalDataProtectionLaw.pdf
- PDPL Implementing Regulation English PDF: https://sdaia.gov.sa/en/SDAIA/about/Documents/ImplementingRegulation.pdf
- SMART App Launch: https://hl7.org/fhir/smart-app-launch/app-launch.html
- FHIR Slot status: https://www.hl7.org/fhir/codesystem-slotstatus.html
- LoRA, arXiv:2106.09685: https://arxiv.org/abs/2106.09685
- QLoRA, arXiv:2305.14314: https://arxiv.org/abs/2305.14314
- Zheng et al., arXiv:2306.05685: https://arxiv.org/abs/2306.05685
- PagedAttention, arXiv:2309.06180. Quote the body, not only the abstract. The ShareGPT comparison is about 1.7–2.7× versus an Orca baseline that knows the output length. That is not this case’s capacity.
- MCP current revision checked in Phase 1: https://modelcontextprotocol.io/specification/2026-07-28
- OpenTelemetry GenAI spans, status Development: https://github.com/open-telemetry/semantic-conventions-genai
- Cormack, Clarke, and Büttcher, reciprocal rank fusion, SIGIR 2009: https://dl.acm.org/doi/10.1145/1571941.1572114
- Anthropic contextual retrieval, 19 September 2024, vendor figures: https://www.anthropic.com/engineering/contextual-retrieval

## Not used as proof

Palantir’s long blog posts returned 403 to a Phase 1 track. Search excerpts are not opened pages. A 2022 getting-started PDF was opened by the arrival-lesson track and may be cited for pre-pilot shape. It is not evidence of current product behavior.
