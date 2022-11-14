#ordenamiento -> Selection Sort

def main():
    lista = [6,5,3,1,8,7,2,4]
    for i in range(len(lista)):
        menor = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        temp = lista[i]
        lista[i] = lista[menor]
        lista[menor] = temp
    print(lista)
main()