#Tratamiento de errores
import socket


def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
    return open_ports

# Ejemplo de uso
host = '192.168.0.14'
ports = scan_ports(host, 20, 1024)
print(f"Puertos abiertos en {host}: {ports}")


"""
Tipos de errores

Errores de Sintaxis: Ocurren cuando el código no sigue las reglas del lenguaje. Son fáciles de 
detectar, ya que los editores suelen resaltarlos y el intérprete avisa antes de ejecutar el código. 
Ejemplo: Olvidar cerrar comillas en una cadena. 

Errores Semánticos o Lógicos: El código se ejecuta, pero con lógica incorrecta. Ejemplo: Usar el 
operador equivocado en una comparación. Son más difíciles de detectar por que no nos avisa el 
interpretador. 

Errores en Tiempo de Ejecución: Suceden mientras el programa corre, como intentar dividir por 
cero o acceder a índices fuera de rango. Nos vamos a enterar con seguridad por la interrupción 
brusca. 

En resumen podemos dividir los errores en: 

De sintaxis (detectados antes de la ejecución) 
En tiempo de ejecución (errores por excepciones, se detiene.) 
Lógicos (comportamiento inesperado sin mensajes de error) 

La palabra clave reservada try marca el lugar donde intentas ejecutar un código que podría 
fallar. 

La palabra clave reservada except indica el lugar donde puedes manejar el error si ocurre, 
o notificarlo y detener la ejecución. 

Cualquier código dentro del bloque try se ejecuta de manera especial. Si se produce un 
error, la ejecución no se interrumpe. En su lugar, el control salta directamente a la primera 
línea del bloque except, y el resto del bloque try no se ejecuta. 

El código en el bloque except solo se ejecuta si ocurre una excepción en el bloque try. o 
se puede acceder a este bloque de ninguna otra forma.  

Una vez que el bloque try o except se ha ejecutado correctamente, el programa vuelve 
al flujo normal y continúa con las siguientes líneas de código.

"""

##Try, except

#Ejemplo

numero = input("Ingresa un número: ") 

try: 
    numero = float(numero) 
    print(f'el reciproco de {numero} es {1/numero}')   
except ValueError: 
    print("ERROR: El valor ingresado no es un número....")     
    exit() 
except ZeroDivisionError: 
    print("ERROR: No se puede dividir por cero --------")  
print("Acá continua el programa.....") 

def dividir(a, b):    
    try: 
        resultado = a / b     
    except ZeroDivisionError: 
        print("Error: No se puede dividir por cero.") 
    else: 
        print(f"Resultado: {resultado}")  
    finally: 
        print("Fin del intento de división.")   
# Ejemplo de uso 
dividir(10, 2)  # Caso exitoso 
dividir(5, 0)   # Caso con excepción 