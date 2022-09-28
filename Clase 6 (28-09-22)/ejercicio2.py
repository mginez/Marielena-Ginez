#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

data_dict = {}
list = ['Name', 'Age', 'Gender', 'Phone Number', 'E-mail']
for index in list:
    data_dict[index] = input(f'Please enter your {index} ')
    print (data_dict)