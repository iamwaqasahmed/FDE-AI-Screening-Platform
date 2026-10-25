# 10 — Finish

Two actions. Replace `knowledge.md`. Run three commands. You are done when each command prints `passed`.

The checks grade the cluster job, the dates, the clinic codes, the relabel, the sample, the scan, the sprint, the patient page, the class table, and the shape of `knowledge.md`. The sentences in `knowledge.md` are still part of done. The checks do not read an interview note. They do not import `pit.py` or `budget.py`. Leave those two files in place.

Use the failure table at the bottom only when a check fails. It is not more work. Do not run `prepare_work.py` on this page unless a row in that table tells you to. A second run erases the files you pasted.

## Do this

1. Open [work/knowledge.md](work/knowledge.md). The full path is `Week 03/Day 01/Student_Copy/work/knowledge.md`. It sits beside `sprint.md`. It does not go inside `work/app`, and it does not go inside `packet/`. If the file is missing, create it in that `work` folder. On Windows the name sometimes becomes `knowledge.md.txt`. Click the name and remove `.txt`. If you cannot see `.txt`, in File Explorer open View and tick File name extensions, then rename the file so the name ends in `.md` only.

   Select the whole file and delete it. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. Paste. Save. These are the finished sentences.

```text
# Knowledge

1. A row count is not a patient count because a mother and a newborn can share a national id, twins can share a phone, and an MRN can be reused.
2. A fidelity card compares a synthetic sample with the real specialty mix, the phrase frequencies, and the label margins.
```

Open [work/knowledge.md](work/knowledge.md). Search inside that file, not inside this chapter. You should see two numbered lines. Line 2 contains `fidelity`. If the search fails, you pasted into the wrong file. The path has to contain `Student_Copy\work`. On macOS it shows as `Student_Copy/work`.

2. Open a terminal in the course folder, the same way as chapter 01. `dir` should list `problem_simulation` and `Week 03`. If chapter 01 told you to use `py`, use `py` here. If that window is already inside `problem_simulation`, skip the `cd` line and run the python lines.

```text
cd problem_simulation
python -m alwaha.check identity --release rel-w3d1 --work "../Week 03/Day 01/Student_Copy/work" --profile practice
python -m alwaha.check labels --release rel-w3d1 --work "../Week 03/Day 01/Student_Copy/work" --profile practice
python -m alwaha.check synthetic --release rel-w3d1 --work "../Week 03/Day 01/Student_Copy/work" --profile practice
```

## You should now see

```text
chk-w3-identity passed.
chk-w3-labels passed.
chk-w3-synthetic passed.
```

Each command prints its own line. Wait for one line before you start the next command. You need all three. `work/knowledge.md` has both answers. The first says a row count is not a patient count because a mother and a newborn can share a national id, twins can share a phone, and an MRN can be reused. The second says a fidelity card compares a synthetic sample with the real specialty mix, the phrase frequencies, and the label margins.

If you see those three `passed` lines, skip the table below and go to Done.

## If a check fails

A failed check prints `failed`, then one or more lines that start with a dash. The words after the dash are what you look up in the left column below. Do what the right column says. Then run the command again. A line can say a mother and a newborn were merged, twins were merged, a reused MRN was linked, a Hijri month boundary is off by a day, the stale clinic code was kept, or a row count was used as a patient count. It can also say the clusters do not match, a job did not run, a page is missing a fact, a phone photo is still a scan, the sample misses the fidelity card, or the sample contains a watermark or a national id. It does not name a national id, a converted date, or a rate. A watermark message does not print the watermark. Where a line does not name the missing fact, the row gives the file to open and the inputs that make the check pass. Then you paste the block from that chapter again, and you label what you see.

| What it prints | Where to go |
| --- | --- |
| `Build rel-w3d1 first.` | The pack or the grader's gold file is missing. From the course folder, run `cd problem_simulation` and then `python -m alwaha.build --profile practice --release rel-w3d1`. If you are already inside `problem_simulation`, skip the `cd` line. Then run the three checks again |
| `a Hijri month boundary is off by a day` | The message does not name the date. Open [identifiers.jsonl](packet/release/history/identifiers.jsonl). Search for `hijri-end`. The `dob` is `1448-07-29` and `era` is empty. Search for `hijri-start`. The `dob` is `1448-08-01`. The shell adds one day when the Hijri day is 1 or at least 29. [Chapter 06](06-the-clusters.md). Paste `dates.py` again. You should see `return _from_hijri(value).isoformat()`. You should not see `timedelta`. The date test expects 14 days from `1448-07-15` to `1448-07-29`, then 2 days to `1448-08-01`. Label that result: the boundary stayed on the civil day. Do not write the converted day on the page |
| `the date conversion did not run` | The message does not name the line. `work/app/dates.py` is missing, or the paste broke the indentation. Run `prepare_work.py` from the course folder, then paste chapters 05 through 10 again from the chapter source |
| `the stale clinic code was kept` | The message does not name the code. Open [clinics.md](packet/release/catalog/clinics.md). Before June 2024, h-wadi keeps `END-01`. On and after that date, both endocrinology codes at h-wadi are `ENDO-CLN`. [Chapter 06](06-the-clusters.md). Paste `codes.py` again. You should see `2024-06-01`. `END-01` remains in the set. That is expected |
| `the clinic code did not run` | The message does not name the line. `work/app/codes.py` is missing, or the paste broke the indentation. Run `prepare_work.py`, then paste chapters 05 through 10 again |
| `a mother and a newborn were merged` | The message does not name an id. Open the history file and search for `mother` and `newborn`. They share a national id and stay two people. The demo's fourth line says the two MRNs stay two people. [Chapter 06](06-the-clusters.md). Paste `cluster.py` again. You should see `newborn` on the skip line |
| `twins were merged` | Search the history file for `twin-a` and `twin-b`. They share a phone and stay two people. Paste `cluster.py` again. You should see `twin` on the skip line |
| `a reused MRN was linked` | Search the history file for `reuse-a` and `reuse-b`. The MRN matches. The people stay apart. Paste `cluster.py` again |
| `a row count was used as a patient count` | The message does not name the number. `patient_count` has to count groups. Paste `cluster.py` again. You should see `return len(partition(rows))`. You should not see `return len(rows)` |
| `the clusters do not match` | The message does not name the groups. Open the history file. A shared phone is not a link. `merge_with` is not a link. `replaces` is a link. A failed check digit stays a person. Search the waitlist for `death-late` and `seen-elsewhere`. Those two are the removal proposals. Paste `cluster.py` again. You should see `death-late`. Then label the rows you opened: who stayed apart, and which flags were proposals |
| `the cluster job did not run` | The message does not name the line. `work/app/cluster.py` is missing, or the paste broke the indentation. Run `prepare_work.py`, then paste chapters 05 through 10 again |
| `patients.md does not define one patient` | The message does not name the missing word. [Chapter 09](09-the-pages.md). The page needs `row`, `mrn`, `national`, `mother`, `newborn`, `twin`, and a reuse word. Paste `patients.md` again. One patient is not one row, not one MRN, and not one national id |
| `sprint.md does not sequence the cluster job` | The message does not print the four words. [Chapter 05](05-the-sprint.md). The page needs cluster, then relabel, then sample, then scan, and it needs adjudication. Paste `sprint.md` again |
| `a phone photo is still a scan` | The message does not quote the letter. Open [ann-v2.md](packet/release/guidelines/ann-v2.md). Phone or photo in the text is source type photo. [Chapter 07](07-the-sample.md). Paste `labels.py` again. You should see `photo`. The word `scan` can remain on the line for a real scan. That is expected |
| `a sub-specialty is still blank` | The message does not name the specialty. ann-v2 fills retina and pediatric from the text. Paste `labels.py` again. You should see `retina` and `pediatric`. Blank stays when the text names neither. That is expected |
| `the sample still follows ann-v1` | [Chapter 07](07-the-sample.md). Paste `labels.py` again. You should see `ann-v2`. You should not see `ann-v1` in the work file |
| `the relabel did not run` | The message does not name the line. `work/app/labels.py` is missing, or the paste broke the indentation. Run `prepare_work.py`, then paste chapters 05 through 10 again |
| `the synthetic sample misses the fidelity card` | The message does not print a rate. Open [fidelity.json](packet/release/cards/fidelity.json). Read `sample_size`, `rare_sub_specialty`, `specialty_mix`, `phrase`, and `label_margin`. [Chapter 07](07-the-sample.md). Paste `synthetic.py` again. You should see `rare_sub_specialty`. You should not see `letters[:1]`. Label the card: the sample has to sit inside those bands |
| `the synthetic sample contains a watermark` | The message does not print the watermark. The sample copied a real letter, or the scan accepted the mark. Paste `synthetic.py` and `scan.py` again from chapter 07. In `scan.py` you should see `CANARY-`. Do not copy the clerk file into `work/` |
| `the synthetic sample contains a national id` | The message does not name the id. The sample copied a history id, or the scan accepted one. Paste `synthetic.py` and `scan.py` again. Do not type a history id into either file. `clerk-row` in the tests is a stand-in. That is expected |
| `the synthetic sample did not run` | The message does not name the line. `work/app/synthetic.py` is missing, or the paste broke the indentation. Run `prepare_work.py`, then paste chapters 05 through 10 again |
| `the scan did not run` | The message does not name the line. `work/app/scan.py` is missing, or the paste broke the indentation. Paste `scan.py` again from chapter 07. You should see `CANARY-` |
| `the classification note is missing` | The message does not name the missing cell. [Chapter 09](09-the-pages.md). `classes.md` needs a table whose header has field and class. The rows are national id, date of birth, name, and phone, each in class phi. The note needs the word scan. Keep the pipe characters. Paste `classes.md` again |
| `knowledge.md needs two answers` | Paste the block above again. Two numbered lines, each with words after the number. A second sentence on the next line does not count |
| `knowledge.md does not say why a row is not a patient` | The message does not name the missing fact. Line 1 of the block above says a mother and a newborn can share a national id, twins can share a phone, and an MRN can be reused |
| `knowledge.md does not say what a fidelity card compares` | Line 2 of the block above says a fidelity card compares a synthetic sample with the real specialty mix, the phrase frequencies, and the label margins |
| `a watermarked sample is in the work directory` | A copy of the clerk file, or another file that carries the mark, is under `work/`. Delete that copy. Leave the clerk file in the built pack. The message does not print the watermark. Do not delete `pit.py` or `budget.py` |
| `The system cannot find the path specified` or `No such file or directory` on the `cd` line | This window is already inside `problem_simulation`. Skip the `cd` line and run the python lines |
| `SyntaxError` or `IndentationError` | Run `python "Week 03/Day 01/Student_Copy/prepare_work.py"` from the course folder. Then paste chapters 05 through 10 again from the chapter source. Do not repair the spaces by hand |

## Done

The day is done when the three checks print `passed` and `work/knowledge.md` answers both questions.

Keep `work/`. The solution copy, when you receive it, is how you compare your pages with a finished set. Leave `problem_simulation/build` closed.
