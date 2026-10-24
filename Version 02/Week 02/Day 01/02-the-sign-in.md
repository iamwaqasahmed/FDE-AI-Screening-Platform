# Sign-in

Read [identity/loa.md](../../data/rel-w2d1/identity/loa.md) and [openapi/iam.yaml](../../data/rel-w2d1/openapi/iam.yaml).

The identity note lists the staff roles. A patient at `loa-1` can open the assistant. The note says which assurance level may book. That step-up is not today's lab.

The product manager copies [templates/states.md](templates/states.md) to `work/states.md` and writes the sign-in states: signed out, the patient, and the coordinator.

The architect copies [templates/token-flow.md](templates/token-flow.md) to `work/token-flow.md`. The token is checked against the discovery document. The session row is written in the application database. A service token is not a patient token.

`svc-integration` is named in the identity note. Do not sign the patient in with it.
