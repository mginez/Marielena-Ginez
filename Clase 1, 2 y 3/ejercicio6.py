numero = input('Introduzca un numero ')
is_valid = True

if numero.isnumeric():
    numero= float(numero)
else:
    is_valid = False
    print('Error')

if numero % 2 == 0:
    print (f'El numero {numero} es par')
else:
    print (f'El numero {numero} es impar')