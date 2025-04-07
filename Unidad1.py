##Unidad 1## 
##Funcion Print ##Imprimir en pantalla

numero = int(input("Ingrese un numero del 1 al 10 "))
if numero == 7:
    print("Es correcto")
elif numero > 7:
	print("Es incorrecto, el numero es menor")
else:
	print("Es incorrecto, el numero es mayor")
	
"""La función print() es una de las más utilizadas en Python. Se usa para mostrar información en la consola, como mensajes o resultados de cálculos.
La sintaxis básica es:
print(argumento1, argumento2, ...)

Cómo funciona print()
Cuando ejecutamos print(), Python realiza varios pasos:

Comprueba que el nombre print es válido.
Verifica los argumentos que le pasaste. Si algo no coincide, muestra un error.
Ejecuta la función, transforma los argumentos en texto comprensible y los muestra en pantalla.
"""

print("Hola Mundo") 
