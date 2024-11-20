from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox

from data.salondb import salonDb
from model.salon import Salon

class AulasWindow():
    def __init__(self):
        self.aulasWindow = uic.loadUi("interface/aulas.ui")
        self.initGui()

    #Metodos para limpiar los campos
    def limpiarCampos(self):
        self.aulasWindow.entryId.clear()
        self.aulasWindow.entrySalon.clear()
        self.aulasWindow.entryEdificio.clear()

    def activar(self):
        self.aulasWindow.btnBuscar.setEnabled(True)
        self.aulasWindow.entryBuscarId.setEnabled(True)
        self.aulasWindow.btnNuevo.setEnabled(True)
        self.aulasWindow.btnGuardar.setEnabled(True)
        self.aulasWindow.btnCancelar.setEnabled(True)
        self.aulasWindow.btnEditar.setEnabled(True)     
    
    def nuevaAula(self):
        print("Boton 'Nuevo' presionado")
        self.limpiarCampos()
        dbSalon = salonDb()
        nuevoId = dbSalon.getMaxId() + 1
        self.aulasWindow.entryId.setText(str(nuevoId))

        #Metodos para deshabilitar o habilitar botones
        self.aulasWindow.btnBuscar.setEnabled(False)
        self.aulasWindow.entryBuscarId.setEnabled(False)
        self.aulasWindow.btnNuevo.setEnabled(False)
        self.aulasWindow.btnGuardar.setEnabled(True)
        self.aulasWindow.btnCancelar.setEnabled(True)
        self.aulasWindow.btnEditar.setEnabled(False)
       
        # if self.perfil == "Administrador":
        #     self.btnEliminarUsuario.config(state="disabled")

    def guardarAula(self):
        print("Boton de 'Guardar' presionado")
        aula = Salon(
            nombre=self.aulasWindow.entrySalon.text(),
            edificio=self.aulasWindow.entryEdificio.text(),
            
        )
        dbAula = salonDb()
        res = dbAula.saveSalon(aula)
        if res:
            print("Exito, Aula registrada con exito")
        else:
            print("Error, Aula no registrada")

    def cancelar(self):
        self.limpiarCampos()
        self.activar()
    
    def editarAula(self):
        print("Boton de 'Editar' presionado")
        aula = Salon(
            id_salon=int(self.aulasWindow.entryId.text()),
            nombre=self.aulasWindow.entrySalon.text(),
            edificio=self.aulasWindow.entryEdificio.text()
        )
        dbAula = salonDb()
        res = dbAula.editSalon(aula)
        if res:
            print("Exito, el Aula se ha editado correctamente")
        else:
            print("Error, el Aula no se ha editado")
        self.limpiarCampos()
        self.activar()
    
    def eliminarAula(self):
        idAula = int(self.aulasWindow.entryId.text())
        dbAula = salonDb()
        res = dbAula.removSalon(idAula)
        if res:
            print("Exito, Aula eliminada correctamente")
        else:
            print("Error, el aula no se ha podido eliminar")
        self.limpiarCampos()
        self.activar()

    def buscarAula(self):
        idAula = int(self.aulasWindow.entryBuscarId.text())
        dbAula = salonDb()
        res = dbAula.searchSalon(idAula)
        if res:
            self.aulasWindow.entryId.setText(res.getId_salon())
            self.aulasWindow.entrySalon.setText(res.getNombre())
            self.aulasWindow.entryEdificio.setText(res.getEdificio())

            print("Exito, Aula encontrada correctamente")
        
        else:
            print("Error, Aula no encontrada")
            
    def initGui(self):
        self.aulasWindow.btnNuevo.clicked.connect(self.nuevaAula)
        self.aulasWindow.btnGuardar.clicked.connect(self.guardarAula)
        self.aulasWindow.btnEditar.clicked.connect(self.editarAula)
        self.aulasWindow.btnEliminar.clicked.connect(self.eliminarAula)
        self.aulasWindow.btnCancelar.clicked.connect(self.cancelar)
        self.aulasWindow.btnBuscar.clicked.connect(self.buscarAula)


        
