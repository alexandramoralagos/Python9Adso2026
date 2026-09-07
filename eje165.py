conexion = float(input("Ingrese la velocidad de conexión en Mbps: "))

if conexion > 20:
    print("La velocidad de descarga será de 10 Mbps")
elif conexion >= 5:
    print("La velocidad de descarga será de 5 Mbps")
else:
    print("La velocidad de descarga será de 1 Mbps")