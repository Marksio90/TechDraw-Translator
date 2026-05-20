from __future__ import annotations

import re
from dataclasses import dataclass

from core.translator import SafeTranslator


@dataclass
class EmailTranslation:
    translated_text: str
    extracted: dict[str, str]


class EmailTranslator:
    def __init__(self, translator: SafeTranslator) -> None:
        self.translator = translator

    def translate_email(self, text: str, source_lang: str = "en", target_lang: str = "pl") -> EmailTranslation:
        translated = self.translator.translate(text, source_lang, target_lang)
        extracted: dict[str, str] = {}
        for key, pat in {
            "quantity": r"\b\d+\s?(pcs|szt)\b",
            "material": r"\bS\d{3,4}[A-Z]*\b|\b1\.\d{4}\b|\bAISI\s?\d+\b",
            "surface": r"\bRAL\s?\d{4}\b",
            "delivery_time": r"\b\d+\s?(weeks?|dni|days?)\b",
        }.items():
            m = re.search(pat, text, flags=re.IGNORECASE)
            if m:
                extracted[key] = m.group(0)
        return EmailTranslation(translated, extracted)
