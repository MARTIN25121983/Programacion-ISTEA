#Itineraciones - Operadores Relacionales

##Bucle while. nos permite ejecutar un bloque de código varias veces
##Estructura
##while expresion_condicional: 
##  Bloque de instrucciones 
##  Más instrucciones... 

#Ejemplo
contador = 5 
  
while contador > 0: 
    print("Estoy dentro del bucle... Quedan", contador, "iteraciones") 
    contador -= 1  # Restamos 1 al contador 
 
print("Fin del programa") 

n = 3   
while n > 0: 
    print("Valor de n:", n) 
    n -= 1 
else: 
    print("El bucle terminó correctamente")
#Operadores logicos
# and, or, not 
# and: devuelve True si ambas condiciones son verdaderas
# or: devuelve True si al menos una de las condiciones es verdadera
# not: invierte el valor de verdad de una condición (True se convierte en False y viceversa)

#Ejemplo and
# Verificar si ambas condiciones son verdaderas 
edad = 25 
salario = 30000 
if edad > 18 and salario > 25000: #Se debe cumplir ambas condiciones
    print("Cumples con los requisitos.") 

#Ejemplo or
# Verificar si al menos una condición es verdadera 
efectivo = 0 
tarjeta = True 
if efectivo > 0 or tarjeta: #se cumple si alguna de las dos condiciones son verdaderas.
    print("Puedes hacer las compras.")

#Ejemplo not
# Invertir una condición 
llueve = False 
if not llueve: #al ser la variable falsa al colocar un not se transforma en verdadero o viceversa. 
    print("Podemos salir a caminar.")

