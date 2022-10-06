pathologies = {
    "Respiratory system": [
        {
            "id": 1,
            "name": "Cystic Fibrosis",
            "price": 300     
        },
        {
            "id": 2,
            "name": "Emphysema",
            "price": 500
        },
        {
            "id": 3,
            "name": "Tuberculosis",
            "price": 450
        }
    ],
    "Nervous system": [
        {
            "id": 4,
            "name": "Parkinson",
            "price": 800     
        },
        {
            "id": 5,
            "name": "Epilepsy",
            "price": 600
        }
    ],
    "Endocrine system": [
        {
            "id": 6,
            "name": "Diabetes",
            "price": 350     
        },
        {
            "id": 7,
            "name": "Acromegaly",
            "price": 700
        },
        {
            "id": 8,
            "name": "Hashimoto’s thyroiditis",
            "price": 900
        }
    ],   
}

data_keys = ['Name', 'Lastname', 'ID']
patient = {}
patients_db = []
option = ''
check = False

while option != '3':
    option = input('\nPlease enter an option:\n1. Register and charge patient\n2. Show patient database\n3. Exit\n-> ')
    if option == '1':
        for key in data_keys:
            patient[key] = input(f'Please enter the {key}: ')
        for pathology, data in pathologies.items():
            print(f'{pathology}:')
            for info in data:
                id = info.get('id')
                name = info.get('name')
                price = info.get('price')
                print(f'{id} - {name} - {price} $')
        id_number = int(input('Please enter the ID of the pathology you want to register: '))
        for pathology, data in pathologies.items():
            for info in data:
                id = info.get('id')
                if id == id_number:
                    patient['Pathology'] = info
        patients_db.append(patient)
        print('\n*********RECEIPT*********')
        for key, value in patient.items():
                if key == 'Pathology':
                    print(f'{key}:', end = ' ')
                    for k, v in value.items():
                        if k == 'name':
                            print(v)
                        elif k == 'price':
                            print(f'TOTAL: {v} $')
                else:
                    print(f'{key}: {value}')
        patient = {}
        option = ''
    if option == '2':
        selected_pathology = int(input('Please enter the ID of the pathology you want to consult: '))
        for pat in patients_db:
            for key, value in pat.items():
                if key == 'Pathology':
                    for k, v in value.items():
                        if v == selected_pathology:
                            check = True
                if check == True:
                    for key, value in pat.items():
                        if key == 'Pathology':
                            print(f'{key}: ')
                            for k, v in value.items():
                                if k == 'name':
                                    print(v)
                        else:
                            print(f'{key}: {value}')
                check = False
        option = ''

#pop()
#popitem()

            
            

print('System closed. Have a good day!')