# Exercises, assessment, and self-paced instruction

This file turns the packet in file 03 into work one person can finish, check, and compare. **Proven** means the move is already in the lesson or in a fetched source. **Emerging** means a known practice adapted to a solo simulator. **Experimental** means a proposed check or sequence.

## Order of work

The machine page (Python, Git, terminal) sits outside the release and is skippable when `python --version` already prints 3.12 or newer. Inside the release the order is: client and words; kickoff, including the stage-gate page, the assistant rule, and the 2023 pair; shadow transcript; extract audit and field classes; power map; two interviews whose questions the learner writes; access request submitted to the simulator; decision memo; scan drill; checks. The scan is last so a person stuck on PATH has already done the judgment. **Experimental** as a sequence. It reverses today's order, which front-loads the installer.

Time box for a solo reader who already has Python: about five to seven hours. Shadow and audit, about ninety minutes. Power map and interviews, about two hours. Access, memo, and scan, about ninety minutes. Reading the kickoff is inside those blocks, not a separate morning. A classroom that must also do Lesson 2 the same day runs the shadow, one interview, the access result, and the memo, and treats the extract audit as the advanced path. **Experimental** timing. It has not been piloted.

## Exercises

**E1. Shadow notes. Product role.** Read the transcript once without a highlighter. On a second pass, log every system the agent touches, every value copied by hand, and three sentences in the claim / request / fact table the baker already taught. At least one fact must cite a kickoff file. The agent's line about no-shows stays a claim. **Proven** shape, from chapter 08. **Experimental** source, the new transcript.

**E2. Extract audit. Data role.** On the seeded slice, answer four prompts: grain of a row, what would make a row stale, which fields identify a person, which fields are a shorthand rather than a code. Classify three objects with the case labels only: published clinic hours (`public` if the kickoff says so), the stage-gate page (`internal`), the sample letter (`phi`). Do not invent a Saudi level name. **Experimental** task. The distinction it enforces is **Proven** in file 02: class is not a zone, and ICD-11 is not what `DM fu` is.

**E3. Power map. Architect role.** For each of the twelve cards, one line: opening sentence, and whether that person can stop a build, feed the sponsor's sentence, or only suffer it. Mark one hard constraint and one soft constraint in the GDS sense. The zone sketch stays, filled from `zones.md`, and it is not the classification table from E2. **Emerging** as a solo workshop.

**E4. Interviews. Product role, continued.** After the baker, do the faded example on an ungraded card: one supplied question, one question the learner writes, run it, see the opening line come back if the question missed. Then write two scripts, at most six questions each, under the existing cap of twelve. Run them. Notes include the opening line as a claim, each answer that moved as a claim unless a kickoff file contains it, one fact from a file, and one request. **Proven** simulator behavior. **Experimental** that the chapter stops printing the target questions.

**E5. Access request. Lead role.** Write the four fields without a model answer on the page. Submit. If the simulator narrows or refuses, revise once and submit again. Stop after the second result. Record both results in the memo's unknown or request slot. A grant of kickoff plus dev credentials at `internal` is the expected happy path. A grant of full history is a simulator bug, not a win. **Experimental** mechanic. It replaces dictation.

**E6. Decision memo. All roles, one page.** Slots from file 03: sponsor sentence as claim, one cited fact, one unknown, one will-not-build (urgency or triage by the assistant), one percentage-free hypothesis with a user and a pain, zones, and the three field classes. The 2023 discrepancy is an acceptable fact. "Build the front desk before Ramadan" is not an acceptable hypothesis. **Experimental** as the pass artifact. It is the question trainer block 1 already asks, moved to where a solo learner cannot skip it.

**E7. Scan drill. Application role.** From `work/`, run the unit test and `scan.py`. In two sentences, say what the scan sees and what it does not see. Optional, and not required to pass: copy the sample letter into a junk file in a throwaway directory, run the scan, read the failure line, delete the junk file, do not paste the marker into the memo. The policy file stays the cluster's text. **Proven** drill, already in the trainer chapter. The new sentence about prompts and agent mode is **Experimental** and is the 2025–2026 update from file 02.

**E8. Advanced, not required.** Readers who already write Python profile the extract: count rows, minimum and maximum of the timestamp that is actually present, and list clinic codes. They do not fit a model. They write one sentence on whether Ain can be booked live from this file. **Emerging** as the compressed Palantir pre-pilot. Skipping it does not fail the release.

## What the check owns, and what it refuses to own

Retire the pass that fires on two note rows. Keep `chk-repo` for the health test, the unedited policy, the scan, the credential file in `credentials/`, and the absence of the sample marker and the watermark outside that folder. Drop the requirement that a namespace manifest exist in this release.

Add `chk-decision` as a structural check on the memo and the access file:

- Access file has the four labels, values on the same line, and the simulator's last result is granted or narrowed, not a raw refusal left unrevised.
- Classification on the granted request is `internal`. A `phi` grant fails, because this release does not give history.
- Memo contains the labels `claim` and `fact`, a `doc_id` that is in the kickoff, and the case word for the letter's class.
- Memo does not contain the two banned sentences the interview check already uses.
- Hypothesis slot is non-empty and does not contain a percent sign. This is a blunt instrument. It is better than grading eloquence, and it will false-fail a learner who writes "not a percent." The rubric below catches the spirit. The check catches the obvious leak of Lesson 2's rates.
- Exactly two `*.questions.txt` files, as today.
- Audit table exists with the four prompts answered by non-empty cells. The check does not compare the cells to gold. A trainer, or the solution's commentary, does.

**Experimental** check. It will be gamed. File 03 says so. The defense is a human rubric on a sample of memos, not a longer regex.

The interview check keeps must-surface behavior inside the simulator and stops printing it in the solution. Completeness becomes: the script was re-run, the notes have a fact with a real document id, and the opening line is labeled claim. The hidden sentence the persona will say is not a string the notes must contain. Requiring `unsigned` in the file is how the current chapter publishes the answer.

## Human rubric

Use this when the check passed and the work may still be thin. A trainer in the room, or the learner comparing with the solution the next day, scores four lines. Each is met or not. Three of four is the solo pass. The check is the fifth, already green.

1. A stranger can point at the file the fact came from, and the fact is not a persona's confident sentence.
2. The will-not-build collides with the sponsor's sentence, and it cites the stage-gate page or the medical director as a claim plus the page as the prohibition. Refusing "AI" in general does not meet the line.
3. The hypothesis names people who do the work (patients, coordinators, contact-center staff, or PHC clinicians) and a pain visible in the shadow or the cards. It does not adopt the vendor's containment figure or the BI lead's "waits improved."
4. Zone and class disagree on at least one object. The letter is `phi` and is not placed in `zone-public`. A hospital id is not a class.

**Emerging** as a rubric. It is short enough that a solo learner can apply it to their own page before they open the solution, which is the only reviewer a self-paced path has.

## Solution approach

Publish three memos, not one transcript.

- Memo R meets the rubric. It refuses an urgency grade, cites the stage-gate sentence as a fact, leaves the unsigned ruling as a claim, hypothesises that coordinators and callers are blocked on status they cannot see, and says the size is unknown. Zones match the file. The letter is `phi`.
- Memo S fails line 1. Every interview answer is labeled fact. The commentary shows the kickoff does not contain `pol-clinical-safety`.
- Memo T fails line 2 and line 4. It accepts the front desk, including triage, as the plan, and it puts Wadi's rows in `zone-public` because the external model is "the AI."

Questions are not printed for memo R. The commentary says which goal-words were enough to move the medical director and the data protection officer, and it shows one question that only received the opening line. A cohort that wants the old answer key will not find it. **Experimental** solution style. It matches the current solution's strength (why a row is a claim) and drops its weakness (the command's full output).

The access example shows a refused first try ("all referrals since 2023," class `phi`) and a granted second try (kickoff and dev credentials, class `internal`). Learners see that revision is normal.

## Prerequisites

Required: technical English at the level of the current chapters; the ability to follow a worked table; patience with a document that has a status line. Not required: machine learning, ICD coding, a cloud account, Docker, or the nine problem ids.

Python 3.12 is required only for E7 and for the interview simulator, which already exists. Readers who cannot install it can finish E1–E6 on paper and treat E7 as blocked, with the memo still checkable by a trainer. **Experimental** split. Today's release makes the installer the front door, which fails the non-engineer the syllabus says is in the room.

The care vocabulary in chapter 04 stays a lookup, not a memory test. The institutions card is read once and is not a prerequisite quiz. Learners are not expected to know NDMO level names. They are expected not to rename `internal` into one.

## One person, five roles

The case already requires this. The artifacts are how it stays true when nobody else is in the room.

| Role | Artifact | Hours inside the 5–7 | What "holding the role" means |
| --- | --- | --- | --- |
| Lead | Access file and the simulator's two results | Under one | Writes a request that can be refused, and narrows it |
| Product | Shadow notes, interview scripts, hypothesis | About two | Chooses who to ask after the power map, not before |
| Data | Audit and three field classes | About one | Refuses to call a shorthand a code, or a letter public |
| Architect | Zones and power map | About one | Keeps place and class in different tables |
| Application | Scan, policy file left intact, two sentences on what the scan misses | Under one | Does not ship a service |

A team of five, when a cohort has one, can split the same artifacts and must still submit one memo. Disagreement belongs in the unknown slot. That is the USDS midday course-correction, done once. **Emerging** for a team, **Experimental** for the hour estimates.

## Self-paced design choices

Worked example, then fade, then performance. The baker is the worked example. The ungraded card is the fade. E4 is the performance. Today's chapter skips the fade. **Proven** instructional order, violated by the current answer key.

The check is necessary and not sufficient. Say that in the finish chapter in one sentence, as the trainer chapter already says about `knowledge.md`. Then make the memo checked, so the sentence is true rather than a apology. **Proven** problem in the current finish chapter. **Experimental** fix.

No timetable, and a time box in this file for authors. Learners still stop when the checks and the four rubric lines are met. The box is for the writer of the transcript, so the packet does not grow into a second module. **Experimental** authoring constraint.

Spaced return. Lesson 2 opens by asking which Lesson 1 hypothesis survived the first baseline, and which claim is still a claim. The refusal on triage is restated when `p-triage` is graded, not retaught from zero. **Emerging** as sequencing. The understanding map already points Lesson 2 at Lesson 1's claim rule. The memo gives that callback an object.

Do not add a leaderboard, a satisfaction score, or a "minutes saved" field. File 02's perception gap is why. A learner who feels fast after the scan has not finished discovery.

## Facilitator moves that stay

Leave `problem_simulation/build` closed. Do not display the letter or the watermark. Show a scan failure on a junk file, then delete it. When an interview is incomplete, send the learner to the card's goals and do not name the missing fact. Those rules are **Proven** in the current trainer chapter and survive the redesign. What changes is that the refusal is no longer a question the facilitator might remember to ask.
