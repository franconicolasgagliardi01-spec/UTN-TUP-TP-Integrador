#Importo archivos con las funciones
import Modificar
import Ordenar
import Filtrar
import Mostrar

#Diccionario paises, que tendra clave = nombre del pais y valor = datos del archivo csv
paises = {}

#Menu secundario/Filtrar paises
def menu_filtrar_paises(paises):
        while True: #Iteracion del menu
            ordenarPor = input("Filtrar países por: \n (1) Continente\n (2) Rango de población\n (3) Rango de superficie\n (4) Volver\n\n")
    
            while not ordenarPor.isdigit() or int(ordenarPor) not in [1, 2, 3, 4]: #Validacion de ordenarPor
                ordenarPor = input("Error. Seleccione una opción válida:\n\n (1) Continente\n (2) Rango de población\n (3) Rango de superficie\n (4) Volver\n\n")
    
            ordenarPor = int(ordenarPor)

            if ordenarPor == 1:
                Filtrar.continente(paises)
            elif ordenarPor == 2:
                Filtrar.rango_poblacion(paises)
            elif ordenarPor == 3:
                Filtrar.rango_superficie(paises)
            elif ordenarPor == 4:
                print("Volviendo al menú principal")
                break #Termino las iteraciones

#Menu secundario/Ordenar paises
def menu_ordenar_paises(paises):
    while True: #Iteracion del menu

        ordenarPor = input("Ordenar por: \n (1) Nombre\n (2) Población\n (3) Superficie\n (4) Volver\n\n")
    
        while not ordenarPor.isdigit() or int(ordenarPor) not in [1, 2, 3, 4]: #Validacion de ordenarPor
            ordenarPor = input("Error. Seleccione una opción válida:\n\n (1) Nombre\n (2) Población\n (3) Superficie\n (4) Volver\n\n")

        ordenarPor = int(ordenarPor)

        if ordenarPor == 1:
            Ordenar.por_nombre(paises)
        elif ordenarPor == 2:
            Ordenar.por_poblacion(paises)
        elif ordenarPor == 3:
    
            while True: #Iteracion del submenu
                filtrarPor = input("Filtrar por superficie: \n (a) Ascendente\n (b) Descendente\n (c) Volver\n\n")
                while not filtrarPor.isalpha() or filtrarPor.lower() not in ["a", "b", "c"]: #Validacion de filtrarPor
                    filtrarPor = input("Error. Seleccione una opción válida:\n\n (a) Ascendente\n (b) Descendente\n (4) Volver\n\n")

                filtrarPor = filtrarPor.lower()

                if filtrarPor == "a":
                    Ordenar.por_superficie_ascendente(paises)
                elif filtrarPor == "b":
                    Ordenar.por_superficie_descendente(paises)
                elif filtrarPor == "c":
                    break #Termino las iteraciones
    
        elif ordenarPor == 4:
            print("Volviendo al menú principal")
            break #Termino las iteraciones

#Menu secundario/Estadisticas
def menu_estadisticas(paises):
    while True: #Iteracion del menu
        ordenarPor = input("Mostrar: \n (1) País con mayor y menor población\n (2) Promedio de población\n (3) Promedio de superficie\n (4) Cantidad de países por continente\n (5) Volver\n\n")
    
        while not ordenarPor.isdigit() or int(ordenarPor) not in [1, 2, 3, 4, 5]: #Validacion de ordenarPor
            ordenarPor = input("Error. Seleccione una opción válida:\n\n (1) País con mayor y menor población\n (2) Promedio de población\n (3) Promedio de superficie\n (4) Cantidad de países por continente\n (5) Volver\n\n")

        ordenarPor = int(ordenarPor)

        if ordenarPor == 1:
            Mostrar.pais_mayor_menor_poblacion(paises)
        elif ordenarPor == 2:
            Mostrar.promedio_poblacion(paises)
        elif ordenarPor == 3:
            Mostrar.promedio_superficie(paises)
        elif ordenarPor == 4:
            Mostrar.cantidad_paises_continente(paises)
        elif ordenarPor == 5:
            print("Volviendo al menú principal")
            break #Termino las iteraciones

#Menú principal
print("Bienvenido al sistema integral de gestión de países")

while True: #Iteracion del menu principal

    error = Modificar.validar_archivo(paises) #Funcion que valida que el csv tenga el formato correcto
    if error: #En caso de error cierro el programa
        break

    Modificar.actualizar_diccionario(paises) #Pongo en el diccionario los datos del csv

    opcion = input("\nIngrese la opción deseada:\n (a) Buscar país\n (b) Filtrar países\n (c) Ordenar países\n (d) Estadísticas\n (e) Agregar país\n (f) Quitar país\n (g) Salir\n\n")
    while opcion.lower() not in ["a", "b", "c", "d", "e", "f", "g"]: #Validacion de la opcion ingresada
        opcion = input("Error. Seleccione una opción válida:\n\n (a) Buscar país\n (b) Filtrar países\n (c) Ordenar países\n (d) Estadísticas\n (e) Agregar país\n (f) Quitar país\n (g) Salir\n\n")

#Opciones segun la variable opcion
    if opcion.lower() == "a":
        Mostrar.buscar_pais(paises)
    elif opcion.lower() == "b":
        menu_filtrar_paises(paises)
    elif opcion.lower() == "c":
        menu_ordenar_paises(paises)
    elif opcion.lower() == "d":
        menu_estadisticas(paises)
    elif opcion.lower() == "e":
        Modificar.agregar_pais(paises)
    elif opcion.lower() == "f":
        Modificar.quitar_pais(paises)
    elif opcion.lower() == "g":
        print("\nCerrando programa")
        break #Termino las iteraciones
