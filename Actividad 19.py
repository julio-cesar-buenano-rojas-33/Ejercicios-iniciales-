#Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales.
variable_número_1=int(input("introduce el primer número:"))
variable_número_2=int(input("introduce el segundo número:"))
if variable_número_1<variable_número_2:
    print(f"el número {variable_número_2} es el mayor que el número {variable_número_1}")
if variable_número_1>variable_número_2:
    print(f"el número {variable_número_1} es el mayor que el número {variable_número_2}")
if variable_número_1==variable_número_2: 
    print("los dos número son iguales")
    