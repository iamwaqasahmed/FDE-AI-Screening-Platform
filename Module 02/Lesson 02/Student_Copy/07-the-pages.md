# 07 — The pages

[Chapter 06](06-the-worker.md) subscribed to the webhook and to `session.cancelled`. This chapter writes what the patient sees, where two pieces sit, and the SMS line. The check runs in chapter 09. Do not run it from this page.

## Read these files

The three blocks lower on this page are the whole pages. Use a search only to see why a row says what it says. You do not take a separate note from this list.

1. [topics.md](packet/release/registry/topics.md). You already used the field list. The Owner cell on `referral.submitted` is `eref`. [Chapter 09](09-finish.md) has the sentence.
2. [session.cancelled.jsonl](packet/release/events/session.cancelled.jsonl). Three deliveries. The first is a happy text. The second is the same event. The third is the rejected receipt. The check's no-slot event is not in this file.
3. [sms-faults.json](packet/release/channels/sms-faults.json). `bkg-2` is `reject`.
4. [sms.py](packet/app/sms.py). Search for `Your booking`. That sentence names the booking id. The page you write names the booking and leaves the id off. It does not use a national id.
5. [zones.md](packet/kickoff/world/zones.md). Search for `h-nakhl`, then `h-safra`, then `h-wadi`. The first two hospitals are in `zone-hospital`. `h-wadi` is in `zone-private`.
6. [feeds.md](packet/release/notices/feeds.md). Search for `int-engine`. HL7 from those two hospitals arrives through the integration engine, so the engine sits in the zone those hospitals use.
7. [namespace.yaml](packet/deploy/namespace.yaml). Search for `wf-session-cancelled`. The worker is a container on the dev namespace, beside chat and the console. The cancellation events name `h-wadi`, the hospital in `zone-private`. The worker sits in that zone.
8. [compose.yaml](packet/compose.yaml). The same worker name is the laptop stand-in. You do not start a cluster today.

## Replace the states

Chapter 01 copied [states.md](packet/templates/states.md) to [work/states.md](work/states.md). The full path is `Module 02/Lesson 02/Student_Copy/work/states.md`. The copy already has the four state names and an empty second cell on each row. Do not type into those empty cells. This block replaces the whole file. It does not replace the template.

Open `work/states.md`. Select the whole file. Delete it. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. Paste. Save. Keep every pipe character. The header row, the dashes row, and the four state rows each need the same two columns: State, and What the patient sees.

If the paste lands as one long line, or a column is missing, select the whole file, delete it, and paste again. Do not repair the table by hand. If the spaces and pipes vanish as you paste, turn off Format On Paste, or use Paste Without Formatting, then paste once more.

```text
# Patient-visible states

| State | What the patient sees |
| --- | --- |
| rebooked | The session moved to a new time |
| notified | A message names the booking |
| compensated | The new hold was released |
| escalated | A person will call |
```

`rebooked` is what the patient is told: the session moved. You will not find `rebooked` in the trace. The worker stores `notified` when the text is accepted. `compensated` is the row it stores when the receipt is rejected and the hold is released. `escalated` is the row it stores when `slot` is false, and a person calls. The states page still names all four, because those are the words the patient can see.

The check looks for those four states, and for a sentence in the second column of each row. It does not name the state when one is missing.

## Replace the zones

This block replaces [work/zones.md](work/zones.md). The full path is `Module 02/Lesson 02/Student_Copy/work/zones.md`. The copy already has an empty row. Do not type into that row. The blank original stays in [packet/templates/zones.md](packet/templates/zones.md).

Open `work/zones.md`. Select the whole file. Delete it. Copy the lines inside the block below. Do not copy the fence lines. Paste. Save. Keep every pipe character. The header row, the dashes row, and the two piece rows each need the same two columns: Piece, and Zone.

```text
# Zone crossing

| Piece | Zone |
| --- | --- |
| int-engine | zone-hospital |
| wf-session-cancelled | zone-private |
```

The engine follows `h-nakhl` and `h-safra`. [zones.md](packet/kickoff/world/zones.md) places those hospitals in `zone-hospital`. The worker is the container named `wf-session-cancelled` in [namespace.yaml](packet/deploy/namespace.yaml). That file does not print a zone. It sits beside `h-wadi`, and the zones page places `h-wadi` in `zone-private`, so the worker row is `zone-private`.

The check looks for `int-engine` in `zone-hospital`, and for a row in `zone-private`. It does not name the piece when a row is missing.

## Replace the SMS

This block replaces [work/sms.md](work/sms.md). The full path is `Module 02/Lesson 02/Student_Copy/work/sms.md`. The copy is only a heading. The blank original stays in [packet/templates/sms.md](packet/templates/sms.md).

Open `work/sms.md`. Select the whole file. Delete it. Copy the lines inside the block below. Do not copy the fence lines. Paste. Save.

```text
# SMS

Your booking has a new time.
```

The sentence uses the word booking. It does not use a national id, and it does not use a ten-digit number. The check says the SMS wording is missing when the word booking is absent. It says the wording carries a national id when a ten-digit number is present.

Read the three files back. The states page is a table with two columns and four states. The zones page is a table with two columns and two pieces. The SMS page is the one sentence under the heading.

Next: [08 — The mart](08-the-mart.md).
