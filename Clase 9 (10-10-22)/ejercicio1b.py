def print_welcome():
    print("*** Welcome ***")

def get_option(options):
    for key,value in options.items():
        print(f'{key}', end='')
        for key_interno, value_interno in value.items():
            print(f" - {value_interno}", end = "")
        print("")
    return input("Please enter a option: ")

def save_option(option, list, options):
    while True:
        list.append(option)
        if input('Do you want to enter another study Y or N: ') == 'N':
            break
        option = get_option(options)
    return list


def get_client_data(list):
    client = {
        "id":input("Please enter the client id: "),
        "age":input("Please enter the client age: "),
        "gender":input("Please enter the client gender M or F: "),
        "studies": list
    }
    return print(client)
    
def get_discounts(client, options, client_number):
    total = 0

    for key, value in client.items():
        if key == 'studies':
            for item in key:
                if item == options.get(client.get(item)):
                    total += options.get(client.get(item)).get("price") 

    print(total)
    discount = 0


    if client.get("gender") == "F" and int(client.get("age")) > 55:
        discount += options.get(client.get("studies")).get("price") * 0.25
    elif client.get("gender") == "M" and int(client.get("age")) > 65:
        discount += options.get(client.get("studies")).get("price") * 0.25
    
    if client_number % 2 != 0:
        discount += options.get(client.get("studies")).get("price") * 0.02

    return discount

def get_net_amount(client, discount, options):
    return options.get(client.get("study")).get("price") - discount


def print_invoice(client, options, net_amount):
    print('*** RECEIPT ***')
    print("Id card:",client.get("id"))
    print("Age:",client.get("age"))
    print("Gender:",client.get("gender"))
    print("Study:",options.get(client.get("study")).get("description"))
    client["total"] = net_amount
    print("Net Amout:",net_amount)


def main():
    studies_dict = {
        "U": {
            "description":"Ultrasonido",
            "price": 8900
        },
        "T": {
            "description":"Tomografia",
            "price": 12640
        },
        "R": {
            "description":"Resonancia",
            "price": 15600
        }
    }
    clients = []
    option_list = []
    studies_list = []
    total_discounts = 0
    total_net_amount = 0
    total_net_amountU = 0
    total_net_amountR = 0
    total_net_amountT = 0
    print_welcome()
    while True:
        option=get_option(studies_dict)
        save_option(option, option_list, studies_dict)
        client = get_client_data(option_list)
        clients.append(client)
        discount = get_discounts(client,studies_dict,len(clients))
        total_discounts += discount
        total = get_net_amount(client,discount,studies_dict)
        total_net_amount += total
        print_invoice(client, studies_dict, total)
        print(client)
        if input("Do you want to continue Y-Yes or N-No") == "N":
            break
    #print_final_day(clients)

main()