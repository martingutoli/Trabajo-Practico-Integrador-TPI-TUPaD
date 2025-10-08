from filtros import (
    filtrar_por_algo, 
    filtrar_por_continente, 
    filtrar_por_poblacion
)





mostrar_menu

menu = [
"1. BUSCAR PAÍS",
"2. FILTRAR PAÍSES",  
"3. ORDENAR PAÍSES",
"4. ESTADÍSTICAS",
"5. GUARDAR RESULTADOS",
"0. SALIR"
]

submenu_busqueda = [
    "1. Búsqueda exacta (nombre completo)", # esto no deberia ser lo mismo?
    "2. Búsqueda parcial (contiene texto)",
    "3. Volver al menú principal"
]

submenu_filtro = [
    "1. Filtrar por continente",
    "2. Filtrar por rango de población",
    "3. Filtrar por rango de superficie",    
    "4. Volver al menú principal"
]

submenu_ordernar = [
    "1. Ordenar por nombre (A-Z)",
    "2. Ordenar por nombre (Z-A)",
    "3. Ordenar por población (mayor a menor)",
    "4. Ordenar por población (menor a mayor)",
    "5. Ordenar por superficie (mayor a menor)",
    "6. Ordenar por superficie (menor a mayor)",
    "7. Volver al menú principal"
]

submenu_estadisticas = [
    "1. Estadísticas de población",
    "2. Estadísticas de superficie",
    "3. Distribución por continentes",
    "4. Reporte completo",
    "5. Volver al menú principal"
]


def mostrar_menu(titulo, opciones):
    print(f"\n{titulo}\n" + "-" * len(titulo))
    for opcion in opciones:
        print(opcion)
    print()
    return input("Seleccione una opción: ")


def main():
    while True:

        opcion = mostrar_menu("MENÚ PRINCIPAL", menu)
        match opcion:
            case "1":   # busqueda
                while True:
                    opcion_busqueda = mostrar_menu("SUBMENÚ DE BÚSQUEDA", submenu_busqueda)
                    if opcion_busqueda == "1":
                        print("Funcionalidad de búsqueda exacta no implementada aún.")
                    elif opcion_busqueda == "2":
                        print("Funcionalidad de búsqueda parcial no implementada aún.")
                    elif opcion_busqueda == "3":
                        break
                    else:
                        print("Opción no válida. Intente nuevamente.")  
            
            case "2":   # filtros
                while True:
                    opcion_filtro = mostrar_menu("SUBMENÚ DE FILTRO", submenu_filtro)
                    if opcion_filtro == "1":
                        fitro_por_continente(continente)
                    elif opcion_filtro == "2":
                        print("Funcionalidad de filtro por rango de población no implementada aún.")
                    elif opcion_filtro == "3":
                        print("Funcionalidad de filtro por rango de superficie no implementada aún.")
                    elif opcion_filtro == "4":
                        print("Funcionalidad de combinación de múltiples filtros no implementada aún.")
                    elif opcion_filtro == "5":
                        break
                    else:
                        print("Opción no válida. Intente nuevamente.")

            case "3":   # ordenar
                print("Funcionalidad de ordenamientos no implementada aún.")

            case "4":   # estadisticas
                print("Funcionalidad de estadisticas no implementada aún.")

            case "0":   # salir
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()



# la validacion de entrada del usuario deberia estar en una funcion
