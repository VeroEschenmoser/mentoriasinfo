import random

n= int (input("ingrese la cantidad de grupos a formar: " ))
def crear_grupos(nombres):
    grupos = [[] for _ in range(n)]  # Crear una lista de grupos vacíos
    
    # Mezclar los nombres
    nombres_mezclados = random.sample(nombres, len(nombres))
    
    # Asignar los nombres a los grupos
    for i, nombre in enumerate(nombres_mezclados):
        grupo = i % n  # Asignar a un grupo según el índice
        grupos[grupo].append(nombre)
    
    return grupos

# Solicitar el ingreso de nombres separados por comas
nombres = input("Ingresa los nombres separados por comas: ").split(",")

# Eliminar espacios en blanco alrededor de cada nombre
nombres = [nombre.strip() for nombre in nombres]

# Crear los grupos
grupos = crear_grupos(nombres)

# Imprimir los grupos
for i, grupo in enumerate(grupos):
    print(f"Grupo {i + 1}: {', '.join(grupo)}")




