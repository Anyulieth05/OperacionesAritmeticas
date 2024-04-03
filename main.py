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

# Solicitar al usuario que ingrese los números
numeros = [None, None]

for i in range(2):
    while True:
        numero = input(f"Ingrese el {'primer' if i == 0 else 'segundo'} número entero y positivo: ")
        numeros[i] = validar_numero(numero)
        if numeros[i] is not None:
            break

num1, num2 = numeros

# Calcular el máximo común divisor
mcd = calcular_mcd(num1, num2)
print("El máximo común divisor de", num1, "y", num2, "es:", mcd)