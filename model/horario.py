class Horario():
    def __init__(self, id_horario=None, turno="", hora=""):
        self.id_horario = id_horario
        self.turno = turno
        self.hora = hora

    def getId_horario(self):
        return self.id_horario
    
    def setId_horario(self, id_horario):
        self.id_horario = id_horario

    def getTurno(self):
        return self.turno
    
    def setTurno(self, turno):
        self.turno = turno

    def getHora(self):
        return self.hora
    
    def setHora(self, hora):
        self.hora = hora