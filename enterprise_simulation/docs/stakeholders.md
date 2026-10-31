# Stakeholders

Northline Access Collaborative is fictional. The titles below are roles.

## Where a student meets the network

`organization.json` lists the Vancouver desk in BC (`America/Vancouver`), Cascade Seattle and Cedar Ridge in Washington, and Fraser Burnaby in BC. Cedar Ridge has `"slot_api": false`. Harbor Coverage uses CAD and USD. The office week is Monday through Friday. Clinical sites file at night, including weekends.

`sponsor.json` is the operations director, in one sentence: "Put one wait number on the patient screen before the long weekend."

Roles appear on streams whose ids start with `org-`. In `extracts/channel.json` and `extracts/hospital.json`, a row keeps `type`, `occurred_at`, and a payload with `role_id`, `title`, `site`, and `statement`. Command ids on those commands start with `cmd-org-`. Member referrals stay on their own streams.

| role_id | Title | Site | Extract | Stream | Event |
| --- | --- | --- | --- | --- | --- |
| ops-director | Operations director | vancouver-desk | channel.json and sponsor.json | org-wait, org-cover | SponsorAsked |
| desk-supervisor | Desk supervisor | vancouver-desk | channel.json | org-wait, org-file | PolicyNoted, SponsorAsked |
| cascade-records | Records officer | cascade-seattle | hospital.json | org-wait, org-leave | PolicyNoted, LeavePosted |
| endocrine-clinician | Endocrine clinician | fraser-burnaby | hospital.json | org-letter | PolicyNoted |
| medical-director | Medical director | fraser-burnaby | channel.json | org-letter | SponsorAsked |
| privacy-officer | Privacy officer | cascade-seattle | hospital.json | org-letter | PolicyNoted |
| finance-partner | Finance partner | vancouver-desk | channel.json | org-letter | SponsorAsked |
| payer-clerk | Eligibility clerk | harbor-coverage | payer.json | org-cover | CoverageDecided |
| cedar-clerk | Nightly file clerk | cedar-ridge | hospital.json | org-file | PolicyNoted |

The payer extract stores the eligibility clerk as coverage: ref `org-cover-clerk`, answer `timeout`, currency `USD`, with empty `effective_from` and `effective_to`. The clerk's statement is on that command. The operations director's channel row uses the same ref and quotes the timeout.

The records officer payload carries `office_id` `cascade-records`. That office string is already on the permit stamp in the hospital extract. The clerk's note names nightly file `cedar-2027-01-09`, which is already a Cedar Ridge file row in the hospital extract.

Each of these rows has an `occurred_at` instant in UTC on the log that wrote it. The instants fall between 2026-11-01 and 2027-01-11.

## What the extracts show them saying

**Screen number.** On `org-wait`, the operations director asks for one wait number on the patient screen before the long weekend. The desk supervisor records Vancouver desk practice: the count they tell the patient starts when the desk takes the call. The records officer records Cascade practice: the board starts when the referral is accepted into the hospital record, and that office keeps that one board.

**Letter.** On `org-letter`, the medical director asks the assistant to grade urgency from the referral letter before the clinic reopens. The endocrine clinician says the letter stays with clinicians and a model does not grade it. The privacy officer blocks upload of letters from Cascade Seattle, Cedar Ridge, and Fraser Burnaby. The finance partner asks to send the letter corpus to an external model because a spreadsheet says it is cheaper today. On `org-leave`, the records officer posts that clinician's leave from 2027-01-10 through 2027-01-11 and states that the letter stays with clinicians. The leave row is later the same Saturday as an already-open Vancouver desk session.

**Nightly file.** On `org-file`, the desk supervisor asks to put "Cedar Ridge tonight" on the patient screen before the nightly file lands. The Cedar Ridge clerk states that the site has no slot API, that the release is nightly file `cedar-2027-01-09`, and that the clerk files at night, including weekends.

**Coverage.** On `org-cover`, the eligibility clerk records timeout on a USD inquiry and does not fill in a yes. The operations director asks for one wait number on the patient screen anyway and asks to treat the member as covered enough to keep that screen simple.
