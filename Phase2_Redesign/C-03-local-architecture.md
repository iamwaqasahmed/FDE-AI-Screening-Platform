# C — Local architecture

The laptop is the system of record for learning. AWS is a later trust boundary, not a second copy of every function. The local stack is what a student can run, test, and hand to the checker with no account and no GPU.

## Shape

Two processes.

1. **The world.** The simulator from document B. It is started, not written, by the student. It exposes the projections, the clock, and the inherited assistant.
2. **The student’s service.** A small Python package. Each gate replaces one module and adds one test file. The package grows. It is not rewritten every lesson.

```text
world (simulator)                student service
  event log                        policy
  projections  <-- HTTP / files -- tools (allowlisted)
  fault schedule                   workflow table + outbox
  gold (closed)                    session store
                                   citation index
                                   decision records
```

The policy decides. Tools perform. The model, when one is used, returns a dialogue act from a closed set. It does not import `book` or `return`.

## Technology choices

| Job | Choice | Rejected | Why the rejection holds |
| --- | --- | --- | --- |
| Language | Python 3.12 | A second language on the core path | The cohort is mixed. One language keeps the checker honest |
| HTTP | The standard library, then a thin framework if a gate needs routes | A full web framework on day one | The first gates are decisions and files. A framework arrives with the service |
| Store | SQLite, one file, WAL | Postgres as a requirement | Transactions are the lesson. SQLite has them. Postgres is the extension when the student turns on Docker |
| Workflow | A table: state, event id, outbox row, same commit | Temporal, Restate, or DBOS as an install | Those products are the comparison card. A retried activity can still run twice. The idempotency key lives on the tool |
| Model | A fixture that reads the pack | A live API on the mastery gate | The checker must be stable. An optional live lab exists and is not the score |
| Embeddings | A token cosine over the pack | A hosted embedding API | The pack is small. The lesson is the filter and the hash, not the vendor index |
| Search | Reciprocal rank fusion in one extension lab | A vector database product on the core path | Scores from keywords and cosines do not share a scale. Fusion is the extension. The core gate is the pre-filter |
| Messages | Files and HTTP, with a recorded accept and a recorded delivery | A broker on the laptop | The crash between send and insert is visible without Kafka |
| Faults | The simulator’s schedule | Toxiproxy on the mastery path | Same idea, fewer moving parts. Toxiproxy is an extension, jitter off if it is graded |
| Tests | pytest, Hypothesis for the calendar, JSON Schema for the reply | Promptfoo as the blocking gate | A snapshot of “the visit is booked” is the wrong contract |
| Time | The case clock passed in | `sleep`, and the wall clock | Phase 1 found the receipt test sleeping for the old delay |
| Containers | Optional, for the promotion lab | A cluster install | The promotion bundle is directories, a digest, and a non-root user. `kind` is a distinction |

## The modules the student owns

Keep them small. One file, one reason.

| Module | Responsibility |
| --- | --- |
| `policy` | Next state from a dialogue act. No write tools imported |
| `capability` | The coordinator’s decision mints a token bound to one referral and one action. The tool checks it |
| `workflow` | Idempotency, calendar, criteria pin, compensation, dead letter |
| `outbox` | The business row and the outgoing message commit together |
| `files` | Control total, poison quarantine, repeat file id, last good file |
| `session` | Session id independent of the subject. Step-up changes the assurance level |
| `authz` | Patient A does not read patient B. A service client does not read as the patient |
| `contract` | The mart’s date starts at booking. The figure is not a patient quote |
| `channel` | Window open or closed. Accept is not delivery |
| `identity` | Deterministic partition. Splink is a note, not an install, on this file |
| `cite` | Audience and status before score. Version pin. Hash. Text equals the clause |
| `eval` | Scores against gold. The judge may not read `pass` |
| `guard` | Allowlist and residency. A missing family label still holds |
| `privacy` | Deletion map: row, memory, index, logs, backups named. Retention holds named |
| `observe` | Spans for the tool and the document id. CPU is present and is not the incident |
| `serve_sim` | Discrete events: static batch, continuous batch, chat reserve. Numbers are scenario knobs |
| `promote` | Digest, signature check, secret scan, live versus ready |
| `drill` | Hypothesis, one fault, idempotent resume |
| `aws_boundary` | A document, then a template: which bytes may leave |

## Validation

Every gate has three checks, and only the first is required to open the next lesson.

1. **Behavior.** The world ends in the required state. Miss text does not contain the gold value, the watermark, or the national-id fixture.
2. **Decision.** A short record: what arrived, what decided, what was refused, what was written, which case id. The checker looks for the ids and the refusal. It does not score prose style.
3. **Regression.** Previous behavior checks stay on. A fix that re-opens booking-from-a-letter fails.

Extension labs add a fourth check, one mechanism. Skipping it does not lock the next gate. The capstone cannot claim the lab.

## What “production” means on a laptop

A promotion directory the hospital side will accept:

- full SHA-256 of the artifact, not a prefix
- a non-root user and the restricted-profile fields written as data, even though no cluster is running
- `/health/live` returns 200 while weights are absent
- `/health/ready` stays unavailable until the loaded digest matches the register
- logs are an allow-list. The logger is not handed the national-id fixture
- a clear-text token fails the copy into the hospital directory
- a keyless signature fails closed. Running a public transparency log is not the assignment

The student can explain what a real admission controller would still have to enforce. The laptop does not pretend to be that controller.
