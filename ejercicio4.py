def sistemas_descuento():
    Precio = int(input("ingresa el precio del producto: "))
    
    print("¿eres estudiante?")
    print("ingresa 1 si eres estudiante o 0 si no lo eres: ")
    opcion1 = int(input("ingresa una opccion: "))
   
    
    if opcion1 == 1:
        print("¡eres estudiante!")
    else:
        print("no eres estudiante")
        
    print("¿es dia de descuento?")
    print("1 = si, 0 = no")
    opcion2 = int(input("ingresa una opcion: "))
    
    
    if opcion2 == 1 and opcion1 == 1:
        print("¡es dia de descuento!")
        precio_25 = Precio * 25 / 100
        precio25_total = Precio - precio_25
        print(f"el tu producto con el 25% de descuento queda en : {precio25_total}")
        
    else:
        print("no es dia de descuento")
        
        Precio_20 = Precio * 20 / 100
        total_20 = Precio - Precio_20
    
        print(f"tu producto con el 20% de descuento queda en: {total_20} ")
   
  
    
  
sistemas_descuento()
    
    
    
    
    
    