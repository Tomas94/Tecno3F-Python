import random

# 1 - Calcular el mayor de dos números ingresados por teclado usando un operador ternario
'''''
while True:
    try:
        print("Ingresa el primer nuemro")
        numero1 = int(input())
        print("Ingresa el segundo nuemro")
        numero2 = int(input())
        break
    except ValueError:
        print("Alguno de los numeros no es valido.")
        
numero_mayor = numero1 if numero1 > numero2 else numero2 if numero2 >numero1 else "ninguno"

print(f"El numero mayor entre los dos es {numero_mayor}") 
'''''

# Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario

'''''
def buscar_palabra_en_lista (palabra, *args):
    
    palabra_buscada = f"{palabra} esta en la lista de args" if palabra in args else f"{palabra} no esta en la lista"
    return palabra_buscada

lista_palabras =[]

while True:
    print("Ingrese una palabra que desea agregar a la lista de palabras o presionte enter para dejar de agregar")
    palabra= input()
    if palabra == "":
        break
    lista_palabras.append(palabra)   

print("Ingrese la palabra que desea buscar.")
palabra_buscada = input()

print(buscar_palabra_en_lista(palabra_buscada,*lista_palabras))

'''''

# Determinar si un número es par o impar

'''''
print("Ingresa un numero entero.")
numero = int(input())

print(f"{numero} es par" if numero%2 == 0 else f"{numero} es impar")

'''''

# Calcular el promedio de una lista de números usando args y un operador ternario

'''''

def promedio_numeros(*args):
    return sum(args)/len(args)

lista_de_numeros = []

for i in range(10):
    numero_aleatorio = random.randint(0,100)
    lista_de_numeros.append(numero_aleatorio)

print(lista_de_numeros)

resultado = promedio_numeros(*lista_de_numeros)

print("El promedio es mayor a 50:" if resultado > 50 else "El promedio es menor a 50:", resultado)

'''''

# Imprimir un mensaje de error si no se pasan suficientes argumentos

# def funcion(argumento1, *args):
#     print(f"Arguemnto 1 : {argumento1}, Args: {args}")

# try:
#     funcion("hola")
# except Exception as e:
#     print("Error de tipo:", e)

texto = "hola"

print(texto[-1])