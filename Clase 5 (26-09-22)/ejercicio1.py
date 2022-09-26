number = int(input('Please enter a postive number: '))
number2 = 1
while number2 < number:
    if number2 < number - 1:
        print(number2, end=', ')
    else:
        print(number2)
    number2 += 2