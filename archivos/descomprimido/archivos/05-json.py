import json
from pathlib import Path

# escribir json
# productos = [
#     {"id": 1, "name": "Surfboard"},
#     {"id": 2, "name": "Bicicleta"},
#     {"id": 3, "name": "Skate"},
# ]

# data = json.dumps(productos, ensure_ascii=False, indent=2)
# print(data)

# # ✅ Guardar en archivo
# ruta = Path("archivos/productos.json")
# ruta.parent.mkdir(parents=True, exist_ok=True)  # por si no existe la carpeta "archivos"
# ruta.write_text(data, encoding="utf-8")

# print("Archivo guardado:", ruta.resolve())
 # Leer json

data = Path("archivos/productos.json").read_text(encoding="utf-8")

productos = json.loads(data)

# Modificar json
productos[0]["name"] = "Chanchito feliz"
Path("archivos/productos.json").write_text(json.dumps(productos), encoding="utf-8")