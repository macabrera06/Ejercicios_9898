class Persona:
    def __init__(self,nombre,edad,cedula):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
    
    def __str__(self) -> str:
        return f"Yo soy {self.nombre}, tengo {self.edad} años y mi cedula es {self.cedula}"
    
    def programar(self):
        return f"Yo {self.nombre} puedo programar"
    
    def trotrar(self):
        return f"Yo {self.nombre} troto todas las mañanas"
    

Miguel = Persona("Miguel", 21, "1722824024")
print(Miguel)
print(Miguel.programar())
print(Miguel.trotrar())