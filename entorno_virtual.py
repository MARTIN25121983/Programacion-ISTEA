#Creacion de entorno virtual
##py --version #Desde el cmd
##pyhton -m venv mi_entorno #Crear entorno
##mi_entorno\Scripts\activate #Activar entorno
##pip install requests #Gestor para instalar paquetes
#Entorno virtual se creo en C:\Users\mario\mi_entorno

## pypi.org se busca modulos

#doc stream
import nmap

scanner = nmap.PortScanner()

ip = '192.168.0.14'
puertos = '22-80'  # Puedes cambiar esto a '1-1024' o lo que necesites

scanner.scan(ip, puertos)

print(f"Escaneo de {ip} en puertos {puertos}:")
for port in scanner[ip]['tcp']:
    estado = scanner[ip]['tcp'][port]['state']
    print(f"Puerto {port}/tcp: {estado}")