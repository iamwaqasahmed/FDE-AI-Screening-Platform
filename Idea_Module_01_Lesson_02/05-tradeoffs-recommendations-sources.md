# 05 — Tradeoffs, recommendations, and sources

This file is the decision record for a later editor. It assumes files 01 through 04. It does not authorize an edit to the student copy by itself.

## Tradeoffs

**Answer key versus a check that does not echo the answer.** Chapter 07 makes the release passable in one sitting, including for a self-paced learner who never interprets a split. It also makes the syllabus verb "select" false. Removing the key without a toy example makes `family does not fit` a locked door, because the checker, correctly, does not say which family would fit. The resolution in file 04 is a worked `p-toy` that uses none of the nine ids and none of the extract digits. Cost: one extra page to maintain when the family vocabulary changes. Benefit: the nine rows become the learner's. This tradeoff should be resolved in favor of the toy. The current resolution, printing the graded table, teaches transcription.

**Strict gold versus implementation freedom.** Later lessons need a stable floor: triage absent, slots not booked by a model, bounce carrying a clause, status coming from a tool. Widening gold so that "agent" is legal on the clock would break Lesson 3 and the readout. Freezing the memo at the token, with no rejected-alternative column, lets a legal token carry an illegal action (classical DNA model, action overbook). The resolution is to keep the forbidden sets, and to add a small stem check on the rejection and the action. Cost: more brittle stems, and a learner who writes a correct idea in unexpected words may fail. Mitigation: the stem list is short and the toy shows the voice. Do not grade the reason with a language model. That would put PHI-adjacent text into a grader and would hide the criterion.

**Any ranking versus a single official order.** The design doc is right that value ranges do not produce one true sequence. The current check is wrong that almost every sequence is acceptable. Illegal sequences are real: blocked problem first; a SAR claim used as a baseline before the clock column is fixed; DNA prioritized on the director's 910,000 while the return figure and the identity dependency are unmentioned. The resolution is constraints, not a unique key. Cost: a learner who puts `p-info` first for a coherent reason must still mention the clock before spending money figures. That is a fair constraint, because the design doc says the clock changes the value of the rest. Benefit: the sponsor cannot lead the roadmap with 3,000,000 SAR and a disclaimer.

**Person holdout on sorted ids versus a person-grouped time split.** The sorted-id split is easy to read in twenty lines and, on this practice file, dramatic (`0.7692` versus `0.0000`). It is not the decision-time split. A person-time split needs dates and an as-of rule, and the score may look disappointingly close to the row split, which is what Wilimitis and Walsh saw when within-person correlation was low. If the new split ships before the debrief is rewritten, learners will think the lesson is broken because the leak "disappeared." Ship the printout with a sentence in the solution, not in the morning glossary, that a small gap can be the true result and the row split is still illegal. Keep the old commands during the transition so existing tests have a home.

**Seasonal naive versus a richer forecast in the same lab.** ETS, Prophet-class holiday regression, and gradient boosting are the serious next tools. Teaching them on this day would bury the baseline. File 02 records why they stay candidates (M5, the 2009 clinic study, Tan and colleagues' ablation and its scope). Tradeoff accepted: the lesson stays with `seasonal` and `mean`.

**Fine-tune now versus fine-tune in Module 3.** Hamel Husain's conditions for fine-tuning (narrow task, prompt becoming a conditional thicket, latency, data that must stay inside the boundary) are exactly the bounce-letter problem once "sugar clinic" and "retina" have beaten the word list. Doing it now duplicates the adapter lesson and trains on a handful of watermarked letters. OpenAI's 30 October 2026 optimization page, which says hosted fine-tuning is winding down for new users and which also lists medical diagnosis as a reinforcement example, makes "just fine-tune the big model" a worse default than it was, and a more dangerous one if the example is copied onto triage. Tradeoff accepted: Lesson 2 prices `cost.label` and `cost.coordinator_hour` and records the keyword list as the line to beat. Module 3 fits the small model inside the ruling, on `local-small`, or it does not fit one at all.

**Reasoning models as a cost surprise.** They can replace some format-following fine-tunes and they can make a single tool call reliable enough for `p-status`. They also add tokens the course price sheet does not name. No verified multiplier is available in this pack. Forcing a number would invent a benchmark. Forcing a blank marked `unpriced` teaches the gap. Tradeoff: the advanced sheet looks unfinished. It should look unfinished. An unpriced risk next to `price.ext_large_per_1k` is the point. Residency still dominates the arithmetic for identified text. A cheaper external token price is not a reason to move PHI.

**Remind-everyone versus a targeted DNA model.** Oikonomidi and colleagues found targeted messages and calls probably reduce no-shows, and found overbooking's effect too uncertain to pool, with equity barely reported. A model that cannot beat "SMS everyone," priced at `cost.sms` of 1 SAR, does not earn a GPU hour at 42 SAR. The practice sample is too small to estimate that saving. The memo can still write the comparison as the gate. Tradeoff: learners want to build the model the family word invites. The family word stays `classical-ml` because the design doc's end state is a model with a person-grouped time split. The gate in front of it is the reminder. Silent overbooking is not a tradeoff. It is forbidden, on the course's own `d-rim` harm and on the mechanism in Samorani and colleagues (about 30 percent longer waits for the higher-risk group in their US specialty data, not a figure to reuse).

**Build versus buy depth.** A full Epic or Mawid lab is impossible and unwanted. A one-page questionnaire is enough for a foundations day. The risk of including vendor names is that a learner writes "Al-Waha uses Cadence." The instruction forbids that sentence. The risk of omitting vendor names is that "system of record" stays a column of magic words (wait-time mart, session book) with no picture of why a second writer is a production incident. Include the names in the advanced reading only.

**Regulator analogues versus the cluster rule.** FDA's four-part non-device CDS test and SFDA MDS-G010 give the learner a way to talk to a sponsor who says "decision support is not a device." They also tempt a fake legal memo. The checker cannot grade law. The chapter says the pack is not legal advice, the in-force control is `pol-stage-gate`, and the external texts explain why a disclaimer is not a control. WHO's autonomy principle is the ethics sentence: a human remains in control of the medical decision. Tradeoff accepted: three short citations in the advanced slice, none in the foundation command list.

**Shared classroom day versus a heavier lab.** Arrival already consumes the first half. Adding person-time data, three retrieval pages, a cost sheet, and a build-versus-buy page on top of an intact chapter 07 will not fit. The deletion of the answer key is what makes room. The advanced slice is after the checks, including as overnight work. A new lesson in the ten-day calendar is refused below.

## Recommendations

Adopt the following, in this order, or do not start:

1. Delete the answer blocks in student chapter 07 and the score spoilers in chapters 04 and 06. Add `p-toy`.
2. Change `chk-brief` so `p-triage` in rank 1 fails even when the urgency sentence is present. Keep the requirement that the urgency sentence appears on the triage line. Update `test_triage_first_needs_the_urgency_rule` in the same change. Update the solution ranking commentary that says any order passes.
3. Grade the four tool sentences and a `rejected` stem column.
4. Stop using 510,000 SAR as the size of `p-waitlist`. Allow a claim size and a measured size on `p-bounce`. Mark the waitlist `unmeasured` until an identity sample exists.
5. Add the advanced slice as student text that the foundation checks do not read: three-id cost sheet, build-versus-buy questions, forecast prior. Put the finished example in the solution copy beside the current optional cost section.
6. When the data generator can do it safely, add `--split person-time` and a leaky column demo that is not the graded script. Do not remove `--split person` until the tests move.
7. Leave Module 3's adapter, Lesson 3's intake, and Lesson 4's booking trap where they are.

Do not adopt: a unique official ranking; a Prophet or LightGBM lab; a live fine-tune; an agent that covers all nine ids; a shadow appointment database; any overbooking simulator; any urgency classifier; a checker that calls a model; pasting this idea pack into `Student_Copy`.

## New lessons, and the ones not to add

The ten-day map pairs this release with arrival. A twenty-first release would shift every later id. Refuse a new lesson slot.

**Add inside this release, foundation.** The rejection column, the rank constraints, the toy, and the graded tool lines. That is a revision of Lesson 2, not a new lesson.

**Add inside this release, advanced, after green checks.** "Three architectures on three problems": ladder, agent-default refusal, second system of record. One cost sheet. One build-versus-buy page. One forecast paragraph. Title it in the student folder as a chapter that opens only after finish, the way other modules already treat advanced files. It is not `rel-m01-l02b`.

**Do not add.** A fine-tuning lesson. Module 3 Lesson 2 is that lesson, and the curriculum map already sends the bounce letters there after the ruling. A forecasting elective can wait until someone has a published outpatient comparison that beats seasonal naive on a later window under a pre-registered split. Until then, a reading note in the advanced chapter is the whole elective. An "AI triage with a human in the loop" lesson would delete the trap the map told editors to keep. A DNA-model-building lesson belongs, if anywhere, after identity and reminder reliability, which the dependency diagram already places upstream, and it would still forbid overbooking. It is not this day's job.

**A later real client** is outside these folders, as the understanding map says. The questionnaire in exercise 8 is the portable piece: system of record, who may write a slot, whether did-not-show is already a message, whether the containment statistic is this site, whether urgency is in the statement of work. That questionnaire is the forward-deployed skill. The nine-row menu is the classroom floor underneath it.

## Deletions, stated as deletions

Delete from the student path, when an editor implements this pack:

- The nine pasted approach lines, six claim lines, nine size lines, and nine rank lines in chapter 07.
- The preview that the person line is `person 0.0000` and the explanation of `p16`–`p23`, in chapters 04 and 06. The solution chapter may keep the practice-profile printout for the comparison after the checks.
- The sentence that any order of the nine ids passes.
- The sentence that triage may be rank 1 if the line mentions a clinician.
- The status of cost as the only economics, and only optional. Keep the 84-word warm-up if the letters stay in `packet/` and no line is copied.
- The parking of `510000` on `p-waitlist` as that problem's size.

Delete from the facilitator story, not from the world:

- The idea that the advanced cost column can remain unscored forever if the syllabus still says "compare."
- The idea that a reasoning model or a small fine-tune is a family. They are implementations inside a family, or they are rejections.

Do not delete:

- Problem ids `p-dna`, `p-status`, `p-bounce`, `p-slots`, `p-clock`, `p-info`, `p-forecast`, `p-waitlist`, `p-triage`.
- Family tokens and the forbidden sets on clock, slots, and triage.
- `dna.py`, `messages.py`, `letters.py`, `demand.py`, and the rule that learners copy them.
- The unread column `appointment_status_final`.
- The watermark failure.
- Banned sentences such as "Waiting time fell last year," "Al-Waha containment is about 70 percent," and "The assistant may set clinical urgency."
- The claim versus fact distinction, the vendor pilot sentence, and `booking_date` as a fact.
- The dependency story: clock before honest value; identity before waitlist, DNA, and status; criteria in force before bounce; reminders before a clever DNA model.
- The trap list in the understanding map.

## Status rollup

| Claim | Label |
| --- | --- |
| Rule before model; simple baseline before a heavier model; temporal test | Proven (Zinkevich) |
| Retrieval for changing facts; fine-tuning for stable behavior; prompt first as an eval stress test | Proven as practice (Husain; OpenAI's accuracy guide, vendor-scoped) |
| Hosted fine-tuning winding down for new users; reasoning controls pushed forward | Emerging market fact, page dated 30 October 2026, will move |
| Vendor example that reinforcement fine-tuning includes medical diagnosis | Experimental as advice; reject for this lesson |
| Agents only when the path is open-ended; workflows when it is not | Proven as vendor engineering guidance (Anthropic) |
| Patient-level and timing leakage are real; the metric gap is sometimes small | Proven (Davis et al.; Roberts et al.; Wilimitis and Walsh) |
| Seasonal naive and ETS-class models; holiday regression as a candidate; boosting as a candidate on calendar-driven counts | Proven methods; unproven on Al-Waha |
| LLM component not shown to help the three ablated time-series methods | Proven inside that paper's scope; Experimental as a universal ban |
| Targeted reminders can reduce no-shows; overbooking evidence is weak; overbook objectives can shift waiting onto a group | Proven (Oikonomidi; Samorani, other populations) |
| Non-device CDS must meet all four FDA criteria; a specific clinical directive fails | Proven US guidance; not KSA law |
| SFDA MDS-G010 covers AI that diagnoses, manages, or predicts disease | Proven KSA device guidance; intended use decides; this pack is not a ruling |
| WHO: humans remain in control of medical decisions | Proven ethics guidance |
| Mawid / Sehhaty is the national appointment layer; Epic and Oracle already serialize slot writes and did-not-show | Proven product facts; installation at any one cluster is unknown |
| This course's family floor | Proven courseware |

## Sources

Accessed 30 October 2026 unless noted. Prefer the primary URL if a search snippet and a fetched page disagree; the fetched page wins.

**Frameworks.** Martin Zinkevich, Rules of Machine Learning, `https://developers.google.com/machine-learning/guides/rules-of-ml`. Hamel Husain, "Is Fine-Tuning Still Valuable?", `https://hamel.dev/blog/posts/fine_tuning_valuable.html`, and "Is RAG dead?", `https://hamel.dev/blog/posts/evals-faq/is-rag-dead.html`. OpenAI, Optimizing LLM Accuracy, `https://developers.openai.com/api/docs/guides/optimizing-llm-accuracy`, and Model optimization, `https://developers.openai.com/api/docs/guides/model-optimization` (fine-tuning wind-down and the medical reinforcement example were on this page when fetched). Anthropic, Building Effective AI Agents, `https://www.anthropic.com/engineering/building-effective-agents`. Alan Turing Institute, small language models, `https://www.turing.ac.uk/blog/why-we-still-need-small-language-models-even-age-frontier-ai`. On-prem break-even preprint, `https://arxiv.org/html/2509.18101v2` (Experimental). Test-time scaling systems preprint, `https://arxiv.org/pdf/2509.19645` (Experimental).

**Leakage and reporting.** Davis, Matheny, Balu, Sendak, JAMIA, `https://pmc.ncbi.nlm.nih.gov/articles/PMC10746313/`. Wilimitis and Walsh, JMIR AI, 18 December 2023, `https://pmc.ncbi.nlm.nih.gov/articles/PMC11041453/`. Roberts and colleagues, Nature Machine Intelligence, 2021, `https://www.nature.com/articles/s42256-021-00307-0` (2,212 studies screened, 62 included, none judged of potential clinical use; patient-level partition recommendation). TRIPOD+AI, BMJ, 16 April 2024, `https://doi.org/10.1136/bmj-2023-078378`.

**Forecasting.** Hyndman and Athanasopoulos, Forecasting: Principles and Practice, toolbox, `https://otexts.robjhyndman.com/fpp2/toolbox.html`, and Prophet chapter, `https://otexts.com/fpptr/prophet.html`. Tan, Merrill, Gupta, Althoff, Hartvigsen, arXiv 2406.16964, `https://arxiv.org/abs/2406.16964` (NeurIPS 2024 proceedings PDF also seen: `https://proceedings.neurips.cc/paper_files/paper/2024/file/6ed5bf446f59e2c6646d23058c86424b-Paper-Conference.pdf`). Makridakis, Spiliotis, Assimakopoulos, International Journal of Forecasting 38 (2022), `https://doi.org/10.1016/j.ijforecast.2021.11.013`. DeLurgio and colleagues, 2009 PDF, `https://btdenton.engin.umich.edu/wp-content/uploads/sites/138/2015/08/DeLurgio-2009.pdf`.

**DNA.** Oikonomidi and colleagues, JAMIA, `https://pmc.ncbi.nlm.nih.gov/articles/PMC9933067/`. Samorani and colleagues, `https://doi.org/10.1287/msom.2021.0999`. Review abstract not re-audited from the publisher PDF: `https://doi.org/10.1016/j.ibmed.2025.100229`. Conference review, thinner extraction: `https://doi.org/10.1109/ictmod63116.2024.10878195`.

**Safety boundaries.** FDA CDS guidance, `https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software`, Federal Register notice, `https://www.federalregister.gov/documents/2022/09/28/2022-20993/clinical-decision-support-software-guidance-for-industry-and-food-and-drug-administration-staff`. SFDA MDS-G010, 29 November 2022, `https://www.sfda.gov.sa/sites/default/files/2023-01/MDS-G010ML.pdf`. WHO, 28 June 2021, `https://www.who.int/news/item/28-06-2021-who-issues-first-global-report-on-ai-in-health-and-six-guiding-principles-for-its-design-and-use`, report `https://www.who.int/publications/i/item/9789240029200`.

**Patient access systems.** MOH on Mawid, 10 September 2020, `https://www.moh.gov.sa/en/ministry/mediacenter/news/pages/news-2020-09-10-010.aspx`. MOH on Sehhaty merger, 26 January 2022, `https://www.moh.gov.sa/en/ministry/mediacenter/news/pages/news-2022-01-26-006.aspx`. Sehhaty booking, `https://www.moh.gov.sa/en/eservices/sehhaty/pages/appointment-booking-on-sehhaty.aspx`. Makkah e-health linkages, 6 February 2022, `https://www.moh.gov.sa/en/ministry/mediacenter/news/pages/news-2022-02-06-004.aspx` (one cluster's announcement, not a national HIS census). Epic Cadence training description, `https://epicsupport.sites.uiowa.edu/epic-resources/scheduling`. VA TRM entry, `https://www.oit.va.gov/Services/TRM/ToolPage.aspx?tid=10776`. Incoming scheduling, including did-not-show, `https://open.epic.com/Scheduling/HL7v2`. Oracle Health schedule appointment, `https://docs.oracle.com/en/industries/health/health-patient-administration/health-patient-admin-userguide/schedule-appointment1.html`.

**Course artifacts this research treated as primary for the fictional world.** `instructional/curriculum-understanding-map.md` Lesson 2. `course_design/module-01.md`. `course_design/slides/module-01-lesson-02.md`. `Module 01/Lesson 02` student chapters 00–08, templates, four baseline scripts, `prices.csv`, extracts, `problems.md`. Solution chapters 01 and 03–06. `problem_simulation/design/02-real-problems.md`. `alwaha/samples/gold.py`. `tests/test_m01_l02_checks.py`. Practice printout used in the evaluation: `row 0.7692`, `person 0.0000`, `keyword 0.3125`, `filled 5`, `seasonal 2.1667`, `mean 12.0324`.

## Five sources that most change the lesson

If an editor reads only five external pages before rewriting chapter 07, read these:

1. `https://developers.google.com/machine-learning/guides/rules-of-ml` — Rule 1 and Rule 4 are why `p-clock`, `p-slots`, and the four scripts exist.
2. `https://www.anthropic.com/engineering/building-effective-agents` — why an agent is the wrong default for a defined access workflow.
3. `https://arxiv.org/abs/2406.16964` — why `p-forecast` does not graduate from seasonal naive to a language model on the strength of a product demo.
4. `https://pmc.ncbi.nlm.nih.gov/articles/PMC9933067/` — why the DNA action is a reminder or a call, and why overbooking is not the success metric.
5. `https://www.sfda.gov.sa/sites/default/files/2023-01/MDS-G010ML.pdf` — why "the assistant sets urgency" is a device-shaped intention in the Kingdom, read next to `pol-stage-gate`, not instead of it.

The FDA CDS guidance and Davis and colleagues on leakage are the next two. Husain is the one to read before anyone deletes fine-tuning from the glossary.
