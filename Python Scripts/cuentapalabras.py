'''Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y
su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla
con la palabra más repetida y su frecuencia.'''

cad = input("Ingrese la frase que quiere analizar:\n")

def dicFrec(cadena):
    listaCad = cadena.split(" ")
    dicPalabras = {}
    for palabra1 in listaCad:
        cont = 0
        for palabra2 in listaCad:
            if palabra1 == palabra2:
                cont += 1
        dicPalabras[palabra1] = cont
    
    return dicPalabras

def tuplaRep (diccionario):
    maxVal = 0
    palabra = ""
    for c,v in diccionario.items():
        if v > maxVal:
            maxVal = v
            palabra = c
    return palabra, maxVal


print(dicFrec(cad),tuplaRep(dicFrec(cad)))