"""Letter templates as the bureau proofs them. The referral result template fails the accessibility standard."""

from __future__ import annotations

from simulation.delivery.accessibility import LETTER_REQUIREMENTS, contrast, failures, header

FAILING = "result-referral"
ALTERNATIVES_LINE = ("If you need this letter in large print, audio, braille, or another language, "
                     "call {{contact_number}} or reply through the patient portal.")

TEMPLATES = {
    "invitation": ("14", "#1A1A1A", "#FFFFFF", "9", (
        "Dear {{forename}},",
        "It is time for your diabetic eye check. The check takes about half an hour.",
        "Your appointment is on {{date}} at {{time}} at {{clinic}}.",
        "Please bring your glasses. Your eyes may be blurry after the drops, so do not drive home.",
    )),
    "reminder": ("14", "#1A1A1A", "#FFFFFF", "8", (
        "Dear {{forename}},",
        "This is a reminder of your eye check on {{date}} at {{time}} at {{clinic}}.",
        "If you cannot come, call us so we can offer the slot to someone else.",
    )),
    "result-routine": ("14", "#222222", "#FFFFFF", "10", (
        "Dear {{forename}},",
        "Your eye check photos have been looked at. Your grade was R0 (no signs of eye damage from diabetes).",
        "We will invite you again in about a year.",
    )),
    FAILING: ("11", "#949494", "#FFFFFF", "15", (
        "Dear {{forename}},",
        "Following retinal photographic assessment undertaken at {{clinic}}, your images were graded R2 and, "
        "in accordance with the programme's referral pathway, an onward referral to the hospital eye service has been initiated.",
        "The hospital eye service will contact you in due course regarding an appointment.",
    )),
    "did-not-attend": ("14", "#1A1A1A", "#FFFFFF", "9", (
        "Dear {{forename}},",
        "We missed you at your eye check on {{date}}. Eye checks find problems early, before you notice them.",
        "Call us or use the patient portal to book a new time.",
    )),
}


def render_template(template_id: str) -> str:
    font, text_colour, background, reading_age, paragraphs = TEMPLATES[template_id]
    lines = [
        f"template_id: {template_id}",
        "version: 2026-06",
        f"font_pt: {font}",
        f"text_colour: {text_colour}",
        f"background_colour: {background}",
        f"reading_age_measured: {reading_age}",
        "",
        *[f"{paragraph}\n" for paragraph in paragraphs],
    ]
    if template_id != FAILING:
        lines.append(f"{ALTERNATIVES_LINE}\n")
    lines.append("Hartland Diabetic Eye Screening Programme")
    return "\n".join(lines) + "\n"


def template_files() -> dict[str, str]:
    return {f"handover/letters/templates/{template_id}.md": render_template(template_id) for template_id in sorted(TEMPLATES)}


def templates_gold() -> dict:
    results = {}
    for template_id in sorted(TEMPLATES):
        text = render_template(template_id)
        fields = header(text)
        results[template_id] = {"fails": failures(text),
                                "contrast": contrast(fields["text_colour"], fields["background_colour"])}
    failing = sorted(template_id for template_id, result in results.items() if result["fails"])
    return {"templates": results, "failing": failing, "checked_requirements": list(LETTER_REQUIREMENTS)}
