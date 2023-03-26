#Script para contar cuantas veces aparece una letra dada
frase = input("Ingrese una frase: ")
letra = input("Que letra desea contar?: ")

cont = 0

for letras in frase:
    if letras == letra:
        cont=cont+1
print("La cantidad de letras es: {}".format(cont))