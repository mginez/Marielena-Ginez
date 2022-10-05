#Elabore un algoritmo que dado un número ingresado por el usuario diga si mencionado número es un “Número Repunit'', 
# y que además indique si la suma de sus dígitos es un número cuadrado.
#Definiciones:
#Número Repunit: todo número que está formado solamente por un solo número. Por ejemplo, 1, 11, 111, 2, 22, 22222, 8, 8888, etc.
#Número Cuadrado: todo número natural que es el cuadrado de otro número natural. Por ejemplo, 9 es un cuadrado ya que 9=3^2.

number = input('Please enter a number ')
list_number = [int(digit) for digit in str(number)]
reference_number = list_number[0] 
is_repunit = True
acum = 0
for digit in list_number:
    acum += digit
    if digit != reference_number:
        is_repunit = False
        print(f'The number {number} is not Repunit')
        break
if is_repunit == True:
    print(f'The number {number} is Repunit', end=' ')

square = acum ** 1/2
if square.is_integer():
    print ('and it\'s square')
else:
    print ('and it\'s not square')

