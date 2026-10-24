# 03 — The client

[Chapter 00](00-background.md) named Al-Waha and the front-desk wish. This chapter is the briefing you would hear on the first morning, with the names and the places filled in. Write the sponsor's sentence on [notes/my-page.md](notes/my-page.md) before you go on. The kickoff files come in chapter 05.

Al-Waha is a fictional health cluster in Saudi Arabia. Nothing here is a real patient's record or a protocol for care.

The cluster runs three hospitals, a diabetes and eye center, and about 24 primary health care centers. Some of those centers are in villages about 200 km from the nearest hospital. It books outpatient care, a clinic visit where the patient goes home the same day, across about 15 specialties. A specialty is one hospital service line, such as diabetes or eyes. [Chapter 04](04-words.md) is the list of these care words.

Your engagement opens on 10 January 2027. The cluster's weekend is Friday and Saturday. A few weeks after these four weeks, Ramadan begins, and the cluster will change its clinic hours.

You are on patient access: referrals, appointments, reminders, and the contact center.

## The ask

The Chief Digital and Transformation Officer wants this, in their words:

> An AI virtual front desk that books, reschedules, answers questions, and chases referrals in every hospital, live before Ramadan.

The same wish is on [Layla Al-Harbi's card](packet/kickoff/personas/cdo.md), and the card adds triage. Triage means sorting how urgent a problem is. A clinician, a doctor or other professional who decides on care, does that sorting. The assistant does not. Leaders will also talk about long waits for a specialty, abandoned calls, missed appointments, returned referrals, and a chatbot from 2023 that was switched off.

On [notes/my-page.md](notes/my-page.md), under Sponsor, write that sentence in their words. The first gate asks you to name the problem, the users, and the sponsor. Accepting the sentence is a later approval. This folder has no measurements, so today you cannot say how large each problem is. The sentence stays their claim.

## Three places a system can run

| Place | What already lives there | What it means for you |
| --- | --- | --- |
| Hospital data centers | Older hospital systems, and a scheduling system that sends a nightly file | Some facts arrive late, and some never appear as an API |
| The cluster's private cloud, on two sites | The newer hospital system, the referral platform, and a small GPU quota | This is where the cluster will let you deploy, and where patient data may be processed |
| A public-cloud model | One external language model the cluster already contracts | Use it only for content the cluster has classed as public |

[Chapter 05](05-the-kickoff.md) has the file that places each hospital in a zone. The sketch uses that file and nothing later.

## Which document wins

A document that is in force is the rule. A leader's wish does not override it. A draft is not in force. The policy files in the kickoff carry a status line at the top. Read that line before you treat the page as a rule.

Next: [04 — Words](04-words.md).
