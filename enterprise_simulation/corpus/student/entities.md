# Northline names used in the document room

Synthetic. No real patient, member, or employee.

## Organizations

- Northline Access Collaborative. Desk in Vancouver, British Columbia. Time zone America/Vancouver. Office week Monday through Friday.
- Cascade Seattle. Hospital. Washington. America/Los_Angeles.
- Cedar Ridge. Rural Washington clinic. Nightly file only. No slot API. Files at night, including weekends.
- Fraser Burnaby. Hospital. British Columbia. America/Vancouver.
- Harbor Coverage. Payer. CAD and USD.
- Inlet Medical. Washington clinic merged into Cedar Ridge on 2026-09-01. The old site id still appears on some files.

## People

| Name | Role |
| --- | --- |
| Dana Okonkwo | Operations director, Vancouver desk |
| Morgan Ibarra | Desk supervisor, Vancouver |
| Noel Park | Desk clerk, Vancouver |
| Priya Shah, MD | Clinician, Fraser Burnaby |
| Evan Cho | Privacy officer, Vancouver |
| Ruth Alvarez | Harbor Coverage clerk |
| Sam Nguyen | Night file clerk, Cedar Ridge |
| Jordan Hale | Records, Cascade Seattle |
| Chris Pell | Finance, Northline |
| Alex Kim, MD | On-call physician |
| Riley Chen | Owner of the 2024 assistant |
| Harper Singh | Integration engineer, left in March 2026 |
| June Lau | Member services, Vancouver desk |
| Omar Farouk | Night supervisor, Cascade Seattle |
| Lena Brooks | Harbor Coverage supervisor, Seattle |
| Wes Calder | Platform lead, left in 2020. Wrote the 2019 clock page |
| Anita Desai | Clinic manager, Fraser Burnaby |
| Bobbi Tran | IT, Northline. Keeps the three logs |
| June Lau | Member services, Vancouver desk |
| Omar Farouk | Night supervisor, Cascade Seattle |
| Lena Brooks | Harbor Coverage supervisor, Seattle |
| Wes Calder | Platform lead, left in 2020. Wrote the 2019 clock page |
| Anita Desai | Clinic manager, Fraser Burnaby |
| Bobbi Tran | IT, Northline. Keeps the three logs |

## Opening case the extracts already show

Reference `REF-4417`. Member region BC. Currency on the payer row is CAD. Cedar Ridge is in WA.

- Payer answer yes, window 2027-01-12 through 2027-04-12.
- Channel request 2027-01-09 08:14Z. The utterance says the visit is booked at Cedar Ridge tonight. The handset was not delivered.
- Hospital cache the same evening: eligible true, window not stored.
- Cedar Ridge file `cedar-2027-01-11` at 2027-01-11 21:00Z.
- Letter text includes urgent chest pain and the string `APR-4417`. Audience clinician.
- The 2024 assistant screen shows wait 0, urgency urgent, approval `APR-4417`, and close 21:00.
- Hours `hours-cedar`: summer close 21:00 is superseded. Winter close 17:00 is in force. A copy stores a hash that does not match its body.
- The facility mart shows wait 0 on booking date 2027-01-11.

Other references already on the extracts: `REF-8801`, `REF-2290` (timeout, no window), `REF-3304` (emergency wording), `REF-5510` (two offers of one slot version), `PERMIT-12`, `THR-17`, `INT-17`, `R2E-9`, `R3F-LEDGER` (board 18420 USD, payer row 18420 CAD), `R3A-MERGE`, contract `MA-2024`, quotation `QUO-18420`.

## What a document must not decide

Do not name a screen label's required event. Do not tell the reader which clock a board is allowed to use. People in the documents may argue. The document itself does not award the argument.

access: student

