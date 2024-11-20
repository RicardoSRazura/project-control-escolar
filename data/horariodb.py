import mysql.connector
from mysql.connector import Error
import conexion as con
from model.horario import Horario

class HorarioDb():
    def saveHorario(self, horario:Horario):
        try:
            self.db_con = con.conexion()
            self.conn = self.db_con.open()
            if self.conn is None:
                raise Exception("No se puede conectar a la basae de datos")
            self.cursor = self.conn.cursor()
            self.sql = "INSERT INTO horario (turno, hora) VALUES (%s, %s)"
            self.datos = (horario.getTurno(), horario.getHora())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            lastId = self.cursor.lastrowid
            self.db_con.close()
            print("Datos insertados correctamente")
            return lastId
        except mysql.connector.Error as err:
            print(f"Error al guardar el horario: {err}")
            return None
        # except Exception as e:
        #     print(f"Error: {e}")
    
    def searchHorario(self, id_horario):
        try:
            self.db_con = con.conexion()
            self.conn = self.db_con.open()
            self.cursor = self.conn.cursor(buffered=True)
            self.sql = "SELECT * FROM horario WHERE id_horario = %s"
            self.cursor.execute(self.sql, (id_horario,))
            row = self.cursor.fetchone()
            self.db_con.close()
            if row:
                horario = Horario(row[0], row[1], row[2])
                return horario
            return None
        except mysql.connector.Error as err:
            print(f"Error al buscar el horario: {err}")
            return None
        
    def editHorario(self, horario:Horario):
        try:
            self.db_con = con.conexion()
            self.conn = self.db_con.open()
            self.cursor = self.conn.cursor()
            self.sql = "UPDATE horario SET turno=%s, hora=%s WHERE id_horario=%s"
            self.datos = (horario.getTurno(), horario.getHora(), horario.getId_horario())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            resultado = self.cursor.rowcount > 0
            self.db_con.close()
            return resultado
        except mysql.connector.Error as err:
            print(f"Error al editar el horario: {err}")
            return None

    def removHorario(self, id_horario):
        try:
            self.db_con = con.conexion()
            self.conn = self.db_con.open()
            self.cursor = self.conn.cursor()
            self.sql = "DELETE FROM horario WHERE id_horario=%s"
            self.cursor.execute(self.sql, (id_horario,))
            self.conn.commit()
            resultado = self.cursor.rowcount > 0
            self.db_con.close()
            return resultado
        except mysql.connector.Error as err:
            print(f"Error al eliminar el horario: {err}")
            return None
    
    def getMaxId(self):
        try: 
            self.db_con = con.conexion()
            self.conn = self.db_con.open()
            self.cursor = self.conn.cursor()
            self.sql = "SELECT MAX(id_horario) FROM horario"
            self.cursor.execute(self.sql)
            row = self.cursor.fetchone()
            self.db_con.close()
            return row[0] if row[0] is not None else 0
        except mysql.connector.Error as err:
            print(f"Error al obtener el maximo ID: {err}")
            return 0
        
    
    def exists(self, horario:Horario):
        try:
            self.db_con = con.conexion()
            self.conn = self.db_con.open()
            self.cursor = self.conn.cursor(buffered=True)
            self.sql = "SELECT COUNT(*) FROM horario WHERE turno = %s"
            self.cursor.execute(self.sql, (horario.getTurno(),))
            result = self.cursor.fetchone()
            self.db_con.close()
            return result[0] > 0
        except mysql.connector.Error as err:
            print(f"Error al verificar existencia del turno: {err}")
            return False