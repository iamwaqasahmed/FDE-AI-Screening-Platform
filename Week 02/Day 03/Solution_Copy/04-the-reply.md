# 04 — The reply

Open the finished [schema.py](work/app/schema.py), [test_schema.py](work/tests/test_schema.py), and [test_journey.py](work/tests/test_journey.py) and put them beside yours.

`schema_ok` is true when `intent` is a non-empty string. An empty sentence with `intent` set to `status` passes. A sentence with no `intent` fails. The words `The visit is booked` are still on that failing line. `schema_ok` does not trust them.

`journey_ok` deletes the reply and returns `booked` from the state. The sentence is not the result.

The journey test loads the fixture from `data/rel-w2d3/fixtures/model.json`. That file stays in the pack. It is not in this `work/` folder. The loaded text still starts with `The visit is booked`. `journey_ok` does not read that sentence. The state on that call has `booked` false, so the result is false. A second call has an empty sentence and `booked` true, so the result is true.

The shell `schema_ok` is true when the sentence is non-empty. The shell `journey_ok` ignores the state and looks for the word booked in the sentence. While that shell is the file that runs, the tests check says `the reply schema is missing` and `the journey followed the sentence`. Neither message names a field.

[pol-assistant-use.md](sources/kickoff/corpus/pol-assistant-use.md) keeps the watermark out of prompts and out of the work you submit. The fixture carries that watermark. The check message does not print it.

Next: [05 — The receipt](05-the-receipt.md).
