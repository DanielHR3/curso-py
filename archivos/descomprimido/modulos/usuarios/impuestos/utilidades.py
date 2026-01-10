if __name__ != "__main__":
    from ..gestion.crud import guardar

    print(__name__)

    def pagar_impuestos():
        print("Pagando impuestos...")
        guardar()

if __name__ == "__main__":
    print("Módulo de utilidades de impuestos cargado.")