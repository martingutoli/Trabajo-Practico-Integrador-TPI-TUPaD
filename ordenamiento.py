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


def ordenar_por_nombre(paises: list) -> list:
    """ordena los paises por nombre
    recibe: la lista de paises, y opcionalmente si el orden es ascendente o no
    retorna: una nueva lista ordenada por nombre, según indique el argumento ascendente"""

    return ordenar_lista(paises, 'nombre')
    

def ordenar_por_poblacion(paises: list) -> list:
    """ordena los paises por poblacion
    recibe: la lista de paises, y opcionalmente si el orden es ascendente o no
    retorna: una nueva lista ordenada por poblacion, según indique el argumento ascendente"""

    return []


def ordenar_por_superficie(paises: list) -> list:
    """ordena los paises por superficie
    recibe: la lista de paises, y opcionalmente si el orden es ascendente o no
    retorna: una nueva lista ordenada por superficie, según indique el argumento ascendente"""

    return []

