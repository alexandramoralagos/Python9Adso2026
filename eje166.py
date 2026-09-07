estrato = int(input("Ingrese el estrato: "))
edad = int(input("Ingrese su edad: "))

if estrato == 1 and edad < 18:
    print("El descuento será del 20%")
elif estrato == 1 and edad >= 18:
    print("El descuento será del 15%")  
elif estrato == 2 and edad < 18:
    print("El descuento sera del 10%")
else:
    estrato == 2 and edad >=18
    print("El descuento sera del 5%")