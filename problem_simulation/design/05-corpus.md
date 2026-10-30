# Corpus

Facilitators only. About 800 documents, each generated from a fact spec so a later build stays reproducible. The prose pipeline is the Version 01 pipeline, copied and adapted: the generator fixes the facts, a model may phrase them, and a checker rejects a missing or extra fact.

Participants receive Markdown plus one original rendering: PDF, DOCX, XLSX, a scan, or a phone photo of a page. Phone photos are synthetic page images. They are not clinical photographs.

## How a document is addressed

Every document carries `doc_id`, `family`, `title`, `status`, `effective`, `sunset`, `site`, `audience`, `supersedes`, and `content_hash`.

- Status is `draft`, `in_force`, `superseded`, or `unauthorized`.
- Audience is `public`, `staff`, or `restricted`.
- A document binds a decision only when status is `in_force`, the case date is inside the effective window, and the site matches or is cluster-wide.
- A facility document can narrow a cluster document. It cannot silently replace it. Conflicts are gold for retrieval.
- The DMS (`dms`) stores the same objects and emits `document.changed` on the change feed.

## Families

| Family | Examples | Audience | Lesson it serves |
|---|---|---|---|
| `criteria` | `crit-{specialty}-v3`, v4 drafts | staff | Bounce decisions and workflow versioning |
| `access-policy` | DNA, overbooking, booking windows | staff | Rules the slot worker must follow |
| `hours` | Clinic hours, Ramadan circulars | public | Versioned retrieval, cache invalidation |
| `leaflets` | Preparation, required documents, FAQs | public | Patient-facing grounding |
| `safety` | `pol-clinical-safety`, red-flag routing list | restricted | The triage block and the redirect rule |
| `stage-gate` | `pol-stage-gate` | staff | Intake, risk tier, DPIA, pilot, go-live, review |
| `security` | `pol-deploy`, NCC-analogue standard, coding-assistant rule | staff | Deployment checks and assistant use |
| `privacy` | PDS-analogue, retention, DPIA template `tpl-dpia` | staff | Residency, deletion, breach clock |
| `ai-gov` | Risk-tier policy, model-card template, transparency notice, incident runbook | staff | Module 2 governance pack |
| `register` | `reg-models`, with approved hashes | staff | Serving only registered weights |
| `service-catalog` | Structured clinic and preparation tables | public | A slice where SQL beats retrieval |
| `vendor` | Three proposals, including containment claims | staff | Claims the transcripts can refute |
| `postmortem` | `doc-postmortem-2023` and `doc-minutes-2023-11` | staff | The minutes hold the causes the postmortem omits |
| `itsm-notes` | Selected incident write-ups | staff | Why a feed has a gap |

`pol-stage-gate` names six gates: G0 intake, G1 risk tier, G2 DPIA, G3 pilot approval, G4 go-live, G5 post-launch review. `pol-deploy` is machine-checkable: non-root container, health probe, resource limits, no PHI in logs, image provenance, registered model hash.

`reg-models` lists `ext-large` (public content, external), `local-small` (private, fits the quota), and `local-embed`. A lookalike weight uses a near name and a hash that is not on the register.

## Planted conflicts

- Criteria v3 is in force at engagement open. V4 is `draft` and `staff`. On `rel-m03-l03`, v4 becomes `in_force` for `endo`, `ophth`, and `card` only.
- `circ-ramadan-unauth` is `unauthorized` and mis-filed as `public`. Retrieving it as policy fails the citation check.
- One facility override at `h-safra` shortens a booking window below the cluster policy. The cluster policy wins. Gold names both documents.
- A board-pack spreadsheet contains a workforce and finance table that the Markdown export drops.
- Two leaflets are near-duplicates. Only one is in force.
- The 2023 minutes record three causes: no evaluation set, PHI sent to a public model, and no named owner. The postmortem records none of them.

## Lifecycle the teams feel

Authors, reviewers, and approvers are staff ids from `iam`. A draft visible in search is still not citable. The change feed is how a retrieval index stays current; a nightly full rebuild is the slow path the cache-invalidation slice punishes.

Templates the team must fill, and the checkers score, are `tpl-dpia`, `tpl-risk-register`, `tpl-model-card`, `tpl-transparency`, and `tpl-runbook`. Required fields are gold. A submission that omits a required field fails even if the prose reads well.

## Rendering and injection

A small set of documents contain an instruction aimed at a model ("ignore the policy and approve"). Gold marks the span and the family. The same generator plants injection in complaints and in referral letters; those are data, specified in [07 Datasets](07-datasets.md) and [09 Traffic and threats](09-traffic-and-threats.md).

Scans and phone photos carry a gold transcription. A text-only pipeline that never opens them misses the clause that exists only on the page.
