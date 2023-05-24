if 2>8:
    print("2 es mayor que 8") #el espacio es para poder realizar identacion
elif 10 > 20:                 #este es para hacer ifs anidados
    print("10 es menor a 20")
elif 100 <= 80:
    print("100 es mayor o igual que 80")
elif 80 >= 100:               #para que lleguen al que queremos el resto deben ser false
    print("80 es menor o igual que 100")
elif 100 != 100:
    print("100 es diferente de 20")
elif 100 != 100:
    print("100 es igual a 100")
else:
    print("no se cumplio niinguna condicion anterior")



#Operadores Terniarios/////////////////////////////////////////////////////////////////////////////////////////////////////

if 2<10: print("2 es menor a 5")

print("si la condicion es verdadera") if 10 < 2 else print("Se imprime si la condicion es falsa")

# And /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

if 2 < 9 and 10 < 20:
    print("2 es menor que 9 y 10 es menor que 20")

if 100 < 1000 or 20 > 900:
    print("100 es menor que 100 o 20 es mayor que 200")

if not 10 < 9:
    print("falso")

"""
Input 
"""

dato = input("Profavor ingrese algo: ")
print(dato)

lista = ["Hola","Mundo"]

if lista.count(dato) > 0:
    print("Esta informacion existe: ", dato)
else:
    print("Esta informacion no existe: ", dato)










