'''Script para saber el total de ganancias de una panaderia teniendo en cuenta el valor del pan y
el descuento que se le hace por ser pan de otro dia'''
valorPan = 3.49
descuento = 0.6
valorPanAyer = valorPan - (valorPan*descuento)

cantidadPan = int(input("Cuantas barras de pan vendio hoy? "))
cantidadPanAyer = int(input("Cuantas de estas son de otro dia? "))

print("El valor del pan fresco es de {:.2f}.\nEl descuento que se le hace a los panes de otro dia es {:.2f}.\n"
      "El costo de esta seria {:.2f}.\nLas ganancias totales son {:.2f}".format(valorPan,(valorPan*descuento),
        valorPanAyer,((cantidadPan-cantidadPanAyer)*valorPan)+(cantidadPanAyer*valorPanAyer)))