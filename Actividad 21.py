# Programa que calcula una ecuación de segundo grado y controla el discriminante.

import math

a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

if a == 0:
    print("El valor de a no puede ser 0: no es una ecuación de segundo grado.")
else:
    discriminante = b**2 - 4 * a * c

    if discriminante < 0:
        print("No hay soluciones reales: no se puede calcular la raíz cuadrada de un número negativo.")
    elif discriminante == 0:
        x = -b / (2 * a)
        print("Hay una única solución:", x)
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        print("Las soluciones son:", x1, "y", x2)