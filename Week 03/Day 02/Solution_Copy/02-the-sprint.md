# 02 — The sprint

Open the finished [sprint.md](work/sprint.md) and put it beside yours.

[ruling.md](sources/release/notices/ruling.md) says the ruling is signed and a cloud fine-tune is closed. The baseline comes first, because the prompt is scored before an adapter is served. The adapter comes next, then the register, then the memo.

The Order section is two sentences. The first says the baseline, then the adapter, then the register, then the memo. The second says the cloud fine-tune is closed. The check looks for baseline, adapter, register, and memo, in that order. It uses the first time each word appears. It also looks for the sentence that the cloud fine-tune is closed. It does not print those words.

The blank sprint has the heading and an empty section. While that blank is the file that runs, the check says `sprint.md does not sequence the adapter`.

Next: [03 — The baseline](03-the-baseline.md).
