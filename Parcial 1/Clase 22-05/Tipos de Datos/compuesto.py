#Las listas en python no son lo mismo que listas en estructura de datos
#LISTAS /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

lista = []

print(type (lista))

lista = ["Ecuador", "Colombia", "Brasil"]
print(lista)

lista = ["juan", 45, 6.5, True, ["Ecuador", "Colombia", "Brasil"] ]
print(lista)

lista = ["Ecuador", "Colombia", "Brasil"]
lista.append("Mexico")          #agrgamos este dato a la lista
print(lista)

lista2 = lista.copy()
print(lista2)

lista2.clear()
print(lista2)

lista2 = lista.copy()
print(lista2.count("Colombia"))
lista2.append("Bolivia")
lista2.append("Colombia")
print(lista2.count("Colombia"))
print(lista2)

print(len(lista2))
"""
append: agrega datos a la lista
clear: elimina todos los elemnetos de una lista "se recomienda usarlo cuando se hace una copia" (nunca hacer un cambio en los datos originales)
copy: permite copiar los datos de una variable
count: permite contar cuantas veces existe un elemento en una lista
len: da la cantidad de valored que hay en una lista
index: da la posicion dentro de la lista de la variable que pongamos
"""

print(lista2[3])
print(lista2[1])
print(lista2[4])

lista2[5] = "Peru"

print(lista2)

#pop es un comando para eliminar el ULTIMO elemento de una lista
lista2.pop()
print(lista2)
#remove elimina especificamente ese dato 
lista2.remove("Brasil")
print(lista2)

#si necesitamos dar la vuelta a una lista podemos usar el metodo reverse
lista2.reverse()
print(lista2)

#otro metodo que organiza los datos es sort
lista2.sort()                               #hace esta organizacion en orden del codigo asqui (orden alfabetico)
print(lista2)

lista3 = ["d","B","b","c"]
lista3.sort()                               #para usar este metodo debemos usar una lista del mismo tipo de dato
print(lista3)


#Tuplas ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

"""
Una dupla se utiliza las () parentesis
las tuplas son tipo de dato compuesto no modificable
"""

tupla = ()
print(type(tupla))

"""
Esto no se puede hacer:
tupla.append("Diego")
print(tupla)
"""

tupla2 = ("Juan", "Pedro", "Maria")
print(tupla2)

print(tupla2.count("Juan"))
print(tupla2.count("Maria"))


print(tupla2.index("Maria"))

# para comentar algo facilmente podemos usar ctrl + k y luego ctrl + c y descomentar es lo mismo pero en vez de c es U

print(tupla2[2])  #usamos corchetes para esto
print(tupla2[1])

lista = list(tupla2)
print(type(lista))

lista.append("Mario")
print(lista)

tupla2 = tuple(lista)
print(tupla2)



#Range ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

rango = range(6)
print(rango)

#Set ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#no puede tener datos duplicados
#set utiliza llaves


set = {2,3,4,5,6,6}
print(set)
print(type(set))


#Diccionarios ///////////////////////////////////////////////////////////////////////////////////////////////////////

cliente001 = {
    "Nombre" : "Miguel",
    "Cedula" : 1722824024,
    "Celular" : "0967355686",
    "Correo" : "macabrera06@gamil.com"
}

print(cliente001)
print(type(cliente001))


print(cliente001["Correo"])

#en lugar de usar un indice utilizamos el nombre 
