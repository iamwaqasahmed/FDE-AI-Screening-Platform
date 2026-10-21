"""Booking API: current slot states, a change feed, contact updates, and SMS receipts for a booking."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel

from serve.booking_log import log_request
from serve.data import matching, read_rows
from serve.events import Event, feed, moment_of, parse_since, stable_id
from serve.guard import guard, settings_of
from serve.pagination import Paging, page, paging

APPOINTMENTS = "booking/appointments.csv"
RECEIPTS = "sms/receipts.jsonl"

router = APIRouter(prefix="/booking", tags=["booking"])
reader = Depends(guard("booking"))
writer = Depends(guard("booking", "write"))


class ContactUpdate(BaseModel):
    forename: str = ""
    surname: str = ""
    phone: str = ""


def _appointments(request: Request) -> list[dict]:
    return read_rows(settings_of(request).handover, APPOINTMENTS)


@router.get("/appointments", dependencies=[reader])
def appointments(
    request: Request,
    site: str | None = None,
    status: str | None = None,
    channel: str | None = None,
    window: Paging = Depends(paging),
) -> dict:
    selected = matching(_appointments(request), site=site, status=status, channel=channel)
    result = page(selected, window)
    log_request(request, result["items"])
    return result


@router.get("/appointments/{booking_id}", dependencies=[reader])
def booking(request: Request, booking_id: str) -> dict:
    rows = matching(_appointments(request), booking_id=booking_id)
    log_request(request, rows)
    if not rows:
        raise HTTPException(404, detail=f"no appointments for booking {booking_id}")
    return {"booking_id": booking_id, "items": rows}


@router.post("/appointments/{appointment_id}/contact", status_code=202, dependencies=[writer])
def contact(request: Request, appointment_id: str, update: ContactUpdate) -> dict:
    rows = matching(_appointments(request), appointment_id=appointment_id)
    log_request(request, rows, body=update.model_dump())
    if not rows:
        raise HTTPException(404, detail=f"no appointment {appointment_id}")
    return {"appointment_id": appointment_id, "accepted": True}


def _events(rows: list[dict]) -> list[Event]:
    events = []
    for row in rows:
        moment = moment_of(row.get("updated_at", ""))
        if moment is None:
            continue
        event_id = stable_id("BKE", row.get("appointment_id", ""), row.get("updated_at", ""), row.get("status", ""))
        events.append(Event(event_id, f"appointment.{row.get('status', 'updated')}", moment, dict(row)))
    return events


@router.get("/events", dependencies=[reader])
def events(request: Request, since: str | None = None, window: Paging = Depends(paging)) -> dict:
    settings = settings_of(request)
    delivered = feed(_events(_appointments(request)), parse_since(since), settings.clock)
    result = page(delivered, window)
    log_request(request, [item["payload"] for item in result["items"]])
    return result


@router.get("/receipts", dependencies=[reader])
def receipts(request: Request, booking_id: str | None = None, window: Paging = Depends(paging)) -> dict:
    rows = matching(read_rows(settings_of(request).handover, RECEIPTS), booking_id=booking_id)
    result = page(rows, window)
    log_request(request, result["items"])
    return result
