# 04 — Words

Read this page once. You do not need to memorize it, and you do not need to open every link. Scan the tables, then go to [chapter 05](05-the-sprint.md). When a later chapter uses a word you want in the file's own sentence, come back to that row and open the link. You do not paste anything on this page, and you do not run a command.

These are the words this day uses. A definition here is the everyday meaning. When the rule lives in a file, the link is beside the word. Open that file when you need the sentence itself. This page does not type a hash, a token, the quota number, a clinic code, or a watermark. Those values stay in the files [chapter 03](03-the-change.md) already opened.

## The service

| Word | Meaning |
| --- | --- |
| Health cluster | A group of hospitals and primary care centers that plan and deliver care for one population. This client is the Al-Waha Health Cluster |
| Patient access | Referrals, appointments, reminders, and the phone line. The assistant you are building sits on that service |
| Referral | A request from a local clinic for a hospital appointment |
| Patient | The person the referral is about |
| Ain | Ain Diabetes and Eye Center. The facility id is `h-ain`. [zones.md](packet/kickoff/world/zones.md) puts it in `zone-hospital` |
| `h-ain` | The facility id for Ain |
| `h-wadi` | Wadi Specialist Hospital. A booking there is not today's file path |
| Chief Information Security Officer | [Omar Al-Zahrani](packet/kickoff/personas/ciso.md). His id is `ciso`. Yesterday's drop is from him |
| Enterprise architect | [Huda Al-Ghamdi](packet/kickoff/personas/ea.md). Her id is `ea`. The checks do not read an interview |
| Private cloud | The cluster's own cloud. [zones.md](packet/kickoff/world/zones.md) calls it `zone-private`. Site-a and site-b sit there |
| `zone-hospital` | The hospital data centers. The Ain file path sits here |
| `zone-public` | The public cloud. `ext-large` sits there |
| URL | `https://assistant.site-a.alwaha.internal`. [guide.md](packet/day4/endpoint/guide.md) states it |
| Namespace | The team folder for the manifest. The guide names it `ns-team` |
| `ep-local-small` | The private endpoint id. The router returns this id |
| `local-small` | The model that serves the assistant, in `zone-private` |
| `ext-large` | The external model. Patient data stays off it |
| Clinician | The person who assigns clinical urgency. The assistant does not |
| Urgency | Clinical urgency. It stays with a clinician |

## The smoke test, already copied

| Word | Meaning |
| --- | --- |
| Health probe | `GET /v1/health`. [health.yaml](packet/day4/openapi/health.yaml) names the call `readHealth`. The body reports the registered hash |
| Hash | The `hash` field on a register row. [models.json](packet/day4/registry/models.json) holds the rows. The probe reports the hash from the approved `local-small` row. You read it from the file. You do not type it |
| Register | [models.json](packet/day4/registry/models.json). Each row has `hash`, `id`, `status`, and `zone`. The spec is [registry.yaml](packet/day4/openapi/registry.yaml) |
| Approved | `status` `approved`. The probe uses this row for `local-small` |
| Quota | The `requests` field in [quota.json](packet/day4/registry/quota.json). Read the number there. This page does not type it |
| Non-root | The container user is not root. [pol-deploy.md](packet/day4/standards/pol-deploy.md) names this check |
| `USER 1000` | The last account line on the Dockerfile. `1000` is not root |
| Credential | The `endpoint` field in a credential file. [dev.json](packet/day4/credentials/dev.json) and [prod.json](packet/day4/credentials/prod.json) each have `endpoint`, `env`, and `registry` |
| Dev | The dev environment. Its credential file is `credentials/dev.json` |
| Prod | The prod environment. Its credential file is `credentials/prod.json`. Prod does not read the dev file |
| Root | The account in [root.json](packet/day4/fixtures/root.json). The image in `work/` already rejects it |
| Candidate | The unregistered near name in [candidate.json](packet/day4/fixtures/candidate.json). The probe in `work/` does not select it |
| National id | An identifier that must not remain on a deploy log line. The admission code already strips it. The check message does not name the id |
| Smoke | The Day 4 URL, probe, image, credential, and router, still in place. The sprint names it first |
| Manifest | [deployment.yaml](work/deploy/deployment.yaml). It already sets `ns-team`, refuses a root account, and calls `/v1/health` |
| CI | [ci.yml](work/.github/workflows/ci.yml). It already runs the suite. You do not replace it |
| Suite | The tests under `work/tests`, together with the app files they call |

## The change and the file

| Word | Meaning |
| --- | --- |
| `cr-ain` | The change request. [cr-ain.md](packet/release/notices/cr-ain.md) says include `h-ain`, and sequence the work |
| Sequence | The order of the work. The smoke test comes before `cr-ain`. The readout and the retro come after |
| `sched-ain` | The schedule interface for Ain. [sched-ain.md](packet/release/systems/sched-ain.md) describes it. The spec is [sched-ain.yaml](packet/release/openapi/sched-ain.yaml) |
| Nightly | A full file that arrives once a night. The last file wins. There is no intraday API |
| Missed night | A night when the file does not arrive. The previous file stays |
| Clinic code | A local code on Ain's file. Read it from [nightly.json](packet/release/fixtures/nightly.json). The previous code is in [missed.json](packet/release/fixtures/missed.json). You do not type either value |
| Previous file | The file a missed night leaves behind. Its status field is `previous` |
| Queued | The status a real-time booking returns. [queued.json](packet/release/fixtures/queued.json) has facility `h-ain` and status `queued` |
| Live-slot | The fault in [live-slot.json](packet/release/fixtures/live-slot.json). The status on that file is `booked`. Do not copy the file |
| Booked | The status of the live-slot fault. It is also what another hospital returns. It is not a confirmed slot at Ain |
| `holds` | The contract function. A queued booking holds. A booked status does not |
| Watermark | The mark on `live-slot.json`. The check message does not print it. A copy of that file in `work/` fails the check |
| Shell | The starter copy in `packet/`. The shell books every hospital, clears a missed night, confirms a failed notice, and accepts every status |
| `practice` | The shared classroom world. The build in chapter 01 uses it |
| `rel-w2d5` | Today's file drop |
| `rel-w2d4` | Yesterday's file drop. The smoke check still reads it |

## The pages

| Word | Meaning |
| --- | --- |
| Sprint | The order of the work. Smoke, then the change, then the readout, then the retro |
| Readout | The note for steering. The headings are Smoke, Change, File, Patients, Monitoring, Model, and Asks |
| Retro | The short look back. The headings are Keep, Drop, and Open |
| Deployment note | [deployment.md](work/deployment.md). The Day 4 headings stay: URL, Zone, Probe, Credentials, Monitoring, Boundary, and Operator steps. Today adds Ain and Change |
| Ain section | The deployment heading that names `h-ain`, `sched-ain`, nightly, and `zone-hospital` |
| Change section | The deployment heading that names `cr-ain` and sequences it after the smoke test |
| Zone row | [zones.md](work/zones.md). The columns are `surface` and `zone`. One row is `url`. One row is `sched-ain` |
| Operator steps | How someone reads the health probe with the prod credential |
| Monitoring | Request rate, error rate, and model latency. [starter.md](packet/day4/dashboard/starter.md) says the rest of the operations stack arrives in Week 4 |
| Latency | Model latency, one of the three lines on the starter dashboard |
| Stage 2 | The operations stack beyond those three lines. It arrives in Week 4 |
| Week 4 | The week that adds that stack |
| Boundary | A clinician assigns clinical urgency. Patient data stays off `ext-large` |
| `pol-deploy` | The checklist id. Chapter 08 cites it |
| Citation | A source a page names. `endpoint/guide.md`, `notices/cr-ain.md`, `systems/sched-ain.md`, `registry/quota.json`, `ciso`, and `ea` are sources |
| PHI | Patient data. It stays off `ext-large` |
| Asks | The readout section that must not be empty. It keeps patient data off `ext-large` |

## What the check will see

| Piece | What you should see |
| --- | --- |
| Probe | The approved `local-small` hash. The message does not name the hash |
| Image | `USER 1000` on the Dockerfile. Root is rejected by admission |
| Credentials | Prod reads `prod.json`. Dev reads `dev.json`. The message does not name a token |
| Router | `ep-local-small`, `local-small`, and `zone-private` |
| Booking | `h-ain` with an empty fault returns `queued`. The live-slot fault returns `booked` |
| File | A missing night returns yesterday. A file that arrives replaces it |
| Notice | A queued booking stays `queued` when the notice fails |
| Contract | `holds` is true for `queued` and false for `booked` |
| Sprint | The words smoke, change, readout, and retro, in that order |
| Zones | `url` in `zone-private`, and `sched-ain` in `zone-hospital` |
| Deployment | The Day 4 facts, plus Ain and Change. `cr-ain` is sequenced after the smoke test |
| Readout | Smoke, Change, File, Patients, Monitoring, Model, and Asks |
| Retro | Keep, Drop, and Open, each with text |
| Knowledge | Why Ain waits, and what Stage 2 adds |
| Demo | The six lines from chapter 03. They do not print nightly or a clinic code |

The hash, the two credentials, the quota number, and the two clinic codes stay in the pack files. This page does not store them.

Next: [05 — The sprint](05-the-sprint.md).
