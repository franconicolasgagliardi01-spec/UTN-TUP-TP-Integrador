#Funcion que calcula los paises con mas y con menos poblacion-------------------------------------------------------------------------------------------------------------------
def pais_mayor_menor_poblacion(paises):
    claves = list(paises) #Creo una lista con las claves del diccionario paises
    paisAux = paises[claves[0]] #Pais que usare para inicializar menor poblacion
    mayorPoblacion = 0 #Contador que sirve para guardar la poblacion del pais que va teniendo mayor poblacion
    mayorPais = [] #Arreglo donde guardare los paises con mayor poblacion
    menorPoblacion = paisAux[1] #Inicializo la varible con los datos del primer pais
    menorPais = [] #Arreglo donde guardare los paises con menor poblacion

    #Parte que calcula el pais con mayor poblacion
    for pais in claves: #Vario en funcion de los datos de la lista claves
        datosPais = paises[pais] #Guardo el valor del diccionario
        if datosPais[1] > mayorPoblacion: #Si la poblacion del pais es mayor a la guardada se guarda el pais
            mayorPoblacion = datosPais[1]
            mayorPais.clear() #Elimino los datos con los paises que tienen menor poblacion
            mayorPais.append(pais) #Agrego al pais con mayor poblacion
        elif datosPais[1] == mayorPoblacion:
            mayorPais.append(pais) #Agrego al pais que tiene la misma poblacion mayor

    #Parte que calcula el pais con menor poblacion
    for pais in claves: #Vario en funcion de los datos de la lista claves
        datosPais = paises[pais] #Guardo el valor del diccionario
        if datosPais[1] < menorPoblacion: #Si la poblacion del pais es menor a la guardada se guarda el pais
            menorPoblacion = datosPais[1]
            menorPais.clear() #Elimino los datos con los paises que tienen mayor poblacion
            menorPais.append(pais) #Agrego al pais con menor poblacion
        elif datosPais[1] == menorPoblacion and pais != claves[0]: #Pongo esta condicion ya que tengo inicializado el primer pais y si no la pongo se va a duplicar
            menorPais.append(pais) #Agrego al pais que tiene la misma poblacion mayor

    #Muestro al pais con mayor poblacion
    if len(mayorPais) == 1:
        print("-----------------------------------------------------") 
        print(f"El pais con la mayor poblacion en la base de datos es {mayorPais[0]}, con una poblacion de {mayorPoblacion}")
    else:
        print("-----------------------------------------------------")
        print("Los paises con la mayor poblacion en la base de datos son: ")
        for pais in mayorPais:
            print(pais)
        print(f"Con una poblacion de: {mayorPoblacion}")

    #Muestro al pais con menor poblacion
    if len(menorPais) == 1:
        print(f"El pais con la menor poblacion en la base de datos es {menorPais[0]}, con una poblacion de {menorPoblacion}")
    else:
        print("Los paises con la menor poblacion en la base de datos son:")
        for pais in menorPais:
            print(f"-{pais}")
        print(f"Con una poblacion de: {menorPoblacion}")

#Funcion que calcula el promedio de poblacion de los paises---------------------------------------------------------------------------------------------------------------------
def promedio_poblacion(paises):
    claves = list(paises)
    sumatoriaPoblacion = 0

    for pais in claves: #Hago la sumatoria de la poblacion
        datosPais = paises[pais]
        sumatoriaPoblacion += datosPais[1]

    promedioPoblacion = sumatoriaPoblacion/len(paises) #Calculo el promedio

    print("-----------------------------------------------------")
    print(f"El promedio de la poblacion de los paises de la base de datos es: {int(promedioPoblacion)}")

#Funcion que calcula el promedio de la superficie de los paises-----------------------------------------------------------------------------------------------------------------
def promedio_superficie(paises):
    claves = list(paises)
    sumatoriaSuperficie = 0

    for pais in claves: #Hago la sumatoria de la superficie
        datosPais = paises[pais]
        sumatoriaSuperficie += datosPais[2]

    promedioSuperficie = sumatoriaSuperficie/len(paises) #Calculo el promedio

    print("-----------------------------------------------------")
    print(f"El promedio de la superficie de los paises de la base de datos es: {int(promedioSuperficie)}")

#Funcion que muestra la cantidad de paises por continente-----------------------------------------------------------------------------------------------------------------------
def cantidad_paises_continente(paises):
    claves = list(paises)
    america = 0 #Inicializo los contadores
    europa = 0
    asia = 0
    oceania = 0
    africa = 0
    antartida = 0

    for pais in claves: #Vario en funcion de los paises
        datosPais = paises[pais]
        if datosPais[3] == "América": #Si el pais esta en América sumo uno al contador
            america += 1
        elif datosPais[3] == "Europa": #Si el pais esta en Europa sumo uno al contador
            europa += 1
        elif datosPais[3] == "Asia": #Si el pais esta en Asia sumo uno al contador
            asia += 1
        elif datosPais[3] == "Oceanía": #Si el pais esta en Oceanía sumo uno al contador
            oceania += 1
        elif datosPais[3] == "África": #Si el pais esta en África sumo uno al contador
            africa += 1
        elif datosPais[3] == "Antártida": #Si el pais esta en Antártida sumo uno al contador
            antartida += 1

    if america == 1:
        print("En América hay un total de 1 pais cargado")
    else:
        print(f"En América hay un total de {america} paises cargados")

    if europa == 1:
        print("En Europa hay un total de 1 pais cargado")
    else:
        print(f"En Europa hay un total de {europa} paises cargados")

    if asia == 1:
        print("En Asia hay un total de 1 pais cargado")
    else:
        print(f"En Asia hay un total de {asia} paises cargados")

    if oceania == 1:
        print("En Oceanía hay un total de 1 pais cargado")
    else:
        print(f"En Oceanía hay un total de {oceania} paises cargados")

    if africa == 1:
        print("En África hay un total de 1 pais cargado")
    else:
        print(f"En África hay un total de {africa} paises cargados")

    if antartida == 1:
        print("En Antártida hay un total de 1 pais cargado")
    else:
        print(f"En Antártida hay un total de {antartida} paises cargados")

#Funcion que busca paises de forma parcial-------------------------------------------------------------------------------------------------------------------------------------- 
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