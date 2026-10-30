# Instructional design for a self-paced advanced course

Proposal only. Nothing in this folder edits the lessons, the checks, or the author record. The course it is written against is the Al-Waha narrative: twenty lessons, traps that stay on the lesson that owns them, student chapters, checks, and a solution copy opened after that lesson's finish chapter says the checks have passed.

Readers are mixed government professionals. Some are engineers. Some are not. One person working alone currently holds five parts on every lesson: lead, AI or data, application, product, and architect. The syllabus asks for working English and some familiarity with programming, databases, APIs, cloud, or machine learning. It does not require all of those. From Module 1, Lesson 3 onward, many chapters are finished Python files to paste. `knowledge.md` is part of done on most lessons, and the checks often do not grade its sentences.

This dossier answers one design problem. More technical depth destroys self-pacing when every lesson is a full distributed system. The proposed architecture is a core path, extension labs, and a capstone, with mastery gates. It prescribes prerequisites and exit criteria. It does not prescribe hours, days, or weeks.

| File | What it decides |
| --- | --- |
| [01-learning-science.md](01-learning-science.md) | Which research findings apply to this course, and where they stop applying |
| [02-assessment-model.md](02-assessment-model.md) | Mastery gates, feedback with no live instructor, and what a check is allowed to mean |
| [03-proposed-progression.md](03-proposed-progression.md) | Core path, extension labs, capstone, prerequisites, exit criteria, lesson shape |
| [04-sources.md](04-sources.md) | Sources opened for this note, with the claim each one is allowed to support |
| [05-core-versus-extension.md](05-core-versus-extension.md) | How the retrieval lesson splits into a core gate and a fusion lab |

## The model in short

Progress is a specification that is met or not yet. The next core lesson opens when the current core specification is met. An extension lab never sits on that path.

The core path keeps the twenty decisions and their traps. Each core lesson teaches one decision: what arrives, which part decides, what it refuses, and what it writes. The required product is that decision, traced to a case id. Code on the core path is at most one completion inside one file, and only when the decision is a behavior a trace cannot show. Lesson 1's existing starter stays there too: the health check and the secret scan are the orientation behavior, and they predate the paste chapters.

Extension labs hold the file replacements that now fill Module 3 and Module 4: the adapter, the index, the deploy manifests, the surge, the failover. Each lab has one mechanism and one check. It opens after the core specification for that decision. Skipping it leaves the next core lesson open. It closes any sentence in the capstone that would claim the lab was run.

The capstone is the proposal at Module 4, Lesson 5. Its prerequisite is the four module core gates. Its exit criteria are the decision specifications below, including a recorded steering answer scored with a rubric. Extension labs are a distinction bundle, not the key to the front door.

## What to stop

- Stop putting a whole subsystem on the only path through a lesson. Nine to eleven replaced modules in one lesson is a completion hazard, not a higher standard.
- Stop counting a pasted gold file as evidence that the learner can defend the decision. The check re-runs the file. That shows the file behaves.
- Stop using an unspoken question as the study of a worked example. The four beats have to be written.
- Stop withholding a procedural example until the check is already green. For a procedure, the example or a completion comes first. A short written prediction comes first only for a conceptual trap the lesson already knows how to answer.
- Stop giving engineers and non-engineers the same required production. They share the case and the decision record. They do not share the implementation quota.
- Stop scoring a design, a DPIA, or a readout as a percentage of a gold fact list. Use a short list of decisions, each met or not yet, plus exemplars.
- Stop letting a calendar pair of releases act as the unit of progress. The understanding map's ten classroom days are a cohort timetable. Self-paced progress is the specification.
- Stop leaving `knowledge.md` outside the gate when it is the only place the judgment lives.

Traps stay. Hint rungs stay, and the third rung still points at a file or a policy, not at a gold value. Solution chapters stay closed until the prediction is committed and the check has run. Foundation specifications still block a distinction. This note sets no numeric cut and no duration.
