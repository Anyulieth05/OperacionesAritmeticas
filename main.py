def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Función para validar si el número ingresado es entero y positivo
def validar_numero(numero):
    try:
        numero_entero = int(numero)
        if numero_entero <= 0:
            raise ValueError
        return numero_entero
    except ValueError:
        print("Por favor, ingrese un número entero y positivo.")
        return None

# Solicitar al usuario que ingrese el primer número
while True:
    num1 = input("Ingrese el primer número entero y positivo: ")
    num1 = validar_numero(num1)
    if num1 is not None:
        break

# Solicitar al usuario que ingrese el segundo número
while True:
    num2 = input("Ingrese el segundo número entero y positivo: ")
    num2 = validar_numero(num2)
    if num2 is not None:
        break

# Calcular el máximo común divisor
mcd = calcular_mcd(num1, num2)
print("El máximo común divisor de", num1, "y", num2, "es:", mcd)