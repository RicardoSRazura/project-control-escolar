import mysql.connector
from mysql.connector import Error
import conexion as con
from model.carrera import Carrera

class CarreraDb():
    def saveCarrera(self, carrera:Carrera):
        try:
            self.db_con = con.conexion()
            self.conn = self.db_con.open()
            if self.conn is None:
                raise Exception("No se puede conectar a la basae de datos")
            self.cursor = self.conn.cursor()
            self.sql = "INSERT INTO carrera (nombre, semestres) VALUES (%s, %s)"
            self.datos = (carrera.getNombre(), carrera.getSemestres())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            lastId = self.cursor.lastrowid
            self.db_con.close()
            print("Datos insertados correctamente")
            return lastId
        except mysql.connector.Error as err:
            print(f"Error al guardar la carrera: {err}")
            return None
        # except Exception as e:
        #     print(f"Error: {e}")
    
    def searchCarrera(self, id_carrera):
        try:
            self.db_con = con.conexion()
            self.conn = self.db_con.open()
            self.cursor = self.conn.cursor(buffered=True)
            self.sql = "SELECT * FROM carrera WHERE id_carrera = %s"
            self.cursor.execute(self.sql, (id_carrera,))
            row = self.cursor.fetchone()
            self.db_con.close()
            if row:
                carrera = Carrera(row[0], row[1], row[2])
                return carrera
            return None
        except mysql.connector.Error as err:
            print(f"Error al buscar la carrera: {err}")
            return None
        
    def editUser(self, carrera:Carrera):
        try:
            self.db_con = con.conexion()
            self.conn = self.db_con.open()
            self.cursor = self.conn.cursor()
            self.sql = "UPDATE carrera SET nombre=%s, semestres=%s WHERE id_carrera=%s"
            self.datos = (carrera.getNombre(), carrera.getSemestres(), carrera.getId_carrera())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            resultado = self.cursor.rowcount > 0
            self.db_con.close()
            return resultado
        except mysql.connector.Error as err:
            print(f"Error al editar la carrera: {err}")
            return None

    def removUser(self, id_carrera):
        try:
            self.db_con = con.conexion()
            self.conn = self.db_con.open()
            self.cursor = self.conn.cursor()
            self.sql = "DELETE FROM carrera WHERE id_carrera=%s"
            self.cursor.execute(self.sql, (id_carrera,))
            self.conn.commit()
            resultado = self.cursor.rowcount > 0
            self.db_con.close()
            return resultado
        except mysql.connector.Error as err:
            print(f"Error al eliminar la carrera: {err}")
            return None
    
    def getMaxId(self):
        try: 
            self.db_con = con.conexion()
            self.conn = self.db_con.open()
            self.cursor = self.conn.cursor()
            self.sql = "SELECT MAX(id_carrera) FROM carrera"
            self.cursor.execute(self.sql)
            row = self.cursor.fetchone()
            self.db_con.close()
            return row[0] if row[0] is not None else 0
        except mysql.connector.Error as err:
            print(f"Error al obtener el maximo ID: {err}")
            return 0
        
    
    def exists(self, carrera:Carrera):
        try:
            self.db_con = con.conexion()
            self.conn = self.db_con.open()
            self.cursor = self.conn.cursor(buffered=True)
            self.sql = "SELECT COUNT(*) FROM carrera WHERE nombre = %s"
            self.cursor.execute(self.sql, (carrera.getNombre(),))
            result = self.cursor.fetchone()
            self.db_con.close()
            return result[0] > 0
        except mysql.connector.Error as err:
            print(f"Error al verificar existencia de carrera: {err}")
            return False