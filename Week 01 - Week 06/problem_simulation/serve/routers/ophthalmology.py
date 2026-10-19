"""Ophthalmology API: referral messages as the hospital received them."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Request

from serve.data import matching, read_rows
from serve.guard import guard, settings_of
from serve.pagination import Paging, page, paging

MESSAGES = "ophthalmology/messages.pipe"

router = APIRouter(prefix="/ophthalmology", tags=["ophthalmology"], dependencies=[Depends(guard("ophthalmology"))])


def _messages(request: Request) -> list[dict]:
    return read_rows(settings_of(request).handover, MESSAGES)


@router.get("/referrals")
def referrals(
    request: Request,
    local_pid: str | None = None,
    grade: str | None = None,
    window: Paging = Depends(paging),
) -> dict:
    return page(matching(_messages(request), local_pid=local_pid, grade=grade), window)


@router.get("/referrals/{mrn}")
def referrals_for(request: Request, mrn: str) -> dict:
    rows = matching(_messages(request), mrn=mrn)
    if not rows:
        raise HTTPException(404, detail=f"no referral messages for {mrn}")
    return {"mrn": mrn, "items": rows}
