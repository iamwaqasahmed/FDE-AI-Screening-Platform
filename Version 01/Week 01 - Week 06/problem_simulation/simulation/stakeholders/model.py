"""A persona: a public card, hidden facts with truth traces, and a question tree that releases them."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field

from simulation.stakeholders.traces import resolve
from simulation.world.staff import BY_KEY


@dataclass(frozen=True)
class Card:
    goals: tuple[str, ...]
    constraints: tuple[str, ...]
    says_first: str
    wants: str


@dataclass(frozen=True)
class Trace:
    source: str
    ref: str
    value: str


@dataclass(frozen=True)
class HiddenFact:
    fact_id: str
    text: str
    traces: tuple[Trace, ...]
    must_surface: bool = True


@dataclass(frozen=True)
class Node:
    node_id: str
    keywords: tuple[str, ...]
    answer: str
    releases: tuple[str, ...] = ()
    parent: str = ""


@dataclass(frozen=True)
class Conflict:
    other: str
    topic: str
    description: str


@dataclass(frozen=True)
class Persona:
    key: str
    card: Card
    facts: tuple[HiddenFact, ...]
    tree: tuple[Node, ...]
    conflicts: tuple[Conflict, ...]
    must_not_claim: tuple[str, ...]
    strong: tuple[str, ...]
    weak: tuple[str, ...]
    extra: dict = field(default_factory=dict)

    @property
    def name(self) -> str:
        return BY_KEY[self.key].name

    @property
    def role(self) -> str:
        return BY_KEY[self.key].role

    def fact(self, fact_id: str) -> HiddenFact:
        return next(item for item in self.facts if item.fact_id == fact_id)

    def must_surface(self) -> list[str]:
        return [item.fact_id for item in self.facts if item.must_surface]

    def to_json(self) -> dict:
        data = asdict(self)
        data.update(name=self.name, role=self.role, must_surface=self.must_surface())
        return data


def fact(world: dict, fact_id: str, template: str, *refs: str, must_surface: bool = True) -> HiddenFact:
    """Each ref is 'source/ref'. Placeholders {0}, {1}... are filled from the traces, so the text carries each value."""
    traces = []
    for item in refs:
        source, ref = item.split("/", 1)
        traces.append(Trace(source, ref, resolve(world, source, ref)))
    return HiddenFact(fact_id, template.format(*(trace.value for trace in traces)), tuple(traces), must_surface)


def node(node_id: str, keywords: str, answer: str, releases: str = "", parent: str = "") -> Node:
    return Node(node_id, tuple(keywords.split()), answer, tuple(releases.split()), parent)
