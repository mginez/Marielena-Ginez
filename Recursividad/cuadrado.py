def numero_cuadrado(numero, aux, resultado):
    resultado = aux ** 2
    if resultado < numero:
        return numero_cuadrado(numero, aux+1, resultado)
    elif resultado > numero:
        return None
    else: return aux
print(numero_cuadrado(25, 1, 1))