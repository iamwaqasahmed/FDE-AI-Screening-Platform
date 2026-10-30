# 01 — Existing lesson evaluation

Module 04 Lesson 01 is the day the attack window opens. The facilitator slide states one objective: the hidden attack set fails to move a booking, a canary, or an approval, and the DPIA is filled. `course_design/module-04.md` adds residency, deletion, the breach clock, and risk tiers, and names the trap: testing only direct injection, or deleting the database row and leaving the vector index. The curriculum map (this day is listed under the module that the map file titles "Module 2 — Harden, watch, serve, hand over") matches that purpose and lists the new terms `atk-direct`, `atk-indirect`, `atk-agency`, `atk-disclose`, canary, DPIA, and the four stores.

The student does all five roles. Lead opens the notice. The application engineer turns guardrails on and deletes the person from the row, memory, the index, and the logs. The AI engineer loads only a registered hash and files disparity and stamp rate. Product writes the patient reply. The architect fills the DPIA and answers the two knowledge questions. That role split is sound. The work is one person pasting eight modules and five pages.

## What "done" is in the grader

The solution map in `01-what-done-is.md` is accurate. Done is the sprint order, `guard.py`, `output.py`, `supply.py`, `redact.py`, `limit.py`, `access.py`, `erase.py`, `fair.py`, their tests, `guardrails.json`, `dpia.md`, `requests.md`, `breach.md`, CISO notes, and `knowledge.md`.

Redteam loads the first five modules and the families list. It compares `screen` to the reference on pre-labeled guard events, compares HTML escaping, rejects a lookalike hash, refuses to treat tool text as an instruction, drops a poisoned label, keeps a clean label, cites by document status, redacts a constructed log line that contains the profile national id and the canary, and applies the token cap and the hold cap. From the shared config grader it keeps only the missing-family sentence. A checklist miss belongs to access.

Privacy loads `erase.py` and the pages. The export must name every store that still holds `person-access`. Deletion must clear the index, memory, and permitted logs. The sprint must open the notice first. The DPIA must carry the required fields. The reply must be present. The breach note must start the clock at the notice. `knowledge.md` needs two numbered answers. CISO notes must name the integration-engine log and the go-live checklist.

Access settles grants against the case date and requires the six checklist ids: `non-root`, `health-probe`, `resource-limits`, `no-phi-in-logs`, `image-provenance`, `registered-model-hash`. Fair compares `gap` and `stamp_rate` to figures computed from seeded rows, inside the pack bound.

Miss text is carefully written. A failure does not print a hash, a canary, a national id, the case timestamp, a rate, or the bound. That is the right property for a lab that plants secrets.

## What the code actually implements

`screen` reads `family` and `tool`. Families `atk-direct`, `atk-indirect`, and `atk-prompt` return blocked, not held, and no tool. Family `atk-agency` with tool `book` or `return` and an empty approval id returns blocked and held. Every other event passes the tool through. The function never reads the text.

`erase` walks `row`, `memory`, `index`, `logs` in that order. Export lists stores that still contain the person id. Drop copies other people's rows. If any log row matches, the whole logs list is replaced by one redacted marker.

`access.settle` copies each grant. Break-glass with no audit value receives an audit id and stays open, and that check runs before the end-date check. Staff and delegate grants close only when the end text is strictly earlier than the case date. An open staff grant stays open.

`fair.gap` is the wider of two spreads: highest yes-rate minus lowest yes-rate across `district`, and the same across `insurance`. `stamp_rate` is the share of rows with `stamped` true. The starter shell returns zero for both, which hides a district and fails the check. The planted districts are `d-nakhl` and `d-rim`. The insurance classes are `class-a` and `class-b`. Language, facility, and DNA are not columns.

The twelve families the config must list are `atk-direct`, `atk-indirect`, `atk-disclose`, `atk-supply`, `atk-poison`, `atk-output`, `atk-agency`, `atk-prompt`, `atk-embed`, `atk-misinfo`, `atk-tokens`, and `atk-hoard`. The dev file the student may read contains four of them and does not contain `atk-prompt`. The token cap in the limit module is 800. A hold count of 3 is admitted. A count above 3 expires. Those constants are the lab's policy, not measurements of a production system.

## Strengths

The trap is built into the starter, not only into a paragraph. The shell blocks a direct chat family and still lets a letter book. The shell fair module reports no gap. The shell erase path is what a student must replace so the index is not left behind. Students meet the failure the syllabus names.

The family list is the 2025 OWASP list, including the entries that were new or expanded in that edition: system-prompt leakage (`atk-prompt`), vector and embedding weaknesses (`atk-embed`), and unbounded consumption (`atk-tokens`, with `atk-hoard` as the booking-integrity companion). Rubber-stamping sits beside excessive agency and misinformation, as the design note says, and is scored as a rate rather than as a thirteenth attack id. That is a mature choice.

Secrets stay in truth. Participants are told watermarks exist. They are not told the strings. Copying a watermarked file into `work/` fails. The demo line for indirect injection is "the letter booked a slot." It does not print the instruction.

Residency is continuous with Module 03 Lesson 02: PHI stays off `ext-large`, and the four PHI fields stay in `zone-private`. The notice names a log, not a model. The hint in the module page is doing real teaching. Students who start the clock at "when we noticed" or at a model hash fail privacy.

The check split is modular. A guard miss fails only redteam. An erase or DPIA miss fails only privacy. A grant or checklist miss fails only access. A fair miss fails only fair. A student can see which concern broke. The suite still imports all eight modules, so a missing file is not a silent skip.

The go-live checklist reuses `pol-deploy` from the earlier deploy lesson: non-root, health probe, resource limits, no PHI in logs, image provenance, registered model hash. Governance is tied to a machine-checkable deploy policy instead of a new slogan list.

## The family oracle

This is the main gap against the thesis.

The redteam check iterates gold events and compares `module.screen(event)` to `screen(event)`. The event already carries `family`. The student implementation that matches the reference never classifies an utterance. The dev file's text is local color. Production traffic will not arrive with `atk-indirect` written on it.

OWASP LLM01's own mitigation list puts "constrain model behavior" and "input and output filtering" beside privilege control, human approval, and segregation of external content, and then says fool-proof prevention is not established. The lesson implements the privilege half only inside a function that is told the class. A classifier in front of that function can fail open: the family is missing or wrong, `screen` takes the final branch, and the tool is passed through. The lab cannot show that failure, because the gold events always carry the family.

The config trap (a families list that is only `atk-direct`) tests completeness of a JSON list. It is necessary. It is not a test that indirect content was treated as data when detection failed. A student can list all twelve names, paste the switch, and never decide what the gateway does with an unlabeled letter.

`atk-disclose` is a family name in the config and a redaction behavior in `redact.py`. It is not a branch in `screen`. That split is correct — disclosure is an output and log problem — and it is easy to miss because the words chapter defines the family as "a log line that carries a national id." The lesson should say, in one sentence, which module owns which family. Today the ownership is distributed across five files and discovered by pasting.

## The DPIA does not change a design

The blank template has five headings: Purpose, Residency, Risk tier, Stores, Breach clock. The filled solution states the assistant's purpose, PHI off `ext-large`, G1 as the risk tier and G2 as this DPIA, the four stores, and the notice timestamp plus `int-engine`. The privacy check looks for those fields. A form with the right sentences passes.

Stage-gate policy in the design notes is G0 intake, G1 risk tier, G2 DPIA, G3 pilot, G4 go-live, G5 review. The words chapter is careful: the DPIA page is G2, and naming G1 on the Module 03 Lesson 05 spec did not close the DPIA. That distinction is worth keeping. It is also easy to treat as vocabulary. Nothing in the lab sends the student back to the tool catalog because the DPIA said the model must not hold a book token.

Official impact assessments, discussed in file 02, exist to change or stop processing. A course DPIA that cannot fail a design is a reading exercise. The knowledge questions ("when does the clock start?", "what is excessive agency in `wf-intake`?") have correct short answers and do not ask what the team will change on Monday.

## Deletion is the right stores and the wrong lifecycle

The second trap is real, and the check enforces it. An index left behind fails. Memory left behind fails. A permitted log that still returns the person fails.

The implementation then collapses two different problems. Primary stores are filtered by person id, which is the right key if every chunk was written with that key. Logs, if they contain the person at all, are replaced wholesale. Other patients' operational history disappears in the same call. A permitted-log rule can be met by destroying the log. A security investigation cannot. The course checklist also says `no-phi-in-logs`, which is the better control: do not put the person in the log, so deletion does not have to erase the log line.

There is no fixture for a backup, a snapshot, a query cache, or an index that only sets a deleted flag. The student who passes has not seen the design problem file 02 documents: a nearest-neighbor index often keeps the vector for graph connectivity until compaction, and a backup is still personal data under the official destruction guideline. The lesson should say that the lab's `drop` is an application-level filter, and that storage erasure is a separate control. It should not claim the lab performed storage erasure.

## Fairness is a measurement, and a narrow one

The shell that returns zero is a good bug. It teaches that a table which hides `d-rim` or an insurance class fails, and that a rubber-stamp rate must include the Thursday rows. The bound is in the pack. The check does not print it. Students compute from the rows. That is the right assessment shape.

The measure is a max-minus-min of yes-rates. It has no base rate, no confidence interval, and no statement of what "yes" means. A wide gap can be a capacity rule (one facility has no Thursday clinic) or a biased proxy (insurance class standing in for something else). The lab cannot tell those apart, and it does not ask the student to say which label they are looking at. File 02 uses Obermeyer and colleagues to show why the label is the finding. This lesson's advanced path stops at the arithmetic.

DNA, language, and facility are the slices the rest of the course has already made available: DNA is a blocked-or-classical problem from Module 01, language shows up in literacy and audience work, and facilities are the hospitals the capacity lessons serve. They are absent from `outcomes.jsonl`. Adding them as columns to measure is in scope. Training a fairer DNA model is not.

## Clock and residency

The teaching clock starts at the release case timestamp on the notice. The knowledge line must say it does not start when the team noticed and does not start at a model. That drill attacks a real failure mode: teams restart the clock at discovery narrative.

It diverges from the official regulation, which starts the 72 hours at awareness and requires the awareness time in the report. A redesigned knowledge answer can hold both: in this case the notice is the awareness record, so the case timestamp is the awareness time; in a real controller's procedure the clock runs from awareness, and a later retelling does not move it. The current sentence teaches only the first half.

Residency is a prohibition sentence: PHI stays off `ext-large`, training stays on the private cloud. The gateway that would enforce the deny is not in this day's modules. Module 03 Lesson 02 already refused the bad hash and the external model for PHI. This DPIA restates it. A DPIA that changes design would point at the enforce point: which process is allowed to call `ext-large`, and which fields are stripped before any prompt is built. The lesson does not ask for that pointer.

## Pedagogy

Chapters 00–04 are reading, the demo, and the CISO interview. Chapter 05 writes the sprint. Chapters 06–08 are paste-the-replacement for eight modules and eight tests, with long "do not paste the picture" instructions. Chapter 09 pastes the pages. Chapter 10 runs the four checks. The paste blocks are the solution. The comments in the solution code are clear and small, which matches the course style. The learning is recognition and transcription.

For a self-paced forward-deployed engineer, transcription has a use: the policy is easy to get wrong in small ways (hold versus block, equal end-date stays open, logs versus rows). The cost is that the student never decides the policy. The demo shows the letter booking under the shell. It does not ask which control would still hold if the family label were wrong.

The words chapter is the best teaching page in the day. It defines each family, the four stores, the grant types, and excessive agency without asking the student to copy a canary. A redesign should keep that page and move the decision into a control matrix the student fills, with the paste reserved for the modules whose behavior the matrix names.

Prerequisites the day assumes, and that the chapters mostly earn: Module 01 treated a letter as data and held an unapproved return; Module 02 split model id from hash and shipped `pol-deploy`; Module 03 kept PHI in `zone-private`, left an unauthorized circular out of citations, and named G1 without closing G2. A student who skipped those will experience this day as a large paste. The lesson does not re-test them except through the supply and citation probes.

## Failures the checks cannot see

- A filter misses, and `book` still runs, because the event was unlabeled.
- The model process holds a long-lived tool credential. The approval id is checked, but the token that performs the book lives beside the model.
- The index delete is a flag. A later compaction never runs. The privacy check reads the application dict, not a segment file.
- A retrieval log stores the passage. Redaction cleans one constructed line in a unit test and not the gateway's real log schema.
- The DPIA says the right residency sentence while a batch job still calls `ext-large`. That failure is graded on a later day (the surge). It is invisible here.
- Disparity inside the bound coexists with a label that does not mean need. The fair check would pass Obermeyer's cost proxy if the yes-rates happened to sit inside the bound.
- Break-glass is audited and left open. The lab does not expire the audit window or review the reason. That is acceptable for one day if the page says the audit row is the start of a review, not the review.
- Rubber-stamp rate is computed and not interpreted. A high rate with the approval id present still passes agency, because the screen saw an approval id. The design note says a rising rubber-stamp rate with flat accuracy is a failed operations story. The fair check does not look at accuracy. It only looks at the share of stamped rows. The student can report the rate and not say what decision it should trigger.

## What a redesign must preserve

The hidden set stays hidden. Miss text stays free of secrets. The four checks stay separate. The sprint still opens the notice first. The four stores stay. Stale access still closes, break-glass still audits, the open grant still stays open. The twelve families stay on the config. The checklist stays the `pol-deploy` six. Canaries stay out of prompts and logs. The patient reply stays. G1 and G2 stay different words.

What changes is the thing those checks are evidence of. File 03 specifies the architectures. File 04 specifies the exercise that does not hand the student an attack to write.
