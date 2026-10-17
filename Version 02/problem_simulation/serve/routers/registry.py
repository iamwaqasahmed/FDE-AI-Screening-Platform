"""Registry API: the current extract, one person per registry number, in schema version 1, 2, or 3."""

from __future__ import annotations

from fastapi import APIRouter, Depends, Header, HTTPException, Request, Response

from serve.data import matching, read_rows
from serve.guard import guard, settings_of
from serve.pagination import Paging, page, paging
from serve.routers.registry_schema import POLICY, SHAPERS
from serve.versions import negotiate

CURRENT = "registry/current.csv"

router = APIRouter(prefix="/registry", tags=["registry"], dependencies=[Depends(guard("registry"))])


def _version(request: Request, response: Response, accept_version: str | None) -> str:
    version = negotiate(POLICY, accept_version, settings_of(request))
    response.headers["Content-Version"] = version
    return version


@router.get("/people")
def people(
    request: Request,
    response: Response,
    district: str | None = None,
    home_clinic: str | None = None,
    record_status: str | None = None,
    window: Paging = Depends(paging),
    accept_version: str | None = Header(default=None),
) -> dict:
    version = _version(request, response, accept_version)
    rows = read_rows(settings_of(request).handover, CURRENT)
    selected = matching(rows, DISTRICT=district, HOME_CLINIC=home_clinic, RECORD_STATUS=record_status)
    result = page(selected, window)
    result["items"] = [SHAPERS[version](row) for row in result["items"]]
    result["version"] = version
    return result


@router.get("/people/{registry_no}")
def person(request: Request, response: Response, registry_no: str, accept_version: str | None = Header(default=None)) -> dict:
    version = _version(request, response, accept_version)
    rows = matching(read_rows(settings_of(request).handover, CURRENT), REGISTRY_NO=registry_no)
    if not rows:
        raise HTTPException(404, detail=f"no registry record {registry_no}")
    return {"version": version, "items": [SHAPERS[version](row) for row in rows]}
