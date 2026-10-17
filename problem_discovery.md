# Problem discovery

Self-paced module for forward deployed engineers. Hartland Regional Health Authority is a simulation. The people, the counts, and the clinical details are for practice. They are not a real health system and not a protocol for patient care.

You are embedded at a regional authority that reports to the Ministry of Health. The only sentence you were given before you arrived is: "We need an AI Screening Platform."

## How to study this

Set aside about half a day. Work in order. Write the two artifacts when the module tells you to stop. The reference debrief at the end is the answer key. Reading it early skips the skill this module exists to teach.

Do not open `data/truth`, `data/eval`, or `problem_simulation/config.yaml`. Those are the grading materials and the generator. The client did not hand them to you.

You need a place to write. Produce two short documents:

1. An ask log, written before you open the files.
2. A problem brief, written after you have queried the files and before you read the debrief.

Skills in [FDE.md](FDE.md) this module trains: problem discovery, product judgment, domain learning, and working while the picture is still incomplete. The folder guide is [problem_simulation/README.md](problem_simulation/README.md).

## What you will be able to do

By the end you can take a vague executive request and turn it into a problem a team can build against.

- Restate the ask without improving it.
- Separate the sponsor's goal from the operator's pain.
- Reconstruct the workflow from the extracts and the written rules, including where they disagree.
- Name one outcome, one first slice, and the work you are leaving for later.
- Say what is still unknown, and proceed anyway.

## The skill

A forward deployed engineer is hired when a customer says "build us a platform." That sentence is a request. The job is to find the problem underneath it.

In a health system the cost of skipping discovery is specific. A model can look strong on a slide and still send the wrong patients into an overcrowded clinic, miss people who never appear in the data, or stall in security review. Discovery is how you find that out while the change is still small.

Use these moves on every engagement. They are the method. Hartland is only the practice.

1. Write the ask down verbatim. Leave your improvements out of it.
2. Name the sponsor's goal and the operator's pain as two different things.
3. Walk the workflow as it is. Include the exceptions, the workaround, and the queue where work waits.
4. Find the scarce person and the costly delay.
5. Separate data that exists from data people wish existed.
6. Name the decision a human still has to own.
7. Choose one outcome an operator would recognize, and a metric for it.
8. Describe the smallest slice that can move that metric.
9. State what you are leaving out of the first release, and why.
10. List what you still do not know.

The brief you hand to the client has ten parts: the ask, the client, who feels the pain, the current workflow, the job to be done, the outcome and metrics, the constraints, the first slice, the later work, and the open questions.

## Terms in this case

| Term | Meaning here |
|---|---|
| Health authority | The regional body that runs public screening programs for the ministry |
| Registry | The list of people known to have diabetes |
| Coverage | The share of eligible people with a recorded result in the last 24 months |
| Fundus photo | A photograph of the retina, used in diabetic eye screening |
| Ungradable | A photo coded so that it cannot be read |
| Referable | A grader's judgment that an eye clinician should see the patient |
| Grader | The trained person who reads the photo and records a result |
| Sight-threatening | The urgent grade that needs a specialist sooner than a routine visit |
| PACS | The hospital image index |
| DPO | Data protection officer, who can stop a deployment that breaks the data rules |

## The engagement

You arrived this morning. Your company expects a recommended first deployment. The authority expects an architecture.

You have one email. You do not have the extract yet.

> From: Chief Digital Officer, Hartland Regional Health Authority
> Subject: AI Screening Platform — kickoff
>
> The ministry's digital program commits us to an AI Screening Platform this quarter. We screen for breast cancer, cervical cancer, and diabetic eye disease, and the platform should cover all three.
>
> A vendor showed us a model last year. Sensitivity was 93%. Procurement is in conversation with them. I need your architecture, the integration plan, and a demo date before the quarter closes.
>
> Our clinicians are busy. Please work from this brief and the vendor slides. I can give you thirty minutes on Friday.

### Stop. Write the ask log.

Write one page before you read any further. Use these headings.

- **Ask, verbatim.** Their words, not a cleaner version.
- **What they think the work is.** The deliverable the email is asking you to produce.
- **What a weak FDE does next.** The actions this email is designed to trigger.
- **Who you still need to hear from.** Roles, not a solution.
- **What you will refuse to propose on Friday.** Leave this as a list of risks, not a design.

The Chief Digital Officer offered you the vendor slides and thirty minutes. Treat that as a constraint on the sponsor, and go find the people who run the work.

## Evidence

You spend the next two days in the building. IT then sends the extract and the written rules. The interviews below are what people said. The files are what you can count. Where a person and a file disagree, the assignment is to show the disagreement, not to average it away.

The extract is [data/handover](data/handover). The written rules are [data/corpus](data/corpus). The cover note in the extract is the authority's note, not this module.

### What people said

**Director of Screening Programs.** Breast screening meets its coverage target. Cervical screening is close. Diabetic eye screening is the program they cannot defend in front of the ministry. They have been saying the registry holds about 84,000 people with diabetes, that coverage is about 41%, and that rural coverage is around a quarter. They do not have a source for the rural figure. It is the number the briefing keeps repeating. Photos go to three graders. One of them has been away. Results go out by letter. Ophthalmology says too many people are referred, and also that the urgent people wait too long.

**Ophthalmology clinical lead.** Do not send a longer list. The routine queue is already past fourteen weeks. A draft note talks about seeing sight-threatening disease within 14 days. Nobody has issued that note. Last year's model marked a large share of hospital photos as positive. Specificity was not on the slide. A grader must remain accountable for any result that changes care. A score can sort a queue. A score cannot discharge a patient or create a referral.

**Nurse at a Hill Counties primary-care site.** Patients travel a long way, longer from the river towns. The nurse takes the photo and does not know if it is usable. The file goes in a shared folder called `EYE SCREEN 2024 final final`. If the picture is no good, the patient has already gone home before anyone says so. The nurse can keep someone for another ten minutes if something on the screen says to retake the photo. The nurse cannot invent a specialist appointment.

**Grader.** The queue is the workbook. Blank results do not sort themselves. The clinic that calls gets opened first. Some sight-threatening cases are written as a code, and some are written only in the notes. Mild referable disease and sight-threatening disease still leave on one referral list.

**Data protection officer.** A previous pilot stored images outside the authority network and was paused. The written rule is the one they will enforce. They will review a bounded service with a data map. They will not review one release that covers breast, cervical, and eye screening.

**IT manager.** The electronic health record team can start an integration in about fourteen months. What exists now is the extract you were given: a registry file, a workbook, a hospital manifest, a shared-folder listing, letters, and referrals. There is no API. Hospital captures are on the PACS manifest. Primary-care and outreach captures are on the shared-folder listing. The cover note tells you how to join the files. IT did not write that note.

**Breast screening program lead.** That program meets its standard. Two readers already review every set. A shared AI platform creates a safety case they did not ask for. Leave that program out of the first release.

**Vendor.** On 1,200 hospital images, sensitivity for referable disease was 93%. Those images came from dilated patients on hospital cameras. Specificity is "available under NDA." The model returns nothing when it judges an image ungradable. The contract in procurement is a regional license for eye, breast, and cervical screening.

### What you count

Use the snapshot on the cover note and the 24-month rule in the issued procedure. Then answer these from the files. Write the queries down. The debrief has the figures, and your counts should match them.

- Who is eligible. Test the cover note and the data dictionary against the registry columns. `RECORD_STATUS` and `FLAG` do not mean what the cover note says.
- Coverage for the authority, and coverage for each district. District names are not spelled one way.
- How many people have a photo and no result. The grade-code list tells you what a blank result means. The dictionary says something else.
- The mix of result codes, after you map the free text in the workbook. Tabs and the `OLD` sheet are part of the mess.
- Median days from photo to letter, for completed results only. Some letter rows match nobody. Some completed results have no letter.
- Median days from an urgent result to a specialist visit. The referral file has no urgent column. The issued procedure explains why.
- What the vendor file actually contains, set next to the 93% sentence in the cover note.
- Which corpus documents are in force, and which document is still a draft.
- How many shared-folder names appear on no workbook row.

`LOCAL_PID` is on the registry and on the workbook. `REGISTRY_NO` is what the cover note tells you to join on. The PACS manifest uses a hospital number. Try all three.

## Stop. Write the problem brief.

Write this before you read the debrief. Two pages is enough. Where the files are thin, say so under open questions. Do not fill the gaps with a platform diagram.

1. **Ask, verbatim.**
2. **Client and sponsor.** Who can say yes, and what they are under pressure to show.
3. **Who feels the pain.** The people whose day changes if you succeed. One sentence each.
4. **Workflow as it is.** From "person with diabetes" to "seen or not seen," including the broken handoffs.
5. **Job to be done.** One paragraph. The request was a platform. The job is the outcome the eye-screening program cannot currently produce.
6. **Outcome and metrics.** One primary outcome. Three to five metrics you counted, or that the first slice would have to start counting.
7. **Constraints.** Clinical, data, integration, and political. Only constraints you can point to in an interview, a file, or a corpus document.
8. **First slice.** The sites, the users, what the agent does this quarter, which tools it calls, which documents it retrieves, and the decision a human still owns.
9. **Later work.** What you will not put in the first release. Each item needs a reason from the evidence.
10. **Open questions.** What would change the slice if the answer came back differently.
11. **Two conversations.** Five lines for the Chief Digital Officer. Five lines for the ophthalmology lead. Same slice, different sentences.

The first slice is an agent with retrieval and tools. Retrieval reads the corpus. Tools read the handover. A chat window that answers from memory, with no tool call and no cited rule, is not that slice. A grader still signs every result that refers, recalls, or reassures a patient.

## Reference debrief

Read this only after your brief exists. A difference is a miss when your version ignores a file or adds a system nobody asked to run.

### What the files support

The Chief Digital Officer asked for a three-program architecture, a vendor already in procurement, and a demo before quarter end. That is the sponsor's goal.

The operator's pain is diabetic eye screening. Breast screening meets its target. Cervical screening is not the failure anyone described. The clinic note already sets breast, cervical, and River Outreach outside the first slice.

Eligible people are registry rows whose `FLAG` is empty. That is 84,120 people, not every row marked `RECORD_STATUS` Active. The extract has 91,406 rows. 7,286 are deceased or moved. The director's "about 84,000" is this denominator, rounded. Coverage is 34,490 / 84,120 = 41%. A photo with no result is not coverage. There are 6,110 of those.

| District | Eligible | Result in 24 months | Coverage |
|---|---:|---:|---:|
| North City | 46,200 | 26,796 | 58% |
| East City | 12,400 | 6,200 | 50% |
| Hill Counties | 15,800 | 1,264 | 8% |
| River Districts | 9,720 | 230 | 2.4% |

Spellings such as `N. City`, `Hill County`, and `Rivers` map back to those four names. The spoken "rural coverage is around a quarter" does not survive that map. Hill Counties and River Districts together are 25,520 eligible people and 1,494 results, about 6%.

Among the 34,490 completed results, after mapping `prolif`, a note of `urgent`, and `ungradable`:

| Result | Count |
|---|---:|
| Readable, not referable (`R0` and `R1`) | 20,694 |
| Ungradable | 7,588 |
| Referable, not urgent (`R2`) | 5,829 |
| Sight-threatening (`R3`) | 379 |

`REGISTRY_NO` is not unique. `LOCAL_PID` joins the workbook to the registry for people who were photographed. The PACS manifest joins on the hospital number. The cover note and the dictionary describe the opposite of those facts. A blank result is an unfinished screen. A blank model label is a silent model. `REFERRAL` = yes is any referral, not an urgent one.

Median days from photo to letter, on completed results that have a letter, is 19. Median days from an urgent result to a specialist visit is 47. The 14-day target is in `sop_urgent_pathway_draft.md`, and that document says `NOT ISSUED`. The issued procedure has one referral box and no day target. Mild and sight-threatening disease therefore share `ophthalmology_referrals.csv`. Mild seen-dates are blank in that file. The fourteen-week routine wait is the clinician's report, not a column you can average.

The vendor file has 400 primary-care images. 140 have no model label. On the other 260, the model and the grader disagree 81 times. The 93% figure belongs to a 1,200-image hospital slide. It is not in the handover, and it is not a result on these 400 images. The shared folder contains names that match no workbook row, including the `IMG_9#####.JPG` decoys.

The scarce people are the graders, the ophthalmologists, and the patients who cannot make a second trip. The costly delays are an unusable photo discovered after the patient has gone home, a letter at 19 days, and an urgent appointment at 47 days.

### A brief that holds up

**Job to be done.** Get more eligible people with diabetes to a completed eye screen, and get sight-threatening cases to a specialist sooner, without lengthening the routine ophthalmology queue.

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
- The agent can list who is due, who has a photo and no result, and which recorded results look sight-threatening. It can draft a letter by filling the template from the row.
- It refuses to diagnose from a photo and refuses to create a referral the grader has not signed.
- Images stay on the authority network. The first integration is the file you were given and a result file back. There is no electronic health record feed.

**Later work, with reasons.**

- Breast and cervical screening. The clinic note and the breast-screening lead already refused a shared release, and the failing pathway is diabetic eye screening.
- River Outreach. Coverage there is 2.4%. The files do not yet tell you whether the gap is cameras, travel, or staffing.
- The regional platform license. The primary-care file does not support the hospital slide.
- Training a model on Hartland images. The data-protection rule requires a separate approval.
- Electronic health record integration and an API. IT placed that work about fourteen months out.
- Treating the 14-day rule as policy. The draft is not issued. Using it in a patient letter would invent a promise the authority has not made.

**Open questions that should stay open.**

- Who the named clinical safety owner is. The draft says the clinical lead must sign before the 14-day rule can be used.
- Whether a retake prompt is enough at the two primary-care sites, or the cameras themselves are the limit.
- How many of the unmatched shared-folder files are real patients.
- Which languages the letter has to go out in.
- Whether procurement can pause the three-program license without the Chief Digital Officer losing the commitment they have already signaled.

### The two conversations

To the Chief Digital Officer: the quarter can produce a working eye-screening agent at three sites, with coverage, unfinished photos, and urgent-wait numbers counted from the extract. The three-program platform is the next decision, after those numbers. The 93% slide is a hospital study. It is not the primary-care file.

To the ophthalmology lead: the agent separates sight-threatening results from mild ones for your review. It does not add referrals. A grader signs every result that changes care. The 14-day target stays a draft until you sign it. Your signature is on that operating rule, or the pilot does not start.

### How to grade your own brief

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

A strong brief can argue for a different third site. It cannot honestly choose a three-disease platform as the first release.

### Misses that look like progress

- An architecture diagram in reply to the email. That is the deliverable the sponsor requested, and it freezes the wrong problem.
- Trusting `data/handover/README.txt` or the data dictionary over a query.
- Treating 93% sensitivity as the requirement. The operators asked for completed screens and a shorter urgent wait.
- A chatbot that explains screening without calling a tool or citing a document. The bottleneck is the queue, the letter, and the referral list.
- A vision model that grades the retina. The drop has paths, not images, and the data-protection rule forbids an unsigned diagnosis.
- Applying the draft 14-day rule as if the issued procedure had been replaced.
- Promising River Outreach a deployment because its coverage is the lowest. Low coverage tells you where to look next.

## Use the method again

Hartland goes away on the next engagement. The moves stay.

When the next client asks for a platform, write the sentence down, then find the queue, the scarce person, the costly delay, the decision a human still owns, and the smallest slice that can move one operator's metric. Leave a list of what you refuse to build yet. Leave a list of what you still do not know.

That list of unknowns is part of the deliverable. An FDE who fills every blank with an architecture has stopped discovering and started guessing.
