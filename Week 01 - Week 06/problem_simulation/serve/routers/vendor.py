"""Vendor model API: pilot cohort scores by image file."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Request

from serve.data import matching, read_rows
from serve.guard import guard, settings_of
from serve.pagination import Paging, page, paging

SCORES = "vendor/scores.csv"

router = APIRouter(prefix="/vendor", tags=["vendor"], dependencies=[Depends(guard("vendor"))])


def _scores(request: Request) -> list[dict]:
    return read_rows(settings_of(request).handover, SCORES)


@router.get("/scores")
def scores(request: Request, site: str | None = None, window: Paging = Depends(paging)) -> dict:
    return page(matching(_scores(request), SITE=site), window)


@router.get("/scores/{file_name}")
def score(request: Request, file_name: str) -> dict:
    rows = matching(_scores(request), FILE_NAME=file_name)
    if not rows:
        raise HTTPException(404, detail=f"no score for {file_name}")
    return rows[0]
