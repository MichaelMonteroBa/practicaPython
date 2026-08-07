while True:
 
    palabra = input('deme una palabra... \n')
    vocales = 'aeiouAEIOU'

    print(f'la palabra {palabra} tiene {sum(1 for letra in palabra if letra in vocales)} vocales')
    continuar = input('quieres continuar? (s/n) \n')
    if continuar != 's':
        break