option = input('Please enter a valid option:\n1. Vegetarian\n2. Non Vegetarian\n-> ')
if option == '1':
    option = 'Vegetarian'
    ingredient = input('Please choose the ingredient that you want:\n1. Pepper\n2. Tofu\n->')
    if ingredient == '1':
        ingredient = 'Pepper'
    else:
        ingredient = 'Tofu'
    print ('The pizza is {} and the ingredients are: Tomate, Mozzarella and {}'.format (option, ingredient))

elif option == '2':
    option = 'Non Vegetarian'
    ingredient = input('Please choose the ingredient that you want:\n1. Salmon \n2. Tofu\n->')
    if ingredient == '1':
        ingredient = 'Pepper'
    elif ingredient == '2':
        ingredient = 'Ham'
    else:
        ingredient = 'Salmon'
    print ('The pizza is {} and the ingredients are: Tomate, Mozzarella and {}'.format (option, ingredient))

else:
    print('Invalid option')
