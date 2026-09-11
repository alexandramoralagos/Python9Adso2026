print("CALCULO DE AREAS")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

continuar = "s"

while continuar == "s":

    print("1. Cuadrado")
    print("2. Circulo")
    print("3. Rectangulo")
    print("4. Triangulo")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        lado = input("Ingrese el lado: ")

        if lado.isdigit():
            lado = float(lado)
            area = lado * lado
            print("El area del cuadrado es:", area)
        else:
            print("Solo se permiten numeros")

    elif opcion == "2":

        radio = input("Ingrese el radio: ")

        if radio.isdigit():
            radio = float(radio)
            area = 3.1416 * radio * radio
            print("El area del circulo es:", area)
        else:
            print("Solo se permiten numeros")

    elif opcion == "3":

        base = input("Ingrese la base: ")
        altura = input("Ingrese la altura: ")

        if base.isdigit() and altura.isdigit():
            base = float(base)
            altura = float(altura)
            area = base * altura
            print("El area del rectangulo es:", area)
        else:
            print("Solo se permiten numeros")

    elif opcion == "4":

        base = input("Ingrese la base: ")
        altura = input("Ingrese la altura: ")

        if base.isdigit() and altura.isdigit():
            base = float(base)
            altura = float(altura)
            area = (base * altura) / 2
            print("El area del triangulo es:", area)
        else:
            print("Solo se permiten numeros")

    else:
        print("Opcion incorrecta")

    continuar = input("Desea continuar? s/n: ")

print("Programa finalizado")
print("Nombre:", nombre)
print("Apellido:", apellido)