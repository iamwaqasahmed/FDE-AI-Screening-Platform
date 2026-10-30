# Access Office

This folder is the specification for a self-paced Forward Deployed Engineering course. A team that has only these files can build the simulator, the checks, and the lessons. Earlier research folders are source material. They are not part of this design.

The student inherits a running assistant that already answers patients. Three organizations each keep a true log. The assistant collapses those logs into one wait number and one urgency field. The course is nine investigations. Each one asks the student to bind a screen, a tool, or a cloud call to the authority that owns it.

## Read in this order

| | Document | Question it answers |
| --- | --- | --- |
| 1 | [Course vision](01_Course_Vision.md) | Who the course is for, and what a graduate can do |
| 2 | [Enterprise problem](02_Enterprise_Problem.md) | The three parties and the collapse |
| 3 | [Simulation architecture](03_Enterprise_Simulation_Architecture.md) | The three processes and the sealed gold |
| 4 | [Data and systems](04_Synthetic_Data_and_Systems.md) | Logs, projections, and what the student sees |
| 5 | [Engineering challenges](05_Engineering_Challenges.md) | The nine failures, as engineering problems |
| 6 | [Solution architecture](06_Complete_Solution_Architecture.md) | The shape of a student system that passes |
| 7 | [Local implementation](07_Local_Implementation.md) | What runs on a laptop |
| 8 | [AWS implementation](08_AWS_Implementation.md) | What an account is allowed to hold |
| 9 | [Local to AWS](09_Local_to_AWS_Progression.md) | Where the laptop design must change |
| 10 | [Curriculum overview](10_Curriculum_Overview.md) | The nine investigations and the rules of progress |
| 11 | [Modules and lessons](11_Modules_and_Lessons.md) | Each investigation as a buildable lesson |
| 12 | [Breakthroughs](12_Lesson_Breakthroughs.md) | The non-obvious point of each lesson |
| 13 | [Self-paced design](13_Self_Paced_Learning_Design.md) | Prediction, naming, checks, resubmission |
| 14 | [Competency framework](14_FDE_Competency_Framework.md) | How mastery is shown |
| 15 | [Implementation roadmap](15_Implementation_Roadmap.md) | Build order for a new team |
| 16 | [Architecture decisions](16_Architecture_Decisions.md) | What was chosen, and what was refused |
| 17 | [Final validation](17_Final_Validation.md) | Coverage, limits, and what is still unproven |

## Names used everywhere

| Name | Meaning |
| --- | --- |
| Cluster | Al-Waha, the hospitals. Fictional |
| Desk | The National Desk, the patient channel. Fictional. Not a real national app |
| Payer | The Coverage Partner. Fictional |
| `log_hospital`, `log_channel`, `log_payer` | Three append-only logs. No shared clock |
| `dec-clinical` | A clinician’s urgency. The assistant does not write it |
| `dec-route` | Desk routing, including emergency wording to a person |
| `dec-accept` | The Desk took the request. Patient wait starts at this event |
| `dec-cover` | The payer’s eligibility decision |
| `dec-slot` | A slot fact from the hospital file, not from a sentence |
| Binding | The student’s JSON of field paths and role tags |
| Holdout | A sealed log the chapter does not contain |
| Case date | The engagement opens 10 January 2027. History in the logs starts earlier |

Laws in the case are fictional analogues. A map in the orientation page points at real documents. The case does not claim to satisfy them.

## What is in this folder

These eighteen files are the whole specification. There are no drafts beside them. Document 5 is the one-page challenge table. Document 11 is the lesson-by-lesson build. Document 12 is the insight, written for authors, and it must not be pasted above a student exercise.
