# Debrief — drop and contracts

Practice seed. Version 3 has 45,180 rows. `HOME_CLINIC` is `REGISTERED_SITE`. The new columns are `DISTRICT_CODE`, `FLAG_DATE`, and `SCHEMA_VERSION`. Every date of birth is an ISO date. Version 2 stops on 2026-10-31.

The reissue batch is 40 numbers, on 2026-10-12. A join of the warehouse snapshot to version 3 on the raw registry number drops those 40 people. Mapping the batch puts them back. Version 3 also restores 2,421 local ids that version 2 left blank.

## The service is not the file

`Accept-Version: 3` still returns `home_clinic`. It does not return `DISTRICT_CODE`, `FLAG_DATE`, or `SCHEMA_VERSION`. It still serves the old registry numbers. A client that trusts the version header has not read `current_v3.csv`.

## Catalogue and reconciliations

These catalogue entries no longer describe the data: `booking_appointments.status`, `call_centre_export.reason_code`, `finance_ledger.cost_centre`, `lab_hba1c.value`, `sms_receipts.receipt_at`, `warehouse.eligible`.

The SMS file has 6,842 duplicate rows. About 0.079 of receipts arrive more than an hour after they were sent. About 0.247 of rows sit earlier in send time than the previous row. The file is not in send order. Dedupe on `event_id`, and order by `occurred_at`.

Booking history is not in the export. The outage is `INC-0281`. The count of rebookings is not a number the export will give you.

Lab patient id and booking id carry no name and no date of birth. They stay unlinked.

## Misses that look like progress

- Renaming `HOME_CLINIC` in the loader and leaving the reissue unmapped.
- Calling the service's version 3 the same schema as the file.
- Copying a catalogue definition because it has a review date.
- A contract that drops a row and writes nothing.

Next: [Identity](identity.md).
