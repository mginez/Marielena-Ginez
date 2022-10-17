def print_studies(dictionary):
    print('')
    for key, value in dictionary.items():
        print(key, end = '')
        for k, v in value.items():
            print(f' - {v}', end = '')
        print('')

def get_client_data(list, dictionary):
    print('')
    for key in list:
        dictionary[key] = input(f'Please enter your {key}: ')
    return dictionary

def get_discount(studies_dictionary, client_dictionary, client_number):
    total = 0
    discount = 0
    for key, value in studies_dictionary.items():
        if key == client_dictionary.get('Study').upper():
            total += studies_dictionary[key]['price']
    if client_dictionary.get('Gender (M or F)').upper() == 'F' and int(client_dictionary.get('Age')) > 55:
        discount += total * 0.25
    elif client_dictionary.get('Gender (M or F)').upper() == 'F' and int(client_dictionary.get('Age')) > 65:
        discount += total * 0.25
    if client_number %2 != 0:
        discount += total * 0.02
    total -= discount
    return total, discount

def print_receipt(client_dictionary, total):
    print('\n***** RECEIPT ******\n')
    for key, value in client_dictionary.items():
        if value != 'U' and value != 'R' and value != 'T':
            print(f'{key}: {value}')
        elif value == 'U':
            print(f'{key}: Ultrasonido')
        elif value == 'T':
            print(f'{key}: Tomografia')
        elif value == 'R':
            print(f'{key}: Radiografia')
    print(f'TOTAL: {total}')

def get_study_totals(study_count_dictionary, client_dictionary, total):
    study_count_dictionary[client_dictionary['Study']]['Clients'] += 1
    study_count_dictionary[client_dictionary['Study']]['Total'] += total
    return study_count_dictionary


def get_total_amounts(total, total_net_amount, discount, total_discount):
    total_net_amount += total
    total_discount += discount
    return total_net_amount, total_discount

def get_averages(client_average, total_net_amount, client_number, study_count_dictionary, study_average):
    client_average = total_net_amount/client_number
    for key, value in study_count_dictionary.items():
        try:
            study_average[key] = study_count_dictionary[key]['Total']/study_count_dictionary[key]['Clients']
        except:
            study_average[key] = 0
    return client_average, study_average

def print_final_data(client_number, total_net_amount, total_discount, client_average, study_average):
    print('\n***** END OF THE DAY DATA ******\n')
    print(f'Total Clients: {client_number}')
    print(f'Total Net Amount: {total_net_amount}')
    print(f'Total Discounts: {total_discount}')
    print(f'Average Net Amount: {client_average}')
    print(f'Average Net Amount per Study:')
    for key, value in study_average.items():
        print(f'- {key}: {value}')
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
    client_study_count = {
        'U':{
            'Clients': 0,
            'Total': 0
            }, 
        'T':{
            'Clients': 0,
            'Total': 0  
            },
        'R':{
            'Clients': 0,
            'Total': 0
        }
        }
    total_discount = 0
    total_net_amount = 0
    client_average = 0
    study_average = {}
    while True:
        client_count += 1
        print_studies(studies_dict)
        client_dict = get_client_data(key_list, client_dict)
        total, discount = get_discount(studies_dict, client_dict, client_count)
        print_receipt(client_dict, total)
        get_study_totals(client_study_count, client_dict, total)
        client_study_count = get_study_totals(client_study_count, client_dict, total)
        total_net_amount, total_discount = get_total_amounts(total, total_net_amount, discount, total_discount)
        client_average, study_average = get_averages(client_average, total_net_amount, client_count, client_study_count, study_average)
        if input('\nDo you want to continue (Y or N): ') == 'N':
            break
    print_final_data(client_count, total_net_amount, total_discount, client_average, study_average)

main()