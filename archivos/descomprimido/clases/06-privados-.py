class Perro:
    def __init__(self, nombre: str, edad: int):
        self.__nombre = nombre
        self.__edad = edad

    def habla(self) -> None:
        print(f"{self.__nombre} dice: ¡Guau guau!")

    @classmethod
    def crear_perro_feliz(cls):
        return cls("Chanchito Feliz", 4)

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if not nuevo_nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nuevo_nombre

    @property
    def edad(self) -> int:
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad: int) -> None:
        if nueva_edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self.__edad = nueva_edad

    def __repr__(self) -> str:
        return f"Perro(nombre='{self.__nombre}', edad={self.__edad})"

    def to_dict(self) -> dict:
        return {"nombre": self.__nombre, "edad": self.__edad}


# Uso
perro1 = Perro.crear_perro_feliz()
perro1.habla()
print(perro1)

print("Nombre:", perro1.nombre)
perro1.nombre = "Firulais Stark"
print("Nuevo nombre:", perro1.nombre)

print("Edad:", perro1.edad)
perro1.edad = 5
print("Nueva edad:", perro1.edad)

print("Estado dict:", perro1.to_dict())
