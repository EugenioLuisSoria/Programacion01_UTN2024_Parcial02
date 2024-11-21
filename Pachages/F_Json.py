import json

# ABRE ARCHIVO
def leer_JSON():
    with open("Programacion01_UTN2024_Parcial02/JSON/data.json", "r") as file: 
        data = json.load(file)
        lista_palabras = data["ahorcado"]
        return lista_palabras

# FUNCION DE SELECCION DE PALABRA DEL DATA.JSON en base a ES/EN
    
