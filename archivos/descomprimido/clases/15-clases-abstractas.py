from abc import ABC, abstractmethod

class Model(ABC):
    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(cls, _id):
        # Creamos una instancia para poder acceder a la property 'tabla'
        instancia = cls()
        print(f"Buscando por id {_id} en la tabla {instancia.tabla}")


class Usuario(Model):

    @property
    def tabla(self):
        return "Usuario"

    def guardar(self):
        print("Guardado usuario en BBDD")


usuario = Usuario()
Usuario.buscar_por_id(5)
usuario.guardar()
