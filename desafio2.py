texto = input("Ingrese un texto: ")
letras = input("Ingrese 3 letras separadas por un espacio: ").split()

# Convertir todo el texto a minúsculas para comparaciones posteriores
texto = texto.lower()

# Contar la cantidad de veces que aparece cada letra en el texto
cantidad_letras = [texto.count(letra.lower()) for letra in letras]

# Contar la cantidad de palabras en el texto
palabras = texto.split()
cantidad_palabras = len(palabras)

# Encontrar la primera letra y la última letra del texto
primera_letra = texto[0]
ultima_letra = texto[-1]

# Invertir el texto
texto_invertido = texto[::-1]

# Verificar si "python" está en el texto
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto
dic = {True:"sí", False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")

# Mostrar los resultados al usuario
print("Cantidad de veces que aparece cada letra: ", cantidad_letras)
print("Cantidad de palabras en el texto: ", cantidad_palabras)
print("Primera letra del texto: ", primera_letra)
print("Última letra del texto: ", ultima_letra)
print("Texto invertido: ", texto_invertido)


