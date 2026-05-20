from __future__ import annotations

import json
from pathlib import Path


class Glossary:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.terms = self._load()

    def _load(self) -> dict[str, str]:
        if not self.path.exists():
            return {}
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        return {k.lower(): v for k, v in raw.items()}

    def save(self) -> None:
        self.path.write_text(json.dumps(self.terms, ensure_ascii=False, indent=2), encoding="utf-8")

    def lookup(self, text: str) -> str | None:
        return self.terms.get(text.strip().lower())

    def apply_inline(self, text: str) -> str:
        out = text
        for src, dst in sorted(self.terms.items(), key=lambda x: len(x[0]), reverse=True):
            out = re_sub_case_insensitive(out, src, dst)
        return out


def re_sub_case_insensitive(text: str, src: str, dst: str) -> str:
    import re

    return re.sub(re.escape(src), dst, text, flags=re.IGNORECASE)
