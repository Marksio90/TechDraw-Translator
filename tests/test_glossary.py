from pathlib import Path
from core.glossary import Glossary


def test_lookup_and_inline():
    g = Glossary(Path(__file__).resolve().parents[1] / "data" / "glossary_en_pl.json")
    assert g.lookup("material") == "materiał"
    assert "materiał" in g.apply_inline("Material thickness")
