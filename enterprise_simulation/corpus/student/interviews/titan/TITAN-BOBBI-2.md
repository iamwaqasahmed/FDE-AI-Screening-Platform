---
id: TITAN-BOBBI-2
title: Cursors, amount 90, and a link I have not taken down
date: 2027-01-28
type: interview
participants:
  - Bobbi Tran
  - Discovery interviewer
systems:
  - hospital log
  - channel log
  - payer log
access: student
---

Discovery interview with Bobbi Tran, IT, Northline Access Collaborative. 28 January 2027. Thursday, an office day. The Vancouver desk is in British Columbia. The office week is Monday through Friday. The counter is open. Bobbi is talking about rows she already wrote down, from the logs on the desk machine. She is not opening a second account somewhere else.

**Interviewer:** What did you see when you opened the hospital log for R3E-SYNC?

**Bobbi Tran:** I saw two cursor rows and two export rows, and I am going to describe them as I saw them. Both cursor rows are hospital events of type ReplicaCursor. Both name source stream r3e-sync and file cedar-r3e-2027-01-18. On cedar-copy I saw seq_caught 14. The command id on that row is cmd-r3e-cursor-cedar. The stream id is r3e-cedar-copy. The occurred_at string is 2027-01-18T22:10:00Z. On cascade-copy I saw seq_caught 10. The command id is cmd-r3e-cursor-cascade. The stream id is r3e-cascade-copy. The occurred_at string is 2027-01-18T22:16:00Z. I wrote 14 beside cedar-copy and 10 beside cascade-copy because that is how the rows were stored when I looked.

**Interviewer:** Which of those copies is current?

**Bobbi Tran:** I am not saying which copy is current. I am describing what I saw. Fourteen is the seq_caught on the cedar-copy cursor row. Ten is the seq_caught on the cascade-copy cursor row. They are two numbers on two rows. A larger number is not a sentence I am willing to say out loud as "current." I will not say cedar-copy is current. I will not say cascade-copy is current. I saw 14 and I saw 10.

**Interviewer:** And the amount?

**Bobbi Tran:** Amount 90 is on both export rows. Both are hospital events of type ReplicaExport. Both name the same source stream and the same file id. On cedar-copy the export command is cmd-r3e-export-cedar, occurred_at 2027-01-19T14:40:00Z, amount 90, currency USD. On cascade-copy the export command is cmd-r3e-export-cascade, occurred_at 2027-01-19T14:46:00Z, amount 90, currency CAD. I saw 90 with USD on one row and 90 with CAD on the other. I am describing the rows. I am not saying which currency is the one that counts, and I am not saying which copy is current.

**Interviewer:** Those export rows are on the hospital log. Harbor's payer log can also carry CAD and USD. Did you move the 90s onto the payer log so they would share a table?

**Bobbi Tran:** No. I read log_hospital for the hospital rows. The amount-90 rows are on the replica streams in that log. They are not on log_payer. Harbor Coverage can carry CAD or USD on a payer row. That fact does not pull these two rows onto the payer log. I did not edit either payload. Update is rejected. Delete is rejected. I am not sending a later append in this interview to force one code. I saw two codes. I am leaving them as two codes.

**Interviewer:** Chris Pell asked you which figure the finance pack should treat as the one that counts. What did you give him?

**Bobbi Tran:** I told him I would write down what I saw. The writing is the two cursors and the two amounts. seq_caught 14 on cedar-copy. seq_caught 10 on cascade-copy. Amount 90 USD on the cedar-copy export. Amount 90 CAD on the cascade-copy export. I did not add those payload numbers to the table's seq, and I did not subtract them. I did not tell him which copy is current. If he needs a winner, he does not have one from me.

**Interviewer:** A desk note says the morning board was printed from cascade-copy. Does that note make cascade-copy current?

**Bobbi Tran:** The note is a sentence I copied off a channel row. DeskNote, stream r3e-desk, command cmd-r3e-desk-note, occurred_at 2027-01-19T15:26:00Z. The sentence stored there is "The morning board was printed from cascade-copy." I copied it because it was the note on the row. A note that names a print source is an additional channel append. It is not me saying cascade-copy is current. It is not me saying cedar-copy is current. I am not promoting the note into a status word the cursor rows do not have.

**Interviewer:** The 2019 page. Is it still linked?

**Bobbi Tran:** Yes. It is still linked. I was about to say, in another sitting, that I took it down when Wes Calder left, and that was wrong, and it is still wrong. Wes left in 2020. He wrote the page. The title is the canonical instant for every feed. The date on it is 2 April 2019. The first-week list still points at it. Harper Singh left in March 2026. His logs page is the one I want open beside the file. The 2019 page is still linked. I have not taken the link off. I am not taking it off in this interview.

**Interviewer:** The page claims the feeds share one instant. You have said the logs do something else. Will you unpublish the page so a new hire cannot be confused?

**Bobbi Tran:** No. I do not unpublish it in this interview. The page claims one instant. What I see when I open the file is that the three logs do not share a clock. I can say both of those things because both are in the building. I am not standing over Wes's page with a pen. Mentioning the link is not the same as taking it down. It is Thursday, the counter is open, and I am still not using the open counter as cover for a quiet edit. The 2019 page stays linked.

**Interviewer:** Do the three logs share a clock?

**Bobbi Tran:** No. The three logs do not share a clock. I open var/log.sqlite. I look at log_hospital, then I close that result, then I look at log_channel, then I look at log_payer. Hospital work from Cascade Seattle, Cedar Ridge, and Fraser Burnaby lands on log_hospital. Channel work from this desk lands on log_channel. Harbor lands on log_payer. The occurred_at value is the string that authority wrote, stored as text. I do not keep a second column that lines the three logs up. A command that tries to install one shared clock is rejected. I did not send one while I was reading these rows.

**Interviewer:** There is also a SlotFiled row on that hospital stream. What was on it, and does it tell you the current copy?

**Bobbi Tran:** It tells me what was on the row. occurred_at 2027-01-18T21:00:00Z, stream revision 1, referral R3E-SYNC, file id cedar-r3e-2027-01-18, site cedar-ridge, clinic ENDO-CLN, state WA, trailer_ok true, trailer_count 8, body_count 8, booking date 2027-01-18. Cedar Ridge has no slot API. The hospital log records the nightly file as an append. I am not describing a slot line I called, because there isn't one. The cursor rows name that file id. Naming it is not me saying which replica is current. I saw the slot row. I saw cursor 14 and cursor 10. I am not ranking the copies.

**Interviewer:** You also copied two handset rows on the channel log. Are those the same fact as the cursors?

**Bobbi Tran:** They are channel rows. I opened log_channel separately. Two HandsetDispatch rows share idempotency key r3e-sms-1 and the same file id, on stream r3e-handset. Attempt 1, command cmd-r3e-handset-1, status sent, occurred_at 2027-01-19T15:02:00Z, transcript "Northline visit filed at Cedar Ridge." Attempt 2, command cmd-r3e-handset-2, status redelivered, occurred_at 2027-01-19T15:08:00Z, transcript "Northline visit booked at Cedar Ridge." I copied both. I did not delete the first. A QueueDepth row at 2027-01-19T15:20:00Z records visible backlog 120, oldest age 5400 seconds, and consumer alive true. Those figures are on the channel log for this referral. I am not sorting them under the hospital cursors and calling the sort one clock. The three logs do not share a clock.

**Interviewer:** Fourteen is greater than ten, and the cedar cursor's time string is earlier than the cascade cursor's time string. Does that pair tell you which copy is ahead?

**Bobbi Tran:** It tells you the pair I saw. I am not turning "greater" into "current," and I am not turning "earlier string" into "current." seq_caught is a field inside the payload. The occurred_at values are the strings on those rows. I read them. I do not finish them into a ranking of copies. I do not say which copy is current. Chris can hold both lines. Jordan Hale has the records seat at Cascade. Sam Nguyen sends the Cedar Ridge night file. I have not asked either of them to replace a number or a currency code.

**Interviewer:** A clerk will ask you to finish these rows into one figure for the morning board. What do you give them?

**Bobbi Tran:** I give them the rows as I saw them. I will show the table, the seq, and the occurred_at string. I will not finish 14 and 10 into one copy, and I will not finish the two amount-90 rows into one currency. I will not say the 2019 page has been taken down, because it has not. The page is still linked. The rows are still the rows I saw.

**Interviewer:** Today is Thursday. A Cedar Ridge file can still arrive on Saturday, when this counter is shut. Does a weekend append change which copy you would call current?

**Bobbi Tran:** I am not calling either copy current on Thursday, so a Saturday append is not going to be the moment I start. A weekend file from Cedar Ridge, if it arrives as hospital, lands on log_hospital with the time string that append brought. It does not move onto the channel log because the Vancouver office is dark, and it does not pull the payer log with it. There is no slot API at that clinic. The absence of a slot line is not a shared clock. I would read the new row the same way I read these rows. I would write down what I saw. I would still not say which copy is current.

**Interviewer:** Dana Okonkwo wants one number on a patient screen. Can you give her one number out of 14, 10, and the two 90s?

**Bobbi Tran:** No. Those are different fields on different rows, and her screen is her ask. I keep the file. I am not sorting 14 and 10 and 90 and 90 into her slide. Amount 90 in USD and amount 90 in CAD are both what I saw. Cursor 14 and cursor 10 are both what I saw. One number would be me choosing. I am not choosing. I am not saying which copy is current.

**Interviewer:** A new hire opens the 2019 link first, then opens your note. What do you tell them to do with the two pages?

**Bobbi Tran:** I tell them the 2019 page is still linked, and that I have not taken it down. I tell them to read the logs one table at a time. I tell them the three logs do not share a clock. I tell them the cursors I saw were 14 on cedar-copy and 10 on cascade-copy, and that amount 90 was stored as USD on one export and CAD on the other. I tell them I am not saying which copy is current. If they want a single figure, they can read the note and they still have both. The link stays up. The rows stay append-only.

**Interviewer:** Say the three things you want left in the book, and stop before a fourth thing chooses between them.

**Bobbi Tran:** I saw cursor 14 on cedar-copy and cursor 10 on cascade-copy. I saw amount 90 in USD on the cedar-copy export and amount 90 in CAD on the cascade-copy export. The 2019 page is still linked. I am describing what I saw, and I am describing the link. I am not saying which copy is current.
