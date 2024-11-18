class Materia():
    def __init__(self, id_materia=None, nombre_asignatura="", creditos=None, semestre="", id_carrera=None, id_horario=None):
        self.id_materia = id_materia
        self.nombre_asignatura = nombre_asignatura
        self.creditos = creditos
        self.semestre = semestre
        self.id_carrera = id_carrera
        self.id_horario = id_horario
        
    def getId_materia(self):
        return self.id_materia
    
    def setId_materia(self, id_materia):
        self.id_materia = id_materia

    def getNombre_asignatura(self):
        return self.nombre_asignatura
    
    def setNombre_asignatura(self, nombre_asignatura):
        self.nombre_asignatura = nombre_asignatura

    def getCreditos(self):
        return self.creditos
    
    def setCreditos(self, creditos):
        self.creditos = creditos

    def getSemestre(self):
        return self.semestre
    
    def setSemestre(self, semestre):
        self.semestre = semestre

    def getId_carrera(self):
        return self.id_carrera
    
    def setId_carrera(self, id_carrera):
        self.id_carrera = id_carrera

    def getId_horario(self):
        return self.id_horario
    
    def setId_horario(self, id_horario):
        self.id_horario = id_horario