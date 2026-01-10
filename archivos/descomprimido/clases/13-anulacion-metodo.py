class Ave:
    def __init__(self):
        self.volador = "Volador"
    def vuela(self):
        print("El ave está volando")

class Pato(Ave):
    def vuela(self):
        super().__init__()
        self.nada = "Nadador"
        print("El pato está volando con estilo")
        super().vuela()


pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)