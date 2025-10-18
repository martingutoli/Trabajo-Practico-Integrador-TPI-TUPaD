import csv
import os

from ordenamiento import (
    ordenar_por_nombre, 
    ordenar_por_poblacion, 
    ordenar_por_superficie
)

from filtros import (
    filtrar_por_continente,
    filtrar_rango_poblacion,
    filtrar_rango_superficie
)

from estadisticas import (
    mayor_poblacion,
    menor_poblacion,
    poblacion_promedio,
    superficie_promedio
)


nombre_archivo = "paises.csv"


### FUNCIONES PARA ESTADISTICAS (MODULO ESTADISTICAS?




### FUNCIONES DE BUSQUEDA

def buscar_por_nombre(paises: list, nombre: str) -> list:
    """buscar por nombre
    recibe el listado de paises y el nombre de pais a buscar
    retorna una lista de los paises econtrados, puede ser mas de uno si la busqueda no es exacta"""

    return []


### MODULO ARCHIVO?

def leer_archivo_csv(nombre_archivo: str) -> list:
    """Recibe el nombre del archivo csv, con encabezado
    Retorna una lista de diccionarios, cada elemento de la lista es un registro del csv
    los nombres de campo provienen de la cabecera (por eso es obligatorio la )"""

    paises = []

  
    # se lee cada registro como un diccionario
    with open(nombre_archivo, 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for pais in lector:            
            # en el csv poblacion es un string que repesenta a un entero
            # superficie es un string que representa a un flotante
            # se convierten ambos datos a entero
            pais['poblacion'] = int(pais['poblacion'])
            # esta es la forma mas facil de eliminar el punto decimal
            pais['superficie'] = int(float(pais['superficie']))
            paises.append(pais)

    return paises



def mostrar_paises(paises: list):
    """Muestra una lista de paises como una tabla
    recibe una lista de diccionarios"""

    print(f"{'Pais':46} {'Poblacion':12} {'Superficie':12} {'Continente':20}")
    
    for pais in paises:
        print(f"{pais['nombre']:46} {pais['poblacion']:12} {pais['superficie']:12} {pais['continente']:20}")



def main():
    if not os.path.exists(nombre_archivo):
        print(f"No se pudo leer el archivo {nombre_archivo}!")
        return
    
    paises = leer_archivo_csv(nombre_archivo)

    # print(" DATOS EN CRUDO (PARA VER SU ESTRUCTURA) ".center(80, "="))
    # print(paises)
    # print(" FIN DATOS EN CRUDO ".center(80, "="))
    # print()
    # print(" PAISES ".center(80, "="))
    # mostrar_paises(paises)
    # print(" FIN PAISES ".center(80, "="))
    # print()
    # print(" FILTROS ".center(80, "="))
    # print("\npor continente")
    # continente = input("ingrese continente...")
    # print(mostrar_paises(filtrar_por_continente(paises, continente)))
    # print("\npor rango de poblacion")
    # print(mostrar_paises(filtrar_rango_poblacion(paises, 4270563, 11890781)))
    # print("\npor rango de superficie")
    # print(mostrar_paises(filtrar_rango_superficie(paises, 236800, 9372610)))
    # print(" FIN FILTROS ".center(80, "="))
    # print()
    # print(" ORDENAMIENTO ".center(80, "*"))
    # print("\npor nombre")
    
    # paises_ordenados = ordenar_por_nombre(paises)
    # mostrar_paises(paises_ordenados)
    # print("\npor poblacion")
    # print(mostrar_paises(ordenar_por_poblacion(paises)))
    # print("\npor superficie")
    # print(mostrar_paises(ordenar_por_superficie(paises)))
    # print(" FIN ORDENAMIENTO ".center(80, "="))
    # print()
    print(" ESTADISTICAS ".center(80, "="))
    print("\npais con menor poblacion")
    print(menor_poblacion(paises))
    print("\npais con mayor poblacion")
    print(mayor_poblacion(paises))
    print("\npoblacion promedio")
    print(poblacion_promedio(paises))
    print("\nsuperficie promedio")
    print(superficie_promedio(paises))
    print(" FIN ESTADISTICAS ".center(80, "="))

if __name__ == '__main__':
    main()