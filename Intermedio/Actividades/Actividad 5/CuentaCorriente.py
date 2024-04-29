from CuentaBancaria import *

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0,limite_extraccion = 500):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._limite_extraccion = limite_extraccion
    
    def obtener_limite_extraccion(self):
        return self._limite_extraccion
    
    def extraer(self, monto):
        if monto <= self.obtener_saldo() and monto <= self.obtener_limite_extraccion():
            self.modificar_saldo(-monto)
            print(f"Se ha extraido ${monto} a la cuenta corriente de {self.obtener_nombre()}, su saldo es de: ${self.obtener_saldo()}")
        else:
            if monto > self.obtener_limite_extraccion():
                print("Usted no puede extraer ese monto")
            else:
                print("Usted no posee saldo suficiente para realizar la operación")
    
    def depositar(self,monto):
        if monto > 0:
            super().modificar_saldo(monto)
            print(f"Se ha depositado ${monto} a la cuenta corriente de {self.obtener_nombre()}, su saldo es de: ${self.obtener_saldo()}")
        else:
            print("El monto a depositar debe ser mayor a 0")