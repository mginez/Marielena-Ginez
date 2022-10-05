infraction={
    1:{"name":"Choque", "cost":50},
    2:{"name":"Semáforo", "cost":30},
    3:{"name":"Falta de documentos", "cost":100},
}

officers={
    1:{"name":"Luis", "lastName":"Bello","ci":13452224},
    2:{"name":"Jose", "lastName":"Quevedo","ci":44235611},
    3:{"name":"Antonio", "lastName":"Guerra","ci":12345678},
}

db={}
register = []
option = '' 
key_list = ['Name', 'Lastname', 'ID']

print('\nWelcome to the Transit Database\n')

while option != '4':
    option = input('\nPlease enter an option:\n 1. Enter data\n 2. Delete data\n 3. Show database\n 4. Exit\n -> ')
    if option == '1':
        for key in key_list:
            db[key] = input(f'Please enter the {key} ')

        for id, inf in infraction.items():
            print(id, inf)

        type_inf = int(input('Please choose the type of infraction '))
        db['Infraction'] = infraction[type_inf]

        for id, inf in officers.items():
            print(id, inf)

        name_off = int(input('Please choose the officer '))
        db['Officer'] = officers[name_off]
        register.append(db)
        print('\nThe current register is:\n')
        for criminal in register:
            print(register.index(criminal), end = '. \n')
            for k, v in criminal.items():
                print(k, ':', v)
            print('\n')
    
        db = {}
        option = ''

    if option == '2':
        print('\nThe current register is:\n')
        for criminal in register:
            print(register.index(criminal), end = '. \n')
            for k, v in criminal.items():
                print(k, ':', v)
            print('\n')
        item_number = int(input('\nPlease enter the item you want to delete'))
        register.pop(item_number)
        print('\nThe current register is:\n')
        for criminal in register:
            print(register.index(criminal), end = '. \n')
            for k, v in criminal.items():
                print(k, ':', v)
            print('\n')
        option = ''

    if option == '3':
        print('\nThe current register is:\n')
        for criminal in register:
            print(register.index(criminal), end = '. \n')
            for k, v in criminal.items():
                print(k, ':', v)
            print('\n')
        option = ''

print('\nChanges saved. Have a good day!')