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

print("vamos a imprimir numero aleatorios entre 0 y 1 ")
print(random.random()) #Muestra un numero aleatorio entre 0 y 1

#Imprimir un numero aleatorio entre 0 y 10
for i in range(10):
    print(random.random()*100) #Muestra un numero aleatorio entre 0 y 10

random.seed(3) #Fija la semilla para que los numeros aleatorios sean siempre los mismos
print("un numero aleatorio con semilla 3" , random.random()) #Muestra un numero aleatorio entre 0 y 1. Siempre sera el mismo numero aleatorio

#randrange() #Genera un numero aleatorio entre dos numeros

print(random.randrange(20, 30, 2)) #Muestra un numero aleatorio entre 20 y 30 y el paso es de 2 en 2
print(random.randrange(20, 30)) #Muestra un numero aleatorio entre 20 y 30
print(random.randrange(20, 30)) #Muestra un numero aleatorio entre 20 y 30
print(random.randrange(20, 30)) #Muestra un numero aleatorio entre 20 y 30
print(random.randrange(20, 30)) #Muestra un numero aleatorio entre 20 y 30

for i in range(10):
    print(random.randrange(20, 30, 2)) #Muestra un numero aleatorio entre 20 y 30


for i in range(10): ##Ejecuta 10 veces
    print(random.randrange(20) ) #Muestra un numero aleatorio entre 0 y 20

#choice() #Elige un elemento aleatorio de una lista

dado =[1, 2, 3, 4, 5, 6] #Lista de numeros del dado
print("tiro el dado y sale: " , random.choice(dado)) #Muestra un numero aleatorio de la lista dado

print("Tiro el dado 3 veces: " , random.sample(dado, 3)) #Muestra 3 numeros aleatorios de la lista dado


