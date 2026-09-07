Instructora = "Valery"
nota1 = 40
nota2 = 30
nota3 = 50

def calcular():
    global total
    total = nota1 + nota2 + nota3
    
calcular()
print("la suma total de las notas del aprendiz Andres:", total)
print("calificado por la instructora:", Instructora)
