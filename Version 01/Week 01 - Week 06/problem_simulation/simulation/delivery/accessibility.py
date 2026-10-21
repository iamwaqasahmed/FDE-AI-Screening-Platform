"""Accessibility requirements for letters and the patient portal, and the checks a template must pass."""

from __future__ import annotations

import re
from datetime import date

from simulation.corpus.add import Extra, add_document
from simulation.world.staff import name

DOC_ID = "standard-accessibility-letters-portal"
MAX_READING_AGE = 11
MIN_CONTRAST = 4.5
MIN_FONT_PT = 12
ALTERNATIVES = ("large print", "audio", "braille", "another language")
CODE_ALONE = re.compile(r"\bR[0-3]\b(?![^.]*\()")

REQUIREMENTS = (
    ("ACC-01", f"Letters are written for a reading age of {MAX_READING_AGE} or below, measured on the final proof."),
    ("ACC-02", f"Text contrast is at least {MIN_CONTRAST} to 1 against its background."),
    ("ACC-03", f"Body text is at least {MIN_FONT_PT} point. A large-print version at 16 point is available on request."),
    ("ACC-04", "Every letter says how to get it in large print, audio, braille, or another language."),
    ("ACC-05", "Information is never carried by colour alone."),
    ("ACC-06", "Portal pages meet WCAG 2.2 level AA."),
    ("ACC-07", "Portal sessions warn before timing out and never time out in under 20 minutes."),
    ("ACC-08", "Results use plain words. A grade code such as R2 is never shown without its meaning in brackets."),
)
LETTER_REQUIREMENTS = ("ACC-01", "ACC-02", "ACC-03", "ACC-04", "ACC-08")


def add_requirements(world: dict) -> None:
    body = ("This standard applies to every patient letter and to the patient portal. "
            f"The accessibility lead is {name('product_owner')}; the patient forum reviews changes.\n\n"
            + "\n\n".join(f"{rid}. {text}" for rid, text in REQUIREMENTS))
    add_document(world, DOC_ID, "standards", "Accessibility requirements for letters and the patient portal", body,
                 date(2026, 3, 2), extra=Extra(original="docx", table=[["requirement", "text"], *map(list, REQUIREMENTS)]))


def luminance(colour: str) -> float:
    channels = [int(colour.lstrip("#")[index:index + 2], 16) / 255 for index in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast(foreground: str, background: str) -> float:
    high, low = sorted((luminance(foreground), luminance(background)), reverse=True)
    return round((high + 0.05) / (low + 0.05), 2)


def header(text: str) -> dict[str, str]:
    fields = {}
    for line in text.splitlines():
        if not line.strip():
            break
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields


def failures(text: str) -> list[str]:
    fields = header(text)
    body = text.lower()
    found = []
    if int(fields["reading_age_measured"]) > MAX_READING_AGE:
        found.append("ACC-01")
    if contrast(fields["text_colour"], fields["background_colour"]) < MIN_CONTRAST:
        found.append("ACC-02")
    if int(fields["font_pt"]) < MIN_FONT_PT:
        found.append("ACC-03")
    if not all(option in body for option in ALTERNATIVES):
        found.append("ACC-04")
    if CODE_ALONE.search(text.split("\n\n", 1)[1]):
        found.append("ACC-08")
    return found
