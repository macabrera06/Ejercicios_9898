#Creacion de diccionarios anidados
perros = {
    "Tobby":{
        "name" : "Tobby",
        "age" : 6
    },
    "Leo":{
        "name" : "Leo",
        "age" : 4
    }
}


#Podemos crear diccionario con diccionarios mas pequeños y unirlos a otro diccionario al poner el nombre : el diccionario que vamos a agregar
rocky = {
    "name" : "Rocky",
    "age" : 1
}

perros["Rocky"] = rocky
print(perros)



