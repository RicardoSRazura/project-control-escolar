from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox

from data.horariodb import HorarioDb
from model.horario import Horario

class HorariosWindow():
    def __init__(self):
        self.horarioWindow = uic.loadUi("interface/horarios.ui")
        self.initGui()

    #Metodos para limpiar los campos
    def limpiarCampos(self):
        self.horarioWindow.entryId.clear()
        self.horarioWindow.cbTurno.setCurrentIndex(0)
        self.horarioWindow.entryHora.clear()
      


    def activar(self):
        self.horarioWindow.btnBuscar.setEnabled(True)
        self.horarioWindow.entryBuscarId.setEnabled(True)
        self.horarioWindow.btnNuevo.setEnabled(True)
        self.horarioWindow.btnGuardar.setEnabled(True)
        self.horarioWindow.btnCancelar.setEnabled(True)
        self.horarioWindow.btnEditar.setEnabled(True)     
    
    def nuevaHorario(self):
        print("Boton 'Nuevo' presionado")
        self.limpiarCampos()
        dbHorario = HorarioDb()
        nuevoId = dbHorario.getMaxId() + 1
        self.horarioWindow.entryId.setText(str(nuevoId))

        #Metodos para deshabilitar o habilitar botones
        self.horarioWindow.btnBuscar.setEnabled(False)
        self.horarioWindow.entryBuscarId.setEnabled(False)
        self.horarioWindow.btnNuevo.setEnabled(False)
        self.horarioWindow.btnGuardar.setEnabled(True)
        self.horarioWindow.btnCancelar.setEnabled(True)
        self.horarioWindow.btnEditar.setEnabled(False)
       
        # if self.perfil == "Administrador":
        #     self.btnEliminarUsuario.config(state="disabled")

    
    
    def guardarHorario(self):
        print("Boton de 'Guardar' presionado")
        hora = Horario(
            turno=self.horarioWindow.cbTurno.currentText(),
            hora=self.horarioWindow.entryHora.text()
        )
        dbHorario = HorarioDb()
        res = dbHorario.saveHorario(hora)
        if res:
            print("Exito, Horario registrado con exito")
        else:
            print("Error, Horario no registrado")

    def cancelar(self):
        self.limpiarCampos()
        self.activar()
    
    def editarHorario(self):
        print("Boton de 'Editar' presionado")
        hora = Horario(
            id_horario=int(self.horarioWindow.entryId.text()),
            turno=self.horarioWindow.cbTurno.currentText(),
            hora=self.horarioWindow.entryHora.text()
        )
        dbHorario = HorarioDb()
        res = dbHorario.editHorario(hora)
        if res:
            print("Exito, el horario se ha editado correctamente")
        else:
            print("Error, el horario no se ha editado")
        self.limpiarCampos()
        self.activar()
    
    def eliminarHorario(self):
        idHorario = int(self.horarioWindow.entryId.text())
        dbHorario = HorarioDb()
        res = dbHorario.removHorario(idHorario)
        if res:
            print("Exito, Horario eliminado correctamente")
        else:
            print("Error, el horario no se ha podido eliminar")
        self.limpiarCampos()
        self.activar()

    def buscarHorario(self):
        idHorario = int(self.horarioWindow.entryBuscarId.text())
        dbHorario = HorarioDb()
        res = dbHorario.searchHorario(idHorario)
        if res:
            self.horarioWindow.entryId.setText(res.getId_horario())
            index = self.horarioWindow.cbTurno.findText(res.getTurno())
            if index >= 0:
                self.horarioWindow.cbTurno.setCurrentIndex(index)
            self.horarioWindow.entryHora.setText(res.getHora())

            print("Exito, Horario encontrado correctamente")
        
        else:
            print("Error, Horario no encontrada")
            

    
    def initGui(self):
        self.horarioWindow.btnNuevo.clicked.connect(self.nuevaHorario)
        self.horarioWindow.btnGuardar.clicked.connect(self.guardarHorario)
        self.horarioWindow.btnEditar.clicked.connect(self.editarHorario)
        self.horarioWindow.btnEliminar.clicked.connect(self.eliminarHorario)
        self.horarioWindow.btnCancelar.clicked.connect(self.cancelar)
        self.horarioWindow.btnBuscar.clicked.connect(self.buscarHorario)


        
