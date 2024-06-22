from .conneciondb import ConnectionDB

def crear_tabla():
    conn = ConnectionDB()
    
    sql= '''
            CREATE TABLE IF NOT EXISTS "Genero" (
	        "id_genero"	INTEGER NOT NULL UNIQUE,
	        "genero"	VARCHAR NOT NULL UNIQUE,
	        PRIMARY KEY("id_genero" AUTOINCREMENT)
            );
            
            CREATE TABLE IF NOT EXISTS "Nacionalidad" (
	        "id"	INTEGER NOT NULL UNIQUE,
	        "nombre"	VARCHAR(50) NOT NULL UNIQUE,
	        PRIMARY KEY("id" AUTOINCREMENT)
            );
            
            CREATE TABLE IF NOT EXISTS "Pacientes" (
	        "id_paciente"	INTEGER NOT NULL UNIQUE,
	        "nombre"	VARCHAR(50) NOT NULL,
	        "apellido"	VARCHAR(50) NOT NULL,
	        "edad"	INTEGER NOT NULL,
	        "sexo"	INTEGER NOT NULL,
	        "documento"	INTEGER NOT NULL UNIQUE,
	        "nacionalidad"	INTEGER NOT NULL,
	        PRIMARY KEY("id_paciente" AUTOINCREMENT),
	        FOREIGN KEY("sexo") REFERENCES "Genero"("id_genero"),
	        FOREIGN KEY("nacionalidad") REFERENCES "Nacionalidad"("id")
            );
            '''
    try:
        conn.cursor.execute(sql)
        conn.close_conection()
    except:
        pass
    
class Pacientes:
    def __init__(self,nombre,apellido,documento,edad,sexo,nacionalidad):
        self.id_pacientes = None
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.edad = edad
        self.sexo = sexo
        self.nacionalidad = nacionalidad
        
    def __str__(self):
        return f'Paciente[{self.nombre},{self.apellido},{self.edad},{self.documento},{self.sexo},{self.nacionalidad}]'
    
def guardar_paciente(paciente:Pacientes):
    conn = ConnectionDB()
    
    sql= f"""
            INSERT INTO Pacientes (nombre,apellido,edad,sexo,documento,nacionalidad)
            VALUES('{paciente.nombre}','{paciente.apellido}','{paciente.edad}','{paciente.sexo}','{paciente.documento}','{paciente.nacionalidad}')
        """
        
    conn.cursor.execute(sql)
    conn.close_conection()
    
def list_pacientes():
    conn=ConnectionDB()
    lista_pacientes=[]
    
    sql="""
        SELECT * FROM Pacientes as p
        INNER JOIN Genero as g
        ON p.sexo = g.id_genero
        INNER JOIN Nacionalidad as n
        ON p.nacionalidad = n.id
    """
    
    try:
        conn.cursor.execute(sql)
        lista_pacientes = conn.cursor.fetchall()
        conn.close_conection()
        
        return lista_pacientes
    except:
        pass
    
def list_sexos():
    conn=ConnectionDB()
    lista_sexos=[]
    sql="""
        SELECT * FROM Genero
    """
    
    try:
        conn.cursor.execute(sql)
        lista_sexos = conn.cursor.fetchall()
        conn.close_conection()
        
        return lista_sexos
    except:
        pass

def list_nacionalidades():
    conn=ConnectionDB()
    lista_nacionalidades=[]
    sql="""
        SELECT * FROM Nacionalidad
    """
    
    try:
        conn.cursor.execute(sql)
        lista_nacionalidades = conn.cursor.fetchall()
        conn.close_conection()
        
        return lista_nacionalidades
    except:
        pass
    
def editar_registro(paciente:Pacientes, id):
    
    conn=ConnectionDB()
    
    sql=f"""
        UPDATE pacientes
        SET nombre = '{paciente.nombre}', apellido = '{paciente.apellido}', edad = '{paciente.edad}', documento= '{paciente.documento}', sexo = '{paciente.sexo}',
        nacionalidad = '{paciente.nacionalidad}'
        WHERE id_paciente = {id};       
    """
    
    conn.cursor.execute(sql)
    conn.close_conection()
    
def borrar_paciente(id):
    conn=ConnectionDB()
    
    sql=f"""
        DELETE FROM pacientes
        WHERE id_paciente = {id};       
    """
    
    conn.cursor.execute(sql)
    conn.close_conection()