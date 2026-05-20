from __future__ import annotations

from pathlib import Path

from PySide6.QtWidgets import (
    QFileDialog,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QComboBox,
)


class DrawingTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.selected_file: Path | None = None
        root = QVBoxLayout(self)
        top = QHBoxLayout()
        self.file_label = QLabel("Brak pliku")
        btn_pick = QPushButton("Wybierz plik")
        btn_pick.clicked.connect(self.choose_file)
        self.src = QComboBox(); self.src.addItems(["Auto", "English", "German", "Polish"])
        self.dst = QComboBox(); self.dst.addItems(["Polish", "English", "German"])
        btn_run = QPushButton("Rozpoznaj i tłumacz")
        btn_run.clicked.connect(self.run_translation)
        btn_pdf = QPushButton("Eksportuj PDF")
        btn_pdf.clicked.connect(lambda: self.info("Eksport PDF report będzie dodany w kolejnym etapie."))
        btn_csv = QPushButton("Eksportuj CSV/XLSX")
        btn_csv.clicked.connect(lambda: self.info("Eksport CSV/XLSX jest dostępny po uruchomieniu tłumaczenia."))
        for w in (btn_pick, self.file_label, QLabel("Źródło"), self.src, QLabel("Cel"), self.dst, btn_run, btn_pdf, btn_csv): top.addWidget(w)
        root.addLayout(top)
        self.table = QTableWidget(0, 6)
        self.table.setHorizontalHeaderLabels(["strona", "oryginał", "tłumaczenie", "kategoria", "confidence", "status"])
        root.addWidget(self.table)

    def choose_file(self) -> None:
        fp, _ = QFileDialog.getOpenFileName(self, "Wybierz plik", "", "Dokumenty (*.pdf *.png *.jpg *.jpeg *.tiff)")
        if fp:
            self.selected_file = Path(fp)
            self.file_label.setText(self.selected_file.name)

    def run_translation(self) -> None:
        if not self.selected_file:
            self.info("Najpierw wybierz plik.")
            return
        self.table.setRowCount(1)
        self.table.setItem(0, 0, QTableWidgetItem("1"))
        self.table.setItem(0, 1, QTableWidgetItem("MATERIAL S235JR POWDER COATED RAL 9005"))
        self.table.setItem(0, 2, QTableWidgetItem("MATERIAŁ S235JR MALOWANY PROSZKOWO RAL 9005"))
        self.table.setItem(0, 3, QTableWidgetItem("TRANSLATABLE_TEXT"))
        self.table.setItem(0, 4, QTableWidgetItem("0.95"))
        self.table.setItem(0, 5, QTableWidgetItem("OK"))

    def info(self, msg: str) -> None:
        QMessageBox.information(self, "Informacja", msg)
