# From prototype to production

**Days 3 and 4. Be the software engineer.** Week 00 - Self Paced already runs. [Its Dockerfile](../../Week%2000%20-%20Self%20Paced/Dockerfile) copies the handover and the corpus into the image, and its command is `screening_service.run`. The checker in that course reads the Dockerfile and passes. Passing there is not the same as meeting Hartland's standards. Read the image against the standards, not against the Week 00 - Self Paced checker.

## Five gaps

Each gap names the standard it breaks.

| Gap | What the image does | Standard |
|---|---|---|
| `data_in_image` | `COPY` lines bring `data/handover` and `data/corpus` into the image | `data-classification-policy` |
| `model_off_register` | The adapter defaults to a model name that is not on `model_register.csv`, at `api.openai.com` | `cloud-policy` |
| `question_in_log` | The access log stores the raw question | `security-logging-standard` |
| `local_log` | The log is a local file. A read of a patient record belongs in the access audit log | `security-logging-standard` |
| `no_sign_in` | `--who` is whatever the caller types. There is no identity-provider sign-in | `security-authentication-standard` |

`copies` is those two paths, `data/handover` and `data/corpus`. `on_register` is false. `logs_question` is true. `sign_in` is false. `replace_with` is the cheapest text-generation model on the register that is approved for official-sensitive data. Price it from `model_register.csv`. An embedding model is not a generator.

## The token

`problem_simulation/serve/tokens.yaml`. The discovery team's token is the one this engagement has been using. Read its expiry. Week 6 runs from the drop's date to the Friday four days later. `expires_this_week` is true when the expiry falls inside that window, including Friday. There is no client named `screening-agent`. `production_client_exists` is false. The standard is `security-authentication-standard`: a service account is named, owned, and limited to the rights it needs. The discovery token is none of those for a service that outlives this week.

## Fill these findings

| Item | What it holds |
|---|---|
| `prototype_gaps` | `copies`, `default_model`, `model_host`, `on_register`, `logs_question`, `sign_in`, `gaps`, `replace_with` |
| `production_account` | `client`, `expires`, `expires_this_week`, `standard`, `production_client_exists` |

`gaps` is a list of `{gap, standard}` for the five rows above. `model_host` is `api.openai.com`. `client` is `discovery-team`.

**A miss that looks like progress.** "The Week 00 - Self Paced checker passed this Dockerfile." It checks that the image does not copy `data/truth`. It does not check residency, the register, or the log.

**Finish.** You can name the five gaps, the model that replaces the default, and the day the discovery token dies.

Next: [The production contract](10-the-production-contract.md).
