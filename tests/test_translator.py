from pathlib import Path
from core.glossary import Glossary
from core.protected_patterns import PlaceholderProtector, ProtectedPatternManager
from core.translator import MockTranslationEngine, SafeTranslator


def test_translation_with_protected_values():
    data = Path(__file__).resolve().parents[1] / "data"
    tr = SafeTranslator(MockTranslationEngine(), Glossary(data / "glossary_en_pl.json"), PlaceholderProtector(ProtectedPatternManager(data / "protected_patterns.json")))
    out = tr.translate("MATERIAL S235JR POWDER COATED RAL 9005", "en", "pl")
    assert "S235JR" in out and "RAL 9005" in out
