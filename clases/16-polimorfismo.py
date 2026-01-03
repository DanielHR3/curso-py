from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def guadar(self):
        pass



class Usuario(Model):
    def guadar(self):
        print("Guardando en BBDD")


class Sesion (Model):
    def guadar(self):
        print("Guardando archivo")


def guardar (entidades):
    for entidad in entidades:
        entidad.guadar()

usuario = Usuario()
sesion = Sesion()

guardar([sesion, usuario])