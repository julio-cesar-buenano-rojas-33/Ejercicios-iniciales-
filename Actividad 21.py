from math import sqrt

# Calcula las soluciones reales de una ecuación de segundo grado.
a = int(input("Introduce un número entero para la variable a: "))
b = int(input("Introduce un número entero para la variable b: "))
c = int(input("Introduce un número entero para la variable c: "))

if a == 0:
    print("No es una ecuación de segundo grado porque a no puede ser 0.")
else:
    r = b**2 - 4 * a * c

    if r < 0:
        print("La ecuación no tiene soluciones reales.")
    elif r == 0:
        x = -b / (2 * a)
        print(f"La ecuación tiene una única solución: {x}")
    else:
        x1 = (-b + sqrt(r)) / (2 * a)
        x2 = (-b - sqrt(r)) / (2 * a)
        print(f"Las soluciones son {x1} y {x2}.")
    