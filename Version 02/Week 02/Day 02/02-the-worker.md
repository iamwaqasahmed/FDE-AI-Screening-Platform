# The worker

Copy [app](app) to `Week 02/Day 02/work/app`. Leave the copy in this folder unchanged. Copy [compose.yaml](compose.yaml), [Dockerfile](Dockerfile), and [deploy/namespace.yaml](deploy/namespace.yaml) with it.

The shell intake still polls `eref`. The shell cancel path applies a delivery every time it sees one, and it leaves the hold open when SMS fails.

Subscribe to `referral.submitted` and to `session.cancelled`. Ignore a field the registry does not list. Do not reject the event for that field.

The event file is three deliveries: the first cancellation, the same event again, and a delivery whose SMS receipt is rejected. A replay must not book or text a second time. When the receipt is rejected, release the new hold and leave nothing booked.

A cancellation with no slot escalates. Do not send an SMS of a booking. The check sends that case. It is not a fourth line in the file.

From `work`, with the pack built:

```text
python app\run.py --pack ..\..\..\data\rel-w2d2 --db sessions.db --out trace.json
```

[compose.yaml](compose.yaml) is the laptop stand-in for the dev namespace. [deploy/namespace.yaml](deploy/namespace.yaml) names `wf-session-cancelled` beside chat and the console. A live cluster deploy is a later day.

The assistant rule from Day 1 still applies. A coding assistant may see your script. It may not see the webhook file. That file is watermarked. Do not copy it into `work/`.
