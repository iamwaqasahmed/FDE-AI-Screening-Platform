"""Architecture invariants: components cover the catalogue, one public-only model, stale catalogue entries, traceable threats."""

from __future__ import annotations

from simulation.architecture.ea_document import DOC_ID
from simulation.systems.catalog import SYSTEMS
from simulation.world.clock import LAB_UNIT_CHANGE
from simulation.world.timeline import TIMELINE

FOLDER = "handover/architecture"


def check_architecture(world: dict, errors: list[str]) -> None:
    files = world["files"]
    components = files[f"{FOLDER}/components.csv"]
    if not {item["system_id"] for item in SYSTEMS} <= set(components["component"]):
        errors.append("Component list misses a catalogue system.")
    register = files[f"{FOLDER}/model_register.csv"]
    if (register["approved_classifications"] == "public").sum() != 1:
        errors.append("Model register does not have exactly one public-only model.")
    _catalogue(files, errors)
    _threats(world, components, errors)
    meta = world.get("corpus_meta", {}).get(DOC_ID, {})
    if meta.get("family") != "architecture" or not meta.get("original", "").endswith(".docx"):
        errors.append("EA current-state document is not in the corpus with a DOCX original.")


def _catalogue(files: dict, errors: list[str]) -> None:
    catalogue = files[f"{FOLDER}/data_catalogue.csv"]
    stale = files["truth/architecture/catalogue_stale.csv"]
    keys = set(zip(catalogue["dataset"], catalogue["column"]))
    if not set(zip(stale["dataset"], stale["column"])) <= keys:
        errors.append("A stale catalogue entry is not in the catalogue.")
    lab = catalogue[(catalogue["dataset"] == "lab_hba1c") & (catalogue["column"] == "value")].iloc[0]
    if lab["last_reviewed"] >= LAB_UNIT_CHANGE.isoformat() or "percent" not in lab["definition"]:
        errors.append("The lab value entry was updated after the 2021 definition change.")


def _threats(world: dict, components, errors: list[str]) -> None:
    threats = {item["threat_id"]: item for item in world["gold"].get("threats", [])}
    if set(threats) != {"T1", "T2", "T3", "T4"}:
        errors.append(f"Threat gold is {sorted(threats)}")
        return
    if len(set(threats["T1"]["zones"])) < 3 or not set(threats["T1"]["components"]) <= set(components["component"]):
        errors.append("The vendor callback threat does not cross zones through known components.")
    roles = world["files"]["handover/identity/role_mappings.csv"]
    held = roles[(roles["account_id"] == threats["T2"]["account_id"]) & (roles["revoked_at"] == "")]
    if threats["T2"]["excess_role"] not in set(held["role"]):
        errors.append("The service account does not hold its excess role.")
    refs = {item.ref for item in TIMELINE}
    if not set(threats["T3"]["refs"] + threats["T4"]["refs"]) <= refs:
        errors.append("A threat cites a reference outside the timeline.")
    stale = {item["account_id"] for item in world["gold"].get("stale_access", [])}
    if set(threats["T4"]["accounts"]) != stale:
        errors.append("The stale-access threat does not list the stale accounts.")
