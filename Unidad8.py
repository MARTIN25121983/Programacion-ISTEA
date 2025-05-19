#Tuplas - Diccionario Clase
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
print(dict_1["direccion"]) #Imprime una de las claves del diccionario

print(f"EL tipo de objeto de dict_1 es {type(dict_1)}")

for i in dict_1:
    print(i)
#Del elimina algun valor del diccionario

#Tuplas - Diccionario -Libro
#Tuplas una vez creadas no permite modificaciones.

#Ejemplo tuplas

colores= ("rojo", "verde", "azul") #Definir la tupla

for color in colores: #Recorre la tupla
    print(color.upper()) #Imprime los valores de la tupla pero en mayuscula

#Diccionario Posee clave - valor. Las claves son unicas. se utiliza para aceder al valor asociado.
#Ejemplos
diccionario_1 = {    
"Nombre": "Sara", 
"Edad": 27, 
"Documento": 1003882    
} 
print(diccionario_1) 

diccionario_2= dict(Nombre="Sara", Edad=27, Documento=1003882) 
print(diccionario_2) 

nro_telefono = { 
'juan': 123456, 
'pedro': 987654, 
'maria': 456789           
} 
print("El numero de telefono de Juan es: ", nro_telefono['juan']) 
print("El numero de telefono de Pedro es: ", nro_telefono['pedro'])  
# Para asegurarnos que la clave existe en el diccionario 
if 'maria' in nro_telefono: 
    print("El numero de telefono de Maria es: ", nro_telefono['maria']) 
else: 
    print("Maria no tiene numero de telefono") 
 
# Si intentamos llamar a un diccionario por una clave que no existe, nos va a dar un error 
#print("El numero de telefono de Ana es: ", nro_telefono['ana']) 

#Metodo Keys
persona = {     
"nombre": "Ana", 
"edad": 25,    
"ciudad": "Buenos Aires" 
}   
# Usamos el método .keys() para obtener las claves del diccionario 

claves = persona.keys()
print(claves) #Imprime las claves

#Recorre el bucle recorriendo las claves
for clave in persona.keys():
    print(clave)

#Recorre el bucle recorriendo los valores
for valores in persona.values():
    print(valores)

#Metodo items Nos devuelve la clave y valores
# Crear un diccionario de frutas y sus precios 
frutas = {  
"manzana": 2.5, 
"banana": 1.8, 
"naranja": 3.0, 
"uva": 4.5}

# Iterar sobre cada par clave-valor usando items() 
for fruta, precio in frutas.items():  #Colocamos la clave y valor para que recorra
    print(f"La {fruta} cuesta ${precio} por kilo.")

#del elimina una key del diccionario
del frutas["manzana"]
for fruta, precio in frutas.items():
    print(f"La fruta {fruta} cueta ${precio} por kilo")