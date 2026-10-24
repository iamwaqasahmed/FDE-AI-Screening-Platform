# The check

From `problem_simulation`, with your work directory filled in:

```text
python -m alwaha.check identity --release rel-w3d1 --work "..\Week 03\Day 01\work"
python -m alwaha.check labels --release rel-w3d1 --work "..\Week 03\Day 01\work"
python -m alwaha.check synthetic --release rel-w3d1 --work "..\Week 03\Day 01\work"
```

`chk-w3-identity` scores the cluster job, the dates, and the clinic codes. A miss says a mother and a newborn were merged, twins were merged, a reused MRN was linked, a Hijri month boundary is off by a day, the stale clinic code was kept, or a row count was used as a patient count. It does not name a national id or a converted date.

`chk-w3-labels` scores the relabel. A miss says a phone photo is still a scan, a sub-specialty is still blank, or the sample still follows ann-v1.

`chk-w3-synthetic` scores the sample, the scan, and the classification note. A miss says the sample misses the fidelity card, contains a watermark, or contains a national id. It does not print the watermark, a rate, or a national id.

A watermarked file copied into `work/` fails the check. The message does not print the watermark.

On `practice`, the instructor can show the false merge:

```text
python -m alwaha.demo.merge --profile practice
```

Then write `work/knowledge.md` from [templates/knowledge.md](templates/knowledge.md), with two short answers:

1. Why is a row count not a patient count?
2. What does a fidelity card compare?

The day is done when the three checks print `passed` and the knowledge file has both answers.
