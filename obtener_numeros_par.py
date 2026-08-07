# Obtener números pares e impares

# funciones

def obtener_numeros_par_impar(b):
    if b % 2 == 0:
        return "El numero es par"
    elif b % 2 == 1:
        return "El numero es impar"

def pedir_numero():
    try:
        a = int(input("Ingrese un numero: "))
        return a
    except ValueError:
        print("Entrada invaidada.")
        return None

# cuerpo funcion

def menu():
    print("===Saber si es par o impar===")
    print("1. Saber si es par o impar")
    print("2. salir")

def seleccionar_opcion():
    opcion = input("Ingrese su opcion: ")
    if opcion not in ("1", "2"):
        print("Opcion no valida.")
        return None
    return opcion

# cuerpo
while True:
   
    menu()
    opcion = input("Ingrese su opcion: ")


    if opcion == "1":
        numero = pedir_numero()
        if numero is not None:
            resultado = obtener_numeros_par_impar(numero)
            print ("numero ingresado: ", {numero})
            print("resultado: ", {resultado})
        else:
            print("No se pudo procesar el numero ingresado.")

    elif opcion == "2":
        print("Adios...")
        break
    else:
        print("Opcion no valida.")