#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está 
# en el diccionario.

currency_dic = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
currency = input('Please enter a currency: ')
print(currency_dic.get(currency.title(), 'Currency not found'))