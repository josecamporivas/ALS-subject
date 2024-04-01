class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Excepciones
try:
    x = input("Ingrese un número: ")
    y = int(x)
    print(5 / y)
    raise Exception("Esto es un error")
except ZeroDivisionError:
    print(f'{Bcolors.FAIL}No se puede dividir por cero{Bcolors.ENDC}')
except ValueError as e:
    print(f'{Bcolors.FAIL}Tienes que ingresar un número entero{Bcolors.ENDC}')
except:
    print("Error capturando cualquier excepción")
finally:
    print(f"{Bcolors.HEADER}Este bloque se ejecuta siempre{Bcolors.ENDC}")

# Aserciones: si la expresión es false, se detiene el programa y se visualiza un mensaje de error
try:
    x = 6
    assert x == 5, "x debe ser 5"
    print("x es 5")
except AssertionError as e:
    print(f'{Bcolors.FAIL}{e}{Bcolors.ENDC}')

"""
$python -O clase7.py # Ejecuta el programa sin las aserciones
"""

if __debug__:
    print("Debug depuración")
else:
    print("Debug despliegue")
