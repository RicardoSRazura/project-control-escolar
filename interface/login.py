from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox

class Login():
    def __init__(self):
        self.login = uic.loadUi("interface/login.ui")
        self.login.show()