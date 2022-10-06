#Nombre del estudiante: Marielena Ginez
#Carnet: 20221110395
#=====================================================================================
number = input('Please enter a number ')
reference_number = number[0] 
is_repunit = True
for digit in number:
    if digit != reference_number:
        is_repunit = False
        print(f'The number {number} is not Repunit')
        break
if is_repunit == True:
    print(f'The number {number} is Repunit', end=' ')