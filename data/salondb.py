import mysql.connector
from mysql.connector import Error
import conexion as con
from model.salon import Salon

class salonDb():
    def saveSalon(self, salon:Salon):
        try:
            self.db_con = con.conexion()
            self.conn = self.db_con.open()
            if self.conn is None:
                raise Exception("No se puede conectar a la basae de datos")
            self.cursor = self.conn.cursor()
            self.sql = "INSERT INTO salon (nombre, edificio) VALUES (%s, %s)"
            self.datos = (salon.getNombre(), salon.getEdificio())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            lastId = self.cursor.lastrowid
            self.db_con.close()
            print("Datos insertados correctamente")
            return lastId
        except mysql.connector.Error as err:
            print(f"Error al guardar el salon: {err}")
            return None
        # except Exception as e:
        #     print(f"Error: {e}")
    
    def searchSalon(self, id_salon):
        try:
            self.db_con = con.conexion()
            self.conn = self.db_con.open()
            self.cursor = self.conn.cursor(buffered=True)
            self.sql = "SELECT * FROM salon WHERE id_salon = %s"
            self.cursor.execute(self.sql, (id_salon,))
            row = self.cursor.fetchone()
            self.db_con.close()
            if row:
                salon = Salon(row[0], row[1], row[2])
                return salon
            return None
        except mysql.connector.Error as err:
            print(f"Error al buscar el salon: {err}")
            return None
        
    def editSalon(self, salon:Salon):
        try:
            self.db_con = con.conexion()
            self.conn = self.db_con.open()
            self.cursor = self.conn.cursor()
            self.sql = "UPDATE salon SET nombre=%s, edificio=%s WHERE id_salon=%s"
            self.datos = (salon.getNombre(), salon.getEdificio(), salon.getId_salon())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            resultado = self.cursor.rowcount > 0
            self.db_con.close()
            return resultado
        except mysql.connector.Error as err:
            print(f"Error al editar el salon: {err}")
            return None

    def removSalon(self, id_salon):
        try:
            self.db_con = con.conexion()
            self.conn = self.db_con.open()
            self.cursor = self.conn.cursor()
            self.sql = "DELETE FROM salon WHERE id_salon=%s"
            self.cursor.execute(self.sql, (id_salon,))
            self.conn.commit()
            resultado = self.cursor.rowcount > 0
            self.db_con.close()
            return resultado
        except mysql.connector.Error as err:
            print(f"Error al eliminar el salon: {err}")
            return None
    
    def getMaxId(self):
        try: 
            self.db_con = con.conexion()
            self.conn = self.db_con.open()
            self.cursor = self.conn.cursor()
            self.sql = "SELECT MAX(id_salon) FROM salon"
            self.cursor.execute(self.sql)
            row = self.cursor.fetchone()
            self.db_con.close()
            return row[0] if row[0] is not None else 0
        except mysql.connector.Error as err:
            print(f"Error al obtener el maximo ID: {err}")
            return 0
        
    
    def exists(self, salon:Salon):
        try:
            self.db_con = con.conexion()
            self.conn = self.db_con.open()
            self.cursor = self.conn.cursor(buffered=True)
            self.sql = "SELECT COUNT(*) FROM salon WHERE nombre = %s"
            self.cursor.execute(self.sql, (salon.getNombre(),))
            result = self.cursor.fetchone()
            self.db_con.close()
            return result[0] > 0
        except mysql.connector.Error as err:
            print(f"Error al verificar existencia del salon: {err}")
            return False