Interviewee: C. Halvorsen, Vendor Account Manager. Held on 2026-10-13.

**Interviewer:** Thank you for joining us. I would like to clarify the service interruption history first, then confirm how image quality affects processing.

**Interviewer:** Has the API experienced an outage associated with an infrastructure problem?

**C. Halvorsen:** Yes. Our API was down on 2025-11-18 after a cloud region failure.

**Interviewer:** Was that related to the cloud environment rather than an issue with an individual user request?

**C. Halvorsen:** That is correct. The cause was a cloud region failure, and the API was unavailable during that event.

**Interviewer:** I would also like to understand what the system does when an image does not meet the required quality standard. Are those images processed normally, or are they screened out?

**C. Halvorsen:** They are screened out when the quality is below the applicable threshold.

**Interviewer:** To make the rule explicit, what happens to images below that threshold?

**C. Halvorsen:** Images with a quality below 0.3 are rejected and get no score.

**Interviewer:** So an image below the threshold is not assigned a partial or provisional result?

**C. Halvorsen:** No. Images with a quality below 0.3 are rejected and get no score.

**Interviewer:** Understood. The key points are that the API interruption followed a cloud region failure, and that images below the stated quality threshold are rejected rather than scored.

**C. Halvorsen:** Yes, that accurately reflects the process.

**Interviewer:** Is there anything you would like to clarify about either point?

**C. Halvorsen:** No. Those are the relevant details.

**Interviewer:** Thank you. That answers the questions for this interview.
