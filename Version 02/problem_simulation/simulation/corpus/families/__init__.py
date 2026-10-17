"""Corpus document families, built in order. Later families may read documents earlier ones added."""

from simulation.corpus.families import (
    board_tables,
    district_reports,
    duplicates,
    governance,
    grader_reviews,
    minutes,
    notices,
    patient_letters,
    procurement,
    proposals,
    quality_audits,
    sharing,
    site_reports,
    standards,
)

FAMILIES = (
    board_tables,
    site_reports,
    district_reports,
    quality_audits,
    grader_reviews,
    notices,
    minutes,
    patient_letters,
    governance,
    sharing,
    standards,
    procurement,
    proposals,
    duplicates,
)
