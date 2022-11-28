def print_products(dictionary):
    print('')
    for key, value in dictionary.items():
        print(key, end='')
        for k, v in value.items():
            print(f' - {v}', end='')
        print('')
    print('')

def is_primo(last_number_rif):
    if last_number_rif != '1' and last_number_rif != '0':
        for n in range(2, int(last_number_rif)-1):
            if int(last_number_rif) % n == 0:
                return False
    else:
        return False

def print_receipt(client,total_client,discount,iva, products):
    print('\n****** RECEIPT ******\n')
    for key, value in client.items():
        if key != 'Product ID':
            print(f'{key}: {value}')
        else:
            print('Product Line:', products[value]['name'])
            
    print(f'Discount: {discount}')
    print(f'Taxes: {iva}')
    print(f'TOTAL: {total_client}')
    print('')


def print_end_day(max_rif, total_discount, total_net_amount, client_count, products):
    print('\n****** END OF THE DAY ******\n')
    print('Number of Clients per Product:')
    for key, value in client_count.items():
        print('-', products[key]['name'], f': {value}')
    print(f'Total Discounts: {total_discount}')
    print(f'Client with the Highest Purchase: {max_rif}')
    print(f'Total Net Amount: {total_net_amount}')
    print('')



def main():
    products = {
        'Q':{
            'name':'Quimicos',
            'price': 1000
        },
        'F':{
            'name':'Farmaceuticos',
            'price': 2500
        },
        'B':{
            'name': 'Biologicos',
            'price': 4000
        }
    }
    client_count = {'Q':0, 'F':0, 'B':0}
    max_purchase = 0
    max_rif = ''
    total_discount = 0
    total_net_amount = 0
    while True:
        client = {}
        discount = 0
        price = 0
        iva = 0
        total_client = 0
        recharge = 0
        client['Rif'] = input('Please enter your RIF: ')
        print_products(products)
        client['Product ID'] = input('Please enter the product ID: ')
        print('\nPayment Methods:\nC - Contado\nR - Credito\n')
        client['Payment Method'] = input('Please enter your Payment Method: ')
        price = products.get(client.get('Product ID')).get('price')
        rif = client.get('Rif')
        if client['Payment Method'].upper() == 'C':
            discount += price * 0.03
        elif client['Payment Method'].upper() == 'R':
            recharge = price * 0.10
        if total_client%2 == 0:
            discount += price *0.02
        if is_primo(rif[-1]) != False:
            discount += price *0.05
        iva = price * 0.12
        total_client = price - discount - iva + recharge
        print_receipt(client,total_client,discount,iva, products)
        if price > max_purchase:
            max_purchase = price
            max_rif = rif
        client_count[client['Product ID']] += 1
        total_discount += discount
        total_net_amount += total_client
        if input('Do you want to continue Y or N: ') == 'N':
            break
    print_end_day(max_rif, total_discount, total_net_amount, client_count, products)
        
main()