class Carrera():
    def __init__(self, id_carrera=None, nombre="", semestres=None):
        self.id_carrera = id_carrera
        self.nombre = nombre
        self.semestres = semestres

    def getId_carrera(self):
        return self.id_carrera
    
    def setId_carrera(self, id_carrera):
        self.id_carrera = id_carrera

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getSemestres(self):
        return self.semestres
    
    def setSemestres(self, semestres):
        self.semestres = semestres