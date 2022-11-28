def print_options(types_vehicles):
    for key, value in types_vehicles.items():
        print(key, end = '')
        for k, v in value.items():
            print(f' - {v}', end = '')
        print('')

def print_receipt(client, client_total, types_vehicles):
    print('****** RECEIPT ******')
    for key, value in client.items():
        if key != 'Type of vehicle':
            print(f'{key}: {value}')
        else:
            print(f'{key}:', types_vehicles[value]['name'])
    print(f'TOTAL: {client_total}')

def print_day(types_vehicles, client_count, discount_count, per_vehicle):
    name = ''
    print('\n****** END OF THE DAY ******')
    print(f'Total Clients: {client_count}')
    print(f'Total Discounts: {discount_count}')
    for key, value in per_vehicle.items():
        name = types_vehicles[key]['name']
        print(f'Promedio {name}: ', end = '')
        try:
            print(per_vehicle[key]['total']/per_vehicle[key]['clients'])
        except:
            print(0)


def main():
    types_vehicles = {
        'A': {
            'name': 'Automatico',
            'price': 2500
        },
        'S': {
            'name':'Sincronico',
            'price': 3500
        }
    }
    per_vehicle = {
        'A':{
            'clients':0,
            'total':0
        },
        'S':{
            'clients':0,
            'total':0
        }
    }
    client = {}
    client_count = 0
    discount_count = 0
    while True:
        price = 0
        discount = 0
        client_count += 1
        client['ID'] = input('Please enter your ID: ')
        print_options(types_vehicles)
        client['Type of vehicle'] = input('Please enter the ID of the type of vehicle you want: ')
        client['Hours'] = int(input('Please enter the duration -in hours- of the class you want to take: '))
        price = types_vehicles[client['Type of vehicle']]['price']
        if client['Hours'] > 3:
            discount = price * 0.15
            discount_count += 1
        client_total = price - discount
        print_receipt(client, client_total, types_vehicles)
        per_vehicle[client['Type of vehicle']]['clients'] += 1
        per_vehicle[client['Type of vehicle']]['total'] +=  client_total
        if input('Do you want to continue Y or N: ') == 'N':
            break
    print_day(types_vehicles, client_count, discount_count, per_vehicle)
    
main()
