def numero_factorial(numero, aux, acum):
    acum *= aux
    if acum < numero:
        return numero_factorial(numero, aux+1, acum)
    elif acum > numero:
        return None
    else: return 'Numero factorial'
print(numero_factorial(6, 1, 1))