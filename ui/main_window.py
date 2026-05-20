from PySide6.QtWidgets import QMainWindow, QTabWidget
from ui.drawing_tab import DrawingTab
from ui.email_tab import EmailTab
from ui.glossary_tab import GlossaryTab
from ui.settings_tab import SettingsTab


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Tłumacz Rysunków Technicznych")
        tabs = QTabWidget()
        tabs.addTab(DrawingTab(), "Rysunek")
        tabs.addTab(EmailTab(), "Mail")
        tabs.addTab(GlossaryTab(), "Słownik")
        tabs.addTab(SettingsTab(), "Ustawienia")
        self.setCentralWidget(tabs)
        self.resize(1100, 750)
