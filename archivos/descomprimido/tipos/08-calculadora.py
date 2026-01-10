n1 = input("Digite primer número: ")
n2 = input("Digite segundo número: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

mensaje = f"""
Paral los números {n1} y {n2},
el resultado de la suma es {suma}.
El resultado de la resta es {resta}.
El resultado de la multiplicación es {multiplicacion}.
El resultado de la división es {division}.
"""

print(mensaje)
