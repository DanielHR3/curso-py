class Animal:
    def comer(self):
        print("Comiendo")

class Perro(Animal):
    def pasear(self):
        print("Paseando")

class Chanchito(Perro):

    def programar(self):
        print("Programando")

Chanchito = Chanchito()
perro = Perro()
perro.pasear()
perro.comer()