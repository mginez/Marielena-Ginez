number = int(input('Please enter a number: '))
aux = 1
for number_for in range (1, number*2, 2):
    aux = number_for
    while aux >= 1:
        if aux == 1:
            print(aux)
        else:
            print(aux, end= ' ')
        aux -= 2