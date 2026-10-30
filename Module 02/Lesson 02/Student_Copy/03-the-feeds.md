# 03 — The feeds

[Chapter 00](00-background.md) named Al-Waha and the front-desk wish. This chapter is the second morning of Module 2. Webhooks, WhatsApp, and the HL7 feeds arrive.

The case date on today's drop is 18 January 2027. The note is from the enterprise architect, [Huda Al-Ghamdi](packet/kickoff/personas/ea.md). Her id is `ea`. She will not promise a live slot where none exists.

## What arrived today

[feeds.md](packet/release/notices/feeds.md) says `eref` pushes `referral.submitted`. WhatsApp is open beside SMS. HL7 v2 from `h-nakhl` and `h-safra` arrives through `int-engine`. The schema registry lists the fields a consumer may trust. A field that is not listed is ignored.

[topics.md](packet/release/registry/topics.md) is that registry. Search for `referral.submitted`. The header row names the columns: Topic, Version, Owner, Required fields. On the `referral.submitted` row, the Owner cell is `eref`. Leave it there. [Chapter 09](09-finish.md) has the sentence that uses it. Search for `session.cancelled`. The Owner cell on that row is `hospital`.

[eref.yaml](packet/release/openapi/eref.yaml) has two paths. Search for `readReferral`. That path is the old poll. Search for `subscribeReferralSubmitted`. That path is the webhook subscription you will use. On Module 1, Lesson 3, `eref.yaml` also listed `decideReferral`. That path held a coordinator decision. Today's file does not list it. The coordinator decision is not today's work.

[zones.md](packet/kickoff/world/zones.md) places `h-nakhl` and `h-safra` in `zone-hospital`, and `h-wadi` in `zone-private`. [Chapter 07](07-the-pages.md) uses those placements.

[referral.submitted.json](packet/release/webhooks/referral.submitted.json) is the webhook fixture. You open it in [chapter 06](06-the-worker.md). You do not copy it into `work/`. The file carries a watermark.

## See the two lines

This command is the only one on this page that starts inside `problem_simulation`. Open a terminal in the course folder, the same way as chapter 01. If that window is already inside `problem_simulation`, skip the `cd` line and run the python line.

```text
cd problem_simulation
python -m alwaha.demo.hl7 --profile practice
```

You should see exactly these two lines, and nothing else:

```text
file order: sequence 1 stands
sequence order: sequence 2 stands
```

Open [int-engine.jsonl](packet/release/feeds/int-engine.jsonl) and look at the first two rows only. The first row has sequence 2. The second row has sequence 1. File order keeps the last of those rows, so sequence 1 stands. Sequence order sorts by the sequence number, so sequence 2 stands. The third row has no sequence. The demo does not use it. You do not copy a field from that row onto a page. The demo does not print a field name. It does not print a facility code.

Open [notes/feed-lines.md](notes/feed-lines.md). Each row already has two pipes. The cell is the empty space after the second pipe. On the File order row, type `file order: sequence 1 stands` in that cell. On the Sequence order row, type `sequence order: sequence 2 stands`. Leave both pipes on each row. The check does not read that worksheet. The label is yours: the two orders keep different sequences.

You do not write a page called `hl7.md`. The check does not read one. You do not write a page about WhatsApp. [Chapter 04](04-words.md) defines those words from the files in the packet.

## What you already decided

`wf-self-service` can report status and book inside the approval rules. Today the book call from chat waits. The new work is the subscription: take the webhook, take a cancelled clinic session, and label the mart clock the desk already distrusts.

`h-wadi` is the hospital on the private cloud. A live deploy of this assistant onto the cluster is a later day. Today the worker is named on the dev namespace, and you run it on your machine.

Next: [04 — Words](04-words.md).
