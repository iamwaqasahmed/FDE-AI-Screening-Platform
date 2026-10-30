# 03 — The forecast

[Chapter 02](02-the-role.md) named the five parts. This chapter opens nine files, in order, and then you run one demo and two interviews. You do not paste a file on this page. There is no heading on this page that starts with Replace.

The blocks under Read these files are pictures. They replace nothing. Do not paste them. A picture belongs to the numbered item above it. The next item starts with the next number. Some items have no picture. Those items say so. Do not look for a block under them.

A jsonl row is one long line. Word wrap can make that line look like several lines. It is still one row. A json file is still one file when it wraps.

Open each link with Ctrl+click on Windows or Command+click on macOS, so the file opens in the editor. Do not double-click the file in File Explorer. A double-click can open Excel or a browser, and the search below will not match what you see. To search, Ctrl+F on Windows or Command+F on macOS, inside the file named in that item. A search inside this chapter does not count. Do not type in a packet file. Close it when the item is done.

Stay on the list until item 9. Then run the demo, then the two interviews. Finish one item before you open the next number. If you are lost, you are on the item you have open. Finish that item.

## Read these files

1. Open [README.md](packet/release/README.md). Search for `p-forecast`.

   There is no picture of this file. There is no block under this item. A picture would copy the rate.

   This file is done when the search finds `p-forecast` and you have read that today's price replaces yesterday's `price.ext_large_per_1k`. Do not copy the rate. The day-notes link in that file does not open. You do not need it. Close the file. The next item is number 2.

2. Open [p-forecast.json](packet/release/forecast/p-forecast.json). Search for `eye-screening`.

   There is no picture of this file. There is no block under this item. A picture would copy the backlog count or the peak time.

   This file is done when the search finds `eye-screening`. Do not copy the backlog count or the peak time. Close the file. The next item is number 3.

3. Open [price-today.json](packet/release/finance/price-today.json). Search for `replaces`.

   There is no picture of this file. There is no block under this item. A picture would copy a price.

   This file is done when the search finds `replaces`. Do not copy a price. Close the file. The next item is number 4.

4. Open [throughput.json](packet/release/serving/throughput.json). Search for `local_batched_tps`.

   There is no picture of this file. There is no block under this item. A picture would copy a tokens-per-second figure or the cold-start number.

   This file is done when the search finds `local_batched_tps`. Do not copy a tokens-per-second figure or the cold-start number. Close the file. The next item is number 5.

5. Open [public.json](packet/release/serving/public.json). Search for `public-hours`.

   The next block is a picture of that file. Do not paste it. This block replaces nothing.

```text
{
  "public-hours": "Clinic hours are on the circular."
}
```

That was a picture. Do not paste it. This file is done when the search finds `public-hours` and you have read the clinic-hours sentence. Close the file. The next item is number 6.

6. Open [mixed.jsonl](packet/release/load/mixed.jsonl). Search for `Referral`.

   The next block is a picture of that file. Do not paste it. This block replaces nothing. A row is one long line. Word wrap can make a row look like several lines. It is still one row.

```text
{"adapter": "lora-intent", "id": "chat-1", "kind": "chat", "phi": true, "text": "Where is my referral?"}
{"adapter": "lora-extract", "id": "batch-1", "kind": "batch", "phi": true, "text": "Referral letter."}
{"adapter": "", "id": "public-hours", "kind": "public", "phi": false, "text": "Clinic hours are on the circular."}
{"adapter": "", "id": "public-hours", "kind": "public", "phi": false, "text": "Clinic hours are on the circular."}
```

That was a picture. Do not paste it. This file is done when the search finds `Referral` and you have seen a phi row and a public row. Close the file. The next item is number 7.

7. Open [adapters.json](packet/release/registry/adapters.json). Search for `lora-extract`.

   There is no picture of this file. There is no block under this item. A picture would copy a hash.

   This file is done when the search finds `lora-extract`. Do not copy a hash. Close the file. The next item is number 8.

8. Open [candidate.json](packet/release/registry/candidate.json). Search for `unregistered`.

   There is no picture of this file. There is no block under this item. A picture would copy a hash.

   This file is done when the search finds `unregistered`. Do not copy a hash. Close the file. The next item is number 9.

9. Open [capacity.md](packet/release/templates/capacity.md). Search for `Serve`. The next block is a picture of that file. Do not paste it. This block replaces nothing. The seven headings inside the picture are the file's headings. They are not the next step. After the picture, the next heading is Run the demo.

```text
# Capacity

## Serve

## Batch

## Route

## Quota

## Scale

## Price

## Backlog
```

That was a picture. Do not paste it. This file is done when the search finds `Serve` and you have seen the seven headings. Close the file. The nine files are done. The next heading is Run the demo. You still do not paste a file.

## Run the demo

The demo uses the window that is still inside `problem_simulation`. If that window is already inside `problem_simulation`, skip the `cd` line and run the python line. If you closed that window, open a terminal in the course folder and run both lines.

```text
cd problem_simulation
python -m alwaha.demo.cold --profile practice
```

You should see two lines. The first line is `missed`. The second line is the cold start. Do not copy that number into a file. The lines do not include a price or the backlog count.

The prompt returns after the second line. That is the command finishing. There is no error. Do not paste the two lines.

Stay on this page. The next heading is Interview finance.

## Interview finance

Stay in that same window, still inside `problem_simulation`. If you opened a new terminal in the course folder, run the `cd` line first. If you are already inside `problem_simulation`, skip the `cd` line.

```text
cd problem_simulation
python -m alwaha.interview --persona finance --script "../Module 04/Lesson 03/Student_Copy/work/interviews/finance.questions.txt"
```

You should see `Q1:`, `Q2:`, and `Q3:`, each followed by `A:`. The command prints no score. The first answer says the line exists. The second answer says SMS and annotation labels are on the price sheet. The third answer says the external token price on today's release replaces yesterday's price, and a plan at yesterday's price is rejected. You paste the notes in [chapter 08](08-the-pages.md). Do not type into [finance.notes.md](work/interviews/finance.notes.md) on this page. The question file is not the graded note.

Stay on this page. The next heading is Interview the BI lead.

## Interview the BI lead

The same window. Skip the `cd` line if you are already inside `problem_simulation`.

```text
cd problem_simulation
python -m alwaha.interview --persona bi-lead --script "../Module 04/Lesson 03/Student_Copy/work/interviews/bi-lead.questions.txt"
```

You should see `Q1:` and `Q2:`, each followed by `A:`. The command prints no score. The first answer says the dashboard is what the board sees. The second answer says the backlog is the eye-screening campaign, not last year's month. You paste the notes in [chapter 08](08-the-pages.md). Do not type into [bi-lead.notes.md](work/interviews/bi-lead.notes.md) on this page. The question file is not the graded note.

This page is done when you have finished all nine items, the demo has printed two lines, and both interviews have printed `Q1:`. You have not pasted a file.

Next: [04 — Words](04-words.md).
