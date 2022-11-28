lista = ['a', 'b', 'c', 'd', 'e']

def search(lista, letter, index):
    if letter == lista[index]:
        return letter
    else:
        if index == len(lista):
            if letter == lista[index]:
                return letter
            else:
                return None
        return search(lista, letter, index+1)