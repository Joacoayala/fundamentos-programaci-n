# Desarrolla un programa en Python que permita ingresar dos números enteros que indiquen un rango numérico. El primer valor debe ser menor que el segundo. 
# El programa generará un número aleatorio dentro de ese rango. Luego, el usuario intentará adivinar el número generado en tres intentos.
#Si el usuario adivina en el primer intento, el programa mostrará el mensaje: "Felicitaciones, adivinaste en el primer intento."
#Si no acierta en el primer intento, el programa indicará si el número es mayor o menor que el intento del usuario.
#En el segundo intento, si el usuario no acierta, se volverá a indicar si el número es mayor o menor.
#Si el usuario no acierta en el tercer intento, el programa mostrará el mensaje: "Perdiste, el número era [número]."


def numero_aleatorio():
    
    import random
 
    
    print("bienvenido al juego de adivinar el numero")
    numero_rango1 = int(input("ingresa el primer numero para generar el rango numerico: "))
    numero_rango2 = int(input("ingresa el segundo numero para generar el rango numerico (debe ser mayor al primero): "))
        
    if numero_rango1 < numero_rango2:
        print("rango numerico generado")
             
    else:
     print("el primer numero debe ser menor al segundo")
        
    num_aleatorio = random.randint(numero_rango1, numero_rango2)
    
    intentos = 2
    
    while intentos >= 0: 
        intentos -= 1
        
        intento_usuario = int(input("ingresa un numero para adivinar, tienes 3 intentos: "))
        
        if num_aleatorio == intento_usuario:
            
            print("¡felicitaciones!, adivinaste el numero")
            break
                
        elif num_aleatorio < intento_usuario:
            
            print("el numero es menor al ingresado")
            
        elif num_aleatorio > intento_usuario:
                        
            print("el numero es mayor al ingresado")
        
    else: 
            print(f"superaste el maximo de intentos, el numero era {num_aleatorio}")
            

            
            

            
    
        
                
                
                    
                                
            
                            
                
                            
                            
                            
                            
                            
numero_aleatorio()
        
        
        
       


    
    