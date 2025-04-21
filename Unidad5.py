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