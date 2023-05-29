class Padre:

    def __init__(self, nombre) -> None:
        self.nombre = nombre

class Hijo(Padre):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)


jorge = Hijo("Jorge")
maria = Hijo("Maria")