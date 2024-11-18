class Salon():
    def __init__(self, id_salon=None, nombre="", edificio=""):
        self.id_salon = id_salon
        self.nombre = nombre
        self.edificio = edificio

    def getId_salon(self):
        return self.id_salon
    
    def setId_salon(self, id_salon):
        self.id_salon = id_salon

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getEdificio(self):
        return self.edificio
    
    def setEdificio(self, edificio):
        self.edificio = edificio