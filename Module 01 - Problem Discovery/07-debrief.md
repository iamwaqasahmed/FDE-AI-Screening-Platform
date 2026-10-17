# Debrief

Read this only after your problem brief exists. A difference is a miss when your version ignores a file or adds a system nobody asked to run.

## What the files support

The Chief Digital Officer asked for a three-program architecture, a vendor already in procurement, and a demo before quarter end. That is the sponsor's goal.

The operator's pain is diabetic eye screening. Breast screening meets its target. Cervical screening is not the failure anyone described. The clinic note already sets breast screening, cervical screening, and River Outreach outside the first slice.

Eligible people are registry rows whose `FLAG` is empty. That is 84,120 people, not every row with `RECORD_STATUS` Active. The extract has 91,406 rows. 7,286 are deceased or moved. The director's "about 84,000" is this denominator, rounded. Coverage is 34,490 / 84,120 = 41%. A photo with no result is not coverage. There are 6,110 of those.

| District | Eligible | Result in 24 months | Coverage |
|---|---:|---:|---:|
| North City | 46,200 | 26,796 | 58% |
| East City | 12,400 | 6,200 | 50% |
| Hill Counties | 15,800 | 1,264 | 8% |
| River Districts | 9,720 | 230 | 2.4% |

Spellings such as `N. City`, `Hill County`, and `Rivers` map back to those four names. The spoken "rural coverage is around a quarter" does not survive that map. Hill Counties and River Districts together are 25,520 eligible people and 1,494 results, about 6%.

Among the 34,490 completed results, after mapping `prolif`, a note of `urgent`, and `ungradable`:

| Result | Ordinary meaning | Count |
|---|---|---:|
| `R0` and `R1` | Readable, specialist not required | 20,694 |
| `U` | Photo could not be read | 7,588 |
| `R2` | Referable, not the urgent group | 5,829 |
| `R3` | Sight-threatening | 379 |

`REGISTRY_NO` is not unique. `LOCAL_PID` joins the workbook to the registry for people who were photographed. The PACS manifest joins on the hospital number. The cover note and the dictionary describe the opposite of those facts. A blank result is an unfinished screen. A blank model label means the model returned nothing. `REFERRAL` = yes is any referral, not an urgent one.

Median days from photo to letter, on completed results that have a letter, is 19. Median days from an urgent result to a specialist visit is 47. The 14-day target is in `sop_urgent_pathway_draft.md`, and that document says `NOT ISSUED`. The issued procedure has one referral box and no day target. Mild and sight-threatening disease therefore share `ophthalmology_referrals.csv`. Seen-dates for the mild referrals are blank in that file. The fourteen-week routine wait is the clinician's report. It is not a column you can average.

The vendor file has 400 primary-care images. 140 have no model label. On the other 260, the model and the grader disagree 81 times. The 93% figure belongs to a 1,200-image hospital slide. It is not in the handover, and it is not a result on these 400 images. The shared folder contains names that match no workbook row, including files named like `IMG_9#####.JPG`.

The scarce people are the graders, the eye specialists, and the patients who cannot make a second trip. The costly delays are an unusable photo discovered after the patient has gone home, a letter at 19 days, and an urgent appointment at 47 days.

## A brief that holds up

**Job to be done.** Get more eligible people with diabetes to a completed eye screen, and get sight-threatening cases to a specialist sooner, without making the routine specialist queue longer.

**Primary outcome.** More completed screens, and faster action on urgent disease, at the sites the clinic note already names.

**Metrics you can count from this drop.**

- Coverage of eligible people, denominator 84,120, until someone defends a different rule.
- Completed results versus photos with no result code.
- Median days from photo to letter.
- Median days from urgent result to specialist visit.
- Agreement between model and grader on the 400 pilot images, with silent outputs counted separately.

**Metric the slice has to start counting.** Share of photos caught as unusable before the patient leaves. The extract does not record a retake.

**First slice.** An agent at Hill Counties Health Centre, Oakridge Primary Care, and North City Eye Clinic.

- Tools answer from the registry, the workbook, the manifests, the letters, and the referrals.
- Retrieval uses the issued procedure for current policy, the grade-code list for the workbook's free text, the letter templates for drafts, the data-protection rule for refusals, and the clinic note for queue order. The urgent-pathway draft is retrieved only to say it is not in force.
- The agent can list who is due, who has a photo and no result, and which recorded results are sight-threatening. It can draft a letter by filling the template from that person's row.
- It refuses to diagnose from a photo and refuses to create a referral the grader has not signed.
- Images stay on the authority network. The first integration is the file you were given and a result file back. There is no electronic health record feed.

**Later work, with reasons.**

- Breast and cervical screening. The clinic note and the breast-screening lead already refused a shared release, and the failing pathway is diabetic eye screening.
- River Outreach. Coverage there is 2.4%. The files do not yet tell you whether the gap is cameras, travel, or staffing.
- The regional platform license. The primary-care file does not support the hospital slide.
- Training a model on Hartland images. The data-protection rule requires a separate approval.
- Electronic health record integration and an API. IT placed that work about fourteen months out.
- Treating the 14-day rule as policy. The draft is not issued. Putting it in a patient letter would invent a promise the authority has not made.

**Open questions that should stay open.**

- Who the named clinical safety owner is. The draft says the clinical lead must sign before the 14-day rule can be used.
- Whether a retake prompt is enough at the two primary-care sites, or the cameras themselves are the limit.
- How many of the unmatched shared-folder files are real patients.
- Which languages the letter has to go out in.
- Whether procurement can pause the three-program license without the Chief Digital Officer losing the commitment they have already signaled.

## The two conversations

To the Chief Digital Officer: the quarter can produce a working eye-screening agent at three sites, with coverage, unfinished photos, and urgent-wait numbers counted from the extract. The three-program platform is the next decision, after those numbers. The 93% slide is a hospital study. It is not the primary-care file.

To the ophthalmology lead: the agent separates sight-threatening results from milder ones for your review. It does not add referrals. A grader signs every result that changes care. The 14-day target stays a draft until you sign it. Your signature is on that operating rule, or the pilot does not start.

## How to grade your own brief

| Check | What "done" looks like |
|---|---|
| Ask left intact | The verbatim request is still a three-program platform |
| Pain located | Diabetic eye screening |
| Numbers from the files | 84,120 eligible, 41% coverage, the district table, 6,110 unfinished photos |
| Cover note tested | `REGISTRY_NO` and `FLAG` were checked, not trusted |
| Rules separated | The issued procedure is in force. The 14-day document is a draft |
| Vendor claim bounded | 93% is not treated as the result on the 400 pilot images |
| Human owner named | A grader signs care-changing results |
| First slice is the agent | Tools on the handover, retrieval on the corpus, three named sites |
| Later work is explicit | Breast, cervical, River Outreach, the platform license, model training, and the health-record integration are deferred |
| Unknowns kept | The safety owner and the unmatched files stay open |

A strong brief can argue for a different third site. It cannot honestly make a three-disease platform the first release.

## Misses that look like progress

- An architecture diagram in reply to the email. That is the deliverable the sponsor requested, and it freezes the wrong problem.
- Trusting `data/handover/README.txt` or the data dictionary over a count.
- Treating 93% sensitivity as the requirement. The operators asked for completed screens and a shorter urgent wait.
- A chat window that explains screening without calling a tool or citing a document. The bottleneck is the queue, the letter, and the referral list.
- A model that grades the retina from an image. The drop has paths, not images, and the data-protection rule forbids an unsigned diagnosis.
- Applying the draft 14-day rule as if the issued procedure had been replaced.
- Promising River Outreach a deployment because its coverage is the lowest. Low coverage tells you where to look next.

## Use the method again

Hartland goes away on the next engagement. The moves stay.

When the next client asks for a platform, write the sentence down, then find the queue, the scarce person, the costly delay, the decision a human still owns, and the smallest slice that can move one operator's metric. Leave a list of what you refuse to build yet. Leave a list of what you still do not know.

That list of unknowns is part of the deliverable. An FDE who fills every blank with an architecture has stopped discovering and started guessing.

Back to the [module guide](README.md).
