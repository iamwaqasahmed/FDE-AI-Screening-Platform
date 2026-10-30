# Sources

Pages were read in October 2026. Titles and behavior below are what those pages stated then. LocalStack's authentication requirement is dated on the Testcontainers page as 23 March 2026.

## Synthea

- [Synthea repository](https://github.com/synthetichealth/synthea). Open-source synthetic patient generator. Disease modules are data. Exports include FHIR.
- [Recreating a Dataset](https://github.com/synthetichealth/synthea/wiki/Recreating-a-Dataset). Same output requires the same version plus `-s` population seed, `-cs` clinician seed, `-r` reference date, and `-e` end date. The end date defaults to the current date, so a later run is a longer simulation.
- [Generator options](https://github.com/synthetichealth/synthea/blob/master/src/main/java/org/mitre/synthea/engine/Generator.java). Defaults for seed, reference time, and end time follow the clock when flags are omitted.
- [Issue 1236](https://github.com/synthetichealth/synthea/issues/1236) and [issue 752](https://github.com/synthetichealth/synthea/issues/752). Same seed, different output, when the end date or the version moved. [Pull request 1237](https://github.com/synthetichealth/synthea/pull/1237) records reproducibility fixes.
- [Running Synthea (NIH ODSS FHIR for Research)](https://nih-odss.github.io/fhir-for-research/modules/synthea-running). Documents `-s` as the reproducibility flag and shows FHIR bundles written per patient.
- [Synthea overview (MITRE FHIR for Research)](https://mitre.github.io/fhir-for-research/modules/synthea-overview). Census-based demographics, one person simulated independently, modules as state machines, export to FHIR, C-CDA, CSV, or text. The sample narrative includes a person seed and a population seed.
- [Customizing Synthea](https://mitre.github.io/fhir-for-research/modules/synthea-customizing). Top-level modules versus submodules; delay, guard, and terminal states.
- [Generator.GeneratorOptions javadoc](https://synthetichealth.github.io/synthea/build/javadoc/org/mitre/synthea/engine/Generator.GeneratorOptions.html). Seed fields, including a default of the current time.

## HAPI FHIR and conformance tests

- [hapi-fhir-jpaserver-starter](https://github.com/hapifhir/hapi-fhir-jpaserver-starter). Local FHIR server. Docker: `hapiproject/hapi`, base URL `http://localhost:8080/fhir`. The README states that the starter ships without a security implementation and that the default subscription broker is in-memory.
- [Plain server getting started](https://hapifhir.io/hapi-fhir/docs/server_plain/get_started.html). A facade over data the implementer maps into resources.
- [JPA schema](https://hapifhir.io/hapi-fhir/docs/server_jpa/schema.html). `HFJ_RESOURCE.RES_VER` is the current version id. `HFJ_RES_VER` stores each version's full text.
- [REST operations, including history](https://hapifhir.io/hapi-fhir/docs/server_plain/rest_operations.html). Instance, type, and server history.
- [HL7 FHIR R4 history](https://hl7.org/fhir/R4/http.html#history). The specification operation a teaching server can implement without adopting HAPI as the system of record.
- [FHIR R4 DocumentReference](https://hl7.org/fhir/R4/documentreference.html). Attachment language is the standards hook for an Arabic and an English rendering of one document.
- [Da Vinci test-ehr](https://github.com/HL7-DaVinci/test-ehr). A HAPI server that loads seed files from `src/main/resources/seed-data` at startup.
- [Public HAPI sandbox](https://hapi.fhir.org/). A shared demonstration server. It is not a seeded Al-Waha environment.
- [ONC Inferno (g)(10) test kit](https://inferno.healthit.gov/test-kits/onc-certification-g10/). Executable FHIR tests plus a simulated conformant API used to demonstrate a pass.
- [Inferno test kits index](https://inferno.healthit.gov/test-kits/). Suites are validators aimed at a specification, grouped as test kits.

## LocalStack and Testcontainers

- [LocalStack with Testcontainers](https://docs.localstack.cloud/aws/customization/integrations/testing/testcontainers/). Local AWS emulation inside tests.
- [Testcontainers LocalStack module](https://java.testcontainers.org/modules/localstack/). States that starting 23 March 2026 `localstack/localstack` requires `LOCALSTACK_AUTH_TOKEN` or the container fails to start.
- [Testing AWS integrations with LocalStack](https://testcontainers.com/guides/testing-aws-service-integrations-using-localstack/). Ephemeral endpoint, random port, S3 and SQS created inside the container, application configured to that endpoint.
- [LocalStack testing overview](https://docs.localstack.cloud/aws/customization/integrations/testing/). Isolated, parallel cloud-API tests.
- [Testcontainers](https://testcontainers.com/). Disposable real dependencies for integration tests.

## Toxiproxy

- [Shopify Toxiproxy](https://github.com/shopify/toxiproxy) and the [README](https://github.com/shopify/toxiproxy/blob/main/README.md). TCP proxy. Toxics: latency (with jitter), bandwidth, slow close, timeout, reset-peer. `toxicity` is the fraction of connections affected. Disabling the proxy brings the upstream down. The README describes laptop-scale throughput and sub-millisecond overhead with no toxics. Jitter and toxicity are the random knobs a graded run must pin (jitter 0, toxicity 1).
- [Latency toxic source](https://github.com/Shopify/toxiproxy/blob/main/toxics/latency.go). Jitter uses an unseeded random integer.
- [Timeout toxic source](https://github.com/Shopify/toxiproxy/blob/main/toxics/timeout.go). Drops data and can close the connection after a fixed timeout.

## Teaching banks, retail, and operations

- [PaySim](https://github.com/EdgarLopezPhD/PaySim). Multi-agent mobile-money simulator built because real logs were not shareable. Later calibrated to aggregated transactions.
- [PaySim.properties](https://github.com/EdgarLopezPhD/PaySim/blob/master/PaySim.properties). `seed=time` unless changed. Also sets client, merchant, bank, and fraudster counts.
- [PaySim paper (EMSS 2016)](https://www.msc-les.org/proceedings/emss/2016/EMSS2016_249.pdf). Lopez-Rojas, Elmir, and Axelsson. Synthetic financial data from agent-based simulation. Fraud-detection methods are described as later work in this paper.
- [PaySim1 on Kaggle](https://www.kaggle.com/datasets/ealaxi/paysim1). The teaching extract. The published column notes, quoted in [this notebook](https://github.com/elangovana/PaySim-Synthetic-Dataset-Fraud-Detection/blob/master/PaySim%20Synthetic%20Dataset%20Fraud%20Detection.ipynb), define `isFraud` as transactions made by fraudulent agents inside the simulation. The label ships with the rows. Merchant destination balances are omitted.
- [Bank of Anthos](https://github.com/GoogleCloudPlatform/bank-of-anthos). Sample bank: ledger writer, balance reader, transaction history, user JWTs, Postgres, and a Locust load generator. Accounts are artificial and user-created. The balance reader is a cache of the ledger.
- [MIT beer game, Sterman](https://web.mit.edu/jsterman/www/SDG/beergame.html). Retailer, wholesaler, distributor, factory. Order delay and shipping delay. Each sector sees local inventory. A small demand change is amplified upstream.
- [MIT Sloan beer game online](https://mitsloan.mit.edu/teaching-resources-library/mit-sloan-beer-game-online). The same game as a multiplayer teaching sim.
- [Bullwhip causes](https://beergame.org/teaching/bullwhip-causes/). Lack of information, lead time, and local optimization. Upstream stages see orders, not customer demand.
- [Beer game debrief](https://beergame.org/teaching/debriefing/). Players blame neighbors; the structure is the delay.
- [Contoso Coffee demo data](https://learn.microsoft.com/en-us/dynamics365/business-central/contoso-coffee/contoso-coffee-intro). Fictitious firm. A tool generates module-scoped setup and transactions from a starting year, country, and price factor. Generated module data is not regenerated in the same company.

## Al-Waha design this note argues from

Facilitator documents already in the repository, read for this review and not modified:

- `problem_simulation/README.md`
- `problem_simulation/design/01-hidden-world.md`
- `problem_simulation/design/03-reference-system.md`
- `problem_simulation/design/04-systems-and-environments.md`
- `problem_simulation/design/05-corpus.md`
- `problem_simulation/design/06-engagement-and-delivery.md`
- `problem_simulation/design/08-live-services.md`
- `problem_simulation/design/11-eval-and-hardness.md`

## Out of scope

MITRE Caldera and similar adversary-emulation ranges were not used as design sources. This folder does not specify offensive cyber exercises. Scripted threat traffic already described in the Al-Waha facilitator notes stays a generated population with labels held in truth.
