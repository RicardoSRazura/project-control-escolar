from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox

from data.carreradb import CarreraDb
from model.carrera import Carrera

class CarrerasWindow():
    def __init__(self):
        self.carreraWindow = uic.loadUi("interface/carreras.ui")
        self.initGui()

    #Metodos para limpiar los campos
    def limpiarCampos(self):
        self.carreraWindow.entryId.clear()
        self.carreraWindow.entryNombreCarrera.clear()
        self.carreraWindow.entrySemestres.clear()

    def activar(self):
        self.carreraWindow.btnBuscar.setEnabled(True)
        self.carreraWindow.entryBuscarId.setEnabled(True)
        self.carreraWindow.btnNuevo.setEnabled(True)
        self.carreraWindow.btnGuardar.setEnabled(True)
        self.carreraWindow.btnCancelar.setEnabled(True)
        self.carreraWindow.btnEditar.setEnabled(True)     
    
    def nuevaCarrera(self):
        print("Boton 'Nuevo' presionado")
        self.limpiarCampos()
        dbCarrera = CarreraDb()
        nuevoId = dbCarrera.getMaxId() + 1
        self.carreraWindow.entryId.setText(str(nuevoId))

        #Metodos para deshabilitar o habilitar botones
        self.carreraWindow.btnBuscar.setEnabled(False)
        self.carreraWindow.entryBuscarId.setEnabled(False)
        self.carreraWindow.btnNuevo.setEnabled(False)
        self.carreraWindow.btnGuardar.setEnabled(True)
        self.carreraWindow.btnCancelar.setEnabled(True)
        self.carreraWindow.btnEditar.setEnabled(False)
       
        # if self.perfil == "Administrador":
        #     self.btnEliminarUsuario.config(state="disabled")

    
    
    def guardarCarrera(self):
        print("Boton de 'Guardar' presionado")
        carre = Carrera(
            nombre=self.carreraWindow.entryNombreCarrera.text(),
            semestres=int(self.carreraWindow.entryApellidoP.text()),
            
        )
        dbCarrera = CarreraDb()
        res = dbCarrera.saveCarrera(carre)
        if res:
            print("Exito, Carrera registrada con exito")
        else:
            print("Error, Carrera no registrada")

    def cancelar(self):
        self.limpiarCampos()
        self.activar()
    
    def editarCarrera(self):
        print("Boton de 'Editar' presionado")
        carre = Carrera(
            id_carrera=int(self.carreraWindow.entryId.text()),
            nombre=self.carreraWindow.entryNombreCarrera.text(),
            semestres=int(self.carreraWindow.entrySemestres.text()),
        )
        dbCarrera = CarreraDb()
        res = dbCarrera.editCarrera(carre)
        if res:
            print("Exito, la carrera se ha editado correctamente")
        else:
            print("Error, la carrera no se ha editado")
        self.limpiarCampos()
        self.activar()
    
    def eliminarCarrera(self):
        idCarrera = int(self.carreraWindow.entryId.text())
        dbCarrera = CarreraDb()
        res = dbCarrera.removCarrera(idCarrera)
        if res:
            print("Exito, Carrera eliminada correctamente")
        else:
            print("Error, la carrera no se ha podido eliminar")
        self.limpiarCampos()
        self.activar()

    def buscarCarrera(self):
        idCarrera = int(self.carreraWindow.entryBuscarId.text())
        dbCarrera = CarreraDb()
        res = dbCarrera.searchCarrera(idCarrera)
        if res:
            self.carreraWindow.entryId.setText(res.getId_carrera())
            self.carreraWindow.entryNombreCarrera.setText(res.getNombre())
            self.carreraWindow.entrySemestres.setText(res.getSemestres())

            print("Exito, Carrera encontrada correctamente")
        
        else:
            print("Error, Carrera no encontrada")
            

    
    def initGui(self):
        self.carreraWindow.btnNuevo.clicked.connect(self.nuevaCarrera)
        self.carreraWindow.btnGuardar.clicked.connect(self.guardarCarrera)
        self.carreraWindow.btnEditar.clicked.connect(self.editarCarrera)
        self.carreraWindow.btnEliminar.clicked.connect(self.eliminarCarrera)
        self.carreraWindow.btnCancelar.clicked.connect(self.cancelar)
        self.carreraWindow.btnBuscar.clicked.connect(self.buscarCarrera)


        
