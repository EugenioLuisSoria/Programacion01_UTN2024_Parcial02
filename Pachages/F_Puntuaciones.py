import os, json

# ABRE ARCHIVO // lo abre como una lista de diccionarios... NO como un dict con lista con dicts
def leer_json_score():
    with open("Programacion01_UTN2024_Parcial02/JSON/scores.json", "r") as file: 
        data_scores = json.load(file)
        scores = data_scores["jugadores"]
        return scores

# SOBREESCRIBE ARCHIVO
def escribir_json_score(nueva_lista):
    with open("Programacion01_UTN2024_Parcial02/JSON/scores.json", "r+") as file: 
        data_scores = json.load(file)
        # Actualizar los datos
        data_scores["jugadores"] = nueva_lista
        # Volver al inicio del archivo para escribir desde cero
        file.seek(0)
        # Sobrescribir con los datos actualizados
        json.dump(data_scores, file, indent=4)
        # Truncar para eliminar contenido sobrante
        #file.truncate()

#SUMAR PUNTOS
def sumar_puntos(resultado):
    if resultado == True:        
        nombre_usuario = input("Cual es su nombre?: ").upper()
        lista_score = leer_json_score()
        
        #MODIFICAR O CREAR UN SCORE NUEVO:
        
        existe_jugador = False
        for jugador in lista_score:
            if jugador["nombre"] == nombre_usuario:
                #le sumo 1 a a puntuacion vieja
                nueva_puntuacion = jugador["puntuacion"] + 1
                jugador["puntuacion"] = nueva_puntuacion 
                existe_jugador = True
                break
            else:
                continue
        if existe_jugador == False: 
            lista_score.append({"nombre": f"{nombre_usuario}", "puntuacion": 1})
        
        escribir_json_score(lista_score)
    return 

def ordenar_lista(lista):
  largo = len(lista)
  for i in range(largo):
    for j in range(largo - i - 1):
      if lista[j]["puntuacion"] < lista[j+1]["puntuacion"]:
        lista[j], lista[j+1] = lista[j+1], lista[j]
    """ print(lista) """
  return lista

#LISTA Y MUESTRA PUNTUACIONES
def imprimir_puntuaciones():
    os.system("cls" if os.name == "nt" else "clear")    
    puntuaciones_lista = leer_json_score()
    ordenar_lista(puntuaciones_lista)
    
    print("--MEJORES 5 PUNTUACIONES:--")
    if len(puntuaciones_lista) > 0:
        for i in range(len(puntuaciones_lista)):
            print(f"""       
            PUESTO : {i+1}
            Nombre: {puntuaciones_lista[i]["nombre"]}
            PUNTUACION: {puntuaciones_lista[i]["puntuacion"]}
            """, end="-----------------")
            #print(puntuaciones_lista[i])
            if i > 3 and len(puntuaciones_lista) > 4:
                break
           
    
    

imprimir_puntuaciones()



