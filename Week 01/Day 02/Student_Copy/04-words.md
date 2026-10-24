# 04 — Words

Read this page once. You will look back at it while you run the baselines and fill the memo. You do not need to memorize it.

These are the words this day uses. A definition here is the everyday meaning. When the rule lives in a file, the link is beside the word. Open that file when you need the sentence itself.

## The service

| Word | Meaning |
| --- | --- |
| Health cluster | A group of hospitals and primary care centers that plan and deliver care for one population. This client is the Al-Waha Health Cluster |
| Primary health care center (PHC) | The local clinic that refers a patient onward |
| Referral | A request from a PHC, or another clinic, for a hospital appointment |
| Return (bounce) | The hospital sends the referral back because it cannot accept it as written. Problem `p-bounce` is this symptom |
| Coordinator | The staff member who accepts, returns, or redirects referrals |
| Contact center | The cluster's phone and chat service. Problem `p-status` is a question that service is asked |
| Waitlist | The list of people waiting for an appointment. Problem `p-waitlist` is rows on that list that the coordinators do not trust |
| Session | A clinic's scheduled block of appointments. Problem `p-slots` is a session that goes out with empty chairs. Problem `p-forecast` is a plan for how full those sessions will be |
| Appointment | A booked time for a patient to be seen |
| Slot | One bookable appointment on a clinic's schedule. A sentence in a letter must not give a slot away |
| Did not attend (DNA) | The patient had a booking and did not come. Staff also call this a no-show. Problem `p-dna` is this symptom |
| No-show | The same event as DNA. The cost note uses this word for the money figure |

## Care

| Word | Meaning |
| --- | --- |
| Specialty | One hospital service line |
| Endocrinology | Hormones and diabetes |
| Ophthalmology | Eyes. A letter may say "eye clinic" |
| Diabetes | The sugar disease. A letter may say "diabetes" or "sugar clinic". Sugar clinic is not the same wording as diabetes |
| Cardiology | The heart service. A letter may say "cardiology" or "heart" |
| Heart | The everyday word for the cardiology clinic. The letter list treats "heart" as a specialty word |
| Retina | An eye service. The word retina is not on the letter list inside [letters.py](packet/baselines/letters.py) |
| Sugar clinic | A diabetes clinic named in everyday words. That phrase is not on the letter list |
| Triage | Sorting how urgent a problem is. Problem `p-triage` is the sponsor's wish that the assistant do this |
| Clinician | A doctor or other professional who decides on care. [Dr. Faisal Al-Otaibi](packet/kickoff/personas/med-dir.md) says clinicians own urgency |
| Clinical urgency | How serious a problem is, and how soon it needs a person. [pol-stage-gate.md](packet/kickoff/corpus/pol-stage-gate.md) says a clinician still assigns every clinical urgency. The assistant does not grade urgency |

## The people and their figures

| Word | Meaning |
| --- | --- |
| Sponsor | The leader who asked for the program. Today that is [Layla Al-Harbi](packet/kickoff/personas/cdo.md), Chief Digital and Transformation Officer |
| Virtual front desk | The sponsor's name for one assistant that books, reschedules, answers questions, and chases referrals. [sponsor-ask.md](packet/release/extracts/sponsor-ask.md) is the office's page |
| SAR | Saudi riyal. The currency on the cost notes and on [prices.csv](packet/release/finance/prices.csv) |
| Median wait | The middle value of waiting times on the board chart. Problem `p-clock` is that chart. The page is [dashboard.md](packet/release/extracts/dashboard.md) |
| `booking_date` | The column the chart uses as the start of the wait. The dashboard names it. That column name is a fact. The median printed beside it is a claim |
| Wait-time mart | The table the chart reads. It is the system of record for the board's wait number |
| Containment | The share of chats a bot handles without a person. [Daniel Okonkwo](packet/kickoff/personas/vendor.md) wants a number the board will repeat. [vendor-note.md](packet/release/extracts/vendor-note.md) gives a percent for a national pilot. That pilot is not the Al-Waha Health Cluster. The percent is a claim about the pilot |

## Data and decisions

| Word | Meaning |
| --- | --- |
| Protected health information (PHI) | Information that identifies a patient in the context of care. The letter file and the DNA file are this kind of material for today |
| In force | A document whose status, dates, and site make it the rule today. [pol-stage-gate.md](packet/kickoff/corpus/pol-stage-gate.md) and [pol-assistant-use.md](packet/kickoff/corpus/pol-assistant-use.md) are in force. A leader's wish does not override them |
| Watermark | A marker planted in a file so a copy can be recognized. [pol-assistant-use.md](packet/kickoff/corpus/pol-assistant-use.md) says the watermark stays out of prompts, tickets, and the work you submit. The letter file you open in [chapter 06](06-the-baselines.md) carries one. Read it where it sits |
| Claim | Their sentence, or a figure they published. You have not measured it |
| Request | What you will do next |
| Fact | A sentence you can point at in a file in this folder |
| System of record | The system that holds the fact. A number on a slide is not the system of record. The architect column in the memo is this name |
| `ext-large` | The public-cloud model. [zones.md](packet/kickoff/world/zones.md) calls that place `zone-public`. The price key on the price sheet is `price.ext_large_per_1k` |
| `local-small` | The smaller local price on the same sheet. The key is `price.local_per_1k`. You need these two keys only if you fill the optional cost lines |

## Baselines

A baseline is the simple score a heavier method has to beat. Each script today is one-feature: it uses a single column or a single word list.

| Word | Meaning |
| --- | --- |
| Row split | In [dna.py](packet/baselines/dna.py), keep every row whose position is a multiple of 5. The same person can sit on both sides. The printed line starts with `row`. The memo does not use it |
| Person split | Hold back the last 30 percent of the sorted person ids, and score only those people. A person is entirely in or entirely out. The printed line starts with `person`. The memo uses it |
| `prior_dna` | How many earlier missed visits are already on the row. The script guesses a miss when this value is at least 1 |
| `did_not_attend` | `1` if the patient missed that visit, `0` if they came. This is the label the DNA score is checked against |
| Keyword | The share of messages whose text contains the word status. The printed line starts with `keyword` |
| Filled | How many letters contain a specialty word from the list in [letters.py](packet/baselines/letters.py). The printed line starts with `filled` |
| Seasonal | The average error of 2026 against the same month in 2025. The printed line starts with `seasonal`. The memo uses it |
| Mean | The average error of 2026 against the average of the earlier years. The printed line starts with `mean`. Keep it in your notes. The memo does not use it |
| Measured | A number a baseline printed. In the brief, kind `measured` is that number |
| Claim size | A figure copied from a file, still marked as their figure. In the brief, kind `claim` is that figure |

## Family words

You will write these in the approach memo. Join two of them with `+` only when the problem needs both. [Chapter 07](07-the-memo.md) says which problem needs two, and which problems take one word alone.

| Word | Use it when |
| --- | --- |
| `classical-ml` | A score comes from columns in a table. The DNA file is this kind of question |
| `extract` | You pull one field out of a text and give it a name. The specialty in a letter is this kind of question |
| `retrieve` | The answer is a document that is in force for that reader. Hours, preparation, and required documents are this kind of question. A returned referral still has to name the rule that sent it back |
| `agent` | A model has to call a tool before it can state a fact that lives in a system. A status question is this kind of question |
| `forecast` | A monthly baseline is the number a heavier model has to beat. The demand file is this kind of question |
| `no-model` | The decision is a query, a rule, or a workflow. A date column is this kind of question. A slot that a sentence must not give away is this kind of question. Waitlist rows people do not trust are a matching rule, so they are this kind of question too |
| `blocked` | You do not build it. A person already owns the decision. Clinical urgency is this kind of question |

## Fine-tuning

Fine-tuning means changing a model's weights on the cluster's own examples. Retrieval leaves the weights alone and looks up a document that is in force. Use retrieval when the answer is a document that can change by site or by version. The knowledge question at the end of the day asks you to name that problem.

You have the words the later chapters use.

Next: [05 — The extracts](05-the-extracts.md).
