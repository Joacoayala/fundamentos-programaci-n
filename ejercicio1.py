def contador_de_edad():

    fecha_de_nacimiento_consola_texto = input("ingresa tu año de nacimiento: ")
    edad = 2025
    fecha_nacimiento_numero = int(fecha_de_nacimiento_consola_texto)
    edad_actual = edad - fecha_nacimiento_numero
    print(f"tu edad actual es: {edad_actual}")
    if edad_actual>= 18:
        print("eres mayor de edad")
    else: 
        print("eres menor de edad")
    
contador_de_edad()








