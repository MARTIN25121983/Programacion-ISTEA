#Creacion de entorno virtual
##py --version #Desde el cmd
##pyhton -m venv mi_entorno #Crear entorno
##mi_entorno_virtual\Scripts\activate.bat #Activar entorno
##pip install requests #Gestor para instalar paquetes
#Entorno virtual se creo en C:\Users\mario\mi_entorno_virtual
##https://www.programaenpython.com/miscelanea/crear-entornos-virtuales-en-python/

import nmap

# Predefined
separator = "********************************************"

# Functions
def printFoundHosts( allHostsList : list[str] ):
    if len( allHostsList ) > 0:
        print( "\n*--- Dispositivos encontrados:\n" )

        for i, host in enumerate( allHostsList ):
            print( separator )
            print( f"*** Dispositivo #{ i + 1 } ***" )
            print( f"Nombre:        { devScanner[host].hostname() }" )
            print( f"Dirección Ip:  { host }" )

            if 'mac' in devScanner[host]['addresses']:
                print( f"Dirección MAC: { devScanner[host]['addresses']['mac'] }" )

            print( f"Estado:        { devScanner[host].state() }" )
            
            protocolsList = devScanner[host].all_protocols()

            if len( protocolsList ) > 0:
                print( "\n* Protocolos *" )

                for proto in devScanner[host].all_protocols():
                    print( f"\tProtocolo: { proto }" )
                    lport = devScanner[host][proto].keys()
                    #lport.sort()
                    for port in lport:
                        print ( f"\t\tPuerto: { port }\tEstado: { devScanner[host][proto][port]['state'] }" )

        print( separator )
    else:
        print( "\nNo se encontraron dispositivos en el segmento de red indicado." )

## pypi.org se busca modulos