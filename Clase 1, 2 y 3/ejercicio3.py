cant_barras_nofrescas = float(input('Introduzca el número de barras no frescas que se han vendido '))
print('Una barra de pan tiene un costo original de 3.49$')
cost_barras_nofrescas = float(3.49*cant_barras_nofrescas)
descuento = float(cost_barras_nofrescas*0.6)
print(f'Por no ser fresca se hace un descuento del 60% lo que equivale a: {descuento}$')
coste_total = cost_barras_nofrescas-descuento
resultado = round(coste_total, 3)
print(f'Su coste total con descuento es de: {resultado}$')