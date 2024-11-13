from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox

from data.usuariodb import UsuarioDb
from interface.ventanaPrincipal import MainWindow
from model.usuario import Usuario

class Login():
    def __init__(self):
        self.login = uic.loadUi("interface/login.ui")
        self.initGui()
        self.login.lbMensaje.setText("")
        self.login.show()
    
    def ingresar(self):
        if len(self.login.entryCorreo.text()) < 2:
            self.login.lbMensaje.setText("Ingrese un correo valido")
            self.login.entryCorreo.setFocus()
        elif len(self.login.entryContrasena.text()) < 3:
            self.login.lbMensaje.setText("Ingrese una contraseña valida")
            self.login.entryContrasena.setFocus()

        else:
            self.login.lbMensaje.setText("")   
            usu = Usuario(correo=self.login.entryCorreo.text(), contrasena=self.login.entryContrasena.text())
            usuDb = UsuarioDb()
            res = usuDb.login(usu)
            if res:
                self.main = MainWindow()
                self.login.hide()
                print(f"Este es el id del usuario logueado: {res.getNombre()}")
                print(f"Usuario logueado con rol: {res.getRol()}")  # Imprimir el rol del usuario
                print("Exito", "Login exitoso")
                self.login.lbMensaje.setText("Login Correcto")  
            else:
                self.login.lbMensaje.setText("Correo o contraseña incorrectos")  
                print("Error", "Correo o contraseña incorrectos")

    def initGui(self):
        self.login.btnLogin.clicked.connect(self.ingresar)
    