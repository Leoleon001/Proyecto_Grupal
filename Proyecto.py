from Funciones import *
from Clases import *
import sqlite3
import os

print("Bienvenido al programa de organigramas!")
men=0
persAux = Personas
while True:

    print("""Que es lo que desea hacer?
1-Crear un Organigrama
2-Abrir un Organigrama
3-Eliminar un Organigrama
4-Salir""")
    Selec = int(input(""))
    while True:
        if Selec==1 :
            Base=CrearOrg()
            BaseD=Base+".db"
            print("Organigrama Creado con exito!")
            print("Ingrese el nombre de la primera dependencia que desea agregar: ",end="")
            while True:
                Dep = input()
                if CrearDep(BaseD,"Organigrama",Dep):
                    break
            AgregarNombres(Base)
            men=1
            break

        if Selec==2 :
            print("Ingrese el nombre del organigrama que desea abrir")
            while True:
                ImprimirNombres()
                Base=input()
                archivo=open("Nombres_Organigrama.txt",'r')
                Lineas=archivo.readlines()
                archivo.close()
                Base2=Base+"\n"
                if Base2 not in Lineas:
                    print("El organigrama ingresado no existe")
                    print("Favor ingrese un nombre valido de la lista")
                else:
                    break

            BaseD=Base+".db"
            men=1
            break

        if Selec==3 :
            print("Que organigrama deseas Eliminar?")
            while True:
                ImprimirNombres()
                Base=input()
                archivo = open("Nombres_Organigrama.txt", 'r')
                Lineas = archivo.readlines()
                archivo.close()
                Base2=Base+"\n"
                if Base2 not in Lineas:
                    print("El organigrama ingresado no existe")
                    print("Favor ingrese un nombre valido de la lista")
                else:
                    break

            BaseD=Base+".db"
            EliminarOrg(BaseD)
            EliminarNombres(Base)
            break

        if Selec==4 :
            break

        print("Error, favor elija una opcion")
        break

    while men==1:
        Menu(Base)
        Opcio=int(input())
        if Opcio==1:
            print("Ingrese el nombre de la dependencia que va a crear: ")
            Dep=input()
            print("Ingrese la tabla de la cual va a descender: ")
            while True:
                ImprimirDepTodas(BaseD)
                Tabla=input()
                if Tabla!=None:
                    if VerificarExistTabla(BaseD,Tabla):
                        print("La Dependencia que usted eligio no existe, favor elija otra")
                    else:
                        break
                else:
                    print("Favor elija una dependencia: ")
            CrearDep(BaseD,Tabla,Dep)

        if Opcio==2:
            print("Ingrese la dependencia a eliminar\nOBS: SE ELIMINARAN TODAS LAS DESCENDENCIAS SUBSECUENTES ")
            while True:
                ImprimirDepTodas(BaseD)
                Tabla = input()
                if Tabla!=None:
                    if VerificarExistTabla(BaseD,Tabla):
                        print("La Dependencia que usted eligio no existe, favor elija otra")
                    else:
                        break
                else:
                    print("Favor elija una dependencia: ")
            print("Esta seguro que desea eliminar",Tabla,"?")
            if DescendenciaDepExist(BaseD,Tabla):
                print("Se eliminaran las siguientes Dependencias: ")
                DescendenciaDepImp(BaseD,Tabla)
            print("Y/N")
            validar=input()
            if validar=='Y' or validar=='y':
                EliminarDep(BaseD,Tabla)
                print("Se elimino la Dependencia ",Tabla,"y todas sus dependencias sucesoras ")


        if Opcio==3:
            print("Ingrese la dependencia que desea modificar:")
            while True:
                DescendenciaDepImp(BaseD, Dep)
                dep=input()
                if dep!=None:
                    conexion = sqlite3.connect(Base)
                    cursor = conexion.cursor()
                    boole=True
                    while boole:
                        Data = cursor.execute(f'SELECT Dep1 ,Dep2, Dep3, Dep4, Dep5 FROM "{Dep}"')

        if Opcio==6:
            print("Ingrese en que dependencia quiere ingresar a la Persona ")
            ImprimirDepTodas(BaseD)
            Dep=input()
            print("Ingrese los datos de la persona a ser ingresada: ")
            persAux.COD=int(input("Ingrese el codigo de la persona: "))
            persAux.DOC=input("Ingrese la cedula de la persona: ")
            persAux.NOM=input("Ingrese el nombre de la persona: ")
            persAux.APE=input("Ingrese el apellido de la persona: ")
            persAux.TEL=input("Ingrese el numero de telefono la persona: ")
            persAux.DIR=input("Ingrese donde vive esa persona: ")
            persAux.DEP=Dep
            persAux.SAL=input("Ingrese el salario neto de la persona: ")
            IngresarPersonas(BaseD,Dep,persAux)
            print("La persona ha sido añadida a ",Dep," exitosamente!")

        if Opcio==11:
            men=0
            break


    if Selec==4:
        print("Gracias por usar un programa de Martin y Asociados!")
        break