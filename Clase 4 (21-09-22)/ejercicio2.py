number = int(input('Please enter a number: '))
aux = number - 1
is_prime = False

while aux > 1:
    if number%aux == 0:
        is_prime = True
        break
    aux-=1

if number > 1 and is_prime == True:
    print(f'The number {number} is prime')
else:
    print(f'The number {number} is not prime')