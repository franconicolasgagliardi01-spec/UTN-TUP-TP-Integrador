from pathlib import Path #Importo esta libreria para acceder al archivo
ruta = Path(__file__).parent / "paises.csv" #Voy a la carpeta padre de Modificar.py y accedo a paises que se encuentra ahi

def actualizar_diccionario(paises): #Funcion que sirve para actualizar el diccionario en base al archivo paises
    with open(ruta,"r", encoding="utf-8") as archivo: #Abro el archivo, la parte de encoding es para que entienda acentos
        for linea in archivo: #Vario en funcion de las filas del archivo
            pais = linea.strip().split(",") #Guardo la fila

            if pais[0].isdigit():#Valido el nombre
                print(f"Error, nombre con tipo incorrecto, nombre:{pais[0]}: Revise el archivo csv")
                return True #Retorno que hobo error
            elif not pais[1].isdigit() or not pais[2].isdigit():#Valido la poblacion y superficie
                print(f"Error, poblacion o superficie con tipo incorrecto en pais {pais[0]}: Revise el archivo csv")
                return True #Retorno que hubo error
            elif pais[3] not in ["África","Antártida","Asia","Europa","América","Oceanía"]:#Valido continente
                print(f"Error, el continente {pais[3]} en el pais {pais[0]} no es valido: Revise el archivo csv")
                return True #Retorno que hubo un error

            pais[1] = int(pais[1])#Convierto poblacion a int
            pais[2] = int(pais[2])#Convierto superficie a int

            paises[pais[0]] = pais #Pongo el nombre como clave y la lista pais como valor
    return False #Retorno que no hubo error

def agregar_pais():
    pass

def quitar_pais():
    pass
