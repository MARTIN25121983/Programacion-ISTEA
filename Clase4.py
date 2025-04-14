##While Bucle. con break salimos del bucle
contador = 10

while contador > 0:
    print("Estoy dentro del bucle while, quedan ", contador, "iteraciones")
    contador -= 1
print("Fin del programa")

### and ###

numero = 15

if numero > 10 and numero < 20:
    print("El número está entre 10 y 20.")
else:
    print("El número está fuera del rango de 10 a 20.")

### or ###

numero = 120

if numero < 0 or numero > 100:
    print("El número es negativo o mayor que 100.")
else:
    print("El número está entre 0 y 100.")

### not ###

numero = 5

if not numero == 0:
    print("El número no es igual a cero.")
else:
    print("El número es igual a cero.")

#for 
muchos_nombres = ["Juan", "Pedro", "Maria", "Ana", "Luis"]
for nombre in muchos_nombres:
    print( nombre)
print("Fin del programa")

for numero in range(10): ##Arranca del 0 al 10 y uno para atras
    print("valor del numero:", numero) ##imprime del 0 al 9

##for numero (10,20, 2) Va del 2 en 2 del 10 al 20.

## for break
for i in range(10):
    print("La variable i vale", i)
    pass ## no realiza ninguna accion, se realiza para seguir con el codigo sino da error
    print("Aca sigue")

