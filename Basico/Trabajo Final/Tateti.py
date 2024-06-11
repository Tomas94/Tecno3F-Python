import random, os, sys

tateti_valores = (1,2,3,4,5,6,7,8,9)
tateti_soluciones = ({1,2,3},{1,4,7},{1,5,9},{2,5,8},{3,6,9},{3,5,7},{4,5,6},{7,8,9})

#Metodo que muestra el menu de inicio con las opciones de juego
def menu_inicio():
    os.system("cls")
    print("".center(80,"="))
    print(" BIENVENIDO AL JUEGO DE TATETI ".center(80," "))
    print("".center(80,"="))

    while True:
        print("""
Elige el modo de juego:

    1 - Jugador Vs Maquina
    2 - Jugador Vs Jugador
    3 - Salir
    """)
        modo_seleccionado = input("Opción elegida: ")
        
        if modo_seleccionado in dict_opciones_menu:
            dict_opciones_menu[modo_seleccionado]()
        else:
            print("Ingresa una opción valida")

#Juego Jugador vs Maquina
def juego_JvM():
    os.system("cls")
    
    print("TATETI JUGADOR VS MAQUINA".center(80,"="))
    contador = 9
    tateti = list(tateti_valores)
    casillas_jugador=set()
    casillas_maquina=set()
    
    jugadores = ["Jugador","Maquina"]
    turno = random.choice(jugadores)    

    print("El Jugador juega con las X, la Maquina con las O")

    while True:
        mostrar_tablero(tateti)
        
        if comprobar_ganador(casillas_jugador):
            print("Gana el jugador.")
            break
        if comprobar_ganador(casillas_maquina):
            print("Gana la maquina.")
            break
        if contador == 0:
            print("Tenemos un empate.")
            break     
        
        if turno == "Jugador":
            turno = seleccion_casilla_jugador("Jugador 1", casillas_jugador, "X", tateti, "Maquina")
        elif turno == "Maquina":
            while True:
                casillaM = random.choice(tateti_valores)
                
                if tateti[casillaM - 1] in tateti_valores:
                    tateti[casillaM - 1] = "O"
                    print(f"Turno de la MAQUINA.\nSeleccionó la casilla: {casillaM}")
                    casillas_maquina.add(casillaM)
                    turno = "Jugador"
                    break
        
        contador -=1
    print("FIN DEL JUEGO.".center(80,"="))
        
#Juego Jugador vs Jugador
def juego_JvJ():
    os.system("cls")
    
    print("TATETI JUGADOR VS JUGADOR".center(80,"="))
    
    contador = 9
    tateti = list(tateti_valores)
    
    casillas_jugador1=set()
    casillas_jugador2=set()
    
    jugadores = ["Jugador1","Jugador2"]
    turno = random.choice(jugadores)    

    print("El Jugador1 juega con las X, el Jugador2 con las O")

    while True:
        os.system("cls")
        mostrar_tablero(tateti)
        
        if comprobar_ganador(casillas_jugador1):
            print("Gana el jugador 1.")
            break
        elif comprobar_ganador(casillas_jugador2):
            print("Gana el jugador 2.")
            break     
        elif contador == 0:
            print("Tenemos un empate.")
            break
        
        if turno == "Jugador1":
            turno = seleccion_casilla_jugador("Jugador 1", casillas_jugador1, "X", tateti, "Jugador2")
        elif turno == "Jugador2":
            turno = seleccion_casilla_jugador("Jugador 2", casillas_jugador2, "O" ,tateti, "Jugador1")
        
        contador -=1
    print("FIN DEL JUEGO.".center(80,"="))

#Muestra el tablero de juego
def mostrar_tablero(tablero):
    print(f"""
    |=========+=========+=========|
    |         |         |         |
    |    {tablero[0]}    |    {tablero[1]}    |    {tablero[2]}    |
    |         |         |         |
    |=========+=========+=========|
    |         |         |         | 
    |    {tablero[3]}    |    {tablero[4]}    |    {tablero[5]}    |
    |         |         |         |
    |=========+=========+=========|
    |         |         |         |
    |    {tablero[6]}    |    {tablero[7]}    |    {tablero[8]}    |
    |         |         |         |
    |=========+=========+=========|
        """)

#Verifica si se tiene una combinacion ganadora
def comprobar_ganador(jugador):
    return any(combinacion_ganadora.issubset(jugador) for combinacion_ganadora in tateti_soluciones)

#Metodo para elegir una casilla como jugador
def seleccion_casilla_jugador(nombre_jugador, casilla_jugador, simbolo, tablero, prox_jugador):
    while True:        
                casilla = input(f"Turno del {nombre_jugador}, elige una casilla:  ")
                
                if not(casilla.isdigit()):
                    print("Ingresa una opcion valida")
                    continue
                
                casilla = int(casilla)
                
                if 1 <= casilla <= 9 and tablero[casilla - 1] in tateti_valores:
                    tablero[casilla - 1] = simbolo
                    casilla_jugador.add(casilla)
                    return prox_jugador
                    break
                else:
                    print("Ya esta ocupado o no es una posición valida.")         

#Metodo para salir del programa
def salir_programa():
    os.system("cls")
    print("\n" + " MENÚ DE SALIDA ".center(80,"="))
    while True:
        respuesta = input("¿Seguro que desea salir? SI/NO: ").upper()
        if respuesta == "SI":
            print("¡Gracias por jugar!")
            sys.exit()
        elif respuesta == "NO":
            menu_inicio()
        else:
            print("Respuesta incorrecta, vuelva a intentarlo.")
#-----------------------------------------------------------------------------------------#

dict_opciones_menu = {"1":juego_JvM, "2":juego_JvJ, "3":salir_programa}

#Inicio Programa
menu_inicio()