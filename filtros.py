def filtrar_por_continente(paises: list, continente: str) -> list:
    """filtra los paises por continente
    recibe: la lista de paises, y el continente por el que desea filtrar
    retorna: una lista nueva con los paises que tienen el continente recibido"""

    filtrado_por_continente = []

    for pais in paises:
        if continente.lower() == pais['continente'].lower():
            filtrado_por_continente.append(pais)
    
    return filtrado_por_continente


def filtrar_rango_poblacion(paises: list, poblacion_minima: int, poblacion_maxima: int) -> list:
    """filtra los paises por rango de poblacion
    recibe: la lista de paises, el rango minimo y maximo de poblacion para filtrar
    retorna: una lista nueva con los paises que cumplan con el rango minimo y maximo recibidos
    """

    return []


def filtrar_rango_superficie(paises: list, superficie_minima: int, superficie_maxima: int) -> list:
    """filtra los paises por rango de superficie
    recibe: la lista de paises, el rango minimo y maximo de superficie para filtrar
    retorna: una lista nueva con los paises que cumplan con el rango minimo y maximo recibidos
    """

    return []