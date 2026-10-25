# 04 — The contract

Open the finished [contract.py](work/app/contract.py) and [test_contract.py](work/tests/test_contract.py) and put them beside yours.

`holds` returns true only when the status is `queued`. A status of `booked` is the live-slot fault. It does not hold. The comment above the return can still say `booked`. That is expected. The comparison the check runs is `status == "queued"`.

The test file contains the word `holds`. `test_queued_fixture_holds` stays green. `test_live_slot_fault_fails_the_contract` goes red. That second test still contains `booked` inside `assertFalse(holds("booked"))`. That is the fault. The line `parents[1]` points at the `app` folder beside `tests`.

The shell returns true for every status. While that shell is the file that runs, the individual check says `the contract test accepted the live-slot fault`. If `holds` rejects `queued`, the check says `the contract test rejected the queued booking`. If the test file is missing, or it does not contain `holds`, the check says `the contract test is missing`.

The live-slot fixture is not in this folder. The individual check reads it from the built pack. A copy in `work/` fails the check, and the message does not print the watermark.

The suite in this `work/` folder prints `Ran 11 tests` and `OK`. The packet suite, beside the shells, prints `Ran 10 tests` and `OK`. The contract test is the extra test. The suite does not read the pages.

Next: [05 — The pages](05-the-pages.md).
