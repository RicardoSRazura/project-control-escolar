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
                usuario = Usuario(nombre=row[1], perfil=row[6])
                self.cursor.close()
                self.db_con.close()
                return usuario
            else:
                self.cursor.close()
                self.db_con.close()
                return None
        except mysql.connector.Error as err:
            print("Error", f"Error al conectar con la base de datos: {err}")
    
    def saveUser(self, usuario:Usuario):
        try:
            self.db_con = con.conexion()
            self.conn = self.db_con.open()
            if self.conn is None:
                raise Exception("No se puede conectar a la basae de datos")
            self.cursor = self.conn.cursor()
            self.sql = "INSERT INTO usuarios (nombre, apellidop, apellidom, correo, contrasena, perfil) VALUES (%s, %s, %s, %s, %s, %s)"
            self.datos = (usuario.getNombre(), usuario.getApellidop(), usuario.getApellidom(), usuario.getCorreo(), usuario.getContrasena(), usuario.getPerfil())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            print("Datos insertados correctamente")
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al guardar el usuario: {err}")
        except Exception as e:
            print(f"Error: {e}")
    
    def searchUser(self, usuario:Usuario):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor(buffered=True)
            self.sql = "SELECT * FROM usuarios WHERE id_usuario = %s"
            self.cursor.execute(self.sql, (usuario.getId_usuario,))
            row = self.cursor.fetchone()
            self.con.close()
            if row:
                usuario = Usuario(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                return usuario
            return None
        except mysql.connector.Error as err:
            print(f"Error al buscar el usuario: {err}")
            return None
    def editUser(self, usuario:Usuario):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "UPDATE usuarios SET nombre=%s, apellidop=%s, apellidom%s, correo=%s, contrasena=%s, perfil=%s WHERE id_usuario=%s"
            self.datos = (usuario.getNombre(), usuario.getApellidop(), usuario.getApellidom(), usuario.getCorreo(),usuario.getContrasena(), usuario.getPerfil(), usuario.getId_usuario())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al editar el usuario: {err}")

    def removUser(self, usuario:Usuario):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "DELETE FROM usuarios WHERE id_usuario=%s"
            self.cursor.execute(self.sql, (usuario.getId_usuario(),))
            self.conn.commit()
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al eliminar el usuario: {err}")
    
    def getMaxId(self):
        try: 
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "SELECT MAX(id_usuario) FROM usuarios"
            self.cursor.execute(self.sql)
            row = self.cursor.fetchone()
            self.con.close()
            return row[0] if row[0] is not None else 0
        except mysql.connector.Error as err:
            print(f"Error al obtener el maximo ID: {err}")
            return 0
    
    def exists(self, usuario:Usuario):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor(buffered=True)
            self.sql = "SELECT COUNT(*) FROM usuarios WHERE correo = %s"
            self.cursor.execute(self.sql, (usuario.getCorreo(),))
            result = self.cursor.fetchone()
            self.con.close()
            return result[0] > 0
        except mysql.connector.Error as err:
            print(f"Error al verificar existencia de usuarios: {err}")
            return False