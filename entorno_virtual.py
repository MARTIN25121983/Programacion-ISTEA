#Creacion de entorno virtual
##py --version #Desde el cmd

import nmap

scanner = nmap.PortScanner()

ip = '192.168.0.14'
puertos = '22-80'  # Puedes cambiar esto a '1-1024' o lo que necesites

scanner.scan(ip, puertos)

print(f"Escaneo de {ip} en puertos {puertos}:")
for port in scanner[ip]['tcp']:
    estado = scanner[ip]['tcp'][port]['state']
    print(f"Puerto {port}/tcp: {estado}")

##pyhton -m venv mi_entorno #Crear entorno
##mi_entorno\Scripts\activate #Activar entorno
##pip install requests #Gestor para instalar paquetes
#Entorno virtual se creo en C:\Users\mario\mi_entorno



## pypi.org se busca modulos

def calculadora(operacion, num1, num2):
    """
    Operacion matematica entre dos números.

    Parámetros:
        operacion (str): Tipo de operación: "suma", "resta", "multiplicación", "división".
        num1 (float): Primer número.
        num2 (float): Segundo número.

    Retorna:
        float: Resultado de la operación.

    Maneja errores comunes como:
        - Operación no válida
    """
    try:
        if operacion == "suma":
            return num1 + num2
        elif operacion == "resta":
            return num1 - num2
        elif operacion == "multiplicación":
            return num1 * num2
        elif operacion == "división":
            return num1 / num2
        else:
            ValueError("Operación no válida. Usa: suma, resta, multiplicación o división.")
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."


#doc stream
"""import nmap

scanner = nmap.PortScanner()

ip = '192.168.0.14'
puertos = '22-80'  # Puedes cambiar esto a '1-1024' o lo que necesites

scanner.scan(ip, puertos)

print(f"Escaneo de {ip} en puertos {puertos}:")
for port in scanner[ip]['tcp']:
    estado = scanner[ip]['tcp'][port]['state']
    print(f"Puerto {port}/tcp: {estado}")



"""
