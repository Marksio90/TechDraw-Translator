# TechDraw Translator / Tłumacz Rysunków Technicznych

Lokalna aplikacja desktopowa (Python + PySide6) do tłumaczenia treści z rysunków technicznych (PDF/JPG/PNG) i maili RFQ. Program działa **lokalnie**, nie wysyła plików do chmury.

## Dla kogo
- kalkulacja i ofertowanie w produkcji,
- technolodzy,
- działy handlowe techniczne,
- firmy obróbki metali i konstrukcji.

## Funkcje
- import PDF/JPG/PNG/TIFF,
- OCR pipeline (moduły przygotowane pod PaddleOCR + Tesseract fallback),
- klasyfikacja bloków tekstu i ochrona wartości technicznych,
- tłumaczenie z priorytetem słownika technicznego,
- tłumaczenie maila + ekstrakcja wymagań technicznych,
- eksport CSV/XLSX,
- UI z zakładkami: Rysunek, Mail, Słownik, Ustawienia.

## Instalacja (Windows)
```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app/main.py
```

Lub:
```bat
run.bat
```

## Jak dodać słownik techniczny
- Edytuj `data/glossary_en_pl.json` i `data/glossary_de_pl.json`,
- albo użyj zakładki **Słownik** (dodawanie haseł).

## Ochrona danych technicznych
Reguły są w `data/protected_patterns.json`. Wartości typu `M8`, `Ø10`, `S235JR`, `RAL 9005`, normy i tolerancje są zamieniane na placeholdery, tłumaczony jest tylko tekst ogólny, a potem wartości są przywracane.

## Eksport PDF
W tej iteracji dostępny jest eksport tabelaryczny (CSV/XLSX), a moduły PDF overlay/report są przygotowane do kolejnego etapu wdrożenia.

## Znane ograniczenia
- OCR zależy od jakości skanu,
- automatyczne tłumaczenie wymaga weryfikacji człowieka,
- do pełnego lokalnego tłumaczenia Argos wymagane są zainstalowane modele językowe,
- obecna wersja UI pokazuje działający przepływ i tłumaczenie maila, a renderowanie pełnego overlay PDF jest planowane.

## Plan rozwoju
1. pełny OCR dla PDF/obrazów,
2. stabilny pipeline klasyfikacji + edycja tłumaczeń w tabeli,
3. overlay PDF i report mode,
4. historia tłumaczeń i konfiguracja per użytkownik,
5. rozszerzenie słowników branżowych.

## Odpowiedzialność
Program pomaga analizować dokumentację ofertową, ale **nie zastępuje odpowiedzialności technologa/kalkulatora**. Każde tłumaczenie techniczne należy zweryfikować.
