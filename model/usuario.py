class Usuario():
    def __init__(self, id_usuario=None, nombre="", apellidop="", apellidom="", correo="", contrasena="", perfil=""):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellidop = apellidop
        self.apellidom = apellidom
        self.correo = correo
        self.contrasena = contrasena
        self.perfil = perfil

    def getId_usuario(self):
        return self.id_usuario
    
    def setId_usuario(self, id_usuario):
        self.id_usuario = id_usuario

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getApellidop(self):
        return self.apellidop
    
    def setApellidop(self, apellidop):
        self.apellidop = apellidop

    def getApellidom(self):
        return self.apellidom
    
    def setApellidom(self, apellidom):
        self.apellidom = apellidom

    def getCorreo(self):
        return self.correo
    
    def setCorreo(self, correo):
        self.correo = correo

    def getContrasena(self):
        return self.contrasena
    
    def setContrasena(self, contrasena):
        self.contrasena = contrasena

    def getPerfil(self):
        return self.perfil
    
    def setPerfil(self, perfil):
        self.perfil = perfil