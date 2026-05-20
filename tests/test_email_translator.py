from pathlib import Path
from core.email_translator import EmailTranslator
from core.glossary import Glossary
from core.protected_patterns import PlaceholderProtector, ProtectedPatternManager
from core.translator import MockTranslationEngine, SafeTranslator


def test_email_translation_extracts_technical_requirements():
    data = Path(__file__).resolve().parents[1] / "data"
    et = EmailTranslator(SafeTranslator(MockTranslationEngine(), Glossary(data / "glossary_en_pl.json"), PlaceholderProtector(ProtectedPatternManager(data / "protected_patterns.json"))))
    res = et.translate_email("Please quote 400 pcs. Material S235JR. RAL 9005. Delivery 4 weeks.")
    assert res.extracted["quantity"] == "400 pcs"
    assert res.extracted["material"] == "S235JR"
