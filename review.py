# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.

import math

r = float(input("Ingrese el radio del círculo: "))
h = float(input("Ingrese la altura del cilindro: "))

def area(r):
    global a
    a = 3.1416 * math.pow(r,2)
    print(f"El área del círculo es {a}")
    volumen(a)

def volumen(a):
    vol = a * h
    print(f"El volumen del cilindro es {vol}")

area(r)
#volumen(h) El error de imprimir dos veces es porque area() ya imprime volumen() y yo la volvía a llamar.