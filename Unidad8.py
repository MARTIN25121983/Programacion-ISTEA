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

#Diccionarios es una coleccion de pares clave-valor. Cada clave es unica. Puede ser int, float o string 

dict_1 = {"nombre": "sara",
          "apellido": "perez",
          "edad": 27,          
          "documento": "27654343",
          "direccion": "Bulnes 777",
          "CP": "1212"
} #Se crea un diccionario

print(dict_1)
##Hay 4 claves que tiene 4 valores, 1 para cada clave

print(f"EL tipo de objeto de dict_1 es {type(dict_1)}")


