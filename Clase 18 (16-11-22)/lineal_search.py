#Search -> lineal search

def lineal_search(lista, number):
        for n in lista:
            if n==number:
                return number

def main():
    lista = [6,5,3,1,8,7,2,4]
    number = int(input('Please enter a number: '))
    if lineal_search(lista, number):
        print(f'The number {number} is on the list.')
    else:
         print(f'The number {number} is not on the list.')
    
main()