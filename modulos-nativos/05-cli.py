import os
from pathlib import Path
import sys


def cli(args):
    if len(args) ==1:
        print("No se pasaron argumentos")
        return
    if len(args) != 3:
        print("Se necesitan 2 argumentos")
        return

    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print("El archivo no existe")
        return

    destino = args[2]
    d = Path(destino)
    if d.exists():
        print("El destino no puede existir")
        return

    os.rename(str(origen), str(destino))
    print("Archivo renombrado exitosamente")



cli(sys.argv)