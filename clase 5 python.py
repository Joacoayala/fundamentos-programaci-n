def descuento_matricula():
    Nombre =  input("ingresa tu nombre: ")
    print(f"bienvenido: {Nombre}")
    #calificaciones
    Calificacion =  float(input("ingresa tu calificacion: "))
    if Calificacion >= 6:
        print("!felicitaciones¡, tienes un descuento para tu matricula del 20%")
    elif Calificacion >= 5:
        print("!buena calificacion¡, tienes un descuento de tu matricula del 15%")
    elif Calificacion >= 4:
        print("¡sigue practicando!, tienes un descuento en tu matricula del 10%")
    else:
        print("reprobado")



descuento_matricula()

