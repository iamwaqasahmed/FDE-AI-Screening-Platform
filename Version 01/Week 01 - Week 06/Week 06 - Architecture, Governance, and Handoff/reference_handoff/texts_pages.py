"""The executive page, the clinical page, and the runbook. Same sites, same date."""

from __future__ import annotations


def executive(items: dict, sites: list[str]) -> str:
    owner = items["drop_owner"]
    path = items["conditions"]["CSO-5"]
    site = items["conditions"]["CSO-2"]
    names = ", ".join(sites)
    return (
        f"# Executive page\n\nFor the Chief Digital Officer.\n\n"
        f"{owner['owner']} is named in the week 6 memo, and the owners register is blank. "
        f"The pilot stays stopped until every condition is confirmed.\n\n"
        f"The sites are {names}. {site['withdraw']} does not join. That needs a data protection decision.\n\n"
        f"The earliest go-live is {path['not_before']}. The requested date {path['requested']} does not work.\n"
    )


def clinical(items: dict, sites: list[str]) -> str:
    owner = items["drop_owner"]["owner"]
    path = items["conditions"]["CSO-5"]["not_before"]
    names = ", ".join(sites)
    return (
        f"# Clinical page\n\nFor {owner}.\n\n"
        f"The sites are {names}. The earliest go-live is {path}.\n\n"
        f"A grader signs every result. The model output is advisory. "
        f"The hazard log is unsigned. No condition is confirmed, and the pilot stays stopped.\n"
    )


def runbook(items: dict, names: dict) -> str:
    expires = items["production_account"]["expires"]
    return (
        "# Runbook\n\n"
        f"Call {names['programme']} about operations. Call {names['security']} about an incident. "
        f"Call {names['owner']} to suspend the system. A possible patient-harm incident is reported within four hours.\n\n"
        f"The service will not diagnose, will not send a letter, and stays stopped. "
        f"The discovery token expires on {expires}. It is not valid for production.\n"
    )
