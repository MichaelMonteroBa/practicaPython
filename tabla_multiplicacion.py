
def tabla_multiplicar(numero):
    print(f"La tabla del numero {numero}:")
    for i in range (1,11):
        resultado = numero * i
        print (f"{numero} x {i} = {resultado}")



numero = int(input("Ingrese un numero para mostrar su tabla de multiplicar: "))
tabla_multiplicar(numero)
