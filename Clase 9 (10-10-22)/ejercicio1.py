
def print_welcome():
    print('*** Welcome ***')
def get_option(studies):
    for key, value in studies.items():
        for key_interno, value_interno in value.items():
            print(f'{key} - {value_interno}', end = '')
        print('')
    return input('Please enter an option: ')
def get_client_data(study):
    client = {
        'id':input('Please enter your ID: '),
        'age':input('Please enter your age: '),
        'gender':input('Please enter your gender: '),
        'study': study
    }
    return client
def print_invoice(client, studies, discount):
    print('***RECEIPT***')
    print('id card:', client.get('id'))
    print('age:', client.get('age'))
    print('gender:', client.get('gender'))
    print('study:', client.get('study').get('description'))
    print('Net Amount:', studies.get(client.get('study').get('price'))) 
clients = []
def get_discount(client, studies, client_number):
    discount = 0
    if client.get('gender') == 'F' and int(client.get('age')) > 55:
        discount += studies.get('study').get('price') * 0.25
    elif client.get('gender') == 'M' and int(client.get('age')) > 65:
        discount += studies.get('study').get('price') * 0.25

    if client_number % 2 != 0:
        discount += studies.get('study').get('price') * 0.02

    return discount

def main():
    studies_dict = {
        'U':{
            'description':'Ultrasonido',
            'price': 8900
        },
        'I':{
            'description': 12640
        },
        'R':{
            'description':'Resonancia',
            'price': 15600
        }
    }

    print_welcome()
    while True:
        option = get_option(studies_dict)
        client = get_client_data(option)
        clients.append(client)
        discount = get_discount(client, studies_dict, len(clients))
        print(discount)
        print_invoice(client, studies_dict, discount)
main()