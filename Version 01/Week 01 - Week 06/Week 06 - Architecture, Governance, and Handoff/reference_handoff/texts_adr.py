"""Four proposed decisions. None is accepted this week."""

from __future__ import annotations


def adr(number: str, title: str, decider: str, consulted: str, body: str, documents: str) -> str:
    consulted_line = f"\nConsulted: {consulted}\n" if consulted else "\n"
    return (
        f"# ADR-{number} {title}\n\nStatus: Proposed\n\nDecider: {decider}\n"
        f"{consulted_line}\n{body}\n\nDocuments cited: {documents}\n"
    )


def all_records(names: dict, model: str) -> dict[str, str]:
    return {
        "adr-01": adr("01", "Residency", names["dpo"], "", _residency(names["dpo"]), "cloud-policy, dpia-vendor-2024"),
        "adr-02": adr("02", "Score path", names["architect"], names["security"], _path(), "ea-principles, security-supplier-assurance"),
        "adr-03": adr("03", "Sign-off", names["owner"], names["grader"], _sign(names["grader"]), "dpo-rule-2018, ai-human-oversight-standard"),
        "adr-04": adr("04", "Production path", names["security"], "", _image(model), "security-logging-standard, cloud-policy"),
    }


def _residency(decider: str) -> str:
    return (
        f"{decider} has not approved the vendor region in writing. Official-sensitive captures would sit in an EU region. "
        "This stays proposed. Hospital studies stay in the hospital zone."
    )


def _path() -> str:
    return (
        "Scores return vendor to vendor-callback to integration-engine to grader. "
        "The callback does not land on the grader workbench. This stays proposed."
    )


def _sign(grader: str) -> str:
    return f"{grader} signs every result on the grader workbench. The model output is advisory. This stays proposed."


def _image(model: str) -> str:
    return (
        f"The service is rebuilt around {model}. It is read-only. A question in the log fails the run. "
        "The Week 00 - Self Paced image is not reused. This stays proposed."
    )
