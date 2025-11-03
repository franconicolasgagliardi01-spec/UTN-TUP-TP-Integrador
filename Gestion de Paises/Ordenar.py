#ORDEN POR NOMBRE
def por_nombre(paises):
    while True:
        #Se ingresa a la función eligiendo la opción deseada
        print("-----------------------------------------------------")    
        print("Ingrese la opción deseada: ")
        opcion = input(" (a) Orden alfabético (A - Z)\n (b) Orden alfabético inverso (Z - A)\n (c) Volver \n\n").upper()

        #Valido que la opción elegida sea correcta
        while opcion not in ["A", "B", "C"]:
            print("-----------------------------------------------------")
            opcion = input("Error. Seleccione una opción válida: \n (a) A - Z\n (b) Z - A\n (c) Volver \n\n").upper()


        #Creo el diccionario agrupados: inicial → clave | nombres de países → valor
        agrupados = {}
        for pais in paises:
            inicial = pais[0].upper()
            if inicial not in agrupados:
                agrupados[inicial] = []
            agrupados[inicial].append(pais)

        #Opción A: Orden alfabético
        if opcion == "A":
            print("-----------------------------------------------------")
            print("Orden A - Z:")
            #Con la función sorted ordeno alfabéticamente las claves del diccionario agrupados{}
            for letra in sorted(agrupados.keys()):
                #Uso la función join() para unir todos los elementos del diccionario usando coma y espacio como separador
                print(f"- {letra}: {', '.join(sorted(agrupados[letra]))}")

        #Opción B: Orden alfabético inverso
        elif opcion == "B":
            print("-----------------------------------------------------")
            print("Orden Z - A:")
            #Ordeno alfabéticamente todas las claves del diccionario agrupados{} y las muestro en reversa aplicando "reverse=True"
            for letra in sorted(agrupados.keys(), reverse=True):
                print(f"- {letra}: {', '.join(sorted(agrupados[letra], reverse=True))}")

        #En caso de que la opción sea "C" el bucle se rompe y vuelve al submenú "Ordenar por:"
        elif opcion == "C":
            break

        #Validación de salida
        salida = input("\n¿Desea ordenar países por orden alfabético nuevamente?\n - Si desea continuar ingrese ¨s¨\n - Si desea salir ingrese ¨n¨\n\n").lower()
        if salida == "n":
            break
        elif salida != "s":
            print("Error. Ingrese:\n - 's' para continuar\n - 'n' para salir")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#ORDEN POR POBLACIÓN
def por_poblacion(paises):
    while True:
        #Se ingresa a la función eligiendo la opción deseada
        print("-----------------------------------------------------")
        print("Ingrese la opción deseada: ")
        opcion = input(" (a) Población ascendente\n (b) Población descendente\n (c) Top 3 paises más poblados \n (d) Volver\n\n").upper()

        #Valido que la opción elegida sea correcta
        while opcion not in ["A", "B", "C", "D"]:
            print("-----------------------------------------------------")
            opcion = input("\nError. Seleccione una opción válida: \n (a) Población ascendente\n (b) Población descendente\n (c) Top 3 paises más poblados \n (d) Volver\n\n").upper()
        
        #Creo función para poder reutilizar según el parámetro de busqueda
        def mostrar_paises_por_poblacion(paises, descendente=False):
            lista = [] #Creo la lista para guardar los datos de población
            for nombre, datos in paises.items():
                poblacion = datos[1]
                lista.append([nombre, poblacion]) #Relleno la lista previamente creada

            #key=lambda --> utilizada para crea una función pequeña, de manera ágil. En este caso para ordenar la población
            lista = sorted(lista, key=lambda x: x[1], reverse=descendente)
            for nombre, poblacion in lista: #Imprimo los datos de población para cada país
                print(f"- {nombre}: {poblacion:,} habitantes") 
        
        #Población ascendente
        if opcion == "A":
            print("-----------------------------------------------------")
            print("\nPaíses ordenados por población ascendente:")
            mostrar_paises_por_poblacion(paises) #Llamo a la función solo con el parámetro paises, para que se imprima la población de forma ascendente 

        #Población descendente
        elif opcion == "B":
            print("-----------------------------------------------------")
            print("\nPaíses ordenados por población descendente:")
            mostrar_paises_por_poblacion(paises, descendente=True) #Agrego el parámetro "descendente=True" para mostrar la población de forma descendente
            

        #Top 3 paises más poblados
        elif opcion == "C":
            top_paises = [] #Creo la lista para guardar los países con mayor población
            for nombre, datos in paises.items():
                poblacion = datos[1] #Le asigno los datos de población a la variable población
                top_paises.append([nombre, poblacion]) #Relleno la lista previamente creada

            #Utilizo nuevamente "key=lambda", en esta ocasión para ordenar la lista de forma descendente (aplicando "reverse=True")
            top_paises = sorted(top_paises, key=lambda x: x[1], reverse=True)

            print("-----------------------------------------------------")
            print("\nTop 3 países más poblados:")
            #Muestro los 3 primeros países de la lista, e decir, los más poblados
            for nombre, poblacion in top_paises[:3]:
                print(f"- {nombre}: {poblacion:,} habitantes")
        
        #En caso de que la opción sea "D" el bucle se rompe y vuelve al submenú "Ordenar por:"
        elif opcion == "D":
            break

        #Validación de salida
        while True:
            salida = input("\n¿Desea ordenar paises según su población nuevamente?\n - Si desea continuar presione ¨s¨\n - Si desea salir presione ¨n¨\n\n").lower()
            if salida == "s":
                break
            elif salida == "n":
                return
            else:
                print("Error. Ingrese:\n - 's' para continuar\n - 'n' para salir")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Creo función para modularizar el código y evitar redundancias
def ordenar_paises_superficie(paises, descendente=False):
    ordenar_paises = [] #Creo la lista para rellenar los países según su superficie
    for nombre, datos in paises.items():
        superficie = datos[2] #Le asigno los datos de superficie a la variable superficie
        ordenar_paises.append([nombre, superficie]) #Relleno la lista previamente creada

    #Utilizo nuevamente "key=lambda", en esta ocasión para ordenar la lista según necesidad o búsqueda
    ordenar_paises_superficie = sorted(ordenar_paises, key=lambda x: x[1], reverse=descendente)

    #Llamo a la función según la opción ingresada
    if descendente:
        orden = "descendente"
    else:
        orden = "ascendente"
    print("-----------------------------------------------------")
    print(f"\nPaíses ordenados por superficie {orden}:")
    for nombre, superficie in ordenar_paises_superficie:
        print(f"{nombre}: {superficie:,} km²")


#ORDEN POR SUPERFICIE ASCENDENTE
def por_superficie_ascendente(paises):
    ordenar_paises_superficie(paises)

#ORDEN POR SUPERFICIE DESCENDENTE
def por_superficie_descendente(paises):
    ordenar_paises_superficie(paises, descendente= True)