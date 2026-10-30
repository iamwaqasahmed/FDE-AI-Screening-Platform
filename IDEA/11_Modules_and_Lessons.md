# 11 — Modules and lessons

There is one module, the engagement, and nine lessons. Splitting them into themed modules would imply a sequence of subjects. The sequence is the dependence of the contracts.

Shared rules for every lesson are in [the learning design](13_Self_Paced_Learning_Design.md). This file records only what changes per lesson.

## INV-01 — Whose clock

- **Purpose.** Bind a screen to the authority its label promises.
- **Problem.** The wait matches the warehouse and still misinforms the patient.
- **Needs.** The setup commands.
- **Concepts.** Authority, a start event, a projection that can be a correct aggregate of the wrong clock.
- **World.** Five extracts. The mart. The sponsor’s demand for one number.
- **Do.** Write `binding.json` for the screen.
- **Local.** `repair.bind`.
- **AWS.** A note that a cloud metric has the same hole. No template.
- **Deliver.** The binding. The prediction file.
- **Check.** Practice, holdout, mini-world. Always discarding the warehouse fails the row whose label is the hospital series.
- **Breakthrough.** A reconciled report can still be the wrong promise.
- **Mastery.** The miss, if any, names the relationship and not the gold column.

## INV-02 — Whose decision

- **Purpose.** Store four decisions with their owners. The model writes none.
- **Problem.** One urgency field matches the sponsor’s sentence.
- **Needs.** INV-01.
- **Concepts.** `dec-clinical`, `dec-route`, `dec-cover`, `dec-slot`. A stop that ends a feature.
- **World.** A letter that contains clinical words. Emergency wording. A payer timeout.
- **Do.** Split the fields. Route emergency wording to a person. Leave `dec-clinical` unchanged.
- **Local.** `repair.decisions`.
- **AWS.** The state payload schema, when it arrives, has no clinical grade.
- **Deliver.** The four fields and a one-line refusal of the sponsor’s feature.
- **Check.** Holdout letters do not set `dec-clinical`. Returns still wait. Coverage timeout does not confirm a slot.
- **Breakthrough.** A disclaimer on a collapsed field does not preserve the owner.
- **Mastery.** Cumulative with INV-01.

## INV-03 — Whose write

- **Purpose.** The tool rejects a well-formed id that came from the document reader.
- **Problem.** Schema validation passes and a slot is booked.
- **Needs.** INV-02.
- **Concepts.** Capability, origin of a value, allowlist.
- **World.** A letter that contains an approval-shaped string. Two offers of one slot version.
- **Do.** Mint the capability in the coordinator path. Check it inside `book`.
- **Local.** `repair.capability`.
- **AWS.** State in the chapter, on a different example, that a workflow callback token is not this capability.
- **Deliver.** The tool and a trace.
- **Check.** Document-sourced ids do not book. A second offer does not double-book. Ain is not confirmed from a sentence.
- **Breakthrough.** A typed tool call is not a decision.
- **Mastery.** Cumulative.

## INV-04 — Whose delivery

- **Purpose.** One business key across a crash, a redelivery, and a file.
- **Problem.** Two texts, or a text for a visit the file cancelled.
- **Needs.** INV-03.
- **Concepts.** At-least-once, outbox, idempotency key, control total, poison file.
- **World.** A crash window. A repeated file id. A bad manifest. Ain’s nightly file.
- **Do.** Store the key with the operation. Quarantine a bad trailer. Keep the last good file.
- **Local.** `repair.delivery` and SQLite.
- **AWS.** Template fragment: queue, dead-letter queue, consumer. Policy pack fails a public bucket. Synth only.
- **Deliver.** The consumer test and the template fragment.
- **Check.** Redelivery does not double-book. A missing module fails. The file night does not confirm coverage before `effective_from`. A working day is Sunday through Thursday. Friday and Saturday are not counted. A holiday is an announced list, not a guess from a calendar library.
- **Breakthrough.** The queue does not owe you exactly-once.
- **Mastery.** Cumulative.

## INV-05 — Whose document

- **Purpose.** Filter before score. Bind version and hash.
- **Problem.** The quote is accurate and the asker must not see it, or the body changed under the same version id.
- **Needs.** INV-04.
- **Concepts.** Audience, in-force, in-flight version, content hash.
- **World.** `dms`, including an unauthorized circular and a lagged translation.
- **Do.** One function, `repair.cite`.
- **Local.** Token overlap is sufficient.
- **AWS.** Boundary note: a retrieved chunk in a prompt is a copy. Only public clauses are candidates for a later object store.
- **Deliver.** The function and a citation record.
- **Check.** Wrong audience and unauthorized status are not cited. Hash mismatch fails.
- **Breakthrough.** Faithfulness to the passage is not authority.
- **Mastery.** Cumulative.

## INV-06 — Whose score

- **Purpose.** Score without the label. Refuse a call the fixture does not support.
- **Problem.** The calibration row contains the answer. A small difference looks like a win.
- **Needs.** INV-05.
- **Concepts.** A leaked label. A pre-registered decision rule. Keyed fields versus prose.
- **World.** A calibration file. Counts revealed only after the rule is written.
- **Do.** Strip the label. Write the rule. On this fixture the rule’s only legal result is no call.
- **Local.** `repair.score`.
- **AWS.** None.
- **Deliver.** The rule and the scorer.
- **Check.** An input that still contains `pass` fails. Declaring a winner fails. Planted failure types are identified by ids the student cites.
- **Breakthrough.** You measured the channel that carried the label.
- **Mastery.** Cumulative.

## INV-07 — Whose signal

- **Purpose.** Page on the document the user was told.
- **Problem.** CPU is flat. The hours on the phone are yesterday’s.
- **Needs.** INV-06.
- **Concepts.** SLI, a document id, shadow traffic that must not write.
- **World.** A replay. `DocumentChanged`. A cache.
- **Do.** Change the signal. Keep bodies off the span.
- **Local.** `repair.signal`.
- **AWS.** A metric definition and a log filter in the template. The canary string is denied. Prompt text is absent.
- **Deliver.** The board definition.
- **Check.** A stale document fails a healthy host. Flushing every document fails. A shadow sentence served to the patient fails.
- **Breakthrough.** A healthy process can be the incident.
- **Mastery.** Cumulative.

## INV-08 — Whose bytes

- **Purpose.** Class the object. Compare the endpoint region to the processor region.
- **Problem.** A nearby region returns success. The bytes were restricted, or the processor record is elsewhere.
- **Needs.** INV-07.
- **Concepts.** Restricted and public. Shared responsibility. Endpoint versus execution. `sa-east-1` is not a Kingdom code.
- **World.** Fixtures: a letter, a national id, a quotation, a public leaflet. A call record whose processor region differs. A call record whose processor region matches and whose bytes are still restricted.
- **Do.** `repair.boundary`. A template with no model resource.
- **Local.** The class function, and the promotion directory from [the local document](07_Local_Implementation.md).
- **AWS.** The template in [the AWS document](08_AWS_Implementation.md). Synth and policy pack.
- **Deliver.** The binding, the template, the policy output.
- **Check.** Restricted fixtures are absent from the asset list. A matching processor region does not admit them. A public bucket, a wildcard, a plaintext secret, or a model resource fails.
- **Breakthrough.** The region dropdown is not a data path, and a matching processor is not permission.
- **Mastery.** Cumulative.

## INV-09 — Different nouns

- **Purpose.** Apply the same binding shape where the previous names do not exist.
- **Problem.** A short symptom log from a second desk.
- **Needs.** INV-08.
- **Concepts.** Transfer. A handoff a person can use.
- **World.** A new projection. Column names from INV-01 are absent.
- **Do.** Fill a blank binding. One code change. A handoff record: intent, what was tried, what is unresolved, a next step a human may override.
- **Local.** The same package.
- **AWS.** A boundary note, unless the symptom is a bucket or a call.
- **Deliver.** The binding and the handoff.
- **Check.** The new holdout. A solution that only renames Access Office columns fails. An invented `dec-clinical` on the handoff fails.
- **Breakthrough.** The questions transfer. The previous answers do not.
- **Mastery.** The cumulative suite, plus this pack.
