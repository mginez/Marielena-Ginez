number = int(input('Please enter a postive number: '))
number2 = 1
for number_for in range(1, number+1, 2):
    if number_for >= number -1:
        print(number_for)
    else:
        print(number_for, end=", ")