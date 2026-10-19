"""Write one note per persona from the interview simulator. Questions carry no seed-specific values."""

from __future__ import annotations

from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent / "scripts"


def write(folder: Path) -> None:
    from simulation.stakeholders.interview import score_script

    folder.mkdir(parents=True, exist_ok=True)
    for path in sorted(SCRIPTS.glob("*.txt")):
        questions = path.read_text(encoding="utf-8").splitlines()
        result = score_script(path.stem, questions)
        lines = [f"# {path.stem}", ""]
        for turn in result["turns"]:
            lines.append(f"Q: {turn['question']}")
            lines.append(f"A: {turn['answer']}")
            lines.append("")
        (folder / f"{path.stem}.md").write_text("\n".join(lines), encoding="utf-8")
