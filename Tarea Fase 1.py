import pandas as pd
import sys

Alumnos = {"Angel":[], "Pedro" :[], "Miguel" :[], "Mario" :[], "Julio" :[], \
                    "Imanol" :[], "Fernanda" :[], "Lizeth" :[], "Diana" :[], "Diego" :[], \
                    "Fernando" :[], "Oscar" :[], "Daniela" :[], "Karen" :[], "Franco" :[], \
                    "Isabel" :[], "Arick" :[], "Edson" :[], "Manuel" :[], "Arely" :[], "Gaby" :[], \
                    "Lalo" :[], "Saul" :[], "Karl" :[], "Carlos" :[], "Melisa" :[], \
                    "Susana" :[], "Andrea" :[], "Rebeca" :[]}

materias= ["Estadistica","Creatividad","Liderazgo","Estructura de datos",\
                 "Programacion de base de datos"]

op = 0
while op != 4:

    print("1.- Registrar Calificaciones")
    print("2.- Mostrar Calificaciones")
    print("3.- Mostrar alumnos reprobados")
    print("4.- Mostrar Estadistica descriptiva")
    print("5.- Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        for e in Alumnos:
            print("Nombre Alumno:",e)
            for i in materias:
                resultado1 = 0
                resultado1 = int(input("Cual es la calificacion?"))
                Alumnos[e].append(resultado1)
    elif opcion == 2:
        opcin2 = pd.DataFrame(Alumnos)
        opcin2.index = [materias]
        print(opcin2.T)
        
    elif opcion == 3:
        opcin2 = pd.DataFrame(Alumnos)
        opcin2.index = [materias]
        var1 = Alumnos.keys()
        for a in var1:
            variable_control = Alumnos.get(a,())
            print(" ")
            print("Alumno:",a)
            print("Reprobados")
            for e in variable_control:
                if e < 60:
                    print(e)
        
    elif opcion == 4:
        opcin2 = pd.DataFrame(Alumnos)
        opcin2.index= [materias]
        print("La media Estandart es")
        print(opcin2.T.std())
        print("El promedio es:")
        print(opcin2.T.mean)
        
    elif opcion == 5:
        exit()

    else:("Opcion no valida")
        
