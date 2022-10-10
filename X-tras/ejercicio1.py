#Ejercicio quiz mejorado

anime = {
    "Demon Slayer": {
        "Temporada 1": [
        {
            "cap": 1,
            "name": "Crueldad",
            "duration": "23:39"
        },
        {
            "cap": 4,
            "name": "Selección final",
            "duration": "23:40"
        },
        {
            "cap": 19,
            "name": "Dios del fuego",
            "duration": "23:40"
        },
        {
            "cap": 26,
            "name": "Una nueva misión",
            "duration": "24:10"
        }
    ],
        "Temporada 2": [
        {
            "cap": 26,
            "name": "Un sueño profundo",
            "duration": "22:55"
        },
        {
            "cap": 43,
            "name": "¡No me rendiré!",
            "duration": "23:40"
        }
    ]
 
        },
    "Spy × Family": {
       
        "Temporada 1":[
        {
            "cap": 4,
            "name": "Objetivo: pasar la entrevista",
            "duration": "24:10"
        },
        {
            "cap": 7,
            "name": "El segundo hijo del objetivo",
            "duration": "24:10"
        }
    ]
    },
    "Attack on Titan": {
        "Temporada 3": [
            {
                "cap": 46,
                "name": "La reina de la muralla",
                "duration": "23:55"
            },
            {
                "cap": 54,
                "name": "Héroe",
                "duration": "23:55"
            }
    ],
        "Temporada 4":[
            {
                "cap": 60,
                "name": "Al otro lado del mar",
                "duration": "23:55"
            },
            {
                "cap": 72,
                "name": "Los hijos del bosque",
                "duration": "23:55"
            }
        ]
        }
}

option = ''
data_capitulo = {}
historial = []
count1 = 1
count2 = 0
option_validation = []
anime_name = ''

while option !='3':
    option = input('\nPor favor ingrese una opcion\n1. Ver catalogo\n2. Ver el historial de reproducciones\n3. Salir\n-> ')
    if option == '1':
        print('\n')
        for serie, temporadas in anime.items():
            print(f'{count1}. {serie}')
            count1 +=1
        count1 = 1
        serie_selec = input('\nPor favor ingresa el numero de la serie que deseas ver: ')
        print('\n') 
        series = {'1':'Demon Slayer', '2':'Spy × Family', '3':'Attack on Titan'}
        for serie, temporadas in anime.items():
            if serie == series.get(serie_selec):
                option_validation.append(True)
                for temporada, capitulos in temporadas.items():
                    print(temporada)
                temp_selec = input('\nIngresa el numero de la temporada que deseas ver: ')
                print('\n')
                for temporada, capitulos in temporadas.items():
                    if temporada[10] == temp_selec:
                        option_validation.append(True)
                        for capitulo in capitulos:
                            cap = capitulo.get('cap')
                            name = capitulo.get('name')
                            duration = capitulo.get('duration')
                            print(f'{cap} - {name} - {duration}')
                        num_capitulo = int(input(('\nIngresa el numero del capitulo: ')))
                        for capitulo in capitulos:
                            cap = capitulo.get('cap')
                            name = capitulo.get('name')
                            duration = capitulo.get('duration')
                            if num_capitulo == cap:
                                option_validation.append(True)
                                data_capitulo['serie'] = serie
                                data_capitulo['cap'] = cap
                                data_capitulo['name'] = name
                                data_capitulo['duration'] = duration
                                print(f'\nAhora estas viendo... {serie}: {cap} - {name} - {duration}') 
                                historial.append(data_capitulo)
                                break
                        break
                break
        
        if len(option_validation) < 3:
            print('\nError 404: Option not found')
                
        data_capitulo = {}
        option_validation = []
                            

    elif option == '2':
        print('\nEl historial de reproducciones es...\n\nVisto mas recientemente:')
        for vistos in historial[::-1]:
            count2 += 1 
            anime_name = vistos.get('serie')
            cap = vistos.get('cap')
            name = vistos.get('name')
            duration = vistos.get('duration')
            print(f'{anime_name}: {cap} - {name} - {duration}')
        print(f'\nCapitulos vistos: {count2}')

    elif option != '3':
        print('\nError 404: Option not found')

print('\nGracias por ver Anima-te-ve!\n')
count2 = 0