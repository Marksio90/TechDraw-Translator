from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Pattern


class ProtectedPatternManager:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.patterns = self._load_patterns()

    def _load_patterns(self) -> list[Pattern[str]]:
        payload = json.loads(self.path.read_text(encoding="utf-8"))
        return [re.compile(p, re.IGNORECASE) for p in payload.get("patterns", [])]

    def find_matches(self, text: str) -> list[str]:
        matches: list[str] = []
        for pattern in self.patterns:
            matches.extend(m.group(0) for m in pattern.finditer(text))
        return sorted(set(matches), key=len, reverse=True)


class PlaceholderProtector:
    def __init__(self, manager: ProtectedPatternManager) -> None:
        self.manager = manager

    def protect(self, text: str) -> tuple[str, dict[str, str]]:
        mapping: dict[str, str] = {}
        protected = text
        i = 1
        for match in self.manager.find_matches(text):
            placeholder = f"__PROTECTED_{i}__"
            protected = protected.replace(match, placeholder)
            mapping[placeholder] = match
            i += 1
        return protected, mapping

    @staticmethod
    def restore(text: str, mapping: dict[str, str]) -> str:
        restored = text
        for placeholder, value in mapping.items():
            restored = restored.replace(placeholder, value)
        return restored
