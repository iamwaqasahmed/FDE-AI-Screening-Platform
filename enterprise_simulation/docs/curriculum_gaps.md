# Curriculum gaps

`commands()` in `src/access/curriculum_evidence.py` is appended by `history()`. Nothing here is a repair.

- **INV-01.** Boards, the three logs, the mart at wait 0, the sponsor's demand for one number, and REF-8801 (hospital acceptance beside an earlier channel request) are already in the pack. No new command.
- **INV-02.** The REF-4417 letter contains clinical wording, REF-3304 has emergency wording and a return, and REF-2290 is a payer timeout with no window. The assistant screen already shows one urgency field. No new command.
- **INV-03.** The letter contains APR-4417, the assistant screen shows that id accepted, and REF-5510 has two offers of slot-v3. The channel utterance on REF-4417 has `handset_delivered` false. No new command.
- **INV-04.** The crash window is the unacked then redelivered key sms-4417. A replayed Cedar Ridge file id, poison file cedar-poison-2026, Saturday file cedar-2027-01-09, and a file night before coverage are already in the logs. The pack has no cancelled visit with a later handset text, and it has no announced closure list. `cmd-cur-visit-cancelled` records a cancelled Cedar Ridge file row for CUR-4. `cmd-cur-text-after-cancel` records a handset text for that same file. `cmd-cur-closures` records announced office closure dates 2027-01-01 and 2027-02-15.
- **INV-05.** The document extract has superseded, in-force, unauthorized, and in-flight rows, plus a hash mismatch. A draft row is also present (`leg-dms-draft` from the legacy desk, and `dms-draft-fraser` once round-2 feeds are on the log).
- **INV-06.** `calibration.json` already holds the labeled sheet. Its rows include a pass field and an arm, including the small comparison 0.5001 versus 0.5000 at n 8. A second hospital calibration event would repeat that sheet. `cmd-cur-tiny-delta` is a channel event. Its tiny_delta note is `scores 0.5002 vs 0.5000, n 9`, and the payload also carries those two scores and n.
- **INV-07.** `host.json` is a green host at cpu 12. Served hours `2026-summer` sit on a separate extract. `shadow.json` records a write and a sentence, with no referral on the row. Hours documents are already in the hospital log. The eligibility cache on REF-4417 is a coverage bit. `cmd-cur-shadow-wrote` is a shadow replay for CUR-7 with `shadow_wrote` true and a slot write. `cmd-cur-host-green` records cpu_percent 11, status green, served_version `old-hours`, and `from_cache` true on desk-app-9.
- **INV-08.** The letter, the national-id file, the quotation, the wage note, the leaflet, and the call records (a region mismatch and a region match on a letter) are already in the pack. The mixed object the checker grades stays out of the pack. `cmd-cur-faq-quote` stores faq id `faq-mixed-cur` and the sentence `Patient reports urgent chest pain.` which is the first sentence of the REF-4417 letter. The payload is that faq id and that sentence.
- **INV-09.** PERMIT-12 is lodged in Vancouver and stamped in Washington, and the board label is `since_lodged`. No new command. The permit world is left as it is.

## Command ids

- `cmd-cur-visit-cancelled` (`cur-cancel`)
- `cmd-cur-text-after-cancel` (`cur-text`)
- `cmd-cur-closures` (`cur-closures`)
- `cmd-cur-tiny-delta` (`cur-score`)
- `cmd-cur-shadow-wrote` (`cur-shadow`)
- `cmd-cur-host-green` (`cur-host`)
- `cmd-cur-faq-quote` (`cur-faq`)
