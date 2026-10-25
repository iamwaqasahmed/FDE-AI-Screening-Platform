# 04 — The pages

These are the three pages from the morning. Open them and put them beside yours.

## States

Open [states.md](work/states.md).

The columns are State and What the patient sees. The four states are the ones the blank page already listed. Each second cell is filled.

| State | Why that sentence |
| --- | --- |
| rebooked | The session moved. The SMS sentence says the booking has a new time |
| notified | [cancel.py](work/app/cancel.py) stores this when the receipt is accepted, and the patient sees a message that names the booking |
| compensated | The rejected receipt releases the hold. The patient sees that the new hold was released |
| escalated | No slot. A person will call. Nothing is booked |

The check requires every one of those four names, and a non-empty second cell. When one is missing, the message is `a patient-visible state is missing`. It does not name the state.

## Zones

Open [zones.md](work/zones.md).

[feeds.md](sources/release/notices/feeds.md) says HL7 from `h-nakhl` and `h-safra` arrives through `int-engine`. [zones.md](sources/kickoff/world/zones.md) places those two hospitals in `zone-hospital`, so the engine is in `zone-hospital`.

[namespace.yaml](work/deploy/namespace.yaml) names `wf-session-cancelled` on the dev namespace. The cancellation events name `h-wadi`, which the zones page places in `zone-private`. The worker is in `zone-private`.

The check looks for `int-engine` together with `zone-hospital`, and for any row whose zone contains `zone-private`. When that pair is missing, the message is `zone crossing is missing`. It does not name the piece.

## SMS

Open [sms.md](work/sms.md).

The sentence is `Your booking has a new time.` It contains the word booking. It has no ten-digit number. [sms.py](work/app/sms.py) uses the same sentence and adds the booking id at send time. The page leaves the id off.

The check says `sms wording is missing` when the word booking is absent. It says `sms wording carries a national id` when a ten-digit run is present.

Next: [05 — The mart](05-the-mart.md).
