---
id: NET-MIGRATE
title: A map of leftovers on the shelves, with no list of work to construct
date: 2027-01-08
type: packet
author: Bobbi Tran
participants:
  - Bobbi Tran
  - Harper Singh
  - Wes Calder
  - Sam Nguyen
systems:
  - hospital log
  - channel log
  - payer log
  - phone field
  - cedar ridge night file
access: student
---

# NET-MIGRATE

Bobbi Tran, information technology, Northline Access Collaborative, Vancouver desk. Friday, 8 January 2027. The office week is Monday through Friday. Today is an office day. The wall clock is America/Vancouver. I am writing this at the integration shelf, which is the shelf Harper Singh left when he left the seat in March 2026. The shelf still has his March handover, my December year leaf, and a stack of year pages that go back further than my hire. I made tea in the closet kettle and left the mug on a coaster. The coaster is not a leftover of a migration. I am mentioning it so a later reader does not file the mug ring as a fifth log.

This page is a map of leftovers. A leftover, as I am using the word, is something that is still on a shelf or still in a file after a later page has been written beside it. I am mapping five of them: the spreadsheet years, the three logs, phones in two shapes, Cedar still on a file, and the 2019 page. The order is the order of the shelves from the door to the window. Shelf order is not a sequence of work. I am not closing any of the five. I am not writing, under any of them, a list of things for a person to construct.

Harper's last day in the integration seat was Thursday, 5 March 2026. I wrote a handover note on Friday, 6 March. I am not replacing that note. YR-2026, which I filed on 18 December 2026, listed open items and did not close them. Today is three weeks after that Friday. The items are still open. January has not retired December.

## Spreadsheet years

The year drawer still holds the leaves. I can put a hand on YR-2018, YR-2019, YR-2020, YR-2021, YR-2023, YR-2024, YR-2025, and YR-2026 without inventing a year that is not in the drawer. I am not ranking the leaves. I am saying they are still there, paper years, after the logs have also been there.

The leaf I keep being handed, when a clerk asks what a Harbor file or a Cascade file used to be, is YR-2021. June Lau wrote it on 19 November 2021. The title on it is that Harbor and Cascade still arrive as spreadsheets. She wrote that a shared book had not replaced the sheets. Harbor's workbook, in that leaf, comes from Ruth Alvarez, or from the mailbox Lena Brooks's office uses when Ruth is not the one who attaches it. Cascade's workbook comes from Jordan Hale, or from the night tray when Omar Farouk's shift has put a workbook on the wire. June wrote that the columns are not the same columns. She wrote that a referral code typed into both workbooks is two typings, not a table both of them write. She wrote that she had not been offered a login to either book. She had been offered spreadsheets.

The time cells on those workbooks are the part she asked a later reader to leave alone. Harbor's sheet can carry the time Ruth's office recorded and the time a notice was printed. Cascade's sheet can carry the time Jordan's room wrote and the time a night export was saved. June's own working sheet can carry the time she typed the row, a Vancouver afternoon on a weekday. She wrote that she had not picked one of them for a display. I am not picking one now, from information technology, in order to make the year drawer look finished. The cells remain cells. The leaves remain leaves.

A spreadsheet year is a leftover because the logs I keep are not those workbooks, and the workbooks were not thrown out when the logs were described. I still get asked to open a workbook when a file will not open. Opening a workbook is not a merge of the workbook into a log. I have not converted the year leaves into one table. I have not relabeled June's 2021 sentences as a schema. Chris Pell still does not want a currency code tidied before he sees the cell. I leave the code as the cell has it when a workbook is what I was handed. A tidy code would be a code I had chosen. I have not chosen one on this map.

Fraser Burnaby, in that same 2021 leaf, does not send those workbooks. Anita Desai's office is a hospital in British Columbia. Priya Shah's name appears on clinical paper that June said she does not retype into Harbor's columns. I am not pulling clinical paper into this map in order to give the spreadsheets a clinical sentence. The spreadsheet leftover is the file Harbor or Cascade sent, and the year pages that still describe that habit.

## The three logs

I keep three logs. Their names are hospital, channel, and payer. They share one SQLite file, `var/log.sqlite`, and they do not share a table. The tables are `log_hospital`, `log_channel`, and `log_payer`. A command names its authority. The writer accepts those three names. Harper's note TECH-LOGS-2026, dated 1 October 2026, is his last edit before he left the seat, and it is still the note on the shelf. SPEC-LOGS, dated 15 October 2026, is beside it. I am not merging those two notes into a third note that picks a wording.

Each log row holds `seq`, `event_id`, `type`, `occurred_at`, `stream_id`, `stream_rev`, and a payload stored as text. `seq` is the primary key of that table. Update is rejected. Delete is rejected. A command that tries to install one shared clock is rejected. The writer refuses a payload that carries a shared instant for every authority. Each stored event keeps the time that arrived with it. `occurred_at` on the hospital log is the string the hospital command brought. `occurred_at` on the channel log is the string the channel command brought. `occurred_at` on the payer log is the string the payer command brought. Those strings are not converted onto one another when they are appended.

There is no foreign key from a hospital row to a channel row, or from a payer row to either of the others. A referral string copied into more than one payload is text in more than one place. The file does not declare it as a key. I do not have a join I am willing to pretend the file enforces. When I read, I read one table at a time. In the autumn a new hire added two seq counters together because the digits looked alike. I had them read the afternoon again. Two counters that show the same digits are two counters. `seq` counts inserts on that table alone. I am not adding the counters together on this map.

Projections, when they are built, are built one log at a time into `var/proj/hospital.sqlite`, `var/proj/channel.sqlite`, and `var/proj/payer.sqlite`. A projection replaces the projection file it is writing. It does not join the three logs. The local reader binds on this machine. It reads extracts. It does not append. I am describing the files I keep. I am not describing a different machine I have been asked to stand up. No account is open. I am not loading a job into a remote account, because there is no account in the note I am mapping.

The three logs are a leftover in the sense that they sit beside the older claim, further down this page, that there is one table and one instant. Both the three-log note and the one-table page are on the shelf. I have not taken either down.

## Phones in two shapes

Phones are in two shapes. I have not chosen a shape.

The older shape is digits. The field name is `phone`. The form name on the 2025 schema note is `digits`. The example on that note is `6045552701`. The person id on the note is `p-r2f-2701`.

On the channel log, stream `r2f-schema`, command `cmd-r2f-schema-1` is a SchemaEpoch at stream revision 1. `occurred_at` is `2025-01-15`. The payload says field `phone`, form `digits`, example `6045552701`.

On the channel log, stream `r2f-phone`, command `cmd-r2f-phone-digits` is a PhoneRecorded at stream revision 1. `occurred_at` is `2025-04-11T17:20:00Z`. The payload stores form `digits` and phone `6045552701` for person `p-r2f-2701`.

On the payer log, stream `r2f-member`, command `cmd-r2f-payer-digits` is a PhoneFiled at stream revision 1. `occurred_at` is `2025-04-11T19:05:00Z`. The payload stores the same person, the same form `digits`, the same phone `6045552701`, and referral `R2F-2701`. That payer row is its own append. It is not a foreign key back to the channel row. The channel `occurred_at` and the payer `occurred_at` are two strings. I am not sorting the channel log and the payer log together and calling that the moment the number was captured.

The later shape is dashed. On 1 June 2026 the channel log took a second schema append. Command `cmd-r2f-schema-2` is a SchemaEpoch on stream `r2f-schema` at stream revision 2. `occurred_at` is `2026-06-01`. The payload says field `phone`, form `dashed`, example `604-555-2701`, person `p-r2f-2701`. That schema row does not edit revision 1. Revision 1 still says `digits` and still shows `6045552701`.

Harper wrote RUN-MIGRATE on 2 June 2026, just before new phone rows took the dashed form. He wrote that old rows were not rewritten. He wrote that the digits `6045552701` and the dashed string `604-555-2701` are the two shapes of this one synthetic member number. He wrote that a sheet which shows a single phone column has collapsed two stored strings into one display, and that the log did not collapse them. He wrote that he was not adding a check that strips hyphens before insert. I have not added that check since he left. I have not deleted `6045552701`. I have not padded it with dashes in the stored text. I have not stripped the dashes off a later row to make it match the earlier one. Update is not how these tables are kept. Delete is not how these tables are kept.

In YR-2026 I listed both shapes and said I had not chosen. On this Friday in January the rows are still both shapes. A clerk who searches will find both and may think I forgot to pick. I did not forget. The map records the two strings. The 2021 spreadsheet leaf, above, describes a telephone column of digits, examples `6045550136` and `2065550148`, with no dash. That leaf is a year. It is not a rewrite of the 2025 digits row, and it is not a rewrite of the dashed schema append. Three descriptions of a phone can sit in one building. I am mapping them. I am not issuing a habit for every notebook.

June Lau and Noel Park can ask me which characters are on a phone row, and I will quote the row they named. I will quote `6045552701` when the row they named is the digits row. I will quote `604-555-2701` when the row they named is a dashed row. I will say which command id I read. I will not quote the other shape and call it a correction of the one they asked about.

## Cedar still on a file

Cedar Ridge is still a nightly file. It is a rural clinic in Washington. It files at night, including Saturday and Sunday. It has no slot line the desk can call. Sam Nguyen is the night file clerk. The Vancouver office week is Monday through Friday. A weekend file does not become an office-day row because I am writing on a Friday. I am not flattening Sam's packet into Ruth's columns so that a week looks like one grid. June wrote that refusal in 2021, when Inlet Medical was still its own clinic. I am writing the later state, which is not the same state, and I am not erasing her sentence in order to make the later state the only sentence.

Inlet Medical merged into Cedar Ridge on 2026-09-01. I was not the clerk who rolled the cabinet. Sam wrote the night book on 2 September. The chart in the jacket is referral R3A-MERGE. He had two file names in the tray: inlet-2026-11-02 still arriving under the old site id inlet-medical, and cedar-r3a-2026-11-02 under the site id cedar-ridge. He did not strike either name. He wrote that he does not know which id the payer uses. I do not know either. I have not retired inlet-medical on the files that still carry it. The old site id still appears. Anita Desai wrote, in the week after the join, that Inlet's charts are not Fraser's cabinet. I am not moving them onto Fraser in order to give the map a single site.

Cedar is still on a file. That is the sentence I want in the middle of the map, in plain words. The cedar name is a file id on paper, cedar-r3a-2026-11-02, next to the older file id that the join did not strike. The clinic itself is still a nightly file, not a slot line. Both of those are leftovers. Neither one is a site id I am choosing for the chart.

There is an older remainder on the same theme. Sam's August 2025 notebook still has two counts on cedar-2025-08-16. I have not picked 11. I have not picked 14. The file id is still the file id. The two counts are still the two counts. I am not using January to finish an August notebook.

CASE-MERGE-FILE is still open in the jacket Sam keeps. I am not closing it from this shelf. Pat Morales asked, in October, which historical files stay under the old site id. Sam did not name a winner. I am not naming one from the logs. The logs have the rows they have.

## The 2019 page

The 2019 page is still linked. The page is TECH-CLOCK-2019. The title is "Canonical instant for every feed." The date on it is 2 April 2019. Wes Calder wrote it. Wes left in 2020. The status printed on the page is still the status that was printed when Harper clicked the link in March and did not take it down. I have not removed the link. I have not written a sunset. I have not written a banner that would tell a clerk the page is historical only.

The page says the hospital feed, the channel feed, and the payer feed are stamped with one canonical instant. It says local clocks are display offsets. It says the facility mart is that instant. It says a nightly file does not bring its own night. Beside it on the shelf is SPEC-OLD-FEED, 1 May 2019, also Wes, which describes one table and one timestamp, and says there is no second table for the hospital, no second table for the channel, and no second table for the payer. Beside those two is HIST-ONE-CLOCK, a draft, effective date 1 June 2019, status not adopted. Harper said, and I repeated in December, that the three logs do not share a clock, and that the 2019 page still claims they do, and that he would not say what a screen should use. I am not saying it for him. The disagreement is still a disagreement.

I am mapping the page as a leftover link. The link is a fact about the shelf. The three logs are a fact about the file. The spreadsheet years are a fact about the drawer. I am not saying the logs have defeated the page. I am not saying the page has enacted itself on the logs. I am not saying the spreadsheets have done either of those things. A reader who sorts the shelf by date will find 2019 before 2021 before 2026. Date order is not a rank. I am not applying the page to a phone string, and I am not applying it to a Cedar file id, and I am not applying it to a time cell in a workbook.

## What the map is

The five leftovers, in shelf order, and not as a sequence of work:

1. Spreadsheet years. Harbor and Cascade workbooks, and the year leaves that still describe them, including June's 2021 leaf. Time cells are still cells. I have not made the leaves into one table.

2. The three logs. Hospital, channel, and payer, in `var/log.sqlite`, without a shared table and without a shared clock. I read one table at a time.

3. Phones in two shapes. Digits `6045552701` on the older rows, dashed `604-555-2701` on the later schema append. Old rows were not rewritten. I have not chosen a shape.

4. Cedar still on a file. The clinic is still a nightly file. The file ids inlet-2026-11-02 and cedar-r3a-2026-11-02 are both still in the R3A-MERGE jacket. The old site id still appears. The August 2025 counts 11 and 14 are both still on cedar-2025-08-16.

5. The 2019 page. TECH-CLOCK-2019 remains linked. SPEC-OLD-FEED remains beside it. HIST-ONE-CLOCK remains a draft that was not adopted. I have not taken the link down, and I have not signed the page onto the logs.

None of these items tells a screen which clock it may use. I am not adding that sentence in the form of an answer. If a person came to this page hoping to be told what to construct, the page does not contain that list. The shelves contain what they contained this morning. Copies of this map go to the integration shelf, to my own book, and to Dana Okonkwo's shelf so the list is not only in my notebook. I am not sending it to Harper. I am not sending it to Wes. Nothing under my signature on this Friday retires a link, rewrites a phone, retires a site id, or paints a time.

I will not choose.
