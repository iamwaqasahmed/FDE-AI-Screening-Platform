# 02 — Industry research

**Proven**: public specification and production use. **Emerging**: sound, but a one-day exact grader cannot own it. **Experimental**: wrong instrument here, or a privacy claim the cited evidence does not support. Claims are attributed. No fidelity score and no privacy guarantee is added.

## Splink (Proven software)

[Splink](https://moj-analytical-services.github.io/splink/index.html) (Ministry of Justice, Splink 5) links records with no unique person id. The [Fellegi–Sunter guide](https://moj-analytical-services.github.io/splink/topic_guides/theory/fellegi_sunter.html) uses lambda (prior match), m (agreement if a match), and u (agreement if not). Weight is log-odds of lambda plus log2(m/u), added across columns only under independence. Estimation can be unsupervised. The site's NHS England note is their claim, not an audit. Paper: Linacre et al., [IJPDS 2022](https://ijpds.org/article/view/1794).

Extra weight for a shared national id is the mother/newborn error. That field supports Iqama `replaces` and is barred for a newborn. Shared phone is the twin error. Shared MRN is the reuse error. Splink belongs on leftover pairs after those vetoes, not in place of graded `partition()`.

## Deterministic rules (Proven; this lab)

The reference module is entity resolution: national id links, except `newborn` and `twin`; `replaces` links Iqama to visitor; phone and MRN do not; the count is groups, not rows. The engineer implements this. It is not probabilistic linkage.

## Synthea (Proven generator; Experimental as privacy here)

The [MITRE overview](https://mitre.github.io/fhir-for-research/modules/synthea-overview) says modules use public statistics, no person's record enters a module, and the output is therefore unrestricted. That claim does not cover a fit on `clerk.jsonl`. Rarer conditions may be missing. [Keep modules](https://mitre.github.io/fhir-for-research/modules/synthea-customizing) miss impossible filters and then stop. [Recreation](https://github.com/synthetichealth/synthea/wiki/Recreating-a-Dataset) needs the same commit, seed, and dates; multithreading and time zone can change ids or timestamps. It is Java, US-census based, and not this label schema.

## Fidelity versus privacy, and differential privacy

Stadler, Oprisanu, and Troncoso, [USENIX Security 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/stadler), report that the generators they tested either failed to stop inference attacks or failed to keep utility, and that the privacy–utility tradeoff was hard to predict. Attribute disclosure means someone who already knows quasi-identifiers infers a withheld sensitive attribute. No attack steps and no rates are restated here. The lesson card only checks marginals on a 4–8 row hand sample.

[NIST SP 800-226](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-226.pdf) defines pure ε-differential privacy: neighboring datasets differ by one person; a randomized mechanism's outcome probabilities differ by at most e^ε. The guarantee is ε plus the neighbor definition. Smaller ε is stronger privacy and lower accuracy. Releases compose by adding ε. This lesson sets none of those ingredients. A card pass is not a differential-privacy claim.

## Two Hijri calendars (Proven)

Graded code is tabular. Saudi civil Hijri is Umm al-Qura. [hijridate](https://hijridate.readthedocs.io/en/stable/) covers 1343–1500 AH (1 August 1924–16 November 2077) from official calendars and KACST data, and is not for crescent sighting. ICU4X [`UmmAlQura`](https://unicode-org.github.io/icu4x/rustdoc/icu/calendar/cal/hijri/struct.UmmAlQura.html) uses KACST lengths for 1300–1600 AH and a tabular fallback outside, and may change if government tables change. Rows `1448-07-29` and `1448-08-01` sit in both ranges. No civil date is printed. Gold follows tabular arithmetic, so a correct Umm al-Qura day can fail the check. Name both calendars. Leave `dates.py` tabular until gold is regenerated on purpose.

## PDPL (duties only)

Primary: [PDPL English PDF](https://sdaia.gov.sa/en/SDAIA/about/Documents/PersonalDataProtectionLaw.pdf) (V2-23April2023) on sdaia.gov.sa. The Controller sets purpose and manner; the Processor acts for the Controller; Health Data is Sensitive Data. Article 5: consent for processing and for a new purpose, with listed exceptions and withdrawal. Article 10: collect from the person for the original purposes, with exceptions that include public health. Article 11: minimum necessary, then destroy when the purpose ends. Article 14: accuracy, completeness, timeliness, relevance. Article 15: disclosure only in listed cases, one of which is later processing that makes identification impossible. A fidelity card does not show that. Legitimate-interest disclosure excludes Sensitive Data, so it excludes health data. Article 19: safeguards, including in transfer. Article 20: notify the authority of a breach, and the person when harm or prejudice would follow. Article 22: an impact assessment. Article 23: tighter staff limits for health-data access and processing.

Secondary, not the statute: the SDAIA [controller guide](https://dgp.sdaia.gov.sa/wps/wcm/connect/f579bc32-fda8-47bd-bc6f-66b8cb77985c/ENG-Guide+to+the+saudi+PDP+law+for+controllersprocessors.pdf?MOD=AJPERES) notes extra sector rules, including healthcare. [Implementing Regulation](https://sdaia.gov.sa/en/SDAIA/about/Documents/ImplementingRegulationPersonalDataProtectionLaw.pdf) Article 32 lists officer appointments, including for core processing of sensitive data. Do not quiz the law or call Al-Waha compliant.

## Contracts, label versions, canaries

[ODCS v3.2.0](https://bitol-io.github.io/open-data-contract-standard/v3.2.0/) is versioned YAML with schema, quality checks, and tags; the [tags page](https://bitol-io.github.io/open-data-contract-standard/v3.2.0/tags/) gives `phi` as an example the organisation must define. [Confluent contracts](https://docs.confluent.io/cloud/current/sr/fundamentals/data-contracts.html) version schemas and can carry migration rules. The clinic rename is that pattern: `END-01` means `ENDO-CLN` only at `h-wadi` on or after June 2024. The [annotation rubric](https://datacuration.org/rubric/) ranks a versioned guideline above unilateral edits. `ann-v2` adds source type and a sub-specialty when the text names one. An `ann-v1` label is a different target. The SAR figure is a spend cap.

[Canarytokens](https://docs.canarytokens.org/guide/getting-started.html) are unique markers that can notify an owner when used. Silence is not proof of containment. The course scan returns false for `CANARY-` or a history national id. It detects that marker and those ids. It is not anonymisation. This lesson does not teach lures.
