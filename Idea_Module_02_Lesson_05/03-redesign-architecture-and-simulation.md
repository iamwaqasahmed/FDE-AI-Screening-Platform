# 03 — Redesign architecture and simulation

Proposal only. Nothing under `Module 02/Lesson 05` or `problem_simulation` changes until a later implementation pass. The fictional client, the zones, `h-ain`, `cr-ain`, and the ban on echoing clinic codes stay.

## Outcomes the simulation has to make visible

Fowler's first strangler activity is the outcome, not the module list. For this day the outcomes are:

1. Ain is included. Refusal without a reason is still a failed change.
2. A patient at Ain never sees `booked` from the assistant. The nightly file remains the slot master.
3. A bad file, a repeated file, and a missed night each leave a defined schedule, and only the missed night and the good file change what "current" means.
4. The change record names authority, backout, and the success test before the readout.
5. The monitoring answer lists the signals the starter dashboard does not have.

## Target architecture

```
zone-hospital                          zone-private
sched-ain                              assistant
  nightly full file                      book() -> queued for h-ain
  local clinic codes                     acl translates code -> facility
  no intraday API                        control check, then ledger
        |                                reconcile shadow vs intents
        |  file drop                     notify stays queued
        +-------------------------------> poison quarantine
                                         last good file retained
```

Wadi stays on the existing live path (`booked`). That split is the strangler seam: one facility moved, one facility explicitly not moved. The translator is the anti-corruption layer. It is a consuming mimic of Ain's file and, until Ain publishes an API, it is also the enduring partner boundary from the Legacy Mimic article. The readout says "enduring," not "temporary leftover," unless the pack grows a dated API promise. This pack does not.

### File document

Teaching JSON, not ACH and not HL7. One night looks like this:

```json
{
  "file_id": "ain-2027-01-21",
  "facility": "h-ain",
  "rows": [
    {"clinic_code": "<local>", "slot_count": 4}
  ],
  "control": {"row_count": 1, "slot_total": 4, "code_hash": "<hex>"}
}
```

`code_hash` is a hash of the clinic codes in row order. The checker computes it. The student function recomputes it. Check messages still must not print the code or the hash. They say `the control total did not match` or `a clinic code could not be translated`.

### Apply rules

State is `{good, ledger, poison}`. `good` is the last accepted file or `None` at the start. `ledger` is the set of accepted `file_id`s. `poison` is a count.

| Arrival | Result |
| --- | --- |
| `None` | `good` unchanged. Missed night. |
| `file_id` already in `ledger` | `good` unchanged. Idempotent resend. |
| `control.row_count` or `slot_total` or `code_hash` disagrees with the body | `good` unchanged, `poison` increases, file stored aside. |
| A row whose clinic code is not in the hospital map | Same as a bad control. The map is pack data, not a hardcoded display of the code. |
| Else | `good` becomes this file, `file_id` enters the ledger. Patient status does not become `booked`. |

Half-written files are represented by a missing ready flag on the fixture, treated as `None` for apply purposes and as a distinct miss if the function consumes them: `a partial file replaced the schedule`. That is the Hohpe timing rule, kept as one case so the day does not grow a filesystem lab.

### Reconciliation

A shadow ledger lists intents `book` accepted since the previous good file: facility, a synthetic patient key, status `queued`. After a successful apply, `reconcile` compares the count of those intents with the count of rows the translator accepted. A mismatch is an open item on the change record. It does not book, does not delete intents, and does not edit the file. This is the parallel run the hospital cases support: one master, one shadow, no second confirmation.

Exit from the shadow is not "the file exists." Exit is the success test on the change record: one accepted file whose totals matched, poison still zero for that night, and the synthetic book still `queued`.

### Notice

`notify` may record that a "still queued" message was attempted. If `sent` is false, the attempt stays retryable and the status stays `queued`. A true send also leaves `queued`. There is no transition to `booked` on either result. That replaces the current function, which deletes `sent`, while keeping the rule the shell violates.

### Change record

One page, `work/change.md`, beside the client's `cr-ain` card. The card stays the trigger and still need not contain the word nightly if the release test must keep that puzzle. The change record is where the interface is allowed to be named, because the student writes it after reading `sched-ain.md`.

| Field | Content for this case |
| --- | --- |
| Id | `cr-ain` |
| Model | Normal. First inclusion of a file-only hospital. |
| Authority | Delegated to the FDE using `sched-ain.md`. Not a standing board. |
| Schedule | After the deploy smoke and the synthetic book. Before any patient-facing claim of a slot. |
| Risk | A patient told they have a slot; a short file wiping clinics; a resend double-applying. |
| Backout | Stop apply. Retain the last good file. Every Ain status remains `queued`. Turn the synthetic expectation into the rollback check. |
| Success | One night accepted, totals recomputed equal, poison did not increase, synthetic book returned `queued`. |
| Later model | Nightly apply of a new `file_id` with a matching trailer becomes a standard change, pre-authorized by this record. Not built this day. |

PeopleCert's public purpose is the checklist for this page: risk assessed, change authorized, schedule managed. The CAB is discussed in the words chapter as the anti-pattern, in one paragraph, flagged as a paraphrase of the paid practice guide. Students do not role-play a board.

### Smoke and the monitoring gap

Release smoke, graded, cheap, in-process or against the existing test app:

1. Lesson 4 invariants, unchanged: hash, non-root, prod credential, private route.
2. `book("h-ain", "") == "queued"`.
3. No row with status `booked` and facility `h-ain` exists after that call.
4. A fixture file with a wrong `row_count` leaves the previous good file in place.

Synthetic monitoring, written and not implemented: the same book probe on a schedule against the deployed URL, plus a cutoff check that today's `file_id` has been accepted. White-box gaps written beside it: age of the oldest `queued` intent, poison count, control-break count. The starter three charts remain in the note as what the team has. The banned sentence is any claim that those three are enough, and any claim that "the rest" arrives in a named module as a substitute for the list.

### What Stage 2 still lacks, the sentence the readout must contain

The team can see request rate, error rate, and model latency. It cannot see file age past the cutoff, a control-total break, poison count, queue age, or a repeating probe that Ain still returns queued. Those five are the gap. Building them is a later module. Naming them is this lesson.

## Alternatives

### A — File-protocol day (recommended)

The day above, scoped to one afternoon. The student replaces apply, translate, reconcile, notify, and the contract, and writes the change record, the deployment note, the readout, and the retro. Paste blocks that are the full solution are not in the chapter. The chapter shows the fixture shapes, the table of arrivals, and failing tests the student has to turn green.

**Keeps** the trap, the zones, the missed night, the failed-notice rule, the Lesson 4 byte-identical smoke files, and secret hygiene.

**Deletes** optional modules, the `booked` return for the `live-slot` fault, last-dict-wins as a full mark, and the Stage 2 deferral sentence.

**Cost.** New fixtures and new miss strings. `serve/ain.py` and `queue_w2.py` change in a later implementation. Student chapters 06, 07, and 09 are rewritten, not patched.

**Why it is the default.** It is the boring interface the thesis says the FDE must ship. Strangler and ITIL show up as the seam and the record, not as a second syllabus.

### B — Strangler-and-ACL day

Spend the lab on the seam. `book` routes `h-wadi` to the live path and `h-ain` to a translator. The translator's tests are unknown codes, swapped codes between the nightly file and the missed-night file, and a ban on the raw code appearing in the private-zone status object. Dual-run is a written sequence: intercept at the facility id, shadow, exit criterion. The file trailer is a single assertion, not the center of the day.

**Gains.** Fowler's 2024 activities and Evans's two-way translation become the thing the student does. The clinic codes finally have a job.

**Loses.** Idempotent resend, partial file, and poison-versus-missed-night stay as readings. An FDE can still ship a translator that accepts a short file. That fails the thesis halfway.

**Use.** Steal B's translator tests and the "enduring versus transitional" readout sentence. Do not run B as the whole day.

### C — Change-enablement day

The lab artifact is the change record and a rehearsal of backout. Code stays close to today's three functions. Students label normal versus standard, name a delegate, and write the success test. A short reading contrasts a standing CAB with delegated authority, with the practice-guide paraphrase flagged.

**Gains.** The course word "change request" stops being confused with the practice. Question 2 of the steering card ("where in the sequence?") gets a real schedule and a backout.

**Loses.** The file remains last-dict-wins. Theater is reduced and the engagement still dies on a bad trailer. ITIL without the file is the mirror image of today's file-word without ITIL.

**Use.** Steal C's `change.md` fields. Do not drop the protocol.

### D — Monitoring paragraph only (rejected)

Keep every paste. Replace "Stage 2 adds the rest in Module 2" with the five signal names. Tighten the readout checker so `latency` plus `stage 2` is no longer enough.

**Why it fails.** It answers the knowledge question and leaves the optional modules, the collapsed miss, and the ungraded trailer. A student can delete `file_ain.py` and still pass, having written an eloquent gap list about a file they removed. The thesis is that the FDE must ship the interface. D ships a sentence.

### Rejected variant inside A

Big-bang option: `sched-ain` gains `POST /book` returning `booked` for the lab so the new system can be "complete." That is the trap, and it is the cut-over Fowler argues against. It also contradicts Module 1's recorded fact that Ain has no slot API. The curriculum map says the lesson depends on that fact.

## Simulation constraints

- Profiles `practice` and `small` keep distinct clinic codes and a single watermark, as `test_profiles_differ_by_canary` requires now.
- Prose fixtures and the change card can keep the ban on embedding the code. The nightly JSON keeps the code, as `test_notice_keeps_the_clinic_code_out` requires now.
- The demo can still avoid the word nightly. The student meets the protocol in `sched-ain.md` and the fixtures, then writes it.
- Check messages gain the new miss strings and still omit codes, hashes, tokens, quota, and national ids.
- `queue.py`, `file_ain.py`, and `notify.py` become required. Deleting them is `the booking path is missing`, not a pass.
- `live-slot.json` remains a fault fixture the student must not copy into `work/`. The function rejects that fault with an error status or a refused result. It does not return `booked`. The contract test expects the refusal. The journey miss for "returned booked on the happy path" and the miss for "treated the fault as a success" are different strings.
- Lesson 4 files stay byte-identical. The new work is new modules plus the notes.
- No network, no real hospital, no second confirming master.

## Module boundaries

Keep the files small, one decision each.

| Module | Decision |
| --- | --- |
| `app/queue.py` | Facility seam only. Ain queues. Wadi books. The live-slot fault is refused. |
| `app/acl.py` | Code to facility, or poison. No status flip. |
| `app/file_ain.py` | Apply table: miss, resend, poison, accept. |
| `app/reconcile.py` | Counts match or an open item. Never books. |
| `app/notify.py` | Retry bit without a status flip. |
| `app/contract.py` | `queued` holds. `booked` does not. A poison marker does not. |
| `work/change.md` | The enablement record. |
| `work/deployment.md` | Lesson 4 facts, Ain, the file protocol, the backout. |
| `work/readout.md` | Steering headings, with the five monitoring gaps named. |
| `work/retro.md` | Keep the seam, drop the live-slot promise, open the standard-change promotion after one clean night. |

`individual_w2` runs the contract tests, or calls `holds` on queued, booked, and poison. A source-string check for `holds` is not the grade.

## Relation to neighboring lessons

Lesson 4's deploy stays the smoke base. Lesson 2's event and HL7 work is a different style in Hohpe's list; this day should say so in the words chapter, in one paragraph, so students do not hear "integration" as only webhooks. Module 3 Lesson 1 is still the next morning (labels, synthetic sample). The carry-forward sentence changes: the file protocol is in place, Ain is still queued, and the monitoring gaps are named for a later operations lesson. It does not say the operations stack arrived, and it does not say the file was a placeholder Module 3 will delete.
