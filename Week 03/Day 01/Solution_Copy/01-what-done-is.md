# 01 — What done is

This page is the map. The day is finished by the sprint, the date conversion, the clinic code, the cluster job, the relabel, the synthetic sample, the scan, the invite-time features, the label budget, the patient page, the class table, and the knowledge file.

Open `work/` and find each row.

| In this folder | What it is for |
| --- | --- |
| [sprint.md](work/sprint.md) | Cluster, then relabel, then sample, then scan, and adjudication. Explained in [chapter 02](02-the-sprint.md) |
| [app/dates.py](work/app/dates.py) | A Hijri month boundary stays on the civil day. Explained in [chapter 03](03-the-clusters.md) |
| [app/codes.py](work/app/codes.py) | h-wadi endocrinology follows June 2024. Explained in chapter 03 |
| [app/cluster.py](work/app/cluster.py) | A mother and a newborn stay apart. Twins stay apart. A reused MRN stays two people. Explained in chapter 03 |
| [tests/test_dates.py](work/tests/test_dates.py) | 14 days, then 2 days. A Gregorian date is unchanged |
| [tests/test_codes.py](work/tests/test_codes.py) | May keeps END-01. July at h-wadi is ENDO-CLN |
| [tests/test_cluster.py](work/tests/test_cluster.py) | The three splits, the Iqama link, and two removal flags |
| [app/labels.py](work/app/labels.py) | ann-v2 reads the text. Explained in [chapter 04](04-the-sample.md) |
| [app/synthetic.py](work/app/synthetic.py) | Four invented rows inside the fidelity card. Explained in chapter 04 |
| [app/scan.py](work/app/scan.py) | A mark or a history id is refused. A clean line is accepted. Explained in chapter 04 |
| [tests/test_labels.py](work/tests/test_labels.py) | A phone photo becomes photo, and retina is filled |
| [tests/test_synthetic.py](work/tests/test_synthetic.py) | The letter is not copied. Two rows name the rare sub-specialty |
| [tests/test_scan.py](work/tests/test_scan.py) | The mark and a listed token are refused. A clean sentence passes |
| [app/pit.py](work/app/pit.py) | Features as of the invite. Explained in [chapter 05](05-the-advanced.md). The three checks do not require it |
| [app/budget.py](work/app/budget.py) | Uncertain labels until the budget stops. Explained in chapter 05. The three checks do not require it |
| [tests/test_pit.py](work/tests/test_pit.py) | March keeps the January district |
| [tests/test_budget.py](work/tests/test_budget.py) | Price 2 and budget 6 buy three items |
| [.github/workflows/ci.yml](work/.github/workflows/ci.yml) | Runs the suite. Same bytes as the packet |
| [patients.md](work/patients.md) | One patient. Explained in [chapter 06](06-the-pages.md) |
| [classes.md](work/classes.md) | Four phi rows, and a scan before sharing. Explained in chapter 06 |
| [knowledge.md](work/knowledge.md) | The two answers. Explained in [chapter 07](07-knowledge.md) |
| [dpo.notes.md](work/interviews/dpo.notes.md) | A trainer note. The morning did not ask for an interview. The checks do not read it. Do not go back and add one |
| [dpo.questions.txt](work/interviews/dpo.questions.txt) | The questions that produced those notes. The checks do not read them |
| [coord-lead.notes.md](work/interviews/coord-lead.notes.md) | A trainer note. The morning did not ask for an interview. The checks do not read it |
| [coord-lead.questions.txt](work/interviews/coord-lead.questions.txt) | The questions that produced those notes. The checks do not read them |

The checks print `passed` when the Hijri boundary stays on the civil day, h-wadi endocrinology follows June 2024, a mother and a newborn stay apart, twins stay apart, a reused MRN stays two people, the count is people, the sprint sequences cluster then relabel then sample then scan and mentions adjudication, the patient page defines one patient, a phone photo is a photo, a named sub-specialty is filled, the guideline is ann-v2, the sample sits inside the fidelity card with no history id and no watermark, the scan refuses a mark and a history id, the class table has the four phi rows and the word scan, and both knowledge answers are present.

The clerk file is not in this folder. A copy of it here would fail the check. The message does not print the watermark. The scan reads that file from the built pack.

Next: [02 — The sprint](02-the-sprint.md).
