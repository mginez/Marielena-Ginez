def main():
    lista = [6,5,3,1,8,7,2,4]#1
    for a in range(len(lista)):#n
        menor = a#n
        for b in range(a+1, len(lista)):#n2
            if lista[b] < lista[menor]:#n2
                menor = b #n2
        aux = lista[a] #n
        lista[a] = lista[menor] #n
        lista[menor] = aux #n
    print(lista) #1
    #3n2+5n+2
main()