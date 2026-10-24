# Failover

## Replicas

site-a and site-b both sit behind the balancer.

## Drill

site-a is down. site-b is serving.

## Approvals

In-flight approvals resume from the workflow store.

## Breaker

insure is a partner. The breaker opens, and the booking path does not call it.

## Patient

Status still works. A booking does not wait on insure.
