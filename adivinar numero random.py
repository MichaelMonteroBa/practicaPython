import random
numero_secreto = random.randint(1, 100)

print('a que no sabes que numero estoy pensando'.title())

entrada = int(input('Di tu numero: '))

while entrada < numero_secreto or entrada > numero_secreto:
    print('lo siento, ese no es el numero correcto. Intentalo de nuevo.'.upper())
    if entrada < numero_secreto:
        print('el numero que estoy pensando es mayor que el que ingresaste'.lower())
    elif entrada > numero_secreto:
        print('el numero que estoy pensando es menor que el que ingresaste'.lower())
    entrada = int(input('ingresa un numero: '))
    if entrada == numero_secreto:
        print('felicidades, has adivinado el numero secreto!'.title())