#Manejo de api's

import requests

url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json'
r = requests.get(url)
edd = r.json()

print(edd[0])

#innertools

#TXT

import json

file_name = 'edd.json'

with open(file_name, 'r', encoding = 'utf-8') as f:
    my_data = f.read() 

my_data = f.read()

my = json.loads(my_data)

