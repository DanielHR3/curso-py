


class Usuario():
    def guadar(self):
        print("Guardando en BBDD")


class Sesion ():
    def guadar(self):
        print("Guardando archivo")


def guardar (entidades):
    for entidad in entidades:
        entidad.guadar()

usuario = Usuario()
sesion = Sesion()

guardar([sesion, usuario])