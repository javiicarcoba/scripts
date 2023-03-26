import random
#Escribir una función que reciba un número positivo y devuelva la potencia n de este numero
def potencia(base, exponente):
    if exponente == 0:
        return 1
    
    if exponente % 2 == 0:
        pot = potencia(base,exponente/2)
        res = pot * pot
    else:
        pot = potencia(base, (exponente-1)/2)
        res = pot * pot * base

    return res

#Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.
def digitos(num):
    if num < 10:
        return 1
    else:
        cant = digitos(num//10)
        res = cant + 1
    
    return res

"""
    El juego de la rata consiste en que una rata tiene 3 opciones de escape de la jaula de donde esta capturada.
    Si elige el camino uno tardara 3 minutos en recorrer la ruta y volverá a la jaula.
    Si elige el camino dos tardara 5 minutos y volverá a la jaula.
    Si elige el camino tres podrá escapar.
    Esta función devolverá el tiempo que tarda la rata en escapar de la jaula.
"""
def juego_rata():
    camino_elegido = random.randint(1, 3)
    if camino_elegido == 1:
        return 3 + juego_rata()
    elif camino_elegido == 2:
        return 5 + juego_rata()
    else:
        return 7
    
print(f"La rata a tardado {juego_rata()} minutos en salir de la jaula")