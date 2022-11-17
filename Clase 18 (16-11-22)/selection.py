
def selection(lista):
    for i in range(len(lista)):
            menor = i
            for j in range(i+1, len(lista)):
                if lista[j] < lista[menor]:
                    menor = j
            temp = lista[i]
            lista[i] = lista[menor]
            lista[menor] = temp
    return lista