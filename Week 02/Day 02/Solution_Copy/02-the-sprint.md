# 02 — The sprint

This is the sprint from the morning. Open the [finished sprint.md](work/sprint.md) and put it beside yours.

[feeds.md](sources/release/notices/feeds.md) says `eref` pushes `referral.submitted`. The mart extract is a database read that comes after that subscription. Booking from chat is still later.

The check looks for a subscription word before the word mart. The subscription word can be `webhook` or the start of `subscribe`. In this file, First says subscribe, and Later says mart. When the mart sentence comes first, or when one of the two ideas is missing, the message is `sprint.md does not sequence the subscription before the mart`. The message does not print the words it looked for.

`wf-session-cancelled` is named in First because that worker sends the SMS. [namespace.yaml](work/deploy/namespace.yaml) is where that name sits on the dev namespace. [compose.yaml](work/compose.yaml) is the laptop stand-in. A live cluster deploy is a later day.

Next: [03 — The worker](03-the-worker.md).
