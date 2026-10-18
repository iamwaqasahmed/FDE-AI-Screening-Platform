# Decisions on the record

**Days 3 and 4. Architect.** Stop and write four architecture decision records. Use [the ADR template](templates/adr.md). Save them as `adr/ADR-01.md`, `adr/ADR-02.md`, `adr/ADR-03.md`, and `adr/ADR-04.md`.

Status is `Proposed` on every one. You are not the decider. A record marked Accepted fails.

The decider is the owner of the rule or the component the decision changes. Write the person's name.

| Id | Decision | Decider | Also name |
|---|---|---|---|
| ADR-01 | Where official-sensitive captures may be hosted | The data protection officer, the sender of the Week 3 memo | `EU`, `official-sensitive`, `cloud-policy` |
| ADR-02 | The path a score takes back to the grader | The owner of `integration-engine` | The information security officer. `vendor-callback`, `integration-engine`, `grader` |
| ADR-03 | Who signs a result | The sender of the Week 6 memo | The lead grader, who acts on CSO-3. The model output is `advisory` |
| ADR-04 | The production path off the Version 01 image | The information security officer | The model from note 09. `read-only`. A `question` must not be stored |

Say what you considered and rejected. ADR-01 does not grant hospital studies to the vendor. ADR-02 does not let the callback write straight to the grader. ADR-03 does not let the model sign the result. ADR-04 does not copy the Version 01 image unchanged.

## Fill these findings

| Item | What it holds |
|---|---|
| `adr_index` | `ids`, `deciders`, `status` |

`ids` is `ADR-01` to `ADR-04`. `deciders` maps each id to the person's name. `status` is `proposed`.

**A miss that looks like progress.** "Status: Accepted." Nothing in this drop accepts a decision. The data protection officer has not written the region approval. The clinical director has not confirmed the conditions.

**Finish.** Four records, four named deciders, and not one of them accepted.

Next: [The governance pack](12-the-governance-pack.md).
