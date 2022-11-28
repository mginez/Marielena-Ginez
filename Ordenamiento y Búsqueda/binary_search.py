def busqueda_binaria(lista, numero):
    inicio = 0
    final = len(lista) - 1
    medio = (inicio + final) // 2

    if len(lista) == 1:
        if lista[0] == numero:
            return numero
        else:
            return None

    if numero > lista[medio]:
        return busqueda_binaria(lista[medio+1:], numero)
    elif numero < lista[medio]:
        return busqueda_binaria(lista[inicio:medio], numero)
    else:
        return lista[medio]

print(busqueda_binaria([1,2,3,4,5,6,7,8,9], 1))