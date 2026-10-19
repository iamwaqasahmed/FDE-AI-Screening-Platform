"""One row per findings item: who it belongs to, whether a rerun grades it, and the check."""

from __future__ import annotations

from enterprise_check.items import cohorts, counts, drop, identity, pathway, quality, release

DE, DS, ML, SW, AR, PM, CO = (
    ("data_engineering",),
    ("data_science",),
    ("ml",),
    ("software",),
    ("architect",),
    ("pm",),
    ("consultant",),
)


def _row(item_id, check, roles, mode):
    return {"id": item_id, "check": check, "roles": roles, "mode": mode}


ITEMS = [
    _row("drop_schema", drop.drop_schema, DE + SW, "computed"),
    _row("drop_reissue", drop.drop_reissue, DE + PM, "computed"),
    _row("drop_local_ids", drop.drop_local_ids, DE, "computed"),
    _row("api_v3", drop.api_v3, SW + AR, "read"),
    _row("catalogue_stale", quality.catalogue_stale, AR, "computed"),
    _row("sms_reconcile", quality.sms_reconcile, SW + DE, "computed"),
    _row("booking_reconcile", quality.booking_reconcile, SW + DS, "computed"),
    _row("feed_dedupe", quality.feed_dedupe, SW, "read"),
    _row("unlinked_keys", identity.unlinked_keys, DE + AR, "read"),
    _row("identity_defects", identity.identity_defects, DE + ML, "computed"),
    _row("confidence_rule", identity.confidence_rule, DE + DS, "read"),
    _row("eligible_people", counts.eligible_people, DE, "computed"),
    _row("eligible_by_district", counts.eligible_by_district, DE + DS, "computed"),
    _row("coverage", counts.coverage, DE + AR, "computed"),
    _row("site_rules", pathway.site_rules, DS + AR, "computed"),
    _row("stale_register", pathway.stale_register, DS + AR, "read"),
    _row("overdue", cohorts.overdue, DS + CO, "computed"),
    _row("vendor_cohort", cohorts.vendor_cohort, ML + DE, "computed"),
    _row("split_leak", cohorts.split_leak, ML + DS, "computed"),
    _row("release_plan", release.release_plan, PM + AR, "computed"),
    _row("freeze_blocked", release.freeze_blocked, PM, "computed"),
    _row("rerun_contracts", release.rerun_contracts, PM + CO, "read"),
    _row("raci_v3", release.raci_v3, PM + CO, "read"),
]
