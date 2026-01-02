class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"chao perro {self.nombre}")

    def __str__(self):
        return f"Clase Perro: {self.nombre} ({self.edad} años)"

    def habla(self):
        print(f"{self.nombre} dice guau guau")


perro = Perro("Chanchito", 3)
del perro  # Output: chao perro Chanchito