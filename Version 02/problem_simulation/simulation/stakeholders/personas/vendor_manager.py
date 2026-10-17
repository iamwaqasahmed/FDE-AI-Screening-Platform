"""Vendor account manager: headline accuracy holds only for a subgroup and comes from a different population."""

from __future__ import annotations

from simulation.stakeholders.model import Card, Conflict, Persona, fact, node

KEY = "vendor_manager"
MODEL = "constant/simulation.ml.vendor_model"


def build(world: dict) -> Persona:
    facts = (
        fact(world, "vm-subgroup", "Sensitivity holds at {0} for people under 75, but it is {1} for people aged 75 and over.",
             "events/vendor_sens_younger", "events/vendor_sens_older"),
        fact(world, "vm-population", "Hartland scores only exist from {0}; the headline numbers come from a different "
             "population.", f"{MODEL}:RETRO_FROM"),
        fact(world, "vm-firmware", "Score calibration shifted after the outreach camera firmware update on {0}.",
             "clock/FIRMWARE_RIVER"),
        fact(world, "vm-outage", "Our API was down on {0} after a cloud region failure.", "timeline/INC-0274:start"),
        fact(world, "vm-reject", "Images with a quality below {0} are rejected and get no score.", f"{MODEL}:REJECT_BELOW"),
        fact(world, "vm-operator", "Scores are weaker on captures by the operator with initials {0}.",
             "constant/simulation.devices.quality:POOR_OPERATOR", must_surface=False),
    )
    tree = (
        node("accuracy", "accuracy accurate sensitivity specificity performance metrics", "Our sensitivity is above "
             "ninety percent."),
        node("subgroup", "subgroup subgroups age older elderly groups breakdown", "It varies a little.", "vm-subgroup",
             "accuracy"),
        node("population", "population validation validated dataset trained", "We used a large dataset.",
             "vm-population", "accuracy"),
        node("drift", "drift calibration stable stability firmware", "The model is stable."),
        node("camera", "camera update upgrade outreach site", "There was one adjustment.", "vm-firmware", "drift"),
        node("service", "service uptime availability sla outage api", "Our uptime is excellent."),
        node("down", "down incident failure ever", "Once, briefly.", "vm-outage", "service"),
        node("images", "image images quality ungradable reject rejected", "We handle poor images gracefully."),
        node("threshold", "threshold below cut score none empty blank", "There is a cut-off.", "vm-reject", "images"),
        node("operator", "operator operators photographer", "Capture technique matters.", "vm-operator"),
        node("goals", "goal goals want priority priorities success", "We want to expand to every site in Hartland."),
    )
    return Persona(
        key=KEY,
        card=Card(
            goals=("Expand the contract to every site", "Renew before the year end"),
            constraints=("Commercially motivated", "Cannot see Hartland outcomes beyond the pilot file"),
            says_first="Our model outperforms human graders. The evidence is in our proposal.",
            wants="A site-wide contract extension.",
        ),
        facts=facts,
        tree=tree,
        conflicts=(
            Conflict("dpo", "data fields", "Wants hospital studies and a field the DPO bans."),
            Conflict("lead_grader", "accuracy", "Claims to beat graders; the lead grader disputes it."),
        ),
        must_not_claim=("The vendor's headline sensitivity holds for every age group",
                        "The vendor's figures were measured on Hartland's population",
                        "Vendor calibration is stable across firmware versions"),
        strong=(
            "What accuracy and sensitivity does the model achieve?",
            "How does it break down by subgroup, for example older age groups?",
            "What population was it validated on?",
            "Is calibration stable, or does it drift?",
            "Did a camera firmware update at an outreach site change scores?",
            "What is the service uptime and API availability?",
            "Has the API ever gone down in an incident?",
            "What happens to poor quality images?",
            "Below what threshold are they rejected with no score?",
        ),
        weak=(
            "What are your goals?",
            "Is the model good?",
            "How much does it cost?",
            "Anything else?",
        ),
    )
