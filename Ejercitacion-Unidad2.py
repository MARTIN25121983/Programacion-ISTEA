
# 1. Calcula el área de un rectángulo con base 5 y altura 3. Imprime el resultado.
base = 5
altura = 3
resultado = base * altura
print("El area del rectangulo es ",  resultado)

# 2. Convierte la temperatura de Celsius a Fahrenheit. Pide al usuario ingresar la temperatura en Celsius y luego imprime la temperatura equivalente en Fahrenheit.
temperatura_celsius = float(input("Ingrese la temperatura "))
temperatura_farenheit = (temperatura_celsius * 9/5) + 32
print("La temperatura en farenheit es", temperatura_farenheit)

# 3. Concatena tu nombre y tu edad como strings y guárdalos en una variable. Luego imprime el tipo de dato de esa variable.
nombre = "Martin"
edad = 41
informacion_personal = nombre + str(edad)
print(type(informacion_personal))

# 4. Calcula el área de un círculo con radio 4. Imprime el resultado.
##Area de un circulo = 3.14 * r **2
pi = 3.14
radio= 4
resultado= pi * (radio ** 2)
print("El area del circulo es ", resultado)

# 5. Pide al usuario que ingrese dos números y muestra la suma, resta, multiplicación y división de esos números.
numero_uno = float(input("Ingrese un numero "))
numero_dos = float(input("Ingrese un numero "))
suma = (numero_uno + numero_dos)
resta = (numero_uno - numero_dos)
multiplicacion =(numero_uno * numero_dos)
division = (numero_uno / numero_dos)

print("La suma es =", suma)
print("La resta es =", resta)
print("La multiplicacion es =", multiplicacion)
print("La division es =", division)


# 6. Almacena el resultado de una operación aritmética compleja en una variable y luego imprime tanto el resultado como el tipo de dato de esa variable.
operacion_compleja = (3*2) + (4/2) ** 3
print("El resultado de la operacion compleja es" , operacion_compleja)
print(type(operacion_compleja))

# 7. Crea una variable booleana que represente si un alumno ha aprobado o no un examen y luego imprime su estado.
nota = 8
aprobado = nota >=6
print (aprobado)

# 8. Calcula el perímetro de un triángulo equilátero con lados de longitud 6. Imprime el resultado.
#Perimetro del triangulo es = A + B + C
lado = 6
perimetro_triangulo = 3 * 6
print("El perimetro del triangulo equilatero es" , perimetro_triangulo)

# 9. Pide al usuario que ingrese su nombre, edad y ciudad de residencia y luego imprime cada uno de esos datos con su respectivo tipo de dato.
nombre = input("Ingrese su nombre ")
edad = input("Ingrese su edad ")
ciudad_de_residencia = input("Ingrese su ciudad de residencia ")

print(type(nombre))
print("El nombre es: " , nombre)
print(type(edad))
print("La edad es: " , edad)
print(type(ciudad_de_residencia))
print("La ciudad de residencia es: " , ciudad_de_residencia)


# 10. Realiza una operación matemática que involucre paréntesis, multiplicación, suma y resta. Guarda el resultado en una variable y luego imprímela junto con su tipo de dato.
operacion_matematica = (3*2) + (4-2)
print(type(operacion_matematica))
print("El resultado es:" , operacion_matematica)