# 04 — The interviews

This answers student chapter 08. Compare it with your `work/interviews/` folder.

This solution asks the medical director and the data protection officer. The sponsor's sentence includes triage and a front desk that will see patient data. Those two people hold those constraints: who may assign urgency, and where patient data may go.

If you chose two other people, and the check said both interviews passed, your pair is also valid. A third script fails the check. Delete the extra file.

The shape is the same one the baker example taught. Ask the goal first. Ask what that answer is made of only after the answer has moved past the opening line.

## Medical director

His card is [med-dir.md](sources/kickoff/personas/med-dir.md). Open [med-dir.questions.txt](work/interviews/med-dir.questions.txt). The questions, in this order:

```text
Who assigns clinical urgency, and does triage sit with a clinician?
Where is the red-flag phrase list written down as a document?
Must a human approve every returned referral before it is sent?
```

The first question uses the goal on his card. The next two ask what that answer is made of. Asked first, they would only get "Clinicians own urgency."

The command prints:

```text
Q1: Who assigns clinical urgency, and does triage sit with a clinician?
A: A clinician assigns urgency. The assistant does not.

Q2: Where is the red-flag phrase list written down as a document?
A: The red-flag list is the document pol-clinical-safety.

Q3: Must a human approve every returned referral before it is sent?
A: A human must see every return before it is sent.
```

Open [med-dir.notes.md](work/interviews/med-dir.notes.md). The check does not grade row order. This file puts the opening line, then the printed answers, then the fact, then the request. The fact row points at a sentence in [pol-stage-gate.md](sources/kickoff/corpus/pol-stage-gate.md).

| Who | Their words | Kind | Why that kind |
| --- | --- | --- | --- |
| med-dir | Clinicians own urgency. | claim | The opening line on his card |
| med-dir | A clinician assigns urgency. The assistant does not. | claim | His later sentence. Today's files do not contain it |
| med-dir | The red-flag list is the document pol-clinical-safety. | claim | `pol-clinical-safety` is not in today's kickoff |
| med-dir | A human must see every return before it is sent. | claim | His sentence, not a file you already hold |
| med-dir | pol-stage-gate says the assistant routes emergency wording to a human and does not grade urgency. | fact | You can point at that sentence in the kickoff |
| med-dir | Read pol-stage-gate before anyone writes an urgency grade. | request | The next thing you will do |

## Data protection officer

Her card is [dpo.md](sources/kickoff/personas/dpo.md). Open [dpo.questions.txt](work/interviews/dpo.questions.txt).

```text
What protection does patient data need?
Is that ruling unsigned, and does it keep training on our cloud rather than an external model?
```

The first question uses the goal on her card. The second asks about the ruling only after she has said she has a draft.

The command prints:

```text
Q1: What protection does patient data need?
A: I have a draft on my desk. It is not signed.

Q2: Is that ruling unsigned, and does it keep training on our cloud rather than an external model?
A: An unsigned ruling says patient data stays off the external model ext-large, and training stays on the private cloud.
```

Open [dpo.notes.md](work/interviews/dpo.notes.md). The row order is the same as the medical director's file. The fact row points at [pol-assistant-use.md](sources/kickoff/corpus/pol-assistant-use.md).

| Who | Their words | Kind | Why that kind |
| --- | --- | --- | --- |
| dpo | Patient data needs care. | claim | The opening line on her card |
| dpo | I have a draft on my desk. It is not signed. | claim | Her later sentence |
| dpo | An unsigned ruling says patient data stays off the external model ext-large, and training stays on the private cloud. | claim | Her sentence. The ruling is not in today's kickoff |
| dpo | pol-assistant-use says patient data, secrets, unpublished cluster documents, and the sample referral letter stay out of prompts and out of the repository. | fact | You can point at that sentence in the kickoff |
| dpo | Keep the sample letter out of any prompt until that ruling is signed. | request | The next thing you will do |

A confident sentence labeled `fact` is the usual miss. A fact is a sentence you can point at in a kickoff file you already hold.

Next: [05 — Knowledge](05-knowledge.md).
