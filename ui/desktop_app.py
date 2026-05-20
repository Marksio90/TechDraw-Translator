from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow


def run() -> int:
    app = QApplication([])
    window = MainWindow()
    window.show()
    return app.exec()
