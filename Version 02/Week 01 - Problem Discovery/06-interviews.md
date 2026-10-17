# Interviews

**Days 3 and 4.** The persona cards in `data/engagement/personas/` say what each person says first. The important facts come out only when you ask a follow-up, after the topic that unlocks it. A question about a detail, before the topic, gets the opening line again.

You have twelve questions per person. The score is the share of the important facts you reached.

## Run them

From `problem_simulation`:

```text
python -m simulation.stakeholders.interview --persona cdo
python -m simulation.stakeholders.interview --persona lead_grader --script questions.txt
```

`--script` is a text file, one question per line. Persona keys:

`cdo`, `ophthalmology_lead`, `programme_manager`, `lead_grader`, `dpo`, `records_manager`, `finance_head`, `enterprise_architect`, `security_officer`, `outreach_coordinator`, `patient_rep`, `vendor_manager`.

Save each script as `interviews/<persona>.txt` in your work folder. The checker runs the same simulator and expects a score of at least 0.80 for every persona. Plan the twelve questions. Spend the early ones on topics. Spend the later ones on the follow-up.

The corpus already holds transcripts of strong and weak interviews. You may read them. Quoting a transcript is not a substitute for a script that can reach the facts on a fresh seed: the scripts are scored against the persona, not against the practice transcript.

## Write the note

For each persona, write `notes/<persona>.md` from [the template](templates/persona-note.md). Record what they did not say first: the dates, the counts, the names, and the claims you will not repeat. A note that only restates the opening line fails. A note that copies a sentence they would not stand behind also fails.

Two disagreements are worth a page of their own. The ophthalmology lead and the programme manager give different backlog numbers. The programme manager's story of the 2023 letter delays is not the lead grader's. Do not average them. Hold both, and go to the files.

**Finish.** Twelve scripts score 0.80 or better, and twelve notes exist.

Next: [Walk one person](07-walk-one-person.md).
