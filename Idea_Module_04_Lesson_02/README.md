# Module 04 Lesson 02 — research folder

This folder is an independent curriculum proposal for **The incident** (`rel-m04-l02`). It does not change the student copy, the solution, the checks, or the pack. The course on disk still grades `chk-m04-l02-incident` and `slice-cache`.

**Thesis.** OpenTelemetry-style traces of latency are necessary and miss the actual AI incident. On 1 February 2027 the replay’s CPU stays flat at 0.2 while `referral.status` errors, and a separate failure is worse: cached clinic hours still describe the superseded circular after `circ-ramadan-hours` is in force. The lesson should teach GenAI semantic conventions (experimental), a blameless incident timeline, cache invalidation on `document.changed`, and shadow evaluation that cannot change the patient reply.

## Read in this order

| File | Job |
| --- | --- |
| `01-existing-lesson-evaluation.md` | What the lesson, the pack, the starter tests, and the two checks actually do |
| `02-industry-research.md` | Conventions, SRE timelines, drift definitions, cache, shadow safety, product examples |
| `03-redesign-architecture-and-simulation.md` | Four observability architectures and the local replay |
| `04-exercises-assessment-instruction.md` | Self-paced sequence, the runnable replay, prerequisites, how to grade |
| `05-tradeoffs-recommendations-sources.md` | What to delete, what to keep, what not to add, full source list |

A facilitator can read this file and file 05 and stop. A writer who will change the student chapters should read 01 before touching a paste fence, then 03 and 04 before replacing those fences with the replay. File 02 is the citation file: if a slide names a drift, the sentence has to match a row there. Nothing in this folder is licensed as a drop-in replacement for `Student_Copy`. Adopting it means editing the course in a later change, on purpose.

## Labels used in every file

| Label | Meaning here |
| --- | --- |
| **Proven** | A practice with a stable primary source and a failure mode this lesson can show on disk |
| **Emerging** | Used in production AI stacks, still moving, or only partly specified |
| **Experimental** | A spec marked Development, a 2025 paper, or a classroom probe that is not yet a check |

## What the current lesson already gets right

Keep these. They are the lesson’s engineering decisions, and the hidden grader already enforces them.

- The alert span is evidence, not a request. It stays out of error rate, p95 latency, and tool-failure counts. The window is five minutes from the first `referral.status` error (`2027-02-01T09:12:00+03:00`) to the alert (`2027-02-01T09:15:00+03:00`).
- A board that returns only `cpu` fails. The starter `dashboard.py` does exactly that.
- Gateway cost is a sum per hospital (`h-wadi`, `h-nakhl`, `h-safra`), and the rate is not printed on a miss.
- Cached hours change only when `topic` is `document.changed` and `doc_id` is `circ-ramadan-hours`. Another document leaves the cache.
- `reply` returns the registered pending sentence. The shadow sentence must not appear in it. `promote` returns a candidate hash only when `compared` and `matched` are both true. The pack’s `shadow-extract.json` has no `compared` field.
- The demo prints a tool, a hash, and a token count, and it does not print the error detail.
- Old hours text stays out of the pack. Gold and the patient-representative interview carry the 21:00 close. The new body is “Evening clinics close at 01:00. Daytime slots are not offered.”

## What the lesson currently teaches instead of the thesis

Chapters 05 through 09 are paste fences. The sprint, the seven modules, their tests, the timeline (including both timestamps), the dashboard sentence, the runbook, both interview notes, and the two knowledge lines are copied from the chapter into `work/`. The starter unit tests assert the traps: `test_dashboard.py` expects `{"cpu": 0.2}`, and `test_cache.py` expects the old 21:00 string to survive `document.changed`. A student who makes the starter tests pass has implemented the incident. The student is then told to replace those tests with tests that expect the fix, in the same paste as the fix.

The three names the knowledge check requires — ramadan hours, criteria v4, campaign clinic — are a label map from `kind` to a phrase. They are operational mismatches in this case. They are not the statistical trio data drift, concept drift, and embedding drift. Tool-schema drift is absent. A timeline can match the replay by containing two timestamps and the string `referral.status`, with no sentence that says the hours bug was invisible on a latency board.

## Architectures, in one pass

| Architecture | Label | What it is for on this day |
| --- | --- | --- |
| Host board (CPU, or RED latency and errors with no GenAI attributes) | Proven for services | Shows the tool outage. Misses the circular |
| GenAI spans on OpenTelemetry (Development conventions) | Experimental conventions, Proven transport | Names the model, the tool, tokens, retrieval documents, tool definitions |
| Semantic quality plane: versioned cache, shadow with no patient write, override rate | Emerging as an AI practice; the cache rule itself is Proven | Catches stale hours and a bad adapter while the patient still hears the registered reply |
| A vendor trace product (Langfuse, Phoenix, Braintrust) | Emerging products | Optional sinks. Not a dependency of the lab |

## Two failures, one morning

Failure T is the tool page. At 09:12, 09:13, and 09:14 on 1 February 2027, `referral.status` spans are errors with latencies 2400, 2600, and 2800 ms. The alert span is at 09:15. The gap is three minutes, inside the five-minute detection window in `replay/note.md`. Every span, including the alert, has `cpu` 0.2. The reference board drops the alert, then reports error rate 0.6, p95 latency 2800 ms, and three tool failures. A function that returns only `cpu` is the starter module, and the starter test expects that return value.

Failure H is the hours page. `circ-ramadan-hours` is in force and supersedes `circ-ramadan`. The new body says evening clinics close at 01:00 and daytime slots are not offered. The cache still holds the previous evening close at 21:00. No span carries a document id. Repairing p95 does not change what the phone line quotes. `slice-cache` grades one call: the real event must yield the new body, and the old sentence must not remain inside it. A decoy document is graded by the solution unit test, not by that check. The proposal treats the decoy as part of the lesson.

Shadow traffic sits beside both failures and must not be used to paper over either. The registered reply is “Your referral is still pending.” The shadow reply says the referral was accepted. The pack records no `compared` field. Promotion of the candidate hash is a third incident if it happens because a trace existed.

## The local replay

`04-exercises-assessment-instruction.md` contains a stdlib program. Save it as `replay_incident.py`. This review extracted that block and ran it.

- `python replay_incident.py` prints `replay ok`. CPU is 0.2. The SLI board is error rate 0.6, p95 2800, three tool failures, alert at 09:15. An unrelated document leaves the 21:00 sentence. The hours circular replaces it. The patient line stays the pending sentence. The uncompared hash prints empty.
- `python replay_incident.py --pack` pointed at `Module 04/Lesson 02/Student_Copy/packet/release` also prints `replay ok`. Hospital totals differ from the embedded fixture because the pack’s meter depends on the profile seed. The script does not embed that seed’s hash.
- `--break cpu`, `--break ttl`, `--break flush`, `--break shadow-reply`, `--break promote`, and `--break schema` each print `replay failed` and exit 1. `ttl` is the cache that survives the circular. `flush` is the cache that treats every document change as the hours circular. `schema` is a tool whose name and latency look healthy while the definition hash moved.

The script does not call a model, a vendor, or the grader, and it does not write into `Module 04/`.

## Decisions this proposal will not reopen

The alert stays in the replay. Students do not invent a new bug to make a page fire. Content on spans stays opt-in, in line with the Development GenAI document and with the demo that hides the error detail. An LLM judge does not set `matched`. Embedding-model upgrade papers stay on the reading list. Lesson 3 still owns the shared quota and the price change. The official pass lines stay `chk-m04-l02-incident passed.` and `slice-cache passed.`

## Deletions, short form

Remove paste-as-the-path. Remove starter tests that define the bug as success. Remove the claim that three case labels are the ML drift taxonomy. Keep both check ids, the doc-id guard, the registered reply, the five-minute window, and the decision to hide error detail.

## Five sources to open first

1. OpenTelemetry GenAI spans, status Development: https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md
2. Google SRE, Managing Incidents: https://sre.google/sre-book/managing-incidents/
3. Google SRE, Postmortem Culture: https://sre.google/sre-book/postmortem-culture/
4. Istio traffic mirroring (responses discarded): https://istio.io/latest/docs/tasks/traffic-management/mirroring/
5. Gama et al. 2014, concept drift survey: https://dl.acm.org/doi/10.1145/2523813
