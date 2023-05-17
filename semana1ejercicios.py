# ejercicio 1: Escribe un programa que solicite al usuario su nombre y lo imprima en la
# pantalla.
# nombre = input("Por favor, introduce tu nombre: ")
# print("Hola", nombre, "! Bienvenido/a a Python")

# 2-Escribe un programa que solicite al usuario su nombre y luego imprima un
# mensaje de bienvenida.

# # Pedimos al usuario que ingrese su nombre
# nombre = input("Ingrese su nombre: ")

# # Imprimimos un mensaje de bienvenida
# print("¡Bienvenido/a, " + nombre + "!")


# 3-Crea un programa que pida al usuario su edad y lo imprima en pantalla.

# # Pedimos al usuario que ingrese su edad
# edad = input("Ingrese su edad: ")

# # Imprimimos la edad en pantalla36
# print("Tu edad es: " + edad)



# 4-Crea un programa que calcule la suma de dos números y lo imprima en
# pantalla.

# # Pedimos al usuario que ingrese dos números
# numero1 = float(input("Ingrese el primer número: "))
# numero2 = float(input("Ingrese el segundo número: "))

# # Calculamos la suma de los números
# suma = numero1 + numero2

# # Imprimimos la suma en pantalla
# print("La suma de " + str(numero1) + " y " + str(numero2) + " es: " + str(suma))




# 5-Crea un programa que pida al usuario dos números enteros y muestre en
# pantalla su cociente y su resto.

# # Pedimos al usuario que ingrese dos números enteros
# dividendo = int(input("Ingrese el dividendo: "))
# divisor = int(input("Ingrese el divisor: "))

# # Calculamos el cociente y el resto
# cociente = dividendo // divisor
# resto = dividendo % divisor

# # Imprimimos el cociente y el resto en pantalla
# print("El cociente de " + str(dividendo) + " entre " + str(divisor) + " es: " + str(cociente))
# print("El resto de " + str(dividendo) + " entre " + str(divisor) + " es: " + str(resto))



# 6-Crea un programa que pida al usuario el radio de un círculo y calcule su área.
# La fórmula A = pi * r^2. Luego, muestra en pantalla el resultado.
# Supongamos que pi = 3.1416

# # Pedimos al usuario que ingrese el radio del círculo
# radio = float(input("Ingrese el radio del círculo: "))

# # Definimos el valor de pi
# pi = 3.1416

# # Calculamos el área del círculo
# area = pi * (radio ** 2)

# # Imprimimos el resultado en pantalla
# print("El área del círculo de radio " + str(radio) + " es: " + str(area))




# 7-Escribe un programa que calcule el área de un triángulo a partir de la base y la
# altura dadas.

# # Pedimos al usuario que ingrese la base y la altura del triángulo
# base = float(input("Ingrese la base del triángulo: "))
# altura = float(input("Ingrese la altura del triángulo: "))

# # Calculamos el área del triángulo
# area = (base * altura) / 2

# # Imprimimos el resultado en pantalla
# print("El área del triángulo de base " + str(base) + " y altura " + str(altura) + " es: " + str(area))



# 8-Crea un programa que pida al usuario el radio de un círculo y muestre su
# diámetro, su circunferencia y su área.
# Supón que pi es aproximadamente 3.14159.

# # Pedimos al usuario que ingrese el radio del círculo
# radio = float(input("Ingrese el radio del círculo: "))

# # Definimos el valor de pi
# pi = 3.14159

# # Calculamos el diámetro, la circunferencia y el área del círculo
# diametro = radio * 2
# circunferencia = 2 * pi * radio
# area = pi * (radio ** 2)

# # Imprimimos los resultados en pantalla
# print("El diámetro del círculo es: " + str(diametro))
# print("La circunferencia del círculo es: " + str(circunferencia))
# print("El área del círculo es: " + str(area))



# 9-Escribe un programa que solicite al usuario dos números y luego imprima la
# suma, la resta, la multiplicación y la división de los dos números.

# # Pedimos al usuario que ingrese dos números
# num1 = float(input("Ingrese el primer número: "))
# num2 = float(input("Ingrese el segundo número: "))

# # Realizamos las operaciones matemáticas
# suma = num1 + num2
# resta = num1 - num2
# multiplicacion = num1 * num2
# division = num1 / num2

# # Imprimimos los resultados en pantalla
# print("La suma de los dos números es: " + str(suma))
# print("La resta de los dos números es: " + str(resta))
# print("La multiplicación de los dos números es: " + str(multiplicacion))
# print("La división de los dos números es: " + str(division))



# 10-Crea un programa que pida al usuario una cantidad en dólares y la convierta a
# euros.
# Supón que el tipo de cambio es de 0.84 euros por dólar.

# # Pedimos al usuario que ingrese una cantidad en dólares
# dolares = float(input("Ingrese la cantidad en dólares: "))

# # Definimos la tasa de conversión
# tasa_conversion = 0.84  # 1 dólar estadounidense = 0.84 euros (valor aproximado en abril de 2023)

# # Convertimos los dólares a euros
# euros = dolares * tasa_conversion

# # Imprimimos el resultado en pantalla
# print(str(dolares) + " dólares equivalen a " + str(euros) + " euros.")


# 11-Crea un programa que pida al usuario una palabra y muestre en pantalla
# cuántas letras tiene.
# Pss psssss toma... .len()

# # Pedimos al usuario que ingrese una palabra
palabra = input("Ingrese una palabra: ")

# # Contamos la cantidad de letras en la palabra
cantidad_letras = len(palabra)

# # Imprimimos el resultado en pantalla
print("La palabra '" + palabra + "' tiene " + str(cantidad_letras) + " letras.")


# 12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato
# dd/mm/aaaa y luego imprima su edad en años.
# Utiliza la función .split()



# # Pedimos al usuario que ingrese su fecha de nacimiento en formato dd/mm/aaaa
# fecha_nacimiento = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")

# # # Separamos la fecha en día, mes y año utilizando la función split()
# dia, mes, anio = fecha_nacimiento.split('/')

# # # Convertimos los valores a enteros
# dia = int(dia)
# mes = int(mes)
# anio = int(anio)

# # # Calculamos la edad en años 
# fecha_actual = 2023- int(anio)
# edad = fecha_actual

# # # Imprimimos la edad en años
# print("Su edad es de", edad, "años.")



# 13-Escribe un programa que solicite al usuario su nombre y su edad, y luego
# imprima un mensaje que indique cuántos años tendrá el usuario en 10 años más.

# # Pedimos al usuario que ingrese su nombre y edad
# nombre = input("Ingrese su nombre: ")
# edad = int(input("Ingrese su edad: "))

# # Calculamos la edad en 10 años más
# edad_futura = edad + 10

# # Imprimimos un mensaje con la edad futura del usuario
# print("Hola", nombre + ", en 10 años tendrás", edad_futura, "años.")


# 14-Escribe un programa que solicite al usuario un número entero y luego
# imprima el doble y el triple de ese número.

# # Solicitamos al usuario un número entero
# numero = int(input("Ingrese un número entero: "))

# # Calculamos el doble y el triple del número
# doble = numero * 2
# triple = numero * 3

# # Imprimimos el doble y el triple del número
# print("El doble de", numero, "es", doble)
# print("El triple de", numero, "es", triple)

# 15-Escribe un programa que solicite al usuario una temperatura en grados
# Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
# La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32.

# # Solicitamos al usuario una temperatura en grados Celsius
# celsius = float(input("Ingrese una temperatura en grados Celsius: "))

# # Convertimos la temperatura a grados Fahrenheit utilizando la fórmula
# fahrenheit = (celsius * 1.8) + 32

# # Imprimimos la temperatura en grados Fahrenheit
# print("La temperatura equivalente en grados Fahrenheit es:", fahrenheit)


# 16-Escribe un programa que solicite al usuario su peso y su altura, y luego calcule
# e imprima su índice de masa corporal (IMC).
# La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).

# # Solicitamos al usuario su peso en kg y su altura en metros
# peso = float(input("Ingrese su peso en kg: "))
# altura = float(input("Ingrese su altura en metros: "))

# # Calculamos el IMC utilizando la fórmula
# imc = peso / (altura ** 2)

# # Imprimimos el resultado del IMC redondeado a 2 decimales
# print("Su índice de masa corporal (IMC) es:", imc)




# 17-Escribe un programa que solicite al usuario dos palabras y luego las imprima
# en orden inverso.
# Por ejemplo, si el usuario ingresa "hola" y "mundo", el programa debe imprimir
# "mundo hola".

# # Solicitamos al usuario dos palabras
# palabra1 = input("Ingrese la primera palabra: ")
# palabra2 = input("Ingrese la segunda palabra: ")

# # Imprimimos las palabras en orden inverso
# print(palabra2 + " " + palabra1)


# 18-Crea un programa que pida al usuario su nombre, su edad y su ciudad de
# residencia, y lo muestre en pantalla Utilizando una sola línea de código.
# *Recuerda el print() del ejercicio anterior

# # Solicitamos al usuario su nombre, edad y ciudad de residencia
# nombre,edad,ciudad = input("Ingrese su nombre, Ingrese su edad, Ingrese su ciudad de residencia separados por una coma  ")split(",")


# # Mostramos los datos del usuario en una sola línea de código
# print(f"El usuario {nombre}, de {edad} años, reside en la ciudad de {ciudad}.")



# 19-Escribe un programa que solicite al usuario un número decimal y luego
# imprima la parte entera y decimal por separado

num = float(input("Ingrese un número decimal: "))
parte_entera = int(num)
parte_decimal = num - parte_entera

print("La parte entera del número es:", parte_entera)
print("La parte decimal del número es:", parte_decimal)
