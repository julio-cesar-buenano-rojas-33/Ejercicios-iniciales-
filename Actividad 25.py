#Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos. 

nota = float(input("Introduce la nota de 0 a 10: "))

if nota < 0 or nota > 10:
    print("La nota debe estar entre 0 y 10")
elif nota >= 8.5 and nota <= 10:
    print("Excelente")
elif nota >= 6.5 and nota < 8.5:
    print("Notable")
elif nota >= 5 and nota < 6.5:
    print("Satisfactorio")
else:
    print("Insuficiente")