from pathlib import Path
from time import ctime

archivo = Path("archivos/archivo-prueba.txt")
# archivo.exists()  # Verifica si el archivo existe
# archivo.rename()
# archivo.unlink()  # Elimina el archivo

#print(archivo.stat())

print("acceso", ctime(archivo.stat().st_atime))
print("creación", ctime(archivo.stat().st_ctime))
print("modificación", ctime(archivo.stat().st_mtime))