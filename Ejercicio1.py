"""
Ejercicio 1 – Factorial recursivo

Crear una función recursiva que reciba N y calcule N!.

Ejemplo:


5! = 120


Identificar claramente:

Caso base.

Caso recursivo.
"""

def factorial(num):
    if num == 1 or num == 0:
        return 1
    res = num * factorial(num - 1)
    return res

print(factorial(5))