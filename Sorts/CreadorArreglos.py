import random

# Generar el arreglo aleatorio
arregloRandom = [random.randint(1, 9000000000) for _ in range(10000)]

# Escribir el arreglo al archivo con formato de lista
with open("arregloRandom.txt", "w") as file:
    file.write(str(arregloRandom))  # Convierte el arreglo a su representación en cadena

print("Array successfully written to arregloRandom.txt")
