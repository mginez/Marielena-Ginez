#ordamiento -> Quick Sort

def quicksort(lista):
    if len(lista) < 2:
        return lista
    menor, pivote, mayor = partition(lista)
    return quicksort(menor) + [pivote] + quicksort(mayor)
    
def partition(lista):
    menores = []
    mayores = []
    pivote = lista[0]
    for i in range(len(lista)):
        if lista[i] < pivote:
            menores.append(lista[i])
        elif lista[i] > pivote:
            mayores.append(lista[i])
    return menores, pivote, mayores

def main():
    lista = [6,5,3,1,8,7,2,4]
    lista2 = quicksort(lista)
    print(lista2)
main()