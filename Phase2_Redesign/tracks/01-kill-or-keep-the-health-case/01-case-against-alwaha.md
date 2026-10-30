# The case against keeping Al-Waha

Al-Waha is a fictional health cluster: three hospitals, a diabetes and eye center, about twenty-four primary care centers, referrals, appointments, reminders, and a contact center. The engagement in the case opens on 10 January 2027. A clinician assigns clinical urgency. The assistant is forbidden to do that. Phase-1 enterprise research said to keep the narrative and thicken six frictions inside it. That was a coherent answer to a brief that wanted a better simulator. It is the wrong answer to a brief that wants AWS as an implementation track under the Personal Data Protection Law.

## The cloud the case already chose

The student-facing case names three places a system can run. Older hospital systems sit in hospital data centers and emit nightly files. The newer hospital system, the referral platform, and a small GPU quota sit on the cluster's private cloud, on two sites. That private cloud is where patient data may be processed, and it is the deployment target. A public-cloud model is limited to content the cluster has classed as public.

A student AWS account is a public-cloud tenant. It is not the cluster's private cloud. Treating LocalStack, or a diagram of two sites, as the AWS track keeps the logo and withholds the implementation: IAM, encryption keys, bucket policies, trails, budgets, and a workflow whose failure the student can see in a real account. Treating the real account as the private cloud moves referral and appointment content into a place the case has already limited to public-class content.

**Proven** as a reading of `case/README.md`. **Speculative** as the claim that no cohort arrangement (a contracted in-Kingdom landing zone, shared by the sponsor) will exist. This pack does not assume a sponsor-held government tenant. It assumes a laptop and an ordinary student account, because that is the constraint the brief states.

## Health data is a special regime, and a region launch does not close it

The Personal Data Protection Law defines Health Data as personal data related to a person's health condition or to health services received, and lists it inside Sensitive Data. Article 23 tells the regulations to add controls, including minimum access to medical files and minimum processing for health services or health-insurance programs. The Implementing Regulation's article on processing health data then points at controls from the Ministry of Health, the Saudi Health Council, the Saudi Central Bank, and the Council of Health Insurance, requires a record of who did each processing stage, and limits processing to the minimum necessary for care or insurance. The transfer regulation requires a risk assessment for continuous or large-scale transfer of Sensitive Data outside the Kingdom, and it says a high risk to privacy stops the transfer.

The English Implementing Regulation also says anonymized data is not personal data only once re-identification is impossible. A referral letter with the obvious names removed, still joinable to an appointment and a national identifier, fails that test. Calling it synthetic does not change the shape of the fields. Phase-1 already rejected a Massachusetts synthetic population for that reason. The same rejection applies to "de-identify, then call a public model."

AWS's own migration post of 15 October 2026 says the first Region in the Kingdom is on track for December 2026, that an in-country Region lets customers store and process data inside the Kingdom for healthcare, financial services, and government, and that location alone does not establish compliance. The customer still chooses where data sits, including backups and replicas. The same post says a new Region opens with a core set of services and adds more later, and that where prices are not published the estimate must name a reference Region and label the assumption. About Amazon's LEAP announcement repeats the December 2026 target, a planned investment of more than 5.3 billion US dollars, and says HUMAIN's ALLAM Arabic model will soon be available through Amazon Bedrock. "Will soon" is a roadmap.

**Proven:** the legal texts and the two AWS pages, as worded. **Emerging:** the Region date, until it is open, and ALLAM on Bedrock. **Speculative:** any claim that a particular service (Step Functions, Bedrock, a given instance type) will exist in that Region in January 2027. The course date sits weeks after the announced launch. A syllabus that requires those services on day one is betting on a launch checklist the vendor says to re-check.

National Cybersecurity Authority Cloud Cybersecurity Controls (CCC-2: 2024) apply to cloud tenants that are government agencies, including companies and sub-entities, and to private operators of critical national infrastructure. The 2024 update deleted the old localization lines and told entities to refer to the National Data Management Office before acting on localization. A classroom account is not that tenant decision.

## The classification policy does not rescue a shortcut

NDMO's data-classification policy (Arabic) sorts government data by impact. The illustrative list for **مقيد** (restricted) includes the individual's health file, identity attributes (name, address, national ID, phone, account numbers, licenses, biometrics), employee salaries, supplier contracts and their quotations, and bid submissions. **عام** (public) includes information already public, public-service information, and public announcements. The highest class in a mixed set wins. NCA's cloud controls use a different four-word scale (top secret, secret, confidential, public). Phase-1 already warned against merging the two vocabularies. This pack repeats that warning.

The useful fact is narrower. Under this policy's examples, a health file and a supplier quotation are the same illustrative tier. "It is not PHI, so the student bucket is fine" is false. What health uniquely adds is the PDPL health-data article and, where the model's intended use is medical, the device guidance below. What health lacks is a large public-class corpus at the center of the job. Opening hours and a clinic name can be public. The referral, the letter, and the reason for the visit are the work.

## The decision the course is proud of refusing is not the decision it ships

SDAIA's AI ethics principles say automated systems whose impact is irreversible, hard to reverse, or life-and-death need human oversight and a human final determination, and that AI systems should not be used for social scoring or mass surveillance. The same document asks whether the design can abort or intervene when the system leaves its intended behavior, and it tells builders to classify data before they protect it. The Implementing Regulation requires explicit consent when a decision is made solely by automated processing of personal data.

SFDA guidance MDS-G010 (version 1.0, version date 29 November 2022 on the PDF; the authority's guide page is dated 3 January 2023) applies to AI and machine-learning technologies that diagnose, manage, or predict disease from medical data. Intended use for investigation, detection, diagnosis, monitoring, treatment, or management of a condition puts the product under medical-device controls, including clinical evaluation. MDS-G027 (file dated August 2025) lists workflow optimization among healthcare uses and says AI software with a medical purpose is typically regulated as software as a medical device, with a defined role for human review.

The current course draws the right line: the assistant does not set clinical urgency. Phase-1's own FDE note then says a stop has to be available on a live option, not only on a trap the author has already labeled `p-triage`. The live option in Al-Waha is the front desk the chief digital officer asked for: book, reschedule, answer, chase referrals, before Ramadan. The prohibited decision is fenced off before the student arrives. Evaluation can still catch a bad citation or a stale hour. It does not practice the harder act, which is stopping a shipment the client wants, on a decision the client is pressuring the team to automate.

**Proven:** the principle text, the consent clause, the SFDA scope, and the phase-1 sentence about `p-triage`. **Speculative:** that a referral-chasing assistant will be pulled across the intended-use line in a long course. The pull is real enough to design against. It is not a finding that today's front desk is a medical device.

## One cluster is the wrong size of mess

The Health Holding Company says it was established on 2 June 2022 under Cabinet Resolution No. 469, dated 19/8/1443H, and that it provides care through twenty health clusters. The same about page says the company serves over 20 million people. That population sentence is the company's own wording, not a census this pack rechecked. Its model-of-care page describes the split the transformation is aiming at: the Ministry of Health regulates and supervises, the National Health Insurance Center funds, and the holding company owns and manages the clusters that deliver care.

On 26 January 2022 the Ministry of Health said it had merged Sehha, Tetamman, and Mawid into Sehhaty. The same notice describes Mawid as the central appointment system for primary care and for appointments at any referral hospital: book, cancel, reschedule. The national channel is a second writer on the slot.

The nphies implementation guide (financial services, edition 1) describes a single gateway between providers, insurers, and third-party administrators. In prose it says the gateway validates and does not adjudicate, does not determine fraud, and does not replace the payer's or the provider's system. A key-performance table on the same page includes "Authorization Adjudication within 30 minutes" at 96 percent, and the prose and the table do not share one count of providers or insurers (the prose says 6,600 providers and 28 insurers as of October 2025; the table says 6,419+ facilities and 25 insurers). This pack does not pick a winner among those figures and does not import them as Al-Waha volumes. The contradiction matters for teaching. A hybrid built on that page will not know whether the bus is a courier or an adjudicator, and students will follow the metric.

A thickened Al-Waha still inherits one delivery organization's mart, session book, and referral record. Discovery of who masters the slot, who pays, and who may write the national appointment is the actual forward-deployed question. The prior research already knew the national names and then kept them in advanced reading so the fictional cluster would not be accused of running a named product. That caution is right. The cost is a client whose integration mess has been simplified past the point where identity, a second writer, and a payer are structural.

## What "keep Al-Waha and add AWS" would fake

- A private cloud drawn as three AWS icons.
- Referral text, a national identifier, or a letter body in a student bucket or a public model, described as de-identified.
- A December 2026 Region, or the Bahrain Region, described as already an accredited host for this cluster.
- Bedrock answering a clinical or urgency question.
- ALLAM treated as available because a press page said "soon."
- A containment rate, a wait reduction, or a headcount copied from Sehhaty, nphies, or the holding company onto Al-Waha.
- A stop-shipment exercise whose only prohibited action was prohibited in the case preface.

## What still stands

Access work is real engineering: two systems that both accept a booking, a policy circular that is the wrong version, a bilingual notice, a surge before a calendar change, a cost sheet whose volumes are blank when they are unknown. Government employees meet Sehhaty as residents, so the domain is legible. The ban on automated clinical urgency matches SDAIA's life-and-death line and SFDA's intended-use line. Those are reasons to keep a clinic vignette. They are not reasons to keep the cluster as the twenty-lesson world once the implementation track has to be a real account and the data regime is the health-data one.

**Speculative:** many learners will not work in a cluster, so a health spine is a poor transfer. This pack has no employment statistic and does not invent one. The transfer argument is not the load-bearing one. The load-bearing one is the collision between the private-cloud deployment target, the health-data rules, and a serious public-cloud track.
