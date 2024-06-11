import pickle, sys, os, random

#Metodo para decidir que operación quiere realizarse
def menu_inicial():
    os.system("cls")
    print("\n" + " MENÚ DE INICIO ".center(80,"="))
    print("""
1 - Generar Ticket.
2 - Leer Ticket.
3 - Salir.      
    """)
    while True:
        seleccion = input("Ingrese el número de la opción que desea realizar: ")
        if seleccion == "1":
            alta_ticket()
            break
        elif seleccion == "2":
            leer_ticket()
            break
        elif seleccion == "3":
            salir_programa()
            break
        else:
            print("Respuesta incorrecta, vuelva a intentarlo.")

#Metodo para crear tickets
def alta_ticket():
    os.system("cls")
    print("\n" + "ALTA DE TICKET ".center(80,"="))
    print("\nIngrese los datos para generar un nuevo ticket.")
            
    ticket = crear_ticket()
    
    print("".center(80,"="))
    print("||" + "SE GENERÓ EL SIGUIENTE TICKET".center(76," ") + "||")
    print("".center(80,"="))
    mostrar_ticket(ticket)
    
    print(f"POR FAVOR RECORDAR SU NUMERO DE TICKET.".center(80," "))
        
    with open(f"Ticket {ticket['Número']}", "wb") as t:
        pickle.dump(ticket, t)
    
    while True:
        respuesta = input("¿Desea generar un nuevo ticket? SI/NO:").upper()
        if respuesta == "SI":
            alta_ticket()
            break
        elif respuesta == "NO":
            menu_inicial()
            break
        else:
            print("Respuesta incorrecta, vuelva a intentarlo.")

#Metodo para leer los tickets guardados            
def leer_ticket():
    os.system("cls")
    print("\n" + " LECTURA DE TICKET ".center(80,"="))
    
    numero = input("Ingrese el número de ticket: ")
    ticket_buscado = f"Ticket {numero}"
        
    if os.path.isfile(ticket_buscado):    
        with open(ticket_buscado, "rb") as t:
            ticket_cargado = pickle.load(t)
            
        print("".center(80,"="))
        print("||" + "MOSTRANDO TICKET".center(76," ") + "||")
        print("".center(80,"="))
        mostrar_ticket(ticket_cargado)
    else:
        print(f"No existe el ticket N°{numero}.")
                
    while True:
        respuesta = input("¿Desea leer otro ticket? SI/NO:").upper()
        if respuesta == "SI":
            leer_ticket()
            break
        elif respuesta == "NO":
            menu_inicial()
            break
        else:
            print("Respuesta incorrecta, vuelva a intentarlo.")

#Metodo de confirmacion de salida del programa
def salir_programa():
    os.system("cls")
    print("\n" + " MENÚ DE SALIDA ".center(80,"="))
    while True:
        respuesta = input("¿Seguro que desea salir? SI/NO: ").upper()
        if respuesta == "SI":
            print("Gracias por usar nuestro sistema.")
            sys.exit()
        elif respuesta == "NO":
            menu_inicial()
        else:
            print("Respuesta incorrecta, vuelva a intentarlo.")

#Metodo para ingresar la información del ticket
def crear_ticket():
    ticket = {
        "Número" : random.randrange(1000, 9999),
        "Nombre" : input("Ingrese su nombre: ").title(),
        "Sector" : input("Ingrese su sector: ").title(),
        "Asunto" : input("Ingrese el asunto: ").capitalize(),
        "Mensaje": input("Ingrese un mensaje: ").capitalize()
        }   
    return ticket

#Metodo para imprimir un ticket en consola
def mostrar_ticket(ticket:dict):
    
    for titulo , info in ticket.items():
        print(f"    {titulo}: {info}")


#------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Inicio Programa
print("||" + "".center(76,"=") + "||")
print("||" + " Hola, bienvenido al sistema de Tickets ".center(76," ") + "||")
print("||" + "".center(76,"=") + "||\n") 

menu_inicial()
