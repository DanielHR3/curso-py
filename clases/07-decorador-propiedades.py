class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    @property
    def nombre(self):
        print("Llamando al getter de nombre")
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        print("Llamando al setter de nombre")
        if nombre.strip():
            self.__nombre = nombre
            return

perro = Perro("choclo")
print(perro.nombre)  # Output: choclo