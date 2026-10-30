# Reference simulators

These programs show techniques worth borrowing. None of them is a substitute for the Al-Waha case. MITRE Caldera and other adversary-emulation ranges were left out of this review on purpose. This note does not describe offensive cyber ranges.

## Synthea: a seeded population, a complete chart

Synthea (MITRE's Synthetic Health project) builds fictional patients from public statistics and disease modules. No real patient's record is an input. Each person is simulated from birth to death or to an end date. Modules are JSON state machines. Control states delay or guard. Clinical states write conditions, encounters, and procedures. Transitions can be direct, conditional, or weighted. A seed is supposed to recreate a population.

The project wiki is explicit that a matching seed is not enough. Recreation also needs the same Synthea version, the same clinician seed (`-cs`), the same reference date (`-r`), and the same end date (`-e`). The end date defaults to the day of the run. A later run with the same `-s` can add events and change ids. Issues 752 and 1236 record years of that failure, followed by fixes. The generator options default seed, reference time, and end time to `System.currentTimeMillis()`.

Exports include FHIR R4 transaction bundles, C-CDA, and CSV. The FHIR narrative has been observed to embed the person seed and the population seed in `Patient.text`. The bundle is one longitudinal chart: the patient resource first, then clinical resources in time order.

**Use.** Steal the discipline: one seeded random stream, an explicit end date, a pinned tool version, and modules as data so a behavior can change without a new program. Disease-shaped modules are a reasonable internal representation for latent specialty need, if they stay in the facilitator tree.

**Leave.** Do not put Synthea bundles in the participant pack. A complete chart is the opposite of Nakhl versus Safra versus a nightly Ain file. A narrative that prints the seed leaks the hidden world. US census demographics and US Core profiles are the wrong population for this case. Synthea also does not model a consulting engagement, a policy corpus, or a procurement calendar.

## HAPI FHIR: a protocol server with history

The HAPI FHIR JPA starter is a local FHIR server. Docker image `hapiproject/hapi:latest` serves `http://localhost:8080/fhir`. The starter ships with no security layer, no enterprise log pipeline, and an in-memory subscription broker. The public sandbox at `hapi.fhir.org` is a shared server with no Al-Waha data. The JPA schema stores every resource version in `HFJ_RES_VER` (`RES_VER` 1, 2, 3, …). Clients read history with `GET [base]/[type]/[id]/_history` and a specific version with vread. HL7's own history operation is the same idea. The Da Vinci `test-ehr` starter loads FHIR files from `src/main/resources/seed-data` at boot.

A plain HAPI server is a facade: existing rows are mapped into resources, and search parameter names are the FHIR names, not the hospital's column names. That is the interesting pattern for `his-wadi`.

**Use.** If Wadi's mock grows a history operation, preload it from the worldbuild export for that team and profile. Versioned `DocumentReference` or `Library` resources can carry `status`, effective period, and `content.attachment.language` for Arabic and English. Students who always read the current version fail the citation check. The binding decision stays a grader function over status, case date, and site scope.

**Leave.** An empty HAPI, or the public sandbox, teaches the wire format and nothing about this cluster. Do not let students treat one JPA database as the identity of a person who has three MRNs. Do not turn the Markdown corpus into a generic FHIR dump. The leaflets, the unauthorized circular, and the postmortem are the case. FHIR is one more rendering, seeded from the same fact spec, for the hospital that already speaks FHIR.

ONC Inferno is the grading analogue. The (g)(10) test kit is an executable suite, and it ships a simulated conformant API so a pass can be demonstrated. The suite checks requests and responses. It does not ask a model whether the server "seemed" compliant.

## LocalStack and Testcontainers: local, isolated, real clients

LocalStack emulates AWS APIs on a laptop so a client uses the AWS SDK against `localhost` instead of a cloud account. Testcontainers starts that emulator, or Postgres, or a broker, in a disposable container on a random port. The same image is what CI runs. The LocalStack Testcontainers guide shows S3 and SQS created inside the container, then an application pointed at those endpoints. Tests can run in parallel because nothing shares a fixed port.

As of the Testcontainers LocalStack module note dated 23 March 2026, the `localstack/localstack` image requires a `LOCALSTACK_AUTH_TOKEN` or the container fails to start. A course that grades on a laptop without a vendor account should not take that dependency for the core path.

**Use.** Steal isolation and disposal. Each team profile (`team-1` … `team-5`, `personal`, `assessment`) already has a seed. The grading service should boot a fresh mock network from that seed, run the scripted journeys against the team's `POST /v1/chat`, read mock end state, and throw the network away. One team's booking must not remain for the next submission.

**Leave.** The partners in this case are hospitals, national identity, SMS, WhatsApp, insurance, maps, and a document store. They are not S3 and SQS. Speaking AWS to LocalStack would invent a second enterprise beside Al-Waha. Ain's nightly file is already a file drop. Keep `python -m alwaha.serve`.

## Toxiproxy: faults in front of a partner, small enough for a laptop

Shopify's Toxiproxy is a TCP proxy with an HTTP API. Documented toxics include latency (milliseconds plus jitter), bandwidth, slow close, timeout, and reset-peer. Disabling the proxy is how a service "goes down." Each toxic has a direction (upstream or downstream) and a `toxicity` from 0 to 1, the fraction of connections affected. The latency toxic draws jitter with an unseeded random call. With no toxics, the proxy's own overhead is well under a millisecond, so it is a laptop tool, not a cluster product.

**Use.** Put a proxy, or an in-process equivalent with the same vocabulary, in front of `insure`, `nid`, `sms`, `wa`, and the maps vendor. The case clock selects the toxic set. Graded runs set `toxicity` to 1 and `jitter` to 0, and they use fixed millisecond values stored in truth. A Tuesday timeout for Rim travel, a duplicated SMS receipt, and a disabled insurance proxy during `rel-m04-l04` are then replayable. Practice drills can show jitter. Those runs are not the score.

**Leave.** Do not grade a run whose latency depends on `rand.Int63n`. Do not ask students to operate a chaos product. They feel slow and closed sockets. Facilitators own the script.

## PaySim and Bank of Anthos: teaching financial enterprises

PaySim is a multi-agent mobile-money simulator. It was built because real transaction logs were private. Agents and aggregated statistics produce synthetic payments. The open-source `PaySim.properties` defaults `seed` to `time`, so two launches differ unless the operator pins it. The PaySim1 extract published for Kaggle includes `isFraud` on every row: the generator's label ships beside the transaction. Merchant rows also omit destination balances, which is a small, useful partial view. The 2016 paper treats fraud injection as later work; the teaching file most people download has already attached the label.

Bank of Anthos (Google) is a small bank students can run: a web front end, a ledger writer, a balance reader, a transaction history, Postgres, a user service that signs JWTs, contacts, and a Locust load generator that opens accounts and sends payments. The ledger is the system of record. The balance reader is a cache of that ledger. Users create artificial accounts, so the world changes under the class. There is no held-back gold set and no policy corpus.

**Use.** From PaySim, take agent behavior calibrated to published aggregates, and take the warning that a label column in the student file ends the exercise. From Bank of Anthos, take the split between a ledger and a stale readable cache (the consent cache and the insurance snapshot are the same shape), scripted background load, and service-to-service tokens that are not user tokens. The confused-deputy case, where `svc-integration` can read any patient, is this pattern with higher stakes.

**Leave.** Do not publish pairwise identity labels, fraud flags, or "this citation is wrong" columns in the participant pack. Do not let the graded world be whatever the last student wrote into a shared bank. Reset from the seed.

## The beer game and Contoso Coffee: operations delay and a fictional firm

The MIT beer distribution game (Jay Forrester's industrial dynamics, later John Sterman's flight simulator) puts people in a retailer, wholesaler, distributor, and factory. Each week has an order delay and a shipping delay. Each role sees its own inventory and the order in front of it. Customer demand is a card deck. A one-step change in retail demand is amplified upstream because shipments are still in transit. Sterman's account is that players order as if the pipeline were visible. It is not. Costs are defined (inventory and backlog) so a debrief can compare a feeling with a number. The modern online game keeps that structure for a class of any size.

Contoso Coffee is Microsoft's fictitious company for Dynamics 365 Business Central training. A demo tool writes setup, master, and transactional data for selected modules. Parameters include a starting year, a country, and a price factor. The documentation says a module generated into a company cannot be generated again there. Country datasets localize the same firm.

**Use.** Procurement in Al-Waha should feel like the beer game's pipeline. A GPU purchase order placed on 10 January 2027 is acknowledged late, may arrive incomplete, and runs into the Ramadan freeze. Sixteen weeks is the published lead time. The vendor's other customers and internal queue stay hidden. The team's cost model can still use the existing keys (`cost.gpu_hour_rent`, `cost.gpu_buy`). From Contoso, take the idea of a named fictional firm whose data generator is parameterized by a start year and whose modules can be turned on without a second company. Al-Waha already has the better grading property: the same seed rebuilds the world. Contoso's one-shot company is a caution.

**Leave.** Do not replace the health system with a supply-chain board or an ERP sample company. The delay structure is what transfers. The patients, the clinics, and the statutes stay.

## What the set teaches together

| Need in this course | Closest working pattern | Property to keep out of the student pack |
|---|---|---|
| Seeded population | Synthea's pinned seed, clinician seed, reference date, end date, version | The complete chart and the seed printed in the narrative |
| Versioned documents | HAPI resource history and Inferno's executable checks | A public sandbox or an empty server |
| Isolated grading | Testcontainers' disposable, per-run endpoints | A LocalStack account and an AWS-shaped hospital |
| Unreliable partners | Toxiproxy toxics with toxicity 1 and jitter 0 | Unseeded jitter on a graded run |
| Hidden labels | PaySim's privacy motive, inverted: labels stay facilitator-side | PaySim1's `isFraud` column |
| Stale reads and scripted load | Bank of Anthos ledger versus balance cache, plus Locust | A world students permanently mutate |
| Procurement lag and local vision | Beer game order and shipping delays | A full view of the vendor's queue |
| Fictional firm as a generator | Contoso's module-scoped demo data | A one-shot company that cannot be rebuilt |
