while True:
    letra = input("Introduce una letra: ")

    if len(letra) != 1:
        print("Introduce solo un carácter.")
    elif letra.isalpha():
        break
    elif letra.isdigit():
        print("Has introducido un número, no una letra.")
    else:
        print("Has introducido un símbolo, no una letra.")

es_mayuscula = False

if letra.isupper():
    es_mayuscula = True

if letra.islower():
    es_mayuscula = False

print("La condición de mayúscula es:", es_mayuscula)