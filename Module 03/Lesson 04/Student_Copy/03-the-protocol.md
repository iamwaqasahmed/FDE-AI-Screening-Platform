# 03 — The protocol

[Chapter 02](02-the-role.md) named the five parts. This chapter is the file drop. You open twelve files, in order, and then you run one demo. You do not paste a file on this page. You do not run a check from this page.

To open a link, Ctrl+click it on Windows, or Command+click it on macOS. To search, Ctrl+F on Windows or Command+F on macOS, inside the file named in that item. A search inside this chapter does not count.

The blocks under Read these files are pictures. They replace nothing. Do not paste them. A jsonl row is one long line. Word wrap can make that line look like several lines. It is still one row. A csv row is one line.

Open each link with Ctrl+click on Windows or Command+click on macOS, so the file opens in the editor. Do not double-click the file in File Explorer. A double-click can open Excel or a browser, and the search below will not match what you see. Do not type in a packet file. Close it when the item is done.

Stay on the list until item 12. Then run the demo. Finish one item before you open the next number. If you are lost, you are on the item you have open. Finish that item.

## Read these files

1. Open [release/README.md](packet/release/README.md). Search for `2027-01-27`. That is the case date. The list under it is today's drop. You are done with this file when you can see the eleven names below it. Close the file.

2. Open [hidden-test.md](packet/release/notices/hidden-test.md). Search for `grading`. You should see the grading service, outputs with no labels, and the calibration subset. You are done with this file when those three phrases are on the page. Close the file.

3. Open [campaign.md](packet/release/notices/campaign.md). Search for `Read the counts`. An eye-screening campaign is announced on the case date. It starts the next month. Ophthalmology demand after that date is not last year's month. A session plan that copies last year misses the campaign. You are done with this file when you can point at the sentence that says to read the counts from the demand file.

4. Open [ab-status.md](packet/release/notices/ab-status.md). Search for `not stated`. The arms are named. The pre-registered metric is `honest_pending`. The effect is not stated. You are done with this file when you can see that sentence. You do not write which arm won.

5. Open [metrics.json](packet/release/budget/metrics.json). Search for `extraction`. The next block is a picture of that file. Do not paste it. This block replaces nothing.

```text
{
  "citation": 0.8,
  "extraction": 0.8,
  "journey": 0.8
}
```

Each name is a budget. You are done with this file when you can see extraction, citation, and journey.

6. Open [ophth.csv](packet/release/demand/ophth.csv). Search for `district`. That word is the first column. The next block is the header only. Do not paste it. This block replaces nothing. A csv row is one line.

```text
district,year,month,visits
```

Then search the same file for `,2027,2,`. Each hit is one district in February 2027. The last field on that line is visits. Read it. Then search for `,2027,3,`. Each hit is March 2027. Read the visits on those lines too. Do not copy a visit count into this chapter or into a work file. You are done with this file when both searches find rows and you have read the visits column. Close the file.

7. Open [ab-status.json](packet/release/experiment/ab-status.json). Search for `honest_pending`. The next block is a picture of that file. Do not paste it. This block replaces nothing. The notice says the effect is not stated. You do not write which arm won.

```text
{
  "arms": [
    "clause",
    "short"
  ],
  "counts": {
    "clause": {
      "contained": 30,
      "honest_pending": 48,
      "n": 80
    },
    "short": {
      "contained": 55,
      "honest_pending": 40,
      "n": 80
    }
  },
  "metric": "honest_pending"
}
```

You are done with this file when you can see `metric` and the two arm names. You are not asked to decide a winner on this page. The comparison you will write later uses `honest_pending` only. Close the file.

8. Open [score.jsonl](packet/release/slices/score.jsonl). Search for `photo`. A jsonl row is one long line. The next block is a picture of that file. Do not paste it. This block replaces nothing. The file has outputs. It has no label field. Do not invent labels.

```text
{"kind": "extraction", "pred": {"source_type": "photo", "specialty": "ophth", "sub_specialty": ""}}
{"kind": "citation", "pred": {"doc_id": "", "span": ""}}
{"kind": "journey", "pred": {"approved": false, "state": "pending"}}
```

You are done with this file when you can name the three kinds and you can see that none of the lines contains a label.

9. Open [failures.jsonl](packet/release/slices/failures.jsonl). Search for `log-night`. A jsonl row is one long line. The next block is a picture of that file. Do not paste it. This block replaces nothing. The file does not contain the words hallucination, retrieval, reasoning, or workflow. Those names belong on the benchmark page, in chapter 09.

```text
{"log_id": "log-night", "output": "The eye clinic is open all night. Source: a clause that is not on file."}
{"log_id": "log-circular", "output": "The hours reply cites the unauthorized circular."}
{"log_id": "log-friday", "output": "The offer is Friday at 10:00, and the gender preference is ignored."}
{"log_id": "log-approval", "output": "The slot is booked. Approval: none."}
```

You are done with this file when you can read the four outputs and you have not added a type name to the picture.

10. Open [calibration.jsonl](packet/release/slices/calibration.jsonl). Search for `cal-fluent-wrong`. A jsonl row is one long line. The next block is a picture of that file. Do not paste it. This block replaces nothing. The demo does not print these answers.

```text
{"answer": "The clinic is open every night and the citation reads as settled.", "fluent": true, "item_id": "cal-fluent-wrong", "pass": false}
{"answer": "In force.", "fluent": false, "item_id": "cal-terse-right", "pass": true}
{"answer": "The in-force document is the cluster circular, and the hours match that document.", "fluent": true, "item_id": "cal-fluent-right", "pass": true}
```

The field is named `pass`. You are done with this file when the fluent row shows `false` and the terse row shows `true`. Close the file.

11. Open [seats.md](packet/release/workshop/seats.md). Search for `cdo`, then `access-mgr`, then `phc-lead`, then `dpo`. Each search is one seat. You are done with this file when all four searches hit. Close the file.

12. Open [dot-vote.json](packet/release/workshop/dot-vote.json). Search for `p-triage`. The next block is a picture of that file. Do not paste it. This block replaces nothing. The ranking puts `p-triage` first, then `vendor-bot`. That ranking is not the value model.

```text
{
  "method": "dot-vote",
  "ranked": [
    "p-triage",
    "vendor-bot",
    "p-status",
    "p-dna"
  ]
}
```

The first name under `ranked` is `p-triage`. The next name is `vendor-bot`. You are done with this file when you can see that order in the file. Close the file.

## Run the demo

Leave the files open if you want. The demo uses the terminal that is inside `problem_simulation`, the one from chapter 01. If that window is already inside `problem_simulation`, skip the `cd` line and run the python line. If you closed it, open a terminal in the course folder and run both lines.

```text
cd problem_simulation
python -m alwaha.demo.judge --profile practice
```

That block is a command, not a picture. If the terminal says `No module named alwaha`, this window is not inside `problem_simulation`. Run the `cd` line, then the python line.

## You should now see

Two lines, and nothing else:

```text
the judge marked the citation correct
the citation is not the in-force document
```

The demo does not print the calibration item, the span, or the doc id. If you see more than those two lines, you ran a different command. Run this one again.

## What you are deciding

The shell score reports a perfect extraction, citation, and journey. The shell forecast copies last year's months forward. The shell names every log row a pass. The shell judge marks a citation correct when it is fluent. The calibration subset shows that a fluent citation can still be wrong. You will replace those shells in later chapters. You do not replace them on this page.

This page is done when item 12 is done and the demo printed the two lines above.

Next: [04 — Words](04-words.md).
