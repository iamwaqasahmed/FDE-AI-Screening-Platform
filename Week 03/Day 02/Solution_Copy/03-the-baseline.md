# 03 — The baseline

Open the finished [prompt.py](work/app/prompt.py), [extract.py](work/app/extract.py), and [intent.py](work/app/intent.py) and put them beside yours.

## Prompt

[ruling.md](sources/release/notices/ruling.md) says patient data stays off `ext-large`. The shell serves the prompt and sends phi to `ext-large`. While that shell is the file that runs, the check says the prompt baseline is still the served model, and the call sends phi to ext-large. The message does not name the model.

The filled prompt returns false from `served` and targets `local-small` with phi false. `extract` still types every letter and leaves the sub-specialty blank. `intent` still returns `status`. That is expected. Those two functions are the weak baseline. Copying the letter relabel and the message classifier into this file makes `slice-lora` say the prompt baseline clears the slice.

## Letters

[letters.jsonl](sources/release/slices/letters.jsonl) is the dev slice. Phone or photo in the text is source type photo. The word scan, with neither phone nor photo, is scan. Retina fills retina. Pediatric fills pediatric when retina is absent. Otherwise the sub-specialty stays blank and the source type stays typed.

The shell returns an empty source type and an empty sub-specialty. While that shell is the file that runs, the check says extraction F1 is outside the budget. The message does not print an F1 or a gold label. The held-out letters are not in the release. The same rules read their text.

## Messages

[messages.jsonl](sources/release/slices/messages.jsonl) is the dev slice. An emergency phrase is checked first. Chest pain is one of those phrases, and it is on the second dev row. A status question with no emergency phrase stays status.

The shell calls every message a status question. While that shell is the file that runs, the check says intent F1 is outside the budget. The message does not print an F1 or a gold label. `return "status"` is still in the filled file, after the emergency rule. That is expected.

The same tests sit beside the shell and beside this copy. They fail on the shell. They pass here. They were not replaced.

Next: [04 — The adapter](04-the-adapter.md).
