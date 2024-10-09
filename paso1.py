def suma(a, b):
    resultado = a + b
    print(f"La suma de {a} + {b} es: {resultado}")


def resta(a, b):
    resultado = a - b
    print(f"La resta de {a} - {b} es: {resultado}")


def multiplicacion(a, b):
    resultado = a * b
    print(f"La multiplicación de {a} * {b} es: {resultado}")


def calculadora():
    print("Bienvenido a la calculadora")
    print("Elige una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    
    opcion = int(input("Selecciona una opción (1/2/3): "))
    
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
    
    if opcion == 1:
        suma(a, b)
    elif opcion == 2:
        resta(a, b)
    elif opcion == 3:
        multiplicacion(a, b)
    else:
        print("Opción no válida")


calculadora()