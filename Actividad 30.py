#Realiza un programa que controle si la longitud de una frase introducida por teclado es igual, menor o mayor de 11 caracteres. Utiliza elif 

frase = input("Introduce una frase: ")
longitud = len(frase)

if longitud == 11:
    print("La frase tiene exactamente 11 caracteres.")
elif longitud < 11:
    print("La frase tiene menos de 11 caracteres.")
else:
    print("La frase tiene más de 11 caracteres.")
 