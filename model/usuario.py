class Usuario():
    def __init__(self, id_usuario=None, nombre="", correo="", contrasena="", rol=""):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol

    def getId_usuario(self):
        return self.id_usuario
    
    def setId_usuario(self, id_usuario):
        self.id_usuario = id_usuario

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getCorreo(self):
        return self.correo
    
    def setCorreo(self, correo):
        self.correo = correo

    def getContrasena(self):
        return self.contrasena
    
    def setContrasena(self, contrasena):
        self.contrasena = contrasena

    def getRol(self):
        return self.rol
    
    def setRol(self, rol):
        self.rol = rol