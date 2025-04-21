##Script_1
"""
Crear una variable con valor 20 va a ser como referencia el minimo.
Otra con valor de 500, va a ser como referencia el maximo.
Luego pregunta al usuario por un valor, almacenarlo en otra variable, forzar a que ponga un numero, sino preguntar repetidamente.
Ese numero transformarlo en integer

Ahora imprimir en pantalla.
Si el numero que puso el usuario es menor que el valor minimo definido mostrar el texto VALOR BAJO
Si el numero que puso el usuario es mayor que el valor maximo definido mostrar el texto VALOR ALTO
Si el numero que puso el usuario esta entre el valor minimo y el valor maximo mostrar el texto VALOR MEDIO
"""


valor_min = 20
valor_max = 500

numero = input("Ingrese un numero: ")
while not numero.isdigit():
    numero = input("Ingrese un numero: ")

# debe continuar acá el programa

print("fin del programa........aun sin resolverlo.")

"""
Script 2
Escriba un programa que pida un año y que escriba si es bisiesto o no.
Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí.
"""
año_bisiesto = int(input("Ingrese el año: "))
if (año_bisiesto % 4 == 0 and año_bisiesto % 100 !=0) or (año_bisiesto % 400 ==0):
	print(año_bisiesto, "es bisiesto")
else:
	print(año_bisiesto, "no es bisiesto")
     
##Script_3
"""
Pedir al usuario que ingrese un número de inicio del bucle
Pedir al usuario que ingrese un número de fin del bucle
Validar que el número de inicio sea menor al número de fin, si no es así volver a pedir los dos números, hasta que ésto sea correcto
Luego de que el usuario ingrese los dos números, mostrar en pantalla todos los números que hay entre el número de inicio y el número de fin
De la siguiente manera:
Este es el bucle número 1
Este es el bucle número 2
Este es el bucle número 3
---
Fin del programa.
"""

# Validar entrada del usuario
while True:
    inicio = int(input("Ingrese el número de inicio del bucle: "))
    fin = int(input("Ingrese el número de fin del bucle: "))
    
    if inicio < fin:
        break
    else:
        print("El número de inicio debe ser menor que el número de fin. Intente de nuevo")

# Mostrar los números entre inicio y fin
contador = 1
for i in range(inicio, fin):
    print("Este es el bucle número", contador)
    contador += 1

print("Fin del programa.")

"""
Script 4
Vamos a realizar un programa que nos va a decir la nota promedio de un alumno en todo el cuatrimestre.
Dentro del cuatrimestre son 4 examenes y luego un examen final.
La aprobación del cuatrimestre es con nota 6 o mayor de promedio.
Y si el alumno tiene aprobada la cursada (es decir, obtuvo seis o más de 6 de promedio en sus 4 examenes, rinde el examen final)
Si el alumno tiene aprobada la cursada y el examen final, entonces el alumno aprobó la materia.

Entonces el programa debe preguntar por la nota de cada examen.
En función de las respuestas, primero debe avisar el promedio de las 4 notas de los examenes.
En caso de que el promedio sea mayor o igual a 6, debe avisar que el alumno tiene aprobada la cursada.
En caso de que el promedio sea menor a 6, debe avisar que el alumno no tiene aprobada la cursada.
Luego preguntar por nota del final (en caso de que haya aprobado la cursada), si es mayor o igual a 6, debe avisar que el alumno aprobó la materia.
En caso de que sea menor a 6, debe avisar que el alumno no aprobó el final de la materia, y puede rendir recuperatorio.

"""

nota_uno = float(input("Ingrese la nota del primer examen: "))    
nota_dos = float(input("Ingrese la nota del primer examen: "))    
nota_tres = float(input("Ingrese la nota del primer examen: "))    
nota_cuatro = float(input("Ingrese la nota del primer examen: "))    

promedio = (nota_uno + nota_dos + nota_tres + nota_cuatro) / 4

if promedio >= 6:
    print("El alumno tiene aprobada la cursada.")
    
    # Pedir nota del final
    nota_final = float(input("Ingrese la nota del examen final: "))
    
    if nota_final >= 6:
        print("El alumno aprobó la materia")
    else:
        print("El alumno no aprobó el final, va a recuperatorio")
else:
    print("El alumno no tiene aprobada la cursada")





