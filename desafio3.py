from random import randint

intentos = 0
estimado = 0
num_secreto = randint(1,100)
nombre = input('Ingresa tu nombre: ')

print(f'{nombre}, he pensado un numero entero entre 1 y 100')

while intentos < 8:

    print(f'Tienes {8 - intentos } intentos')
    estimado = input('Cual es el numero ?: ')

    if estimado.isdigit():
        estimado = int(estimado)
        intentos += 1

        if estimado < num_secreto:
            print('Mi numero es mas alto')
        elif estimado > num_secreto:
            print('Mi numero es mas bajo')
        else:
            print(f'Felicitaciones {nombre}! Has adivinado en {intentos} intentos')
            break
    else:
        print(f'{estimado} No es un numero entero')

else:
    print(f'Lo siento, se han agotado los intentos. El numero secreto era {num_secreto}')