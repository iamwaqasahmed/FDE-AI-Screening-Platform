---
id: SES-BOBBI
title: How I read the three logs
date: 2027-01-23
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

Discovery interview with Bobbi Tran, IT, Northline Access Collaborative. 23 January 2027. Saturday. The Vancouver desk is in British Columbia. The office week is Monday through Friday, so the counter is shut. Bobbi is not opening the counter. She is talking about the three logs she keeps, from the machine, not from the phone bay.

**Interviewer:** How do you read the three logs?

**Bobbi Tran:** One at a time. I open `var/log.sqlite` on this machine. I look at `log_hospital`, then I close that result, then I look at `log_channel`, then I look at `log_payer`. I write three notes. If the notes have become one sorted column, I start again. That is the reading. I have said it to every new hire since November, and I am saying it on a Saturday because the file does not become a different file when the counter is shut.

**Interviewer:** Walk me through a first pass, as if I had the file in front of me and I was about to do it wrong.

**Bobbi Tran:** List the table names. Confirm you see those three and not a fourth. Read a handful of rows from one table, ordered by `seq` on that table. Read `occurred_at` as text. Read the payload as text. Then stop. Do not paste the next table underneath it. Hospital work from Cascade Seattle, Cedar Ridge, and Fraser Burnaby lands on `log_hospital`. Channel work from this desk lands on `log_channel`. Harbor Coverage lands on `log_payer`. A referral code copied into two payloads is text in two places. It is not a join the file enforces. I don't have a foreign key between them, and I don't want you to invent one with a spreadsheet.

**Interviewer:** Do the three logs share a clock?

**Bobbi Tran:** No. The three logs do not share a clock. The hospital log keeps the time string that hospital wrote. The channel log keeps the time string that channel wrote. The payer log keeps the time string that payer wrote. Those strings are not converted onto one another when they are appended. I store the string the command brought. I do not keep a second column that lines the three logs up. A command that tries to install one shared clock is rejected. I have watched people try. The writer refuses it.

**Interviewer:** If I sort all three by the time string and call that the order of the day, what have I built?

**Bobbi Tran:** A sheet you made. Not the day. I need you to hear that without a softer version. Do not sort the three logs together and call that the order of the day. Sequence is append order on one table. A higher `seq` on the hospital table can carry an earlier time string than the row above it, because the log appended when the command arrived and the authority wrote the time it wrote. Cedar Ridge files at night, including weekends. The office week here is still Monday through Friday. A weekend file does not become an office-day row because you sorted it next to a Friday channel line.

**Interviewer:** What is `occurred_at`, in your mouth, when someone asks you what the column means?

**Bobbi Tran:** It is the time that authority wrote on the event, stored as the string they sent. It might be a full instant. It might be a calendar date. I read what is stored. I do not finish it into a shared instant so the three rows look cooperative. Harbor uses Canadian dollars and US dollars. Currency is a field on a payer row. It is not a clock, and it does not pull the other two logs onto the payer's string. I am telling you how I read. I am not telling you what to print in front of a member.

**Interviewer:** The number 40 on the hospital table and the number 40 on the payer table. One counter?

**Bobbi Tran:** Two counters that happen to show the same digits. `seq` counts inserts on that table alone. I had a new hire last autumn add them together. I made them do the afternoon again. Same digits, different tables, not one day. If you quote me as saying the forties line up, you have quoted the mistake, not the reading.

**Interviewer:** A clerk asks you to delete a row because the story feels messy. What happens?

**Bobbi Tran:** I refuse. Update is rejected. Delete is rejected. The triggers abort both. A correction, if an authority sends one, is a later append. The earlier row stays, with the payload it had when it was inserted. I have watched people hover over a delete button in a browser. The button is not the log. I am not going to reach into a table and erase a first row because a night clerk, or a supervisor, is unsure. Sam Nguyen can be unsure. I still do not delete.

**Interviewer:** The 2019 clock page. Is it still linked?

**Bobbi Tran:** I— I was about to say I took it down when Wes Calder left. That is wrong. Wes left in 2020. He wrote that page. I have not taken the link off. The first-week list still points at it, the page titled as the canonical instant for every feed, dated 2 April 2019. I left it on the list as background, next to Harper Singh's logs page. Harper left in March 2026. His page is the one I want open beside the file. The 2019 page is still linked. I had the history wrong for a second, and I am correcting it. It is still linked.

**Interviewer:** Will you unpublish it now, on this call, so the new hire does not read it?

**Bobbi Tran:** No. I do not unpublish it in this interview. I am not walking over to the list and pulling the link while we are talking, and I am not telling you I already did. I mentioned it because it is still there. Mentioning it is not the same as taking it down. If someone wants it unpublished, that is a later act, by a person who is doing that act. I am not doing it today. It is Saturday, the counter is shut, and I am not using a shut counter as cover for a quiet edit.

**Interviewer:** What does that page claim, as a page, when a new hire actually opens the link?

**Bobbi Tran:** It claims the feeds share one instant, and that the facility mart is that instant. Wes believed one instant would end the arguments. I can tell you what the page says because I have left the link up and I have read it. I can also tell you what I see when I open the file. The three logs do not share a clock. Both of those things are in the building this week. The page claims one thing. The logs I read do another. I am not standing over Wes's page with a pen. I am not handing you a corrected page on this call.

**Interviewer:** A supervisor will ask you which of those a screen should follow. What do you answer?

**Bobbi Tran:** I answer that I read the logs, and that I am not choosing a time for a screen. Dana Okonkwo keeps the operations ask. I keep the file. I will show you the row. I will tell you which table I opened, which `seq` I saw, and which `occurred_at` string was on it. Then I will open the next table and do it again. I will not sort the three logs into her slide. I will not say the 2019 page wins, and I will not say I have unpublished it, because I have not.

**Interviewer:** Today is Saturday. Cedar Ridge may have filed last night. Does a weekend row change the way you read?

**Bobbi Tran:** No. A Cedar Ridge night file, Saturday included, is a hospital append if it was sent as hospital. It lands on `log_hospital`, with the time string that append brought. It does not move onto the channel log because the Vancouver office is dark, and it does not pull the payer log with it. There is no slot API at that clinic. The absence of a slot line is not a shared clock. I read the hospital table. Then I stop. Then I read another table, if I have a reason to.

**Interviewer:** You said you would not delete a first row even if Sam is unsure. Have you checked whether his first row is still there?

**Bobbi Tran:** I have not. He did not ask me. I am not going to pretend I looked, and I am not going to look up HX-0045 in the middle of this answer and call the look a finding. I don't know, from this chair, whether that first row is gone. Delete would be rejected if someone asked me to make it gone. Not knowing is not the same as deleting. I am leaving his question as his question.

**Interviewer:** Harbor's rows can be CAD or USD. Does a difference of currency tell you the logs share a clock, or that they don't?

**Bobbi Tran:** Neither. Currency is not how I read time. I read three tables, three time strings, no shared clock. A CAD row and a USD row are payer rows. They do not merge the hospital log into the payer log. I am not going to let a currency code become a theory of time on a Saturday. Lena Brooks can ask finance what a member was sent. That question is not a sort of my file.

**Interviewer:** Harper's 2026 page and Wes's 2019 page are both still available to a new hire. Which one do you tell them to use for the file?

**Bobbi Tran:** Harper's, for the file they are about to open. The 2019 page stays on the list as background. I am not unpublishing it in this interview. I am also not going to pretend the background page describes the clocks I actually read. The three logs do not share a clock. I read them one table at a time. I do not sort them into one day. That is the reading. The link stays until someone, not me in this conversation, takes it down.
