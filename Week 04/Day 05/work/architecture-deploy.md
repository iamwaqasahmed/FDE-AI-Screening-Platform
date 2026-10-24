# Deployment architecture

## Zones

zone-private holds the assistant on site-a and site-b. zone-hospital holds int-engine. zone-public is the path to ext-large.

## Flows

cc receives the handoff. bi is the warehouse feed. hr sends leave. The bus carries session.cancelled.

## Boundary

A clinician assigns urgency. The assistant routes emergency wording to a human.
