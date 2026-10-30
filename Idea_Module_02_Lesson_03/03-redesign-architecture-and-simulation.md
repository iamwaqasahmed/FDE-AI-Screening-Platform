# 03 — Redesign, architecture, and simulation

## `[ALT-A]` Layered pytest (recommended)

| Layer | Asserts | When |
| --- | --- | --- |
| Examples | Two calendar dates; empty text with `intent`; sentence with no `intent`; three receipt points | `[GATE]` |
| Properties | Working-day membership and exact count; receipt purity | `[GATE]` |
| Schema | JSON Schema on the reply; `pending`↔202 and `due`↔200 | `[GATE]` |
| Recorded journey | Pack fixture, no network; state `booked` or `delegate`; `text` unread | `[GATE]` |
| Seeded mutant | Switch on; suite red; receipt stays `pending` | `[GATE]` |
| Usability rubric | CDC length, one action, control name; caregiver `delegate` | `[GATE]` via `chk-ux` |
| Live model | promptfoo, cache, `is-json`, no `equals` | `[NIGHTLY]` |
| mutmut, Hijri, `phone-only` | Killed mutants; weekend exclusion; outcome `callback` | `[NIGHTLY]` |

`now` is an argument. The test reads `minutes` from `receipt.json`. A freezer appears only if a later function calls `datetime.now`. `MODEL_GATE=recorded` fails the push if a socket opens. Live is `workflow_dispatch` plus a weekly run: `npx promptfoo@latest eval --fail-on-error`. `[DELETE]` the frozen-workflow rule. Push runs `pytest -m "not live"`.

## `[ALT-B]` Pact for the receipt

Consumer tests record GET → 202 pending and GET → 200 due. Provider state `receipt-late` forces pending after the interval. The partner verifier replays them. The reply schema stays in pytest: Pact’s FAQ says a schema is not a pact. Calendar properties and the rubric stay as in `[ALT-A]`.

Choose `[ALT-B]` when a real SMS vendor verifies. A pact copied from `sms.yaml` marks the author’s own exam.

## `[ALT-C]` promptfoo as the whole suite

Every check becomes a promptfoo case, and the GitHub Action is the only CI. Reject this as the day-one gate. The cache makes a live call look stable. Calendar math does not need a model. Students will `equals` the watermarked sentence. An `llm-rubric` as the blocking check on `status-short` is OpenAI’s “it seems to work” anti-pattern. promptfoo belongs inside `[ALT-A]` as the nightly live gate.

## Simulation (proposal only)

`[REPLACE]` `chk-tests` still probes the three functions and runs student pytest with `live` off. A missing property, a schema miss, or a pass/fail taken from `reply["text"]` is a miss. Miss text still hides the interval, the delay, and the due dates.

`[REPLACE]` The sleep miss is an AST check for `time.sleep`, `asyncio.sleep`, or a numeric wait in the receipt module or its test. A comment may contain the word.

`[REPLACE]` `chk-ux` scores the two replies: CDC band, one imperative, a control name, caregiver `delegate` and not booked. `yes` with no reply is the unfinished-script miss. Clause ids are the rubric’s rule names. `phone-only` stays out.

`[KEEP]` Watermark and a copied `model.json` fail closed. `[KEEP]` the two demo lines, the zone rows, and suite-before-sign-off, with sign-off meaning the rubric.

## Deletions

| Item | Why it leaves |
| --- | --- |
| Finished tests as the whole lab | The check never runs three of them |
| Calling `journey_ok` a booking walk | The test supplies the state |
| Usability graded only on `yes` | No message is measured |
| Substring ban on `sleep` | A warning fails; a `wait` can pass |
| Frozen `ci.yml` | The recorded gate has nowhere to live |
| `equals` or BLEU on model prose | `[DO NOT SNAPSHOT]` |
| Ghostwriter idempotence on `add_working_days` | Wrong property for a counter |
| `mutmut run` on the student Windows laptop | No `fork` |
| `phone-only` forced into the foundation table | Stays advanced |
