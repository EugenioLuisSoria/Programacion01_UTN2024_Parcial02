from Pachages import F_AHORCADO as FA
from Pachages import F_GRALES as FG
from Pachages import F_Puntuaciones as FP

import os

# Despeja la terminal, para comenzar con pantalla limpia:
os.system("cls" if os.name == "nt" else "clear")


def menu():
    while True:
        # Mostrar las opciones del menú
        print("\n---- Menu Principal ---:")
        print("1.Jugar")  
        print("2.Puntajes")  
        print("3. Salir")  
        opcion = FG.pedir_opcion("Seleccione una opcion: ")

        match opcion:
            case 1:
                #JUGAR
                idioma = input("En que idioma quiere jugar? ES/EN: ").upper()
                while idioma != "ES" and idioma != "EN":
                    idioma = input("Idioma no registrado. Elija nuevamente. ES/EN: ").upper()
                resultado = FA.jugar_ahorcado(idioma)
                if resultado == True:
                    print("\nUSTED HA GANADO!!! SIII!\n")
                    FP.sumar_puntos(resultado)
                else:
                    print("\nUSTED HA PERDIDO!!! BUUUUH!!!\n NO OBTIENE PUNTO ALGUNO.")
            
            case 2:
                FP.imprimir_puntuaciones()
                
            case 3:
                #SALIR
                print("\nSaliendo del programa...")
                break
            
            case _:
                print("\n OPCIÓN NO VÁLIDA.\n")

menu()



