#Modulo video de youtube Juan Pablo

# al ser un codigo muy largo se divide por partes (en modulos) para que sea mas facil de entender

#Ejemplo de modulo Se va a trabajar sobre el archivo modulo.prueba.py
#Importar un modulo nuestro personzalizado

import modulo_prueba #Trae el archivo en memoria

modulo_prueba.saludar()  #Llama a la funcion saludar del modulo modulo_prueba

print("Mi nombre es: ", modulo_prueba.nombre) ##Llama al modulo_prueba pero al nombre solamente 
print("Mi apellido es: ", modulo_prueba.apellido) ##Llama al modulo_prueba pero al apellido solamente

#Importar un modulo de python

import math #Modulo de python nativo de natematica
#ceil() #Redondea hacia arriba
print (math.ceil(3.2)) #Redondea hacia arriba el 3.2 y lo convierte en 4

import math
numero_original = 3.4
print(type(numero_original))
numero= math.ceil(numero_original) #Redondea hacia arriba el 3.4 y lo convierte en 4
print("numero" , numero) #Muestra el resultado de la variable numero
print(type(numero)) #Muestra el tipo de dato de la variable numero

#Otra manera de importar un modulo
from math import ceil, pow #Importa las funciones ceil y pow del modulo math #ceil() #Redondea hacia arriba. #pow() #Eleva un numero a otro numero
numero_original = 3.4 #Variable de tipo float
print(type(numero_original)) #Muestra el tipo de dato de la variable numero_original
numero= ceil(numero_original) #Redondea hacia arriba el 3.4 y lo convierte en 4
print("numero" , numero) #Muestra el resultado de la variable numero
print(type(numero)) #Muestra el tipo de dato de la variable numero

# ver todo el contenido de un modulo
print(dir(math)) #Muestra todo el contenido del modulo math

numero_elevado = pow(numero_original, 2) #Eleva el numero_original a la potencia 
print (numero_elevado) #Muestra el resultado de la variable numero_elevado
print(type(numero_elevado)) #Muestra el tipo de dato de la variable numero_elevado

#Importar modulo random
import random #Modulo de python nativo de numeros aleatorios
print(dir(random)) #Muestra todo el contenido del modulo random


