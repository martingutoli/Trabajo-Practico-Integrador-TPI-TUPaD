import copy


def ordenar_lista(lista: list, campo: str) -> list:
    """recibe una lista de diccionarios y los ordena por el campo indicado
    retorna una nueva lista ordenada"""

    lista_ordenada = copy.deepcopy(lista)
    longitud = len(lista)

    for i in range(longitud):
        for j in range(0, longitud - i - 1):
            if lista_ordenada[j][campo] > lista_ordenada[j+1][campo]:
                lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]

    return lista_ordenada


# # ejemplo

# lista = [
#     {'nombre': 'pepe', 'edad': 1},
#     {'nombre': 'walter', 'edad': 2},
#     {'nombre': 'maria', 'edad': 4},    
#     {'nombre': 'ariel', 'edad': 5},
#     {'nombre': 'belen', 'edad': 6},    
#     {'nombre': 'carlos', 'edad': 8},
# ]

# print("lista desordenada")
# print(lista)

# print("orden por nombre: ", ordenar_lista(lista, 'nombre'))
# print("orden por edad: ", ordenar_lista(lista, 'edad'))