# The precedent

**Days 1 and 2. Be the product manager, then the data engineer, then the consultant.** The bureau notice names no ticket. The cause it describes is already in the service desk, and in a notice from 2025.

## The same sentence

Match the notice's cause to a ticket. `handover/service_desk/tickets.csv` and `corpus/notices/` both carry it. The notice for that ticket says letters were lost. The policy record of the same week, `incident-letter-2025`, says each dispatch was written twice. It does not say letters were lost.

`handover/letters/incident_2025-03.csv` is that week's dispatch file. It has no request id. Every row is in the file twice, and there is no authority file to subtract from. Nobody could have counted the 2025 losses from the files the bureau returned.

This time the authority kept the request file. That is the control. Without it, this week would end the way 2025 ended: a notice, a doubled file, and no list of people.

## The catalogue

`handover/architecture/data_catalogue.csv` says `letters_dispatch` is one row per letter. The lineage edge into that dataset was last verified in 2022. The request file is not in the catalogue at all. A grain claim that the week 4 file breaks is a finding, not a quibble.

## Fill these findings

| Item | What it holds |
|---|---|
| `precedent` | `ref`, `start`, `end`, `notice`, `notice_says_lost`, `record`, `record_says_lost`, `has_request_id`, and `second_copies` |
| `catalogue_lineage` | `dataset`, `grain_claim`, `grain_holds`, `upstream`, `verified`, and `requests_catalogued` |

`second_copies` is the number of rows in the 2025 file that repeat a row already in that file. `grain_claim` is the sentence "One row per letter." `verified` is `YYYY-MM-DD`.

**A miss that looks like progress.** Quoting the bureau's "we believe" as the finding. The 2025 notice already said letters were lost. The bureau's belief is the claim you are checking.

**Finish.** You can name the 2025 ticket, the document that omits the losses, and the date the lineage was last verified.

Next: [The chase list](05-the-chase-list.md).
