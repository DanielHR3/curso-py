from pathlib import Path

path = Path("rutas")
# path.exists()   # False
# path.mkdir()     # Crea el directorio
# path.rmdir()    # Elimina el directorio
# path.rename("chanchito-feliz")

archivos = [p for p in path.iterdir() if not p.is_dir()]
archivos = [p for p in path.glob("01*.py")]
archivos = [p for p in path.glob("**/*.py")]
print(archivos)