from asyncore import read
#script para leer la cadena de insulina ingresada en un archivo txt

insulina = open('prepoinsulin-seq.txt', 'r')
cadenaIns = insulina.read()
cont = 0
isinsulinSeq = binsulinSeq = cinsulinSeq = ainsulinSeq = ""

for letras in cadenaIns:
    if cont<=24:
        isinsulinSeq = isinsulinSeq + letras
    elif cont<=54 and cont>24:
        binsulinSeq = binsulinSeq + letras
    elif cont<=89 and cont>54:
        cinsulinSeq = cinsulinSeq + letras
    elif cont<=110 and cont>89:
        ainsulinSeq = ainsulinSeq + letras
    cont +=1

insulin = binsulinSeq + ainsulinSeq

print("La secuencia de la prepoinsulina humana {}.\nIsinsulina: {}\nBinsulina: {}\nCinsulina: {}\nAinsulina: {}\nInsulina: {} "
      .format(cadenaIns, isinsulinSeq, binsulinSeq, cinsulinSeq, ainsulinSeq, insulin))