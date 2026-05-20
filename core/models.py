from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional

TextCategory = Literal[
    "TRANSLATABLE_TEXT",
    "PROTECTED_TECHNICAL_VALUE",
    "DIMENSION",
    "MATERIAL",
    "STANDARD",
    "THREAD",
    "SURFACE_FINISH",
    "TOLERANCE",
    "PART_NUMBER",
    "REVISION",
    "TABLE_HEADER",
    "LOW_CONFIDENCE",
    "UNKNOWN",
]


@dataclass
class BoundingBox:
    x1: float
    y1: float
    x2: float
    y2: float


@dataclass
class OCRTextBlock:
    page: int
    text: str
    bbox: BoundingBox
    confidence: float
    source: str


@dataclass
class ClassifiedTextBlock:
    page: int
    original_text: str
    category: TextCategory
    bbox: BoundingBox
    confidence: float
    should_translate: bool
    reason: str


@dataclass
class TranslationResult:
    page: Optional[int]
    original_text: str
    translated_text: str
    category: TextCategory
    confidence: float
    status: str
    bbox: Optional[BoundingBox] = None
