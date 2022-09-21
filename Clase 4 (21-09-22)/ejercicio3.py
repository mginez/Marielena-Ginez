number = int(input('Please enter a number: '))
aux = number - 1
acum = 0

while aux >= 1:
    if number%aux == 0:
        acum+=aux
    aux-=1

if acum >= number:
    print(f'The number {number} is abundant')
else:
    print(f'The number {number} is not abundant')