# Agent execution

On 30 October 2026, ten local agents ran in parallel. Each owned different files. This coordinator then wired their commands into `history()`, taught the payer projection to keep non-coverage rows, and added `python -m access scenario`. No AWS account was opened. `repair` was not written.

| Agent | Owned files | Result |
| --- | --- | --- |
| [Org stakeholders](dc874082-175c-4369-aa58-765a4dafc624) | `org_model.py`, `docs/stakeholders.md` | 12 commands: one wait number, the letter, Cedar Ridge night file, a payer timeout |
| [Problem threads](76b95b0f-5649-464f-ba01-3182671cf3f3) | `problem_threads.py`, `docs/problem_threads.md` | THR-17 across desk, file, payer, and cache |
| [Synthetic data](dc12a4d5-282d-42e5-bc3a-10b723c0d95f) | `data_quality.py`, `docs/data_quality.md` | 12 commands: shared phone, currency flip, local date, bad postal, empty phone, appended correction |
| [Legacy desk](36da9b41-2707-4f2b-9cc3-bcfb018d30b2) | `legacy_desk.py`, `docs/legacy_desk.md` | Reused screen code, stuck caller, hidden pending, no slot API |
| [Integrations](de2970a5-bf9b-4958-8737-8b38e2812617) | `integration_faults.py`, `docs/integration_faults.md` | Repeated outbox, INT-17 cancel time before file time with a later revision |
| [Access audit](f506a24c-a53a-45c1-b993-e29ec9a323dc) | `access_audit.py`, `docs/access_audit.md` | Clerk download, `us-east-1` copy, wage attached to an hours packet, break-glass with no reviewer |
| [Scenarios](91b441cf-39a8-45ad-a407-3a2afaa66f7e) | `scenarios.py`, `docs/scenarios.md` | `partner-outage` and `hours-served-stale`, off until named |
| [Local runtime](ef8f4d75-d55f-4df2-b5ee-454433a8df7a) | `runtime_check.py`, `docs/local_runtime.md` | Read-only local report. That agent ran it once: Python 3.14.6, no leaks |
| [Curriculum evidence](a1ce4971-00ea-45a8-9f72-25f1c8d54c2b) | `curriculum_evidence.py`, `docs/curriculum_gaps.md` | Cancelled visit still texted, tiny score note, shadow write, FAQ that quotes a letter |
| [Adversarial tests](11b3e005-aab6-4335-b656-accafd0eba30) | `tests/test_adversarial.py` | 11 tests, OK, before the extra history was wired |

After wiring, `python -m unittest tests.test_simulation tests.test_releases tests.test_adversarial tests.test_threads` reported `Ran 39 tests in 2.876s` and `OK`. `python -m access init` printed 772 events for seed `20270110`. The student pack was searched and did not contain `dec-accept`, `dec-clinical`, or `refused`.

## Round 2

Ten more local agents ran in parallel on 30 October 2026. Their modules were then appended to `history()`, except the incident overlays and the 400-referral workload file.

| Agent | Owned files | Result |
| --- | --- | --- |
| [Business processes](b52a3398-65b1-41cc-91c6-8f9fc633c196) | `round2/operations.py` | Onboarding, quotation `QUO-18420` with two supplier ids, Saturday file notes |
| [Correlated cohort](eb207068-7b3d-4f71-8134-e1bfbfc0c433) | `round2/cohort.py` | 48-referral cohort on the log. `workload(400)` is 1040 commands in `var/workload.jsonl` |
| [Lesson feeds](73936536-0961-415c-b81e-0112be4acec2) | `round2/lesson_feeds.py` | Draft document, lagged Cascade read model, separate Fraser and Cedar feeds, delivery split, leave |
| [Queries](91187e94-cb2f-40ab-b059-3b54429de28b) | `round2/query.py`, `link_events.py` | `by_ref` is served at `GET /ref/<ref>`. `R2D-7` has two member ids |
| [Deeper case](2c7405ef-b7ff-454c-a34f-08bf35bf0a3b) | `round2/deep_case.py` | `R2E-9` |
| [Timelines](13bf689b-7871-497d-87d2-cb98860beaa0) | `round2/timelines.py` | Schema epochs, late record, source row `S-14` used twice |
| [Incidents](54e11993-b6e5-4bff-9072-d669a90590a9) | `round2/incident_overlays.py` | `replay-storm` (953 events) and `partial-write` (954), then base restored at 949 |
| [Locale audit](bc68a69b-1d1b-4977-aad3-9fa92426500e) | `round2/locale_examples.py` | Postal versus ZIP, CAD versus USD, spreadsheet stamp that dropped the offset |
| [Student walkthrough](bccee256-b538-4788-abfa-1995721022bb) | `tests/test_lesson_access.py` | 10 tests, OK, against the pack. Noted the Monday–Friday deviation from IDEA's Sunday–Thursday line |
| [QA](d54f0d68-f470-4276-be9a-c167ddd44839) | `tests/test_round2_qa.py` | 10 tests, OK |

After that wiring, the six test modules together reported `Ran 59 tests in 3.999s` and `OK`. `init` printed 949 events. `GET /ref/REF-4417` returned 34 hits. Document statuses on disk were `draft`, `in_flight`, `in_force`, `superseded`, and `unauthorized`.

## Round 3

Ten more local agents ran in parallel. Their commands were appended to `history()`. The stress generator was not. The mart extract no longer carries the field `booking_date_only`.

| Agent | Owned files | Result |
| --- | --- | --- |
| [Merger](063d3bea-de9f-4492-84c0-e3b33c904966) | `round3/merger.py` | Inlet Medical merged into Cedar Ridge; both site ids still file |
| [Seasonality](fe7bb914-f526-4091-a583-53d42e1a0020) | `round3/seasonality.py` | 24-month volume in the pack. January 2026 WA volume is 498 against July 238 |
| [Identity graph](671d0507-6ba3-43a1-9c8d-9e389dc8426b) | `round3/identity_graph.py` | 9 edges, including a phone copied onto the wrong chart |
| [Contracts](728f6e48-6159-4713-861f-f794b295023c) | `round3/contracts.py` | MA-2024 versions, a mislabeled print, a backdated amendment |
| [Replicas](b184dc7f-1e06-42b4-8d62-5e84537ef478) | `round3/replicas.py` | Cursors 14 and 10. Amount 90 in USD and CAD |
| [Ledger](3e9427b5-404d-42ed-9e52-03e779a9a54f) | `round3/ledger.py` | `R3F-LEDGER` |
| [Governance](c0b0d431-ad95-4bd6-9660-e816192f4cf3) | `round3/governance.py` | Consent disagrees. Copy completed with no reviewer |
| [FDE review](d2ccac70-bd05-4a30-85d1-4d65bc0fe4da) | `docs/round3/challenge_review.md`, `tests/test_round3_challenge.py` | Flagged `booking_date_only` on every mart row. That field was removed |
| [Scale](fe40e41a-ecfd-4faf-9195-9cdc28b05700) | `round3/scale.py` | 2000 events appended in 0.162 seconds on a temp database |
| [QA](e3c139f5-af24-4130-8f8c-3fd312a41608) | `tests/test_round3_qa.py` | 8 tests. Seasonality was skipped until the module existed; the later full run included it |

The eight test modules then reported `Ran 68 tests in 5.684s` and `OK`. `init` printed 1005 events.

