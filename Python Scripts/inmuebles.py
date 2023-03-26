'''Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:'''

listaInm = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
            {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
            {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
            {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
            {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

'''Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. 
La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con los inmuebles cuyo 
precio sea menor o igual que el dado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada 
diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las siguiente fórmula en función 
de la zona:

Zona A: precio = (metros x 1000 + habitaciones x 5000 + garaje x 15000) x (1 - antiguedad / 100)
Zona B: precio = (metros x 1000 + habitaciones x 5000 + garaje x 15000) x (1 - antiguedad / 100) x 1.5
'''

def buscaInmuebles(lista, precioCli):
    presupuesto = []
    cont = 0
    for inmuebles in lista:
        if lista[cont].get('zona') == 'A':
            precioInm = lista[cont].get('metros')*1000 + lista[cont].get('habitaciones')*5000
            if lista[cont].get('garage'):
                precioInm = precioInm + 15000
            precioInm = precioInm*(1 - (2022 - lista[cont].get('año')) / 100)
        elif lista[cont].get('zona') == 'B':
            precioInm = lista[cont].get('metros')*1000 + lista[cont].get('habitaciones')*5000
            if lista[cont].get('garage'):
                precioInm = precioInm + 15000
            precioInm = precioInm*(1 - (2022 - lista[cont].get('año')) / 100)*1.5
        
        if precioInm <= int(precioCli):
            presupuesto.append({'inmueble': lista[cont], 'precio': precioInm})
        cont += 1
    return presupuesto

print("Estos son los inmuebles que estan en el precio dado:\n{}".format(buscaInmuebles(listaInm,
       input("Ingrese el precio máximo que desea pagar: "))))