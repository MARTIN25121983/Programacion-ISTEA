##Funciones (Unidad 6) y listas (Unidad 7)
##Funciones Bloque codigo para resolver algo especifico
#Ejemplos

def mi_primer_funcion(): ##Definicion de la funcion
    print("Hola, soy una funcion") ##imprime el mensaje
mi_primer_funcion() ##llama a la funcion para que se ejecute

##Se puede armar una funcion sin definir lo que realiza, pero se debe poner un pass para que no de error
def mi_segunda_funcion(): ##Definicion de la funcion
    pass ##no hace nada, pero no da error
mi_segunda_funcion() ##llama a la funcion para que se ejecute

def texto_ingrese_valor():
    print("Ingrese un valor") ##imprime el mensaje


texto_ingrese_valor() ##llama a la funcion para que se ejecute
valor_uno = input() ##pide al usuario que ingrese un valor
texto_ingrese_valor() ##llama a la funcion para que se ejecute
valor_dos = input() ##pide al usuario que ingrese un valor
print("El valor uno es:", valor_uno, "El valor dos es: ", valor_dos) ##imprime el valor uno y valor dos

#Otro ejemplo de funcion
def texto_imprimir(texto, caracter_cuadro ):
    print(caracter_cuadro * 20) ##imprime el caracter 20 veces
    print(caracter_cuadro * 20) ##imprime el caracter 20 veces
    print(caracter_cuadro * 20) ##imprime el caracter 20 veces
    print(texto) ##imprime el texto
    print(caracter_cuadro * 20) ##imprime el caracter 20 veces
    print(caracter_cuadro * 20) ##imprime el caracter 20 veces
    print(caracter_cuadro * 20) ##imprime el caracter 20 veces

texto_imprimir("Ingrese un valor numerico: ", "-*") #Invocar la funcion para que se ejecute


def sumar(numero_uno, numero_dos): ##definicion de la funcion sumar y los parametros que recibe
    total = numero_uno + numero_dos ##suma los dos numeros
    return total ##devuelve el resultado de la suma

texto_imprimir("Ingrese el primer numero: ", "-") ##llama a la funcion texto_imprimir para que se ejecute
numero_uno = int(input())  ##pide al usuario que ingrese un valor y lo convierte a entero
texto_imprimir=("Ingrese el segundo numero: ", "-") ##llama a la funcion texto_imprimir para que se ejecute
numero_dos = int(input()) ##pide al usuario que ingrese un valor y lo convierte a entero

total = sumar(numero_uno, numero_dos) ##llama a la funcion sumar para que se ejecute
print("El resultado de la suma es: ", total)##imprime el resultado de la suma 

##Scope de las funciones # Alcance de las funciones 
##Las variables definidas dentro de una funcion no pueden ser utilizadas fuera de la funcion

##Listas
##Es una variable que puede almacenar varios valores, se definen con corchetes [] y separados por comas
##Ejemplo de lista. La lista puede almacenar diferentes tipos de datos, como enteros, cadenas, booleanos, etc.

nombres = ["Juan", "Pedro", "Maria", "Ana", "Luis"] ##definicion de la lista nombres
libreria=["boligrafo", "goma", "lapiz", "marcador"] ##definicion de la lista libreria
print(type(nombres)) ##imprime el tipo de la variable nombres
print(type(libreria)) ##imprime el tipo de la variable libreria
print("tipo de dato :", type(nombres)) ##imprime el tipo de dato de la variable nombres

print(len(nombres)) ##imprime la cantidad de elementos de la lista nombres
print(len(libreria)) ##imprime la cantidad de elementos de la lista libreria
print(nombres[0]) ##imprime el primer elemento de la lista nombres
print(nombres[-1]) ##imprime el ultimo elemento de la lista nombres
print(nombres[1:3]) ##imprime los elementos de la lista nombres desde la posicion 1 a la 3 (sin incluir la 3)   
nombres.append("Jose") ##agrega el elemento Jose al final de la lista nombres
print(nombres) ##imprime la lista nombres con el nuevo elemento agregado
nombres.insert(2, "Carlos") ##agrega el elemento Carlos en la posicion 2 de la lista nombres
print(nombres) ##imprime la lista nombres con el nuevo elemento agregado    
nombres.remove("Carlos") ##elimina el elemento Carlos el primero que figura de la lista nombres
print(nombres) ##imprime la lista nombres sin el elemento Carlos
nombres.pop(2) ##elimina el elemento de la posicion 2 de la lista nombres
print(nombres) ##imprime la lista nombres sin el elemento de la posicion 2
nombres.count("Juan") ##cuenta la cantidad de veces que aparece el elemento Juan en la lista nombres


