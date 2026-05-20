from __future__ import annotations

import csv
from pathlib import Path
from core.models import TranslationResult


def export_csv(path: Path, rows: list[TranslationResult]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["page", "original", "translation", "category", "confidence", "status"])
        for r in rows:
            writer.writerow([r.page, r.original_text, r.translated_text, r.category, r.confidence, r.status])
