from io import open

# Escritura
# texto = "Hola mundo"
# archivo = open("archivos/hol-mundo.txt", "w", encoding="utf-8")
# archivo.write(texto)
# archivo.close()

# Lectura
# archivo = open("archivos/hola-mundo.txt", "r", encoding="utf-8")
# texto = archivo.read()
# archivo.close()
# print(texto)

# Lectura como lista
# archivo = open("archivos/hola-mundo.txt", "r", encoding="utf-8")
# texto = archivo.readlines()
# archivo.close()
# print(texto)

# whit y seek
# with open("archivos/hola-mundo.txt", "r", encoding="utf-8") as archivo:
#     print(archivo.readlines())
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)

# Agregar
# archivo = open("archivos/hola-mundo.txt", "a", encoding="utf-8")
# archivo.write("\nChao mundo!")
# archivo.close()

# Lectura y escritura

with open("archivos/hola-mundo.txt", "r+", encoding="utf-8") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Chanchito Feliz!\n"
    print(texto)
    archivo.writelines(texto)