#IMPRIMIR

def pedir_opcion(mensaje: str) -> int:
    entrada = input(mensaje)
    while not entrada.isdigit() and entrada > 3 and entrada < 1:
        print("\n Por favor, ingrese una opción válida.\n")
        entrada = input(mensaje)
    else:
        return int(entrada)
            
