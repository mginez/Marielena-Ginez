def print_options(options_dictionary):
    for key, value in options_dictionary.items():
        print(key, end = '')
        for k, v in value.items():
            print(f' - {v}', end = '')
        print('')

def print_receipt(client_dictionary, client_total, options_dictionary):
    print('\n****** RECEIPT ******')
    for key, value in client_dictionary.items():
        if key != 'ID':
            print(f'{key}: {value}')
        else:
            print(f'{key}:', options_dictionary[value]['name'])
    print(f'TOTAL: {client_total}')
    print('')

def main():
    options_dictionary = {
        'X': {
            'name':'a',
            'price':0
        },
        'Y': {
            'name':'a',
            'price':0
        },
        'Z': {
            'name':'a',
            'price':0
        }
    }
    while True:

        if input('Do you want to continue Y or N: ') == 'N':
            break
main()