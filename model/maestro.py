class Maestro():
    def __init__(self, id_maestro=None, id_materia=None, id_usuario=None):
        self.id_maestro = id_maestro
        self.id_materia = id_materia
        self.id_usuario = id_usuario
        

    def getId_maestro(self):
        return self.id_maestro
    
    def setId_maestro(self, id_maestro):
        self.id_maestro = id_maestro

    def getId_materia(self):
        return self.id_materia
    
    def setId_materia(self, id_materia):
        self.id_materia= id_materia

    def getId_usuario(self):
        return self.usuario_id
    
    def setId_usuario(self, usuario_id):
        self.usuario_id = usuario_id

    