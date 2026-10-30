# AWS landing zone for a fictional Saudi operational assistant

Research date: 30 October 2026. This is a teaching architecture for a fictional government assistant. It is not a compliance opinion and not a statement that any AWS service meets a Saudi regulatory test.

## The honest architecture

On 30 October 2026 there is no AWS Region whose geography is Saudi Arabia. Bahrain (`me-south-1`) and the UAE (`me-central-1`) are real, opt-in Regions in other countries. An AWS blog dated 15 October 2026 says the first Region in Saudi Arabia is on track to launch in December 2026, and it says to plan before that Region opens. The Regions user guide that same week still lists 34 Regions and no Saudi Region code. Details and the pages opened are in [01-region-and-residency.md](01-region-and-residency.md).

Regulated records for this assistant — protected health information, a national identifier, and clinical text — stay on the student laptop, inside a simulated private network that is not an AWS VPC. AWS receives public content, infrastructure-as-code, continuous-integration output, a file drop that has already been checked to contain no regulated text, and operations metrics that have had identifiers removed.

Amazon Bedrock is not on the path. A Bedrock endpoint in Bahrain or the UAE does not mean a model runs there. On the model table opened 30 October 2026, Bahrain had no in-region model. The UAE had in-region support for Amazon Nova Lite and Amazon Nova Pro only. Other models listed for those Regions, including Claude Sonnet 5.5 and GPT-5.6 Sol, were global cross-Region only. Global routing processes the prompt in a commercial Region Bedrock selects. That is the wrong place for clinical text, and the UAE is still the wrong country for a Kingdom residency claim.

## What runs where

| Place | What it holds |
| --- | --- |
| Laptop, simulated private network | PHI, national ID, clinical text, the fictional national directory, any model call that would see that text |
| AWS teaching account | Public API, public objects, catalog of those objects, de-identified metrics, IaC, CI scans, a budget |

A private subnet in Bahrain or the UAE is still those countries. Privacy of the subnet is not a national boundary.

Service-by-service choices, including the rejected alternative and why, are in [02-service-choices.md](02-service-choices.md). What a student can prove with no paid account, and what a single teaching account still cannot claim, are in [03-what-students-can-run.md](03-what-students-can-run.md). Every page this research opened is in [04-sources.md](04-sources.md).

## Account shape

One account is not a production landing zone. AWS's multi-account whitepaper uses separate accounts to separate environments, limit blast radius, and constrain sensitive data. This course does not put sensitive data in AWS at all. A teaching account can still show a pinned Region, a task role, encryption of the public bucket, a budget, and a template that scanners can fail. It cannot show service control policies or an organization-wide audit account.

No price is stated in these notes. The 15 October 2026 post says Saudi Region prices may be unpublished and that a reference Region used for a model must be labeled as an assumption.
