def print_receipt(client_dict, studies_dict, total):
    print('\n****** RECEIPT ******\n')
    for key, value in client_dict.items():
        if key == 'Study':
            print(f'{key}: {value}')
        else:
            print(f'{key}:', studies_dict[value]['name'])
    print(f'TOTAL: {total}')

def print_final_data(studies_dict, client_count, total_discounts, net_amount, client_average, study_averages):
    print('\n****** END OF THE DAY ******\n')
    print(f'Number of clients: {client_count}')
    print(f'Total Discounts: {total_discounts}')
    print(f'Total Net Amount: {net_amount}')
    print(f'Average Net Amount: {client_average}')
    print(f'Average Amount per Study:')
    for key, amount in study_averages.items():
        print('-', studies_dict[key]['name'], f': {amount}')
    print('')

def main():
    studies_dict = {
        'U':{
            'name':'Ultrasonido',
            'price': 8900
            },
        'T':{
            'name':'Tomografia',
            'price': 12640  
            },
        'R':{
            'name':'Resonancia',
            'price': 15600
        }
        }
    key_list = ['Study', 'ID', 'Age', 'Gender (M or F)']
    client_dict = {}
    client_count = 0
    net_amount = 0
    total_discounts = 0
    client_average = 0
    study_averages = {}
    study_count = {
        'U':{
            'clients':0,
            'total':0
        },
        'R':{
            'clients':0,
            'total':0
        },
        'T':{
            'clients':0,
            'total':0
        }
    }
    while True:
        discount = 0
        total = 0
        client_count += 1
        print('')
        for key, value in studies_dict.items():
            print(f'{key}', end = '')
            for k, v in value.items():
                print(f' - {v}', end='')
            print('')
        print('')
        for key in key_list:
            client_dict[key] = input(f'Please enter the {key}: ')
        total = studies_dict.get(client_dict.get('Study')).get('price')
        if client_dict['Gender (M or F)'] == 'F' and int(client_dict['Age']) > 55:
            discount += total * 0.25
        elif client_dict['Gender (M or F)'] == 'M' and int(client_dict['Age']) > 65:
            discount += total * 0.25
        if client_count %2 != 0:
            discount += total * 0.02
        total -= discount
        print_receipt(client_dict, studies_dict, total)
        net_amount += total
        total_discounts += discount
        study_count[client_dict.get('Study')]['clients'] += 1
        study_count[client_dict.get('Study')]['total'] += total
        client_average = net_amount/client_count
        for item, value in study_count.items():
            try:
                study_averages[item] = study_count[item]['total']/study_count[item]['clients']
            except:
                study_averages[item] = 0
        if input('Do you want to continue (Y or N): ').upper() == 'N':
            break
    print_final_data(studies_dict, client_count, total_discounts, net_amount, client_average, study_averages)


main()