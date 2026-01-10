try:
    n1= int(input("Ingrese primer número: "))
except Exception as e:
    print("Ocurrió un error")
else:
    print("No hubo errores. El número ingresado es:", n1)
finally:
    print("Ejecución del bloque finally. Fin del programa.")