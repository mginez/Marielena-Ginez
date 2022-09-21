num1 = input('Introduzca un numero ')
num2 = input('Introduzca otro numero ')
is_valid = True

if num1.isnumeric():
    num1= float(num1)
else:
    is_valid = False

if num2.isnumeric():
    num2= float(num2)
else:
    is_valid = False

if num2 == 0:
    print('No es posible la division por cero')
else:
    num3= num1/num2
    print(f'La division de los numeros es {num3}')