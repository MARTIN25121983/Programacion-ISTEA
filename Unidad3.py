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

"""Operador igualdad (==)
Ejemplo a==b nos indica que ambas variables tiene el mismo valor

1 == 2    # False, porque 1 y 2 no son iguales. 
2 == 2    # True, porque 2 y 2 son iguales. 
"abc" == "abc"  # True, porque ambas cadenas son idénticas. 
"ABC" == "abc"  # False, porque las letras mayúsculas y minúsculas son diferentes.
"""

"""Operador desigualdad (!=)
Nos indica si dos valores no son iguales
True los valores son diferentes
False los valores son iguales
Ejemplo

1 != 2  # True, porque 1 y 2 son diferentes. 
2 != 2  # False, porque 2 y 2 son iguales. 
"abc" != "abc"  # False, porque las cadenas son iguales. 
"ABC" != "abc"  # True, porque las cadenas son diferentes (por las mayúsculas y minúsculas).>>> 1 != 2  # True, porque 1 y 2 son diferentes. 
2 != 2  # False, porque 2 y 2 son iguales. 
"abc" != "abc"  # False, porque las cadenas son iguales. 
"ABC" != "abc"  # True, porque las cadenas son diferentes (por las mayúsculas y minúsculas).
"""

"""mayor que (>)
5 > 3  # True, porque 5 es mayor que 3. 
2 > 7  # False, porque 2 no es mayor que 7.
"""

"""
Menor que (<)
5 < 3  # False, porque 5 no es menor que 3. 
2 < 7  # True, porque 2 es menor que 7. 
"""

"""
Mayor o igual que (>=)
temperatura >= 0  # True si la temperatura es mayor o igual a 0 grados.
"""

"""
Menor o igual que (<=)
dinero <= 100  # True si el dinero es menor o igual a 100.
"""

"""
Prioridad sobre los operadores
2 + 3 > 4  # True, porque primero se realiza la suma (2 + 3 = 5) y luego la comparación (5 > 4).
"""


## Condicional Sentencia IF
##Ejemplo
alumno_nombre= "Juan" ##Se define variable
alumno_edad= 18 ##Se define variable
if alumno_edad >= 18: ##Se coloca la condicion a comparar y se finaliza con :
    print("El alumno", alumno_nombre, "es mayor de edad", end="!!") ##se imprime la conclusion sobre la condicion planteada
