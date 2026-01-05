from pathlib import Path

# Path(r"C:\Archivos de Programa\Minecraft")
# Path("/usr/bin")
# Path()
# Path.home()
# Path("one/__init__.py")

path = Path("hola-mundo/mi--archivo.py")
path.is_file()      # False
path.is_dir()       # True
path.exists()       # True

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
      )

p = path.with_name("chanchito.exe")

print(p)
p = path.with_suffix(".bat")
print(p)
p = path.with_stem("feliz")
print(p)