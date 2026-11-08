#Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas 
frase = "A quién madruga Dios ayuda."
palabra = "MADRUGA"

indice = frase.lower().find(palabra.lower())

if indice != -1:
    print("La palabra aparece en el índice", indice)
else:
    print("La palabra no aparece en la frase.")