#Validar que un numero introducido es oblongo. Numero oblongo: la multiplicacion de dos numeros consecutivos.

number = int(input('Please enter a  number: '))
count = 1
aux = 1
oblongo = 0
is_oblongo = False
for count in range(1, number):
    aux = count + 1
    oblongo = count * aux
    if number == oblongo:
        is_oblongo = True
        print (f'The number {number} is oblongo')
        break
if is_oblongo == False:
    print (f'The number {number} is not oblongo')

