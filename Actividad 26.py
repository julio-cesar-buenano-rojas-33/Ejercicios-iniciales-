#Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición. 

letra = input("Introduce una letra: ")
es_mayuscula = False

if letra.isupper():
    es_mayuscula = True

if letra.islower():
    es_mayuscula = False

print("La condición de mayúscula es:", es_mayuscula)