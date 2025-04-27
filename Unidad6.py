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

imprimir_pantalla(suma_valor) #Invocamos la funcion y le pasamos el texto como parametro
