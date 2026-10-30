# 9 — From the laptop to AWS

One system. The contracts move. The topology changes only where a trust boundary or a delivery guarantee changes.

| Laptop fact | Account fact |
| --- | --- |
| The tool checks a capability | The state machine’s task token does not replace that check |
| The business key is stored with the operation | SQS will deliver again. The consumer stores the same key |
| The outbox commits with the business row | The same transaction if the store moves to RDS. A later publish can still happen twice |
| Spans carry a document id, not a body | The log group has a filter. The canary string is denied |
| Class is a function over the object | The template is failed by the policy pack if a restricted fixture appears |
| The case clock is an argument | Production uses a service clock and records it. Tests still pass the case clock in |

Investigations 1, 2, 5, and 6 end with a boundary note and no template. Investigations 4, 7, and 8 change the design: a queue, a log filter, and a payload schema. “Move the SQLite file to a managed database” without those changes does not finish them.

A student who never applies a stack can finish. Their cloud evidence is the synthesized template and the policy findings. A student who applies a stack also shows a destroy and an alarm that existed before the apply.
