"""
Ejercicio 2 – Suma de números

Crear una función recursiva que calcule:


1 + 2 + 3 + ... + N


Ejemplo:


N = 5
Resultado = 15
"""

def suma(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
    return num + suma(num - 1)

print(suma(1))