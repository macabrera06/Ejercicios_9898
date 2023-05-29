class Monster:

    def __init__(self,nombre,categoria):     #pasamos los parametros basicos necesarios para crear el objeto
        self.nombre = nombre
        self.categoria = categoria
    
    def __str__(self):                       
        return f"Soy {self.nombre} y mi categoria es {self.categoria}"

    def myFunc(self):
        print("Hey, soy un " + self.nombre)

monstruito = Monster("Sulivan", "Asustador")
print(monstruito.nombre)
print(monstruito)
monstruito.myFunc()