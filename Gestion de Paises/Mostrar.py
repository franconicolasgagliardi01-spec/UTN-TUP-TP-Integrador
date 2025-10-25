def pais_mayor_menor_poblacion(paises):
    pass

def promedio_poblacion(paises):
    pass

def promedio_superficie(paises):
    pass

def cantidad_paises_continente(paises):
    pass

def buscar_pais(paises):
    nombrePaises = list(paises) #Creo una lista con los nombres de los paises
    claves = [] # Aqui se guardan los paises con coincidencias parciales

    print("-----------------------------------------------------")
    nombre = input("Ingrese el nombre del pais que desea buscar: ") #Ingreso el nombre del pais que busco
    nombre = nombre.strip().capitalize() #Saco espacios y hago la primer letra mayuscula y el resto minuscula

    for pais in nombrePaises: #En caso de que la coincidencia sea total
        if nombre == pais:
            datosPais = paises[pais]
            print("-----------------------------------------------------")
            print(f"Pais {pais} encontrado: ")
            print(f"Poblacion: {datosPais[1]}")
            print(f"Superficie: {datosPais[2]} km cuadrados")
            print(f"Continente: {datosPais[3]}")
            return
    
    #En caso de no haber coincidencia total

    for pais in nombrePaises: #Vario en funcion de los paises
        largoPais = len(pais) #Guardo el largo del pais
        for i in range(-1,-largoPais,-1): #Voy de -1 hasta -largo del pais
            if nombre == pais[:i]: #Cada iteracion le resta mas letras al pais
                claves.append(pais) #Guardo el pais con coincidencia parcial

    if not claves:
        print("No se encontro ninguna coincidencia en la base de datos...")
    else:
        for pais in claves:
            datosPais = paises[pais]
            print("-----------------------------------------------------")
            print(f"Pais {pais} encontrado: ")
            print(f"Poblacion: {datosPais[1]}")
            print(f"Superficie: {datosPais[2]} km cuadrados")
            print(f"Continente: {datosPais[3]}")