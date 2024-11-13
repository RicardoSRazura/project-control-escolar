import mysql.connector
from mysql.connector import Error
import conexion as con
from model.usuario import Usuario

class UsuarioDb():
    def login(self, usuario:Usuario):
        try:
            self.db_con = con.conexion()
            self.conn = self.db_con.open()
            if self.conn is None:
                raise Exception("No se pudo conectar a la base de datos")
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM usuarios WHERE correo=%s AND contrasena=%s", (usuario.getCorreo(), usuario.getContrasena()))
            row = self.cursor.fetchone()
            # self.db_con.close()
            if row:
                usuario = Usuario(nombre=row[1], rol=row[6])
                self.cursor.close()
                self.db_con.close()
                return usuario
            else:
                self.cursor.close()
                self.db_con.close()
                return None
        except mysql.connector.Error as err:
            print("Error", f"Error al conectar con la base de datos: {err}")