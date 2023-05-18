from Clases import *
import os
import datetime
import sqlite3
"""
Indice de Funciones
"""
def Menu(Base):
    print("""Bienvenido al Organigrama""",Base,"""
1-Crear Dependencia
2-Eliminar Dependencia
3-Modificar Dependencia (En curso)
4-Editar Ubicacion de Dependencia  (En curso)
5-Fusionar Dependencias  (En curso)
6-Agregar Personas Dependencia 
7-Modificar Persona Dependencia  (En curso)
8-Copiar Organigrama  (En curso)
9-Graficar Organigrama  (En curso)
10-Eliminar Organigrama  (En curso)
11-Salir""")

def ImprimirNombres():
    archivo=open('Nombres_Organigrama.txt','r')
    x=1
    for Linea in archivo:
        print(x,"-",Linea,end="")
        x+=1

    archivo.close()

def EliminarNombres(Base):
    archivo = open('Nombres_Organigrama.txt', 'r')
    Lineas=archivo.readlines()
    Base2=Base+"\n"
    if Base2 in Lineas:
        Lineas.remove(Base2)
    archivo.close()
    archivo = open('Nombres_Organigrama.txt', 'w')
    for dato in Lineas:
        archivo.write(dato)
    archivo.close()

def AgregarNombres(Base):
    archivo = open('Nombres_Organigrama.txt', 'a')
    archivo.write(Base+"\n")

    archivo.close()

def CrearOrg():
    ORG_AUX=Organigrama
    #Crea una base de datos segun un nombre ingresado por el usuario
    while True:
        ORG_AUX.ORG=input("Ingrese el nombre del organigrama: ")
        ruta=ORG_AUX.ORG+".db"

        #Si el nombre para la base de datos ya existe no se crea la base de datos
        if os.path.exists(ruta):
            print("Ya existe una base de datos con ese nombre ")
        else:
            conexion = sqlite3.connect(ruta)
            break

    ORG_AUX.FEC=datetime.date.today()
    ORG_AUX.COD_ORG=int(input("Ingrese el codigo del organigrama: "))

    #Se procede a crear una tabla principal para guardar los datos de codigo, nombre y fecha
    cursor=conexion.cursor()
    cursor.execute("CREATE TABLE Organigrama (COD REAL , ORG TEXT, FEC TEXT, Dep1 TEXT, Dep2 TEXT, Dep3 TEXT, Dep4 TEXT, Dep5 TEXT)")
    cursor.execute("INSERT INTO Organigrama (COD, ORG, FEC ) VALUES ( ?, ?, ?)",(ORG_AUX.COD_ORG , ORG_AUX.ORG , ORG_AUX.FEC))
    #Se guarda y despues se cierra la conexion con la base de datos
    conexion.commit()
    conexion.close()
    return ORG_AUX.ORG

def CrearDep(Base,Tabla,Dep):
    conexion=sqlite3.connect(Base)
    cursor=conexion.cursor()
    Data=cursor.execute(f'SELECT Dep1 ,Dep2, Dep3, Dep4, Dep5 FROM "{Tabla}"')
    #Verificar que la Dependencia que se esta intentando ingresar no Exista

    #Verificacion de que a la tabla X aun se le pueden asignar dependencias subsecuentes
    dato=Data.fetchone()
    DepP=Dep+"P"
    while True:

        if dato[0]==None :
            cursor.execute(f'UPDATE "{Tabla}" SET Dep1= (?) ',(Dep,))
            cursor.execute(f'CREATE TABLE "{Dep}" (COD REAL , NOM TEXT, CODRES TEXT, DepPadre TEXT, Dep1 TEXT, Dep2 TEXT, Dep3 TEXT, Dep4 TEXT, Dep5 TEXT)')
            cursor.execute(f'INSERT INTO "{Dep}" (COD, NOM,DepPadre) VALUES ( ? , ? , ? )',(1,Dep,Tabla))
            cursor.execute(f'CREATE TABLE "{DepP}" (COD REAL PRIMARY KEY, DOC TEXT , APE TEXT, NOM TEXT, TEL TEXT, DIR TEXT, DEP  TEXT, SAL REAL)')
            print("Dependencia creada con exito!")
            break

        if dato[1]==None :
            cursor.execute(f'UPDATE "{Tabla}" SET Dep2= (?) ', (Dep,))
            cursor.execute(f'CREATE TABLE "{Dep}" (COD REAL , NOM TEXT, CODRES TEXT, DepPadre TEXT, Dep1 TEXT, Dep2 TEXT, Dep3 TEXT, Dep4 TEXT, Dep5 TEXT)')
            cursor.execute(f'INSERT INTO "{Dep}" (COD, NOM,DepPadre) VALUES ( ? , ? , ? )', (1, Dep, Tabla))
            cursor.execute(f'CREATE TABLE "{DepP}" (COD REAL PRIMARY KEY, DOC TEXT , APE TEXT, NOM TEXT, TEL TEXT, DIR TEXT, DEP  TEXT, SAL REAL)')
            print("Dependencia creada con exito!")
            break

        if dato[2]==None :
            cursor.execute(f'UPDATE "{Tabla}" SET Dep3= (?) ', (Dep,))
            cursor.execute(f'CREATE TABLE "{Dep}" (COD REAL , NOM TEXT, CODRES TEXT, DepPadre TEXT, Dep1 TEXT, Dep2 TEXT, Dep3 TEXT, Dep4 TEXT, Dep5 TEXT)')
            cursor.execute(f'INSERT INTO "{Dep}" (COD, NOM,DepPadre) VALUES ( ? , ? , ? )', (1, Dep, Tabla))
            cursor.execute(f'CREATE TABLE "{DepP}" (COD REAL PRIMARY KEY, DOC TEXT , APE TEXT, NOM TEXT, TEL TEXT, DIR TEXT, DEP  TEXT, SAL REAL)')
            print("Dependencia creada con exito!")
            break

        if dato[3]==None :
            cursor.execute(f'UPDATE "{Tabla}" SET Dep4= (?) ', (Dep,))
            cursor.execute(f'CREATE TABLE "{Dep}" (COD REAL , NOM TEXT, CODRES TEXT, DepPadre TEXT, Dep1 TEXT, Dep2 TEXT, Dep3 TEXT, Dep4 TEXT, Dep5 TEXT)')
            cursor.execute(f'INSERT INTO "{Dep}" (COD, NOM,DepPadre) VALUES ( ? , ? , ? )', (1, Dep, Tabla))
            cursor.execute(f'CREATE TABLE "{DepP}" (COD REAL PRIMARY KEY, DOC TEXT , APE TEXT, NOM TEXT, TEL TEXT, DIR TEXT, DEP  TEXT, SAL REAL)')
            print("Dependencia creada con exito!")
            break

        if dato[4]==None :
            cursor.execute(f'UPDATE "{Tabla}" SET Dep5= (?) ', (Dep,))
            cursor.execute(f'CREATE TABLE "{Dep}" (COD REAL , NOM TEXT, CODRES TEXT, DepPadre TEXT, Dep1 TEXT, Dep2 TEXT, Dep3 TEXT, Dep4 TEXT, Dep5 TEXT)')
            cursor.execute(f'INSERT INTO "{Dep}" (COD, NOM,DepPadre) VALUES ( ? , ? , ? )', (1, Dep, Tabla))
            cursor.execute(f'CREATE TABLE "{DepP}" (COD REAL PRIMARY KEY, DOC TEXT , APE TEXT, NOM TEXT, TEL TEXT, DIR TEXT, DEP  TEXT, SAL REAL)')
            print("Dependencia creada con exito!")
            break

        print("No se pueden asignar mas Dependencias a ",Tabla)
        break

    conexion.commit()
    conexion.close()
    return True

def VerificarExistTabla(Base,Tabla):
    conexion = sqlite3.connect(Base)
    cursor = conexion.cursor()
    tabla = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    if Tabla not in tabla:
        bool=False
    else:
        bool=True

    conexion.close()
    return bool

def ModificarDep(Base,Dep):
    return 0

def DescendenciaDepExist(Base,Dep):
    conexion=sqlite3.connect(Base)
    cursor=conexion.cursor()
    Data = cursor.execute(f'SELECT Dep1 ,Dep2, Dep3, Dep4, Dep5 FROM "{Dep}"')
    dato=Data.fetchone()
    bool=False
    if dato[0] != None:
        bool=True

    if dato[1] != None:
        bool=True

    if dato[2] != None:
        bool=True

    if dato[3] != None:
        bool=True

    if dato[4] != None:
        bool=True

    conexion.close()
    return bool

def DescendenciaDepImp(Base,Dep):
    conexion = sqlite3.connect(Base)
    cursor = conexion.cursor()
    Data = cursor.execute(f'SELECT Dep1 ,Dep2, Dep3, Dep4, Dep5 FROM "{Dep}"')
    dato = Data.fetchone()

    if dato[0] != None:
        print(dato[0])
        DescendenciaDepImp(Base,dato[0])

    if dato[1] != None:
        print(dato[1])
        DescendenciaDepImp(Base,dato[1])

    if dato[2] != None:
        print(dato[2])
        DescendenciaDepImp(Base,dato[2])

    if dato[3] != None:
        print(dato[3])
        DescendenciaDepImp(Base,dato[3])

    if dato[4] != None:
        print(dato[4])
        DescendenciaDepImp(Base,dato[4])
    conexion.close()

def ImprimirDepTodas(Base):
    conexion=sqlite3.connect(Base)
    cursor=conexion.cursor()
    tabla=cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for T in tabla:
        print(T[0])

def EliminarDep(Base,Dep):
    conexion=sqlite3.connect(Base)
    cursor=conexion.cursor()
    Data = cursor.execute(f'SELECT Dep1 ,Dep2, Dep3, Dep4, Dep5, DepPadre FROM "{Dep}"')
    dato=Data.fetchone()
    #Verifica y halla cuales son las dependencias sucesoras de la base de datos
    if dato[0] != None:
        EliminarDep(Base,dato[0])

    if dato[1] != None:
        EliminarDep(Base,dato[1])

    if dato[2] != None:
        EliminarDep(Base,dato[2])

    if dato[3] != None:
        EliminarDep(Base,dato[3])

    if dato[4] != None:
        EliminarDep(Base,dato[4])
    DepP=Dep+"P"
    cursor.execute(f'DROP TABLE IF EXISTS "{DepP}"')
    cursor.execute(f'DROP TABLE IF EXISTS "{Dep}"')
    Data=cursor.execute(f'SELECT Dep1 ,Dep2, Dep3, Dep4, Dep5 FROM "{dato[5]}"')
    dato2=Data.fetchone()
    print(dato[5])
    for x in dato2:
        print(x)

    if dato2[0]==Dep:
        cursor.execute(f'UPDATE "{dato[5]}" SET Dep1= NULL ')

    if dato2[1]==Dep:
        cursor.execute(f'UPDATE "{dato[5]}" SET Dep2= NULL ')

    if dato2[2]==Dep:
        cursor.execute(f'UPDATE "{dato[5]}" SET Dep3= NULL ')

    if dato2[3]==Dep:
        cursor.execute(f'UPDATE "{dato[5]}" SET Dep4= NULL ')

    if dato2[4]==Dep:
        cursor.execute(f'UPDATE "{dato[5]}" SET Dep5= NULL ')

    conexion.commit()
    conexion.close()
    return dato[5]

def EliminarOrg(Base):
    ruta_archivo="C:\\Users\\marti\\OneDrive\\Escritorio\\Algoritmo 2\\Algoritmo 2\\Ejercicios Algoritmo 2\\Trabajo practico Arboles\\"+Base
    if os.path.isfile(ruta_archivo):
        os.remove(ruta_archivo)
        print("Organigrama eliminado con éxito.")
    else:
        print("El Organigrama no existe.")

def IngresarPersonas(Base,Dep,persona):
    conexion=sqlite3.connect(Base)
    cursor=conexion.cursor()
    DepP=Dep
    cursor.execute(f'INSERT INTO "{DepP}" (COD , DOC , APE , NOM , TEL , DIR , DEP , SAL) VALUES ( ? , ? , ? , ? , ? , ? , ? ,?)',(persona.COD, persona.DOC, persona.APE, persona.NOM, persona.TEL, persona.DIR, persona.DEP, persona.SAL))
    conexion.commit()
    conexion.close()

def ImprimirDepDatos(Base):
    conexion=sqlite3.connect(Base)
    cursor=conexion.cursor()
    Data=cursor.execute(f'SELECT * FROM {Base}')
    Datos=Data.fetchone()
    for Dato in Datos:
        print(Dato)

    conexion.close()
