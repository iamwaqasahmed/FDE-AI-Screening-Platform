# 02 — Industry research

This file is overview-level. It maps official sources onto `rel-m04-l01`. It does not restate attack procedures from those sources. Scenario write-ups in the OWASP PDF are left in the PDF.

Al-Waha Health Cluster, `ext-large`, `zone-private`, `int-engine`, and stage gates G1 and G2 are fictional. They are teaching analogues. They are not citations of Saudi law. Official PDPL and NDMO/SDAIA statements below come from pages on `sdaia.gov.sa` and the Bureau of Experts law portal. English PDPL PDFs on SDAIA are translations; SDAIA's own regulation text says to refer to the Arabic for the original. This pack is not a legal opinion.

## OWASP Top 10 for LLM Applications, 2025 edition

The project site is [genai.owasp.org/llm-top-10](https://genai.owasp.org/llm-top-10/). The foundation project page points there as the latest list. The PDF "OWASP Top 10 for LLM Applications 2025" is version 2025, dated 18 November 2024, licensed CC BY-SA 4.0. Revision history in that PDF: 1.0 on 1 August 2023, 1.1 on 16 October 2023, 2025 on 18 November 2024. This research did not find a 2026 Top 10. The course design note `09-traffic-and-threats.md` already maps the library onto this edition. That mapping is right and should stay.

| Course id | OWASP 2025 | Defensive point the lesson can teach |
| --- | --- | --- |
| `atk-direct`, `atk-indirect` | LLM01 Prompt injection | Impact depends on agency. Segregate untrusted content. Do not give the model the privilege. |
| `atk-disclose`, and canaries | LLM02 Sensitive information disclosure | Least privilege on data. Do not put secrets in the prompt or the log. |
| `atk-supply` | LLM03 Supply chain | Only registered hashes load. Tool text is data. |
| `atk-poison` | LLM04 Data and model poisoning | A poisoned label drops. A clean label stays. |
| `atk-output` | LLM05 Improper output handling | Escape before the staff console renders. |
| `atk-agency` | LLM06 Excessive agency | Book and return wait for an approval the model does not mint. |
| `atk-prompt` | LLM07 System prompt leakage | The prompt is not a secret and not a control. The risk is the privilege behind it. |
| `atk-embed` | LLM08 Vector and embedding weaknesses | Permission-aware retrieval. An unauthorized circular is not a citation. |
| `atk-misinfo` | LLM09 Misinformation | The in-force document stays. Human oversight includes the rubber-stamp rate. |
| `atk-tokens`, `atk-hoard` | LLM10 Unbounded consumption | Per-session cap and expiring holds. |

LLM01's prevention section says prompt injection is possible because of how generative models work, and that it is unclear whether fool-proof prevention exists. The mitigations it lists that match this thesis are privilege control with the application's own tokens, least privilege, human approval for high-risk actions, and segregation of external content. Filtering and "instruct the model to ignore attempts to modify core instructions" are on the same list. They are mitigations. They are not the boundary. No numeric bypass rate is published in that section. This pack does not add one.

LLM06 and LLM07 say the same thing from the agency side. Critical controls — privilege separation, authorization bounds — must be enforced outside the model, in a deterministic and auditable way. If tasks need different access, use separate least-privilege capabilities rather than one agent that holds all of them. A system prompt that describes roles is not the authorization system. The course's approval queue is this control, in miniature. The course's family switch is not, until something other than the model decides the family.

LLM08's mitigations are permission and access control on the vector store, logical partitioning, validation of knowledge sources, classification tags, and monitoring of retrieval. The monitoring bullet asks for detailed logs. That collides with LLM02 and with erasure. The design resolution is in the deletion section below: log document ids and allow/deny decisions, not passage text and not national ids. The course checklist item `no-phi-in-logs` is the same resolution.

LLM09's mitigations include retrieval from trusted sources, human oversight, and telling users the limits. The course already refuses a superseded circular. The rubber-stamp rate is the oversight measure. OWASP does not claim fine-tuning removes misinformation. The lesson should not claim it either. LLM10 expands the old denial-of-service entry to resource and cost. The 800-token cap and the hold expiry are the lab's concrete controls. They are policy choices of the pack, not a measured capacity plan. Capacity is Lesson 3.

## NIST AI RMF 1.0 and the Generative AI Profile

AI RMF 1.0 is NIST AI 100-1, January 2023, [NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1). It is voluntary. Its core is four functions: Govern, Map, Measure, Manage. Profiles implement the functions for a setting. The framework defines current and target profiles and asks organizations to close the gap. It does not prescribe a template.

The Generative AI Profile is NIST AI 600-1, published 26 July 2024, [NIST.AI.600-1](https://doi.org/10.6028/NIST.AI.600-1). NIST's publication page describes it as a cross-sectoral companion to AI RMF 1.0. As fetched on 30 October 2026, the NIST AI RMF site says AI RMF 1.0 is being revised, and that the Playbook will be updated after that revision. Cite 1.0 and 600-1 as the published documents. Do not cite a draft revision this pack has not read.

600-1 groups generative-AI risks in a way a DPIA can reuse without copying the whole catalog. The risks that touch this lesson are information security (it describes direct and indirect prompt injection in prose), data privacy, confabulation, harmful bias and homogenization, and value-chain and component integration (third-party weights and data). Suggested action GV-1.2-002 is to evaluate risk-relevant capabilities and the robustness of safety measures before deployment and on an ongoing basis. That is the red-team requirement stated as governance, not as a jailbreak lab. GV-1.1-001 aligns use with applicable privacy law. Measure is where fairness slices belong: the profile treats harmful bias as something to measure in context, not as a filter you switch on.

For the course, G1 is the risk-tier gate and G2 is the DPIA gate. NIST's language is Govern (who is accountable, what the risk tolerance is) then Map (this assistant books and answers, it does not triage) then Measure (hidden set, disparity, stamp rate, canary scan) then Manage (approval queue, deletion, breach clock). The lesson currently does a thin Map and a thin Govern, and a stronger Measure on the attack families than on the privacy design. A DPIA that changes a token is Manage. Triage stays blocked from earlier modules. This lesson does not become a biosecurity unit. 600-1 discusses several misuse classes, including chemical, biological, radiological, and nuclear information, and this day does not teach them.

## ISO/IEC 42001 at overview level

[ISO/IEC 42001:2023](https://www.iso.org/standard/42001) is the management-system standard for organizations that provide or use AI. ISO's explainer describes an AI management system as policies, processes, and controls across the lifecycle: context and leadership, risk assessment and treatment, data and lifecycle, transparency, performance evaluation, internal audit, and continual improvement. Certification is voluntary and is done by certification bodies, not by ISO. The standard does not replace law.

The text is paywalled. This pack does not invent clause numbers. Fit to the fictional stage gates, at overview level only: G1 is the risk tier and policy, G2 is the impact assessment that can change processing, the gateway and the register and deletion are the treatment the organization then has to operate, and the four checks plus the disparity table are performance evaluation when the hash or the corpus changes. ISO's management system and the PDPL impact assessment are different instruments. A one-day lab is not a certification exercise, and 42001 does not specify index compaction.

## Instruction hierarchy

The OpenAI Model Spec dated 29 October 2026, [model-spec.openai.com/2026-10-29](https://model-spec.openai.com/2026-10-29.html), assigns authority in this order: Root, System, Developer, User, Guideline, and then no authority by default. Assistant messages, tool messages, and quoted or untrusted text have only the authority an applicable instruction delegates. The developer documentation on prompt engineering states the same product rule in shorter form: developer messages outrank user messages. This is a vendor specification for one provider's models. It is Emerging as a model property. It is not a control you can buy by writing a longer system prompt.

Read beside OWASP LLM07. A referral letter, a tool card, and a retrieved circular are untrusted data. They do not outrank the booking policy. A model instructed to treat them as data will still sometimes fail. The gateway must not depend on that success: the letter is data, and the book capability is absent from the model's token set. Cite the Model Spec as a vendor spec, paired with OWASP, not as a standard.

## Saudi PDPL and NDMO/SDAIA — official pages only

Primary pages used:

- Personal Data Protection Law, English PDF hosted by SDAIA: [PersonalDataProtectionLaw.pdf](https://sdaia.gov.sa/en/SDAIA/about/Documents/PersonalDataProtectionLaw.pdf). Royal Decree M/19, amended by M/148. Arabic original: [Bureau of Experts](https://laws.boe.gov.sa/BoeLaws/Laws/LawDetails/b7cfae89-828e-4994-b167-adaa00e37188/1).
- Implementing Regulation, English PDF: [ImplementingRegulation.pdf](https://sdaia.gov.sa/en/SDAIA/about/Documents/ImplementingRegulation.pdf). The file states it is a translation and the Arabic prevails.
- SDAIA laws and regulations index, which links the PDPL, the implementing regulation, data classification, and destruction guidance: [RegulationsAndPolicies](https://sdaia.gov.sa/en/SDAIA/about/Pages/RegulationsAndPolicies.aspx).
- Personal Data Destruction, Anonymization, and Pseudonymisation Guideline: [SDAIA PDF](https://sdaia.gov.sa/Documents/PersonalDataDestructionAnonymizationAndEncryptionGuideline.pdf).
- National data classification policy (NDMO policy document hosted by SDAIA), including least privilege and disposal: [Data Classification Policy PDF](https://sdaia.gov.sa/ar/SDAIA/about/Documents/Data%20Classification%20Policy.pdf).

Articles that this lesson touches, from the English translation: Article 1 defines processing to include indexing, retrieving, and destroying, and defines destruction as making data unreadable and irretrievable or impossible to identify to the subject. Sensitive data includes health data. Article 4 gives access and a right to request destruction when the data is no longer needed, subject to Article 18, which requires destruction without undue delay unless a legal period or a judicial case requires retention. Article 20 requires notice of a breach to the authority and, where rights are prejudiced, to the subject. Article 22 requires an impact assessment as the regulations specify. Article 23 limits health-data access to the minimum staff needed for the service. Article 29 permits transfer outside the Kingdom only for listed purposes, with equivalent protection, and only the minimum data, with a necessity exception for preventing, examining, or treating disease. The course ban on `ext-large` is a stricter fictional client rule. Do not teach it as Article 29.

Implementing Regulation Article 24 starts the 72 hours when the controller becomes aware, if the incident may harm the data or the subject or conflict with their rights. The notice includes that awareness time, categories, risks, measures, and whether the subject was told. Incomplete notices are finished as soon as possible with reasons. Subject notice is without undue delay, in clear language. National Cybersecurity Authority reporting is additional. In the case, the PHI-in-logs notice is the awareness record, so its timestamp is the awareness time. A later meeting does not restart the clock. The statute does not start at an arbitrary file drop with no awareness finding. The DPIA should say both.

Article 25 of the regulation requires a written assessment for cases that include sensitive data, new technologies, and automated decisions. Contents include purpose and legal basis, scope, necessity and proportionality of minimization, impact, and measures. If processing will harm privacy, the controller addresses the reasons and assesses again. The course's five headings (purpose, residency, tier, stores, clock) omit legal basis, proportionality, and a measure changed because a harm was found. That is the gap file 03 closes. The five headings are not Article 25.

The destruction guideline requires permanent, irrevocable deletion so data are inaccessible, unrecoverable, and unidentifiable. Backups and archives are not destruction; they remain personal data. Other recipients are asked to destroy copies. Anonymization must be irreversible; pseudonymized data remains personal data. The classification policy uses least privilege and ends access when the staff relationship ends, which is the stale-grant control. A disposal log that still contains the personal data fails the guideline. Wiping every patient's logs to redact one person is not a disposal log. The lesson needs these points, not a tour of the full NDMO standards catalog.

## Deletion in vector stores and logs

Design problem, not an exploit note.

An embedding is derived data. Deleting the source row leaves the vector searchable if the index was built from it. The course trap is this fact at application level: the index is a store, and `person_id` must match there too. That is necessary and not sufficient.

Approximate nearest-neighbor indexes, including common HNSW implementations, often mark a vector deleted and keep the node so the graph stays connected until compaction or rebuild. The preprint "Ghost Vectors" ([arxiv.org/html/2606.18497](https://arxiv.org/html/2606.18497)) reports that soft-deleted embeddings remained recoverable from raw index files in the authors' setup. On a Wikipedia biographies set they report 25.5% exact person-name recovery and 46.4% geographic-location recovery. On NIH Synthea records they report 100% recovery of age and gender markers. On image embeddings they report 100% tissue classification and 99% top-1 facial identity recovery. Their epoch-key-rotation construction (encrypt, then discard the key) reduced observed recovery of those fields to 0% in their experiments, about 2.5 ms for 500 vectors in that setup. Those figures are theirs, on those sets, for an adversary who can read the index files. They are not an Al-Waha rate and not a lab procedure. The qualitative lesson is enough: a delete flag is not destruction. Epoch-key rotation is Experimental and stays a paragraph, not a coding task.

Other copies the application filter does not see: replicas, snapshots taken before the delete, incremental backups, write-ahead logs, embedding caches, and retrieval logs that stored the top passages. The SDAIA guideline already says backups are not destruction. Vendor features that delete by id prefix remove vectors from that product's retrieval path. They are a useful keying practice (every chunk carries the subject id). They are not, by themselves, proof of storage erasure.

The design the lesson should teach:

1. Minimize. Do not embed raw national ids. Do not log passage text. The canary scan is how you notice you failed.
2. Key. Every derived artifact carries the subject id or it is not allowed into the index.
3. Delete on the read path. The export lists the stores. A follow-up read by that id returns empty.
4. Erase at rest on a schedule the DPIA names: compaction or rebuild, and crypto-erasure of backup keys where the backup cannot be edited. The lab can require the student to name the step. It cannot run a real compaction.
5. Keep a disposal record that contains the request id, the stores, and the time, and does not contain the personal data.

Logging for LLM08 monitoring and logging for erasure are the same design if the log is content-free. They conflict if the log is a transcript.

## Fairness slices: DNA, language, facility

Measurement only. No debiasing recipe.

Obermeyer, Powers, Vogeli, and Mullainathan, Science, 2019, [doi:10.1126/science.aax2342](https://www.science.org/doi/10.1126/science.aax2342), studied a widely used United States health-system algorithm. At a given risk score, Black patients were sicker than White patients. The authors' abstract states that remedying the disparity would raise the percentage of Black patients receiving additional help from 17.7% to 46.5%. The mechanism they identify is the label: the model predicted cost, and unequal access meant less was spent on Black patients who had the same need, so cost was a biased proxy for illness. Reformulating away from the cost proxy is what removed that bias in their analysis. The number is theirs, for that algorithm. It is not a rate for Saudi districts, insurance classes, or DNA.

The lesson for Al-Waha is the label, not the demographic. The course fair table measures yes-rate by district and insurance class. Those slices can show a disparity. They do not say whether "yes" means "a slot was clinically appropriate," "a slot was free," or "the patient generates cost." Insurance class can behave like the cost proxy. A gap inside the pack bound can still be the wrong label.

DNA (did not attend) is an operational model the course already classified as classical ML, not as a chatbot task. A DNA label confounds need with friction: transport, language of the reminder, clinic hours, and prior non-attendance that itself came from those frictions. Slicing false alarms and missed attendances by language and by facility tells you whether the model is a reminder-priority tool or a penalty on the clinics and languages that already face access barriers. This pack did not retrieve a Saudi national DNA fairness statistic and does not invent one. The exercise is to compute the slices on a planted file and write what the label is. Removing the language column and reprinting a higher overall accuracy is not a result the rubric accepts.

A facility gap is often the roster: no evening clinic means fewer evening bookings. Record it and do not drop the facility column to shrink the number. A language gap in a reminder is a product defect even when the facility slice is explained. NIST's harmful-bias risk is the umbrella: disaggregated performance, label written down, bound kept as a tripwire.

Rubber-stamp rate is an oversight measure, not a fairness slice. A high rate means coordinators are approving what the model already did, which is excessive agency with a human signature. Report it beside the disparity table. Do not average it into the gap.

## What this research refuses to claim

- A percentage of injections that bypass a named product filter.
- That ISO/IEC 42001 certification makes the assistant safe.
- That the course DPIA complies with PDPL Article 22 or Regulation Article 25.
- That the four-store `drop` meets the destruction guideline.
- That matching Obermeyer's percentages, or inverting them, is a target for `d-nakhl` and `d-rim`.
- That instruction hierarchy in one vendor's spec is a completed control.
- A debiasing method that guarantees equal yes-rates without changing the label or the service.
