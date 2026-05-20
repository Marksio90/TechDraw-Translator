from pathlib import Path
from core.protected_patterns import ProtectedPatternManager, PlaceholderProtector


def _protector() -> PlaceholderProtector:
    manager = ProtectedPatternManager(Path(__file__).resolve().parents[1] / "data" / "protected_patterns.json")
    return PlaceholderProtector(manager)


def test_thread_and_diameter_detection():
    p = _protector()
    txt, m = p.protect("Use M8 and hole Ø10")
    assert "M8" not in txt and "Ø10" not in txt
    assert len(m) >= 2


def test_protect_material_and_ral():
    p = _protector()
    text = "MATERIAL S235JR POWDER COATED RAL 9005"
    protected, mapping = p.protect(text)
    assert "S235JR" not in protected
    assert "RAL 9005" not in protected
    assert "__PROTECTED_" in protected
    restored = p.restore(protected, mapping)
    assert restored == text
