# The boundary

[data/corpus/dpo_operating_rule.md](../data/corpus/dpo_operating_rule.md) is the deployment spec. It is in force.

- Screening records stay in this run. They are not sent anywhere else.
- Every ask is written to an access log.
- Patient images are not used to train a model. This service does not train.
- A generated letter may repeat a grader's code. It must not contain a diagnosis.
- A grader still signs any result that refers, recalls, or reassures a patient.

The service does not add a count or a search. It calls the agent you already have. The default model is scripted, so a cold start does not need an API key.

Next: [Access log](02-access-log.md).
