'''Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-1.txt con la tabla de
multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un
mensaje por pantalla informando de ello.'''

def buscaResult(a, b):
    cont = 1
    try:
        tabla = open('tabla-'+n+'.txt', 'r')
        for operacion in tabla:
            if cont == int(b):
                result = operacion
            cont += 1
        tabla.close()
    except:
        result = "No esta la tabla del " + a

    return result

n = input("Ingrese el primer numero (del 1 al 10): ")
m = input("Ingrese el segundo numero (del 1 al 10): ")

print(buscaResult(n, m))