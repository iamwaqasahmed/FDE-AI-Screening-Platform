---
id: RUN-ONBOARD
title: First-week reading list for IT
date: 2027-01-04
type: runbook
author: Bobbi Tran
systems:
  - hospital
  - channel
  - payer
  - local-read-api
access: student
---

# RUN-ONBOARD

I am Bobbi Tran. I keep the three logs for Northline Access Collaborative. This is the first-week reading list for a new IT hire on the Vancouver desk, written 4 January 2027. The desk is in Vancouver, British Columbia. The office week is Monday through Friday. The wall clock is America/Vancouver. Cascade Seattle and Cedar Ridge are in Washington and use America/Los_Angeles. Fraser Burnaby uses America/Vancouver. Harbor Coverage is the payer. Dana Okonkwo is operations director. Morgan Ibarra supervises the desk. Evan Cho is the privacy officer. Noel Park and June Lau work the desk. Jordan Hale keeps records at Cascade Seattle. Sam Nguyen sends the Cedar Ridge night file. Chris Pell is finance. You will meet them. You will not need every name on the first morning. You will need the file and the pages below.

No account is open. I am not giving you a login to a cloud account, because we do not have one open, and the logs were not deployed to one. Your first week is this machine: `var/log.sqlite`, the projection files under `var/proj/`, and the local HTTP reader over `student_pack/extracts`. If someone forwards you a diagram of buckets and functions, it is not the system you are operating. Come and show me the diagram before you hunt for it.

## The machine you are learning

The live record is three append-only tables in one SQLite file, `var/log.sqlite`. The tables are `log_hospital`, `log_channel`, and `log_payer`. A command names its authority, and only those three authorities are accepted. `append_all` writes a batch in one transaction, and each command in the batch still lands on the one table its authority names. There is no foreign key from one log to another. A referral code copied into two payloads is text in two places.

Each row holds `seq`, `event_id`, `type`, `occurred_at`, `stream_id`, `stream_rev`, and `payload`. `seq` counts inserts on that one table. `occurred_at` is the time string that authority sent. The hospital log keeps hospital time, the channel log keeps channel time, and the payer log keeps payer time. Those strings are not converted onto one another at append. There is no shared clock. A command that tries to install one shared clock is rejected. The writer refuses a payload that carries a shared instant for every authority, and it refuses a command whose type exists only to set that shared instant.

Update is rejected. Delete is rejected. The triggers abort both, and the abort says that log rows are append-only. A correction is a later append with a new `stream_rev`. Replaying a command id that was already accepted returns the original event id and does not write a second row. I wrote this up for new hires on 1 November 2026 in [How a new hire reads the three logs](RUN-LOGS.md). Read that note on your first afternoon and follow it while the file is open. The instruction in it is the one I repeat in person: do not sort the three logs together and call that the order of the day. Read one table, then the next table. Write three notes. A single sorted column is a sheet you built. It is not the store.

`project` reads one log at a time and writes `var/proj/hospital.sqlite`, `var/proj/channel.sqlite`, and `var/proj/payer.sqlite`. Each projection file is replaced from its own log. It is not a join of the three. The hospital mart keeps a wait figure beside the booking date from the slot payload, and that wait figure is written as 0. A nightly file keeps trailer fields when the hospital sent them. A payer timeout is stored with a null window. Cedar Ridge has no slot API. The night file, including a file that lands on a weekend, is a hospital append. The Vancouver office week remains Monday through Friday. Those are properties of the rows. They are not a merged day.

The desk reads extracts on the local HTTP process. From this tree, `python -m access serve` binds `127.0.0.1` and port 8088 unless you pass another port. It reads every JSON file in `student_pack/extracts`. It does not append to the logs, and it does not open the projection files to answer a request. `GET /` and `GET /health` return a status of up. `GET /extracts` returns the bundle, with keys taken from the file names. `GET /extracts/<name>` returns one file. `GET /ref/<ref>` returns the hits for that referral. Anything else is a 404. Responses are JSON. On Tuesday of your first week, start the reader, open `GET /health`, then open `GET /extracts/hospital`, `GET /extracts/channel`, and `GET /extracts/payer`. Then open the sqlite file and read one table. You should be able to say, out loud, which of those you are looking at.

`python -m access init` and `python -m access reset` rebuild generated local state on this machine. They are how you get a clean `var/` when you have been experimenting. They are not a remote deploy. An account is not open, so there is nothing remote to reset.

## First-week reading list

The list is short on purpose. Read in this order across the week. Bring questions to me before you bring them to the phone bay.

Start with the 2026 logs page. Harper Singh wrote [Hospital, channel, and payer logs](../TECH-LOGS-2026.md) on 1 October 2026. The file is `TECH-LOGS-2026.md` in the technical folder, one level above this runbook. That is the page I want open while you learn `var/log.sqlite`. Harper's page names the three tables, the append-only rules, the rejection of a shared clock, the way `seq` works inside one table, the projections, and the local reader. It is the integration note for the logs we are running. Read it on Monday. Read it again on Wednesday with the file open, and point at a real row for each sentence you can.

The list still has the 2019 clock page as background. For background, read [Canonical instant for every feed](../TECH-CLOCK-2019.md). The file is `TECH-CLOCK-2019.md` in the same technical folder. The page is dated 2 April 2019. Wes Calder wrote it while he was platform lead. I am leaving that page on the first-week list as background, next to Harper's logs page, so you have the earlier write-up of time in the collaborative while you learn the desk. Read it on Thursday as background. I have not taken it off the list.

Also read my November note, [How a new hire reads the three logs](RUN-LOGS.md), the same afternoon you read Harper. The two sit together well: Harper's page is the integration description, and my note is the new-hire pass through the same file. On Friday, read Harper's phone note, [Phone rows change shape without a rewrite](RUN-MIGRATE.md), dated 2 June 2026. Phones were stored as digits. New rows use dashes. Old rows were not rewritten. Harper's sentence, which I want you to be able to repeat, is that both shapes will be in the log. The examples on that page are `6045552701` and `604-555-2701` for person `p-r2f-2701`. When you search a payload, quote the shape that is on the row.

Riley Chen's operator guide for the assistant is [Operator guide for northline-assistant-2024](../TECH-ASSISTANT.md), dated 20 November 2024, file `TECH-ASSISTANT.md`. The assistant is a reader. It fills a screen from hospital rows for one referral. It does not append to the three logs. IT needs to know that, because clerks will ask you to "fix the panel by editing the log," and the edit they want is an update or a delete. Both are rejected. The guide is the description of the product. Privacy questions about letter text go to Evan Cho. Clinical wording in a hospital letter stays on the hospital side. Do not copy letter text into a new file because a screen looks empty. Do not copy a wage note or a national-id file anywhere either. If you are unsure whether a JSON file is something you may duplicate onto a laptop share, ask Evan before you copy it.

Names and sites are listed for the document room. If you need a role, ask me and I will point you at the person. Priya Shah is the clinician at Fraser Burnaby. Anita Desai manages that clinic. Ruth Alvarez and Lena Brooks are at Harbor Coverage. Omar Farouk supervises nights at Cascade Seattle. Alex Kim is the on-call physician. You do not need to interview them in week one. You need to know they exist so a referral name in a payload has a place attached to it.

## How the days go

Monday is Harper's 2026 logs page and a supervised look at `var/log.sqlite`. You list the three table names. You read five rows from `log_hospital` ordered by `seq`. You stop. You do the same for `log_channel`, then for `log_payer`. You write the `occurred_at` strings as they appear. You do not paste the three results into one sheet sorted by time.

Tuesday is the local reader. You start `python -m access serve`, you fetch health, you fetch one extract by name, and you fetch one referral through `GET /ref/<ref>`. You say which file the hit came from. You shut the reader down with Ctrl+C when you are done. The process is foreground and local. It does not open an account.

Wednesday is projections. You look at `var/proj/hospital.sqlite`, `var/proj/channel.sqlite`, and `var/proj/payer.sqlite` as three builds. You pick one referral and find its hospital documents, then its channel documents, then its payer documents, without stacking the timestamps into a single day. If a payer row is a timeout, you read the null window as a null window. If a hospital nightly file has trailer fields, you read them. If it does not, you leave them absent.

Thursday is background reading. You read the 2019 clock page, Canonical instant for every feed, as background, and you keep Harper's 2026 logs page at hand because that is the page for the file. Friday is the phone note, plus a short pass through the assistant guide so you can tell a clerk that the panel is a reader. If a phone payload shows digits and another shows dashes, you report both shapes. Harper already said both shapes will be in the log. Old rows were not rewritten.

## What I will ask you on Friday

I will ask you where the file is. I will ask you the three table names. I will ask you what happens if you try to delete a row. I will ask you what a shared-clock command does. I will ask you what the local reader reads, and what it does not write. I will ask you which page you used for the logs, and I expect the 2026 logs page. The 2019 clock page is on your list as background, and I will ask whether you read it. I will ask you what a new phone row looks like next to an old one.

I will not ask you to produce one instant for a referral by sorting the three logs. I will not ask you to rewrite a digits phone into dashes. I will not ask you to deploy anything. An account is not open. Bring the pages, the file, and the questions. That is week one.
