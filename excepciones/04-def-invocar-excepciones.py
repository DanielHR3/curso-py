def division(n = 0):
    if n == 0:
        raise ZeroDivisionError("El valor de n no puede ser cero.", f"{n}")
    return 5/n

try:
    division(0)
except ZeroDivisionError as e:
    print(e)
