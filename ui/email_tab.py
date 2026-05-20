from pathlib import Path
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QPushButton, QTableWidget, QTableWidgetItem, QComboBox

from core.argos_translator import ArgosTranslationEngine
from core.email_translator import EmailTranslator
from core.glossary import Glossary
from core.protected_patterns import PlaceholderProtector, ProtectedPatternManager
from core.translator import MockTranslationEngine, SafeTranslator


class EmailTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        data = Path(__file__).resolve().parents[1] / "data"
        manager = ProtectedPatternManager(data / "protected_patterns.json")
        glossary = Glossary(data / "glossary_en_pl.json")
        engine = MockTranslationEngine()
        self.translator = EmailTranslator(SafeTranslator(engine, glossary, PlaceholderProtector(manager)))
        root = QVBoxLayout(self)
        top = QHBoxLayout()
        self.lang = QComboBox(); self.lang.addItems(["English", "German"])
        btn = QPushButton("Tłumacz mail")
        btn.clicked.connect(self.translate)
        top.addWidget(self.lang); top.addWidget(btn)
        root.addLayout(top)
        self.input = QPlainTextEdit(); self.input.setPlaceholderText("Wklej treść maila...")
        self.output = QPlainTextEdit(); self.output.setReadOnly(True)
        self.table = QTableWidget(0,2); self.table.setHorizontalHeaderLabels(["pole","wartość"])
        root.addWidget(self.input); root.addWidget(self.output); root.addWidget(self.table)

    def translate(self) -> None:
        src = "en" if self.lang.currentText()=="English" else "de"
        res = self.translator.translate_email(self.input.toPlainText(), src, "pl")
        self.output.setPlainText(res.translated_text)
        self.table.setRowCount(len(res.extracted))
        for i,(k,v) in enumerate(res.extracted.items()):
            self.table.setItem(i,0,QTableWidgetItem(k)); self.table.setItem(i,1,QTableWidgetItem(v))
