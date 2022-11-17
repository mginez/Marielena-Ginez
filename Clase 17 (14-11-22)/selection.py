#ordenamiento -> Selection Sort

def main():
    lista = [6,5,3,1,8,7,2,4]#1
    for i in range(len(lista)):#n
        menor = i#n
        for j in range(i+1, len(lista)):#n2
            if lista[j] < lista[menor]:#n2
                menor = j #n2
        temp = lista[i] #n
        lista[i] = lista[menor] #n
        lista[menor] = temp #n
    print(lista) #1
    #3n2+5n+2
main()