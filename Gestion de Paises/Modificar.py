from pathlib import Path #Importo esta libreria para acceder al archivo
ruta = Path(__file__).parent / "paises.csv" #Voy a la carpeta padre de Modificar.py y accedo a paises que se encuentra ahi

#Funcion auxiliar para saber si un numero es entero
def es_entero(cadena): 
    try:
        int(cadena)
        return True
    except ValueError:
        return False

def validar_archivo(paises):
    with open(ruta,"r", encoding="utf-8") as archivo: #Abro el archivo, la parte de encoding es para que entienda acentos
        for linea in archivo: #Vario en funcion de las filas del archivo
            pais = linea.strip().split(",") #Guardo la fila

            if pais[0].isdigit():#Valido el nombre
                print(f"Error, el nombre de un pais no puede ser un numero, el nombre es:({pais[0]}): Revise el archivo csv")
                return True #Retorno que hubo error
            elif not pais[1].isdigit() or not pais[2].isdigit():#Valido la poblacion y superficie
                print(f"Error, poblacion o superficie con tipo incorrecto en pais {pais[0]}: Revise el archivo csv")
                return True #Retorno que hubo error
            elif pais[3] not in ["África","Antártida","Asia","Europa","América","Oceanía"]:#Valido continente
                print(f"Error, el continente {pais[3]} en el pais {pais[0]} no es valido: Revise el archivo csv")
                print("Continentes validos: África, Antártida, Asia, Europa, América, Oceanía")
                return True #Retorno que hubo un error
    return False #Retorno que no hubo error

#Funcion para actualizar el diccionario
def actualizar_diccionario(paises): #Funcion que sirve para actualizar el diccionario en base al archivo paises
    with open(ruta,"r", encoding="utf-8") as archivo: #Abro el archivo, la parte de encoding es para que entienda acentos
        for linea in archivo: #Vario en funcion de las filas del archivo
            pais = linea.strip().split(",") #Guardo la fila

            pais[1] = int(pais[1])#Convierto poblacion a int
            pais[2] = int(pais[2])#Convierto superficie a int

            paises[pais[0]] = pais #Pongo el nombre como clave y la lista pais como valor

#Funcion para agregar paises al archivo
def agregar_pais(paises):
    nombre = input("Ingrese el nombre del pais que desea agregar: ") #Ingreso nombre del pais
    while nombre.strip().capitalize() in paises or es_entero(nombre): #Validacion del nombre, capitalize()conviete todo en miniscula y la primer letra en mayuscula y strip es para los espacios en blanco
        if es_entero(nombre):
            print("El nombre del pais no puede ser un numero")
            nombre = input("Ingrese el nombre del pais que desea agregar: ")
        else:
            print("Ese pais ya se encuentra en la base de datos")
            nombre = input("Ingrese el nombre del pais que desea agregar: ")
    nombre = nombre.strip().capitalize() #Elimino espacios en balnco y pongo primera letra en mayuscula

    poblacion = input("Ingrese la cantidad de poblacion del pais: ") #Ingreso la poblacion
    while not es_entero(poblacion) or int(poblacion) <= 0: #Valido la poblacion
        if not es_entero(poblacion):
            print("La poblacion debe ser un numero")
            poblacion = input("Ingrese la cantidad de poblacion del pais: ")
        else:
            print("La poblacion debe ser mayor a cero")
            poblacion = input("Ingrese la cantidad de poblacion del pais: ")

    superficie = input("Ingrese la superficie del pais en metros cuadrados: ") #Ingreso la superficie
    while not es_entero(superficie) or int(superficie) <= 0: #Valido la superficie
        if not es_entero(superficie):
            print("La superficie debe ser un numero")
            superficie = input("Ingrese la superficie del pais en metros cuadrados: ")
        else:
            print("La superficie debe ser mayor a cero")
            superficie = input("Ingrese la superficie del pais en metros cuadrados: ")

    continente = input("Ingrese el continente en el que se encuentra el pais: ") #Ingreso continente
    while not continente.strip().capitalize() in ["África","Antártida","Asia","Europa","América","Oceanía"]: #Valido continente
        print("El continente ingresado es invalido")
        print("Continentes validos: África, Antártida, Asia, Europa, América, Oceanía")
        continente = input("Ingrese el continente en el que se encuentra el pais: ")
    continente = continente.strip().capitalize()#Elimino espacios en balnco y pongo primera letra en mayuscula

    with open(ruta, "a", encoding="utf-8") as archivo: #Pongo los datos en el archivo
        archivo.write("\n"+nombre+","+poblacion+","+superficie+","+continente)
    print("Pais cargado en el archivo...")

#Funcion para eliminar paises del archivo
def quitar_pais(paises):
    with open(ruta, "r", encoding="utf-8") as archivo: #Verifico si el archivo tiene alguna linea
        lineas = archivo.readlines() #Creo una lista de strings que son las lineas
        if not lineas: #Veo si esta vacia la lista
            print("El archivo esta vacio....")
            return

    nombre = input("Escriba el nombre del pais que desea eliminar: ") #Ingreso nombre 
    while not nombre.strip().capitalize() in paises: #Valido nombre
        print("El nombre seleccionado no existe en la base de datos")
        nombre = input("Escriba el nombre del pais que desea eliminar: ")
    
    del paises[nombre.strip().capitalize()] #Elimino del diccionario el pais

    with open(ruta, "w", encoding="utf-8") as archivo: #Guardo el nuevo diccionario como archivo
        contador = 0 #Contador que uso para saber cul es la ultima iteracion
        for pais in paises: #Vario en funcion de las claves
            contador += 1
            datosPais = paises[pais]
            if contador < len(paises):
                archivo.write(datosPais[0]+","+str(datosPais[1])+","+str(datosPais[2])+","+datosPais[3]+"\n") #Debo convertir a string ya que esos datos estan como int en el diccionario
            else:
                archivo.write(datosPais[0]+","+str(datosPais[1])+","+str(datosPais[2])+","+datosPais[3]) #En la ultima iteracion no hago salto de linea, para concordar con agregar pais

    print("Pais eliminado del archivo...")