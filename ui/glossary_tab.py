from pathlib import Path
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QInputDialog
from core.glossary import Glossary


class GlossaryTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.path = Path(__file__).resolve().parents[1] / "data" / "glossary_en_pl.json"
        self.glossary = Glossary(self.path)
        root = QVBoxLayout(self)
        self.list = QListWidget(); root.addWidget(self.list)
        btn = QPushButton("Dodaj hasło")
        btn.clicked.connect(self.add_entry)
        root.addWidget(btn)
        self.refresh()

    def refresh(self) -> None:
        self.list.clear()
        for k,v in sorted(self.glossary.terms.items()): self.list.addItem(f"{k} -> {v}")

    def add_entry(self) -> None:
        k, ok = QInputDialog.getText(self, "Źródło", "Fraza źródłowa")
        if not ok or not k: return
        v, ok = QInputDialog.getText(self, "Cel", "Tłumaczenie")
        if not ok or not v: return
        self.glossary.terms[k.lower()] = v
        self.glossary.save(); self.refresh()
