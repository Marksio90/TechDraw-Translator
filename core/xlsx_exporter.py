from __future__ import annotations
from pathlib import Path
from core.models import TranslationResult


def export_xlsx(path: Path, rows: list[TranslationResult]) -> None:
    try:
        from openpyxl import Workbook
    except Exception as exc:
        raise RuntimeError("openpyxl is required for XLSX export") from exc
    wb = Workbook()
    ws = wb.active
    ws.append(["page", "original", "translation", "category", "confidence", "status"])
    for r in rows:
        ws.append([r.page, r.original_text, r.translated_text, r.category, r.confidence, r.status])
    wb.save(path)
