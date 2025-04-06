
##1. Solicita al usuario que ingrese su nombre y su edad. Luego, imprime un mensaje que diga "¡Hola, [nombre]! Tienes [edad] años".
nombre = (input("Ingrese su nombre "))
edad = (input("Ingrese su edad "))

print("¡Hola," , nombre,"!", "Tienes", edad , "años")

##2. Imprima en pantalla las siguientes figuras geometricas (utilizar concatenación y replicación de strings)

"""

+***************+
*               *
*               *
*               *
+***************+

"""
print("+" + "*" *16 + "+")
print("*" + " " *16 + "*")
print("*" + " " *16 + "*")
print("*" + " " *16 + "*")
print("+" + "*" *16 + "+")
"""
+---+
|   |
|   |
|   |
+---+

"""
print("+" + "-" * 3 + "+")
print("|" + " " *3 + "|")
print("|" + " " *3 + "|")
print("|" + " " *3 + "|")
print("+" + "-" * 3 + "+")

"""
###################################
###################################
##                               ##
##                               ##
##                               ##
###################################
###################################
"""
print("#" * 35)
print("#" * 35)
print("#" * 2 + " " * 31 + "#" *2)
print("#" * 2 + " " * 31 + "#" *2)
print("#" * 2 + " " * 31 + "#" *2)
print("#" * 35)
print("#" * 35)


#3. Solicita al usuario que ingrese dos números enteros. Luego, convierte estos números a float, realiza la división de ambos y muestra el resultado.
numero_uno = int(input("Ingrese un numero entero "))
numero_dos = int(input("Ingrese un numero entero "))

numero_uno_float = float(numero_uno)
numero_dos_float = float(numero_dos)

division = (numero_uno_float / numero_dos_float)
print("El resultado es:" , division)
#4. Pide al usuario que ingrese una cadena que represente un número entero. Convierte esta cadena a un entero usando la función int() y luego suma 10. Imprime el resultado.
cadena = input("Ingrese un numero entero ")
numero_entero = int(cadena)
resultado = numero_entero + int(10)
print("El resultaod es:" , resultado)

#5. Pregunta al usuario que ingrese un número. Si el número es mayor que 10, imprime "El número es mayor que 10". Si es igual a 10, imprime "El número es igual a 10". De lo contrario, imprime "El número es menor que 10".
numero = float(input("Ingrese un numero "))
if numero >10:
    print("El numero es mayor a 10")
elif numero == 10:
    print("El numero es igual a 10")
else:
    print("El numero es menor a 10")

#6. Solicita al usuario que ingrese dos números y compara si son iguales. Si lo son, imprime "Los números son iguales". De lo contrario, imprime "Los números son diferentes".
numero_uno = float(input("Ingrese un numero "))
numero_dos = float(input("Ingrese un numero "))
if numero_uno == numero_dos:
    print("Los numero son iguales")
else:
    print("Los numero son diferentes")

#7. Pregunta al usuario que ingrese su edad. Si la edad es mayor o igual a 18, imprime "Eres mayor de edad". De lo contrario, imprime "Eres menor de edad".
edad = int(input("Ingrese su edad "))
if edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#8. Pide al usuario que ingrese una temperatura en Celsius. Si la temperatura es mayor o igual a 100, imprime "El agua está hirviendo". Si es menor o igual a 0, imprime "El agua está congelada". De lo contrario, imprime "El agua está en estado líquido".
temperatura_celsius = float(input("Ingrese la temperatura en celsius "))
if temperatura_celsius >=100:
    print("El agua esta hirviendo")
elif temperatura_celsius <=0:
    print("El agua esta congelada")
else:
    print("El agua esta en estado liquido")

#9. Pregunta al usuario que ingrese un número. Si es positivo, imprime "El número es positivo". Si es negativo, imprime "El número es negativo". Si es cero, imprime "El número es cero".
numero= float(input("Ingrese un numero"))
if numero >0:
    print("El numero es positivo")
elif numero <0:
    print("El numero es negativo")
else:
    print("El numero es cero")

##10. Solicita al usuario que ingrese un número del 1 al 7. Luego, imprime el día de la semana correspondiente (1 para Lunes, 2 para Martes, etc.). Si ingresa un número fuera de ese rango, imprime "Número de día no válido".


#11.Calculadora básica
#Crea un programa que tome dos números como entrada y luego imprima la suma, resta, multiplicación y división de esos dos números. Usa operadores aritméticos y asegúrate de manejar casos donde el divisor sea cero.


#12.Calculador de IMC
#Crea un programa que calcule el Índice de Masa Corporal (IMC) de una persona. Pide al usuario su peso en kilogramos y su altura en metros. Luego, calcula el IMC usando la fórmula `IMC = peso / altura**2` y muestra el resultado con un mensaje que indique si el IMC está en el rango normal, bajo peso, sobrepeso, etc.


#13.Conversión de unidades
#Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit. La fórmula de conversión es `F = C * 9/5 + 32`. Pide al usuario que ingrese una temperatura en Celsius y muestra el resultado en Fahrenheit.


#14.Juego de adivinanza
#Crea un programa que pida al usuario que adivine un número entre 1 y 10. El programa debe comparar el número ingresado con uno predefinido (por ejemplo, 7) y decir si es correcto o no. Si es incorrecto, debe dar una pista si el número es mayor o menor.


#15.Identificación del tipo de dato
#Escribe un programa que tome una entrada del usuario y determine su tipo de dato usando la función `type()`. El programa debe imprimir un mensaje indicando si el dato es un número entero, flotante, cadena de texto, etc.


#16.Calculador de calificaciones
#Crea un programa que pida al usuario que ingrese sus calificaciones en tres materias. Luego, calcula el promedio de esas calificaciones e imprime un mensaje que indique si el alumno aprobó (promedio ≥ 6) o no.


#17.Concatenación de strings
#Escribe un programa que pida al usuario su nombre y su color favorito. Luego, concatena estos datos en una sola oración que diga "Hola [nombre], tu color favorito es [color]" y la imprima.