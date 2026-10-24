# Deployment

Cited from ciso and from endpoint/guide.md. The checklist is pol-deploy.

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
