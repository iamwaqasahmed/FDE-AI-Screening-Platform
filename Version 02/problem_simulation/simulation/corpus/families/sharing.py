"""Data sharing agreements. One clause in the vendor agreement conflicts with the vendor pilot DPIA."""

from __future__ import annotations

from datetime import date

import numpy as np

from simulation.corpus.add import Extra, add_document
from simulation.world.staff import VENDORS, name

FAMILY = "data-sharing"
AUTHORITY = "Hartland Health Authority"

AGREEMENTS = (
    ("dsa-north-city-hospitals-2019", "North City hospitals", date(2019, 4, 1),
     ("Registry demographics and screening grades for people under the care of the hospital eye service.",
      "Purpose: screening and referral only.", "Retention: eight years after the last encounter.",
      "Images stay in the hospital zone; only study metadata is shared.")),
    ("dsa-east-city-hospitals-2019", "East City hospitals", date(2019, 4, 1),
     ("Registry demographics and screening grades for people under the care of the hospital eye service.",
      "Purpose: screening and referral only.", "Retention: eight years after the last encounter.",
      "Images stay in the hospital zone; only study metadata is shared.")),
    ("dsa-postright-2020", VENDORS["bureau"], date(2020, 1, 6),
     ("Name, address, and letter content for result and invitation letters.", "Purpose: printing and posting letters.",
      "Retention: ninety days after dispatch, then deletion with a certificate.", "Processing in a UK region only.")),
    ("dsa-hospital-lab-2021", "Hospital laboratory", date(2021, 4, 1),
     ("HbA1c results keyed by lab patient id.", "Purpose: risk-based screening intervals and evaluation.",
      "Retention: as for screening records.", "No onward sharing.")),
    ("dsa-retinalytics-2025", VENDORS["retinalytics"], date(2025, 3, 3),
     ("Screening photographs and grades, including hospital studies, for service improvement and model retraining.",
      "Purpose: triage support for the pilot and improvement of the supplier's products.",
      "Retention: twenty-four months in the supplier's EU region.",
      "The supplier may use de-identified images to train models offered to other customers.")),
)

CONFLICT = {
    "agreement": "dsa-retinalytics-2025",
    "agreement_clause": "Clause 1",
    "dpia": "dpia-vendor-2024",
    "dpia_clause": "vendor-receive",
    "summary": "The agreement shares hospital studies and allows retraining for other customers; the DPIA limits the vendor "
               "to primary-care photographs for the named pilot cohort.",
    "also": ["Clause 3 retention and EU region are not covered by the DPIA", "Clause 4 secondary use is not covered by the DPIA"],
}


def build(world: dict, rng: np.random.Generator) -> None:
    for doc_id, party, effective, clauses in AGREEMENTS:
        add_document(world, doc_id, FAMILY, f"Data sharing agreement: {AUTHORITY} and {party}",
                     _body(party, clauses), effective, extra=Extra(original="pdf", cites=("dpo-rule-2018",)))
    world["gold"]["dsa_conflict"] = CONFLICT


def _body(party: str, clauses: tuple[str, ...]) -> str:
    lines = ["## Parties", f"{AUTHORITY} and {party}.", "## Clauses"]
    lines += [f"Clause {number}. {text}" for number, text in enumerate(clauses, start=1)]
    lines += ["## Signatures", f"For the authority: {name('dpo')}, Data Protection Officer.",
              f"Approved by {name('cdo')}, Chief Digital Officer."]
    return "\n\n".join(lines)
