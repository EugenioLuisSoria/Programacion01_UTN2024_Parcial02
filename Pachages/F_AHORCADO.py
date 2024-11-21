
import os, random
from . import F_Json as FJ
from . import Validaciones as Val

def seleccionar_palabra(idioma_usuario):
    lista_completa_palabras = FJ.leer_JSON()
    id = random.randint(0,9)
    palabra = lista_completa_palabras[id][idioma_usuario]
    return palabra

def imprimir_monigote(contador_intentos):
    os.system("cls" if os.name == "nt" else "clear")
    print(""" 
||=====
||
||""")
    match contador_intentos:
        case 0:
            print("")
        case 1:
            print(" O ")
            print("\n")
            print("\n")
        case 2:
            print(" O ")
            print(" | ")
            print("\n")
        case 3:
            print(" O ")
            print("/| ")
            print("\n")
        case 4:
            print(" O ")
            print("/|\ ")
            print("\n")
        case 5:
            print(" O ")
            print("/|\ ")
            print("/  ")
        case 6:
            print(" O ")
            print("/|\ ")
            print("/ \ ")
            print("\n")
            print("¡Ahorcado!")
            print("\n")

def jugar_ahorcado(idioma_usuario):
    # Se elije palabra
    #HARCODEANDO PALABRA: #############################################  palabra = "ASD"
    palabra = seleccionar_palabra(idioma_usuario).upper()    
    
    #LOGICA DEL JUEGO
    ganador = False
    intentos = 0 
    palabra_revelandose = ["_"] * len(palabra)
    palabra_lista = []
    letras_usadas = []
    for i in range(len(palabra)):
        palabra_lista += [f"{palabra[i]}"]
     
    while intentos < 7:
        os.system("cls" if os.name == "nt" else "clear")
        imprimir_monigote(intentos)
        
                        #MODULARIZAR ESTE FOR, PARA QUE ESTÉ EN F_GRALES
        #Imprime los guioncitos de la palabra revelándose
        for i in range(len(palabra_revelandose)):
            print(f"{palabra_revelandose[i]}", end="")
        print("\n")
        
        #Seleccion de LETRA por el usuario
        if intentos != 6:
            print(f"A usted le quedan: {6 - intentos} intentos")
            print(f"Usted ha utilizado estas fallidas letras: ", end="")
            for i in range(len(letras_usadas)):
                print(letras_usadas[i], end=", ")
                
            letra_usuario = input("\nIngrese una letra: ").upper()
            es_string = Val.validar_letra(letra_usuario)
            while es_string == False:
                letra_usuario = input("Ingrese una letra VÁLIDA: ")
                es_string = Val.validar_letra(letra_usuario)
        
        #Comprobacion de acierto de Letra en Palabra:
        contador_aciertos = False
        for i in range(len(palabra_lista)):
            if palabra_lista[i] == letra_usuario:
                palabra_revelandose[i] = palabra_lista[i]
                contador_aciertos = True
            else:
                continue
        
        if letra_usuario not in letras_usadas:
            letras_usadas +=  [letra_usuario.upper()]
            
        
        if contador_aciertos == False:
            intentos += 1
        
        
        #Comprobacion de Ganador Juego:
        if not any(i == "_" for i in palabra_revelandose):
            os.system("cls" if os.name == "nt" else "clear")
            print(f""" 
             O 
            /|\  SOY LIBRE! SIII!! 
            / \     La palabra que me salvó es: {palabra.upper()}

                  
                  """)
            ganador = True
            break
        
    return ganador
    


