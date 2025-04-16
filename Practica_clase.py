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

"""
Script 3
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

