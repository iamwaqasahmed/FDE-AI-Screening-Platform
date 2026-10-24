"""Every export named in the systems note."""

from __future__ import annotations

from alwaha.systems import (
    bi,
    catalog,
    cc,
    complaints,
    consent,
    dms,
    eref,
    finance,
    his_nakhl,
    his_safra,
    his_wadi,
    hr,
    iam,
    insure,
    int_engine,
    itsm,
    nid,
    phc_templates,
    sched_ain,
    sms,
    wa,
)

EXPORTS = (
    his_nakhl,
    his_safra,
    his_wadi,
    eref,
    phc_templates,
    sched_ain,
    nid,
    sms,
    wa,
    cc,
    complaints,
    consent,
    insure,
    hr,
    bi,
    iam,
    finance,
    int_engine,
    dms,
    catalog,
    itsm,
)


def faults(profile) -> list[dict]:
    return [module.fault(profile) for module in EXPORTS]
