# Desafío 1:
# Trabajas en una empresa X donde sus vendedores cobran comisiones del 6% de
# sus ventas totales y el departamento comercial te solicita que ayudes a los
# vendedores a calcular sus comisiones creando un programa que les pregunte su
# nombre y cuánto han vendido en éste mes.
# Tu programa le va a responder con una frase que incluya su nombre y el monto
# que le corresponde por las comisiones


# nombre = input("Ingresa tu nombre: ")
# ventas = float(input("Ingresa tus ventas del mes: "))
# comision = ventas * 0.06
# print(f"{nombre}, tu comisión por ventas del mes es de ${comision:.2f}")



# Desafio 2
# Escribe un programa que solicite al usuario su información personal, incluyendo
# su nombre completo, edad, estatura, peso, dirección y número de teléfono.
# A continuación, el programa deberá imprimir un mensaje con los datos
# ingresados por el usuario en el siguiente formato:
# La información ingresada es la siguiente:
# Nombre completo: [nombre completo]
# Edad: [edad]
# Estatura: [estatura] cm
# Peso: [peso] kg
# Dirección: [dirección]
# Número de teléfono: [número de teléfono]


nombre_completo = input("Ingrese su nombre completo: ")
edad = input("Ingrese su edad: ")
estatura = input("Ingrese su estatura en cm: ")
peso = input("Ingrese su peso en kg: ")
direccion = input("Ingrese su dirección: ")
telefono = input("Ingrese su número de teléfono: ")

print("La información ingresada es la siguiente:")
print("Nombre completo:", nombre_completo)
print("Edad:", edad)
print("Estatura:", estatura, "cm")
print("Peso:", peso, "kg")
print("Dirección:", direccion)
print("Número de teléfono:", telefono)

