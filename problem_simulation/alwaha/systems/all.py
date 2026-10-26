"""Every export named in the systems note.

EXPORTS is the order the exports are reported. faults() asks each of those modules for its record. record.py is not itself an export; the export modules call it.
"""

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
    """Return one fault record per export, in EXPORTS order.

    The profile is passed through to each module. The list has one record for every export.
    """
    return [module.fault(profile) for module in EXPORTS]
