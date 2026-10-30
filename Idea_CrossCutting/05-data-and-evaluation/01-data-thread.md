# The data thread

A self-paced reader meets identity, Hijri dates, label versions, and the fidelity card on Module 3 Lesson 1, then does not return to them as data problems. The later retrieval lesson treats documents as an index. The evaluation lessons treat failures as model faults. For this assistant, most of those faults are data faults that a model then repeats.

Teach one data contract, and make every later lesson read it.

## Person grain before any score

The waitlist, the DNA table, and the warehouse are wrong when two rows of one person count twice, and wrong in a different way when a mother and a newborn collapse. Module 1 already plants the first version of this: a row split looks stronger because the same person sits on both sides. Module 3 Lesson 1 should feel like the measurement of that earlier trap, with gold clusters at a point in time (`chk-m03-l01-identity`).

Splink is the method to teach, and it is a linker. The Ministry of Justice library scores pairs that lack a unique person id, using a Fellegi-Sunter model, then clusters them into an estimated person id. The documented parameters are λ (how often two random records match), m (how often a field agrees when the records are the same person: a data-quality number), and u (how often a field agrees when they are not: a coincidence number). Match weights add only because the model assumes comparisons are independent. The project states that it works best with several columns that are not highly correlated, and that it is the wrong tool for one bag-of-words column. Term-frequency adjustments exist because a common city is weak evidence. Training can be unsupervised; labels make m and u more accurate. Blocking decides which pairs are even scored. The quickstart's `fake_1000` set and its 0.95 cluster threshold are demo settings.

What the course should make the reader compute, on the cluster's rows:

- Normalize Hijri and Gregorian birthdates to one civil date before comparison and before blocking. Splink's documented date-of-birth comparison is an ordinary date comparison. A Hijri string and a Gregorian string for the same birth never enter the same block, so the true pair is invisible and the match weight never sees the disagreement.
- Treat a shared household phone, address, and surname as correlated evidence. The independence assumption will stack them. A mother and a newborn are the drill: those fields agree, the birthdates do not, and the relationship edge is not an identity link. If the birthdate comparison is null because one source stored only a Hijri value, the household fields can carry the match.
- Use term frequency for common Arabic given names and for a clinic switchboard number. An exact match on a very common name is weak; the docs' city example is the same idea.
- Report cluster precision and recall against point-in-time gold. An estimated person id is a prediction. It is not the MRN.

## Time, codes, and labels are the same kind of object

A fact in this cluster has an effective window. That applies to clinic codes, criteria (`crit-endo-v3` against v4 for three specialties only), hours circulars, and annotation guidelines (`ann-v1` against `ann-v2`).

The reader should keep the code and the criteria version that were in force when the referral was submitted, and use a crosswalk only when the question is about the current catalog. A join to the latest clinic row changes specialty, SLA, and which circular may be cited. That is the same point-in-time rule as the DNA feature join, which must not see `appointment_status_final` or a later address.

Labels are versioned data, not a column the model owns. Clerks labeled under `ann-v1`. Training on those labels after `ann-v2` is the Lesson 1 trap. The adjudicated slice, the label budget, and active learning (`slice-active`) belong next to the guideline id. Agreement is reported against `ann-v2`, on the held-out slice, at person grain after the cluster step. A duplicate person who was labeled twice under two MRNs will inflate agreement if the split is by row.

## Documents, the mart, and the channels

The policy corpus is already specified as data: `doc_id`, status (`draft`, `in_force`, `superseded`, `unauthorized`), effective and sunset times, site, audience, `supersedes`, and `content_hash`. Module 3 Lesson 3 should teach that table before it teaches embeddings. Hybrid search, ACL, and version binding are queries over it. `circ-ramadan-unauth` is an unauthorized object mis-filed as public. A staff leaflet is a different audience from a patient leaflet. In-flight referrals keep the criteria version they started on.

Add three operational shapes the current document generator does not, by itself, force the reader to join:

- Bilingual clauses. One `clause_id`, Arabic and English bodies, and a translation that can lag the source. Gold for a patient-facing answer is the in-force clause, the asker's language, and the audience. A high retrieval score on the other language is a miss.
- The mart as a delayed aggregate. The booking system is the system of record. The warehouse wait number has an as-of time and a grain. After a cancellation, or after two MRNs are recognized as one person, the mart can still show the old count. Module 2 already tells the reader to distrust that number. The data thread should store the snapshot, the as-of, and the grain so the distrust is a join, not a slogan.
- Channel templates. One reminder intent, four legal bodies: SMS, WhatsApp inside the session window, the phone-only script, and the short caregiver wording (`status-short`, `caregiver`). The template id, channel, and session-window rule are columns. A single message-quality score hides a body that was legal on one channel and illegal on another.

## How the four failure types sit on this contract

| Planted type | First place the data thread makes it visible |
| --- | --- |
| Workflow | Two MRNs, a missed idempotency key, a Friday counted as a working day, a mother merged with a newborn, a handoff with no summary |
| Retrieval | Wrong status, wrong audience, wrong language, superseded or unauthorized circular, criteria version other than the one the referral started on |
| Reasoning | A constraint set (date, hours, gender preference, travel) resolved against a stale code or a Hijri value that was never converted |
| Hallucination | An answer whose claims are not in the cited span. Faithfulness to whatever text was retrieved is a different number, and it is taught in the eval thread |

The synthetic sample, the fidelity card, and the canary scan stay on Lesson 1, and the card should list these invariants. Distributional similarity to a clinical record is the wrong card for an access assistant. The design of that corpus is in `03-simulated-corpora.md`.
