while True:
    x = input(" Ingresa un numero mayor a 0 para iniciar el programa, otro para terminar la ejecución. ".center(100,"-") + "\n")
    if  not(x.isdigit()) or int(x) <= 0:                                        #Verificacion de que se ingresa un numero mayor a 0
        print("Hasta Pronto.")
        break

    frase = input("Ingresa una palabra o frase.".center(100,"-")+"\n")          #Ingreso y calculo de cantidad de caracteres de palabra o frase
    caracteres = len(frase)                                                     
    print(f"{frase} tiene {caracteres} carácteres.")
    
    print(f" Vamos a calcular el factorial de {caracteres} ".center(100,"-"))   #Inicio de calculo del factorial
    factorial = caracteres  
    if caracteres == 0:
        print(f"El factorial de 0 es igual a 1.")
    else:
        contador = caracteres  
        while contador > 1:
            contador -= 1
            factorial *= contador
        print(f"El factorial de {caracteres} es igual a {factorial}.")
    
    print(f" Vamos a ver si el resultado del factorial es par o impar.".center(100,"-"))    #Inicio de verificacion de número par o impar  
    if factorial % 2 == 0:
        print(f"{factorial} es par.")
    else:
        print(f"{factorial} es impar.")
