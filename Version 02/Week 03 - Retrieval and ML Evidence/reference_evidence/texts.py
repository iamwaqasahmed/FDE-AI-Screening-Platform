"""The contract, the retrieval card, and the evidence note. The checker looks for facts, not headings."""

from __future__ import annotations

import yaml

from simulation.eval.evidence.text import FIELDS


def contract(found: dict) -> str:
    drop = found["drop_restriction"]
    payload = {
        "feed": "vendor_extract",
        "system": "vendor retrospective",
        "zone": "authority",
        "grain": "one scored capture",
        "keys": ["capture_ref", "person_key"],
        "columns": ["capture_ref", "site", "capture_date", "person_key", "vendor_score", "vendor_label"],
        "dates": ["capture_date"],
        "known_defects": ["file name carries a surname", f"{drop['banned_field']} must not cross"],
        "owner": "data protection officer",
        "consumers": ["vendor"],
        "fails_when": "A silent drop of a capture or a column is a failure.",
        "allowed_sites": drop["allowed_sites"],
        "banned_fields": [drop["banned_field"]],
        "crosses_to": (
            f"person_key, not {drop['banned_field']}. {drop['replacement_field']} is not required. "
            "The file name does not cross."
        ),
    }
    missing = [field for field in FIELDS if field not in payload]
    if missing:
        raise ValueError(missing)
    return yaml.safe_dump(payload, sort_keys=False)


def card(found: dict, keyword_percent: int, tfidf_percent: int) -> str:
    originals, duplicates = found["originals"], found["near_duplicates"]
    return "\n".join([
        "# Retrieval card",
        "",
        "## Loss table",
        "keyword and tf-idf both miss a draft, a superseded document, the wrong site, a table that is only in the original, and a forwarded copy.",
        f"keyword {keyword_percent}",
        f"tf-idf {tfidf_percent}",
        "",
        "## What changed the slices",
        "Filtering on status and effective date moves the binding slice. Reading the PDF and spreadsheet originals moves the table slice. Citing the original record rather than the forwarded copy moves the duplicate slice.",
        "",
        "## Not covered",
        "Graph retrieval is not covered. A dense embedding was not needed for a slice the baselines already lost.",
        "",
        f"Original PDFs: {originals['pdf']}. Forwarded copies: {duplicates['count']}.",
    ])


def note(found: dict) -> str:
    drop, scope = found["drop_restriction"], found["vendor_scope"]
    gap, dna, overdue = found["reference_gap"], found["dna_leak"], found["overdue_pilot_scope"]
    removed = ", ".join(drop["removed_sites"])
    return "\n".join([
        "# Evidence note",
        "",
        "## What changed",
        f"On {drop['effective']} the vendor pathway was limited to {', '.join(drop['allowed_sites'])}. {removed} was removed.",
        "",
        "## Which outputs changed",
        "C-03, C-05, and C-08 change. The Week 2 vendor cohort and its split have to be rerun. The identity clusters do not.",
        "",
        "## The index",
        "Answers cite the document whose status is in force on the date, and they cite the original record rather than a forwarded copy.",
        "",
        "## The vendor on its cohort",
        f"{scope['captures']} captures remain, of which {scope['adjudicated']} were adjudicated. "
        f"Against the adjudicated label the sensitivity is {gap['adjudicated']}. The routine grade is not the reference.",
        "",
        "## The claims",
        "The 0.95 claim does not hold for the adjudicated cohort. It is the figure for under 75 and good quality, and that population is in the PDF table. "
        "ClearSight was stopped. The post-mortem blames accuracy. The pilot stays stopped until a safety owner is named.",
        "",
        "## The did-not-attend number",
        f"The leaky column is {dna['leaky_feature']}. A random split reaches {dna['random_auc']:.2f}. "
        f"The honest split reaches {dna['honest_auc']:.2f}.",
        "",
        "## Decisions a person owns",
        "Whether the EU region in the vendor agreement stands needs a decision from the data protection officer. "
        "The file name carries a surname, so it does not cross. DOB stays inside the authority zone. YEAR_OF_BIRTH is the replacement if a year is required. "
        "The safety owner is still unnamed.",
        "",
        "## Two conversations",
        f"To the Chief Digital Officer: the cohort is {scope['captures']} captures and the headline does not hold. The pilot stays stopped. "
        f"To the Data Protection Officer: {removed} left the extract, DOB does not cross, and the pilot-scope overdue count is an upper bound of {overdue['upper_bound']}.",
    ])
