

"""
EJERCICIO 2
###########


Combina dos listas: Escribe una función que combine dos listas en una sola lista.
Ejemplo: [1, 2, 3] y [4, 5, 6] se convierte en [1, 2, 3, 4, 5, 6].

"""

def combinar_listas(lista1, lista2):
    return lista1 + lista2

lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
lista_combinada = combinar_listas(lista_1, lista_2)
print(lista_combinada)  # Resultado: [1, 2, 3, 4, 5, 6]


"""
EJERCICIO 5
###########


Escribe una función llamada es_primo que reciba un número entero como parámetro y determine si es primo o no.
La función debe utilizar un bucle while para verificar si el número es divisible por algún otro número menor que él mismo (excluyendo 1 y el propio número). Si encuentra un divisor, debe retornar False, indicando que el número no es primo. Si no encuentra ningún divisor, debe retornar True, indicando que el número es primo.

"""

def es_primo(numero):
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    
    divisor = 2
    while divisor < numero:
        if numero % divisor == 0:
            return False  # Encontró un divisor, no es primo
        divisor += 1
    
    return True  # No encontró divisores, es primo

# Ejemplo de uso:
print(es_primo(7))  # True
print(es_primo(10)) # False



def interseccion(lista1, lista2):
    """Devuelve la intersección de dos listas."""
    return list(set(lista1) & set(lista2))

def diferencia(lista1, lista2):
    """Devuelve la diferencia entre dos listas."""
    return list(set(lista1) ^ set(lista2))

# Ejemplo de uso:
lista_a = [1, 2, 3, 4, 5]
lista_b = [3, 4, 5, 6, 7]

print("Intersección:", interseccion(lista_a, lista_b))
print("Diferencia:", diferencia(lista_a, lista_b))
