"""Write the architecture handover: EA document, component list, model register, catalogue, lineage, and threat gold."""

from __future__ import annotations

from simulation.architecture.catalogue import catalogue_frame, stale_frame
from simulation.architecture.components import components_frame
from simulation.architecture.ea_document import add_ea_document
from simulation.architecture.lineage import lineage_frame
from simulation.architecture.model_register import model_register
from simulation.architecture.threats import threats

FOLDER = "handover/architecture"


def build_architecture(world: dict, identity: dict) -> None:
    files = world["files"]
    components = components_frame()
    register = model_register()
    files[f"{FOLDER}/components.csv"] = components
    files[f"{FOLDER}/model_register.csv"] = register
    files[f"{FOLDER}/data_catalogue.csv"] = catalogue_frame()
    files[f"{FOLDER}/lineage.csv"] = lineage_frame()
    stale = stale_frame()
    files["truth/architecture/catalogue_stale.csv"] = stale
    add_ea_document(world, components)
    world["gold"]["threats"] = threats(components, identity["accounts"], world["gold"].get("stale_access", []))
    world["gold"]["catalogue_stale"] = stale.to_dict(orient="records")
    world["tables"]["components"] = components
    world["tables"]["model_register"] = register
