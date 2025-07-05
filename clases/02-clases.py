class Perro:
    def habla(self):
        print("Guau guau")


mi_perro = Perro()
mi_perro.habla()  # Imprime: Guau guau
print(isinstance(mi_perro, Perro))  # Imprime: True