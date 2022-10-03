dictionary = {}
list = []
list2 = []
exit = ''
user = ''
while exit.title() != 'Yes':
    data_key = input('Please enter the data you want to save ')
    list.append(data_key)
    exit = input('Continue? ')

for key in list:
    while user.title() != 'Yes':
        list2.append(input(f'Please enter the {key} '))
        dictionary[key] = list2
        user = input('Next item? ')
    user = ''
    list2 = []
print(dictionary)

    