"""The ordered surface stages. Later stages may read what earlier stages put in the world."""

from __future__ import annotations

from simulation.corpus import stage as corpus_stage
from simulation.delivery import stage as delivery_stage
from simulation.drops import stage as drops_stage
from simulation.economics import stage as economics_stage
from simulation.estate import stage as estate_stage
from simulation.ml import stage as ml_stage
from simulation.stakeholders import stage as stakeholders_stage
from simulation.workforce import stage as workforce_stage

STAGES = [
    ("workforce and devices", workforce_stage.build),
    ("corpus", corpus_stage.build),
    ("estate", estate_stage.build),
    ("economics", economics_stage.build),
    ("stakeholders", stakeholders_stage.build),
    ("ml evidence", ml_stage.build),
    ("delivery", delivery_stage.build),
    ("drops", drops_stage.build),
]
