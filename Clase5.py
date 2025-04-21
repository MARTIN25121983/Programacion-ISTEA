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

##Listas
##Es una variable que puede almacenar varios valores, se definen con corchetes [] y separados por comas
##Ejemplo de lista