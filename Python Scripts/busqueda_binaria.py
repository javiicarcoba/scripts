#Mediante busqueda binaria, buscamos el indice del target en una lista ordenada.
#Si el target no esta en la lista, devolvemos el indice donde debería estar.
def searchInsert(nums: list[int], target: int) -> int:
    b_izq = 0
    b_der = len(nums)-1
    while b_izq <= b_der:
        i = b_izq + (b_der - b_izq)//2
        if nums[i] == target:
            return i
        elif nums[i] < target:
            b_izq = i+1
        else:
            b_der = i-1
    return b_izq

prueba = [1,3,5,6]
objetivos = [5,2,7]

for objectivo in objetivos:
    print(searchInsert(prueba, objectivo))