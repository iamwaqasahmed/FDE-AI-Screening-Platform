# Round 4 corpus review

access: instructor

Instructor note. The student corpus must not name a screen's required event.

The check reads markdown and JSONL under `corpus/student`. It does not read `corpus/instructor`. Every markdown file in that student tree needs the exact line `access: student`.

Forbidden strings:

- dec-accept
- dec-clinical
- dec-route
- dec-cover
- dec-slot
- root_cause
- answer_key
- correct_currency
- booking_date_only
- HIPAA
- PIPEDA
