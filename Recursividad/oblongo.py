def numero_oblongo(numero, aux, resultado):
    resultado = aux * (aux+1)
    if resultado < numero:
        return numero_oblongo(numero, aux+1, resultado)
    elif resultado > numero:
        return None
    else: return 'Numero oblongo'
print(numero_oblongo(6, 1, 1))