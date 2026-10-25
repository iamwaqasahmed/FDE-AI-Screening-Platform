# Schema registry

| Topic | Version | Owner | Required fields |
| --- | --- | --- | --- |
| referral.submitted | 1 | eref | event_id, topic, occurred_at, sequence, referral_id, patient_key, letter |
| session.cancelled | 1 | hospital | event_id, topic, occurred_at, sequence, booking_id, session_id, facility_id, slot |

A consumer ignores a field it does not know. session.cancelled is owned by the hospital that holds the session.
