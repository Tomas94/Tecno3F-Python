from abc import ABC , abstractmethod
from datetime import date

class CuentaBancaria(ABC):
    def __init__(self,nombre_titular,dni_titular, fecha_nacimiento, saldo=0):
        self._nombre_titular = nombre_titular       #atributo privado
        self._dni_titular = dni_titular             #atributo privado
        self._fecha_nacimiento = fecha_nacimiento   #atributo privado
        self._saldo = saldo                         #atributo privado


    def obtener_nombre(self):
        return self._nombre_titular

    def obtener_fecha_nacimiento(self):
        return self._fecha_nacimiento
    
    def obtener_edad(self):
        return self._calcular_edad()
    
    def obtener_dni(self):
        return self._dni_titular
        
    def obtener_saldo(self):
        return self._saldo
    
    def modificar_saldo(self,value):
        self._saldo += value
    
     
    @abstractmethod
    def depositar(self,monto):
        pass

    @abstractmethod
    def extraer(self,monto):
        pass

    def _calcular_edad(self):
        fecha_actual = date.today()
        edad = fecha_actual - self.obtener_fecha_nacimiento()
        return edad.days // 365