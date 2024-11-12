from PyQt6.QtWidgets import QApplication

from interface.login import Login

class ControlEscolar():
    def __init__(self):
        self.app = QApplication([])
        self.login = Login()

        self.app.exec()