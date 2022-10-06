products = {
    "mobiles": {
        "Apple": [
            {
                "id": 1,
                "name": "iPhone 7",
                "price": 300
            },
            {
                "id": 2,
                "name": "iPhone 8",
                "price": 350
            },
            {
                "id": 3,
                "name": "iPhone Xr",
                "price": 450
            },
            {
                "id": 4,
                "name": "iPhone Xs",
                "price": 460
            },
            {
                "id": 5,
                "name": "iPhone 11",
                "price": 900
            },
            {
                "id": 6,
                "name": "iPhone 12",
                "price": 1100
            },
            {
                "id": 7,
                "name": "iPhone 13",
                "price": 1300
            },
        ],
        "Samsung": [
            {
                "id": 8,
                "name": "Samsung Galaxy Beam",
                "price": 150
            },
            {
                "id": 9,
                "name": "Samsung Galaxy S6",
                "price": 200
            },
            {
                "id": 10,
                "name": "Samsung Galaxy S7",
                "price": 300
            },
        ],
        "Xiaomi": [
            {
                "id": 11,
                "name": "Xiaomi Redmi Note 8",
                "price": 250
            },
            {
                "id": 12,
                "name": "Xiaomi Redmi Note 8 Pro",
                "price": 300
            },
        ]
    },
    "laptops": {
        "DELL": [
            {
                "id": 13,
                "name": "Dell Inspiron 15",
                "price": 600
            },
            {
                "id": 14,
                "name": "Dell Latitude 14",
                "price": 650
            },
        ],
        "MAC": [
            {
                "id": 15,
                "name": "MacBook Pro 13",
                "price": 900
            },
            {
                "id": 16,
                "name": "MacBook M1",
                "price": 1500
            },
        ]
    },
}
option = ''
category1 = ''
selected_product = {}
shopping_cart = []
data_keys = ['Name', 'ID']
data = {}
client_data = []
checkout =  ''
total = 0

while option != '3':

    option = input('\nPlease enter an option:\n 1. Show inventory \n 2. Register order\n 3. Exit\n -> ')
    
    if option == '1':
        categories = {'1':"mobiles", '2':"laptops"}
        category1 = input('Please enter a category:\n 1. Mobiles\n 2. Laptops\n -> ')
        for type, brands in products.items():
            if type == categories.get(category1):
                for brand, product_list in brands.items():
                    print(brand, ':')
                    for product in product_list:
                        id = product.get('id')
                        name1 = product.get('name')
                        price = product.get('price')
                        print(f'{id} - {name1} - {price}')
    elif option == '2':

        for key in data_keys:
            data[key] = input(f'Please enter you {key}: ')
        client_data.append(data)

        while checkout != '1':
            id_number = int(input('Please enter the ID of the product you want to buy: '))
            for type, brands in products.items():
                    for brand, product_list in brands.items():
                        for product in product_list:
                            if id_number == product.get('id'):
                                name1 = product.get('name')
                                price = product.get('price')
                                selected_product[name1] = price
                                shopping_cart.append(selected_product)
                                break
            selected_product = {}

            print('\nShopping cart:')
            for item in shopping_cart:
                for names, prices in item.items():
                    print(names, '-', prices, '$')

            checkout = input('Checkout order?\n1. Yes\n2. No\n-> ')

        print('********RECEIPT********')

        for client1 in client_data:
            for k, v in client1.items():
                print(k, ':', v)

        for item in shopping_cart:
            for names, prices in item.items():
                print(names, '-', prices, '$')
                total += int(prices)
        
        print(f'TOTAL: {total} $')
        
        
        



        
