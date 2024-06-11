import secrets, string, sys, os

diccionario = {
  'letras': string.ascii_letters,
  'numeros': string.digits,
  'caracteres': string.punctuation
}

#Metodo que muestra el menu de inicio, donde se ingresan la cantidad de caracteres y el tipo de contraseña deseada
def menu_inicio():
    os.system("cls")
    
    print("||" + "".center(76,"=") + "||")
    print("||" + " Hola, bienvenido al generador de contraseñas. ".center(76," ") + "||")
    print("||" + "".center(76,"=") + "||\n")
    cantidad = 0
    
    cantidad = definir_largo_contraseña(4,16)
    
    while True:
        seleccion = input("""
  Seleccione una de las siguientes opciones:

    1 - Generar contraseña solo de LETRAS.
    2 - Generar contraseña solo de NUMEROS.
    3 - Generar contraseña de LETRAS y NUMEROS.
    4 - Generar contraseña de LETRAS, NUMEROS y CARACTERES.
    5 - Salir del programa.     
          """ + " \nOpción seleccionada: ")

        if seleccion in dict_tipos_contraseña:
            os.system("cls")
            dict_tipos_contraseña[seleccion](cantidad)
            break
        else:
            os.system("cls")
            print("Opción invalida, vuelva a intentarlo.")

#Generador de contraseña solo letras
def pass_letras(cantidad): 
    print(" CREACIÓN DE CONTRASEÑA SOLO LETRAS ".center(80,"="))
    
    categorias = ["letras"]
    generar_contraseña(cantidad, categorias)

#Generador de contraseña solo numeros
def pass_numeros(cantidad): 
    print(" CREACIÓN DE CONTRASEÑA SOLO NUMEROS ".center(80,"="))
    
    categorias = ["numeros"]
    generar_contraseña(cantidad, categorias)

#Generador de contraseña con letras y numeros
def pass_alfanumerico(cantidad): 
    print(" CREACIÓN DE CONTRASEÑA LETRAS Y NUMEROS ".center(80,"="))
    
    categorias = ["letras","numeros"]
    generar_contraseña(cantidad, categorias)

#Generador de contraseña con numeros, letras y caracteres especiales
def pass_alfanumerico_y_caracteres(cantidad): 
    print(" CREACIÓN DE CONTRASEÑA LETRAS, NUMEROS Y CARACTERES ".center(80,"="))
    
    categorias = ["letras","numeros","caracteres"]
    generar_contraseña(cantidad, categorias)
  
#Metodo de confirmacion de salida del programa
def salir():
    os.system("cls")
    print(" MENU DE SALIDA DEL PROGRAMA ".center(80,"="))
    while True:
        confirmacion = input("¿Seguro que desea salir? SI/NO: ").upper()
        if confirmacion == "SI":
            print("Hasta luego.")
            sys.exit()
        elif confirmacion == "NO":
            break
        else:
            print("Ingrese una respuesta valida.")

#Metodo para obtener los caracteres de la contraseña
def obtener_caracteres(cantidad, categoria):
    lista_caracteres = ""
    
    for clave, valor in diccionario.items():
        if clave in categoria:
            lista_caracteres += secrets.choice(diccionario[clave])
            cantidad -= 1
        
    while cantidad > 0:
        categoria_actual = secrets.choice(list(diccionario.keys()))
        if categoria_actual in categoria:
            lista_caracteres += secrets.choice(diccionario[categoria_actual])
            cantidad -= 1
    return lista_caracteres

#Metodo para obtener la contraseña a partir de los caracteres obtenidos
def generar_contraseña(cantidad, tipo:list):
    categorias = tipo
    caracteres_aleatorios = obtener_caracteres(cantidad, categorias)
    contraseña = ''.join(secrets.SystemRandom().sample(caracteres_aleatorios, len(caracteres_aleatorios)))
    
    print(f"CONTRASEÑA GENERADA CON EXITO: {contraseña}")
    print("".center(80,"="))

#Metodo para definir limites de la contraseña e ingreso de la cantidad deseada
def definir_largo_contraseña(minimo, maximo):
    while True:
        cantidad = input(f"  Ingrese la cantidad de caracteres para la contraseña, entre {minimo} y {maximo}: ")
        if cantidad.isdigit():
            cantidad = int(cantidad)
            if minimo <= cantidad <= maximo : break
            else: print("Número incorrecto, vuelva a intentarlo.")
        else: print("No se ingresó un número, vuelva a intentarlo.")
    return cantidad

#------------------------------------------------------------------------------------------------------------------------------------------------------------#

dict_tipos_contraseña = {"1": pass_letras, "2":pass_numeros, "3":pass_alfanumerico, "4":pass_alfanumerico_y_caracteres, "5": salir}

#Inicio Programa
menu_inicio()

while True:
    enEjecucion = input("Si desea generar otra contraseña escriba SI: ").upper()
    if enEjecucion == "SI":
        menu_inicio()
    else:
        salir()