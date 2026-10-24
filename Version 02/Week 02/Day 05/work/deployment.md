# Deployment

Cited from ciso and from endpoint/guide.md. The checklist is pol-deploy. The change is notices/cr-ain.md. The file path is systems/sched-ain.md.

## URL

https://assistant.site-a.alwaha.internal

## Zone

The URL is in zone-private.

## Probe

GET /v1/health reports the registered hash for local-small. The container user is non-root.

## Credentials

Dev and prod credentials differ. Dev stays in dev. Prod stays in prod.

## Monitoring

Request rate, error rate, and model latency. The rest of the operations stack waits until Week 4.

## Boundary

A clinician assigns clinical urgency. PHI stays off ext-large.

## Operator steps

Read the health probe with the prod credential.

## Ain

h-ain is included through sched-ain. The interface is a nightly file in zone-hospital. A booking stays queued until that file arrives.

## Change

cr-ain is accepted and sequenced after the smoke test.
