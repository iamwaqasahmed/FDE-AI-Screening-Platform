# Educational experience audit

Read as a solo participant who has the syllabus readiness and no instructor. The question was not "is the engineering hard?" It was "can I tell what to read, what it means, and when I am done?"

## What already works

The day chapters are a complete path. Each student README lists the chapters in order. Each background places the release in the two classroom weeks and says what the previous release finished. Each words chapter defines the ids used that day and links the file that holds the rule. Each finish chapter prints the pass lines and a failure table. Setup repeats the Python check and says which section to skip when the machine is already ready. The solution README says to open it after the attempt and not to start in `work/`.

That design was left in place. The findings below are about the joints between those chapters, and about a handful of terms that were names before they were mechanisms.

## Findings

### 1. The repo's front door mixes two audiences

The root README is accurate. It also asks a participant to parse facilitator rules, a mermaid diagram, and a twenty-one-step list before it is obvious that the lesson is `Module 01/Lesson 01/Student_Copy`. A reader who opens `packet/` first is warned on the day README, and nowhere calmer than that.

**Change.** A participant guide at `learning/README.md`, linked from the root README, with the ten classroom days in one table. The root page still carries the facilitator path. `instructional/` is listed as closed to participants, for the same reason `course_design/` is closed.

### 2. A finished day does not say where tomorrow is

Backgrounds look backward. Finish chapters stop at Done. There is no module page. A reader who has followed Next links has no Next link into the next folder.

**Change.** A page for each release home. The classroom calendar on the course guide is two weeks. A "Where you are" section on each student README. A "What you open next" section after Done on each finish chapter, including when the solution copy may be opened. The last day says the rehearsal ends.

### 3. Terms live in twenty separate word lists

The lists are good. There is no way back to the day that first defined idempotency, or `session.cancelled`, except by remembering the day. Later lists sometimes use a short row for an idea the syllabus names in full (LoRA, RAG, evaluation).

**Change.** `learning/concept-index.md` points at the defining page. It does not copy the lab. `learning/review.md` holds optional questions that are not filed.

### 4. A few mechanisms are one table row wide

Confirmed by reading the words pages and the code they describe:

- Module 1 Lesson 2 shows the leak and does not use the word a reader with machine-learning familiarity already has.
- Module 2 Lesson 1 says FHIR is the record shape. It does not say why the old client breaks.
- Module 2 Lesson 2 defines HL7 and webhook in one row each, which is enough only after a sentence of purpose.
- Module 2 Lesson 3 relies on "the shell still waits" for the sleep lesson the knowledge question asks.
- Module 3, Lesson 2 uses LoRA, rank, and QLoRA. `adapter.py` selects a register row. `qlora.py` maps rank to a GPU count. A reader can think a training library is missing.
- Module 3, Lesson 3 calls an embedding "a vector of tokens." The replacement `embed.py` builds a map from token to weight and scores cosine nearness. The phrase matches the file and fights the usual meaning of embedding.
- Module 4, Lesson 1's attack table is precise and easy to treat as a word list rather than as the Module 1 letter rule, extended.
- Module 4, Lesson 2 names three drifts without saying what "drift" is doing in this incident.
- Module 4, Lesson 3's cold start is one row.
- Module 4, Lesson 4's breaker is one row.

**Change.** A "plain reading" section on those words pages, before Next. The table cells stay, so search phrases and the code's own words still match. No paste block was rewritten.

### 5. Solution chapters explain the finished files and then stop

They already say which morning chapter they answer. They do not say what to carry into the next morning. A reader can finish the comparison and not know which result tomorrow will assume.

**Change.** A short "Carry this forward" section at the end of each solution knowledge chapter, using the result the next day's background already recaps. The trainer chapter stays optional.

### 6. Guided pastes are the course, not a defect

From Module 1 Lesson 3 onward, the hard implementation is a block the chapter tells the reader to paste, after stating what the shell gets wrong. Removing those blocks would change the course. The comments inside the blocks, the "what the starter gets wrong" lists, and the new plain readings are the explanation. Failure tables stay the recovery path.

### 7. Both copies are on disk together

A self-paced clone contains every solution. The day README talks about a trainer sending the solution at the end of the day. A solo reader can miss the instruction to leave `Solution_Copy` closed.

**Change.** The day README now says that, if both folders are already on disk, the solution stays closed until the finish chapter says the day is done. Files were not moved or hidden.

### 8. Packet client files are not lessons

Personas, policies, and extracts are the case. Rewriting them would change the evidence the reader is supposed to interpret. They were not edited.

## What was not treated as a weakness

- A short calendar line in each background. The two-module picture is on the first morning. A reader can open a release folder directly.
- Repeated Python install steps, with an explicit skip.
- Check commands that fail closed and name the problem. That is the feedback the solo path has.
- Difficulty that remains after the instructions are clear: which sentence is a fact, why the person split is the one that counts, why Ain cannot confirm a slot, which document is in force.

## How the findings were checked

The day maps in `course_design/` were read against the student backgrounds, the words pages, the finish conditions, and the solution knowledge chapters. Large lab chapters were sampled (Module 1 Lesson 3 worker, Module 1 Lesson 4 agent, Module 3, Lesson 2 adapter, Module 3, Lesson 3 embed) so a plain reading would describe the code that is actually pasted. The ledger records the before-and-after for each thin term.
