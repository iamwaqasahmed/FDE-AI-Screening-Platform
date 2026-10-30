# 05 — Tradeoffs, recommendations, sources

## Alternatives

| Path | Maturity | Self-paced FDE |
| --- | --- | --- |
| A. Deterministic rules with hard non-links (current `partition`) | Proven | **Implement.** Graded identity. Mother, twin, reuse, and Iqama are exact. |
| B. Splink / Fellegi–Sunter on residual pairs, human review in the middle | Proven software; Emerging as a one-day exact lab | **Sketch the vetoes.** Do not install it for the finish check. EM on this tiny file will not yield a stable threshold, and a shared national id is not automatically a match. |
| C. Synthea-style simulation from public statistics | Proven for US teaching EHRs; Experimental as this sample or as a privacy control | **Name the claim and the limits.** The MITRE "no person's record in the module" claim does not cover a model fit on clerk letters. Stadler et al. show that "synthetic" is not itself a privacy property. |
| D. Differential privacy on a published aggregate | Proven definition; Experimental to code and certify here | **Name NIST.** The card has no ε and no neighbor. Hand rows that hit the card stay the graded sample. |

Copying clerk letters and stripping obvious ids is the shell. It fails the card, the watermark, and the id check. It is not a fifth recommendation.

## Tradeoffs

A is gradable and misses a duplicate that has neither a shared national id nor `replaces`. B can find that duplicate and will false-merge unless the newborn, twin, and reused-MRN vetoes run first. C teaches another population on another stack. D is the only privacy definition here; it spends accuracy and is the wrong tool for four rare-class rows. Ship A, the hand sample, and the string scan. Name D so the card is not read as D.

Pinning `ann-v2` matches the clinic rename: the old value is legal input and the wrong current meaning. Tabular Hijri matches gold. Umm al-Qura can be the civil date and still fail that gold. Ship tabular and name the other calendar.

## Deletions

- Remove the hardness-table claims of precision/recall against point-in-time gold, and of train-on-synthetic test-on-real, unless those tests are built. What runs is exact groups, label fields, card bands, and the marker/id scan.
- Remove any line that treats a card pass or a refusing scan as anonymisation or as a PDPL disclosure basis.
- Remove graded Splink, Synthea, hijridate, and any student-chosen ε.
- Remove `ann-v1` fields as training targets. Letter text may stay as input.
- Remove automatic links on phone, MRN, or every shared national id (the shell).
- Keep the demo, the three checks, the paste chapters, `pit.py`, and `budget.py`. The last two stay after a green finish.

## Recommendation

Ship A, the `ann-v2` pin, the hand sample, and the string canary. Teach B, C, and D as the map around that work. Correct the design sentence on the next documentation edit. Leave Python gold unchanged until a deliberate calendar or metric change regenerates it.

## Sources

- Splink: https://moj-analytical-services.github.io/splink/index.html
- Fellegi–Sunter: https://moj-analytical-services.github.io/splink/topic_guides/theory/fellegi_sunter.html
- Splink paper: https://ijpds.org/article/view/1794
- Synthea overview: https://mitre.github.io/fhir-for-research/modules/synthea-overview
- Synthea Keep modules: https://mitre.github.io/fhir-for-research/modules/synthea-customizing
- Synthea reproducibility: https://github.com/synthetichealth/synthea/wiki/Recreating-a-Dataset
- hijridate: https://hijridate.readthedocs.io/en/stable/
- ICU4X Umm al-Qura: https://unicode-org.github.io/icu4x/rustdoc/icu/calendar/cal/hijri/struct.UmmAlQura.html
- PDPL (primary): https://sdaia.gov.sa/en/SDAIA/about/Documents/PersonalDataProtectionLaw.pdf
- PDPL guide (secondary): https://dgp.sdaia.gov.sa/wps/wcm/connect/f579bc32-fda8-47bd-bc6f-66b8cb77985c/ENG-Guide+to+the+saudi+PDP+law+for+controllersprocessors.pdf?MOD=AJPERES
- Implementing Regulation: https://sdaia.gov.sa/en/SDAIA/about/Documents/ImplementingRegulationPersonalDataProtectionLaw.pdf
- NIST SP 800-226: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-226.pdf
- Stadler, Oprisanu, Troncoso 2022: https://www.usenix.org/conference/usenixsecurity22/presentation/stadler
- ODCS v3.2.0: https://bitol-io.github.io/open-data-contract-standard/v3.2.0/
- ODCS tags: https://bitol-io.github.io/open-data-contract-standard/v3.2.0/tags/
- Confluent data contracts: https://docs.confluent.io/cloud/current/sr/fundamentals/data-contracts.html
- Annotation versioning rubric: https://datacuration.org/rubric/
- Canarytokens: https://docs.canarytokens.org/guide/getting-started.html
