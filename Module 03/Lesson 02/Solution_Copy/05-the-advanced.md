# 05 — The advanced path

Open the finished [qlora.py](work/app/qlora.py), [domain.py](work/app/domain.py), and [prefs.py](work/app/prefs.py) and put them beside yours.

The two checks do not import these files. The suite does. Deleting them is not the fix. The packet copies are the shells. These copies are the replacements. The tests are the same bytes in both places.

## Rank

The shell spends a full LoRA rank even when the quota is smaller. It counts GPUs in steps of 8 and does not cap the need. The filled file counts in steps of 32, then takes the smaller of that need and the quota. The method is `qlora`. The requested rank is kept. Rank 32 fits one GPU.

## Domain

[ds-domain.jsonl](sources/release/domain/ds-domain.jsonl) is three lines of `text`. None of them has an item id. The shell keeps every row, including a letter. The filled file keeps a row only when `item_id` is absent.

## Preferences

[ds-prefs.jsonl](sources/release/prefs/ds-prefs.jsonl) is one `draft` and one `edited` line. The clause id is in the draft. The shell returns the draft unchanged. The filled edit expands `sugar clinic` to endocrinology, drops `Friday` and the date token `2027-03-10`, and drops the tokens `on` and a bare period. It does not call the Module 1 calendar. The word `the` stays, so the line reads `the endocrinology`. That wording is what the test expects. The clause id stays. `Friday` remains on the replace line. That is expected.

The suite from this `work/` folder prints `Ran 12 tests` and `OK`.

## The path through the files

The morning chapter [08-the-advanced.md](../Student_Copy/08-the-advanced.md) has the section How the replacement works. That section is the path through the files this page compares. Read it beside the finished file. The notes above are the decisions the check names.

Next: [06 — The pages](06-the-pages.md).
