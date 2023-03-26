#A partir de un string con datos, separamos la información y la devolvemos en un diccionario de persoanss
datos = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n" \
        "71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n" \
        "98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

info = datos.split("\n")
atributos = info[0].split(";")
info.pop(0)
atributos.pop(0)
dicPersonas = {}
cont1 = 0

for datos in info:
    dicInfo = {}
    cont2 = 0
    nif = info[cont1].split(";", 1)
    aux = nif[1].split(";")
    while cont2 != len(aux):
        dicInfo[atributos[cont2]] = aux[cont2]
        cont2 += 1
    dicPersonas[nif[0]] = dicInfo
    cont1 += 1

print(dicPersonas)