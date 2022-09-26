number = int(input('Please enter a number: '))
count = 0
square = 0
compare = number - square
while abs(compare) > count:
    count += 1
    square = count**2
    compare = number - square 
print(f'The closest square is: {square}')

        