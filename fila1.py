import os
os.system('cls' if os.name == 'nt' else 'clear')

fila = []

fila.append('cliente1')
fila.append('cliente2')
fila.append('cliente3')
print("Los elementos de la fila son", fila)

Cliente_Atendido = fila.pop(0)
print("Cliente atendido fue", Cliente_Atendido)
print("Fila despues de atender un cliente son", fila)
