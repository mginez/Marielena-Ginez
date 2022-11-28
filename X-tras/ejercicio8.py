def print_options(options):
    for key, value in options.items():
        print(key, end = '')
        for k, v in value.items():
            print(f' - {v}', end = '')
        print('')

def main():
    options = {
        'L':{
            'name':'Lomito',
            'price': 15
        },
        'P':{
            'name':'Punta',
            'price': 8
        },
        'M':{
            'name':'Molida',
            'price': 6
        }
    }
    client_count = 0
    discount_count = 0
    while True:
        client = {}
        purchase = {}
        client['ID'] = input('Please enter your ID: ')
        client['Name'] = input('Please enter your name: ')
        
        print_options(options)
        while True:
            purchase['Type'] = input('Please enter your name: ')

            if input('Do you want to add another purchase: ').upper == 'N':
                break
        print(client)

        if input('Do you want to continue Y or N: ') == 'N':
            break
main()