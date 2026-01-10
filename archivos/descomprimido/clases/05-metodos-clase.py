class Perro:
    patas = 4  # Atributo de clase

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Guau guau!")

    @classmethod
    def factory(cls):
        return Perro("Chanchito Feliz", 4)

Perro.habla()
perro1 = Perro("Chanchito", 1)
perro2 = Perro("Felipe", 2)
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre)