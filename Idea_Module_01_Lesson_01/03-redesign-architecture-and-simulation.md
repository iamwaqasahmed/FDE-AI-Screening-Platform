# Redesign: architectures, simulation, data, and failures

File 01 says the current release grades a script. File 02 says the fetched week-one sources grade a decision. This file compares four ways to build the release, specifies the packet, and lists the failures the packet must be able to produce. Labels: **Proven** for a method a fetched source already uses, **Emerging** for a sound adaptation with a narrow evidence base, **Experimental** for a course-design proposal.

## Four architectures

### A — Vocabulary and a green pipeline

This is the release as it stands. The learner reads the kickoff, pastes an access request, keeps `GET /health` and `scan.py` green, and runs two supplied interview scripts. Deploy manifests sit unused.

**Experimental** as an arrival pedagogy. **Proven** pieces inside it: the claim rule, the 2023 document split, and a scan that fails closed on a marker. It hides the system of record, the politics, and the refusal. It is easy to auto-grade and hostile to a non-engineer, because the long path is Python setup in order to watch a test that already passed. It does not spoil Lesson 2's rates, mostly because it never opens the data.

### B — Discovery simulation, no service

The graded object is a decision memo. Inputs are a contact-center transcript, a small dirty extract, the existing kickoff, and the interview simulator with the questions removed from the chapter. The learner may recommend staying at G0 and refusing to grade urgency. No application is built. This is the GDS and USDS shape, compressed into one self-paced sitting: do not start the service; observe; separate assumptions from files; be willing to tell the sponsor the proposed fix is the wrong fix. **Proven** as those organisations' published method. **Experimental** as this particular packet, because a transcript is not a live shift and a two-to-four-week sprint does not fit beside `rel-m01-l02`.

### C — Access plus one query

Palantir's fetched 2022 note puts a scoped problem and technical setup in the same pre-pilot, then an ontology on real objects. A teaching version is: the access request is negotiated, and the learner runs one profile of a granted extract (row count, latest timestamp, grain, identifier collisions) and writes what they would not build. No model, no health URL, no container. **Emerging** as a lesson, because the partnership PDF describes a multi-week pilot with client users in the room, not a solo query. **Experimental** if the chapter prints the query and the expected collisions. The generator's defects (two date eras, a reused clinic code, Ain's nightly file) are the point. The learner should find one of them.

### D — Stage-gate document factory

The learner fills G0 as Cooper-shaped stage work: problem, users, sponsor, a cost guess, a kill criterion, a risk class. The client's page already defines G0 more thinly, as names only. Expanding G0 into a business case copies Stage-Gate's stage 2 into a gate the client defined as intake. **Proven** that authentic Stage-Gate includes a kill (file 02). **Experimental** and a poor fit as the whole release: it produces paper, it does not open the contact center or the extract, and it invites the learner to invent costs Lesson 2 has not released.

### Comparison

| | A. Green pipeline | B. Discovery simulation | C. One query | D. Gate paperwork |
| --- | --- | --- | --- | --- |
| Graded center | Intact template, two scripts | Decision memo a stranger can audit | Memo plus a profile of granted rows | A thicker G0 form |
| Can show a refusal | Only in an unscored debrief | Yes, if the memo requires one | Yes | Yes, if a kill line is required |
| Can show a messy system of record | Mentioned, not examined | Extract plus transcript | Extract is the lab | No |
| Non-engineer path | Blocked on Python | Reading and writing | Blocked if the query is required | Open |
| Lesson 2 spoiler risk | Low | Medium, if rates leak | Medium, if the profile prints a rate | High, if the form asks for savings |
| Auto-grade | Easy and currently too weak | Structural checks only | Structural plus one asserted defect | Easy and gameable |
| Matches fetched week-one sources | The scan only | GDS, USDS, NIST Map | Palantir pre-pilot, compressed | Cooper's kill, not his evidence |

**Recommendation.** B is the spine. Keep a forty-five-minute slice of A after the memo, limited to the scan and the policy file, with the deploy manifests deleted from this release. Offer C as an advanced path for readers who already run Python, not as the pass line. Do not adopt D as the lesson. Keep the client's G0–G5 page in the kickoff so the memo can say "we are still at G0" in the client's words.

## The packet

One person, one sitting of about five to seven hours after the machine page, no second human. The classroom pair stays: this release in the morning, Lesson 2 in the afternoon. Nothing below prints a gold rate.

**Shadow shift.** A transcript of one contact-center hour, written as turns, not as a story with a moral. The agent answers status calls from a screen that does not show pending referrals, copies a phone number into a spreadsheet because the system of record and the dialer disagree, loses a caller, and says "people just don't show up." The learner marks each system switch, each hand copy, and each sentence as claim, request, or fact. A fact must name a file already in the packet. The agent's sentence about no-shows is a claim. **Experimental** as a substitute for USDS observation. It is the honest substitute for a solo learner. Do not add a narrator who explains the nine problems.

**Dirty extract.** Forty to eighty synthetic rows emitted by the existing generator, not by an outside population. Columns a learner can misread without a rate: a facility id, a specialty, a clinic code that appears as both `END-01` and `ENDO-CLN`, a date with no era marker, a nightly-file timestamp on Ain rows and a null slot, a shorthand note, a phone shared by two different names. The audit sheet asks four questions only: what is the grain of a row, what would make the row stale, which fields identify a person, which fields are a code versus a shorthand. No model, no split, no accuracy. **Experimental** as the artifact. **Proven** that these defect types exist in `01-hidden-world.md`. The release shows a handful of rows, not the mechanism and not the percent.

**Power map.** All twelve cards stay visible. The learner places each person on two axes they define in words: who can stop a build, and who is pushing the sponsor's sentence. They must name, from the cards alone, who can forbid an urgency grade, who can forbid `ext-large`, and whose opening number is a claim from outside the cluster (the vendor). Interview budget remains two scripts. The chapter no longer names the pair. A faded example, after the baker, shows one good question and one question that bounces, on a card that is not graded. **Emerging** as a solo substitute for a USDS stakeholder read. The workshop dot-vote in the facilitator design can wait for a later readout. Dropping it into this morning would tell the learner that triage won a vote before they have a reason to refuse it.

**Access negotiation.** The learner writes the four fields. A small simulator, not a paragraph in the chapter, returns one of three results: granted, narrowed, or refused. Full history is refused. A missing classification is refused with the instruction that the office will not guess, which mirrors the shape of the SDAIA sharing rule without citing it as the client's law. Kickoff files plus the watermarked dev credential, classed `internal`, purpose limited to this release's interviews and the scan drill, is granted. A request that calls the sample letter `public` because it is synthetic is refused. The letter stays in the packet either way. **Experimental** as software. The refusal is the lesson. The current chapter's printed grant is the bug.

**Decision memo.** One page, checked for structure. Required slots: the sponsor's sentence copied and marked `claim`; one fact with a document id that exists in the kickoff (the stage-gate line on emergency wording, or a discrepancy between the postmortem and the minutes); one unknown; one will-not-build, which must be an urgency grade or triage by the assistant; one value hypothesis with a user and a pain and no percentage; the zone sketch; a separate three-field classification (for example clinic hours, the kickoff policy, and the sample letter). The hypothesis is allowed to be wrong. Lesson 2 exists to test it. A hypothesis that is only "build the front desk" fails the slot. **Experimental** as the graded center. It is the NIST Map go/no-go, shrunk to a page, and it is not a claim that the learner has finished discovery. GDS's four to eight weeks do not fit in a morning. The page should say so: this is the first cut, and stopping is an allowed recommendation.

**Assistant drill, after the memo.** Run the test and the scan. Read the policy. State, in the memo or a short addendum, that the scan sees `work/` and does not see a prompt or an agent session. Do not paste the letter. The trainer's existing demonstration — a junk file in a throwaway copy, a failure line that names the marker and not the watermark — stays. Delete `Dockerfile`, `compose.yaml`, and `deploy/namespace.yaml` from this release's definition of done. They return on the release that deploys.

**Institutions card.** One page, staff-audience, not a quiz. DGA, SDAIA, NDMO, NCA, and the PDPL exist; the case uses its own gates and its own three labels; the two SDAIA classification PDFs do not even share one fourth name, so the learner must not "correct" `internal` into Restricted or Confidential. **Proven** content, from file 02. **Experimental** as a course page, and it must not be written as legal advice.

## Advanced ideas worth a sidebar, not a second lesson

Epistemic status is already claim, request, and fact. Add two statuses the memo may use and the check need not parse: an assumption (a sentence someone believes, with no file) and a prohibition (a sentence an in-force document forbids). The sponsor's triage line is a claim that collides with a prohibition. **Emerging** as a worksheet extension of a rule the lesson already teaches.

Hard and soft constraints, from the GDS page: the weekend calendar and the clinician-owned urgency are hard inside this case; "security reviews at the end" is a soft constraint the CISO states and the in-force habit of the case should resist. **Proven** as GDS's distinction. **Experimental** as a column on the power map.

Minimum necessary is the access form's real subject. Asking for the kickoff is a different act from asking for every referral since 2023. PDPL's data-minimisation idea and SDAIA's ethics principle are context. The client's rule is the narrower one the simulator enforces. **Proven** as a pattern in the fetched Saudi texts. **Experimental** to assess learners on the statute.

Grain and freshness are the advanced version of C. A row can be a referral, an appointment, or a call. A timestamp can be the referral, the booking, or the nightly file. Lesson 2 owns the dashboard clock. This release only asks which timestamp the extract actually has. **Emerging** as a question. Printing the answer in chapter 09, as the zone table is printed today, would repeat the current failure mode.

The perception gap on coding tools is a sidebar in the drill, with the UK trial and the METR updates cited as in file 02, including the intervals and the authors' caveats. No number is taught as the cohort's expected speedup. **Emerging** evidence, **Experimental** if a quiz item treats 56 minutes as a fact about these learners.

## Datasets and synthetic material

Use the course generator. `01-hidden-world.md` already plants the defects a first audit needs: more than one spelling of a name, a shared phone, Hijri and Gregorian dates, a reused MRN, a clinic-code change at Wadi, Ain as a nightly file, a weekend of Friday and Saturday. Emit a seeded slice for `practice` at `rel-m01-l01` that contains a few of those, stable across runs of that seed, small enough to read in a spreadsheet. Do not include gold rates, pairwise identity labels, or the attendance model. The `personal` profile (hundreds of people) is the right scale if a full practice world is too heavy for a laptop. The `small` profile is a fallback. Either is better than a new population.

Synthea, fetched from its README, is MITRE's synthetic generator, Apache 2.0, copyright 2017–2025, defaulting to Massachusetts demographics and emitting FHIR. See the [README](https://raw.githubusercontent.com/synthetichealth/synthea/master/README.md). **Proven** synthetic. **Experimental** and wrong inside Al-Waha: US defaults, identifiers that are not this case's, and a second population the later checks do not share. It can point at a future prep course. It is not this release's data. The sample letter remains the PHI-shaped object. Synthetic is not a class. Marking it `public` because the file says it is not a real record misses the fields. This review did not open a credentialed clinical corpus and does not recommend one.

Call-center text should be written for the case, not scraped. The facilitator design already calls for observation notes and call-reason codes. Author a short transcript from those intentions. Leave the reason-code distribution, and the fact that uncoded calls are visible, to the release that measures `p-status`. A transcript that says "most calls are status" would steal that measurement. A transcript that shows one status call, one abandoned call, and one hand-copied number does not.

## Production scenarios the memo should survive

These are situations a real first week produces. Each one should be reachable from the packet without a hint paragraph that states the moral.

**The grant is the constraint.** History can be withheld and the learner still decides. The product is a narrower question and a list of unknowns. The unsigned ruling stays a claim. The memo can still keep the sample letter off `ext-large` because the assistant-use policy is in force today.

**Two stories of 2023.** The postmortem and the minutes disagree. A memo that cites only the busy season has treated the write-up as the whole story. A memo that cites only the minutes and ignores the write-up has done the mirror error. Both rows stay. Settled: the bot was switched off, and the minutes name three notes. Unsettled: which of the write-up's causes survive.

**The date may stay unknown.** Spending a question on the CDO can reveal a long purchase. Skipping her should still pass, with the unknown slot saying the date's feasibility was not tested. Printing the lead time in the stem spoils the tree. The card stays visible. The question stays unprinted.

**Ain is not an API.** Ain sits in `zone-hospital`. The extract's Ain rows carry a file timestamp and an empty slot. A memo that promises live booking at every hospital has not read the rows. Do not reprint the facility ids in the finish chapter. The rows do the work.

**The vendor's number and the BI lead's improvement** are claims on cards. A value hypothesis that adopts either one as a baseline fails the "no percentage you did not compute" rule, and it fails the claim rule. Lesson 2 will show why both numbers mislead. This release only requires that they stay claims.

**Friday and Ramadan** are on the kickoff calendar. A hypothesis that assumes a Monday-to-Friday center is already wrong on files in hand. That prepares the later SLA trap without revealing the calendar-count bug.

## Edge cases and failure modes of the simulation itself

**The check becomes the new script.** If one sentence satisfies will-not-build, cohorts will paste it. Check a real document id, the labels claim and fact, the absence of the two banned sentences, a sample-letter class of `phi`, and a hypothesis that names a person rather than "every hospital." Do not grade prose. File 04 is the human rubric for a memo that is structurally valid and still empty.

**Another pair can be right.** The medical director and the data protection officer suffice for the refusal and the residency claim. A learner who interviews the coordinator and the enterprise architect may reach shorthand and the nightly file and miss the unsigned ruling. The unknown slot is how they pass honestly. Failing the "wrong" pair repeats chapter 08. Must-surface facts stay a debrief, matching the facilitator note that skipped personas still meet a paper trail later.

**The shadow must not wink.** If every turn points at one problem id, the learner will rank it without evidence. Write one status call, one abandoned call, one caregiver, and one hand-copied number. The job is to notice workarounds.

**Assistant collusion.** A draft question list is the useful move from file 02. Pasting the extract or the letter is the theatrical one. The scan catches the letter in `work/` and misses the prompt. The drill says so in the learner's words. Decide explicitly whether a `phi` extract is allowed in `work/`. Stripping identifiers so the scan stays green teaches the wrong trade.

**Solo voice.** The packet still splits work by artifact: access file, shadow notes and hypothesis, field classes and audit, zone sketch and power map, scan. File 04 assigns the hours. A single essay that never opens the extract fails because the audit table is missing. A memo that ranks all nine problems is Lesson 2 done early. The hypothesis slot allows one pain. Further pains go in the unknown list, which is what keeps the morning from eating the approach lesson.
