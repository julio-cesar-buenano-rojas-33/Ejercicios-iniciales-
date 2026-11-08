#mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla 

while True:
    letra = input("Introduce una letra: ")

    if len(letra) == 1 and letra.isalpha():
        break
    print("Debes introducir una sola letra, no un número.")

es_mayuscula = False

if letra.isupper():
    es_mayuscula = True

if letra.islower():
    es_mayuscula = False

print("La condición de mayúscula es:", es_mayuscula)