# 7 — Local implementation

## Machine

Python 3.12. A virtual environment. SQLite. No broker, no cluster, and no GPU on the path that opens the next investigation. Docker is a distinction that repeats the INV-04 tests against Postgres. The case clock is an argument to every function that cares about time. Tests do not sleep and do not read the wall clock.

## Layout

```text
access/          simulator: append, project, serve, check
repair/          student package
var/proj/        projection files, rebuilt by project
gold/            sealed, not in the student tree
```

`python -m access.up --release INV-0N` starts the three processes and opens ports when every projector cursor has caught its own log. Cursors are per log. There is no global sequence.

## How a student works an investigation

1. Read the symptom log and the extracts.
2. Write a one-line prediction into `prediction.txt`. The check refuses to run the binding until this file exists and is non-empty. It does not score the sentence.
3. Read the chapter section that names the mechanism on a different object, including one worked procedure when the procedure is new.
4. Submit `binding.json`: field paths and role tags.
5. Run `python -m access.check --release INV-0N`.

The practice scenario can pass the naive patch. The holdout and the mini-world cannot.

## Tools the package uses

| Job | Choice | Refused on this path |
| --- | --- | --- |
| Store | SQLite, WAL | Postgres as a requirement |
| HTTP | The standard library | A web framework before a route is needed |
| Model | A fixture that returns a dialogue act | A live API on the mastery check |
| Search | Token overlap is enough to show filter-before-score | A vector database product |
| Time | The case clock | `sleep` |
| Tests | pytest. One property test where the property is the invariant | A snapshot of a sentence |
| Faults | The simulator’s fixed schedule | A proxy with random jitter on the graded path |

## Promotion bundle, local

INV-08’s local half includes a directory the hospital side would accept, even though no cluster is running:

- Full SHA-256 of the artifact.
- A non-root user recorded in the manifest data.
- Live returns success while weights are absent.
- Ready stays unavailable until the loaded digest matches the register.
- Logs are an allow-list. The logger is not given a national-id fixture.
- A clear-text token fails the copy.
- The note does not claim a statute is met.

A real admission controller would still have to enforce this. The laptop does not pretend to be that controller.
