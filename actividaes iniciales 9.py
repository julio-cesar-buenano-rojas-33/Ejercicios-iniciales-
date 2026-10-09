 #Programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas 
segundos_totales = int(input("Introduce los segundos: "))
horas = segundos_totales // 3600
minutos =(segundos_totales % 3600) // 60
segundos_restantes = segundos_totales % 60
print(f"{segundos_totales} segundos equivalen a {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")