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

#Funcion index Devuelve la posicion de la primera aparicion de un elemento

colores = ["azul", "blanco", "rojo", "negro", "azul"]
print(colores.index("azul")) # Nos indica que la posicion de aparicion es 0

#Funcion count Cuenta la cantidad de veces que aparece un objeto
print(colores.count("azul")) # Indica que aparece dos veces

#Funcion sort  ordena la lista en orden ascendente

numbers=[4,8,6,4,5]
numbers.sort() # ordena en orden ascendente
print(numbers)

numbers.sort(reverse=True) #se indica que ordene en orden descendente
print(numbers)

#Funcion reverse Invierte el orden de la lista
numbers= [1,2,3,4,5]
numbers.reverse() #Invierte el orden la lista
print(numbers)

#Funcion sorted  ordenar una lista sin modificar el orden original de sus elementos,
# Ordenamiento básico de una lista 
numeros = [5, 2, 8, 1, 9] 
ordenados = sorted(numeros)
print(ordenados)  # [1, 2, 5, 8, 9] 
  
# Ordenamiento inverso 
ordenados_inverso = sorted(numeros, reverse=True) 
print(ordenados_inverso)  # [9, 8, 5, 2, 1] 
  
# Ordenamiento de strings 
palabras = ["python", "javascript", "ruby", "java"] 
ordenadas = sorted(palabras) 
print(ordenadas)  # ['java', 'javascript', 'python', 'ruby']

#En listas se puede utilizar bucle for

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
for numero in numeros: 
    print(numero) 

multiplos = [7, 14, 21, 28, 35] 
total = 0 
for numero in multiplos: #Recorre la lista
    total += numero  #Realiza la suma de los elementos de la lista
  
print(total)

#intercambiar valores
a=1
b=2
a,b=b,a #Se intercambia los valores
print(a,b) #Imprime los valores intercambiados en pantalla

lista = [1, 2, 3, 4, 5] 
lista[0], lista[4] = lista[4], lista[0] 
  
# Intercambiamos el segundo y penúltimo 
 
lista[1], lista[3] = lista[3], lista[1] 
print(lista)  # Salida: [5, 4, 3, 2, 1] 

#Encontrando extremos: `min()` y `max()` 
#Son como el termómetro de tus números. Miden quién es el más pequeño y el más grande en la lista. 
temperaturas = [23, 17, 25, 19, 20] 
  
print(min(temperaturas))  # 17 → El día más frío 
print(max(temperaturas))  # 25 → El día más caluroso 
#Funciona con: - Números enteros y decimales - Listas de letras (comparando orden alfabético) 
letras = ['z', 'a', 'm'] 
print(min(letras)) 

#Creando listas numéricas: `range()` + `list()` 
# Del 0 al 4 (5 no se incluye) 
print(list(range(5))) 
# [0, 1, 2, 3, 4] 
  
# Del 2 al 6 (7 no se incluye) 
print(list(range(2, 7))) 
# [2, 3, 4, 5, 6] 
  
# De 10 a 50, de 5 en 5 
print(list(range(10, 51, 5))) 
# [10, 15, 20, 25, 30, 35, 40, 45, 50]
