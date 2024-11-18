class Alumno():
    def __init__(self, id_alumno=None, id_carrera=None, id_usuario=None, id_materia=None, id_grupo=None):
        self.id_alumno = id_alumno
        self.id_carrera = id_carrera
        self.id_usuario = id_usuario
        self.id_materia = id_materia
        self.id_grupo = id_grupo

    def getId_alumno(self):
        return self.id_alumno
    
    def setId_alumno(self, id_alumno):
        self.id_alumno = id_alumno

    def getId_carrera(self):
        return self.id_carrera
    
    def setId_carrera(self, id_carrera):
        self.id_carrera = id_carrera

    def getId_usuario(self):
        return self.id_usuario
    
    def setId_usuario(self, id_usuario):
        self.id_usuario = id_usuario

    def getId_materia(self):
        return self.id_materia
    
    def setId_materia(self, id_materia):
        self.id_materia = id_materia

    def getId_grupo(self):
        return self.id_grupo
    
    def setId_grupo(self, id_grupo):
        self.id_grupo = id_grupo