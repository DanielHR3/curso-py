import csv
import os

# Leer
with open("archivos/archivo.csv", "r", newline="", encoding="utf-8") as archivo:
    reader = csv.reader(archivo)
    for linea in reader:
        print(linea)

# Actualizar CSV (reemplaza la fila con twit_id 1000)
with open("archivos/archivo.csv", "r", newline="", encoding="utf-8") as r, \
     open("archivos/archivo_temp.csv", "w", newline="", encoding="utf-8") as w:

    reader = csv.reader(r)
    writer = csv.writer(w)

    for linea in reader:
        # Evita líneas vacías
        if not linea:
            continue

        if linea[0] == "1000":
            writer.writerow([1000, 1, "Texto modificado"])
        else:
            writer.writerow(linea)

# Reemplazo seguro (mejor que remove + rename)
os.replace("archivos/archivo_temp.csv", "archivos/archivo.csv")
