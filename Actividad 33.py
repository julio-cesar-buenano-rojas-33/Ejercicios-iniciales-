#Programa un código que permita contar el número de vocales de la siguiente frase: No hay mal que dure cien años 
frase = "No hay mal que dure cien años"
vocales = "aeiouáéíóú"
contador = 0

for letra in frase.lower():
    if letra in vocales:
        contador += 1

print("La frase tiene", contador, "vocales.")