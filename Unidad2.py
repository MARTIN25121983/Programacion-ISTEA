##Unidad 2 TIPOS DATOS | OPERADORES | VARIABLES | COMENTARIOS
"""Comentarios -- Son notas, documentacion para darnos una ayuda en un futuro o para que otra persona sepa como esta armado.

un comentario es un texto que comienza con el símbolo # (numeral o almohadilla) y se extiende hasta el final de la línea.
En cambio si queremos agregar un comentario de varias líneas debemos comenzar con comillas, y luego terminar con comillas
"""

##Carácter especial: \n
##La barra invertida (\) se usa para incluir caracteres especiales. Por ejemplo, \n indica un salto de línea:


##Ejemplo
print("Hola Mundo\nHola Python") 

print("Hola Mundo\”Hola Python") ##Inserta comillas dobles 
print("Hola Mundo\tHola Python") ## Tabulacion
print("Hola Mundo\\Hola Python") ## Inserta barra invertida
print("Hola Mundo\’Hola Python") ## Inserta comilla simple

print("Hola", "Python", "Martin") ## Se puede pasar varios argumentos dentro de la funcion print

##Argumento end
print("Hola", end="-") #En este caso end="-" por ende el resultado es Hola-Python
print("Python")

##Argumento sep (Este argumento especifica qué carácter (o cadena de caracteres) se debe utilizar para separar múltiples argumentos posicionales en la salida.)
print("Python", "es", "Genial", sep="-")

##Combinando sep y end  
print("Aprender", "Python","es", "genial", sep="->", end="!!!\n")

##Funcion Type 
print(type("Hola Mundo")) ##Nos indica el tipo de dato.

##Tipos de datos
edad = 25 # El número 25 es del tipo entero (int)
precio = 19.99 # El número 19.99 es del tipo punto flotante (float)
nombre = "Ana" # El texto "Ana" es del tipo cadena de caracteres  (str)
es_estudiante = True, False # El valor True es del tipo booleano (bool)

##Operdores Aritmeticos
##Suma
suma=(8+5)
print(suma) ## Realiza la suma entre los argumentos.

#Resta
resta=8-5
print(resta)

##Multiplicacion(*)
multiplicacion=8*5
print(multiplicacion)

##Division Siempre devuelve un valor flotante.
division=10/2
print(division)

##Division entera // El resultado es entero
division_entera=10//3
print(division_entera)

##Resto o modulo %
resto=10%3
print(resto)

##Exponencial ** 
exponencial= 2**3
print(exponencial)

##Prioridades de operaciones
resultado = 2 + 3 * 4 ## realiza la multiplicacion y luego la suma
print(resultado)

##Variables Las variables son como contenedores que permiten guardar datos y recuperarlos cuando los necesitemos. 
## El nombre "variable" se debe a que su contenido puede cambiar o "variar" a lo largo de la ejecución del programa.

"""Lista de palabras reservadas en Python 
Python tiene un conjunto de palabras reservadas que no puedes usar como nombres de variables. 
En la mayoria de las versiones son las siguientes:   
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']"""

x=10 ##Variable x que tiene en valor de 10
print(x)

x=5
x=x+2
print(x)

x=10
x+=2
print(x)

"""
Operadores Abreviados

+=  x+=3 x=x+3
-=  x-=2 x=x-2
+*  x*=4 x=x*4
/=  x/=2 x=x/2
//= x//=3 x=x//3
%=  x%=5 x=x%5
**= x**=2 x=x**2
"""

##Input Siempre lo toma como string
nombre = input() ## En este caso el input esta vacio
print("Hola, " + nombre) ##Luego de ejecutarlo debemos escribir y luego nos imprime en pantalla

nombre = input("Ingrese su nombre ") # Se solicita el input al usuario
print("Hola, " + nombre, end="!!") #Combinacion de variable ya definida, ingresar una variable y luego usar el end

edad=input("Ingrese su edad ") ##Solicita informacion al usuario
print("Su edad es de "+ edad + " años") ##Imprime en pantalla las variables mas el dato del usuario
print(type(edad)) ##Nos indica la clase de variable

