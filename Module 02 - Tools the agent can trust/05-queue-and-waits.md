# Queue and waits

## The queue

`grader_queue()` follows `clinic_note_pilot_sites.md`, document id `clinic-note`. The work piles, in the note's order, are:

1. Unfinished photos, no result code.
2. Unreadable photos, code `U`.
3. Mild referable disease, code `R2`.
4. Sight-threatening disease, code `R3`.

`R0` and `R1` are completed screens. They are not a pile on that queue. The referral column is not how you detect urgency. `yes` means any referral.

## The waits

`urgent_wait()` measures days from `GRADE_DATE` to `SEEN_DATE` for `R3` rows only, joined to `ophthalmology_referrals.csv` on `LOCAL_PID`. Many referral rows have an empty seen date. The sight-threatening ones should not.

The median is the middle value after you sort. With an even count, average the two middle values.

The 14-day target is in `sop_urgent_pathway_draft.md`. That file's status is draft, so the tool's `document_id` is `sop-urgent-draft` and the result says the draft is not in force. Quoting 14 days as current policy fails the point of the tool.

`letter_timing()` measures days from `PHOTO_DATE` to `SENT_DATE` for completed results that have a letter. Some letter rows match nobody. Some completed results have no letter. The median uses only the pairs that join. Its document is `letter-result`.

Both medians are in the Module 01 debrief.

Open `queue.py` and `waits.py` and match each function to a paragraph above.

**Finish.** You can say why 14 days is reported with document id `sop-urgent-draft`.

Next: [Vendor and letters](06-vendor-and-letters.md).
