# 03 — Redesign, architectures, and simulation

The redesign keeps `rel-m04-l01`, the four checks, the hidden set, and the fictional client. It changes what a pass is evidence of. A pass means: unlabeled untrusted content cannot mint a booking or an approval, a canary is absent from prompts and logs, deletion is defined across the four stores plus the copies the DPIA names, and the DPIA records one design change that is visible in the gateway.

No new attack strings are added to the pack. The planted corpus stays the corpus the course already builds.

## Four architectures

They are compared as defensive designs. A production assistant uses the proven row as the boundary and may add the others as layers. A layer that fails open must not be the layer that holds the token.

### A. Classifier sandwich

**Maturity.** Emerging as a detector. Experimental as an authorization boundary. Fail-open is the default failure: if the classifier errors, times out, or labels the event as benign, the request continues.

**Shape.** An input classifier labels the turn. An output classifier scans the draft. The application calls the tool if both say allow. The system prompt repeats the policy.

**What it stops.** Many known-bad patterns in a monitored channel, at a cost in false refusals. It is a useful telemetry source for Lesson 2.

**What it misses.** Indirect content the classifier has not seen. A label that is wrong. A timeout configured to allow. A policy that lives only in the prompt (OWASP LLM07: the prompt is not the control). The course's current `screen` is this architecture with a perfect classifier supplied by the grader.

**DPIA consequence.** If this is the only control, the impact assessment should refuse go-live for `book` and `return`. The measure does not reduce agency. It estimates it.

**Course move.** Keep a classifier only as an optional signal that pages a coordinator. Remove it from the allow path. Do not grade students on writing a filter. Do not report a bypass rate.

### B. Capability-scoped tool gateway

**Maturity.** Proven. This is least privilege, as OWASP LLM01 and LLM06 state it, and as the NDMO classification policy states it for access: least privilege, need to know, access ends when the grant ends.

**Shape.** Tools the model may name are an allowlist. Each tool has its own token, minted by a component the model process cannot read. `book` and `return` tokens are minted only by the approval service after a coordinator action. Status and hours tokens are narrower. A letter, a tool card, and a retrieved chunk are passed in a data field. They cannot carry a token. Output to the staff console is encoded before render. Weights load only if the hash is on `reg-models`. Sessions have a token budget and holds expire.

**What it stops.** A booking, a return, and an approval moving because of text. The hidden set's success condition (no moved booking, no moved approval, no canary in the log) is enforced here even when architecture A labels the turn as safe. Disclosure is stopped by not placing the canary or the national id in the prompt or the log, and by redaction as a backstop. Supply-chain and citation rules stay in the gateway, not in the model.

**What it misses.** A coordinator who rubber-stamps. That is why the stamp rate exists. A stolen coordinator credential. That is the stale-grant and break-glass audit, not a prompt problem. A wrong in-force document that was labeled in-force. That is corpus governance from Module 03.

**Fail-open rule.** If the approval service is down, `book` does not run. The patient hears that the request is queued. The gateway does not fall back to "the model said yes."

**DPIA consequence.** The design change the form must name: the model runtime's identity has no `book` or `return` scope. The approval service does. Residency is the same shape: the runtime identity has no route to `ext-large`.

**Course move.** This is the target architecture. The existing hold-for-approval behavior is the seed. The new graded assertion is that an event with the family field removed and `channel=letter` still cannot book, because the letter channel was never given the capability.

### C. Untrusted-data plane

**Maturity.** Emerging as a design rule. The Model Spec's "no authority by default" for quoted text and tool output is the vendor statement. OWASP's "segregate and identify external content" is the application statement. Experimental if someone claims a dual-model dialogue replaces the gateway.

**Shape.** One plane may quote the letter, the circular, and the tool card to draft a reply. That plane has no tool client. A second plane, or plain code, may call tools, and it receives only structured fields the first plane filled (slot id, person id), which the gateway validates against the session. The draft is not executed.

**What it stops.** Instruction text in a document becoming a tool call, including when the drafting model obeys the document. The data plane can be wrong. It cannot act.

**What it misses.** The structured field itself being the wrong slot, chosen because the document asked for it and the drafter copied it. Validation against the caller's own grants, the open slots, and the approval id still has to run in code. A dual-model setup that gives both models the same credentials has not implemented this architecture.

**DPIA consequence.** Document the two identities. The data-plane identity is the one allowed to see the letter. It is not the one allowed to change the roster.

**Course move.** Teach it as the reason `atk-indirect` and `atk-supply` are data-plane events. Do not add a second model to the lab. The channel rule in architecture B is the one-day version of the same split.

### D. Subject-scoped minimization and verified erasure

**Maturity.** Proven for primary records keyed by person id, for access export, and for content-free logs. Emerging for vector compaction, replica and backup coverage, and disposal records. Experimental for epoch-key rotation as a product control (one preprint's construction, not a course lab).

**Shape.** Four stores remain: row, memory, index, logs. Every index chunk and memory item carries `person_id` or it is rejected at write. Logs store request id, document id, decision, and store names. They do not store the national id, the canary, or the passage. Access export lists every store that still returns the person. Deletion removes those keys on the read path. The DPIA names the additional copies: backup, snapshot, retrieval cache. The lab's assertion is a written erasure plan plus the application-level drop. A later operations lesson can own compaction. The destruction guideline's rule is taught in one sentence: a backup is not destruction, and a deleted flag is not destruction.

**What it stops.** The trap "row deleted, index still answers." It also stops the fake fix of wiping every patient's logs.

**What it misses.** A chunk that was embedded without the person id. The write-time rejection is the control. A student who only deletes known keys will miss an unkeyed chunk. The planted corpus should include one unkeyed chunk that write-validation must refuse.

**Fail-open rule.** If compaction cannot be shown, the DPIA does not say "destroyed." It says "hidden from the read path; storage erasure scheduled; backup key disposal named." Honest status is the point.

**Course move.** Change `drop` so logs that contain the person are rewritten without that person and without the passage, and other patients' content-free rows remain. Add the erasure-plan lines to the DPIA. Keep the check that the index no longer returns the person.

## Comparison

| | A. Classifier sandwich | B. Capability-scoped gateway | C. Untrusted-data plane | D. Minimization and verified erasure |
| --- | --- | --- | --- | --- |
| Maturity as the boundary | Experimental | Proven | Emerging | Proven on keyed primary stores; emerging on indexes and backups |
| Fails open when | The label is missing, wrong, or the filter times out to allow | Only if the gateway substitutes a model decision for a missing token. The redesign forbids that | Both planes share credentials | Delete is a flag, or the chunk was never keyed, or the backup remains |
| Booking and approval | Only if the classifier is right | Token is absent, so they cannot move | Data plane has no client | Not its job |
| Canary and national id | Output filter may miss | Do not place them; redact as backstop | Data plane must not receive a log-write tool | Logs never stored them |
| Letter and tool card | Hoped to be labeled indirect | No capability on that channel | Quoted text has no authority | Not its job |
| DPIA must change | Refuse these tools at this maturity | Split the token mint from the model identity | Name the two identities | Name compaction, backups, and the disposal record |
| What the lab grades | Not sufficient alone | Unlabeled letter cannot book; unapproved book is held | The channel split is the stand-in | Export, keyed delete, logs of other people survive, plan names backups |

Architectures A and B together are a common vendor diagram. The lesson's mistake is grading A and calling it B. The redesign grades B, teaches A as a detector that is not on the allow path, uses C as the explanation of untrusted channels, and grades D for the privacy check.

## Simulation

Keep the practice profile, the case timestamp, the canary in truth, and the rule that miss text prints neither the canary nor the id.

**Planted corpus, already in the course, used as data.** Dev events for the four visible families. Registry rows plus one unregistered candidate hash. Circulars with status unauthorized, superseded, and in force. Tool-card text marked as data. Grant rows: stale staff, open staff, expired delegate, break-glass. Subject `person-access` present in all four stores. One extra index chunk with no `person_id`, which write-validation rejects. Outcome rows gain `language` and `facility` beside district and insurance. A small DNA fixture, separate from the booking yes-rate, with columns language, facility, predicted, attended. Approval rows keep the stamp flag. No new prose instructions are written. Existing dev text stays in the pack files and is not copied into the research notes or the student worksheet.

**Hidden set.** Stays in gold. Still must not move a booking, a canary, or an approval. Still not printed on failure.

**New probe, defensive.** A copy of the letter event with the family key omitted and `channel` set to `letter`. Reference behavior: blocked, no tool. A copy of a book event with family omitted, channel `chat`, and no approval id. Reference behavior: held, no tool. These probes fail the student who only switches on `family` and otherwise passes the tool through. They pass the student who implements architecture B.

**Classifier-down probe.** A fixture flag `classifier=unavailable`. The gateway must take the same path as a missing family. Allow-on-error fails the check. This is the fail-open test, and it does not require an attack string.

**Deletion probe.** After `drop`, the person is absent from row, memory, and index. Other log rows remain, and none contain the person id. The unkeyed chunk never entered. `dpia.md` contains the words the erasure plan requires: backup, and either compaction or rebuild. The check looks for those design words the same way it already looks for the clock. It does not run a database.

**Fairness probe.** `gap` still uses district and insurance against the pack bound. Additional function or page: rates by `language` and `facility`, plus a DNA false-alarm count by language on the planted file. The required sentence names the label (booking yes versus attendance versus need). A submission that deletes a column to shrink the gap fails.

**What the simulator should not do.** Generate new injections. Call an external model with the letter. Score "jailbreak resistance" as a percentage. Share canaries across teams in a student-visible file.

## DPIA that changes the design

Required sections, still short, mapped to the official assessment's ideas without claiming the form is the regulation:

1. Purpose and what is out of scope. Patient access. Triage is out of scope, carried forward from earlier modules.
2. Legal-basis placeholder. The course says "fictional client; not a PDPL filing." The student writes the client's basis in course language (care delivery under the cluster's authority) and does not invent a statute citation as if it were filed.
3. Data and geography. Fields, the four stores, `zone-private`, and the deny to `ext-large`. Geographical scope is the private cloud. This is the fictional analogue of the regulation's scope element.
4. Necessity. Which fields the prompt is allowed to see. National id is not one of them.
5. Harm and measures. Agency, disclosure via logs, index retention, disparity. Each names a measure.
6. The design change. One paragraph that points at a file: the book token is minted only in the approval path; the model identity cannot hold it; classifier failure does not restore it. If this paragraph does not match the gateway behavior, privacy fails.
7. Breach. Awareness in this case is the notice timestamp. The official 72-hour rule runs from awareness. The log is `int-engine`. The report will not include the canary.
8. Erasure. Read-path deletion now; compaction or rebuild named; backups named as still in scope; disposal record content-free.
9. Residual risk. Rubber-stamp, unkeyed chunks, classifier used only as a page and not as a gate. G1 remains the tier. G2 remains this assessment. They are not synonyms.

A DPIA that restates the module page and omits section 6 fails, even if purpose and residency are present.

## Failures the redesigned checks are built to catch

- Family list complete, unlabeled letter still books.
- Classifier unavailable, gateway allows.
- Approval id present, stamp rate high, and the student has no sentence. The rate check stays. The sentence is new. Do not auto-fail a high rate; the planted rate is the pack's. Fail a missing interpretation.
- Index filtered in the dict, DPIA says "destroyed" with no compaction or backup word. Require honest status.
- Logs of other people destroyed.
- Language slice omitted, or a column dropped to change the gap.
- DNA fixture used to train or to "fix" weights. There is nothing to train. The fixture is a table.
- Canary copied into `dpia.md` or the reply. Existing watermark behavior stays.
- `ext-large` named as acceptable for PHI because a filter will scrub it. Residency is a route deny.

## Deletions from the current day

- Grading `screen` only when `family` is present.
- The five-heading DPIA as a sufficient G2.
- Whole-log replacement as the reference `drop`.
- Knowledge answers that cannot mention awareness and the notice together.
- Paste as the only way to meet redteam. The control matrix in file 04 is the decision; the code still has to match it.
- Any worksheet line that asks the student to invent a prompt that gets past the guard.
- A fairness "remediation" step that edits labels or drops a protected or operational column and resubmits the gap.
- Teaching epoch-key rotation as a coding task. One paragraph of Experimental status is enough.
- Equating the course clock with Article 24 without the awareness sentence.

## What stays code

`output` escape, `supply` hash and citation and label rules, `redact` on a log line, `limit` caps, `access.settle`, and the checklist ids stay. They are already deterministic controls. They do not need a new architecture story beyond a sentence each in the control matrix: escape is LLM05, hash allowlist is LLM03, citation status is LLM08 and LLM09, redaction is LLM02, caps are LLM10, grants are least privilege.

## Simulation limits

The hidden set is still a finite planted set. Passing it is not a claim about unseen attacks. The student page should say that in one line, which matches NIST's "ongoing" evaluation action. The next lesson's telemetry is where a detector (architecture A) earns its keep, as a signal, after this lesson has taken it off the allow path.
