from PySide6.QtWidgets import QWidget, QFormLayout, QComboBox, QDoubleSpinBox


class SettingsTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        form = QFormLayout(self)
        ocr = QComboBox(); ocr.addItems(["PaddleOCR", "Tesseract"])
        tr = QComboBox(); tr.addItems(["Argos", "Mock (test)"])
        conf = QDoubleSpinBox(); conf.setRange(0.1, 1.0); conf.setValue(0.65)
        form.addRow("OCR", ocr); form.addRow("Tłumaczenie", tr); form.addRow("Minimalne confidence", conf)
