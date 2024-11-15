from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox

from data.usuariodb import UsuarioDb
from model.usuario import Usuario



class UsuariosWindow():
    def __init__(self):
        self.userWindow = uic.loadUi("interface/usuarios.ui")
        self.initGui()

    #Metodos para limpiar los campos
    def limpiarCampos(self):
        self.userWindow.entryId.clear()
        self.userWindow.entryNombre.clear()
        self.userWindow.entryApellidoP.clear()
        self.userWindow.entryApellidoM.clear()
        self.userWindow.entryCorreo.clear()
        self.userWindow.entryContrasena.clear()
        self.userWindow.cbPerfil.setCurrentIndex(0)

    def activar(self):
        self.userWindow.btnBuscar.setEnabled(True)
        self.userWindow.entryBuscarId.setEnabled(True)
        self.userWindow.btnNuevo.setEnabled(True)
        self.userWindow.btnGuardar.setEnabled(True)
        self.userWindow.btnCancelar.setEnabled(True)
        self.userWindow.btnEditar.setEnabled(True)     
    
    def nuevoUser(self):
        print("Boton 'Nuevo' presionado")
        self.limpiarCampos()
        dbUsuario = UsuarioDb()
        nuevoId = dbUsuario.getMaxId() + 1
        self.userWindow.entryId.setText(str(nuevoId))

        #Metodos para deshabilitar o habilitar botones
        self.userWindow.btnBuscar.setEnabled(False)
        self.userWindow.entryBuscarId.setEnabled(False)
        self.userWindow.btnNuevo.setEnabled(False)
        self.userWindow.btnGuardar.setEnabled(True)
        self.userWindow.btnCancelar.setEnabled(True)
        self.userWindow.btnEditar.setEnabled(False)
       
        # if self.perfil == "Administrador":
        #     self.btnEliminarUsuario.config(state="disabled")

    
    
    def guardarUser(self):
        print("Boton de 'Guardar' presionado")
        user = Usuario(
            nombre=self.userWindow.entryNombre.text(),
            apellidop=self.userWindow.entryApellidoP.text(),
            apellidom=self.userWindow.entryApellidoM.text(),
            correo=self.userWindow.entryCorreo.text(),
            contrasena=self.userWindow.entryContrasena.text(),
            perfil=self.userWindow.cbPerfil.currentText()
        )
        userDb = UsuarioDb()
        res = userDb.saveUser(user)
        if res:
            print("Exito, Usuario resgitrado con exito")
        else:
            print("Error, Usuario no registrado")

    def cancelar(self):
        self.limpiarCampos()
        self.activar()
    
    def editarUser(self):
        print("Boton de 'Editar' presionado")
        user = Usuario(
            id_usuario=self.userWindow.entryId.text(),
            nombre=self.userWindow.entryNombre.text(),
            apellidop=self.userWindow.entryApellidoP.text(),
            apellidom=self.userWindow.entryApellidoM.text(),
            correo=self.userWindow.entryCorreo.text(),
            contrasena=self.userWindow.entryContrasena.text(),
            perfil=self.userWindow.cbPerfil.currentText()
        )
        userDb = UsuarioDb()
        res = userDb.editUser(user)
        if res:
            print("Exito, el usuario se ha editado correctamente")
        else:
            print("Error, el usuario no se ha editado")
        self.limpiarCampos()
        self.activar()
    
    def eliminarUser(self):
        idUser = self.userWindow.entryId.text()
        userDb = UsuarioDb()
        res = userDb.removUser(idUser)
        if res:
            print("Exito, Usuario eliminado correctamente")
        else:
            print("Error, el usuario no se ha podido eliminar")
        self.limpiarCampos()
        self.activar()

    def buscarUser(self):
        idUser = self.userWindow.entryBuscarId.text()
        userDb = UsuarioDb()
        res = userDb.searchUser(idUser)
        if res:
            self.userWindow.entryId.setText(str(res.getId_usuario()))
            self.userWindow.entryNombre.setText(res.getNombre())
            self.userWindow.entryApellidoP.setText(res.getApellidop())
            self.userWindow.entryApellidoM.setText(res.getApellidom())
            self.userWindow.entryCorreo.setText(res.getCorreo())
            self.userWindow.entryContrasena.setText(res.getContrasena())
            
            # Establece el perfil en el QComboBox
            index = self.userWindow.cbPerfil.findText(res.getPerfil())
            if index >= 0:
                self.userWindow.cbPerfil.setCurrentIndex(index)

            print("Exito, Usuario encontrado correctamente")
        
        else:
            print("Error, usuario no encontrado")
            

    
    def initGui(self):
        self.userWindow.btnNuevo.clicked.connect(self.nuevoUser)
        self.userWindow.btnGuardar.clicked.connect(self.guardarUser)
        self.userWindow.btnEditar.clicked.connect(self.editarUser)
        self.userWindow.btnEliminar.clicked.connect(self.eliminarUser)
        self.userWindow.btnCancelar.clicked.connect(self.cancelar)
        self.userWindow.btnBuscar.clicked.connect(self.buscarUser)


        
