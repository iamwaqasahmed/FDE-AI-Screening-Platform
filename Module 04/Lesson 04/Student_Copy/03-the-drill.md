# 03 — The drill

[Chapter 02](02-the-role.md) named the five parts. This chapter opens ten files, in order, and then you run one demo and two interviews. You do not paste a file on this page. There is no heading on this page that starts with Replace.

The blocks under Read these files are pictures. They replace nothing. Do not paste them. A picture belongs to the numbered item above it. The next item starts with the next number. Some items have no picture. Those items say so. Do not look for a block under them.

A jsonl row is one long line. Word wrap can make that line look like several lines. It is still one row. A json file is still one file when it wraps.

Open each link with Ctrl+click on Windows or Command+click on macOS, so the file opens in the editor. Do not double-click the file in File Explorer. A double-click can open Excel or a browser, and the search below will not match what you see. To search, Ctrl+F on Windows or Command+F on macOS, inside the file named in that item. A search inside this chapter does not count. Do not type in a packet file. Close it when the item is done.

Stay on the list until item 10. Then run the demo, then the two interviews. Finish one item before you open the next number. If you are lost, you are on the item you have open. Finish that item.

## Read these files

1. Open [README.md](packet/release/README.md). Search for `site-b`.

   There is no picture of this file. There is no block under this item. A picture would copy a date.

   This file is done when the search finds `site-b` and you have read that site-b is the second private-cloud site. Do not copy the date. The day-notes link in that file does not open. You do not need it. Close the file. The next item is number 2.

2. Open [site-a.json](packet/release/drill/site-a.json). Search for `killed`.

   There is no picture of this file. There is no block under this item. A picture would copy a budget or a timeout.

   This file is done when the search finds `killed` and you have seen that the killed site is site-a. Do not copy a budget or a timeout. Close the file. The next item is number 3.

3. Open [replicas.json](packet/release/sites/replicas.json). Search for `site-b`.

   There is no picture of this file. There is no block under this item. A picture would copy a hash.

   This file is done when the search finds `site-b` and you have seen site-a down and site-b up. Do not copy a hash. Close the file. The next item is number 4.

4. Open [inflight.jsonl](packet/release/workflow/inflight.jsonl). Search for `apr-1`.

   The next block is a picture of that file. Do not paste it. This block replaces nothing. A row is one long line. Word wrap can make a row look like several lines. It is still one row.

```text
{"id": "apr-1", "status": "pending"}
{"id": "apr-2", "status": "pending"}
```

That was a picture. Do not paste it. This file is done when the search finds `apr-1` and you have seen two pending rows. Close the file. The next item is number 5.

5. Open [outage.json](packet/release/insure/outage.json). Search for `partner`.

   There is no picture of this file. There is no block under this item. A picture would copy a timeout.

   This file is done when the search finds `partner` and you have seen that the partner is insure and the status is down. Do not copy a timeout. Close the file. The next item is number 6.

6. Open [lead-time.json](packet/release/finance/lead-time.json). Search for `purchase_weeks`.

   There is no picture of this file. There is no block under this item. A picture would copy a module count or a date.

   This file is done when the search finds `purchase_weeks`. Do not copy the module count or a date onto a page. Close the file. The next item is number 7.

7. Open [shares.json](packet/release/hospitals/shares.json). Search for `h-nakhl`.

   There is no picture of this file. There is no block under this item. A picture would copy a price or a count.

   This file is done when the search finds `h-nakhl` and you have seen `h-safra`, `h-wadi`, and `h-ain`. Do not copy a figure. Close the file. The next item is number 8.

8. Open [model-down.json](packet/release/serving/model-down.json). Search for `status`.

   The next block is a picture of that file. Do not paste it. This block replaces nothing. A json file is still one file when it wraps.

```text
{
  "model": "down",
  "rows": [
    {
      "id": "status-1",
      "kind": "status",
      "text": "The referral is still pending."
    },
    {
      "id": "book-1",
      "kind": "booking",
      "text": "Offer a slot."
    }
  ]
}
```

That was a picture. Do not paste it. This file is done when the search finds `status` and you have seen a status row and a booking row. Close the file. The next item is number 9.

9. Open [failover.md](packet/release/templates/failover.md). Search for `Replicas`.

   The next block is a picture of that file. Do not paste it. This block replaces nothing. The five headings inside the picture are the file's headings. They are not the next step. After the picture, the next item is number 10.

```text
# Failover

## Replicas

## Drill

## Approvals

## Breaker

## Patient
```

That was a picture. Do not paste it. This file is done when the search finds `Replicas` and you have seen the five headings. Close the file. The next item is number 10.

10. Open [architecture.md](packet/release/templates/architecture.md). Search for `Rent`. The next block is a picture of that file. Do not paste it. This block replaces nothing. The four headings inside the picture are the file's headings. They are not the next step. After the picture, the next heading is Run the demo.

```text
# Architecture

## Rent

## Buy

## Deadline

## Hospitals
```

That was a picture. Do not paste it. This file is done when the search finds `Rent` and you have seen the four headings. Close the file. The ten files are done. The next heading is Run the demo. You still do not paste a file.

## Run the demo

The demo uses the window that is still inside `problem_simulation`. If that window is already inside `problem_simulation`, skip the `cd` line and run the python line. If you closed that window, open a terminal in the course folder and run both lines.

```text
cd problem_simulation
python -m alwaha.demo.drill --profile practice
```

You should see two lines. The first line is `site-a down`. The second line is `site-b serving`. The lines do not include a budget, a hash, or a price. Do not copy a budget, a hash, or a price into a file.

The prompt returns after the second line. That is the command finishing. There is no error. Do not paste the two lines.

Stay on this page. The next heading is Interview the enterprise architect.

## Interview the enterprise architect

Stay in that same window, still inside `problem_simulation`. If you opened a new terminal in the course folder, run the `cd` line first. If you are already inside `problem_simulation`, skip the `cd` line.

```text
cd problem_simulation
python -m alwaha.interview --persona ea --script "../Module 04/Lesson 04/Student_Copy/work/interviews/ea.questions.txt"
```

You should see `Q1:`, `Q2:`, `Q3:`, and `Q4:`, each followed by `A:`. The command prints no score. If the command says it cannot find the script, [chapter 01](01-setup.md) has not created `work/` yet. Run `prepare_work.py` from that chapter, then come back to this heading. The first answer says the strategy is real and the hospitals are not all on it. The second answer says site-b is the second private-cloud site and it takes over when site-a is down. The third answer says in-flight approvals live in the workflow store and they are not on the pod. The fourth answer says insure is a partner and it is not a site. You paste the notes in [chapter 08](08-the-pages.md). Do not type into [ea.notes.md](work/interviews/ea.notes.md) on this page. The question file is not the graded note.

Stay on this page. The next heading is Interview finance.

## Interview finance

The same window. Skip the `cd` line if you are already inside `problem_simulation`.

```text
cd problem_simulation
python -m alwaha.interview --persona finance --script "../Module 04/Lesson 04/Student_Copy/work/interviews/finance.questions.txt"
```

You should see `Q1:`, `Q2:`, and `Q3:`, each followed by `A:`. The command prints no score. If the command says it cannot find the script, [chapter 01](01-setup.md) has not created `work/` yet. Run `prepare_work.py` from that chapter, then come back to this heading. The first answer says the line exists. The second answer says buying GPUs takes 16 weeks and renting them does not. The third answer says a GPU purchase started on this release misses 8 February 2027 and renting meets that date. You paste the notes in [chapter 08](08-the-pages.md). Do not type into [finance.notes.md](work/interviews/finance.notes.md) on this page. The question file is not the graded note.

This page is done when you have finished all ten items, the demo has printed two lines, and both interviews have printed `Q1:`. You have not pasted a file.

Next: [04 — Words](04-words.md).
