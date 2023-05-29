class Padre:

    def __init__(self, nombre, apellidoPaterno) -> None:
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno

class Madre:

    def __init__(self, nombre, apellidoMaterno) -> None:
        self.nombre = nombre
        self.apellidoMaterno = apellidoMaterno
        

class Hijo(Padre,Madre):
    def __init__(self, nombre, apellidoMaterno, apellidoPaterno) -> None:
        super().__init__( apellidoPaterno,  apellidoMaterno)
        self.nombre = nombre

Pedro = Hijo("Miguel", "Diaz", "Cabrera")
print(Pedro.nombre , Pedro.apellidoPaterno , Pedro.apellidoMaterno)