"""The machine-readable component list: every system of record plus the shared platform pieces."""

from __future__ import annotations

import pandas as pd

from simulation.systems.catalog import SYSTEMS
from simulation.world.staff import name

PROTOCOL = {
    "registry": "SFTP CSV monthly", "pacs": "HL7 v2 ORU plus study metadata CSV", "shared-folder": "SMB file share",
    "grader": "HL7 v2 ORU via integration engine", "letters": "SFTP CSV and JSON", "ophthalmology": "HL7 v2 REF pipe-delimited",
    "vendor": "HTTPS REST with callback webhook", "warehouse": "ODBC over SQLite", "booking": "HTTPS REST, FHIR R4 Appointment (partial)",
    "sms": "HTTPS REST with receipt webhook", "call-centre": "CSV export daily", "lab": "HL7 v2 ORU^R01", "camera-inventory": "XLSX by hand",
    "service-desk": "CSV export", "idp": "SAML 2.0 and OIDC, SCIM to booking only", "audit": "JSON lines over syslog",
    "finance": "CSV export annual", "complaints": "CSV export", "epr": "HL7 v2 MDM^T02 with text body",
}
DEPENDS = {
    "registry": (), "pacs": ("integration-engine",), "shared-folder": (), "grader": ("pacs", "shared-folder", "idp", "integration-engine"),
    "letters": ("grader", "registry"), "ophthalmology": ("integration-engine",), "vendor": ("vendor-callback",),
    "warehouse": ("registry",), "booking": ("integration-engine", "idp"), "sms": ("booking",), "call-centre": ("booking", "idp"),
    "lab": ("integration-engine",), "camera-inventory": (), "service-desk": ("idp",), "idp": (), "audit": ("idp",),
    "finance": ("idp",), "complaints": ("idp",), "epr": ("integration-engine",),
}
DR_TIER = {
    "booking": 1, "grader": 1, "idp": 1, "integration-engine": 1, "registry": 2, "letters": 2, "sms": 2, "pacs": 2,
    "ophthalmology": 2, "epr": 2, "lab": 2, "audit": 2, "vendor-callback": 2, "api-gateway": 1, "backup-vault": 1,
    "warehouse": 3, "call-centre": 3, "complaints": 3, "service-desk": 3, "finance": 3, "vendor": 3,
    "shared-folder": 4, "camera-inventory": 4,
}
TIERS = {1: "RTO 4 hours, RPO 15 minutes", 2: "RTO 24 hours, RPO 4 hours", 3: "RTO 72 hours, RPO 24 hours", 4: "Best effort, no backup"}
PLATFORM = (
    ("integration-engine", "Integration engine", "authority", "HL7 v2 MLLP; FHIR R4 Patient and Appointment only", ("idp",), "enterprise_architect"),
    ("api-gateway", "API gateway", "dmz", "HTTPS REST, OAuth client credentials", ("idp",), "enterprise_architect"),
    ("vendor-callback", "Vendor score callback endpoint", "dmz", "HTTPS webhook, shared secret", ("api-gateway", "integration-engine"),
     "enterprise_architect"),
    ("backup-vault", "Backup vault", "authority", "Nightly snapshot, immutable copy weekly", (), "security_officer"),
)


def components_frame() -> pd.DataFrame:
    rows = [_row(item["system_id"], item["name"], item["trust_zone"], PROTOCOL[item["system_id"]],
                 DEPENDS[item["system_id"]], item["owner"]) for item in SYSTEMS]
    rows += [_row(*item) for item in PLATFORM]
    return pd.DataFrame(rows).sort_values("component").reset_index(drop=True)


def _row(component: str, label: str, zone: str, protocol: str, depends: tuple[str, ...], owner: str) -> dict:
    return {"component": component, "name": label, "zone": zone, "protocol": protocol, "depends_on": ";".join(depends),
            "dr_tier": DR_TIER[component], "owner": name(owner)}


def zone_of(frame: pd.DataFrame, component: str) -> str:
    return str(frame.loc[frame["component"] == component, "zone"].iloc[0])


def callback_path() -> tuple[str, ...]:
    return ("vendor", "vendor-callback", "integration-engine", "grader")
