#ordenamiento -> Insertion Sort

def main():
    lista = [6,5,3,1,8,7,2,4] #!
    for i in range(len(lista)): #n
        temp = i #n
        valor = lista[i] #n
        j = i - 1 #n
        while j >= 0 and valor < lista[j]: #n2
            lista[temp] = lista[j] #n2
            lista[j] = valor #n2
            temp -= 1 #n2
            j -= 1 #n2
    print(lista) #1
    #5n2 + 2n + 3
main()