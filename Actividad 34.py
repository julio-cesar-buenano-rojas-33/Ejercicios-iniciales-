#Corrige los 4 errores o añade el código que necesites para que el siguiente programa se ejecute correctamente 

var_numero = 6734
var_suma = 0

var_numero_texto = str(var_numero)
var_longitud = len(var_numero_texto)

for indice in range(var_longitud):
    var_suma += int(var_numero_texto[indice])

if var_suma % 2 == 0:
    print(f"El valor de {var_suma} es par")
else:
    print(f"El valor de {var_suma} es impar")