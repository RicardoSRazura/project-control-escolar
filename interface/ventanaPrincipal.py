from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox

from interface.aulas import AulasWindow
from interface.carreras import CarrerasWindow
from interface.horarios import HorariosWindow
from interface.usuarios import UsuariosWindow

class MainWindow():
    def __init__(self):
        self.ventanaPrincipal = uic.loadUi("interface/ventanPrincipal.ui")
        self.ventanaUsuarios = UsuariosWindow()
        self.ventanaCarreras = CarrerasWindow()
        self.ventanaHorarios = HorariosWindow()
        self.ventanaSalones = AulasWindow()
        self.initGui()
        self.ventanaPrincipal.showMaximized()

    def initGui(self):
        self.ventanaPrincipal.btnUsuarios.triggered.connect(self.abrirUsuarios)
        self.ventanaPrincipal.btnCarrera.triggered.connect(self.abrirCarreras)
        self.ventanaPrincipal.btnHorarios.triggered.connect(self.abrirHorarios)
        self.ventanaPrincipal.btnSalones.triggered.connect(self.abrirSalones)

    def abrirUsuarios(self):
        self.ventanaUsuarios.userWindow.show()

    def abrirCarreras(self):
        self.ventanaCarreras.carreraWindow.show()

    def abrirHorarios(self):
        self.ventanaHorarios.horarioWindow.show()

    def abrirSalones(self):
        self.ventanaSalones.aulasWindow.show()