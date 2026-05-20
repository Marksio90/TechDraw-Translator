from pathlib import Path
from core.models import BoundingBox, OCRTextBlock
from core.protected_patterns import ProtectedPatternManager
from core.text_classifier import TextClassifier


def test_low_confidence_classification():
    c = TextClassifier(ProtectedPatternManager(Path(__file__).resolve().parents[1] / "data" / "protected_patterns.json"), min_conf=0.8)
    b = OCRTextBlock(1, "Some note", BoundingBox(0,0,1,1), 0.7, "ocr")
    assert c.classify(b).category == "LOW_CONFIDENCE"
