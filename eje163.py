estado_civil = input ("Ingrese estado civil (s,c):")
edad = int(input("ingrese edad:"))
buena_persona = input("Es buena persona? (s,n):")
linda = input ("es linda? (s,n):")
if estado_civil =="c":
    print ("No se caso! ni me comprometo")
elif edad<= 30 and linda == "s" or buena_persona =="s":
    print("si me caso!")
else:
    print ("solo me comprometo")