import mysql.connector
from mysql.connector import Error

class conexion:
    def __init__(self):
        self.user = "root"
        self.password = ""
        self.database = "control_escolardb"
        self.host = "localhost"
        self.conn = None

    def open(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                database=self.database
            )
            if self.conn.is_connected():
                print("Conexion exitosa a la base de datos")
            return self.conn
        except mysql.connector.Error as err:
            print(f"Error al conectar con la base de datos: {err}")
            return None
    
    def close(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("Conexion cerrada")

# def autenticar(usuario, contraseña):
#     conexion = conectar_mysql()

#     if conexion:
#         try:
#             cursor = conexion.cursor()
#             sql = "SELECT * FROM user WHERE username = %s AND password = %s"
#             cursor.execute(sql, (usuario, contraseña))
#             resultado = cursor.fetchone()

#             if resultado:
#                 estado_usuario = resultado[5]  # Accede al estado del usuario usando un índice numérico
#                 return True, estado_usuario  # Retornamos un booleano de éxito y el estado del usuario
#             else:
#                 return False, None  

#         except mysql.connector.Error as e:
#             messagebox.showerror("Error de MySQL", f"Error: {e}")

#         finally:
#             cursor.close()
#             conexion.close()
