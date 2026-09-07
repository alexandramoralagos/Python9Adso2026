valor_inicial = int(input("Ingrese el número base: "))
valor_multiplicar = int(input("Ingrese el límite a multiplicar: "))

print(f"\nTabla del {valor_inicial}:")
for i in range(1, valor_multiplicar + 1):
    print(f"{valor_inicial} x {i} = {valor_inicial * i}")