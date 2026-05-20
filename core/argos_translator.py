from __future__ import annotations

from core.translator import TranslationEngine


class ArgosTranslationEngine(TranslationEngine):
    def __init__(self) -> None:
        self._module = None
        try:
            import argostranslate.translate as tr

            self._module = tr
        except Exception:
            self._module = None

    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        if not self._module:
            raise RuntimeError("Argos Translate unavailable. Zainstaluj pakiet i modele językowe.")
        langs = self._module.get_installed_languages()
        src = next((l for l in langs if l.code == source_lang), None)
        tgt = next((l for l in langs if l.code == target_lang), None)
        if not src or not tgt:
            raise RuntimeError(f"Brak modelu językowego Argos: {source_lang}->{target_lang}")
        return src.get_translation(tgt).translate(text)
