# Validation

Run on 30 October 2026 from `enterprise_simulation` with `PYTHONPATH=src`.

```text
python -m unittest tests.test_simulation tests.test_releases tests.test_adversarial tests.test_threads tests.test_lesson_access tests.test_round2_qa tests.test_round3_qa tests.test_round3_challenge
python -m access init
```

That unit command reported `Ran 68 tests in 5.684s` and `OK`. `init` printed `{"seed": "20270110", "events": 1005}`. A 2000-command stress append on a temporary database took 0.162 seconds and was then written to `var/stress.jsonl` (2000 lines). It is not part of the student pack.

What those tests actually did:

- Rebuilt the seed and got the same event ids.
- Rejected a delete on `log_hospital`.
- Read mart `wait_days` 0 on booking date 2027-01-11, and a cache with `eligible` true and `window_present` false.
- Read a CAD coverage window that starts after the file night.
- Read a payer timeout on `REF-2290` with no effective window.
- Confirmed a mother and a newborn share `604-555-0144` as two person ids, and that twins `HX-0012` and `HX-0013` share `604-555-0199`.
- Confirmed `MRN-44190` has a replacement pointer between two persons.
- Confirmed more than 400 events, a repeated Cedar Ridge file on `HX-0045`, and a Saturday nightly file `cedar-2027-01-09`.
- Confirmed the 2024 assistant screen shows wait 0, approval `APR-4417`, and close `21:00`, and that `hours-cedar-copy` stores a hash that does not match its body.
- Confirmed `student_pack` does not contain `dec-accept`, `dec-clinical`, `refused`, or the holdout tokens `APR-9991`, `sms-holdout`, `shortness of breath`, `mixed-faq`, and `cal-h1`.
- Failed a binding that cites `SlotFiled` for `since_you_asked` without naming `RequestAccepted` in the miss text.
- Failed a binding that refuses the facility-accepted label.
- Passed the sealed mapping even when the JSON contains `"pass": false`.
- Refused to grade a binding until `prediction.txt` exists.
- Served `/extracts` on localhost and confirmed the body has the mart and not `dec-accept`.
- For INV-02 through INV-08, executed a failing function and a passing function, including a delivery function that hardcodes the visible poison file and fails the holdout batch.
- Failed a handoff that contains `dec-clinical`, then passed a handoff that does not.
- The template scan failed an `AWS::Bedrock` type and `0.0.0.0/0`.
- Read THR-17 coverage starting after its file night, with the cache eligible and the window absent.
- Read INT-17: the cancel timestamp is earlier than the file and the stream revision is later.
- Read a reused desk screen code, a caller that sticks, a missing slot API, a letter download, and a break-glass row with no reviewer.
- Activated `partner-outage`, then reset back to the base event count.

Not run: a multi-hour load test, a live AWS account, `cdk synth`, or a graded daylight-saving conversion. The fall-back morning is a desk note in the channel log, not a converter. The student package `repair` is not in this tree. That is intentional.

This repository is the instructor tree. `sealed.py`, `sealed_release.py`, `sealed_holdouts.py`, and the reference functions in `tests/test_releases.py` grade the work and are not part of `student_pack/`. A learner copy should omit them. The pack itself was searched and does not contain those answers.

`python -m access reset` deletes `var/` and `student_pack/` and writes them again from the same seed. `python -m access serve --port 8088` serves the extracts. The unit test hit that view on an ephemeral port. It was not left running.
