op = 0
while op != 4:
    print("1 para ver a los alumnos")
    print("2 para editar califiaciones")
    print("3 para ver la estadistica descriptiva de las materias en el periodo")
    print("4 para ver a los alumnos con calificacion reprobada")
    print("0 para salir")
    
    Desarrollo2= int(input("Que proceso quieres realizar:"))
    if Desarrollo2 ==1:
            print(concatenacion.iloc[:,0])
                     
    elif Desarrollo2 == 2:
            for i in range(3):
                Nombres:Alumnokeys.iloc[Numero2,0]
                c1= int(input("Ingresa la calificacion de Estadistica: "))
                c2= int(input("Ingresa la calificacion de Creatividad: "))
                c3= int(input("Ingresa la calificacion de Liderazgo: "))
                c4= int(input("Ingresa la calificacion de Estructura de datos: "))
                c5= int(input("Ingresa la calificacion de Programacion de base de datos: "))
                concatenacion.loc[Numero1] = [Numero2,c1,c2,c3,c4,c5]
                Numero1 = Numero1+1
                Numero2 = Numero2+1
                Numero3 = Numero3+1
                print(concatenacion)
    elif Desarollo3 == 3:
        
        