import csv
import os

nombre_archivo = "paises.csv"


def leer_archivo_csv(nombre_archivo: str) -> list:
    """Recibe el nombre del archivo csv, con encabezado
    Retorna una lista de diccionarios, cada elemento de la lista es un registro del csv
    los nombres de campo provienen de la cabecera (por eso es obligatorio la )"""

    paises = []
   
    # se lee cada registro como un diccionario
    with open(nombre_archivo, 'r', newline='', encoding='utf-8') as csvfile:
        lector = csv.DictReader(csvfile)
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
    """test"""

    print(f"{'Pais':46} {'Poblacion':12} {'Superficie':12} {'Continente':20}")
    
    for pais in paises:
        print(f"{pais['nombre']:46} {pais['poblacion']:12} {pais['superficie']:12} {pais['continente']:20}")



def main():
    if not os.path.exists(nombre_archivo):
        print(f"No se pudo leer el archivo {nombre_archivo}!")
        return
    
    paises = leer_archivo_csv(nombre_archivo)

    print("DATOS EN CRUDO; PARA VER SU ESTRUCTURA")
    print(paises)

    mostrar_paises(paises)
   

if __name__ == '__main__':
    main()