#A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados _números entre 0 y 10 
lista_num = (1, 2, 3, 4, 5 , 6, 7, 8 ,9, 10)
variable_numero_1=float(input("introduce el primer número:"))
variable_numero_2=float(input("introduce el segundo número:"))
if variable_numero_1 or variable_numero_2 != lista_num:
    print("el valor no existe")
else:
    if variable_numero_1<variable_numero_2: 
        print(f"el valor {variable_numero_2} es mayor que el valor {variable_numero_1}")
    if variable_numero_1>variable_numero_2: 
        print(f"el valor {variable_numero_1} es mayor que el valor {variable_numero_2}")
    if variable_numero_1 == variable_numero_2:
        print(f"el valor {variable_numero_1} y {variable_numero_2}, son iguales")