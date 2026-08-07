while True:

    palabra = input('dame una palabra... \n ')
    invertido = palabra [::-1]

    if palabra == invertido:
        print('es un palindromo')
    else:
        print('no es un palindromo')
    continuar = input('quieres continuar? (s/n) \n')
    if continuar != 's':
        break