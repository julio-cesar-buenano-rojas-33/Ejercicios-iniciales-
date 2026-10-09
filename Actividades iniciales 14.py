#Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área 
#y perímetro. Importa la librería math y utiliza el valor PI para hacer el cálculo. Redondea el 
#resultado a un decimal. 
import math
diametro = float(input("Introduce el diámetro del círculo: "))
radio = diametro / 2
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
area_redondeada = round(area, 1)
perimetro_redondeado = round(perimetro, 1)
print(f"El área del círculo es: {area_redondeada}")
print(f"El perímetro del círculo es: {perimetro_redondeado}")