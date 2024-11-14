from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox



class UsuariosWindow():
    def __init__(self):
        self.userWindow = uic.loadUi("interface/usuarios.ui")
        self.initGui()

    
    def initGui(self):
        self.userWindow.btnNuevo.clicked.connect()
    
    def nuevoUser(self):
        self.userWindow.entryId.clear()
        self.userWindow.entryNombre.clear()
        self.userWindow.entry

        
