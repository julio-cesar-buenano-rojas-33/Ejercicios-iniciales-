 #Corrige los errores del siguiente código y comprueba que se ejecuta correctamente 
peso = float(input("Introduce el peso: "))
altura = float(input("Introduce la altura: "))

imc = peso / altura**2

print(f"Si pesas {peso} kilos y mides {altura} metros, tu IMC es: {imc:.2f}")

if imc > 25:
    print("Hay sobrepeso")
else:
    print("Estás dentro de los parámetros normales")