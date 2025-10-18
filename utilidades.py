

def ordenar_lista(lista: list, campo: str) -> list:
    """recibe una lista de diccionarios y los ordena por el campo indicado
    retorna una nueva lista ordenada
    se usa el algoritmo de ordenamiento de burbuja"""

    lista_ordenada = lista.copy() # copia superficial
    longitud = len(lista)

    for i in range(longitud):
        for j in range(0, longitud - i - 1):
            if lista_ordenada[j][campo] > lista_ordenada[j+1][campo]:
                lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]

    return lista_ordenada


if __name__ == '__main__':
    # pruebas

    lista = [
        {'nombre': 'pepe', 'edad': 1},
        {'nombre': 'walter', 'edad': 2},
        {'nombre': 'maria', 'edad': 4},    
        {'nombre': 'ariel', 'edad': 5},
        {'nombre': 'belen', 'edad': 6},    
        {'nombre': 'carlos', 'edad': 8},
    ]

    print("lista desordenada")
    print(lista)

    print("lista ordenana por nombre")
    print(ordenar_lista(lista, 'nombre'))

    print("lista ordenada por edad")
    print(ordenar_lista(lista, 'edad'))