#Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice. madruga 
frase = "A quién madruga Dios ayuda."
palabra = "madruga"

if palabra in frase:
    print("La palabra", palabra, "está en el índice", frase.find(palabra))
else:
    print("La palabra no aparece en la frase.")