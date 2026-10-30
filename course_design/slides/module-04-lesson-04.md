# Module 4, Lesson 4 — The drill — Availability and trade-offs

Facilitator only.

## Objective

The assistant keeps serving when `site-a` dies, and the rent-versus-buy note meets 8 February.

## Teach before the lab

Failover, circuit breakers, graceful degradation, and procurement lead time.

## Case

Site drill and the insurance outage. Release `rel-m04-l04`.

## Lab and trap

Put two replicas behind load balancing, fail over to `site-b`, open the breaker on `insure`, and write the rent-versus-buy paragraph. The trap is a booking path that waits on insurance until the request times out, or a purchase order that cannot arrive before Ramadan.

## Check and demo

`chk-slo`. Kill the practice pod on `site-a`.
