
class Semilla:
    def __init__(self,tamaño):
        self.tamaño = tamaño
    
class Planta(Semilla):
    def __init__(self, tamaño, colorHojas):
        super().__init__(tamaño)
        self.colorHojas = colorHojas
    def fotosintesis(self):
        return f"Yo absorbo vitaminas del sol desde mis hojas color {self.colorHojas}"

class Arbol(Planta):
    def  __init__(self, tamaño, colorHojas, Frutos):
        super().__init__(tamaño, colorHojas)
        self.frutos = Frutos

Manzano = Arbol("Grande", "Verde oscuro", True)
print(Manzano.fotosintesis())
print(Manzano.tamaño)
print(Manzano.colorHojas)