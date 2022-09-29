number = int(input('Please enter a number from 2 to 12: '))
acum=0
count=0
list = []
print(f'The pairs of numbers in the dice that added are equal to number {number} are: ')
for aux in range (1, number):
    acum = number - aux
    if aux and acum not in list:
        list.append(aux)
        list.append(acum)
        print (list[count], 'and', list[count+1])
    count += 2   
