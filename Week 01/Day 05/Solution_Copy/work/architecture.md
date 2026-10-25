# Architecture

## Diagram

```mermaid
flowchart LR
  submit[referral.submitted]
  intake[wf-intake]
  patient[Patient]
  service[wf-self-service]
  coordinator[Coordinator]
  statusTool[referral.status]
  book[slots.book]
  submit --> intake
  intake --> coordinator
  patient --> service
  service --> statusTool
  service --> coordinator
  coordinator --> book
```

The coordinator is the human step. A return and a booking wait there.

## Zones

- zone-hospital
- zone-private
- zone-public

## Tools

referral.status, referral.return, slots.offer, slots.book, sms.send, safety.redirect
