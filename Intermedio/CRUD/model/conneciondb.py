import sqlite3

class ConnectionDB():
    def __init__(self):
        self.base_datos = 'ddbb/CRUD_BBDD.db'
        self.conection = sqlite3.connect(self.base_datos)
        self.cursor = self.conection.cursor()
    
    def close_conection(self):
        self.conection.commit()
        self.conection.close()
        
    