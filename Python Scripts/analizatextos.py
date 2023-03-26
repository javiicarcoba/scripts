'''
Dado un texto y una lista de caracteres permitidos, devolver un diccionario siendo la llave cada palabra y el valor de
la misma una tupla con la cantidad de veces que se repite la palabra, la posición de la primera vez que se encontró y
la posición de la úlitma vez que se repitió. (Si aparece solo una vez la palabra, la posición inicial y final será la misma)
Si una palabra tiene un caracter que no esta en la lista de caracteres permitidos, esta palabra no se contará.
'''

def analizar_texto(texto, caracteres_permitidos):
    texto = texto.lower()
    diccionario = {}
    palabra = ""
    posicion = 0
    for caracter in texto:
        if caracter in caracteres_permitidos:
            palabra += caracter
        else:
            if palabra:
                if palabra in diccionario:
                    diccionario[palabra] = (diccionario[palabra][0]+1, diccionario[palabra][1], posicion-len(palabra))
                else:
                    diccionario[palabra] = (1, posicion-len(palabra), posicion-len(palabra))
                palabra = ""
        posicion += 1
    if palabra:
        if palabra in diccionario:
            diccionario[palabra] = (diccionario[palabra][0]+1, diccionario[palabra][1], posicion-len(palabra))
        else:
            diccionario[palabra] = (1, posicion-len(palabra), posicion-len(palabra))
    return diccionario


texto = "Muchos años después frente al pelotón de fusilamiento el coronel Aureliano Buendía había de recordar aquella " \
        "tarde remota en que su padre lo llevó a conocer el hielo"
caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'á', 'é', 'í', 'ó', 'ú', 'ñ']

print(analizar_texto(texto, caracteres))