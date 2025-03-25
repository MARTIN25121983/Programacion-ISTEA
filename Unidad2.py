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



