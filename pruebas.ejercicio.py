#Escribe un programa que tome una entrada del usuario y determ   entrada = input("Introduce un dato: ")

# Intentar convertir a entero
try:
    valor_convertido = int(entrada)
    print(f"'{entrada}' es un número entero (int).")
except ValueError:
    # Intentar convertir a flotante
    try:
        valor_convertido = float(entrada)
        print(f"'{entrada}' es un número flotante (float).")
    except ValueError:
        # Verificar si es booleano
        if entrada.lower() == "true" or entrada.lower() == "false":
            print(f"'{entrada}' es un valor booleano (bool).")
        else:
            print(f"'{entrada}' es una cadena de texto (str).")




# Solicitar entrada del usuario
entrada = input("Introduce un dato: ")

# Determinar el tipo de dato
if entrada.isdigit():
    tipo_dato = "entero"
elif entrada.replace('.', '', 1).isdigit() and entrada.count('.') < 2:
    tipo_dato = "flotante"
else:
    tipo_dato = "cadena de texto"

# Imprimir el tipo de dato
print(f"El dato introducido es de tipo: {tipo_dato}")