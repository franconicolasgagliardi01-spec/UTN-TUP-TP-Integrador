#Filtrado por continentes
def continente(paises):
 
 agrupados = {} #Creo el diccionario agrupados{}

 #Recorro el diccionario paises para extraer país y continente, y así rellenar el diccionario creado previamente
 for nombre, datos in paises.items():
     continente = datos[3]
     if continente not in agrupados:
         agrupados[continente] = [] #Se agrega el continente en caso de que no aparezca previamente
     agrupados[continente].append(nombre)

 print("Filtrando países por continente:\n")
 #Se muestran por pantalla los paises agrupados por continente
 for continente in sorted(agrupados):
     print(f"\n{continente}:")
     for pais in sorted(agrupados[continente]):
         print(f"  - {pais}")

 #--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Filtrado por rango de población
def rango_poblacion(paises):
    
    while True:
        print("Ingrese rango de población a buscar (en millones de personas):")

        try:
            #Al ingresar los rangos en millones, multiplico por 1000000 para llegar al número deseado
            rangoMin = int(input("Desde: ")) * 1000000 
            rangoMax = int(input("Hasta: ")) * 1000000
        except ValueError:
            print("Error. Ingrese un número válido.")
            continue

        #Validación para verificar que el rango sea correcto
        if rangoMin < 0 or rangoMax < 0 or rangoMin >= rangoMax:
            print("\nError. Ingrese valores válidos (el rango máximo debe ser mayor que el mínimo)\n")
            continue

        paises_en_rango = [] #Creo la lista paises_en_rango[]

        #Relleno la lista creada previamente
        for nombre, datos in paises.items():
            poblacion = datos[1]
            if rangoMin <= poblacion <= rangoMax:
                paises_en_rango.append(nombre)

        #Imprimo por pantalla los paises dentro del rango ingresado
        if paises_en_rango:
             print(f"\nPaíses dentro del rango de {rangoMin:,} y {rangoMax:,} habitantes:\n")
             for pais in paises_en_rango:
                 print(f"- {pais}: {paises[pais][1]:,} habitantes")

        #Si la lista paises_en_rango está vacía (por lo que no se encuentraron países en tal rango) se imprime el siguiente mensaje
        else:  
            print(f"No se encontraron países entre {rangoMin:,} y {rangoMax:,} habitantes")

        #Validación de salida
        while True:
         salida = input("¿Desea filtrar paises por rango de población nuevamente? (s/n): ").lower()
         if salida.lower() == "s":
             break
         elif salida.lower() == "n":
             return
         else:
                print("Error. Ingrese:\n - 's' para continuar\n - 'n' para salir")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Filtrado por rango de superficie
def rango_superficie(paises):

 while True:
        print("Ingrese rango de superficie a buscar:")

        try:
           
            #Solicito los valores del rango
            rangoMin = int(input("Desde (km²): "))
            rangoMax = int(input("Hasta (km²): "))
 
        except ValueError:
            print("Error. Ingrese un número válido.")
            continue

        #Validación para verificar que el rango sea correcto
        if rangoMin < 0 or rangoMax < 0 or rangoMin >= rangoMax:
            print("\nError. Ingrese valores válidos (el rango máximo debe ser mayor que el mínimo)\n")
            continue

        paises_en_rango = [] #Creo la lista paises_en_rango[]

        #Relleno la lista creada previamente
        for nombre, datos in paises.items():
            superficie = datos[2]
            if rangoMin <= superficie <= rangoMax:
                paises_en_rango.append(nombre)

        #Imprimo por pantalla los paises dentro del rango ingresado
        if paises_en_rango:
             print(f"\nPaíses dentro del rango de {rangoMin:,} y {rangoMax:,} km²:\n")
             for pais in paises_en_rango:
                 print(f"- {pais}: {paises[pais][2]:,} km²")

        #Si la lista paises_en_rango está vacía (por lo que no se encuentraron países en tal rango) se imprime el siguiente mensaje
        else:  
            print(f"No se encontraron países entre {rangoMin:,} y {rangoMax:,} km² de superficie")

        #Validación de salida
        while True:
         salida = input("¿Desea filtrar paises por rango de superficie nuevamente? (s/n): ").lower()
         if salida.lower() == "s":
             break
         elif salida.lower() == "n":
             return
         else:
                print("Error. Ingrese:\n - 's' para continuar\n - 'n' para salir")