##Unidad 7 Listas 

##Una lista es un tipo de dato en Python que nos permite almacenar una colección de elementos en un orden específico
#Ejemplo de lista 
#puden tener diferentes tipos de datos int, float, string, boal, etc

colores = ["rojo", "verde", "azul", "amarillo"] 
print(colores) 

#Funcion len contar la cantidad de elementos de una lista

print("La cantidad de colores son:", len(colores))
#Acceder a un elemento de la lista. Si queres acceder al primero debemos:
print(colores[0]) #primer elemento

#Para acceder al ultimo elemento de la lista o empezar del ultimo hacia el primero se usa el numero negativo

numeros= [1,2,3,4,5,6,7,8,9]
#para acceder al utlimos debemos elegir de la siguiente manera
print(numeros[-1]) # se accedea al 9
print(numeros[-2]) # se accedea al 8

#Agregar un elemento en la lista numeros
numeros.append(10) #Se va agregar el 10 como ultimo elemento
print(numeros)

#funcion insert
numeros.insert(11,2) #El primer valor es la posicion y luego el elemento agregar. En este caso en el lugar 11 se coloca el 2
print(numeros)

#funcion remove
numeros.remove(9) #Se elimina el numero 9 de la lista
print(numeros)

#Funcion pop
numero = [1,2,3,4]
numero.pop() #Elimina el ultimo elemento por defecto
numero.pop(2) #Elimina el elemento que se encuentra en la posicion 2
print(numero)

#Funcion index
