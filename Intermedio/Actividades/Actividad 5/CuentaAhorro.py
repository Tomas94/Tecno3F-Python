from CuentaBancaria import *

class CuentaAhorro(CuentaBancaria):
    
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._tasa_interes = 0.001
        
    def obtener_tasa_interes(self):
        return self._tasa_interes    
        
    def calcular_interes(self):
        interes_generado = self.obtener_saldo() * self.obtener_tasa_interes()
        print(f"El interes generado mensualmente con tu saldo de ${self.obtener_saldo()} es de ${interes_generado}.")
        
    def extraer(self, monto):
        return super().extraer(monto)
    
    def depositar(self, monto):
        return super().depositar(monto)    