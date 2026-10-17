## What happened

Incident INC-0270 concerns “PII written to booking API logs.” The incident began on 2025-09-15 and was identified as affecting the booking API. Personal information was recorded in application logs during the incident period. The incident was closed on 2025-10-02.

## Cause

The cause was Debug logging left on after a release. This configuration resulted in information intended for diagnostic purposes being retained in the booking API logs. The logging setting was reviewed as part of the incident response.

## Effect

The effect was Names and phone numbers in application logs. This represented personal information being present in operational records. The incident notice records the affected information and the period during which it was identified. Questions about this notice should be directed to the service desk, quoting INC-0270.
