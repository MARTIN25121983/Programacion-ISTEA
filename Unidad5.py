#Unidad 5 FOR | STRINGS | MODULOS 

##Bucle for
## Ejemplo imprimir del 0 al 99
for i in range(100):
    print(i)

for i in range(5): ## se coloca el filtro del 0 al 5
    print("Hola, alumnos!, linea", i) ##se imprime buscando la condicion del 0 al 4 inclusive
## Otros ejemplos
for i in range (5): ##En este caso el rango es del 0 al 5
    print(i) ## Imprime en pantalla los valores del 0 al 4

for i in range(3, 8): #En este caso el rango seria del 3 al 8
    print(i) #Imprime en pantalla los valores del 3 al 7

for i in range(3, 8, 2): #En este caso el rango seria del 3 al 8 de 2 en 2
    print(i) #Imprime en pantalla los valores del 3 al 7 de 2 en 2  

#Utilizar break para finalizar el bucle

for i in range(10):
    if i == 5: #Condicion para que cuando i sea igual a 5
        break #El break corta el bucle y no imprime el 5
    print(i)
#Utilizar continue para coninuar el bucle
for i in range(10): #En este caso el rango es del 0 al 10
    if i % 2 == 0: 
        continue
    print(i) #Imprime los numeros impares del 0 al 9

#Else en bucles for
numeros = [1,2,3,4,5,6,7,8,9,10]
objetivo = 20
for num in numeros: #Recorre la lista de numeros
    if num == objetivo: #Condicion para que cuando el numero sea igual al objetivo
        print("El numero es igual al objetivo") ##Imprime el mensaje si el numero es igual al objetivo
        break #El break corta el bucle.
    else:
        print("no encontre el numero", objetivo) ##Imprime el mensaje si el numero no es igual al objetivo

for i in range(5):
    print(i) ##Imprime los numeros del 0 al 4
else:
    print("El bucle termino") ##Imprime el mensaje cuando el bucle termina

#Manipulacion de strings
##Concatenadas con el signo +
subcadena_uno = "mi" 
subcadena_dos = "la" 
subcadena_tres = "ne" 
subcadena_cuatro = "sas" 
# Sumo las subcadenas 
cadena = subcadena_uno + subcadena_dos + subcadena_tres + subcadena_cuatro  #Concateno las subcadenas
print(cadena) ##Imprime la cadena completa

##Replicadas con el signo *
# Multiplico la subcadena_uno por 4 
print(subcadena_uno * 4)  ##Imprime la subcadena 4 veces

#len (cadena) #Longitud de la cadena
comidas= "milanesas"
print("la longitud de " + comidas + "es: "  + str(len(comidas))) ##Imprime la longitud de la cadena y la convierte a string

#Index
provincia = "Mendoza" 
print(provincia[2]) ##Imprime la letra que se encuentra en la posicion 2 de la cadena Mendoza 

ciudad = "Mar del Plata" 
len_total = len(ciudad)  ##Longitud de la cadena ciudad
for indice in range(len_total): ##Recorre la cadena ciudad
    print(ciudad[indice]) ##Imprime cada letra de la cadena ciudad

cadena = "Python es un lenguaje multiproposito" 
# mostrar los primeros 6 caracteres 
print(cadena[0:6]) # Imprime la cadena desde la posicion 0 hasta la 6 
# mostrar la primer posicion 
print(cadena[0]) # Imprime la cadena desde la posicion 0 
# mostrar la palabra "es un" 
print(cadena[7:12]) # Imprime la cadena desde la posicion 7 hasta la 12 
# mostrar el último carácter 
print(cadena[-1]) # Imprime la cadena desde la posicion -1 (último carácter) 
#mostrar la palabra multipropósito 
print(cadena[-14:]) # Imprime la cadena desde la posicion -14 (palabra multipropósito) 
# mostrar la cadena sin los 2 primeros y 2 últimos caracteres 
print(cadena[2:-2]) # Imprime la cadena desde la posicion 2 hasta la -2 (sin los 2 primeros y 2 últimos caracteres) 
# Mostrar los caracteres en posición impar 
print(cadena[::2]) # Imprime la cadena desde la posicion 0 hasta la -1 (sin los caracteres en posición par)


abecedario = "abcdefghijklmnñopqrstuvwxyz"   
if "a" in abecedario: ## Verifica si la letra a está en el abecedario
    print("La letra a está en el abecedario")   ## Imprime el mensaje si la letra a está en el abecedario
if "33" not in abecedario: # Verifica si el número 33 no está en el abecedario
    print("El numero 33 no está en el abecedario")  ## Imprime el mensaje si el número 33 no está en el abecedario
if "z" in abecedario: ## Verifica si la letra z está en el abecedario
    print("La letra z está en el abecedario") ## Imprime el mensaje si la letra z está en el abecedario

#Index() 
"""
El método index() (es un método, no una función) busca la secuencia desde el principio, para 
encontrar el primer elemento del valor especificado en su argumento. 
Nota: el elemento buscado debe aparecer en la secuencia, su ausencia causará una excepción 
ValueError. 
El método devuelve el índice de la primera aparición del argumento (lo que significa que el 
resultado más bajo posible es 0).
"""

cadena = "Python es un lenguaje multiproposito"   
indice = cadena.index("l")   ## Busca la posición de la letra "l" en la cadena
print(indice)   ## Imprime la posición de la letra "l" en la cadena

#find()
"""
El método find() funciona de la misma manera que el método index(), con unas diferencias: 
Es más seguro, no genera un error para un argumento que contiene una subcadena 
inexistente (devuelve -1 en dicho caso). 
Funciona solo con strings.
"""

#count()
cadena = "Python es un lenguaje de código abierto"  
letra_e_cantidad = cadena.count("e") ## Cuenta la cantidad de veces que aparece la letra "e" en la cadena
print("Cantidad de veces que aparece la letra e es: " + str(letra_e_cantidad)) ## Imprime la cantidad de veces que aparece la letra "e" en la cadena

#isdigit() ## Verifica si la cadena es un número
#upper() / lower() ## Convierte la cadena a mayúsculas o minúsculas

cadena = "Python es un lenguaje de código abierto"   
cadena_mayuscula = cadena.upper() ## Convierte la cadena a mayúsculas
print(cadena_mayuscula)  ## Imprime la cadena en mayúsculas
cadena_minuscula = cadena.lower() ## Convierte la cadena a minúsculas
print(cadena_minuscula) ## Imprime la cadena en minúsculas

#lstrip() ## Elimina los espacios en blanco a la izquierda de la cadena 
#rstrip() ## Elimina los espacios en blanco a la derecha de la cadena

cadena = "Python es un lenguaje de alto nivel" 
cadena_centrado_izquierda = cadena.ljust(50, '-') #Esta función alinea la cadena a la izquierda y completa con '-' hasta 50 caracteres
print(cadena_centrado_izquierda) 
cadena_centrado_derecha = cadena.rjust(50, '-')  #Esta función alinea la cadena a la derecha y completa con '-' hasta 50 caracteres
print(cadena_centrado_derecha)

#replace() ## Reemplaza una subcadena por otra en la cadena
cadena = "Python es un lenguaje orientado a objetos" 
print(cadena) 
cadena_reemplazada_php = cadena.replace("Python", "PHP") ## Reemplaza "Python" por "PHP" en la cadena
print(cadena_reemplazada_php) 
cadena_reemplazada_javascript = cadena.replace("Python", "Javascript") ## Reemplaza "Python" por "Javascript" en la cadena
print(cadena_reemplazada_javascript) 

#Modulos ## Modulo es un archivo que contiene definiciones y declaraciones de Python.
# Un módulo puede definir funciones, clases y variables. Un módulo puede incluir código ejecutable.
# Un módulo se puede importar en otro módulo o en un script de Python.

#import Importa el módulo
#Importar modulo math y sys

import math # Importa el módulo math 
import sys # Importa el módulo sys
# o de la siguiente forma  
import math, sys # Importa los módulos math y sys

#from Importa funciones específicas de un módulo
#Ejemplo: 
from math import cos, radians, pi # Importa las funciones cos, radians y pi del módulo math
print(math.pi) # Imprime el valor de pi

#dir() ## Devuelve una lista de los nombres de los atributos y métodos de un objeto.

import math # Importa el módulo math
print(dir(math)) # Imprime la lista de los nombres de los atributos y métodos del módulo math

#Funciones modulo math 
"""
ceil(x) → Redondea el valor ingresado como argumento a su valor entero mayor más cercano. 
floor(x) → Redondea el valor ingresado como argumento a su valor entero menor más cercano. 
pow(x) → Hace el exponente. 
sqrt(x) → Resuelve la raíz cuadrada.
"""
#Ejemplos
import math   
numero = 4.6 
print("Numero original: ", numero) ## Imprime el número original
print("Aplicamos ceil() -> ", math.ceil(numero)) ## Redondea el número al entero mayor más cercano
print("Aplicamos floor() -> ", math.floor(numero)) ## Redondea el número al entero menor más cercano
print("Aplicamos pow() -> ", math.pow(numero, 2)) ## Eleva el número al cuadrado
print("Aplicamos sqrt() -> ", math.sqrt( math.floor(numero) )) ## Resuelve la raíz cuadrada del número redondeado al entero menor más cercano

"""
Otras funciones
abs(x) →  Devuelve el valor absoluto del valor ingresado como argumento 
(convierte los valores negativos en positivos, los que ya son positivos 
no se ven afectados). 

round(x,y) → Devuelve un número flotante obtenido luego de redondear el 
primer valor ingresado como argumento. El segundo argumento le 
especifica a la función la cantidad de decimales que se desea conservar, 
este valor es opcional, y en caso de no ser especificado, su valor por 
defecto es 0. 
"""

#Modulo random ## Genera números aleatorios
## La función general llamada random() (no debe confundirse con el nombre del módulo) produce un 
## número flotante x entre el rango (0.0, 1.0) - en otras palabras: (0.0 <= x < 1.0).
##Ejemplo random()

import random # Importa el módulo random  
print(" Vamos a imprimir diez números random entre 0 y 1") ## Imprime el mensaje  
for i in range(10):     ## Recorre el rango del 0 al 10
    print(random.random() * 100) ## Imprime un número aleatorio entre 0 y 100

random.seed(3) ## Establece la semilla para el generador de números aleatorios
print("Serie #1:", random.random(), random.random(), random.random()) #
random.seed(3) ## Establece la semilla para el generador de números aleatorios
print("Serie #2:", random.random(), random.random(), random.random()) # Imprime la segunda serie de números aleatorios

#Valores enteros aleatorios
"""
randrange(fin) 
randrange(inicio, fin) 
randrange(inicio, fin, secuencia) 
randint(izquierda, derecha)
"""

for i in range(10): ## Recorre el rango del 0 al 10
    print("Aleatorio del 1 al 10 -> ", random.randint(1, 10)) ## Imprime un número aleatorio entre 1 y 10
    print("Aleatorio del 20 al 30 -> ", random.randrange(20, 30)) ## Imprime un número aleatorio entre 20 y 30
    print('---------------------------') ## Imprime una línea de separación

#choice()  ## Devuelve un elemento aleatorio de una secuencia no vacía.
#sample()  ## Devuelve una lista de elementos aleatorios de una secuencia no vacía.

dado = [1, 2, 3, 4, 5, 6]  ## Crea una lista con los números del dado
  
print("Dado: ", random.choice(dado)) ## Imprime un número aleatorio del dado
print(random.sample(dado, 3)) ## Imprime una lista de 3 números aleatorios del dado
