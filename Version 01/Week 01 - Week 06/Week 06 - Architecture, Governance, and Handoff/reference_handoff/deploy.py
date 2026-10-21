"""A Dockerfile that does not copy the authority's data or a key."""

from __future__ import annotations


def text(model: str) -> str:
    return (
        "FROM python:3.12-slim\n"
        "WORKDIR /app\n"
        "COPY screening_service /app/screening_service\n"
        f"ENV MODEL_ID={model}\n"
        'CMD ["python", "-m", "screening_service.run"]\n'
    )
