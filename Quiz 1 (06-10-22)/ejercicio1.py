#Nombre del estudiante: Marielena Ginez
#Carnet: 20221110395
#=====================================================================================

penta = [[45,78,65],[12,35,70],[51,3,105],[22,12,85]]
penta_calc = 0
count = 1

print('The pentagonal numbers are: ')
for item in penta:
    for number in item:
        for count in range(1, number):
            penta_calc = count*(3*count-1)/2
            if penta_calc == number:
                print(number)
                break
            count += 1
