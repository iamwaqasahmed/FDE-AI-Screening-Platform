# What the agent may do

**Days 2 and 3. Architect and consultant.** The software engineer builds to this. Read the tier policy, the oversight standard, the logging standard, the authentication standard, the classification policy, and the cloud policy before you pick a model or an account.

## The tier

The agent searches, summarises, and drafts, and a person reads every output. That is tier 2. Tier 2 needs a register entry and a transparency record before anyone but this team uses it. You are not deploying it this week.

Ranking, triaging, or prioritising people, or informing a clinical decision, would make it tier 3. Tier 3 needs a named clinical safety owner. The field is blank. A tier 3 system does not go live, including as a pilot. The agent must not rank the overdue list.

## A rule is a document

Each stop cites the document that makes it. Write the family's document id. Where two documents both make the stop, either is accepted.

| Family | What it stops | Documents |
|---|---|---|
| `stop` | Starting the pilot, or telling anyone it is in use | `owner-governance`, `ai-risk-tier-policy` |
| `scope` | Sending a hospital or outreach capture to the vendor | `dpo-restriction-memo` |
| `tier` | Ranking or prioritising people | `ai-risk-tier-policy` |
| `individual` | A fact about one person, in a line or a file | `data-classification-policy`, `dpo-rule-2018` |
| `model` | Personal data sent to a public-only model | `data-classification-policy`, `cloud-policy` |
| `logs` | A name, phone, address, or national id in a log | `security-logging-standard` |
| `write` | A token used beyond the rights it was given | `security-authentication-standard` |
| `grade` | Grading a photograph | `dpo-rule-2018` |

A question about a forbidden thing is answered, and the answer is the refusal. Doing the thing is the stop.

## The account and the models

`serve/tokens.yaml`. The discovery team's token reads the five systems. It cannot write. It is valid on today's date. Two other clients hold `booking:write`. One client expired before the summer. Those are `excess_rights` and `expired`.

`model_register.csv`. Personal data, including a local id and a complaint, stays on a model approved for official-sensitive data. Price a multi-hop step at 16,000 tokens in and 4,000 out. `multi_hop_cost` is that price for each personal-data generator, not the embedding model. `cheapest_generator` is the lowest of those. `multi_hop_budget` is the multi-hop budget in pounds, 0.05. A generator that costs more than the budget does not fit in one step.

The logging standard says what an application log must not hold, where a read of a patient record goes, and how long an audit log is kept. The trajectory keeps references. It does not keep values.

## Fill these findings

| Item | What it holds |
|---|---|
| `agent_tier` | `tier`, `tier_3_triggers`, `tier_3_lacks`, `tier_2_needs` |
| `veto_sources` | `sources`, one document id per family |
| `service_account` | `client`, `scopes`, `read_only`, `expires`, `burst`, `per_minute`, `excess_rights`, `expired` |
| `model_routing` | `personal`, `official_only`, `public_only`, `cheapest_generator`, `multi_hop_cost`, `multi_hop_budget` |
| `audit_and_logs` | `never`, `reads_go_to`, `retention_years`, `references_not_values` |

`tier` is 2. `tier_3_triggers` is `rank`, `triage`, `prioritise`, `clinical`. `tier_3_lacks` is `clinical safety owner`. `tier_2_needs` is `register entry` and `transparency record`. `never` is `name`, `phone`, `address`, `national id`. `reads_go_to` is `access audit log`. `retention_years` is 7. `references_not_values` is true. `client` is `discovery-team`.

**A miss that looks like progress.** Putting the rules in a system prompt and calling that a veto. A prompt is a request. The stop has to be code that looks at the action.

**Finish.** The veto table is in the card. You can name the account, the models that may see a local id, and the model that may not.

Next: [The baselines](09-the-baselines.md).
