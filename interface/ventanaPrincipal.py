from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox

from interface.usuarios import UsuariosWindow

class MainWindow():
    def __init__(self):
        self.ventanaPrincipal = uic.loadUi("interface/ventanPrincipal.ui")
        self.ventanaUsuarios = UsuariosWindow()
        self.initGui()
        self.ventanaPrincipal.showMaximized()

    def initGui(self):
        self.ventanaPrincipal.btnUsuarios.triggered.connect(self.abrirUsuarios)

    def abrirUsuarios(self):
        self.ventanaUsuarios.userWindow.show()