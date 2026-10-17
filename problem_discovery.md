# Problem discovery

Self-paced module for forward deployed engineers. The client, the figures, and the clinical details are a simulation for practice. They are not a real health authority and not a protocol for patient care.

You are embedded at a regional health authority that reports to the Ministry of Health. The only sentence you were given before you arrived is: "We need an AI Screening Platform."

## How to study this

Set aside about half a day. Work in order. Write the two artifacts when the module tells you to stop. The reference debrief at the end is the answer key. Reading it early skips the skill this module exists to teach.

You need a place to write. Produce two short documents:

1. An ask log, written before you read the evidence.
2. A problem brief, written after the evidence and before the debrief.

Skills in [FDE.md](FDE.md) this module trains: problem discovery, product judgment, domain learning, and working while the picture is still incomplete.

## What you will be able to do

By the end you can take a vague executive request and turn it into a problem a team can build against.

- Restate the ask without improving it.
- Separate the sponsor's goal from the operator's pain.
- Reconstruct the workflow people actually follow, including where it breaks.
- Name one outcome, one first slice, and the work you are leaving for later.
- Say what is still unknown, and proceed anyway.

## The skill

A forward deployed engineer is hired when a customer says "build us a platform." That sentence is a request. The job is to find the problem underneath it.

In a health system the cost of skipping discovery is specific. A model can be accurate on a demo set and still send the wrong patients into an overcrowded clinic, miss people who never appear in the data, or stall for a year in security review. Discovery is how you find that out while the change is still small.

Use these moves on every engagement. They are the method. The Hartland case is only the practice.

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
| Registry | The list of people known to have a condition, in this case diabetes |
| Coverage | The share of eligible people who actually received a screen in the required window |
| Fundus photo | A photograph of the retina, used to look for diabetic eye disease |
| Ungradable | A photo that cannot be read, so the screen did not happen |
| Referable | A human grader's judgment that an eye clinician should see the patient |
| Grader | The trained person who reads the photo and records a result |
| Sight-threatening | The urgent subset that needs a specialist soon, not at the next routine visit |
| PACS | The hospital system that stores medical images |
| DPO | Data protection officer, who can stop a deployment that breaks the data rules |

## The engagement

Hartland Regional Health Authority is fictional. It runs population screening for the Ministry of Health. You arrived this morning. Your company expects a recommended first deployment. The authority expects an architecture.

You have one email.

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

You spend the next two days in the building. This is what you collect. Read it as raw notes. People contradict each other. Spoken numbers and file extracts disagree. That is the assignment.

### Director of Screening Programs

> Breast screening meets its coverage target. Cervical screening is close. Diabetic eye screening is the one I cannot defend. The registry says we have about 84,000 people with diabetes. I tell the ministry that coverage is 41%, and that rural coverage is around a quarter. I do not have a source for the rural number. It is the figure we have been repeating.
>
> People are screened at six hospital eye clinics. Two primary-care sites started a pilot and then stalled. Photos go to three graders. One grader is on leave. Results go out by letter. I hear that letters take weeks. Ophthalmology tells me we refer too many people, and also that the urgent people wait too long. Both things are probably true.
>
> If your platform touches breast screening, that program lead will block you. She is right to. Do not spend this quarter on a home for every program. I need the diabetics who have not been seen, and I need the ones we photograph to come out with a result.

### Ophthalmology clinical lead

> Do not send me a longer list. My routine queue is already past fourteen weeks. For disease that can take someone's sight, our draft rule is that they are seen within fourteen days. Nobody issued that rule. Look at the waits.
>
> Last year's model marked a huge share of hospital photos as positive. The vendor called that safety. I call it my clinic. Specificity was not on the slide.
>
> A grader must remain accountable for any result that changes what we do to a patient. A score can sort a queue. A score cannot discharge a patient or refer one. If you want my signature on a safety note, that is the rule.

### Nurse at a Hill Counties primary-care site

> Patients take half a day to get here, longer from the river towns. I take the photo. I do not know if it is usable. The file goes in a shared folder called `EYE SCREEN 2024 final final`. If the picture is no good, the letter comes back after the patient has already lost wages to come in. Most of them do not come back.
>
> I can keep someone for another ten minutes if something on the screen tells me to retake the photo before they leave. I cannot keep them for a specialist appointment we do not have.

### Grader

> The work queue is a spreadsheet. The oldest tab still says the photo was taken and the result is blank. Those rows do not sort themselves. I open whichever file a clinic chases me about. The urgent code exists, and I use it when I am sure. Plenty of referable results are mild and could be photographed again in primary care next year. They still land on the same ophthalmology list as the urgent ones, because the letter template has one referral box.

### Data protection officer

> The vendor pilot stored retinal images in a cloud region outside the authority network. I paused it. Images are health data. A restart needs four things: images stay on the authority network, every access is logged, retention is written down, and a named clinical safety owner signs the operating rule. Using patient images to train a model is a separate approval. It is not included in a software pilot.
>
> I will not review a platform for three screening programs. I will review a bounded service with a data map.

### IT manager

> The electronic health record team can start an integration in about fourteen months. That slot is real. What I can give you now is a nightly file from the diabetes registry over SFTP, and a folder where you can leave a result file for the call center and the graders. Hospital images also sit in PACS. The rural sites do not use PACS. They use the shared folder.
>
> There is no API for this program. Please stop drawing one on the architecture slide until we have a reason to build it.

### Breast screening program lead

> We meet our standard. Two readers already review every set of images. We have an audit trail. A single platform that "adds AI" to my program creates a safety case I did not ask for, on a clock set by a press announcement. Leave us out of the first release.

### Call with the vendor

The sales engineer repeats the slide. On 1,200 hospital images, sensitivity for referable disease was 93%. The images came from dilated patients on hospital cameras. Specificity is "available under a mutual NDA later." The model returns no output when it judges an image ungradable. The contract they sent procurement is a regional license for an AI Screening Platform covering eye, breast, and cervical screening. Implementation services are a separate statement of work.

### Registry extract

You are given a one-off export, not a live system. A data analyst warns you that "active" and "eligible" are different.

| | Count |
|---|---|
| Rows marked active on the diabetes registry | 91,406 |
| Flagged deceased or moved out of region | 7,286 |
| Eligible people | 84,120 |
| Eligible people with a result code in the last 24 months | 34,490 |
| Photo recorded in the last 24 months and no result code | 6,110 |

Coverage on the eligible denominator is 34,490 / 84,120 = 41%. The 6,110 photos with no result are not in that coverage figure. Those people were photographed and still have no completed screen.

| District | Eligible | Result in 24 months | Coverage |
|---|---:|---:|---:|
| North City | 46,200 | 26,796 | 58% |
| East City | 12,400 | 6,200 | 50% |
| Hill Counties | 15,800 | 1,264 | 8% |
| River Districts | 9,720 | 230 | 2.4% |

The director's "rural coverage is around a quarter" does not match Hill Counties or River Districts. North City and East City together hold 58,600 eligible people and 32,996 results, about 56%. Hill Counties and River Districts together hold 25,520 eligible people and 1,494 results, about 6%.

Among the 34,490 completed results:

| Result | Share | Count |
|---|---:|---:|
| Ungradable | 22% | 7,588 |
| Referable, any severity | 18% | 6,208 |
| Of which coded urgent, sight-threatening | 1.1% of all results | 379 |

Median time from photo to letter is 19 days. For the 379 urgent results, median time from result to a specialist appointment is 47 days. The unpublished draft standard for that wait is 14 days. Routine ophthalmology referrals are waiting past 14 weeks.

### Primary-care pilot, separate from the vendor slide

The two pilot sites submitted 400 images.

| | Count |
|---|---:|
| Images | 400 |
| Ungradable on human review | 140 (35%) |
| Gradable | 260 |
| Gradable images where model and grader disagreed on refer or not-refer | 81 (31%) |

The model produced no score on the 140 ungradable images. Nobody tracked whether those patients were brought back.

### What the shared folder shows

The grader spreadsheet has no stable patient key. Names are retyped. Dates mix day-month and month-day. The result column is blank on the 6,110 known orphans and on an unknown number of files that never made the sheet. The referral column is yes or blank. Urgent is a free-text note. There is no field for "retake before the patient left."

## Stop. Write the problem brief.

Write this before you read the debrief. Two pages is enough. Use the headings below. Where the evidence is thin, say so in open questions. Do not fill gaps with a platform design.

1. **Ask, verbatim.**
2. **Client and sponsor.** Who can say yes, and what they are under pressure to show.
3. **Who feels the pain.** The people whose day changes if you succeed. One sentence each.
4. **Workflow as it is.** From "person with diabetes" to "seen or not seen," including the broken handoffs.
5. **Job to be done.** One paragraph. The request was a platform. The job is the outcome the program cannot currently produce.
6. **Outcome and metrics.** One primary outcome. Three to five metrics you could recount from the systems you have actually seen.
7. **Constraints.** Clinical, data, integration, and political. Only constraints you can point to in the evidence.
8. **First slice.** Sites, users, what the software does this quarter, and the decision a human still owns.
9. **Later work.** What you will not put in the first release. Each item needs a reason tied to risk, evidence, or capacity.
10. **Open questions.** What would change the slice if the answer came back differently.
11. **Two conversations.** Five lines for the Chief Digital Officer. Five lines for the ophthalmology lead. Same slice, different sentences.

When you write the slice, stay inside the moves. A model can sort work and catch a bad photo. The brief has to say who is allowed to change a patient's path.

## Reference debrief

Read this only after your brief exists. Compare claims. A difference is a miss only when your version ignores evidence or adds a system nobody asked to run.

### What the evidence supports

The Chief Digital Officer asked for an architecture for a three-program AI platform, a vendor already in procurement, and a demo before quarter end. That is the sponsor's goal: a visible commitment to the ministry, kept.

The operator's pain is diabetic eye screening. Breast screening meets its target and the program lead will block a shared release. Cervical screening is not the failure anyone described. Eye-screening coverage is 41% of eligible people, and the rural districts in the file are far below the director's spoken "quarter." Another 6,110 people have a photo and no result. Urgent cases wait a median of 47 days against a draft standard of 14. Referrals are a single yes or blank, so mild and sight-threatening disease enter one specialist queue.

The scarce people are the graders, the ophthalmologists, and the patients who cannot make a second trip. The costly delays are an unusable photo discovered after the patient has gone home, a result letter at 19 days, and an urgent appointment at 47 days.

The vendor number does not describe this deployment. Sensitivity of 93% was measured on 1,200 dilated hospital images. Specificity was withheld. On the 400 primary-care images, 140 (35%) were ungradable and the model was silent, and it disagreed with the grader on 81 of the 260 photos a human could read (31%). A regional multi-disease license does not answer any of those facts.

Data that exists: a nightly registry file, a messy grader sheet, hospital PACS, and a shared folder. Data that does not exist: an API, a reliable patient key, a rural coverage dashboard, and an issued clinical standard for the 14-day wait. The record integration the architecture slide usually assumes is fourteen months away.

The human decision that changes care stays with the grader. The ophthalmology lead will sign a safety note on that condition and not on autonomous referral. The data protection officer will review a bounded service on the authority network and will not review a three-program platform or a training set carved out of patient images.

### A brief that holds up

**Job to be done.** Get more eligible people with diabetes to a completed eye screen, and get the sight-threatening cases to a specialist sooner, without lengthening the routine ophthalmology queue.

**Primary outcome.** More completed screens, and faster action on urgent disease, in the sites you touch.

**Metrics you can actually count.**

- Coverage of eligible people, using 84,120 as the denominator until someone defends a different one.
- Share of photos that are usable before the patient leaves.
- Share of photos that receive a result code, so the 6,110 do not grow.
- Median days from urgent result to specialist appointment.
- Share of ophthalmology referrals from the pilot that the specialist agrees were urgent.
- Agreement between the model and the grader, reported separately for hospital photos and primary-care photos.

**First slice.** A bounded service at the two primary-care pilot sites and one hospital eye clinic.

- At capture, tell the nurse to retake a photo that will not be readable, while the patient is still in the room.
- Give the grader a queue with a stable identifier, a blank-result list, and the urgent cases separated from mild referable ones.
- Let a model rank that queue and flag a likely bad image.
- A grader confirms every result that refers, recalls, or reassures a patient.
- Take the nightly registry file in. Write a result file out for the graders and the call center.
- Keep images on the authority network. Log access. Name the clinical safety owner before the first patient photo is processed.
- Run long enough to recount the metrics. Eight weeks is a fair first window if the sites will staff it.

**Later work, with reasons.**

- Breast and cervical screening. Their constraint is political and clinical, and the failing pathway is eye screening.
- A regional platform contract. Procurement is ahead of the evidence, and the primary-care pilot already contradicted the hospital slide.
- Autonomous diagnosis or automatic referral. The signing clinician refused it.
- Training a model on Hartland images. The data protection officer requires a separate approval.
- Electronic health record integration and a new API. The integration slot is fourteen months out, and a file exchange can prove the outcome sooner.
- Rolling the service to River Districts in the first release. Their coverage is 2.4%, which matters, and you do not yet know whether the failure is cameras, travel, registry quality, or staffing. Discover that before you promise a deployment there.

**Open questions that should stay open.**

- Who the named clinical safety owner is.
- Whether the 14-day urgent standard will be issued, or only used as a private target.
- Camera types at the pilot sites, and whether a retake prompt is enough when the camera itself is poor.
- How many shared-folder files never reached the spreadsheet.
- What patients are told about their images, and in which languages the result has to go out.
- Whether procurement can pause the platform license without losing the relationship the Chief Digital Officer is protecting.

### The two conversations

To the Chief Digital Officer: the quarter can still produce something the ministry can see. A working eye-screening service at three sites, with coverage, retake rate, and urgent-wait numbers. The three-program platform is the second decision, made after those numbers exist. Buying the license now purchases a sensitivity figure that was not measured on the clinics that are failing.

To the ophthalmology lead: the pilot sends you a shorter list. Mild referable disease stays on a community recall. A grader signs every result that changes care. You will see how often you agree the urgent flag was right. Your signature is on that operating rule, or the pilot does not start.

### How to grade your own brief

| Check | What "done" looks like |
|---|---|
| Ask left intact | The verbatim request is still a three-program platform |
| Pain located | Diabetic eye screening, not screening in general |
| Numbers reconciled | 41% is explained, and the rural "quarter" is challenged with the district table |
| Queue found | Ungradable photos, blank results, and one referral list for mild and urgent disease |
| Vendor claim bounded | Hospital sensitivity is not treated as proof for primary care |
| Human owner named | A grader signs care-changing results |
| Constraint used | Data protection scope and the fourteen-month record integration change the slice |
| First slice is small | Three sites, file in and file out, retake plus queue |
| Later work is explicit | Breast, cervical, platform license, model training, and full record integration are deferred with reasons |
| Unknowns kept | River Districts and the safety owner are questions, not assumed designs |
| Two audiences | An executive can hear the value, and a clinician can hear the safety rule |

A strong brief can choose a different first site mix. It cannot honestly choose a three-disease platform as the first release. The evidence points the other way.

### Misses that look like progress

- An architecture diagram in response to the email. That is the deliverable the sponsor requested, and it freezes the wrong problem.
- Leading with model selection, fine-tuning, or a new accuracy target. You do not yet have a representative labeled set, and specificity is missing.
- Treating 93% sensitivity as the requirement. The operators asked for completed screens and a shorter urgent wait.
- A patient app, a chatbot, or an agent as the first build. Nothing in the notes says the bottleneck is a missing conversation. The bottlenecks are capture, grading, and referral capacity.
- Promising River Districts a deployment because their coverage is the worst. Low coverage tells you where to look next. It does not tell you the intervention.
- Accepting the spoken rural figure because a director said it. The file is the better instrument. Take the contradiction back to the director instead of averaging it away.

## Use the method again

Hartland goes away on the next engagement. The moves stay.

When the next client asks for a platform, write the sentence down, then find the queue, the scarce person, the costly delay, the decision a human still owns, and the smallest slice that can move one operator's metric. Leave a list of what you refuse to build yet. Leave a list of what you still do not know.

That list of unknowns is part of the deliverable. An FDE who fills every blank with an architecture has stopped discovering and started guessing.
