# 04 — Exercises, assessment, instruction

## Sequence

Suite first, then the rubric.

1. Read `timing.md`, `guide.md`, `receipt.json`, `sms.yaml`, `access.md`, and `scripts.jsonl`. Run the demo. Expect the two lines only.
2. Replace `calendar_count.py` so the walker uses `working_days` and `holidays`. Friday stays in `NAMES`.
3. Replace `test_calendar.py` with the two example dates and one Hypothesis test (membership, holiday exclusion, exact count). Draw 2027 dates with `st.dates`. CI: `derandomize=True`.
4. Replace `schema.py` so `schema_ok` checks the JSON Schema. `journey_ok` still reads `booked` and leaves `text` unread.
5. Replace `test_schema.py` with the empty-text pass, the no-intent fail, and an unknown-intent fail.
6. Replace `test_journey.py`. Under `MODEL_GATE=recorded`, load the pack fixture, check the schema, check `booked` false on the status state, and check `delegate` for the caregiver script. The sentence is loaded and unused.
7. Replace `receipt.py` so the switch forces `pending` and the comparison uses `minutes`. Replace `test_receipt.py`: read `minutes`; pending, due, pending-with-switch; a second call with the same arguments returns the same word. No wait.
8. Point `ci.yml` at `pytest -m "not live"`. Leave the live job untriggered.
9. Write the two replies in `usability.md`. `status-short`: short status, one named control, one next step. `caregiver`: the daughter speaking, outcome `delegate`, not a booking.
10. Name `receipt-late` on the definition of done and state that the suite is red while it is on. Keep the zone rows and the fixture note.

## Traps and checks

`[TRAP]` A sleep or wait sized to the old delay. `[TRAP]` `assertEqual` on the fixture sentence. `[TRAP]` Scripts marked finished with no message. `[DO NOT SNAPSHOT]` the watermark, a wall-clock stamp, or BLEU against one SMS.

`chk-tests` passes when the property and the examples agree with the reference walker, the schema accepts empty text with a known intent and rejects a sentence with no intent, the recorded journey follows state, the receipt matches the clock and stays pending under the switch, purity holds, and the receipt files contain no sleep or wait call. Miss text still hides the interval, the delay, and the due dates.

`chk-ux` passes when both replies pass the rubric, the four clause ids are the rules that passed, the definition of done names the switch and the red suite, both zone rows match, the fixture note names the pack and the state, the sprint lists the suite before the rubric, and CI runs the recorded suite.

Knowledge, after the suite is red on the switch:

1. A fixed sleep follows the wall clock. The receipt follows the pinned case clock, and `receipt-late` can hold it `pending`. The test advances that clock.
2. A recorded journey asserts mock state and the reply schema. The sentence is not the result. A live run is a separate gate and does not snapshot the sentence.

## Instruction

Show the demo first, and the shell sleep only as the packet picture. Before the schema work, the student names which function may ignore the model’s words. On Windows, flip the switch instead of running mutmut. A green rubric is not a caregiver study: cite CDC and Algabbani et al. Arabic for `status-short` is a `[NIGHTLY]` read. `phone-only` stays later, outcome `callback`.
