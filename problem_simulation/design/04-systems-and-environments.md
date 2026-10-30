# Systems and environments

Facilitators only. Seventeen exports, plus four platform services. Each export has an interface note in the participant pack. The note describes the interface the cluster believes it runs. The defect is visible in the rows, the messages, or the log, and it traces to one cause in truth.

Zones are defined in [01 Hidden world](01-hidden-world.md).

## Exports

| Id | Zone | Interface | Planted defect |
|---|---|---|---|
| `his-nakhl` | hospital | HL7 v2 ADT and SIU, file plus a live feed | MRNs reused; a subset of PID dates are Hijri with no era marker |
| `his-safra` | hospital | HL7 v2 ADT and SIU | A merge applied in 2024 and reversed in 2026; SIU messages arrive out of order |
| `his-wadi` | private | FHIR R4 | Clinic code `END-01` became `ENDO-CLN` in June 2024; `rel-m02-l01` publishes FHIR v2 |
| `eref` | private | REST plus webhooks from `rel-m02-l02` | Patient API hides `pending`; return reasons cite the template version |
| `phc-templates` | files | The template pack PHCs actually generate | Still emits criteria v3 fields after the v4 draft exists |
| `sched-ain` | hospital | Nightly full file, last file wins | No intraday API; local clinic codes; a missed night leaves yesterday's slots |
| `nid` | national | Read API, strong auth | Check-digit failures; visitor-to-Iqama lag; death flags lag |
| `sms` | partner | Send plus receipts | Receipts late and duplicated; foreign numbers fail quietly |
| `wa` | partner | Business API from `rel-m02-l02` | Template messages need a registered template; replies die after the session window |
| `cc` | private | Call and chat export, plus the 2023 bot archive | About 45% of calls are reason-coded `GEN`; notes hold PHI; schema adds `disposition` in 2025 |
| `complaints` | private | Case export | Recorded category disagrees with the text; two texts carry prompt injection |
| `consent` | private | Grants with scope and expiry | Expired caregiver grants still served from a cache |
| `insure` | partner | Eligibility, mutual TLS | Snapshot can be 48 hours old; `rel-m04-l04` is a gateway outage |
| `hr` | private | Roster and leave, asked for on `rel-m04-l05` | Leave is entered after the session is published |
| `bi` | private | Waitlist mart and dashboard SQL | Clock starts at `booking_date`; people are counted as rows; eligibility SQL is stale |
| `iam` | private | Staff accounts, groups, access audit | Leavers and a role change keep access; `svc-integration` is a directory admin |
| `finance` | private | Cost centers and the price sheet | A 2025 recode; one benefit counted in two lines; GPU purchase lead time 16 weeks |

Travel minutes are a reference table, `ref-travel`, keyed by PHC and hospital. They are not a system of record. The maps vendor's MCP server is a partner tool and is specified in [08 Live services](08-live-services.md).

## Platform services

| Id | Role | Defect the lessons use |
|---|---|---|
| `int-engine` | Maps HL7 v2 to the cluster's FHIR-shaped event stream | Drops the sub-specialty on one mapping; debug logs include PHI since change `CHG-2025-118` |
| `dms` | Versions, audiences, approvals, change feed | An unauthorized Ramadan circular is filed as `public`. See [05 Corpus](05-corpus.md) |
| `catalog` | Field name, classification, system of record, lineage | `END-01` is still defined; `eligibility` changed meaning in 2024 with no catalog edit |
| `itsm` | Incidents and the change calendar | The cause of a data gap is in the ticket text, among routine tickets. Ramadan module is a change freeze |

## Classification and contracts

The catalog classification decides whether a field may be sent to `ext-large`. Foundation classes are `public`, `internal`, and `phi`. National id, date of birth, name, and phone are `phi`. Clinic hours and public leaflets are `public`.

Each live API has a published OpenAPI document and a fixture of recorded faults. Contract tests in Module 2 run against those fixtures. A data contract names the event topic, the required fields, and the owner. `referral.submitted` is owned by `eref`. `session.cancelled` is owned by the hospital that holds the session. `document.changed` is owned by `dms`.

## Cost keys

Truth and the finance export use the same keys: `cost.slot_missed`, `cost.return_cycle`, `cost.coordinator_hour`, `cost.call_minute`, `cost.sms`, `cost.wa_template`, `cost.label`, `cost.gpu_hour_rent`, `cost.gpu_buy`, `price.ext_large_per_1k`, `price.local_per_1k`, `harm.week_waiting`. Values are seed-generated. Renting GPUs is available in days. Buying them takes the 16 weeks on the procurement route, which misses 8 February 2027.

## Gold

For each export the generator writes a fault record: the cause id, the affected keys, and the clean columns in `truth/`. A check fails when the defect is missing or when the clean copy still contains it. Person-level counts join through the identity layer, not through MRN equality.
