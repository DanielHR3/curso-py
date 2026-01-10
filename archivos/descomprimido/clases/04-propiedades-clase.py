class Perro:
    patas = 4  # Atributo de clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice:  Guau guau!")

Perro.patas = 3  # Modificando el atributo de clase
mi_perro = Perro("Chanchito", 1)
mi_perro.patas = 5  # Modificando el atributo de instancia
mi_perro2 = Perro("Panchito", 1)
print(Perro.patas)
print(mi_perro.patas)
print(mi_perro2.patas)
