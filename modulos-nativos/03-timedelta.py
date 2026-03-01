from datetime import datetime, timedelta

fecha1 = datetime(2023, 1, 1)
fecha2 = datetime(2023, 2, 1)

delta = fecha2 - fecha1
print(delta)
print(delta.days, "días")
print(delta.seconds, "segundos")
print(delta.microseconds, "microsegundos")
print(delta.total_seconds(), "total_seconds()")