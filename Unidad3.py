##Unidad3 STRINGS | COMPARADORES | CONDICIONALES 

##Concatenacion
variable_uno ="Hola"
variable_dos ="Mundo"
resultado= variable_uno + " " + variable_dos ## " " nos hace un espacio
print(resultado)

##Replicacion ## Funciona con un string y numero
mensaje = "Python"
resultado = mensaje * 3
print(resultado)

##Conversion de datos
##Conversion a entero

numero_como_texto = "10"
print(type(numero_como_texto)) ##Me indica que es un string
numero = int(numero_como_texto) ##Transforma de string a int
print(type(numero)) ## Nos imprime que es un int
print(numero) ##Imprime en pantalla la variable

##Conversion a flotante
numero_pi="3.14"
numero = float(numero_pi)
print(numero)

##Conversion a string
numero = 42
texto = str(numero)
print("El numero es: " + texto)

Hoja 45
