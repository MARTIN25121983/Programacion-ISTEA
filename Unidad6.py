## Unidad 6 Funciones
#Definicion de funciones es un bloque de codigo para resolver un tema especifico

def mi_primer_funcion(): 
    print("Hola desde mi primer función")  #Definimos la función, el nombre de la función es mi_primer_funcion y no recibe argumentos
    pass #La función no hace nada, solo imprime un mensaje
  
 
# Debemos llamarla para que se ejecute 
mi_primer_funcion() 

##Ejemplo de una función que solicita los datos por pantalla y luego los print indicados
def funcion_prueba():
    nombre = input("Ingrese su nombre ")
    edad = input("Ingrese su edad ")
    ciudad_de_residencia = input("Ingrese su ciudad de residencia ")
    print(type(nombre))
    print("El nombre es: " , nombre)
    print(type(edad))
    print("La edad es: " , edad)
    print(type(ciudad_de_residencia))
    print("La ciudad de residencia es: " , ciudad_de_residencia)

funcion_prueba() #Invocamos la función para que se ejecute

def suma_valor():
    valor_uno = float(input("Ingrese un numero "))
    valor_dos = float(input("Ingrese un numero "))
    valor_tres = float(input("Ingrese un numero "))
    suma = (valor_uno + valor_dos + valor_tres)
    print("La suma es =", suma)

suma_valor() #Invocamos la función para que se ejecute

#funcion y variable no pueden tener el mismo nombre

#Ejemplo de funcion en el cual dentro de la mimsa se define una variable

def imprimir_pantalla( texto_a_imprimir ): ##Defimos la funcion
    print(texto_a_imprimir) #Se imprime el texto
    pass 
    
texto = "Hola Mundo, pasando parametros!" #se define la variable texto

imprimir_pantalla(texto) #Invocamos la funcion y le pasamos el texto como parametro

#return de una funcion # Ejemplo de una funcion que retorna un valor

def suma(a, b):  #Definimos la funcion suma que recibe dos argumentos a y b
    return a + b #Retorna la suma de a y b
numero_uno = input("Ingrese un valor: ")  #Solicitamos al usuario que ingrese un valor
numero_uno = int(numero_uno) #Convertimos el valor ingresado a entero
numero_dos = input("Ingrese otro valor: ") #Solicitamos al usuario que ingrese otro valor
numero_dos = int(numero_dos) #Convertimos el valor ingresado a entero
print("La suma de los valores es: ", suma(numero_uno, numero_dos)) #Imprimimos el resultado de la suma de los dos valores ingresados por el usuario

#Otro ejemplo
def sumar(a, b): 
    return a + b 
 
resultado = sumar(5, 3)  # Pasamos dos valores 
print(resultado)  # Imprimirá 8 

#Ejemplo para sumar mas de dos valores

def sumar_todos(*numeros): # se define la funcion y al agregar * se permite varios valores
    total = sum(numeros)  # sum() suma todos los valores 
    return total 
 
print(sumar_todos(1, 2, 3, 4, 5))  # Imprimirá 15 
print(sumar_todos(10, 20))  # Imprimirá 30 

