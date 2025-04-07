#15.Identificación del tipo de dato
#Escribe un programa que tome una entrada del usuario y determine su tipo de dato usando la función `type()`. El programa debe imprimir un mensaje indicando si el dato es un número entero, flotante, cadena de texto, etc.
entrada = input("Ingrese la informacion ")
if entrada == int(entrada):
    print(type()"Introduzco un entero"))
elif entrada == float(entrada):
    print(type("Introduzco un flotante"))
elif entrada == str(entrada):
    print(type("Introduzco cadena de texto"))
else:
    print(type("Introduzco un booleano"))