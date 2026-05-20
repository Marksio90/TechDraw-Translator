from __future__ import annotations

from abc import ABC, abstractmethod

from core.glossary import Glossary
from core.protected_patterns import PlaceholderProtector


class TranslationEngine(ABC):
    @abstractmethod
    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        raise NotImplementedError


class MockTranslationEngine(TranslationEngine):
    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        return f"[{target_lang}] {text}"


class SafeTranslator:
    def __init__(self, engine: TranslationEngine, glossary: Glossary, protector: PlaceholderProtector) -> None:
        self.engine = engine
        self.glossary = glossary
        self.protector = protector

    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        direct = self.glossary.lookup(text)
        if direct:
            return direct
        protected, mapping = self.protector.protect(text)
        with_glossary = self.glossary.apply_inline(protected)
        translated = self.engine.translate(with_glossary, source_lang, target_lang)
        return self.protector.restore(translated, mapping)
