# 03 — The brief

[Chapter 02](02-the-role.md) named the five parts. This chapter is the file drop. You open ten files, in order, and then you run one demo. You do not paste a file on this page. There is no heading on this page that starts with Replace.

The blocks under Read these files are pictures. They replace nothing. Do not paste them. A picture belongs to the numbered item above it. The next item starts with the next number. A jsonl row is one long line. Word wrap can make that line look like several lines. It is still one row. A csv row is one line.

Open each link with Ctrl+click on Windows or Command+click on macOS, so the file opens in the editor. Do not double-click the file in File Explorer. A double-click can open Excel or a browser, and the search below will not match what you see. To search, Ctrl+F on Windows or Command+F on macOS, inside the file named in that item. A search inside this chapter does not count. Do not type in a packet file. Close it when the item is done.

Stay on the list until item 10. Then run the demo. Finish one item before you open the next number. If you are lost, you are on the item you have open. Finish that item.

## Read these files

1. Open [release/README.md](packet/release/README.md). Search for `2027-01-28`. That line is the case date. The list under it is today's drop. This item is done when you have seen the case date and the nine links. Close the file.

2. Open [rehearsal.md](packet/release/notices/rehearsal.md). Search for `sponsor`. The next block is a picture of that file. Do not paste it. This block replaces nothing.

```text
# Rehearsal brief

Steering asks for the client requirements. The file is rcp/requirements.md. A list that repeats the sponsor sentence is not a brief.

The price sheet and the annotation budget are in this pack. The second run is scored on slices/before.jsonl. Labels stay on the grading service.

Case date: 2027-01-28.
```

This item is done when you can say the client requirements file is `rcp/requirements.md`, and a list that repeats the sponsor sentence is not a brief. Close the file.

3. Open [steer-m03-l05.md](packet/release/steering/steer-m03-l05.md). Search for `second`. The next block is a picture of that file. Do not paste it. This block replaces nothing.

```text
# steer-m03-l05

The steering committee asks these questions. The committee is cdo, med-dir, dpo, ciso, and finance.

1. What did the second run change?
2. What will the client requirements include, and what is a non-goal?
3. Which stage gate applies, and what is the risk tier?
4. What does the improvement cost, in labels or GPU hours?
5. What will you not copy from the sponsor sentence?
```

This item is done when you have read all five questions. Close the file.

4. Open [role-cards.md](packet/release/workshop/role-cards.md). Search for `cdo`. The next block is a picture of that file. Do not paste it. This block replaces nothing.

```text
# Role cards

ws-access seats. Hidden answers stay in the interview.

## cdo

Layla Al-Harbi, Chief Digital and Transformation Officer.

The virtual front desk, including triage, goes live before Ramadan.

One front door for every hospital. Live before Ramadan.

## access-mgr

Noura Al-Qahtani, Director of Patient Access.

No-shows dominate the cost.

Shorter waits. A quieter contact center.

## phc-lead

Dr. Hassan Al-Dosari, PHC network lead.

Hospitals return referrals arbitrarily.

Fewer returned referrals. A template the PHCs can trust.

## dpo

Sara Al-Mutairi, Data Protection Officer.

Patient data needs care.

Patient data stays in the private cloud. Training data stays here too.
```

The first line under `cdo` is the sponsor sentence. You read it here. You do not copy it into `rcp/requirements.md`. This item is done when you have seen the four seat ids: `cdo`, `access-mgr`, `phc-lead`, and `dpo`. Close the file.

5. Open [stage-gate.md](packet/release/gates/stage-gate.md). Search for `risk`. The next block is a picture of that file. Do not paste it. This block replaces nothing.

```text
# pol-stage-gate

Six gates:

- G0 intake
- G1 risk tier
- G2 DPIA
- G3 pilot approval
- G4 go-live
- G5 post-launch review

G1 is the risk tier.
```

That file does not name the citation requirement. The requirements page you write later is a different file. This item is done when you can say which line names the risk tier. Close the file.

6. Open [prices.csv](packet/release/finance/prices.csv). Search for `cost.label`. A csv row is one line. The next block is a picture of the header only. Do not paste it. This block replaces nothing. The amounts stay in the file. Do not copy an amount onto a page.

```text
key,sar
```

Find the row whose key is `cost.label`. Read the sar on that row from the file. This item is done when you have found that row. Close the file.

7. Open [labels.json](packet/release/budget/labels.json). Search for `price`. The file has two keys, `price` and `sar`. This item has no picture. A picture would copy the numbers, and the numbers stay in the file. Do not copy them onto a page. The `price` key is not `cost.label` from the previous file. Chapter 06 uses `cost.label` as the price of one label. This file's `sar` is the budget that spend is not allowed to pass. The two amounts are different. This item is done when you have seen both keys and you have not treated them as the label price. Close the file.

8. Open [before.jsonl](packet/release/slices/before.jsonl). Search for `hours-c1`. A jsonl row is one long line. Word wrap can make it look like several lines. It is still one row. The file has outputs and no label field. The file has more rows. Several of them repeat the first line. The next block is a picture of two rows from that file. Do not paste it. This block replaces nothing.

```text
{"doc_id": "circ-ramadan", "span": "hours-c1"}
{"doc_id": "circ-ramadan-unauth", "span": "hours-c1"}
```

One of those document ids is not in force. The grading service holds the labels. This item is done when you have seen both document ids and you have not found a label field. Close the file.

9. Open [personal.jsonl](packet/release/slices/personal.jsonl). Search for `asker`. A jsonl row is one long line. The next block is a picture of that file. Do not paste it. This block replaces nothing. The file has no keep field.

```text
{"asker": "patient", "audience": "patient", "doc_id": "circ-ramadan", "kind": "citation", "version": "v4"}
{"asker": "patient", "audience": "staff", "doc_id": "prep-staff", "kind": "citation", "version": "v2"}
{"floor": 0.8, "kind": "metric", "name": "citation", "value": 0.9}
{"floor": 0.8, "kind": "metric", "name": "citation", "value": 0.5}
```

A citation row has `asker`, `audience`, `doc_id`, `kind`, and `version`. A metric row has `floor`, `kind`, `name`, and `value`. This item is done when you have seen both shapes. Close the file.

10. Open [seed.json](packet/release/backlog/seed.json). Search for `story_id`. The next block is a picture of that file. Do not paste it. This block replaces nothing.

```text
[
  {
    "story_id": "p-triage",
    "title": "Set clinical urgency"
  },
  {
    "story_id": "vendor-bot",
    "title": "Replace the contact center with the vendor bot"
  },
  {
    "story_id": "req-cite",
    "title": "Cite the in-force document"
  }
]
```

This item is done when you have seen the three story ids. Close the file.

## Run the demo

The build in chapter 01 left a terminal inside `problem_simulation`. Use that window. If you closed it, open a terminal in the course folder, run `cd problem_simulation`, and then the python line. If that window is already inside `problem_simulation`, skip the `cd` line. That block is a command, not a picture.

```text
cd problem_simulation
python -m alwaha.demo.brief --profile practice
```

## You should now see

Two lines, and nothing else:

```text
the sponsor asks for triage in the front desk
the dpo keeps patient data off ext-large
```

The demo does not print `p-triage`. It does not print a price. If you see more lines, or a traceback, you are not in `problem_simulation`, or the build in chapter 01 did not finish. Run the build command from chapter 01, then run the demo again.

## What you are deciding

The sponsor sentence on the CDO card is not the brief. One retrieval failure is the failure you move. The other three planted failures stay open. Urgency stays with a clinician. Patient data stays off `ext-large`.

This page is done when item 10 is done and the demo printed those two lines.

Next: [04 — Words](04-words.md).
