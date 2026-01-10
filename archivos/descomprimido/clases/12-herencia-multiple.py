class Animal:
    def comer(self):
        print("comiendo")

    def pasear(self):
        print("paseando animales")


class Perro:
    def pasear(self):
        print("paseando al perro")


class Chanchito( Perro, Animal ):
    def programar(self):
        print("programando")

chanchito = Chanchito()
chanchito.pasear()