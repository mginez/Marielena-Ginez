#Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras 
# en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. 
# El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase 
# en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en 
# el diccionario debe dejarla sin traducir.

dictionary = {}
translations = input('Please enter the dictionary ')
translations_list = translations.split(', ')
for translations in translations_list:
    list_of_values = translations.split(':')
    key = list_of_values[0]
    value = list_of_values[1]
    dictionary[key] = value
print(dictionary)
