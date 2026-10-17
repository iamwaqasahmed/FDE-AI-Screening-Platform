"""The estate stage: ten more systems of record, the optional volume streams, and the architecture handover."""

from __future__ import annotations

import numpy as np

from simulation.architecture.landscape import build_architecture
from simulation.config import active
from simulation.estate import volume
from simulation.estate.audit import AUDIT_START, build_audit
from simulation.estate.booking import build_booking
from simulation.estate.booking_logs import build_booking_logs
from simulation.estate.call_centre import build_call_centre
from simulation.estate.common import id_map, log_fault
from simulation.estate.complaints import build_complaints
from simulation.estate.epr_letters import build_epr_letters
from simulation.estate.finance import build_finance
from simulation.estate.identity import build_identity
from simulation.estate.lab import build_lab
from simulation.estate.service_desk import build_service_desk
from simulation.estate.sms import SMS_START, build_sms

STREAMS = 12


def build(world: dict, rng: np.random.Generator) -> None:
    streams = rng.spawn(STREAMS)
    history = build_booking(world, streams[0])
    build_booking_logs(world, history, streams[1])
    sms = build_sms(world, streams[2])
    build_call_centre(world, streams[3])
    build_lab(world, streams[4])
    build_service_desk(world, streams[5])
    identity = build_identity(world, streams[6])
    build_audit(world, identity, streams[7])
    build_finance(world, sms, streams[8])
    build_complaints(world, streams[9])
    build_epr_letters(world, streams[10])
    if active().volume:
        _volume(world, identity, streams[11])
    build_architecture(world, identity)


def _volume(world: dict, identity: dict, rng: np.random.Generator) -> None:
    booking_ids = np.array(sorted(id_map(world["identifiers"], "booking_id").tolist()))
    accounts = np.array(sorted(identity["accounts"]["account_id"].tolist()))
    sms_files, sms_faults = volume.sms_stream(booking_ids, rng, SMS_START)
    audit_files, audit_faults = volume.audit_stream(accounts, booking_ids, rng, AUDIT_START)
    world["files"].update(sms_files)
    world["files"].update(audit_files)
    for entry in sms_faults:
        log_fault(world, "sms-stream", entry)
    for entry in audit_faults:
        log_fault(world, "audit-stream", entry)
