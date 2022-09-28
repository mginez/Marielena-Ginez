#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.


data_dict = {}
list = []
exit = ' '
while exit != 'Yes':
    data_key = input('Please enter the data you want to save ')
    list.append(data_key)
    exit = input('Do you want to exit? ')
for index in list:
    data_dict[index] = input(f'Please enter your {index} ')
    print (data_dict)