# Debrief — the architecture

The callback path is vendor, vendor-callback, integration-engine, grader. The zones, in that order, are external, dmz, authority, screening-service. FHIR appears on booking and on the integration engine. Tier 4, with no backup, is the shared folder and the camera inventory. The shared folder is tier 4, the grader is tier 1, and the vendor is tier 3. The vendor is hosted in the vendor cloud, EU region.

Fifteen flows. Seven are allowed: the photograph into the integration engine, the score along the callback path as far as the grader, the signed grade out to the letter bureau, a local id to M02, and a record reference to the audit log. Two are pending on `cloud-policy`: a photograph to the vendor, and a year of birth to the vendor. The data protection officer, M. Chen, has not approved the region. Six are denied: a hospital study, a date of birth, a score from the callback straight to the grader, a score onward to the letter bureau, a photograph into the agent, and a local id to M06.

T1 and T2 and T4 are live. T3 is not. The service account is usr-0036 and the excess role is directory-admin. The stale accounts are usr-0004, usr-0007, and usr-0023. R-11 reopens. R-08 stays closed.

The design rate is 175 requests a minute: the 08-10 band at 140, times January at 1.25. The vendor target of 0.98 is 14.4 hours a month without scores. Event lag is 240 minutes. The grader does not wait.

Back to the [debrief](../16-debrief.md).
