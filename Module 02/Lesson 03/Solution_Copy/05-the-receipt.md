# 05 — The receipt

Open the finished [receipt.py](work/app/receipt.py) and [test_receipt.py](work/tests/test_receipt.py) and put them beside yours.

[receipt.json](sources/release/clock/receipt.json) has two fields, `minutes` and `switch`. The test reads `minutes` from the pack copy of that file. It does not type the number into the file. The switch value is `receipt-late`.

[guide.md](sources/release/clock/guide.md) says to pin the case clock and advance that pinned time. The finished receipt does not wait on the wall clock. While the switch is on, `receipt_state` returns `pending`. While the switch is off, it returns `due` only after the case clock has moved by `minutes`. A clock that has not moved that far is still `pending`.

The test sends at `2027-01-19T09:00:00`. The same timestamp with the switch off is `pending`. The timestamp plus the minutes from the clock file, with the switch off, is `due`. That later timestamp with the switch on is `pending` again.

The shell returns `due` for every call. While that shell is the file that runs, the tests check says `the suite accepted the receipt fault`. The shell test waits, and the check says `the receipt test sleeps` while that wait is in the file. A result that does not follow the clock file is `the receipt test does not match the clock`. None of those messages names an interval or a delay.

The demo prints two lines and nothing else:

```text
switch off: passed
switch on: failed
```

Those lines do not print `pending`, `due`, the switch name, or a watermark. The test file does use `pending` and `due`. That is expected. The demo's second line is the switch, printed without the word pending.

[sms.yaml](sources/release/openapi/sms.yaml) says the receipt follows the case clock. A due receipt and a receipt that is still pending are different responses.

The workflow [ci.yml](work/.github/workflows/ci.yml) runs `python -m unittest discover -s tests -q`. It was copied and not edited. From `work/`, that command prints `Ran 6 tests` and then `OK` when the suite passes. The time on the `Ran` line can differ. There is no `FAIL`.

## The path through the files

The morning chapter [08-the-receipt.md](../Student_Copy/08-the-receipt.md) has the section How the replacement works. That section is the path through the files this page compares. Read it beside the finished file. The notes above are the decisions the check names.

Next: [06 — The pages](06-the-pages.md).
