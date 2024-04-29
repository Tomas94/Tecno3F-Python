# Ejercicios Excepciones. De Donatis, Tomás.


#Ejercicio 1
# Escribe un programa que intente dividir dos números.
# Si el segundo número es cero, captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.

# Cuando llegué al ejercicio 5 me di cuenta que lo que hice en este ejercicio era lo mismo, ya que desde el inicio estaba cubriendo la posibilidad de que se ingresara un valor no valido.
# Así que el ejercicio 1 y el 5 son practicamente iguales, acá le saco el ultimo except que hace la diferencia.


print("Ingrese el primer numero entero.");
primer_numero = input();
print("Ingrese el segundo numero entero.");
segundo_numero = input();

try:
    resultado_division = int(primer_numero) / int(segundo_numero);
    print(f"Operacion realizada con exito, el resultado es {resultado_division}")
except ZeroDivisionError:
    print("Ha ocurrido un error, no puede dividirse por cero.");

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Ejercicio 2
# Escribe un programa que intente sumar un número y una cadena.
# Si se produce un error de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.

# print("Ingrese un numero entero.");
# numero = input();
# print("Ingrese una cadena de texto.");
# cadena = input();

# try:
#     suma = int(numero) + cadena;
#     print(f"Operacion realizada con exito, el resultado es {suma}");
# except TypeError:
#     print("Ha habido un error de tipo, no pueden sumarse datos numericos con cadenas.");
# except ValueError:
#    print("Se ha ingresado una cadena o un numero no entero cuando se solicito un numero.");

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Ejercicio 3
# Escribe un programa que intente acceder a una clave que no existe en un diccionario.
# Si se produce una excepción KeyError, captura la excepción y muestra un mensaje de error al usuario.

#mi_dicccionario = {"Nombre" : "Tomás" , "Apellido" : "De Donatis", "Edad" : "29"};

# try:
#      print("El numero de telefono solicitado es:", mi_dicccionario["Telefono"]);
# except KeyError:
#      print("Error, no existe la clave solicitada");

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Ejercicio 4
# Escribe un programa que intente abrir un archivo que no existe.
# Si se produce una excepción FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario.
# Sin embargo, también intenta crear el archivo si no existe.

# No habia visto nada sobre manejo de archivos hasta ahora, así que investigando por internet llegué a algo así, aunque aún no termino de entenderlo del todo el manejo de archivos,
# como por ejemplo, hacer que el .txt se cree en la misma carpeta que el script.

# print("Indique el nombre del archivo que desea abrir");
# archivo = input() + ".txt"

# try:
#     archivo_texto = open(archivo, "r");
#     print("Archivo abierto exitosamente");
# except FileNotFoundError:
#     print("El archivo al que intentas acceder no existe")
#     print("Intentando crear el archivo");
#     try:
#         archivo_texto = open(archivo, "x");
#         print("Archivo creado con exito " + archivo_texto.name);
#     except Exception:
#         print("Error al querer crear un archivo nuevo");

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Ejercicio 5
#Escribe un programa que intente dividir dos números.
#Si el segundo número es cero, captura la excepción ZeroDivisionError.
#Si el primer número es un número no válido, captura la excepción ValueError.
#En cualquier caso, muestra un mensaje de error al usuario.

# print("Ingrese el primer numero entero.");
# primer_numero = input();
# print("Ingrese el segundo numero entero.");
# segundo_numero = input();

# try:
#     resultado_division = int(primer_numero) / int(segundo_numero);
#     print(f"Operacion realizada con exito, el resultado es {resultado_division}")
# except ZeroDivisionError:
#     print("Ha ocurrido un error, no puede dividirse por cero.");
# except ValueError:
#     print("Uno de los valores ingresados no es un numero entero.");
