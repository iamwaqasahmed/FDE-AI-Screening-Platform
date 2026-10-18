"""The contract, the card, and the incident note. The checker looks for facts, not headings."""

from __future__ import annotations


def contract(items: dict) -> str:
    zone = items["bureau_agreement"]["zone"]
    days = items["bureau_agreement"]["retention_days"]
    return "\n".join([
        "feed: bureau_dispatch",
        "system: letters",
        f"zone: {zone}",
        "grain: one row per dispatch",
        "keys:",
        "  - request_id",
        "columns:",
        "  - name: template",
        "dates:",
        "  dispatched_at: ISO",
        "known_defects:",
        "  - a retry writes a second row for one request",
        "  - DOB must not cross",
        "owner: programme manager",
        "consumers:",
        "  - screening service",
        "fails_when:",
        "  - a row is dropped silently",
        "  - a request id is repeated",
        "business_key: request_id",
        "reconciles_against: the authority request file",
        f"retention_days: {days}",
        f"crosses_to: {zone}",
        "",
    ])


def card(items: dict, keyword: int, tfidf: int) -> str:
    drop = items["drop_incident"]
    return "\n".join([
        "# Graph card",
        "",
        "Keyword retrieval lost the questions that need a second record.",
        f"TF-IDF lost them too. Keyword overall percent {keyword}. TF-IDF overall percent {tfidf}.",
        "",
        "The business key is request_id. Status and the effective date decide which specialist document binds.",
        "A draft does not bind.",
        "The path records the request, the document, and the MRN where there is one.",
        f"{drop['lost']} requests were lost. {drop['duplicate_rows']} rows are second copies.",
        "",
        "An embedding was not required. The agent is out of scope.",
        "",
    ])


def note(items: dict) -> str:
    drop, lost = items["drop_incident"], items["chase_lost_people"]
    resend, window = items["resend_summary"], items["resend_window"]
    cost = int(round(items["incident_cost"]["total_gbp"]))
    start, end = drop["window"]
    return "\n".join([
        "# Incident note",
        "",
        f"The bureau window is {start} to {end}.",
        f"{drop['lost']} requests have no dispatch, and {drop['duplicate_rows']} rows are second copies.",
        "The service notice does not survive those two files.",
        "",
        f"{lost['local_ids']} local ids in the upper bound were not reached, about {lost['people']} people.",
        "The count is an upper bound. People flagged deceased are not written to again, and neither is someone already seen.",
        "",
        "This is the same failure as INC-0233. The 2025 file had no request id, so the losses could not be counted.",
        f"Re-send {resend['resend']} letters. A print run is not a release. The next letters window is {window['next_window']}.",
        f"The duplicate prints and the re-send cost {cost} pounds.",
        "",
        "DOB stays inside the authority. The safety owner is still unnamed, so the pilot stays stopped.",
        "The programme manager owns the contact list. The bureau corrects its notice and keeps the files until the retention date.",
        "",
    ])
