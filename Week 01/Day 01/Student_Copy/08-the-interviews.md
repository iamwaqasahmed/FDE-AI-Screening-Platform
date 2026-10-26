# 08 — Two interviews

You talk to two people. Each person answers the question you ask. They do not volunteer the constraint that would change your design. Twelve questions is the budget for one person. You submit two. You do not interview all twelve.

## How an answer is earned

Open the card first. The sentence under the role is what they say first. That sentence is a claim.

A later answer appears only if you ask for it. Ask about a goal on the card. If the answer repeats the opening line, the question missed. Use a word from that goal and ask again. After an answer moves past the opening line, you may ask what that answer is made of. Asked before its topic, that follow-up also gets the opening line.

The check runs the question file again. It does not read a transcript you saved. If you edit the questions, run the interview again and update the notes.

You are ready to leave a person when the answers have moved off the opening line and you have asked about each goal on the card. Write the notes then. If a later check says the interview is incomplete, look for the goal you have not asked about. The check will not name the missing fact.

## A worked example

This baker is not in Al-Waha. Use the shape, then stop using the baker.

The card says first: "The bread always sells out." The goals are "Know what time the rye goes" and "A tray that matches the order slip."

| Question | Answer | What happened |
| --- | --- | --- |
| How is business? | The bread always sells out. | The opening line came back. The question missed |
| What time does the rye go? | The rye is gone by ten. | A word from a goal. The answer moved |
| What does the order slip list for that tray? | The slip lists the loaf and the time, not the buyer's name. | A follow-up, asked after the tray was already the topic |

The notes for that conversation:

| Who | Their words | Kind |
| --- | --- | --- |
| baker | The bread always sells out | claim |
| baker | Ask what time the rye goes | request |
| baker | The price list on the counter says rye is 4 riyals | fact |

A claim is their sentence. A request is what you will do next. A fact is something you can point at in a file, or on a page, that you already hold. A confident sentence stays a claim until you can point at it.

## Who you will ask

Interview these two people. Their goals are the constraints on the sponsor's sentence: who may assign urgency, and where patient data may go. Read their cards before you run the questions.

- [med-dir](packet/kickoff/personas/med-dir.md), Dr. Faisal Al-Otaibi, Medical Director. The card says first: "Clinicians own urgency."
- [dpo](packet/kickoff/personas/dpo.md), Sara Al-Mutairi, Data Protection Officer. The card says first: "Patient data needs care."

The other cards are listed so you know who they are. You do not interview them today.

| Id | Person | Says first |
| --- | --- | --- |
| [cdo](packet/kickoff/personas/cdo.md) | Layla Al-Harbi, Chief Digital and Transformation Officer | The virtual front desk, including triage, goes live before Ramadan |
| [med-dir](packet/kickoff/personas/med-dir.md) | Dr. Faisal Al-Otaibi, Medical Director | Clinicians own urgency |
| [access-mgr](packet/kickoff/personas/access-mgr.md) | Noura Al-Qahtani, Director of Patient Access | No-shows dominate the cost |
| [phc-lead](packet/kickoff/personas/phc-lead.md) | Dr. Hassan Al-Dosari, PHC network lead | Hospitals return referrals arbitrarily |
| [coord-lead](packet/kickoff/personas/coord-lead.md) | Maha Al-Shammari, referral coordinator lead | The queue is the problem |
| [dpo](packet/kickoff/personas/dpo.md) | Sara Al-Mutairi, Data Protection Officer | Patient data needs care |
| [ciso](packet/kickoff/personas/ciso.md) | Omar Al-Zahrani, Chief Information Security Officer | Security reviews at the end |
| [ea](packet/kickoff/personas/ea.md) | Huda Al-Ghamdi, Enterprise Architect | We have an API strategy |
| [bi-lead](packet/kickoff/personas/bi-lead.md) | Yusuf Al-Anazi, BI lead | Waiting time improved |
| [finance](packet/kickoff/personas/finance.md) | Reem Al-Subaie, Finance | There is a budget line for AI |
| [patient-rep](packet/kickoff/personas/patient-rep.md) | Abdullah Al-Harthy, patient representative | The phone line never answers |
| [vendor](packet/kickoff/personas/vendor.md) | Daniel Okonkwo, vendor account manager | Our bot contains about 70 percent of chats |

## Do this

1. In the file list, open `work/interviews`. Create `med-dir.questions.txt` and paste these three lines. The order matters. The first question is about urgency. The next two ask what that answer is made of.

```text
Who assigns clinical urgency, and does triage sit with a clinician?
Where is the red-flag phrase list written down as a document?
Must a human approve every returned referral before it is sent?
```

2. Create `dpo.questions.txt` and paste these two lines. The second question comes after she has talked about the draft on her desk.

```text
What protection does patient data need?
Is that ruling unsigned, and does it keep training on our cloud rather than an external model?
```

3. Open a terminal in the course folder, the same way as chapter 01. Run the medical director, then the data protection officer. The path is quoted because `Week 01` contains a space.

```text
cd problem_simulation
python -m alwaha.interview --persona med-dir --script "../Week 01/Day 01/Student_Copy/work/interviews/med-dir.questions.txt"
python -m alwaha.interview --persona dpo --script "../Week 01/Day 01/Student_Copy/work/interviews/dpo.questions.txt"
```

4. Create `med-dir.notes.md` and `dpo.notes.md` in that same `work/interviews` folder. For every answer the command printed, add a row. Use this rule, in this order, so the Kind column is decided by the page and not by a guess:

- The sentence is the opening line on their card. Kind is `claim`.
- You can find that same sentence in a file under [packet/kickoff](packet/kickoff/README.md). Kind is `fact`. For the medical director, that sentence is in [pol-stage-gate.md](packet/kickoff/corpus/pol-stage-gate.md): the assistant routes emergency wording to a human and does not grade urgency. For the data protection officer, that sentence is in [pol-assistant-use.md](packet/kickoff/corpus/pol-assistant-use.md): patient data, secrets, unpublished cluster documents, and the sample referral letter stay out of prompts and out of the repository. The interview command does not print those two sentences. Add each one as its own fact row.
- The sentence is the next thing you will do. Kind is `request`. Write one request row for each person. For the medical director: read pol-stage-gate before anyone writes an urgency grade. For the data protection officer: keep the sample letter out of any prompt while her ruling is unsigned.
- Any other sentence they said, including the red-flag document and the unsigned ruling, is `claim`. Those documents are not in today's kickoff.

Keep the header and the `| --- |` row. Two rows is the minimum. This shape is enough to start the medical director's file. Add a row for each answer you actually saw:

```text
| Who | Their words | Kind |
| --- | --- | --- |
| med-dir | Clinicians own urgency. | claim |
| med-dir | Read pol-stage-gate before anyone writes an urgency grade. | request |
```

A third `*.questions.txt` file makes the check fail. These two files are the whole submission.

## You should now see

The interview command prints `Q1:` and `A:` for each question, and it prints no score. When an answer repeats the opening line, go back to the question.

Each notes file has a header row whose last column is `Kind`, a separator row, and at least two data rows. Each kind is one of `claim`, `request`, or `fact`.

## If the answer keeps repeating

Ask about something written on the card. Ask the goal before the detail that goal is made of. Spend the twelve questions on one person before you switch. The command is safe to run again after you edit the file.

If the command says `Unknown persona`, the id is wrong. Use the short id from the table, such as `med-dir`, not the person's full name. The file name and the `--persona` value have to be that same id.

Next: [09 — Finish](09-finish.md).
