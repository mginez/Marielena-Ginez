#Nombre del estudiante: Marielena Ginez
#Carnet: 20221110395
#=====================================================================================

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

while option !='3':
    option = input('\nPor favor ingrese una opcion\n1. Ver catalogo\n2. Ver el historial de reproducciones\n3. Salir\n-> ')
    if option == '1':
        for serie, temporadas in anime.items():
            print(f'{count1}. {serie}')
            count1 +=1
        count1 = 1
        serie_selec = input('\nPor favor ingresa el numero de la serie que deseas ver: ') 
        series = {'1':'Demon Slayer', '2':'Spy × Family', '3':'Attack on Titan'}
        for serie, temporadas in anime.items():
            if serie == series.get(serie_selec):
                for temporada, capitulos in temporadas.items():
                    print(temporada)
                temp_selec = input('\nIngresa la temporada que deseas ver: ')
                for temporada, capitulos in temporadas.items():
                    if temp_selec.title() == temporada:
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
                                data_capitulo['cap'] = cap
                                data_capitulo['name'] = name
                                data_capitulo['duration'] = duration
                                print(f'\nAhora estas viendo: {cap} - {name} - {duration}') 
                                historial.append(data_capitulo)
                                break
        data_capitulo = {}
                            

    if option == '2':
        print('El historial de reproducciones es...\nVisto mas recientemente:')
        for cap in historial[::-1]:
            id = cap.get('cap')
            name = cap.get('name')
            duration = cap.get('duration')
            print(f'{id} - {name} - {duration}')

print('\nGracias por ver Anima-te-ve!\n')                            
                            
        


        


