# Calculadora Cli proyect

# funciones

def suma(a,b):
    suma = a+b
    return suma

def resta(a,b):
    resta = a-b
    return resta

def multiplicacion(a,b):
    multiplicacion = a*b
    return multiplicacion

def division(a,b):
    if b == 0:
         return "error no se puede dividir por cero"    
    return a / b
def pedir_numero():
    try:
        a = float(input("Primer numero: "))
        b = float(input("Segundo numero: "))
        return a, b
    except ValueError:
        print("Entrada invalidad.")
        return None, None 
# menu

def menu():
    print("===calculadora===")
    print("1. suma (+)")
    print("2. resta (-)")
    print("3. multiplicacion (*)")
    print("4. dividir (/)")
    print("5. salir ")

# Cuerpo
def main():
    while True:
        menu()
        opcion = input("Ingrese su operacion: ")
    
        if opcion == "5":
            print("Adios...")
            break
    
        if opcion not in ("1", "2", "3", "4"):
            print("opcion no valida")
            continue
        
        a, b = pedir_numero()
        if a is None:
            continue

        if opcion == "1":
            resultado = suma(a,b)
        elif opcion == "2":
            resultado = resta(a,b)
        elif opcion == "3":
            resultado = multiplicacion(a,b)
        elif opcion == "4":
            resultado = division(a,b)

        print(f"resultado: {resultado}")

if __name__== "__main__":
    main()

