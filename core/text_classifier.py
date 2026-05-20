from __future__ import annotations

import re
from core.models import ClassifiedTextBlock, OCRTextBlock
from core.protected_patterns import ProtectedPatternManager


class TextClassifier:
    def __init__(self, manager: ProtectedPatternManager, min_conf: float = 0.65) -> None:
        self.manager = manager
        self.min_conf = min_conf

    def classify(self, block: OCRTextBlock) -> ClassifiedTextBlock:
        txt = block.text.strip()
        if block.confidence < self.min_conf:
            return ClassifiedTextBlock(block.page, txt, "LOW_CONFIDENCE", block.bbox, block.confidence, False, "Low OCR confidence")
        for pat in self.manager.patterns:
            if pat.search(txt):
                return ClassifiedTextBlock(block.page, txt, "PROTECTED_TECHNICAL_VALUE", block.bbox, block.confidence, False, "Matched protected pattern")
        if re.match(r"^[A-Z\s]{3,}$", txt):
            return ClassifiedTextBlock(block.page, txt, "TABLE_HEADER", block.bbox, block.confidence, True, "Likely header")
        return ClassifiedTextBlock(block.page, txt, "TRANSLATABLE_TEXT", block.bbox, block.confidence, True, "Default")
