from CuentaCorriente import *
from CuentaAhorro import *

cuenta_corriente1 = CuentaCorriente("Satoru Gojo", 33268752, date(1989,12,7),350000,25000)
cuenta_ahorro1 = CuentaAhorro("Tomás De Donatis", 38588745, date(1994,9,25),10000)

cuenta_corriente1.extraer(30000)
cuenta_corriente1.extraer(15000)
cuenta_corriente1.depositar(5600)

cuenta_ahorro1.calcular_interes()

