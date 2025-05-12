#Tuplas - Diccionario
#Tuplas  Se define con (), Mayor eficiencia que las listas.
colores =("rojo", "verde", "azul", "amarillo", "naranja", 130) #Definir tupla
print(f"El tipo de dato de colores es: {type(colores)}") #Nos indica el tipo de datos

print(colores) #Nos permite imprimir strings, numeros, etc
print(colores [0:3]) #Imprime los 3 primeros rojo verde y azul

#colores [0] ="verde" #No permite cambiar el valor 0 a verde

#Itenacion
for color in colores:  
    print(color) #Definir los valores

#Condicional para buscar el color si se encuentra en la tupla
if "negro" in colores:
    print("El color esta en la tupla")
else:
    print("El color negro no esta en la tupla")

