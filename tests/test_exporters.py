from pathlib import Path
from core.csv_exporter import export_csv
from core.models import TranslationResult


def test_csv_export(tmp_path: Path):
    p = tmp_path / "a.csv"
    export_csv(p, [TranslationResult(1, "A", "B", "TRANSLATABLE_TEXT", 1.0, "OK")])
    assert p.exists()
